# Roadmap

The public roadmap now starts from a completed **AIOS V3 P0 — Governed Agent Runtime** milestone while preserving AIOS V2 as the historical governed-execution backbone.

## Completed Public Milestone

- V3 P0 architecture documented at a public-safe level;
- `AIOS_V3_P0_GATE=PASS`;
- **562/562 targeted P0 tests PASS**;
- Adversarial Remediation Gate: **354/354 PASS**;
- governed model/tool round-trip verified;
- synthetic persistence/reopen/resume verified;
- provider-neutral `ModelPort`;
- one governed OpenAI `gpt-5.6-sol` live invocation verified.

Completion refers to the declared P0 validation scope, not unrestricted production readiness.

## Near-Term Public Work

1. Keep V3 status, architecture, evidence, and limitations aligned without exposing implementation.
2. Preserve V2 documents, public demonstrations, proof tests, and field-test artifacts as immutable historical context except for necessary accuracy or safety corrections.
3. Extend public evidence only through sanitized, aggregate reports with explicit scope and non-claims.
4. Keep automated public checks version-aware so V2 demonstration invariants are not mistaken for V3 implementation tests.
5. Review every future public update against the bounded technical disclosure policy.

## Future Engineering Direction

Future milestones may broaden provider, tool, persistence, recovery, deployment, and integration validation. Any such result should be published only after its scope is verified and its disclosure risk reviewed.

No future milestone is implied complete by this roadmap.

## What Is Intentionally Not On This Roadmap

- publishing or reconstructing the private V3 runtime;
- publishing raw schemas, fixtures, logs, traces, prompts, probes, or configuration;
- publishing private authorization, approval, or trust-boundary mechanisms;
- turning the V2 mock runtime into a V3 replica;
- making production-readiness, security-certification, or universal-provider claims without matching evidence.
