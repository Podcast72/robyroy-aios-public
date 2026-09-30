# AIOS V3 Current Evidence

This is the canonical aggregate, public-safe record of AIOS V3 progression through EA-0B Slice 3 as of 30 September 2026. The P2.7 / R2.7 governed-core baseline remains frozen and valid. It does not publish private source, tests, schemas, traces, credentials, local paths, authority mechanisms, or adversarial procedures.

## Milestone Narrative

```text
V2 — Governed Execution Backbone
-> V3 P0 — Governed Agent Runtime
-> P1 — Governed Real Execution
-> P2.0 — Initial natural-language governed interaction
-> P2.1–P2.7 — Accepted in declared scopes
-> R2.7 — Remediation and closeout completed
-> Governed Core — FROZEN / AGENT-READY
-> P3 native multi-agent — ACCEPTED in its declared sequential scope
-> EA-0A — Governed preformed proposal admission ACCEPTED
-> EA-0B Slice 1 — External governed READ ACCEPTED
-> EA-0B Slice 2 — External governed WRITE/approval/resume ACCEPTED
-> EA-0B Slice 3 — Tested macOS two-principal isolation ACCEPTED
```

V3 P0 and P1 completed in their declared scopes. P2.0–P2.7 were accepted in declared scopes. P2.7 / R2.7 remains **FROZEN**, and the governed Core remains **AGENT-READY**. P3 native multi-agent, EA-0A, and EA-0B Slices 1–3 are accepted in their declared scopes above that baseline. These statuses do not establish unrestricted deployment readiness.

## P2 Milestone Record

| Milestone | Public-safe outcome |
| --- | --- |
| P2.0 — Initial natural-language governed interaction | Accepted |
| P2.1 — Governed WRITE approval | Accepted |
| P2.2 — OpenAI live runtime | Accepted; model-provider path, not an OpenAI Agent integration |
| P2.3 — Canonical action / approval binding | Accepted |
| P2.4 — Approval consumption and replay safety | Accepted |
| P2.5 — Authoritative effect reconciliation | Accepted |
| P2.6 — Durable effect receipt journal | Accepted |
| P2.7 — Governed filesystem WRITE | Accepted in bounded declared scope |
| R2.7 — Remediation and closeout | Completed; Core frozen and agent-ready |
| P3 — Native multi-agent | Sequential specialist roles accepted inside one AIOS root run; authority remains with AIOS |
| EA-0A — Preformed proposal admission | External proposal admitted as non-authoritative; existing governance retained with zero inference |
| EA-0B Slice 1 — External READ | Vendor-neutral external process boundary, durable proposal binding, observational status, one observed READ dispatch |
| EA-0B Slice 2 — External WRITE | Durable approval wait, AIOS-only approval, identity-based resume, one observed dispatch |
| EA-0B Slice 3 — Tested OS isolation | Two-principal macOS pilot; tested direct bypass denied and governed READ/WRITE retained |

These names state architectural outcomes, not private implementation procedures.

## Capability And Evidence Summary

