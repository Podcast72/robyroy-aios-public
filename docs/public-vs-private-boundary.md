# Public vs Private Boundary

This repository follows **bounded technical disclosure**.

It publishes enough architecture, properties, evidence, and limitations to support technical review without publishing the mechanisms required to reproduce the private AIOS V3 runtime.

## Public Evolution

The public narrative is versioned:

```text
AIOS V2 — Governed Execution Backbone
-> AIOS V3 P0 — Governed Agent Runtime
-> P1 — Governed Real Execution
-> P2.0 — Initial natural-language governed interaction
-> Further P2 work — In progress
```

V2 remains public historical evidence. Its documentation, public mock runtime, proof tests, ANDY field tests, and public-safe validation summaries are not erased or presented as if they were V3.

V3 is documented through architecture-level descriptions, claim limits, and aggregate evidence only. P2.0 is implemented and validated in its declared scope. Further P2 work remains in progress; current public evidence does not support broad phase completion.

## What Is Public For V3

The public V3 surface includes:

- the principle **Models propose. AIOS governs. AIOS executes.**;
- the high-level `User -> AgentLoop -> governed execution -> final answer` flow;
- `AgentLoop`, `ModelPort`, `ExecutionEngine`, `RunStore`, and `ResultGate` as architectural roles;
- separation of conversation/session state from execution truth;
- fail-closed retry/recovery and `UNKNOWN_EFFECT` posture;
- the completed P0 and P1 milestone statements in their declared scopes, and P2.0 implemented and validated in its declared scope;
- aggregate validation of governed READ, bounded governed WRITE, and durable SQLite WRITE;
- the fact that explicit approval was observed where required in the bounded pilot;
- the aggregate result of one OpenAI `gpt-5.6-sol` end-to-end pilot and its focused **10/10 PASS** gate;
- explicit scope limits and non-claims.

Named boundaries in the pilot describe aggregate passage through the runtime. They do not publish schemas, interfaces, action formats, or implementation relationships.

## What Remains Private

Do not publish:

- V3 source code;
- implementation-sensitive details or private class structure;
- private test source or fixtures;
- raw `RunStore`, conversation/checkpoint-state, context, or trace schemas;
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

These artifacts demonstrate the V2 governed-backbone model. They are not the publication of the private V3 runtime, and the mock must remain V2-shaped.

## Aggregate Evidence Rule

Public V3 evidence must remain aggregate and conservatively worded.

Allowed examples include:

- a named milestone completed in its declared scope;
- a scoped test result already authorized for public use;
- a capability verified in a named or described bounded scope;
- a sanitized one-shot provider or end-to-end outcome;
- a high-level list of governed boundaries traversed without raw records or implementation detail.

A public claim must not imply:

- access to or publication of raw private evidence;
- a security certification;
- production readiness;
- formal proof;
- universal provider, capability, or deployment support;
- arbitrary READ or WRITE access;
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
