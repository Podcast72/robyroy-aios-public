# Architecture

AIOS is currently documented as a **governed agent runtime and execution layer**.

> **Models propose. AIOS governs. AIOS executes.**

The architecture has evolved across two public milestones:

```text
AIOS V2 — Governed Execution Backbone
->
AIOS V3 P0 — Governed Agent Runtime
```

V3 does not erase V2. The V2 backbone, public demonstrations, field tests, and proof tests remain historical evidence for the earlier milestone.

## Current V3 P0 Architecture

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

This is a high-level authority and data-flow view, not a copy of the private implementation.

## Authority Boundaries

The architectural problem changes when an AI-assisted system can request inference, use tools, and produce operational effects. V3 makes the authority split explicit:

- `AgentLoop` coordinates work but does not own execution authority;
- model calls and tool calls traverse the governed execution backbone;
- `ModelPort` makes the model provider replaceable;
- `GovernedModelPort` keeps inference on the governed path;
- `ExecutionEngine` remains the execution authority;
- `ResultGate` controls outward result release;
- `RunStore` represents authoritative execution truth;
- conversation/checkpoint state remains separate from execution truth.

A model proposal is input to the governed runtime. It is not authorization.

## Governed Runtime Properties

The V3 P0 public architecture describes these properties without exposing their private mechanisms:

- retry and recovery fail closed;
- `UNKNOWN_EFFECT` prevents blind automatic re-execution when an effect may have occurred;
- executable and artifact identity are bound to the governed path;
- budget accounting is authoritative within the verified scope;
- credential egress and content provenance are governed;
- persistence, replay, reopen, and resume avoid duplicate execution in the verified synthetic P0 scope;
- a Composition Root assembles the runtime without giving the agent loop, provider, or tools an alternate authority path.

## Provider Boundary

`ModelPort` is provider-neutral. OpenAI is the first real provider validated through the governed path, and `gpt-5.6-sol` is the exact model used for the published live evidence.

Provider-neutral does not mean every provider has been implemented or validated. It describes the architectural boundary between provider integration and execution authority.

## Historical V2 Public Backbone

The canonical V2 public reference path remains:

```text
request -> planner -> execution_engine -> tool_registry -> runtime_guard -> tool -> result_gate -> result
```

That path remains valid for the V2 public mock runtime, curated examples, and public invariant tests. The V3 architecture extends the governing model to agent and model calls; it does not retroactively redefine those artifacts.

## Public Scope

This repository publishes architectural roles, properties, aggregate evidence, and limits. It does not publish private V3 source, schemas, authorization, approval, or trust-boundary mechanisms, test fixtures, adversarial probes, prompts, local paths, credentials, raw logs or traces, configuration, or deployment wiring.

See [AIOS V3 Architecture](public/aios-v3/AIOS_V3_ARCHITECTURE.md) and [Public vs Private Boundary](public-vs-private-boundary.md).
