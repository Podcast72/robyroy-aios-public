# Roadmap

**Status review — 13 October 2026:** RM-21 is ACCEPTED for its corrected offline candidate; RM-22 remains BLOCKED before LIVE. The Hermes governed plugin is implemented and offline verified. OpenAI uses the Responses API SDK; OpenAI Agents SDK remains deferred. [Current qualification and integration record](public/aios-v3/AIOS_V3_RELEASE_QUALIFICATION.md).

The governed Core reached the historical **P2.7/R2.7 FROZEN / AGENT-READY** baseline. V3 P0 and P1 completed in declared scopes, P2.0–P2.7 were accepted in declared scopes, and R2.7 remediation and closeout completed. P3 native multi-agent, EA-0A preformed proposal admission, and EA-0B external-host governance are accepted above that frozen baseline in their declared scopes. AIOS V2 remains the historical governed-execution backbone.

## Completed Milestones

### V3 P0 — Governed Agent Runtime

- agent-runtime architecture documented at a public-safe level;
- governed model/tool round trip and synthetic recovery properties validated in the declared P0 scope;
- historical aggregate gate evidence preserved in the P0 evidence document.

### P1 — Governed Real Execution

- governed READ validated;
- bounded governed WRITE validated;
- durable SQLite WRITE validated in its declared scope;

P0 and P1 completion refers only to the declared milestone scopes. It does not establish unrestricted production readiness.

## P2.0 — Initial Natural-Language Governed Interaction

- implemented and validated in its declared scope;
- one real OpenAI `gpt-5.6-sol` end-to-end pilot completed;
- focused pilot gate: **10/10 tests PASS**.

P2.0 validation refers only to its declared scope. It does not establish unrestricted production readiness.

## P2.1–P2.7 And R2.7

P2.1–P2.7 accepted governed WRITE approval, OpenAI live runtime, canonical action/approval binding, approval consumption and replay safety, authoritative effect reconciliation, durable effect receipt journal, and bounded governed filesystem WRITE in their declared scopes. R2.7 remediation and closeout completed. The Core is frozen and agent-ready; no unrestricted deployment claim is implied.

## P3 — Native Multi-Agent

Accepted in its declared sequential scope at `P3_NATIVE_MULTI_AGENT_LIVE_ACCEPTED`. The bounded live pilot exercised Coordinator, Analyst, Challenger, and Operator with one governed effect. The separate P3 `tests_v3` gate reported **1753 passed, 1 skipped, 1209 subtests passed**. [Post-Core Evidence](public/aios-v3/AIOS_V3_POST_CORE_EVIDENCE.md) gives the limits.

## EA-0A and EA-0B — External Host Governance

EA-0A accepted non-authoritative preformed proposals. EA-0B accepted a vendor-neutral external process boundary for governed READ, WRITE with AIOS approval/resume, and tested macOS two-principal isolation. See [External Host Evidence](public/aios-v3/AIOS_V3_EXTERNAL_HOST_EVIDENCE.md) for aggregate evidence and limits. A Hermes governed plugin is now implemented and offline verified. Other unqualified vendor adapters and MCP remain future work.

## RM-01 Through RM-21 — Installed And Operational Qualification

The private track completed baseline and development-package work, host/configuration/approval administration, execution-history integrity and recovery operations, gateway client and Hermes plugin integration. RM-13 was a design milestone; implementation followed in RM-14. RM-20 records an offline report workflow and a reported second-operator repeat with limited traceability. **RM-21 was accepted offline on 8 October 2026 for the corrected installed candidate.** [Milestone dates, scopes and aggregate evidence](public/aios-v3/AIOS_V3_RELEASE_QUALIFICATION.md).

## RM-22 — Preparation, BLOCKED Before LIVE

Local campaign and Hermes functional tests show narrower offline progress. Qualification of the changed candidate on the effective deployment, provider bindings, attributable accounting sources and explicit economic authorization remain open. No accepted RM-22 LIVE qualification or final production release is claimed. Historical RM-21 acceptance does not transfer automatically to new bytes.

## Near-Term Public Work

1. Keep V3 status, architecture, evidence, glossary, invariants, and limitations aligned without exposing implementation.
2. Preserve V2 documents, public demonstrations, proof tests, and field-test artifacts as historical context except for necessary accuracy or safety corrections.
3. Extend public evidence only through sanitized, aggregate reports with explicit scope and non-claims.
4. Keep automated public checks version-aware so V2 demonstration invariants are not mistaken for V3 implementation tests.
5. Review every future public update against the bounded technical disclosure policy.

## Future Engineering Direction

P3 native sequential multi-agent has been implemented and accepted in its declared scope. The gateway client and Hermes governed plugin are now implemented and offline verified; other adapter engineering remains future work. OpenAI is a validated model provider; OpenAI Agents SDK is not implemented. The earlier Hermes decision-source experiment used an artifact adapter. The later plugin/client path has separate RM-18/RM-21 offline verification, without production qualification. `ModelPort` separates provider concerns from AIOS / `ExecutionEngine` authority. Future claims require their own verified scope and disclosure review.

No future capability is implied complete by this roadmap.

## What Is Intentionally Not On This Roadmap

- publishing or reconstructing the private V3 runtime;
- publishing raw schemas, fixtures, logs, traces, prompts, probes, or configuration;
- publishing private authorization, approval, or trust-boundary mechanisms;
- turning the V2 mock runtime into a V3 replica;
- making production-readiness, security-certification, formal-proof, or universal-provider claims without matching evidence.
