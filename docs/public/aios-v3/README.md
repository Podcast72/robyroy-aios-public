# AIOS V3 Public Documentation

**P2.7 / R2.7 Core FROZEN and AGENT-READY · P3 native multi-agent ACCEPTED · EA-0A and EA-0B external-host milestones ACCEPTED in declared scopes.** P0 and P1 completed in declared scopes, P2.0–P2.7 were accepted in declared scopes, and R2.7 closeout completed.

> **Models/agents propose. AIOS governs. AIOS executes admitted actions. AIOS verifies the observed effect.**

V3 evolves the governed execution backbone documented for AIOS V2 into a governed agent runtime. The `AgentLoop` can request model or tool work, but it does not own execution authority. P1 extends that governed path to scoped real execution, including validated governed READ, bounded governed WRITE, and durable SQLite WRITE capabilities.

## Current Status

- V3 P0 governed agent-runtime foundation completed in its declared scope
- P1 governed real execution completed in its declared scope
- P2.0–P2.7 accepted in their declared scopes; R2.7 remediation and closeout completed
- P2.7 / R2.7 frozen; governed Core agent-ready
- P3 native multi-agent accepted in its declared sequential scope; live pilot observed one governed effect
- EA-0A preformed proposal admission accepted with zero inference and retained AIOS authority
- EA-0B external-host boundary accepted for governed READ and approval-bound WRITE; tested macOS two-principal isolation accepted in its tested scope
- governed READ and bounded governed WRITE validated in successive milestones
- durable SQLite WRITE validated in its declared scope
- governed filesystem WRITE validated in its bounded declared scope
- one real OpenAI `gpt-5.6-sol` end-to-end pilot completed
- historical P2.7/R2.7 full private regression: **2510 passed, 1 skipped, 11350 subtests passed**
- targeted P2.7/R2.7 closeout retest: **5 passed**
- separate P3 `tests_v3` gate: **1753 passed, 1 skipped, 1209 subtests passed**
- latest EA-0B Slice 3 canonical full-repository gate: **2,888 collected, 2,887 passed, 1 skipped, 0 failed/errors, 12,407 subtests passed**
- recovery remains fail-closed; `UNKNOWN_EFFECT` blocks blind re-execution
- no unrestricted production-readiness, certification, formal-proof, or distributed exactly-once claim

The historical P2.7/R2.7 full regression preceded its documentation-only closeout. A separate P3 `tests_v3` gate reported **1753 passed, 1 skipped, 1209 subtests passed** after the native multi-agent live pilot. OpenAI is a validated model provider; OpenAI Agents SDK remains unimplemented. Hermes decision-source evidence remains experimental. The EA-0B gate is a separate, later full-repository run; these counts are not additive.

## Documents

| Document | Purpose |
| --- | --- |
| [AIOS_V3_CURRENT_EVIDENCE.md](AIOS_V3_CURRENT_EVIDENCE.md) | Canonical P0-to-EA-0B progression and separately scoped gates. |
| [AIOS_V3_EXTERNAL_HOST_EVIDENCE.md](AIOS_V3_EXTERNAL_HOST_EVIDENCE.md) | EA-0A and EA-0B Slice 1–3 aggregate external-host evidence and limits. |
| [AIOS_V3_POST_CORE_EVIDENCE.md](AIOS_V3_POST_CORE_EVIDENCE.md) | External review, P3 live pilot, Hermes A/B experiments, and limits. |
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
-> P3 — Native multi-agent ACCEPTED in its declared scope
-> EA-0A — Governed preformed proposal admission ACCEPTED
-> EA-0B — External-host governance READ/WRITE and tested OS isolation ACCEPTED in declared scope
```

P3, EA-0A, and EA-0B build above the unchanged frozen core baseline. Each milestone claim is limited to its declared scope; none establishes unrestricted deployment readiness.

## Evolution, Not Replacement

The public history remains available under [AIOS V2](../aios-v2/README.md). Its governed-backbone documentation, ANDY field tests, at-most-once evidence, and public proof artifacts remain historical evidence for the preceding milestone.

The small executable demo under [`public_mock_runtime/`](../../../public_mock_runtime/README.md) remains intentionally V2-shaped. It is not a publication or replica of the private V3 runtime.

## Disclosure Boundary

This folder publishes properties, architectural roles, limits, and aggregate evidence. It does not publish V3 source, private test fixtures, raw schemas, private authorization, approval, or trust-boundary mechanisms, detailed adversarial probes, private prompts or operator internals, local paths, credentials, raw logs or traces, private configuration, or deployment internals.

That is the repository's **bounded technical disclosure** model.
