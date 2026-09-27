# AIOS V3 Public Documentation

**P2.7 / R2.7 — FROZEN · Governed Core — AGENT-READY.** P0 and P1 completed in declared scopes, P2.0–P2.7 were accepted in declared scopes, and R2.7 closeout completed.

> **Models propose. AIOS governs. AIOS executes.**

V3 evolves the governed execution backbone documented for AIOS V2 into a governed agent runtime. The `AgentLoop` can request model or tool work, but it does not own execution authority. P1 extends that governed path to scoped real execution, including validated governed READ, bounded governed WRITE, and durable SQLite WRITE capabilities.

## Current Status

- V3 P0 governed agent-runtime foundation completed in its declared scope
- P1 governed real execution completed in its declared scope
- P2.0–P2.7 accepted in their declared scopes; R2.7 remediation and closeout completed
- P2.7 / R2.7 frozen; governed Core agent-ready
- governed READ and bounded governed WRITE validated in successive milestones
- durable SQLite WRITE validated in its declared scope
- governed filesystem WRITE validated in its bounded declared scope
- one real OpenAI `gpt-5.6-sol` end-to-end pilot completed
- latest recorded full private regression: **2510 passed, 1 skipped, 11350 subtests passed**
- targeted P2.7/R2.7 closeout retest: **5 passed**
- recovery remains fail-closed; `UNKNOWN_EFFECT` blocks blind re-execution
- no unrestricted production-readiness, certification, formal-proof, or distributed exactly-once claim

The full regression preceded the final documentation-only closeout and was not rerun for documentation changes. The targeted retests covered relevant filesystem ambiguity/recovery and result-exposure properties at an aggregate level. The next phase is provider-neutral Agent Integration Architecture, with OpenAI as the first planned external agent integration; that integration is not yet implemented.

## Documents

| Document | Purpose |
| --- | --- |
| [AIOS_V3_CURRENT_EVIDENCE.md](AIOS_V3_CURRENT_EVIDENCE.md) | Canonical P0-to-P2.7 progression, aggregate validation, and claim boundaries. |
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
-> P2.1–P2.7 — Accepted in declared scopes
-> R2.7 — Closed; Core FROZEN / AGENT-READY
```

Each milestone claim is limited to its declared scope. Agent-ready is a baseline for future integration engineering, not unrestricted deployment readiness.

## Evolution, Not Replacement

The public history remains available under [AIOS V2](../aios-v2/README.md). Its governed-backbone documentation, ANDY field tests, at-most-once evidence, and public proof artifacts remain historical evidence for the preceding milestone.

The small executable demo under [`public_mock_runtime/`](../../../public_mock_runtime/README.md) remains intentionally V2-shaped. It is not a publication or replica of the private V3 runtime.

## Disclosure Boundary

This folder publishes properties, architectural roles, limits, and aggregate evidence. It does not publish V3 source, private test fixtures, raw schemas, private authorization, approval, or trust-boundary mechanisms, detailed adversarial probes, private prompts or operator internals, local paths, credentials, raw logs or traces, private configuration, or deployment internals.

That is the repository's **bounded technical disclosure** model.
