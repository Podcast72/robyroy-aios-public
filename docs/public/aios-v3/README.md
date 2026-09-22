# AIOS V3 Public Documentation

AIOS V3 has progressed from the P0 governed-runtime foundation through **P1 — Governed Real Execution**, both completed in their declared scopes. **P2.0 — initial natural-language governed interaction** is implemented and validated in its declared scope.

> **Models propose. AIOS governs. AIOS executes.**

V3 evolves the governed execution backbone documented for AIOS V2 into a governed agent runtime. The `AgentLoop` can request model or tool work, but it does not own execution authority. P1 extends that governed path to scoped real execution, including validated governed READ, bounded governed WRITE, and durable SQLite WRITE capabilities.

## Current Status

- V3 P0 governed agent-runtime foundation completed in its declared scope
- P1 governed real execution completed in its declared scope
- P2.0 initial natural-language governed interaction implemented and validated in its declared scope
- further P2 work remains in progress
- governed READ and bounded governed WRITE validated in successive milestones
- durable SQLite WRITE validated in its declared scope
- one real OpenAI `gpt-5.6-sol` end-to-end pilot completed
- focused pilot gate: **10/10 tests PASS**
- recovery remains fail-closed; `UNKNOWN_EFFECT` blocks blind re-execution
- no unrestricted production-readiness, certification, formal-proof, or distributed exactly-once claim

These are aggregate, scope-bound engineering results.

## Documents

| Document | Purpose |
| --- | --- |
| [AIOS_V3_CURRENT_EVIDENCE.md](AIOS_V3_CURRENT_EVIDENCE.md) | Current P0-to-P2.0 milestone narrative, capability evidence, and real-pilot boundary. |
| [AIOS_V3_ARCHITECTURE.md](AIOS_V3_ARCHITECTURE.md) | High-level V3 architecture, authority boundaries, and illustrative public flow. |
| [AIOS_V3_STATUS_AND_LIMITS.md](AIOS_V3_STATUS_AND_LIMITS.md) | Current status, verified scope, non-claims, and disclosure limits. |
| [AIOS_V3_P0_OVERVIEW.md](AIOS_V3_P0_OVERVIEW.md) | Historical overview of the completed P0 foundation. |
| [AIOS_V3_P0_EVIDENCE.md](AIOS_V3_P0_EVIDENCE.md) | Historical aggregate evidence for the P0 gate. |

## Progression

```text
V2 — Governed Execution Backbone
-> V3 P0 — Governed Agent Runtime
-> P1 — Governed Real Execution
-> P2.0 — Initial natural-language governed interaction
-> Further P2 work — In progress
```

P2.0 is implemented and validated in its declared scope. Further P2 work remains in progress; public evidence does not support a broader P2 completion claim.

## Evolution, Not Replacement

The public history remains available under [AIOS V2](../aios-v2/README.md). Its governed-backbone documentation, ANDY field tests, at-most-once evidence, and public proof artifacts remain historical evidence for the preceding milestone.

The small executable demo under [`public_mock_runtime/`](../../../public_mock_runtime/README.md) remains intentionally V2-shaped. It is not a publication or replica of the private V3 runtime.

## Disclosure Boundary

This folder publishes properties, architectural roles, limits, and aggregate evidence. It does not publish V3 source, private test fixtures, raw schemas, private authorization, approval, or trust-boundary mechanisms, detailed adversarial probes, private prompts or operator internals, local paths, credentials, raw logs or traces, private configuration, or deployment internals.

That is the repository's **bounded technical disclosure** model.
