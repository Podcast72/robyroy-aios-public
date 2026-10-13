"""Independent tests of the public V2 demonstration, using synthetic files."""
from __future__ import annotations

import contextlib
import io
import json
import tempfile
import unittest
from pathlib import Path

from public_mock_runtime import mock_runtime as runtime


class MockRuntimeSafetyTests(unittest.TestCase):
    def request(self, **updates):
        request = {"action": "read_file", "tool": "mock_reader",
                   "target_path": "public_mock_runtime/examples/data/public-config.json"}
        request.update(updates)
        return request

    def test_absolute_parent_escape_is_rejected(self):
        path = runtime.ROOT_DIR / ".." / "README.md"
        with self.assertRaises(ValueError):
            runtime.resolve_public_path(str(path))

    def test_absolute_symlink_escape_is_rejected(self):
        with tempfile.TemporaryDirectory() as outside, tempfile.TemporaryDirectory(dir=runtime.ROOT_DIR) as inside:
            target = Path(outside) / "synthetic.txt"
            target.write_text("synthetic outside content")
            link = Path(inside) / "link.txt"
            link.symlink_to(target)
            with self.assertRaises(ValueError):
                runtime.resolve_public_path(str(link))

    def test_invalid_request_never_reaches_tool(self):
        for request in (None, [], {}, self.request(action=3), self.request(tool=""),
                        self.request(target_path=3), self.request(arguments=[])):
            with self.subTest(request=request):
                response, context = runtime.execute_request(request)
                self.assertEqual(response["error"], "invalid_request")
                self.assertEqual(response["guard_verdict"], "BLOCK")
                self.assertIsNone(response["result"])
                self.assertEqual(context.tool_executions, [])

    def test_empty_explicit_rules_do_not_fall_back_to_defaults(self):
        response, context = runtime.execute_request(self.request(), ruleset={})
        self.assertEqual(response["error"], "invalid_rules")
        self.assertEqual(context.tool_executions, [])

    def test_invalid_rules_never_reach_tool(self):
        invalid = [[], {"default_verdict": "PERMIT", "rules": []},
                   {"default_verdict": "ALLOW", "rules": "invalid"},
                   {"default_verdict": "ALLOW", "rules": [{"id": "demo", "verdict": "ALLOW", "match": {"typo": True}}]},
                   {"default_verdict": "ALLOW", "rules": [{"id": "demo", "verdict": "ALLOW", "match": {"intent_in": "read_file"}}]}]
        for rules in invalid:
            with self.subTest(rules=rules):
                response, context = runtime.execute_request(self.request(), ruleset=rules)
                self.assertEqual(response["error"], "invalid_rules")
                self.assertEqual(context.tool_executions, [])

    def test_tool_error_does_not_echo_file_path(self):
        response, _ = runtime.execute_request(self.request(target_path="public_mock_runtime/missing-synthetic-file.txt"))
        self.assertEqual(response["error"], "tool_failed")
        self.assertIsNone(response["result"])

    def test_cli_malformed_json_returns_error_envelope(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "bad.json"
            path.write_text("{")
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                code = runtime.main([str(path)])
            self.assertEqual(code, 1)
            self.assertEqual(json.loads(output.getvalue())["error"], "invalid_request_file")

    def test_cli_empty_arguments_do_not_consume_process_arguments(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            code = runtime.main([])
        self.assertEqual(code, 1)
        self.assertEqual(json.loads(output.getvalue())["guard_verdict"], "BLOCK")
