"""Exercise the offline link checker against independent miniature repositories."""
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "check_markdown_links.py"


class MarkdownLinkTests(unittest.TestCase):
    def run_checker(self, files):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for name, content in files.items():
                path = root / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content)
            return subprocess.run([sys.executable, str(SCRIPT), str(root)], capture_output=True, text=True)

    def test_valid_relative_anchor_and_encoded_space(self):
        result = self.run_checker({"README.md": "[doc](docs/A%20B.md#same-1)", "docs/A B.md": "# Same\n# Same\n"})
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("1 local links", result.stdout)

    def test_missing_file_is_reported(self):
        result = self.run_checker({"README.md": "[missing](missing.md)"})
        self.assertEqual(result.returncode, 1)
        self.assertIn("missing target", result.stdout)

    def test_missing_anchor_is_reported(self):
        result = self.run_checker({"README.md": "[doc](doc.md#absent)", "doc.md": "# Present"})
        self.assertEqual(result.returncode, 1)
        self.assertIn("missing anchor", result.stdout)

    def test_fenced_examples_and_external_links_are_ignored(self):
        result = self.run_checker({"README.md": "```md\n[example](absent.md)\n```\n[web](https://example.invalid)"})
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_image_and_reference_links_are_checked(self):
        result = self.run_checker({"README.md": "![image](missing.png)\n[guide][g]\n[g]: absent.md"})
        self.assertEqual(result.returncode, 1)
        self.assertIn("missing.png", result.stdout)
        self.assertIn("absent.md", result.stdout)

    def test_shorter_fence_inside_longer_example_does_not_end_it(self):
        result = self.run_checker({"README.md": "````md\n```md\n[example](absent.md)\n```\n````\n"})
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("0 local links", result.stdout)

    def test_heading_suffix_collision_generates_unique_anchor(self):
        result = self.run_checker({"README.md": "[doc](doc.md#foo-1-1)", "doc.md": "# Foo\n# Foo\n# Foo-1\n"})
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
