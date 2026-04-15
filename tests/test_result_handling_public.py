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


class ResultHandlingPublicTests(unittest.TestCase):
    def test_result_redaction_is_additive_to_the_backbone(self) -> None:
        payload = load_json("result-redaction-case.json")
        self.assertEqual(payload["runtime_guard"]["verdict"], "ALLOW")
        self.assertTrue(payload["tool"]["executed"])
        self.assertEqual(payload["result_handling"]["status"], "REDACTED")
        self.assertFalse(payload["result_handling"]["replaces_backbone"])
        assert_order(
            self,
            payload["trace"],
            ["runtime_guard_allow", "tool_executed", "result_handling_redacted", "result_emitted"],
        )

    def test_governance_override_has_no_automatic_runtime_effect(self) -> None:
        payload = load_json("governance-override-example.json")
        decision = payload["governance_decision"]
        self.assertEqual(decision["status"], "approved")
        self.assertEqual(decision["approval_scope"], "governance_only")
        self.assertEqual(decision["runtime_effect"], "none")
        self.assertFalse(decision["override_applied"])
        self.assertEqual(decision["runtime_application_status"], "not_applied")
        self.assertTrue(payload["official_backbone_unchanged"])

    def test_docs_keep_result_handling_and_governance_separate(self) -> None:
        result_doc = (ROOT / "docs" / "result-handling.md").read_text(encoding="utf-8")
        governance_doc = (ROOT / "docs" / "governance-layer.md").read_text(encoding="utf-8")
        self.assertIn("Result handling does not redefine the official backbone.", result_doc)
        self.assertIn("A governance approval does not silently become runtime application.", governance_doc)


if __name__ == "__main__":
    unittest.main()
