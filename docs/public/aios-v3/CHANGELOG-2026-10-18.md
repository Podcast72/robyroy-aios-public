# macOS Core technical freeze — 18 October 2026

**TEST SUITE VERIFIED · TECHNICAL FREEZE COMPLETE**, within the declared macOS profile. **RM-23 ACCEPTED** for serial operation with synthetic workloads; **RM-24 ACCEPTED** for the technical macOS candidate `aios-macos-c3-20261017-r3`.

This update moves the public account from the 15 October evidence-preservation freeze to an identified, qualified macOS Core technical baseline. The private record reports no remaining demonstrated technical blocker in that profile. This is not acceptance of a graphical application, a SaaS service, Linux/VPS deployment, or a commercial release.

## Provenance and verification level

This is a maintainer-published synthesis of the private RM-23 final-readiness and capacity records, RM-24 differential review and TLS correction record, and the 18 October freeze closure and recovery receipts. Those records were inspected for this publication; only aggregate outcomes and explicitly selected artifact identities are disclosed here. The acceptance decisions belong to that internal qualification process, not to an independent certification body.

Private suites, provider calls, OS-principal tests and recovery operations were **not rerun for this public documentation update**. Reported private results below are distinct from the public repository's own V2 mock tests and link checks. Raw evidence and V3 source remain private, so this repository does not let a public reader independently reproduce the private qualification or download the frozen product.

## What changed since the last public update

Comparison baseline: the [15 October security-freeze account](../security-freeze-2026-10-15/README.md), published in public commit `9441f1bf8133b2ca2058e9448da5e54bf2db0a3b`. At that point, the public qualification pages still reflected their 13–14 October review: RM-21 accepted offline and RM-22 blocked before LIVE. These are dated historical statements, not a description of the 18 October macOS candidate.

| Area | Previous public account | New documented position |
| --- | --- | --- |
| Freeze meaning | Evidence and installed packages preserved; no automatic qualification of the checkout or later milestones | c3-r3 macOS Core technical freeze, with selected artifact identities, source/test snapshot and private recovery receipts |
| Qualification | RM-21 corrected offline candidate; RM-22 preparation and open gates in the older review | RM-23 accepted in the serial synthetic macOS profile; RM-24 accepted in the technical macOS profile |
| Canonical regression | RM-21: 3,233 pass / 0 fail / 1 skip; 13,654 subtests | c3 snapshot: 3,288 pass / 0 fail / 1 skip; 13,712 subtests; separate run, never added to earlier totals |
| Governed execution and approval | Earlier scoped READ/WRITE and approval evidence; 15 October policy denial and operator rejection | Later installed macOS record adds scoped IPC, store/resource access, approval, replay and restart checks with two real OS principals and synthetic resources |
| Capacity and conservative recovery | Earlier scope-bound persistence and uncertainty evidence | Explicit serial capacity profile, bounded broker admission and failure checks; uncertainty remains terminal against blind retry |
| Adversarial review | The evidence-preservation freeze did not establish a new adversarial qualification | RM-24 differential A–J review with classified reuse of unchanged evidence; TLS finding closed on r3, with separate focused regressions |
| HTTPS transport | No new c3-r3 transport result in the previous publication | Real TLS 1.3 connection with certificate-chain and hostname verification; credential-free HEAD returned HTTP 421, without inference |
| Recoverability | Earlier archival preservation, with artifact/checkout distinctions | Fresh GitHub clone recovery reports 6,552 inventoried files and offline installation checks; original checkout not required |

The 15 October observations keep their original meaning: later acceptance does not turn its rejected or waiting actions into successful writes. Likewise, the separate [14 October Hermes demonstration](../../demos/hermes-aios-2026-10-14/README.md) remains historical real-provider evidence. Neither that demo nor the new TLS check establishes a new full provider-live campaign for c3-r3.

## Public evidence matrix

All results in this table are attributed to the private records summarized above. Rows are separate verification scopes; counts are not additive.

