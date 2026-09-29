# AIOS V3 Status And Limits

## Current Status

**P2.7 / R2.7 — FROZEN · Governed Core — AGENT-READY · P3 native multi-agent ACCEPTED in its declared sequential scope.** V3 P0 and P1 completed in their declared scopes; P2.0–P2.7 were accepted and R2.7 closed in declared scopes. P3 was built and validated above that unchanged frozen baseline.

> **Models/agents propose. AIOS governs. AIOS executes admitted actions. AIOS verifies the observed effect.**

| Area | Public status |
| --- | --- |
| Governed agent runtime | P0 completed in its declared scope |
| Governed real execution | P1 completed in its declared scope |
| Initial governed interaction | P2.0 implemented and validated in its declared scope |
| P2 progression | P2.1–P2.7 accepted in declared scopes; R2.7 completed |
| P3 native multi-agent | Sequential Coordinator/Analyst/Challenger/Operator path accepted inside one AIOS root run |
| Governed READ | Validated in a successive real-execution milestone |
| Bounded governed WRITE | Validated with applicable authority and approval requirements |
| Durable persistence | Bounded SQLite WRITE validated in its declared scope |
| Governed filesystem WRITE | Validated in a bounded declared scope |
| Execution authority | `ExecutionEngine` remains authoritative |
| Agent loop | Coordinates work; does not own execution authority |
| State model | Conversation/session state and execution truth remain separate |
| Recovery | Fail-closed; `UNKNOWN_EFFECT` blocks blind re-execution |
| Real-provider pilot | One OpenAI `gpt-5.6-sol` governed pilot completed |
| Historical P2.7/R2.7 `tests_v2 + tests_v3` regression | **2510 passed, 1 skipped, 11350 subtests passed** |
| Targeted P2.7/R2.7 closeout | **5 passed** |
| P3 `tests_v3` gate, 29 September 2026 | **1753 passed, 1 skipped, 1209 subtests passed**, exit 0 |
| Public distribution | Documentation and minimal V2 demonstrations only; private V3 runtime not distributed |

## Current Claim Boundary

The published evidence supports engineering milestone and observed-pilot claims, not assurance claims. `PASS`, `verified`, and `completed` refer only to the named gate, capability, or tested scope.

The public material may state that:

- P0 and P1 completed in their respective declared scopes;
- P2.0–P2.7 were accepted in declared scopes and R2.7 closeout completed;
- governed READ, bounded governed WRITE, and a durable SQLite WRITE were validated in successive scopes;
- recovery remains fail-closed and uncertain effects stop at `UNKNOWN_EFFECT`;
- one `gpt-5.6-sol` end-to-end pilot read allowed state, selected one bounded WRITE, obtained explicit approval, and completed through the governed runtime;
- the historical P2.7/R2.7 `tests_v2 + tests_v3` regression reported **2510 passed, 1 skipped, 11350 subtests passed**;
- the targeted P2.7/R2.7 closeout retest reported **5 passed** for relevant filesystem ambiguity/recovery and result-exposure properties;
- P3 native sequential multi-agent was accepted with one bounded live pilot and a separate `tests_v3` gate of **1753 passed, 1 skipped, 1209 subtests passed**;
- the Hermes direct/governed experiment and experimental decision-source pilot support a bounded agent-decision / AIOS-authority distinction.

The historical P2.7/R2.7 full regression preceded its documentation-only closeout. The P3 gate covered a different suite and date; counts are not additive.

## P2 Progression Posture

P2.7 / R2.7 is frozen and the governed Core is agent-ready in its declared scope. This does not establish general autonomous operation or unrestricted deployment readiness.

## P3 Progression Posture

P3 native multi-agent is accepted for sequential roles in one AIOS root run and one synthetic-task live pilot. OpenAI is a validated model provider, while OpenAI Agents SDK is not implemented. Hermes supplied an experimental decision artifact; no production Hermes integration is claimed. The separate P3.6a `approval_wait_already_resumed` limitation remains open for further steps after that wait in the same root run. See [Post-Core Evidence](AIOS_V3_POST_CORE_EVIDENCE.md).

## Limits And Non-Claims

This public status does not claim:

- production readiness or release readiness for unrestricted deployment;
- security certification, penetration-test certification, or formal verification;
- that all providers, tools, integrations, or environments are supported;
- that OpenAI Agents SDK or production Hermes integration is implemented;
- that the external Hermes/DeepSeek read-only review is a security certification, penetration-test certification, formal verification, or independent commercial certification;
- that every possible failure, bypass, or adversarial condition has been eliminated;
- arbitrary READ or WRITE access outside the admitted capability scope;
- arbitrary filesystem, database, or API WRITE;
- universal persistence or transactional guarantees;
- distributed exactly-once behavior or independent multi-host correctness;
- correctness after loss or corruption of authoritative persistence;
- that no secret could ever leak under a different configuration or threat model;
- that the public mock runtime is the private V3 runtime.

## Scope Of Persistence And Recovery Evidence

P0 persistence/reopen/replay/resume evidence was synthetic and scope-bound. Later real-execution evidence validated one bounded durable SQLite WRITE in its declared scope. Neither result is a universal durability or exactly-once claim.

If an effect may have occurred but the runtime cannot establish the outcome, `UNKNOWN_EFFECT` prevents blind automatic re-execution. Reconciliation is required. This conservative terminal state is a safety posture, not a guarantee that the unknown external outcome can always be reconstructed.

## Provider And Pilot Limit

`ModelPort` is provider-neutral as an architectural boundary. OpenAI is the first real model provider validated, and `gpt-5.6-sol` is the exact model used in the historical pilot evidence. OpenAI Agents SDK is not integrated or accepted; native AIOS multi-agent is a distinct capability. Execution authority remains with AIOS / `ExecutionEngine`.

The historical P2 pilot is evidence of one successful governed end-to-end path and a focused 10-test gate. The later P3 pilot separately exercised native sequential specialists. Neither is a latency, scale, availability, cost, reliability, or security benchmark.

## Public/Private Boundary

The public repository follows **bounded technical disclosure**. It publishes architectural roles, properties, limits, and aggregate evidence. It does not publish the private V3 runtime or the mechanisms that would allow the public documents to become a replica of it.

For the complete disclosure policy, see [Public vs Private Boundary](../../public-vs-private-boundary.md).

## Historical Evidence

The completed P0 record remains available in the P0 overview and evidence documents. AIOS V2 documentation, public demonstrations, public proof tests, ANDY field tests, and at-most-once evidence remain available as historical evidence for the governed execution backbone milestone. Later milestones do not erase or broaden those earlier results.
