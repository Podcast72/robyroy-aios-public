# AIOS V3 Status And Limits

## Current Status

**Reviewed 18 October 2026: RM-23 ACCEPTED for the serial synthetic macOS profile; RM-24 ACCEPTED for the technical macOS profile; Core c3-r3 technically frozen.** The [dated evidence matrix](CHANGELOG-2026-10-18.md) records private provenance, exact artifact identities, the canonical **3,288 PASS / 0 FAIL / 1 SKIP with 13,712 subtests**, separate TLS checks and fresh-clone offline recovery. No private suite was rerun for this publication.

The qualified envelope is one user and one active execution on macOS; three broker handlers do not mean three parallel runs. Synthetic workloads, real OS-principal tests, historical provider-live pilots and the credential-free HTTPS transport check remain distinct. Recovery requires compatible macOS and the preserved Python runtime prerequisites. No GUI, SaaS, Linux/VPS or independent certification claim follows.

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
| Gateway client / Hermes governed plugin | RM-17/RM-18 implemented; RM-21 installed local boundary offline verified, with separate later technical macOS evidence. Historical provider pilots do not establish c3-r3 production readiness. |
| OpenAI provider | Implemented via the Responses API SDK; historical bounded real-provider pilots. |
| OpenAI Agents SDK / other unqualified adapters / MCP | Deferred or planned; native AIOS orchestration and API SDK use do not implement these integrations. |

## Historical RM-21 Evidence Scopes

RM-21's retained canonical private result is **3,233 passed, 0 failed, 1 skipped; 13,654 subtests passed; exit 0**. Its separate installed replay suite reports **202 passed, 0 failed, 0 skipped; exit 0**. Focused checks and parent-only coverage are recorded separately in the [qualification table](AIOS_V3_RELEASE_QUALIFICATION.md#rm-21-candidate-and-aggregate-evidence).

The one canonical skip requires a case-sensitive filesystem unavailable on the measured host. Parent coverage excludes worker, CLI, host, registry, broker and OS processes from its numerator. Functional observations cover stated boundaries separately. The final operational controller exited before all scenarios; only the reached subset has a passing assertion. No whole-controller success is inferred.

[Earlier P2/P3 evidence](AIOS_V3_CURRENT_EVIDENCE.md) and [EA-0B results](AIOS_V3_EXTERNAL_HOST_EVIDENCE.md) are historical, separately scoped and never summed with RM-21. Private suites were not rerun for this public refresh.

## Historical RM-22 Review And Candidate Changes

The earlier 13 October review recorded narrower passing synthetic/local functional preparation and RM-22 BLOCKED, with deployment/provider/accounting and authorization gates still open. This is retained history. The later RM-23/RM-24 macOS decisions and c3-r3 identity have their own [18 October evidence](CHANGELOG-2026-10-18.md). Absent usage or cost is not available, never assumed zero.

Neither RM-21 acceptance nor an earlier installed OS-boundary slice automatically qualifies modified source, a new wheel or a changed deployment. The c3-r3 technical freeze does not establish a new provider-live campaign or final production release.

## Recovery And Integration Limits

`UNKNOWN_EFFECT` remains terminal against blind automatic re-execution. It does not guarantee reconstruction of every external effect. The native multi-agent pilot was sequential, on a synthetic task, with a bounded real-provider run; it was not a reliability benchmark. The historical native approval-wait continuation limitation remains scoped to that path; the Hermes gateway flow does not silently close it.

Earlier Hermes decision-artifact experiments, the implemented offline plugin, and any separate provider-live production qualification are separate evidence categories.

## Non-Claims And Disclosure

The evidence does not establish unrestricted production readiness, security or compliance certification, formal proof, universal provider/tool/deployment support, hostile-admin containment, or distributed exactly-once effects.

The executable public mock remains V2-shaped. It has no private V3 source, durable approval, persistent recovery, provider integration or OS isolation. Its public path checks are not a filesystem race-proof sandbox.

[Bounded technical disclosure](../../public-vs-private-boundary.md) remains unchanged: private source, tests, fixtures, schemas, approval mechanisms, security probes, raw artifacts, personal data, paths, credentials and deployment internals are withheld.