| Capability | Public-safe evidence | Claim boundary |
| --- | --- | --- |
| Governed agent runtime | V3 P0 completed in its declared validation scope | Historical foundation; not a production-readiness claim |
| Governed READ | Validated in a successive real-execution milestone | Limited to the admitted capability and tested scope |
| Bounded governed WRITE | Validated with applicable authority and approval requirements | Not arbitrary filesystem, database, or external-system write access |
| Durable SQLite WRITE | Validated in its declared persistence scope | Not universal durability or distributed exactly-once semantics |
| P2 progression | P2.0–P2.7 accepted in declared scopes; R2.7 completed | No claim beyond accepted scopes |
| Governed filesystem WRITE | Validated in a bounded declared scope | Not arbitrary filesystem WRITE |
| Approval path | Explicit approval was required and observed for the pilot WRITE | Does not disclose approval implementation or policy internals |
| Recovery posture | Historical synthetic P0 replay, reopen, and resume evidence plus later scoped effect reconciliation remain fail-closed; uncertain effects stop at `UNKNOWN_EFFECT` | Does not guarantee reconstruction of every external outcome or universal duplicate-effect prevention |
| Real-provider pilot | One OpenAI `gpt-5.6-sol` end-to-end pilot completed; historical focused gate **10/10 PASS** | One observed governed pilot, not an implemented external agent integration |
| Historical P2.7/R2.7 `tests_v2 + tests_v3` regression | **2510 passed, 1 skipped, 11350 subtests passed** | Preceded final documentation-only closeout |
| Targeted P2.7/R2.7 closeout | **5 passed** | Focused filesystem ambiguity/recovery and result-exposure properties |
| P3 targeted multi-agent gate, 29 September 2026 | **164 passed, 77 subtests passed** | Slice 1–4 and related focused families |
| P3 `tests_v3` gate, 29 September 2026 | **1753 passed, 1 skipped, 1209 subtests passed**, exit 0 | Post-pilot final runtime/test tree; different suite from historical P2.7/R2.7 gate |
| EA-0A governed admission | Preformed READ and approval-bound WRITE/replay with zero inference | Existing Core authority; no external gateway yet |
| EA-0B Slice 1 full-repository gate | **2,843 collected, 2,842 passed, 1 skipped, 12,240 subtests passed** | External READ; separate private run |
| EA-0B Slice 2 full-repository gate | **2,880 collected, 2,879 passed, 1 skipped, 12,282 subtests passed** | External WRITE/approval/resume; separate private run |
| **EA-0B Slice 3 canonical full-repository gate, 30 September 2026** | **2,888 collected, 2,887 passed, 1 skipped, 0 failed/errors, 12,407 subtests passed** | Latest complete private gate; 469 monitored source/test files byte-stable |

The P2.7/R2.7 full regression was not rerun solely for its final documentation-only closeout. The five targeted retests are narrower. The later P3 `tests_v3` result is a separate suite and must not be added to or directly trended against the historical `tests_v2 + tests_v3` result. The EA-0B full-repository gates are later private runs and are not additive with the P2 or P3 gates. The Slice 3 canonical gate followed a separately recorded sandbox-environment failure; that earlier run is not a passing gate. None establishes security certification or formal verification.

## Governed READ

Governed READ was validated as a real-execution capability after the P0 runtime foundation. The public claim is limited: the runtime admitted access to allowed state through its governed path. It does not imply unrestricted file, database, network, or system visibility.

## Bounded Governed WRITE

A bounded WRITE capability was validated in a later milestone. The action remained scope-constrained, subject to runtime admission, and approval-bound where required. The model proposal did not become execution authority.

This evidence does not support a claim of arbitrary write access, universal policy coverage, or operation outside the declared capability boundary.

## Durable Persistence

A durable SQLite WRITE was validated in its declared scope. The result supports a bounded persistence claim: the admitted change was observed through the governed durable path under the tested assumptions.

It does not establish universal transactional behavior, independent multi-host correctness, or distributed exactly-once semantics.

## Governed Filesystem WRITE

P2.7 accepted a governed filesystem WRITE in a bounded declared scope. R2.7 remediation and closeout completed. The public claim covers admission, effect observation, uncertainty handling, and result exposure at an aggregate level. It does not authorize arbitrary filesystem access or disclose implementation mechanisms.

## Approval Path

In the observed pilot, the model selected one bounded WRITE only after reading allowed state. The action required explicit approval before execution. Approval was part of the governed path; it was not inferred from model prose and did not grant authority outside the proposed action.

The implementation of approval binding, verification, and authorization remains private.

## Recovery Posture

The historical P0 persistence/reopen/replay/resume evidence remains synthetic and scope-bound. Later accepted milestones add scoped effect reconciliation and durable evidence. The recovery posture remains conservative:

- terminal outcomes can be replayed from authoritative execution state rather than blindly executed again;
- retry is permitted only when the governed runtime can establish that it is safe within the applicable scope;
- an uncertain external effect converges to `UNKNOWN_EFFECT` and requires reconciliation;
- no universal exactly-once or duplicate-effect-prevention claim is made.

