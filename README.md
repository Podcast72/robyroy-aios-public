# AIOS — Governed Agent Runtime & Execution Layer

![AIOS demo architecture](assets/aios-demo-hero.png)

> **Models propose. AIOS governs. AIOS executes.**

## What AIOS Is

AIOS is a governed agent runtime and execution layer. It separates model proposals and agent coordination from the authority to execute actions, records execution truth independently of the conversation, and controls which results may be released.

This repository contains public technical documentation, aggregate evidence and a runnable V2 demonstration. The V3 product runtime remains private under [bounded technical disclosure](docs/public-vs-private-boundary.md).

## Live Demonstration — Hermes × AIOS

[![Live Hermes × AIOS demonstration: scope checks, human approval, governed execution and independent verification.](docs/demos/hermes-aios-2026-10-14/demo-flow.svg)](docs/demos/hermes-aios-2026-10-14/README.md)

AIOS doesn't trust what an AI agent says it did.
It verifies what actually happened.

On **14 October 2026**, Hermes **0.21.0** with DeepSeek **`deepseek-v4-flash`** used the AIOS governed adapter: an authorized READ succeeded, an out-of-scope READ was blocked by the runtime guard, and a WRITE waited for explicit human approval before AIOS executed and independently verified it. Hermes then encountered a final-response error; AIOS's execution evidence already confirmed the change. A rate limit is not established by that error.

[Read the real experiment and its evidence summary](docs/demos/hermes-aios-2026-10-14/README.md). This bounded real-provider demo is not a security certification, the LIVE RM-22 qualification, or evidence of isolation between macOS users. Only the AIOS tools used are governed.

## Security Freeze — 15 October 2026

[![Security freeze, 15 October 2026: separate roles and preserved evidence. Read the scope and results.](assets/security-freeze-20261015.svg)](docs/public/security-freeze-2026-10-15/README.md)

Hermes proposes, AIOS governs, and the operator decides on requests that require approval. The macOS laboratory record preserves policy denials, a separate human rejection, and OS access denials in the tested profile. The freeze secures the evidence and exact archived packages; it does **not** automatically qualify the repository checkout, RM-21 or RM-22.

[What was achieved](docs/public/security-freeze-2026-10-15/README.md) · [How the roles are separated](docs/public/security-freeze-2026-10-15/isolation.md) · [Evidence and qualification limits](docs/public/security-freeze-2026-10-15/evidence-and-limits.md)

## Current Status

**Reviewed 18 October 2026 · RM-23 ACCEPTED in the serial synthetic macOS profile · RM-24 ACCEPTED in the technical macOS profile · Core c3-r3 technical freeze complete.**

The identified c3 snapshot records **3,288 PASS / 0 FAIL / 1 SKIP and 13,712 subtests**. The c3 wheel is unchanged; the r3 broker/bundle correction has separate **44 PASS** installed regressions. The private freeze record reports fresh-clone recovery of **6,552 files** and a successful offline runtime recovery. These are maintained private qualification results, summarized here with [provenance, artifact identities and limits](docs/public/aios-v3/CHANGELOG-2026-10-18.md); no private suite was rerun for this publication.

**Operating envelope:** macOS, one user and one active execution, synthetic workloads for RM-23. Three broker handlers do not mean three parallel runs. This is a Core technical baseline; graphical application, SaaS, Linux/VPS and unrestricted production readiness are not established.

**OpenAI integration:** the OpenAI Python SDK and Responses API support the implemented model provider; AIOS owns native orchestration. **OpenAI Agents SDK remains deferred.** The separate [14 October real-provider demonstration](docs/demos/hermes-aios-2026-10-14/README.md) remains historical evidence. The later TLS 1.3 HEAD check verifies transport, without a new inference or full provider-live campaign.

