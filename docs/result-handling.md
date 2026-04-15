# Result Handling

This repository documents result handling as a post-tool control surface.
It exists because execution governance does not end at tool invocation.
Once a tool has produced output, the system may still need to inspect, constrain, redact, or reject what becomes externally visible.

## Public position

Result handling is documented here as additive to the official runtime backbone.
Result handling does not redefine the official backbone.

The official reference path remains:

```text
request -> planner -> execution_engine -> tool_registry -> runtime_guard -> tool -> result
```

Result handling therefore sits conceptually after tool execution and before final release of the outward result.
Its presence does not move `runtime_guard` after the tool and it does not replace execution governance.

## What result handling covers in this repository

The public perimeter focuses on a narrow and credible subset:

- controlled post-tool inspection
- selective redaction of sensitive content
- blocking of outputs that should not be released as-is
- preservation of the distinction between runtime decisions and result decisions

## Why this distinction matters

A system can be strict before tool execution and still mishandle the resulting output.
Likewise, a result control surface can be useful without being misdescribed as the core execution authority.

That is why this repository keeps two claims separate:

- pre-tool runtime mediation matters
- post-tool result control also matters

Both are important.
They are not the same layer.

## Public proof area

The repository includes a curated public case in which the tool runs, the pre-tool guard allows execution, and the returned material is later redacted before external release.
That proof is intentionally narrow and public-facing.

- [`examples/result-redaction-case.json`](../examples/result-redaction-case.json)
- [`tests/test_result_handling_public.py`](../tests/test_result_handling_public.py)

