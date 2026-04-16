from __future__ import annotations

import json
import subprocess
import unittest
from pathlib import Path

from public_mock_runtime import mock_runtime

RUNTIME_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = RUNTIME_ROOT.parent


class MockRuntimeTests(unittest.TestCase):
    def _load_example(self, name: str) -> dict[str, object]:
        example_path = RUNTIME_ROOT / "examples" / f"{name}.json"
        return json.loads(example_path.read_text(encoding="utf-8"))

    def _run_example(self, name: str) -> tuple[dict[str, object], mock_runtime.RuntimeContext]:
        request = self._load_example(name)
        return mock_runtime.execute_request(request)

    def test_allow_path_returns_success(self) -> None:
        response, _ = self._run_example("allow")
        self.assertEqual(response["status"], "success")
        self.assertEqual(response["guard_verdict"], "ALLOW")

    def test_warn_path_returns_success_with_warn_verdict(self) -> None:
        response, _ = self._run_example("warn")
        self.assertEqual(response["status"], "success")
        self.assertEqual(response["guard_verdict"], "WARN")

    def test_warn_path_still_executes_the_tool(self) -> None:
        response, context = self._run_example("warn")
        self.assertEqual(response["status"], "success")
        self.assertEqual(context.tool_executions, ["mock_reader"])

    def test_block_path_returns_error(self) -> None:
        response, _ = self._run_example("block")
        self.assertEqual(response["status"], "error")
        self.assertEqual(response["guard_verdict"], "BLOCK")
        self.assertEqual(response["error"], "blocked_by_runtime_guard")

    def test_block_path_never_executes_the_tool(self) -> None:
        _, context = self._run_example("block")
        self.assertEqual(context.tool_executions, [])

    def test_observed_path_for_allow_includes_tool(self) -> None:
        response, _ = self._run_example("allow")
        self.assertIn("tool", response["observed_path"])

    def test_observed_path_for_block_does_not_include_tool(self) -> None:
        response, _ = self._run_example("block")
        self.assertNotIn("tool", response["observed_path"])

    def test_matched_rules_are_reported_correctly(self) -> None:
        warn_response, _ = self._run_example("warn")
        block_response, _ = self._run_example("block")
        self.assertEqual(warn_response["matched_rules"], ["sensitive_env_path_access"])
        self.assertEqual(block_response["matched_rules"], ["destructive_data_erasure_request"])

    def test_output_json_shape_remains_stable(self) -> None:
        expected_keys = {
            "status",
            "guard_verdict",
            "matched_rules",
            "observed_path",
            "result",
            "error",
        }
        for example_name in ("allow", "warn", "block"):
            response, _ = self._run_example(example_name)
            self.assertEqual(set(response.keys()), expected_keys)

    def test_readme_examples_are_consistent_with_actual_command_behavior(self) -> None:
        readme_path = RUNTIME_ROOT / "README.md"
        readme = readme_path.read_text(encoding="utf-8")
        commands = {
            "allow": "ALLOW",
            "warn": "WARN",
            "block": "BLOCK",
        }
        for example_name, verdict in commands.items():
            command_text = (
                f"python3 public_mock_runtime/mock_runtime.py "
                f"public_mock_runtime/examples/{example_name}.json"
            )
            self.assertIn(command_text, readme)
            completed = subprocess.run(
                [
                    "python3",
                    "public_mock_runtime/mock_runtime.py",
                    f"public_mock_runtime/examples/{example_name}.json",
                ],
                cwd=REPO_ROOT,
                capture_output=True,
                text=True,
                check=False,
            )
            output = json.loads(completed.stdout)
            self.assertEqual(output["guard_verdict"], verdict)
            if example_name == "block":
                self.assertNotEqual(completed.returncode, 0)
            else:
                self.assertEqual(completed.returncode, 0)


if __name__ == "__main__":
    unittest.main()
