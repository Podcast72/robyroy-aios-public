# Public vs Private Boundary

This repository follows **bounded technical disclosure**.

It publishes enough architecture, properties, evidence, and limitations to support technical review without publishing the mechanisms required to reproduce the private AIOS V3 runtime.

## Public Evolution

The public narrative is versioned:

```text
AIOS V2 — Governed Execution Backbone
->
AIOS V3 P0 — Governed Agent Runtime
```

V2 remains public historical evidence. Its documentation, public mock runtime, proof tests, ANDY field tests, and public-safe validation summaries are not erased or presented as if they were V3.

V3 is documented through architecture-level descriptions and aggregate evidence only.

## What Is Public For V3

The public V3 surface includes:

- the principle **Models propose. AIOS governs. AIOS executes.**;
- the high-level `User -> AgentLoop -> governed model/tool execution -> final answer` flow;
- the fact that `AgentLoop` does not own execution authority;
- the provider-neutral `ModelPort` boundary;
- `ExecutionEngine` as execution authority;
- separation of conversation state from execution truth;
- fail-closed retry/recovery and `UNKNOWN_EFFECT` behavior;
- governed executable/artifact identity, budget accounting, credential egress, and content provenance;
- synthetic P0 persistence/reopen/resume properties;
- Composition Root assembly as an architectural property;
- aggregate P0 gate and live-provider results;
- explicit scope limits and non-claims.

## What Remains Private

Do not publish:

- V3 source code;
- implementation-sensitive details;
- private test source or fixtures;
- raw `RunStore` schema;
- private authorization, approval, and trust-boundary mechanisms;
- detailed exploit or adversarial probes;
- private prompts;
- private operator internals;
- local paths;
- credentials or credential fragments;
- raw audit records, logs, or traces;
- private configuration;
- deployment internals.

The absence of these materials is intentional and should not be interpreted as evidence that the underlying properties do or do not exist beyond the published aggregate statements.

## Preserved V2 Public Surface

The V2 public perimeter remains intentionally inspectable:

- architecture and backbone documentation;
- the small public mock runtime;
- curated JSON examples;
- adapted public invariant tests;
- public proof artifacts;
- sanitized ANDY field-test evidence;
- bounded at-most-once evidence.

The V2 path remains:

`request -> planner -> execution_engine -> tool_registry -> runtime_guard -> tool -> result_gate -> result`

These artifacts demonstrate the V2 governed-backbone model. They are not the publication of the private V3 runtime.

## Aggregate Evidence Rule

Public V3 evidence must remain aggregate and conservatively worded.

Allowed examples include a named gate result, a scoped test count, a high-level property verified in a named scope, and a sanitized one-shot provider outcome.

A public claim must not imply:

- access to or publication of raw private evidence;
- a security certification;
- production readiness;
- universal provider or deployment support;
- distributed exactly-once guarantees;
- universal absence of secret leakage or bypasses.

## Why The Boundary Exists

The boundary keeps the public record technically honest:

- reviewers can distinguish architecture from implementation;
- historical V2 demonstrations remain reproducible;
- V3 claims stay tied to aggregate evidence and explicit limits;
- the public mock is not mistaken for the private runtime;
- sensitive mechanisms and operational artifacts remain out of the repository.

The purpose is clarity and controlled disclosure, not mystique.
