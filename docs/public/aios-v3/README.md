# AIOS V3 P0 Public Documentation

AIOS V3 P0 is the current public architecture milestone for the source-private AIOS track.

> **Models propose. AIOS governs. AIOS executes.**

V3 evolves the governed execution backbone documented for AIOS V2 into a governed agent runtime. The `AgentLoop` can request model or tool work, but it does not own execution authority. Model calls and tool calls remain inside the governed path, with `ExecutionEngine` as the execution authority.

## Status

- AIOS V3 P0 completed
- `AIOS_V3_P0_GATE=PASS`
- **562/562 targeted P0 tests PASS**
- Adversarial Remediation Gate: **354/354 PASS**
- governed model/tool round-trip verified
- persistence, reopen, and resume verified in the synthetic P0 scope
- provider-neutral `ModelPort`
- first real provider: OpenAI
- exact model validated: `gpt-5.6-sol`
- one live provider invocation passed through the governed path

These are aggregate, scope-bound engineering results. They are not a security certification, a formal proof, or a production-readiness claim.

## Documents

| Document | Purpose |
| --- | --- |
| [AIOS_V3_P0_OVERVIEW.md](AIOS_V3_P0_OVERVIEW.md) | Public overview of the V2-to-V3 evolution and the P0 properties. |
| [AIOS_V3_ARCHITECTURE.md](AIOS_V3_ARCHITECTURE.md) | High-level V3 architecture and authority boundaries. |
| [AIOS_V3_P0_EVIDENCE.md](AIOS_V3_P0_EVIDENCE.md) | Aggregated P0 gate, round-trip, persistence, and live-provider evidence. |
| [AIOS_V3_STATUS_AND_LIMITS.md](AIOS_V3_STATUS_AND_LIMITS.md) | Current status, verified scope, non-claims, and disclosure limits. |

## Evolution, Not Replacement

The public history remains available under [AIOS V2](../aios-v2/README.md). Its governed-backbone documentation, ANDY field tests, at-most-once evidence, and public proof artifacts remain historical evidence for the preceding milestone.

The small executable demo under [`public_mock_runtime/`](../../../public_mock_runtime/README.md) also remains intentionally V2-shaped. It is not a publication or replica of the private V3 runtime.

## Disclosure Boundary

This folder publishes properties, architectural roles, and aggregate evidence. It does not publish V3 source, private test fixtures, raw schemas, private authorization, approval, or trust-boundary mechanisms, detailed adversarial probes, private prompts or operator internals, local paths, credentials, raw logs, traces, private configuration, or deployment internals.

That is the repository's **bounded technical disclosure** model.
