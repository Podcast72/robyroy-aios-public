#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable

ROOT_DIR = Path(__file__).resolve().parent
REPO_ROOT = ROOT_DIR.parent
RULES_PATH = ROOT_DIR / "rules.json"


@dataclass
class RuntimeContext:
    observed_path: list[str] = field(default_factory=list)
    tool_executions: list[str] = field(default_factory=list)


def load_request(request_path: str | Path) -> dict[str, Any]:
    with Path(request_path).open("r", encoding="utf-8") as handle:
        return json.load(handle)


def load_rules(rules_path: Path = RULES_PATH) -> dict[str, Any]:
    with rules_path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def planner(request: dict[str, Any], context: RuntimeContext) -> dict[str, Any]:
    context.observed_path.append("planner")
    return {
        "request_id": request.get("request_id", "mock-request"),
        "intent": request["action"],
        "tool_name": request["tool"],
        "target_path": request["target_path"],
        "arguments": request.get("arguments", {}),
    }


def resolve_tool(tool_name: str, context: RuntimeContext) -> Callable[[dict[str, Any], RuntimeContext], dict[str, Any]]:
    context.observed_path.append("tool_registry")
    registry: dict[str, Callable[[dict[str, Any], RuntimeContext], dict[str, Any]]] = {
        "mock_reader": mock_reader,
        "mock_analyzer": mock_analyzer,
        "mock_delete": mock_delete,
    }
    if tool_name not in registry:
        raise KeyError(tool_name)
    return registry[tool_name]


def runtime_guard(plan: dict[str, Any], ruleset: dict[str, Any], context: RuntimeContext) -> tuple[str, list[str]]:
    context.observed_path.append("runtime_guard")
    matched_rules: list[str] = []
    verdict = ruleset.get("default_verdict", "ALLOW")
    verdict_priority = {"ALLOW": 0, "WARN": 1, "BLOCK": 2}

    for rule in ruleset.get("rules", []):
        if rule_matches(rule, plan):
            matched_rules.append(rule["id"])
            rule_verdict = rule["verdict"]
            if verdict_priority[rule_verdict] > verdict_priority[verdict]:
                verdict = rule_verdict

    return verdict, matched_rules


def rule_matches(rule: dict[str, Any], plan: dict[str, Any]) -> bool:
    target_path = str(plan.get("target_path", ""))
    intent = plan.get("intent", "")
    tool_name = plan.get("tool_name", "")
    arguments = plan.get("arguments", {})
    match = rule.get("match", {})

    if "intent_in" in match and intent not in match["intent_in"]:
        return False
    if "tool_in" in match and tool_name not in match["tool_in"]:
        return False
    if "path_exact" in match and target_path != match["path_exact"]:
        return False
    if "path_endswith" in match and not target_path.endswith(match["path_endswith"]):
        return False
    if "path_contains" in match and not any(fragment in target_path for fragment in match["path_contains"]):
        return False
    if "flag_true" in match:
        flag_name = match["flag_true"]
        if not bool(arguments.get(flag_name)):
            return False
    return True


def build_response(
    *,
    status: str,
    guard_verdict: str,
    matched_rules: list[str],
    observed_path: list[str],
    result: dict[str, Any] | None,
    error: str | None,
) -> dict[str, Any]:
    return {
        "status": status,
        "guard_verdict": guard_verdict,
        "matched_rules": matched_rules,
        "observed_path": observed_path,
        "result": result,
        "error": error,
    }


def resolve_public_path(target_path: str) -> Path:
    resolved = Path(target_path)
    if not resolved.is_absolute():
        resolved = (REPO_ROOT / resolved).resolve()
    public_root = ROOT_DIR.resolve()
    if public_root not in resolved.parents and resolved != public_root:
        raise ValueError("mock_reader_only_reads_public_mock_runtime_files")
    return resolved