| Evidence | Recorded outcome | What it supports and where it stops |
| --- | --- | --- |
| RM-23 decision | ACCEPTED | Identified macOS serial profile with synthetic workloads; not a concurrent multi-user service |
| Canonical c3 full suite | **3,288 PASS / 0 FAIL / 1 SKIP; 13,712 subtests; exit 0** | Earlier identified source/test snapshot; skip requires a case-sensitive filesystem. No fresh full suite was run on the freeze commit |
| Real macOS OS-principal checks | Two distinct real OS principals; scoped IPC, store/resources, approval, replay and restart evidence retained | Real local OS/process boundaries with synthetic resources. No universal containment of hostile workers or administrators |
| Capacity and failure handling | Bounded busy/rejection, timeout and worker-failure checks in the serial profile | Three broker handlers are an ingress limit, not three simultaneous runs. No universal overload latency or HTTP 503 delivery guarantee |
| RM-24 differential review | ACCEPTED for c3-r3; applicable unchanged evidence reused | A–J review is a bounded internal technical assessment, not proof of absence of vulnerabilities |
| r3 broker/TLS regressions | **44 PASS / 0 FAIL / 0 SKIP**, installed; **1 PASS** source fixture separately | Focused broker/bundle change. The c3 wheel is unchanged; this is not another canonical full run |
| Public HTTPS transport | TLS 1.3; chain and hostname verified; HEAD to `api.openai.com`, HTTP 421 | No credentials, request body, inference or new billed model usage. Transport verification does not establish API inference success |
| Fresh-clone recovery | **6,552 files** inventoried; complete canonical snapshot of **2,836 files**, including **264 tests**; **24 Git refs** retained | Separate clone and recovery verification, not qualification on a second physical Mac |
| Offline runtime recovery | New environment; **90 installed product members** matched the wheel; dependency consistency and build-tool recovery passed | Requires compatible macOS and the preserved Python 3.13.2 runtime at its standard installation prefix; arbitrary relocation is not qualified |

The previously observed intermittent `tool_contract_drift` failure retains its unresolved historical causal uncertainty. The accepted final identified snapshot and passing results do not retroactively prove the cause or a runtime fix for that earlier observation. Failed intermediate attempts remain failures in the private record.

## Frozen identity

These are reference identifiers from the private freeze record, not public download links or a public source release. Hashes support artifact identity checks; they do not independently prove behavior or security.

| Reference | Identifier |
| --- | --- |
| Freeze date | `2026-10-18` |
| Selected candidate | `aios-macos-c3-20261017-r3` |
| Private annotated freeze tag | `AIOS-macOS-Core-Freeze-c3-r3-20261018` |
| Private final freeze commit | `39a2abe80fa3d6be2ee47237eaa152fb76ab14d4` |
| c3 wheel SHA-256 | `a41c417bb9e57d67e09f887b6ca53391ea35028dff0fbf6a17cd4f43ac0e3874` |
| c3-r3 bundle SHA-256 | `cb55c09c2f9dd645047172fb6a58cf8601465c5883c4b9ac683e41788c883988` |

The freeze preserves previously qualified bytes and adds archival/identity verification. The r3 broker/bundle correction has its own focused evidence; the earlier full-suite result is retained for the unchanged c3 wheel and identified snapshot. No new full run on the final archival commit is implied. Older c1/c2/r1/r2 artifacts remain historical evidence, not the selected candidate.

The private recovery record reports preservation of essential source, tests, dependencies, runtime/build inputs and Git objects without dependence on the original checkout. The exact runtime and installer are preserved privately. Compatible macOS remains a prerequisite; this is not an image of the entire operating system or a guarantee that any Mac can run it unchanged.

## Operating envelope and non-claims

- One user and one active execution; three broker handlers do not imply three runs or users.
- Existing budgets and two cumulative admissions per namespace in the tested profile; the measured READ/WRITE limits remain bounded. Rejection or BUSY after the documented cases does not promise automatic restoration of authority.
- `UNKNOWN_EFFECT` remains terminal against blind automatic re-execution. Replay and restart evidence does not establish distributed exactly-once effects or recovery of every external outcome.
- No universal hostile-worker sandbox, hostile-admin containment, or guaranteed detection of coherent rollback using only a local reference.
- CPU/RSS hard caps, saturation SLAs, multi-user throughput and remote-LLM cost/performance are not qualified by these results.
- No graphical application readiness, SaaS readiness, Linux/VPS qualification, independent security certification, universal provider/tool support or unrestricted production readiness is claimed. RM-25 is outside this update.
- Native AIOS orchestration and OpenAI Responses API use remain distinct from OpenAI Agents SDK, which remains deferred in the public integration record.

Future changes require a distinct candidate and relevant qualification. This publication does not change the private freeze tag or artifacts.

## Public/private boundary

Published here: a dated delta, aggregate matrix, selected reference identities and explicit limits. Withheld: private source and documentation, tests/fixtures, raw logs and receipts, local paths and account identifiers, personal data, credentials, security probes, deployment configuration and reserved artifacts. Private links are not presented as accessible resources.

[Repository home](../../../README.md) · [Current V3 evidence](AIOS_V3_CURRENT_EVIDENCE.md) · [Qualification history](AIOS_V3_RELEASE_QUALIFICATION.md) · [Status and limits](AIOS_V3_STATUS_AND_LIMITS.md) · [Public/private boundary](../../public-vs-private-boundary.md)
