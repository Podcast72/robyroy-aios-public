# AIOS V3 Current Evidence

This page publishes aggregate, public-safe engineering evidence for the current AIOS V3 progression. It does not publish private source, test fixtures, raw schemas, prompts, traces, logs, credentials, configuration, or trust-boundary internals.

## Milestone Narrative

```text
V2 — Governed Execution Backbone
-> V3 P0 — Governed Agent Runtime
-> P1 — Governed Real Execution
-> P2.0 — Initial natural-language governed interaction
-> Further P2 work — In progress
```

V3 P0 and P1 are completed in their respective declared scopes. P2.0 is implemented and validated in its declared scope. Further P2 work remains in progress; the evidence does not establish broad P2 completion or unrestricted deployment readiness.

## Capability And Evidence Summary

| Capability | Public-safe evidence | Claim boundary |
| --- | --- | --- |
| Governed agent runtime | V3 P0 completed in its declared validation scope | Historical foundation; not a production-readiness claim |
| Governed READ | Validated in a successive real-execution milestone | Limited to the admitted capability and tested scope |
| Bounded governed WRITE | Validated with applicable authority and approval requirements | Not arbitrary filesystem, database, or external-system write access |
| Durable SQLite WRITE | Validated in its declared persistence scope | Not universal durability or distributed exactly-once semantics |
| P2.0 governed interaction | Initial natural-language governed interaction implemented and validated in its declared scope | Later P2 work remains in progress |
| Approval path | Explicit approval was required and observed for the pilot WRITE | Does not disclose approval implementation or policy internals |
| Recovery posture | Synthetic P0 replay, reopen, and resume evidence remains fail-closed; uncertain effects stop at `UNKNOWN_EFFECT` | Does not extend the recovery claim to later real-execution evidence or guarantee reconstruction of every external outcome |
| Real-provider pilot | One OpenAI `gpt-5.6-sol` end-to-end pilot completed; focused gate **10/10 PASS** | One observed governed pilot, not a benchmark or certification |

## Governed READ

Governed READ was validated as a real-execution capability after the P0 runtime foundation. The public claim is limited: the runtime admitted access to allowed state through its governed path. It does not imply unrestricted file, database, network, or system visibility.

## Bounded Governed WRITE

A bounded WRITE capability was validated in a later milestone. The action remained scope-constrained, subject to runtime admission, and approval-bound where required. The model proposal did not become execution authority.

This evidence does not support a claim of arbitrary write access, universal policy coverage, or operation outside the declared capability boundary.

## Durable Persistence

A durable SQLite WRITE was validated in its declared scope. The result supports a bounded persistence claim: the admitted change was observed through the governed durable path under the tested assumptions.

It does not establish universal transactional behavior, independent multi-host correctness, or distributed exactly-once semantics.

## Approval Path

In the observed pilot, the model selected one bounded WRITE only after reading allowed state. The action required explicit approval before execution. Approval was part of the governed path; it was not inferred from model prose and did not grant authority outside the proposed action.

The implementation of approval binding, verification, and authorization remains private.

## Recovery Posture

The published persistence/reopen/replay/resume evidence remains synthetic and scope-bound. The recovery posture is described conservatively:

- terminal outcomes can be replayed from authoritative execution state rather than blindly executed again;
- retry is permitted only when the governed runtime can establish that it is safe within the applicable scope;
- an uncertain external effect converges to `UNKNOWN_EFFECT` and requires reconciliation;
- no universal exactly-once claim is made.

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

## Evidence Boundary

No raw pilot trace, audit record, prompt, fixture, schema, policy implementation, approval mechanism, trust-boundary detail, credential, local path, or deployment configuration is published here. The named components describe aggregate passage through the governed runtime; they are not an implementation recipe.

For the complete claim and disclosure limits, see [AIOS V3 Status and Limits](AIOS_V3_STATUS_AND_LIMITS.md) and [Public vs Private Boundary](../../public-vs-private-boundary.md).
