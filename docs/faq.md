# FAQ

## Is this the full RobyRoy AIOS codebase?

No.
This is a curated public technical repository.
It documents architecture, governance model, and public technical proofs without exposing the full private operational codebase.

## What is the official runtime path?

The public reference path is:

```text
request -> planner -> execution_engine -> tool_registry -> runtime_guard -> tool -> result
```

## Is governance the same as runtime execution?

No.
Governance records and approves decisions, but governance is documented separately from runtime execution.
A governance approval does not silently become runtime application.

## Are compat paths part of the official backbone?

No.
Compat or legacy surfaces may exist in a broader system context, but this repository does not present them as the official backbone.

## Does public evidence mean the whole system is public?

No.
The public evidence is selective and proof-oriented.
It is meant to explain and support specific architectural claims.

## Why are some tests adapted for public release?

Because public tests need to stand on their own.
An adapted public test preserves the architectural meaning of a real invariant without depending on private modules, private data, or non-public runtime material.