## Real-Provider End-To-End Pilot

One real governed pilot used OpenAI model `gpt-5.6-sol` and completed the following bounded path:

1. read allowed state;
2. selected a single bounded WRITE;
3. requested explicit approval;
4. executed the admitted action through `ExecutionEngine`;
5. traversed the governed `RunStore`, structured trace, `ResultGate`, and controlled execution-context boundaries;
6. completed the governed end-to-end response path.

The focused pilot gate reported **10/10 tests PASS**.

This is one observed governed pilot. It does not establish unrestricted production readiness, security certification, formal proof, universal provider behavior, or performance and reliability at scale.

## Synthetic Evidence And Real End-To-End Evidence

Synthetic evidence isolates runtime properties and failure handling under controlled validation conditions. It is useful for checking invariants, state transitions, replay behavior, and fail-closed outcomes, but it does not by itself demonstrate a real provider and real admitted effect in one path.

The pilot evidence is end to end in a narrower sense: a real model provider interpreted allowed state, proposed one bounded action, obtained explicit approval, and completed the governed durable path. That broader path does not invalidate the limits of the synthetic evidence or turn one pilot into a deployment claim.

## Post-core P3 and external decision evidence

The accepted P3 native multi-agent pilot used OpenAI `gpt-5.6-sol` on a synthetic task with Coordinator, Analyst, Challenger, and Operator roles in one AIOS session/root run. It recorded 10 governed model inferences, 10 network calls, 3 governed tool calls (2 READ, 1 WRITE), zero retries, ordinary approval, one observed effect, and replay without duplicate WRITE. Its first separate attempt failed closed before READ, WRITE, or approval. The later successful pilot did not inject a live crash.

A separate external model-assisted read-only technical review through Hermes with DeepSeek V4 Pro provided findings for private remediation. Hermes direct and governed A/B pilots, then an experimental Hermes-decision / AIOS-authority pilot, provide bounded evidence for the distinction between agent decision and AIOS execution authority. [Post-Core Evidence](AIOS_V3_POST_CORE_EVIDENCE.md) records the review, remediation sequence, pilots, and limits.

`ModelPort` keeps provider concerns separate from AIOS / `ExecutionEngine` execution authority. Native AIOS multi-agent support and validated OpenAI model-provider use do **not** imply OpenAI Agents SDK integration; that SDK is not implemented. The Hermes decision source was an experimental adapter, not a production Hermes integration. The separate P3.6a `approval_wait_already_resumed` limitation remains open for further steps in the same root run after that wait.

## External Agent / Host Evidence

EA-0A admitted preformed external proposals as proposals, preserving AIOS authority and the existing governed path with zero inference. EA-0B added a vendor-neutral external process boundary. Slice 1 observed one governed READ dispatch and historical result replay after restart rather than a fresh target read. Slice 2 observed zero dispatch before AIOS approval, then one governed WRITE dispatch after resume of the same durable action; replay remained safe in the tested scope and canonical target drift was blocked. Slice 3 tested two distinct macOS OS principals: direct access to protected AIOS resources in the pilot was denied, while governed READ and WRITE remained available through EA-0B. The final probe observed 487 denied operations and an unchanged protected tree; a 31-file/60-value leakage audit found no leakage. This is a bounded configuration claim, not a universal sandbox or exactly-once claim. See [External Host Evidence](AIOS_V3_EXTERNAL_HOST_EVIDENCE.md).

The earlier Hermes experiments in [Post-Core Evidence](AIOS_V3_POST_CORE_EVIDENCE.md) remain distinct from EA-0B; they do not constitute a production Hermes adapter.

## Evidence Boundary

No raw pilot trace, audit record, prompt, fixture, schema, policy implementation, approval mechanism, trust-boundary detail, credential, local path, or deployment configuration is published here. The named components describe aggregate passage through the governed runtime; they are not an implementation recipe.

For the complete claim and disclosure limits, see [AIOS V3 Status and Limits](AIOS_V3_STATUS_AND_LIMITS.md) and [Public vs Private Boundary](../../public-vs-private-boundary.md).