[![RM-23](https://img.shields.io/badge/RM--23-accepted%20macOS%20serial-1f7a4d)](docs/public/aios-v3/CHANGELOG-2026-10-18.md)
[![RM-24](https://img.shields.io/badge/RM--24-accepted%20macOS%20technical-1f7a4d)](docs/public/aios-v3/CHANGELOG-2026-10-18.md)
[![Core freeze](https://img.shields.io/badge/macOS%20Core-c3--r3%20frozen-2456a6)](docs/public/aios-v3/CHANGELOG-2026-10-18.md#frozen-identity)
[![Scope](https://img.shields.io/badge/disclosure-bounded-lightgrey)](docs/public-vs-private-boundary.md)
[![History](https://img.shields.io/badge/AIOS%20V2-evidence%20preserved-6f42c1)](docs/public/aios-v2/README.md)

[What changed on 18 October](docs/public/aios-v3/CHANGELOG-2026-10-18.md) · [Qualification history](docs/public/aios-v3/AIOS_V3_RELEASE_QUALIFICATION.md) · [Evaluator guide](FOR_EVALUATORS.md) · [Architecture](docs/public/aios-v3/AIOS_V3_ARCHITECTURE.md) · [Status and limits](docs/public/aios-v3/AIOS_V3_STATUS_AND_LIMITS.md)

## What AIOS Actually Does

An agent proposes work. AIOS checks whether that work is admitted under the applicable policy, capability, budget and approval, executes the admitted action, records the observed outcome and controls result release. The following describes architectural roles, not internal interfaces or an implementation recipe.

| Component | Practical role |
| --- | --- |
| `AgentLoop` / native multi-agent | Coordinates bounded turns and specialist roles; coordination grants no execution authority. |
| `ModelPort` / governed inference | Keeps provider concerns separate and routes model work through governance. |
| `GovernedActionPort` | Carries proposals toward the existing governed authority path. |
| `ExecutionEngine` | Admits and executes governed model and tool work. |
| `TrustPlane` / approval | Keeps trusted host authority separate from agent claims and binds approval to the admitted action. |
| SQLite `RunStore` | Preserves authoritative execution truth independently of conversation state. |
| `ResultGate` | Controls outward result release; a tool's output alone does not prove success. |
| External Agent Adapters | Translate bounded external proposals; they cannot approve or execute effects directly through this path. |
| Recovery / replay | Uses authoritative state and stops blind repetition when an effect is uncertain. |

## Governed Execution Backbone

### Current V3 architecture

```mermaid
flowchart TD
  U[User] --> A[AgentLoop / native specialists]
  A --> P[Model and action proposals]
  X[External agent / Hermes adapter] --> H[External Host Admission]
  H --> P
  P --> G[AIOS governance / TrustPlane / applicable approval]
  G --> E[ExecutionEngine]
  E --> W[Admitted model or tool work]
  W --> R[Authoritative RunStore / observed outcome]
  R --> Q[ResultGate]
  Q --> F[Controlled result / final answer]
```

This is a high-level authority and data-flow diagram. Model calls and tool calls are governed work; external provenance and persuasive text do not create authority. Private schemas, contracts, approval mechanisms and deployment wiring remain private.

### V2 public backbone

```text
request -> planner -> execution_engine -> tool_registry -> runtime_guard -> tool -> result_gate -> result
```

The public mock preserves this V2 path. Its safety corrections improve the demonstration without turning it into a private V3 replica.

## External Agent / Host Governance

EA-0A and EA-0B established scoped external proposal admission, governed READ, approval-bound WRITE, replay/restart and tested macOS two-principal isolation. RM-17 added the gateway client; RM-18 added an actual Hermes plugin; RM-21 verified the installed local host/registry boundary offline using synthetic resources and real local processes.

Hermes remains a proposer. AIOS retains policy, capability, budget, approval, execution, replay, recovery and result-release authority. Earlier Hermes A/B decision-source experiments remain historical evidence, distinct from the implemented plugin and from a future provider-live qualification.

[External Host Evidence](docs/public/aios-v3/AIOS_V3_EXTERNAL_HOST_EVIDENCE.md) · [Historical Hermes experiments](docs/public/aios-v3/AIOS_V3_POST_CORE_EVIDENCE.md) · [Current integration status](docs/public/aios-v3/AIOS_V3_RELEASE_QUALIFICATION.md#integration-status)

## Current V3 Evidence

[![AIOS V3 macOS Core: test suite verified and technical freeze complete, 18 October 2026. Reported private result: 3,288 pass, zero fail, one skip; RM-23 and RM-24 accepted within their stated macOS scopes.](assets/macos-core-freeze-20261018.svg)](docs/public/aios-v3/CHANGELOG-2026-10-18.md)

[18 October changelog, evidence matrix and freeze identities](docs/public/aios-v3/CHANGELOG-2026-10-18.md) · Reported private qualification; serial macOS scope; no independent certification.

![AIOS demo architecture](assets/aios-demo-hero2.png)

*Historical P2.7/R2.7 illustration. The banner and dated record above describe the current macOS qualification; the illustration's future integration labels remain historical.*

| Capability | Implemented / verified state | Limit |
| --- | --- | --- |
| Governed execution, AgentLoop and inference | Implemented; offline and bounded historical provider-live evidence | AIOS native orchestration, not OpenAI Agents SDK. |
| Governed READ and bounded WRITE | Verified in successive named scopes; corrected installed host qualified by RM-21 | Explicit approval where required; no arbitrary filesystem access. |
| Persistent approval binding, replay and crash recovery | Implemented and tested in declared persistence scopes | `UNKNOWN_EFFECT` remains terminal against blind re-execution; no distributed exactly-once claim. |
| SQLite RunStore and ResultGate | Implemented; authoritative truth and controlled result release | Conversation state and agent claims cannot substitute for execution evidence. |
| macOS host isolation | Verified in named local two-principal profiles | Neither a universal sandbox nor qualification of later changed deployments. |
| Hermes plugin and gateway client | Implemented and offline verified; separate bounded real-provider demo on 14 October 2026 | Historical provider evidence is separate from c3-r3 technical qualification and does not establish production readiness. |
| OpenAI Agents SDK | Planned / explicitly deferred | OpenAI API SDK use is a separate implemented integration. |
| RM-23 / RM-24 macOS qualification | ACCEPTED in the serial synthetic / technical macOS scopes respectively; c3-r3 frozen | One active execution; no GUI, SaaS, Linux/VPS or universal deployment qualification. |

### Separate verification snapshots

| Milestone and date | Result | Scope |
| --- | --- | --- |
| Historical P2.7/R2.7 | **2,510 passed, 1 skipped; 11,350 subtests passed** | Private `tests_v2 + tests_v3`; targeted closeout separately **5 passed**. |
| P3, 29 September 2026 | **1,753 passed, 1 skipped; 1,209 subtests passed** | Private `tests_v3`; sequential multi-agent, distinct historical live pilot. |
| EA-0B Slice 3, 30 September 2026 | **2,888 collected; 2,887 passed; 1 skipped; 12,407 subtests passed** | Separate canonical full-repository run. |
| **RM-21, 8 October 2026** | **3,233 passed, 0 failed, 1 skipped; 13,654 subtests passed; exit 0** | Corrected candidate, clean private `tests_v2 + tests_v3`. |
| **RM-21 installed package, 8 October 2026** | **202 passed, 0 failed, 0 skipped; exit 0** | Identified installed candidate outside the checkout. |
| **c3 canonical snapshot, retained for 18 October freeze** | **3,288 PASS / 0 FAIL / 1 SKIP; 13,712 subtests; exit 0** | Identified private snapshot; unchanged c3 wheel; no new full on the freeze commit. |
| **c3-r3 broker/TLS correction, 18 October 2026** | **44 PASS installed; 1 PASS source separately** | Focused broker/bundle regression, distinct from the canonical suite. |
| **c3-r3 private recovery, 18 October 2026** | **6,552 inventoried files; offline recovery PASS** | Fresh GitHub clone; compatible macOS/Python prerequisites, not qualification on another physical Mac. |

Counts are never summed. The RM-21 skip requires a case-sensitive volume unavailable on that host. Parent-only coverage and functional process evidence are separately delimited in the [qualification record](docs/public/aios-v3/AIOS_V3_RELEASE_QUALIFICATION.md). The final operational controller did not finish every scenario; only its reached subset was asserted passing, with remaining applicable properties checked at their stated levels.

The historical P2 OpenAI pilot and P3 multi-agent pilot were real provider runs on bounded synthetic tasks. RM-21 is an offline qualification, even where actual local processes and OS principals were used. No private suite or provider call was executed for this public refresh. Historical evidence does not automatically qualify changed candidates; the c3-r3 claim relies on its own identified records and applicable reuse, described in the [18 October update](docs/public/aios-v3/CHANGELOG-2026-10-18.md).

## V2 Historical Evidence Preserved

AIOS V2 remains documented as **AIOS V2 — Governed Execution Backbone**. The complete public V2 package, field tests, proof tests, and demonstration runtime remain in this repository as evidence of the preceding phase.

### At-most-once execution evidence

The V2 private enterprise runtime was adversarially validated within its declared persistent-runtime scope against duplicate ownership and blind re-execution. When an effect may have occurred but the outcome cannot be proven, the documented runtime converges to `UNKNOWN_EFFECT` rather than automatically retrying.

| V2 evidence | Historical result |
| --- | --- |
| At-most-once semantics | Verified in the declared V2 persistent-runtime scope |
| Concurrent duplicate callers | Blocked from duplicate ownership/execution |
| Repeated race validation | **125/125 passed** |
| V2 private enterprise suite snapshot | **927 tests passed + 6525 subtests passed** |
| Accounting/audit convergence | **PARTIAL** |
| Distributed/multi-host guarantee | **NOT CLAIMED** |

[Read the V2 at-most-once evidence](docs/public/aios-v2/AT_MOST_ONCE_EXECUTION_EVIDENCE.md).

## Proposed Restack Project — Separate Open Kernel

The **Open Governed Capability Execution Kernel** is a proposed future Restack project, not a claim about functionality already implemented in this repository. The proposed work would extract and develop a standalone, model-neutral capability-execution kernel for general networked software. It would govern explicitly declared capabilities, authorization, execution state, audit evidence, result release, and fail-closed recovery without requiring an AI model, an agent framework, OpenAI, or the private AIOS V3 runtime.

If selected, all software, tests, specifications, documentation, and other project results funded through Restack would be developed publicly and released in their entirety under the Apache License 2.0. The funded scope would exclude LLM or model development, integration, evaluation, and AI-specific orchestration. Existing AIOS material would provide background and prior engineering evidence only; it would not be a closed dependency of the proposed kernel.

[Read the proposed Restack project boundary](docs/public/restack/OPEN_GOVERNED_CAPABILITY_EXECUTION_KERNEL.md).

### ANDY controlled field tests

- The 2026-05-17 controlled Docker field test reported **13/13 checks passed**, with governed requests routed through AIOS, blocked cases remaining non-executed, and no direct bypass observed in that scope.
- The 2026-05-22 controlled Docker/VPS bypass-attempt follow-up reported **8/8 scenarios PASS**, with no useful action observed outside the governed backbone and no execution recorded outside the governed route.

These are controlled V2 field-test snapshots, not production-readiness or security-certification claims.

- [ANDY controlled field-test evidence](docs/public/field-tests/andy-aios-2026-05-17/README.md)
- [ANDY bypass-attempt evidence](docs/public/field-tests/andy-backbone-bypass-2026-05-22/ANDY_BACKBONE_BYPASS_ATTEMPT_EVIDENCE.md)
- [V2 public proof tests](docs/public-proof-tests/README.md)
- [V2 external public-mock validation](docs/public/aios-v2/AIOS_EXTERNAL_PIPELINE_VALIDATION.md)

## Quick Links

| Area | Link |
| --- | --- |
| External agent / host governance | [AIOS_V3_EXTERNAL_HOST_EVIDENCE.md](docs/public/aios-v3/AIOS_V3_EXTERNAL_HOST_EVIDENCE.md) |
| Proposed Restack project boundary | [Open Governed Capability Execution Kernel](docs/public/restack/OPEN_GOVERNED_CAPABILITY_EXECUTION_KERNEL.md) |
| Evaluator guide | [FOR_EVALUATORS.md](FOR_EVALUATORS.md) |
| AIOS in 5 minutes | [docs/public/AIOS_IN_5_MINUTES.md](docs/public/AIOS_IN_5_MINUTES.md) |
| V3 public index | [docs/public/aios-v3/README.md](docs/public/aios-v3/README.md) |
| Current V3 evidence | [AIOS_V3_CURRENT_EVIDENCE.md](docs/public/aios-v3/AIOS_V3_CURRENT_EVIDENCE.md) |
| V3 architecture | [AIOS_V3_ARCHITECTURE.md](docs/public/aios-v3/AIOS_V3_ARCHITECTURE.md) |
| V3 status and limits | [AIOS_V3_STATUS_AND_LIMITS.md](docs/public/aios-v3/AIOS_V3_STATUS_AND_LIMITS.md) |
| Historical P0 evidence | [AIOS_V3_P0_EVIDENCE.md](docs/public/aios-v3/AIOS_V3_P0_EVIDENCE.md) |
| Integration model | [docs/public/AIOS_INTEGRATION_MODEL.md](docs/public/AIOS_INTEGRATION_MODEL.md) |
| Roadmap | [docs/roadmap.md](docs/roadmap.md) |
| V2 historical index | [docs/public/aios-v2/README.md](docs/public/aios-v2/README.md) |
| Public/private boundary | [docs/public-vs-private-boundary.md](docs/public-vs-private-boundary.md) |

## Why Agent Governance Needs A Runtime

The risk changes when AI moves from answer to action. A model that can request tools, files, APIs, databases, or business workflows can create effects before the final answer is reviewed.

Direct model-to-tool patterns are useful prototypes, but the model should not be the final authority over execution. AIOS puts an independent runtime boundary between a proposal and its operational effect, then keeps result release and authoritative execution state inside that governed path.

| Concern | Direct agent path | AIOS-governed path |
| --- | --- | --- |
| Model output | Proposal can become action | Proposal remains non-authoritative |
| Model and tool calls | May use separate or implicit paths | Both traverse the governed backbone |
| Execution authority | Can be blurred into orchestration | Remains with `ExecutionEngine` |
| Approval | May be implicit in the request | Applied explicitly where the governed action requires it |
| Recovery | Retry may duplicate an uncertain effect | Fail-closed recovery and `UNKNOWN_EFFECT` block blind retry |
| State | Conversation and execution may be conflated | Conversation state and execution truth remain separate |
| Results | Output may be returned directly | `ResultGate` controls outward release |
| Evidence | Hard to reconstruct | Run state and audit remain reviewable |

## What Can Be Tested

The public executable surface remains V2-shaped and requires only **Python 3.11 or later**, without provider credentials or third-party packages.

| Testable area | Where |
| --- | --- |
| ALLOW/WARN/BLOCK, read-only demo and stable errors | [Public mock runtime](public_mock_runtime/README.md) |
| Public backbone consistency and synthetic JSON examples | [Backbone guide](backbone_public_test/README.md) |
| Input/rule validation and path containment regressions | [Independent public regressions](tests/test_mock_runtime_safety.py) |
| Local Markdown targets and heading anchors | [Offline checker](scripts/check_markdown_links.py) |
| Result redaction and approval without automatic runtime effect | [Examples](examples/) |
| Historical proof artifacts | [V2 public proofs](docs/public-proof-tests/README.md) |

```bash
python3 -B -m unittest discover -s tests -v
python3 -B -m unittest discover -s public_mock_runtime/proof_tests -v
python3 -B scripts/check_markdown_links.py
python3 public_mock_runtime/mock_runtime.py public_mock_runtime/examples/allow.json
python3 public_mock_runtime/mock_runtime.py public_mock_runtime/examples/warn.json
python3 public_mock_runtime/mock_runtime.py public_mock_runtime/examples/block.json
```

The BLOCK example intentionally exits with code 1 before tool execution. GitHub Actions runs the public test/check commands on Python 3.11 and 3.13; hosted results are pending until publication and execution. The V3 suite and source remain private; public mock tests cannot reproduce private qualification.

## What Is Public Here

- High-level V3 architecture, status, aggregate milestone results and explicit limits.
- Historical V2 documentation, proof tests, synthetic examples and sanitized field tests.
- A small V2-shaped executable mock and independent public regressions.
- An offline link checker and CI configuration without provider credentials.

## What Is Not Public

- V3 source code or private implementation details;
- private test source or fixtures;
- raw `RunStore` schema;
- private authorization, approval, and trust-boundary mechanisms;
- detailed exploit or adversarial probes;
- private prompts or operator internals;
- local paths, credentials, or credential fragments;
- raw audit records, logs, or traces;
- private configuration or deployment internals.

This is **bounded technical disclosure**: public properties, architecture, and aggregate evidence without a public replica of the private runtime.

## Public Presentation

The existing presentation is an AIOS V2 historical artifact. It explains the governed execution concept and remains available without being relabeled as a V3 runtime publication.

[Download the AIOS V2 Governed AI Execution Layer PDF](docs/public/AIOS_Governed_AI_Execution_Layer.pdf).

## Repository Map

| Path | Purpose |
| --- | --- |
| [FOR_EVALUATORS.md](FOR_EVALUATORS.md) | Guided review path for technical and grant evaluators |
| [docs/public/aios-v3/](docs/public/aios-v3/) | Current V3 architecture, evidence, status, and limits |
| [docs/public/aios-v2/](docs/public/aios-v2/) | Preserved V2 historical documentation and evidence |
| [docs/public/field-tests/](docs/public/field-tests/) | Sanitized V2 ANDY field-test evidence |
| [docs/public-proof-tests/](docs/public-proof-tests/) | Preserved V2 public proof artifacts |
| [public_mock_runtime/](public_mock_runtime/) | Minimal V2-shaped executable demonstration |
| [backbone_public_test/](backbone_public_test/) | V2 backbone consistency guide |
| [examples/](examples/) | Curated V2 public JSON cases |
| [tests/](tests/) | Public invariant tests for the V2 demonstration surface |
| [reference/](reference/) | Version-aware glossary and public invariants |

## What Comes Next

Finish the remaining RM-22 candidate/deployment and provider-accounting gates, freeze the qualified candidate, and obtain explicit economic authorization before a paid LIVE qualification. OpenAI Agents SDK and other unqualified adapters remain future work. Publishing this public refresh is a separate owner-approved step.

[Roadmap](docs/roadmap.md) · [Current limits](docs/public/aios-v3/AIOS_V3_STATUS_AND_LIMITS.md)

## Status

**RM-21 ACCEPTED within its identified offline scope; RM-22 BLOCKED before LIVE.** The private development package is not a final production release. Accepted milestones, isolated passing suites and historical pilots do not establish production readiness, certification, universal security or distributed exactly-once behavior.

## License

This repository is released under the [MIT License](LICENSE).
