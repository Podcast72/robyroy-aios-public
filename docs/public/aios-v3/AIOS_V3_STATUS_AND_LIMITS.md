# AIOS V3 Status And Limits

## Current Status

AIOS V3 P0 is complete in its declared validation scope.

```text
AIOS_V3_P0_GATE=PASS
```

The current public description is **AIOS V3 P0 — Governed Agent Runtime**.

> **Models propose. AIOS governs. AIOS executes.**

| Area | Public status |
| --- | --- |
| Agent runtime | P0 completed in the declared private validation scope |
| Execution authority | `ExecutionEngine` remains authoritative |
| Agent loop | Coordinates work; does not own execution authority |
| Model path | Governed through provider-neutral `ModelPort` / `GovernedModelPort` |
| Tool path | Governed through the execution backbone |
| State model | Conversation state and execution truth remain separate |
| Recovery | Fail-closed; `UNKNOWN_EFFECT` blocks blind re-execution |
| Persistence | Reopen/replay/resume verified in the synthetic P0 scope |
| Test evidence | 562/562 targeted P0 tests PASS |
| Adversarial gate | 354/354 PASS |
| Real provider | OpenAI, exact model `gpt-5.6-sol` |
| Live evidence | One governed invocation returned `AIOS_LIVE_OK` |
| Public distribution | Documentation and minimal V2 demonstrations only; private V3 runtime not distributed |

## Current Claim Boundary

The P0 evidence supports an engineering milestone claim, not an assurance claim. `PASS`, `verified`, and `completed` refer to the specifically named gate or tested scope.

The public material may state that:

- the targeted P0 and adversarial gates passed;
- governed model/tool round-trip and synthetic persistence/reopen/resume were verified;
- the provider-neutral model boundary was exercised with a real OpenAI provider;
- one `gpt-5.6-sol` invocation completed through the governed path with no fallback, no retry, and no observed raw-secret leak.

## Limits And Non-Claims

This public status does not claim:

- production readiness or release readiness for unrestricted deployment;
- security certification, penetration-test certification, or formal verification;
- that all providers, tools, integrations, or environments are supported;
- that every possible failure, bypass, or adversarial condition has been eliminated;
- distributed exactly-once behavior or independent multi-host correctness;
- correctness after loss or corruption of authoritative persistence;
- that no secret could ever leak under a different configuration or threat model;
- that the public mock runtime is the private V3 runtime.

## Scope Of Persistence Evidence

Persistence, reopen, replay, and resume were verified within the synthetic P0 boundary. The claim is limited to the tested execution identity and authoritative persistence assumptions.

If an effect may have occurred but the runtime cannot establish the outcome, `UNKNOWN_EFFECT` prevents blind automatic re-execution. Reconciliation is required. This conservative terminal state is a safety property, not a guarantee that the unknown external outcome can always be reconstructed.

## Provider Limit

`ModelPort` is provider-neutral as an architectural boundary. OpenAI is the first real provider validated, with exact model `gpt-5.6-sol`. This does not imply validated parity across other providers or models.

The single live invocation is evidence of one successful governed path, not a latency, scale, availability, cost, or reliability benchmark.

## Public/Private Boundary

The public repository follows **bounded technical disclosure**. It publishes architectural roles, properties, limits, and aggregate evidence. It does not publish the private V3 runtime or the mechanisms that would allow the public documents to become a replica of it.

For the complete disclosure policy, see [Public vs Private Boundary](../../public-vs-private-boundary.md).

## Historical V2 Evidence

AIOS V2 documentation, public demonstrations, public proof tests, ANDY field tests, and at-most-once evidence remain available as historical evidence for the governed execution backbone milestone. V3 adds the governed agent runtime; it does not erase the V2 record.
