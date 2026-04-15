# Runtime Guard

Within the documented public perimeter, the `runtime_guard` is the pre-tool runtime decision layer.
Its public role is to assess execution intent before the tool runs.

The key point is positional as much as functional.
In the official path, the guard stands before the tool:

```text
request -> planner -> execution_engine -> tool_registry -> runtime_guard -> tool -> result
```

## Public decision states

### `ALLOW`

`ALLOW` means the documented request can proceed through the mediated path and the tool may execute.
In the public examples, this is used for low-risk, read-oriented, or otherwise acceptable runtime requests.

### `WARN`

`WARN` means execution is still permitted, but the request carries conditions that deserve explicit visibility.
The public meaning is not "hidden failure."
It is "proceed with declared caution."

### `BLOCK`

`BLOCK` means the tool does not execute.
This matters because a blocked request is not the same as "tool executed and the output was later discarded."
In the public reference model, `BLOCK` ends the path before tool execution.

## What is documented here

This repository documents guard behavior at the level of architectural meaning:

- a pre-tool decision exists
- the decision can be `ALLOW`, `WARN`, or `BLOCK`
- tool execution depends on that decision
- blocked cases do not silently pass into the tool

## What is not claimed here

This repository does not claim universal public coverage of every internal rule, every internal classifier, or every private runtime branch.
The public material is selective and proof-oriented.
It is meant to show how the boundary works, not to publish the entire private rule surface.

## Public references

- [`examples/allow-case.json`](../examples/allow-case.json)
- [`examples/warn-case.json`](../examples/warn-case.json)
- [`examples/block-case.json`](../examples/block-case.json)
- [`tests/test_runtime_guard_public.py`](../tests/test_runtime_guard_public.py)

