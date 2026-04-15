from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_json(name: str) -> dict:
    return json.loads((ROOT / "examples" / name).read_text(encoding="utf-8"))


def assert_order(test_case: unittest.TestCase, trace: list[str], expected: list[str]) -> None:
    positions = [trace.index(item) for item in expected]
    test_case.assertEqual(positions, sorted(positions))


class RuntimeGuardPublicTests(unittest.TestCase):
    def test_allow_case_executes_tool_after_allow(self) -> None:
        payload = load_json("allow-case.json")
        self.assertEqual(payload["runtime_guard"]["verdict"], "ALLOW")
        self.assertTrue(payload["tool"]["executed"])
        assert_order(
            self,
            payload["trace"],
            ["tool_registry_resolved", "runtime_guard_allow", "tool_executed", "result_emitted"],
        )

    def test_warn_case_preserves_mediation(self) -> None:
        payload = load_json("warn-case.json")
        self.assertEqual(payload["runtime_guard"]["verdict"], "WARN")
        self.assertTrue(payload["tool"]["executed"])
        self.assertTrue(payload["operator_attention_required"])
        assert_order(
            self,
            payload["trace"],
            ["tool_registry_resolved", "runtime_guard_warn", "tool_executed", "result_emitted"],
        )

    def test_block_case_stops_before_tool_execution(self) -> None:
        payload = load_json("block-case.json")
        self.assertEqual(payload["runtime_guard"]["verdict"], "BLOCK")
        self.assertFalse(payload["tool"]["executed"])
        self.assertNotIn("tool_executed", payload["trace"])
        assert_order(
            self,
            payload["trace"],
            ["tool_registry_resolved", "runtime_guard_block", "result_emitted"],
        )


if __name__ == "__main__":
    unittest.main()