def mock_reader(plan: dict[str, Any], context: RuntimeContext) -> dict[str, Any]:
    context.tool_executions.append("mock_reader")
    target_path = str(plan["target_path"])

    if target_path == ".env" or target_path.endswith("/.env"):
        return {
            "message": "Mock sensitive read simulated",
            "path": target_path,
            "content_preview": "[redacted]",
            "simulation": True,
        }

    file_path = resolve_public_path(target_path)
    content = file_path.read_text(encoding="utf-8")
    return {
        "message": "Mock read completed",
        "path": str(Path(target_path)),
        "bytes_read": len(content.encode("utf-8")),
        "content_preview": content[:120],
        "simulation": False,
    }


def mock_analyzer(plan: dict[str, Any], context: RuntimeContext) -> dict[str, Any]:
    context.tool_executions.append("mock_analyzer")
    target_path = str(plan["target_path"])

    if target_path == ".env" or target_path.endswith("/.env"):
        return {
            "message": "Mock analysis completed on simulated sensitive path",
            "path": target_path,
            "summary": {"classification": "sensitive", "analysis_mode": "simulated"},
        }

    file_path = resolve_public_path(target_path)
    content = file_path.read_text(encoding="utf-8")
    return {
        "message": "Mock analysis completed",
        "path": str(Path(target_path)),
        "summary": {
            "line_count": len(content.splitlines()),
            "char_count": len(content),
            "looks_like_json": file_path.suffix == ".json",
        },
    }


def mock_delete(plan: dict[str, Any], context: RuntimeContext) -> dict[str, Any]:
    context.tool_executions.append("mock_delete")
    return {
        "message": "Mock delete simulated only",
        "path": str(plan["target_path"]),
        "side_effects": "none",
    }


def execute_request(
    request: dict[str, Any],
    *,
    ruleset: dict[str, Any] | None = None,
    context: RuntimeContext | None = None,
) -> tuple[dict[str, Any], RuntimeContext]:
    runtime_context = context or RuntimeContext()
    active_rules = ruleset or load_rules()
    plan = planner(request, runtime_context)
    runtime_context.observed_path.append("execution_engine")

    try:
        tool = resolve_tool(plan["tool_name"], runtime_context)
    except KeyError:
        runtime_context.observed_path.append("result")
        return (
            build_response(
                status="error",
                guard_verdict="BLOCK",
                matched_rules=["unknown_tool_request"],
                observed_path=runtime_context.observed_path,
                result=None,
                error="unknown_tool",
            ),
            runtime_context,
        )

    guard_verdict, matched_rules = runtime_guard(plan, active_rules, runtime_context)
    if guard_verdict == "BLOCK":
        runtime_context.observed_path.append("result")
        return (
            build_response(
                status="error",
                guard_verdict=guard_verdict,
                matched_rules=matched_rules,
                observed_path=runtime_context.observed_path,
                result=None,
                error="blocked_by_runtime_guard",
            ),
            runtime_context,
        )

    runtime_context.observed_path.append("tool")
    try:
        result = tool(plan, runtime_context)
        runtime_context.observed_path.append("result")
        return (
            build_response(
                status="success",
                guard_verdict=guard_verdict,
                matched_rules=matched_rules,
                observed_path=runtime_context.observed_path,
                result=result,
                error=None,
            ),
            runtime_context,
        )
    except Exception as exc:  # pragma: no cover - defensive fallback
        runtime_context.observed_path.append("result")
        return (
            build_response(
                status="error",
                guard_verdict=guard_verdict,
                matched_rules=matched_rules,
                observed_path=runtime_context.observed_path,
                result=None,
                error=str(exc),
            ),
            runtime_context,
        )


def main(argv: list[str] | None = None) -> int:
    args = argv or sys.argv[1:]
    if len(args) != 1:
        print(
            json.dumps(
                {
                    "status": "error",
                    "guard_verdict": "BLOCK",
                    "matched_rules": [],
                    "observed_path": [],
                    "result": None,
                    "error": "usage: python3 public_mock_runtime/mock_runtime.py <request.json>",
                },
                indent=2,
                ensure_ascii=False,
            )
        )
        return 1

    request = load_request(args[0])
    response, _ = execute_request(request)
    print(json.dumps(response, indent=2, ensure_ascii=False))
    return 0 if response["status"] == "success" else 1


if __name__ == "__main__":
    raise SystemExit(main())
