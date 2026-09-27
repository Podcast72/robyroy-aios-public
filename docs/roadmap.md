# Roadmap

The governed Core reached **P2.7 / R2.7 FROZEN** and is **AGENT-READY**. V3 P0 and P1 completed in declared scopes, P2.0–P2.7 were accepted in declared scopes, and R2.7 remediation and closeout completed. AIOS V2 remains the historical governed-execution backbone.

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

## Near-Term Public Work

1. Keep V3 status, architecture, evidence, glossary, invariants, and limitations aligned without exposing implementation.
2. Preserve V2 documents, public demonstrations, proof tests, and field-test artifacts as historical context except for necessary accuracy or safety corrections.
3. Extend public evidence only through sanitized, aggregate reports with explicit scope and non-claims.
4. Keep automated public checks version-aware so V2 demonstration invariants are not mistaken for V3 implementation tests.
5. Review every future public update against the bounded technical disclosure policy.

## Future Engineering Direction

The next phase is **provider-neutral Agent Integration Architecture**: Governed Core -> provider-neutral agent integration boundary -> external agent systems. OpenAI is the first planned implementation; it is not yet implemented. Other systems may follow behind an appropriate boundary. `ModelPort` separates provider concerns from execution authority, which remains with AIOS / `ExecutionEngine`. Any result should be published only after its scope is verified and its disclosure risk reviewed.

No future capability is implied complete by this roadmap.

## What Is Intentionally Not On This Roadmap

- publishing or reconstructing the private V3 runtime;
- publishing raw schemas, fixtures, logs, traces, prompts, probes, or configuration;
- publishing private authorization, approval, or trust-boundary mechanisms;
- turning the V2 mock runtime into a V3 replica;
- making production-readiness, security-certification, formal-proof, or universal-provider claims without matching evidence.
