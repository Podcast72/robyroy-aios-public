# AIOS V3 P0 Overview

AIOS V3 P0 is a governed agent runtime built on the execution discipline established by AIOS V2.

> **Models propose. AIOS governs. AIOS executes.**

The P0 milestone moves AIOS from a governed execution backbone with public demonstrations to a private agent-runtime implementation whose public surface is limited to architecture, properties, and aggregate evidence.

## From V2 To V3

AIOS V2 established the public governed-backbone model:

```text
request -> planner -> execution_engine -> tool_registry -> runtime_guard -> tool -> result_gate -> result
```

AIOS V3 P0 retains that governing idea and extends it to the agent loop and model-call path. The historical V2 documentation is not superseded as evidence; it documents the earlier milestone and remains available under [`docs/public/aios-v2/`](../aios-v2/README.md).

The current V3 P0 architecture is described at a deliberately higher level:

```text
User
  -> AgentLoop
  -> ModelPort / GovernedModelPort
  -> ExecutionEngine
  -> governed model or tool execution
  -> RunStore / ResultGate / audit
  -> AgentLoop
  -> final answer
```

This diagram describes authority and data-flow boundaries, not private implementation structure.

## P0 Properties

| Property | Public description |
| --- | --- |
| Agent-loop authority | `AgentLoop` coordinates the run but does not possess execution authority. |
| Governed calls | Model calls and tool calls traverse the governed execution backbone. |
| Provider neutrality | `ModelPort` keeps the model provider replaceable at the runtime boundary. |
| Execution authority | `ExecutionEngine` remains the authority that admits and executes governed work. |
| State separation | Conversation/checkpoint state remains separate from authoritative execution truth. |
| Failure posture | Retry and recovery are fail-closed; uncertain effects do not trigger blind re-execution. |
| Uncertain effects | `UNKNOWN_EFFECT` is terminal for automatic retry and requires reconciliation. |
| Execution identity | Executable and artifact identity are bound to the governed path. |
| Accounting | Budget accounting is authoritative within the verified P0 scope. |
| Egress and provenance | Credential egress and content provenance are governed at the relevant boundaries. |
| Persistence | Persistence, replay, reopen, and resume avoid duplicate execution within the verified synthetic P0 scope. |
| Assembly | A Composition Root assembles the P0 without making private internals part of the public contract. |

## Provider Model

The runtime uses a provider-neutral `ModelPort`. OpenAI is the first real provider validated through that port, and the exact validated model is `gpt-5.6-sol`.

Provider-neutral does not mean that every provider is already implemented or validated. It means the runtime boundary does not make one provider the execution authority and is designed so a provider can be replaced behind the port without moving governance into the model.

## What P0 Completed Means

`P0 completed` means the declared V3 P0 gate passed for its targeted, synthetic validation scope. Publicly authorized aggregate evidence includes:

- `AIOS_V3_P0_GATE=PASS`;
- **562/562 targeted P0 tests PASS**;
- Adversarial Remediation Gate: **354/354 PASS**;
- governed model/tool round-trip verified;
- persistence, reopen, and resume verified in the synthetic P0 scope;
- one governed live OpenAI provider invocation completed successfully.

It does not mean security certification, formal verification, unrestricted production readiness, universal provider support, or validation across every deployment environment.

## Public Package

This repository provides a bounded technical disclosure:

- public V3 architecture and property descriptions;
- aggregate P0 evidence;
- explicit limits and non-claims;
- preserved V2 documentation, demos, proof tests, and field-test evidence.

It does not distribute the private V3 runtime.
