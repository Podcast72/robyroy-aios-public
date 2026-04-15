from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BACKBONE = "request -> planner -> execution_engine -> tool_registry -> runtime_guard -> tool -> result"


def load_json(name: str) -> dict:
    return json.loads((ROOT / "examples" / name).read_text(encoding="utf-8"))


class BackbonePublicTests(unittest.TestCase):
    def test_readme_contains_required_sections(self) -> None:
        text = (ROOT / "README.md").read_text(encoding="utf-8")
        required_sections = [
            "## What this repository is",
            "## What this repository is not",
            "## Official runtime backbone",
            "## Why this matters",
            "## Repository map",
            "## Current proof areas",
            "## Declared limitations",
        ]
        for section in required_sections:
            self.assertIn(section, text)

    def test_backbone_wording_is_consistent_across_core_docs(self) -> None:
        paths = [
            ROOT / "README.md",
            ROOT / "docs" / "architecture.md",
            ROOT / "docs" / "runtime-backbone.md",
            ROOT / "docs" / "runtime-guard.md",
            ROOT / "docs" / "result-handling.md",
            ROOT / "docs" / "official-vs-compat-paths.md",
            ROOT / "reference" / "glossary.md",
            ROOT / "reference" / "invariants.md",
        ]
        for path in paths:
            self.assertIn(BACKBONE, path.read_text(encoding="utf-8"), msg=str(path))

    def test_examples_keep_the_same_official_backbone(self) -> None:
        for name in [
            "allow-case.json",
            "warn-case.json",
            "block-case.json",
            "result-redaction-case.json",
        ]:
            payload = load_json(name)
            self.assertEqual(payload["backbone_path"], BACKBONE)

    def test_compat_is_not_promoted_in_public_examples(self) -> None:
        governance = load_json("governance-override-example.json")
        self.assertTrue(governance["official_backbone_unchanged"])
        self.assertFalse(governance["compat_promoted_to_official"])


if __name__ == "__main__":
    unittest.main()

