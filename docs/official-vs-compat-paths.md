# Official vs Compat Paths

This repository draws a strict public distinction between the official runtime backbone and other surfaces that may exist around it.
That distinction is necessary to avoid architectural ambiguity.

## Official runtime backbone

The official public reference path is:

```text
request -> planner -> execution_engine -> tool_registry -> runtime_guard -> tool -> result
```

When this repository says "official path," it refers to that sequence.

## Compat or legacy surfaces

Compat or legacy surfaces may exist in a broader operational estate, but they are not the official public backbone by default.
They are not promoted to the core path simply because they are useful, historically present, or share some components with the official runtime.

Publicly, this repository uses the term `compat path` for non-core paths that must remain distinguishable from the official backbone.

## Other support or adjacent areas

Some important areas are neither compat paths nor official backbone nodes.
Examples in this repository include:

- governance records
- audit artifacts
- result handling controls
- public technical proofs

These areas matter, but they should not be mistaken for substitutions of the core execution path.

## Why the distinction matters

If official, compat, governance, and result-control surfaces are all described as if they were the same thing, several problems appear:

- tool access boundaries become less clear
- runtime authority becomes harder to interpret
- public claims become broader than the evidence supports
- readers can no longer tell what the public proofs actually prove

## Public rule of interpretation

In this repository:

- the backbone remains explicit
- compat remains non-core
- governance remains separate from runtime application
- result handling remains additive rather than redefining the backbone

