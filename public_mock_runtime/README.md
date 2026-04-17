# Public Mock Runtime

`public_mock_runtime/` is a public demo and a minimal reference implementation.

It shows one backbone flow only:

`request -> planner -> execution_engine -> tool_registry -> runtime_guard -> tool -> result`

It is intentionally small, runnable, and easy to inspect.

It is not:

- the private AIOS core
- the full AIOS runtime
- a complete publication of internal modules
- a 1:1 replica of the internal system

## What It Shows

The demo keeps the mediation chain explicit in code and output.
It demonstrates one minimal read-only flow through the backbone, not the whole system.
Its `proof_tests/` directory validates the demo itself, not the repository-level backbone public test suite.

The runtime prints a readable JSON envelope with:

- `status`
- `guard_verdict`
- `matched_rules`
- `observed_path`
- `result`
- `error`

The three official examples demonstrate:

- `ALLOW` for a non-sensitive config read
- `WARN` for a simulated access to `.env`
- `BLOCK` for a destructive delete request that is stopped before tool execution

## What It Does Not Try To Do

- It does not expose or import private AIOS modules.
- It does not claim complete policy coverage.
- It does not execute real destructive operations.
- It does not collapse the flow into one opaque function.
- It is not the separate [Backbone public test](../backbone_public_test/README.md) area.

## Run It

From the repository root:

```bash
python3 public_mock_runtime/mock_runtime.py public_mock_runtime/examples/allow.json
python3 public_mock_runtime/mock_runtime.py public_mock_runtime/examples/warn.json
python3 public_mock_runtime/mock_runtime.py public_mock_runtime/examples/block.json
```

Run the tests:

```bash
python3 -m unittest discover -s public_mock_runtime/proof_tests -p 'test_*.py'
```

## Official Examples

`public_mock_runtime/examples/allow.json`

- uses `mock_reader`
- reads `public_mock_runtime/examples/data/public-config.json`
- returns `status: success` and `guard_verdict: ALLOW`

`public_mock_runtime/examples/warn.json`

- uses `mock_reader`
- targets `.env`
- returns `status: success` and `guard_verdict: WARN`
- still executes the mock tool, with a simulated redacted read

`public_mock_runtime/examples/block.json`

- uses `mock_delete`
- requests `delete_file`
- returns `status: error` and `guard_verdict: BLOCK`
- stops before the tool step

In the `BLOCK` case, the block is the expected behavior of the mock runtime. The output JSON shows that `runtime_guard` interrupts the flow before tool execution. In this scenario the CLI can terminate with a non-zero exit code, because the operational outcome is a controlled error (`blocked_by_runtime_guard`), not a success.

## Extend It

To extend the demo without changing its positioning:

- add a new public rule in `rules.json`
- add a new mock tool in `mock_runtime.py`
- add or update an example JSON request
- add a test in `proof_tests/test_mock_runtime.py`

Keep the mediation model intact and visible:

`planner -> execution_engine -> tool_registry -> runtime_guard -> tool -> result`
