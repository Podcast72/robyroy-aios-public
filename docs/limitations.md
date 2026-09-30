# Limitations

AIOS V3 P0 and P1 completed in declared scopes, P2.0–P2.7 were accepted in declared scopes, and R2.7 remediation and closeout completed. **P2.7 / R2.7 remains FROZEN and AGENT-READY; P3 native multi-agent, EA-0A proposal admission, and EA-0B external-host governance are accepted in their declared scopes above that baseline.** This public repository and its evidence remain intentionally limited.

## Milestone Limit

The existing P0 gate results remain historical aggregate evidence. P1 and P2.0–P2.7 acceptance, governed READ, bounded governed WRITE, durable SQLite WRITE, and governed filesystem WRITE describe later named scopes. The historical focused pilot-gate **10/10 PASS** result retains its original scope.

The historical P2.7/R2.7 full private regression was **2510 passed, 1 skipped, 11350 subtests passed**. The targeted P2.7/R2.7 closeout retest was **5 passed**. The P2.7/R2.7 regression preceded its documentation-only closeout. The separate P3 `tests_v3` gate is reported in the P3 section below; the suites are not additive.

They do not mean:

- unrestricted production or release readiness;
- security certification or formal verification;
- universal provider, model, tool, or integration support;
- elimination of every failure, bypass, or adversarial condition;
- correctness in every deployment environment.

Test counts refer only to their named gates. They must not be combined into a new unique-test total.

## P3 and external-agent limit

P3 native multi-agent was accepted for sequential roles and one bounded live pilot; it does not prove parallel or arbitrary agent orchestration. Its `tests_v3` gate was **1753 passed, 1 skipped, 1209 subtests passed**, separate from the P2.7/R2.7 `tests_v2 + tests_v3` historical gate. The P3.6a further-step-after-wait limitation remains open. Hermes decision-source evidence is experimental, not a production connector. OpenAI Agents SDK remains unimplemented.

EA-0A and EA-0B are accepted in declared scopes. The EA-0B Slice 3 canonical private full-repository gate recorded **2,888 collected, 2,887 passed, 1 skipped, 0 failed/errors, 12,407 subtests passed**. It is separate from the P2 and P3 gates. The macOS two-principal denial and leakage observations apply only to the tested configuration; they do not establish a universal sandbox, ready-made vendor adapters, security certification, universal recovery, or distributed exactly-once effects. See [External Host Evidence](public/aios-v3/AIOS_V3_EXTERNAL_HOST_EVIDENCE.md).

## Capability Limit

Governed READ does not imply unrestricted state visibility. Bounded governed WRITE, including filesystem WRITE, does not imply arbitrary filesystem, database, API, or external-system mutation. The durable SQLite and filesystem results apply only to their declared admitted operations and assumptions.

## Real-Pilot Limit

One real OpenAI pilot used exact model `gpt-5.6-sol` to read allowed state, select one bounded WRITE, request explicit approval, and complete the governed end-to-end path. The focused pilot gate reported **10/10 tests PASS**.

That observation is not a latency, cost, scale, availability, reliability, provider-security, or broad autonomy benchmark. It is historical evidence distinct from later accepted P2 milestones and from the separate P3 native multi-agent milestone. OpenAI Agents SDK remains unimplemented.

## Persistence And Recovery Limit

P0 persistence, reopen, replay, and resume evidence was synthetic and scope-bound. Later milestones added bounded durable SQLite and filesystem WRITE, effect reconciliation, and durable effect evidence in declared scopes. These results depend on their tested identity and persistence assumptions.

`UNKNOWN_EFFECT` prevents blind automatic re-execution when an external effect may have occurred but cannot be proven. It does not guarantee that the external outcome can always be reconstructed. The public evidence does not claim distributed exactly-once semantics or independent multi-host correctness.

## Public Implementation Limit

The private V3 runtime is not distributed here. This repository does not publish:

- V3 source or implementation-sensitive details;
- private test source or fixtures;
- raw `RunStore`, conversation/checkpoint-state, context, or trace schemas;
- private authorization, approval, and trust-boundary mechanisms;
- exploit or adversarial probe details;
- private prompts or operator internals;
- local paths, credentials, raw audit/log/trace data, private configuration, or deployment internals.

As a result, the V3 evidence cannot be reproduced from this public repository alone.

## Public Demonstration Limit

The runnable public mock and public invariant tests remain intentionally V2-shaped. They demonstrate the earlier governed-backbone model:

`request -> planner -> execution_engine -> tool_registry -> runtime_guard -> tool -> result_gate -> result`

They are not a reduced V3 runtime and must not be used to infer private V3 implementation details.

## Historical Evidence Limit

The V2 field tests, proof tests, at-most-once evidence, and enterprise-suite snapshots retain the claim limits stated in their own documents. V3 milestones do not broaden those historical results.

## Disclosure Model

The repository uses **bounded technical disclosure**: enough architecture, properties, aggregate evidence, and limits for public review without publishing the mechanisms required to replicate the private runtime.
