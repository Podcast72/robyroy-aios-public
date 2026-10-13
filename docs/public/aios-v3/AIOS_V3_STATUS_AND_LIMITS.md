# AIOS V3 Status And Limits

## Current Status

**Reviewed 13 October 2026: RM-21 ACCEPTED for the corrected offline candidate of 8 October 2026. RM-22 remains BLOCKED before LIVE.** The [qualification record](AIOS_V3_RELEASE_QUALIFICATION.md) defines IMPLEMENTED, TESTED, OFFLINE VERIFIED, LIVE VERIFIED, ACCEPTED and PLANNED, identifies the candidate, records milestone dates and separates every test scope.

> **Models propose. AIOS governs. AIOS executes.**

P0/P1, P2.0–P2.7, R2.7, P3 and EA-0A/EA-0B retain their historical declared acceptance scopes. P2.7/R2.7 is a historical frozen baseline, not a statement that later corrected artifacts are unchanged.

## Implemented And Verified Scope

| Area | Evidence and limit |
| --- | --- |
| Governed execution, AgentLoop and model inference | Implemented; tested offline and in bounded historical provider-live pilots. Models and orchestration hold no execution authority. |
| Governed READ / bounded WRITE | Verified in named capability scopes, including corrected installed-host composition; no arbitrary mutation. |
| Persistent approval binding | Implemented and tested; canonical approval is distinct from persuasive model text and agent provenance. |
| Replay / crash recovery | Verified at stated Core, installed and functional levels; uncertain effects prohibit blind redispatch. |
| SQLite RunStore / ResultGate | Authoritative execution truth and controlled result release remain separate from conversation state. |
| Host configuration/lifecycle and separate administration | RM-09–RM-12 implemented and qualified in declared local scopes. |
| macOS isolation | Tested named two-principal profiles, including RM-21 protected-resource denials; no universal sandbox or changed-candidate qualification. |
| Integrity, failure views and backup/restore | RM-13 design; RM-14–RM-16 implementation and bounded qualification. No distributed rollback guarantee. |
| Gateway client / Hermes governed plugin | RM-17/RM-18 implemented; RM-21 installed local boundary offline verified. Production/provider-live qualification remains open. |
| OpenAI provider | Implemented via the Responses API SDK; historical bounded real-provider pilots. |
| OpenAI Agents SDK / other unqualified adapters / MCP | Deferred or planned; native AIOS orchestration and API SDK use do not implement these integrations. |

## Separate Evidence Scopes

RM-21's retained canonical private result is **3,233 passed, 0 failed, 1 skipped; 13,654 subtests passed; exit 0**. Its separate installed replay suite reports **202 passed, 0 failed, 0 skipped; exit 0**. Focused checks and parent-only coverage are recorded separately in the [qualification table](AIOS_V3_RELEASE_QUALIFICATION.md#rm-21-candidate-and-aggregate-evidence).

The one canonical skip requires a case-sensitive filesystem unavailable on the measured host. Parent coverage excludes worker, CLI, host, registry, broker and OS processes from its numerator. Functional observations cover stated boundaries separately. The final operational controller exited before all scenarios; only the reached subset has a passing assertion. No whole-controller success is inferred.

[Earlier P2/P3 evidence](AIOS_V3_CURRENT_EVIDENCE.md) and [EA-0B results](AIOS_V3_EXTERNAL_HOST_EVIDENCE.md) are historical, separately scoped and never summed with RM-21. Private suites were not rerun for this public refresh.

## RM-22 And Candidate Changes

Later local preparation has narrower passing synthetic/local functional tests. Effective deployment isolation, real-provider bindings, attributable usage/accounting sources and economic authorization remain open. RM-22 is BLOCKED; absent usage or cost is not available, never assumed zero.

Neither RM-21 acceptance nor an earlier installed OS-boundary slice automatically qualifies modified source, a new wheel or a changed deployment. No accepted later LIVE milestone or final production release is established.

## Recovery And Integration Limits

`UNKNOWN_EFFECT` remains terminal against blind automatic re-execution. It does not guarantee reconstruction of every external effect. The native multi-agent pilot was sequential, on a synthetic task, with a bounded real-provider run; it was not a reliability benchmark. The historical native approval-wait continuation limitation remains scoped to that path; the Hermes gateway flow does not silently close it.

Earlier Hermes decision-artifact experiments, the implemented offline plugin, and a future provider-live production qualification are separate evidence categories.

## Non-Claims And Disclosure

The evidence does not establish unrestricted production readiness, security or compliance certification, formal proof, universal provider/tool/deployment support, hostile-admin containment, or distributed exactly-once effects.

The executable public mock remains V2-shaped. It has no private V3 source, durable approval, persistent recovery, provider integration or OS isolation. Its public path checks are not a filesystem race-proof sandbox.

[Bounded technical disclosure](../../public-vs-private-boundary.md) remains unchanged: private source, tests, fixtures, schemas, approval mechanisms, security probes, raw artifacts, personal data, paths, credentials and deployment internals are withheld.
