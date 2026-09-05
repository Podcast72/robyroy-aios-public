# AIOS Integration Model

AIOS V3 P0 is designed to sit between model or agent intent and operational execution.

> **Models propose. AIOS governs. AIOS executes.**

AIOS does not replace an AI model, agent framework, business application, identity system, or secure infrastructure. It provides the governed runtime path through which model calls and tool calls are admitted, executed, persisted, and result-gated.

## Current V3 P0 Integration Shape

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

The `AgentLoop` coordinates work but does not own execution authority. The provider-neutral `ModelPort` keeps a model provider replaceable, while `GovernedModelPort` routes model work through `ExecutionEngine`. Tool work crosses the same governed authority boundary.

The public diagram does not define a private API, payload schema, deployment topology, or implementation recipe.

## Where AIOS Can Sit

AIOS can govern agent work involving:

- model-provider inference;
- internal or external APIs;
- databases and data services;
- file systems and document pipelines;
- ticketing, CRM, or ERP systems;
- local tools and scripts;
- workflow automation;
- sensitive output channels.

Each integration still needs its own identity, permission, policy, infrastructure, and threat-model review.

## Example Integration Scenarios

### Enterprise assistant using a model and internal API

The agent loop may request inference to interpret a task, then propose an internal API call. Both the model call and the tool call remain governed work. The provider response does not grant authority for the API call; `ExecutionEngine` admits each governed action separately.

### Coding agent modifying files or running tests

A coding agent may propose edits or commands. AIOS can keep path scope, capability, budget, approval, execution identity, result release, and audit inside the governed runtime rather than relying only on model instructions.

### Support agent updating tickets

The agent can propose a ticket change, but the proposal does not become an update until the governed path admits the tool action. Conversation state remains separate from the authoritative execution record.

### Data agent querying protected data

A model can propose a query or analyze results while credential egress and content provenance remain governed. ResultGate can prevent an otherwise successful call from releasing material that should not leave the boundary.

### Workflow agent resuming after interruption

The agent loop can reopen or resume from persisted state. The runtime uses authoritative execution truth to replay terminal outcomes or stop uncertain effects, avoiding blind duplicate execution in the verified P0 scope.

## Model Provider Integration

`ModelPort` is provider-neutral by design. OpenAI is the first real provider validated through the governed path, using exact model `gpt-5.6-sol`.

A single live invocation returned `AIOS_LIVE_OK` with RunStore `SUCCEEDED`, ResultGate `ALLOW`, `model_calls=1`, `tool_calls=0`, `network_calls=1`, and `retries=0`. No fallback, retry, or raw-secret leak was observed.

This is a one-invocation path validation. It is not a provider reliability, availability, latency, cost, or security benchmark.

## Execution And Recovery Boundary

An integration must not treat agent intent or conversation state as execution truth.

Within the verified P0 scope:

- `ExecutionEngine` remains authoritative;
- executable and artifact identity are tied to the governed path;
- budget accounting is authoritative;
- terminal results are replayed rather than re-executed;
- retry/recovery fail closed;
- `UNKNOWN_EFFECT` blocks blind re-execution when an effect may have occurred;
- persistence, reopen, and resume avoid duplicate execution under the tested assumptions.

The public documentation does not claim distributed exactly-once semantics or independent multi-host correctness.

## Historical V2 Integration Model

The preserved V2 public surface demonstrates this tool-oriented backbone:

```text
request -> planner -> execution_engine -> tool_registry -> runtime_guard -> tool -> result_gate -> result
```

Its public mock runtime, examples, and field tests remain valid historical evidence. They are minimal demonstrations of the previous governed-backbone model, not the private V3 runtime.

## What AIOS Does Not Replace

AIOS does not replace:

- model-provider safeguards;
- identity and access management;
- secure infrastructure and network controls;
- logging, monitoring, and incident response;
- legal, compliance, or domain review;
- environment-specific validation;
- reconciliation for `UNKNOWN_EFFECT`;
- human approval where policy requires it.

## Public Status

The V3 P0 milestone has `AIOS_V3_P0_GATE=PASS`, with **562/562 targeted P0 tests PASS** and the Adversarial Remediation Gate at **354/354 PASS**.

The private runtime source and integration internals are not distributed here. Public materials support architecture review and bounded technical evaluation, not deployment from this repository alone.
