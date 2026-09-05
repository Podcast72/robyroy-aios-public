# AIOS V3 P0 Evidence

This page publishes aggregate, public-safe evidence for the AIOS V3 P0 milestone. It does not publish private source, test fixtures, raw logs, traces, schemas, prompts, credentials, or configuration.

## P0 Gate

| Evidence | Public-safe result |
| --- | --- |
| Milestone | AIOS V3 P0 completed |
| P0 gate | `AIOS_V3_P0_GATE=PASS` |
| Targeted P0 tests | **562/562 PASS** |
| Adversarial Remediation Gate | **354/354 PASS** |
| Governed model/tool round-trip | Verified |
| Persistence/reopen/resume | Verified in the synthetic P0 scope |
| Provider boundary | Provider-neutral `ModelPort` |
| First real provider | OpenAI |
| Exact validated model | `gpt-5.6-sol` |

The test counts describe their named gate scopes. They are not presented as a combined unique-test total.

## Governed Round-Trip Evidence

The targeted P0 evidence supports the following bounded statement:

> In the verified P0 scope, the `AgentLoop` completed governed model/tool round trips without acquiring execution authority, while model and tool work remained routed through `ExecutionEngine` and governed persistence/result boundaries.

The synthetic P0 validation also covered persistence, reopen, replay, and resume behavior intended to avoid duplicate execution in the tested scope. This does not establish distributed exactly-once execution or behavior outside the tested identity and persistence boundary.

## Live Provider Evidence

One real OpenAI provider invocation was authorized and observed through the governed path.

| Signal | Observed result |
| --- | --- |
| Provider | OpenAI |
| Exact model | `gpt-5.6-sol` |
| Provider invocations | 1 |
| Response | `AIOS_LIVE_OK` |
| RunStore | `SUCCEEDED` |
| `model_calls` | `1` |
| `tool_calls` | `0` |
| `network_calls` | `1` |
| `retries` | `0` |
| ResultGate | `ALLOW` |
| Fallback | None |
| Retry | None |
| Raw-secret leak | None observed |

This proves only that the single observed invocation completed through the governed provider path with the listed outcome. It is not a reliability benchmark, provider certification, security certification, or evidence of broad production operation.

## What The Evidence Supports

- the V3 P0 gate completed for its declared target scope;
- the agent loop can use governed model and tool paths without owning execution authority;
- model-provider coupling is mediated by a provider-neutral port;
- authoritative execution state, result gating, and audit remain part of the governed round trip;
- fail-closed recovery and `UNKNOWN_EFFECT` prevent blind re-execution in the verified scope;
- a single live `gpt-5.6-sol` call completed without fallback or retry and without an observed raw-secret leak.

## What The Evidence Does Not Support

- security certification or formal verification;
- unrestricted production readiness;
- universal provider compatibility;
- universal prevention of duplicate effects;
- independent multi-host or distributed exactly-once guarantees;
- conclusions about deployments, configurations, or threat models outside the tested scope;
- disclosure of the private implementation from aggregate results.

## Evidence Boundary

The following remain private: V3 source, private test source and fixtures, raw `RunStore` schema, authorization, approval, and trust-boundary mechanisms, detailed exploit or adversarial probes, private prompts and operator internals, local paths, credentials, raw logs, traces, private configuration, and deployment internals.
