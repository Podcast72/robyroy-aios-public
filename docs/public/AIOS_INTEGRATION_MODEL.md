# AIOS Integration Model

AIOS is designed to sit between model or agent intent and operational execution. P0 and P1 completed in declared scopes, P2.0–P2.7 were accepted in declared scopes, and R2.7 closeout completed. **P2.7 / R2.7 remains FROZEN and AGENT-READY; P3 native multi-agent is accepted in its declared scope above that baseline.**

> **Models/agents propose. AIOS governs. AIOS executes admitted actions. AIOS verifies the observed effect.**

AIOS does not replace an AI model, agent framework, business application, identity system, or protected infrastructure. It provides the governed runtime path through which model calls and tool calls are admitted, executed, persisted, and result-gated.

## Current V3 Integration Shape

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

The `AgentLoop` coordinates work but does not own execution authority. The provider-neutral `ModelPort` keeps model/provider concerns separate from execution authority, while `GovernedModelPort` routes model work through `ExecutionEngine`. Governed READ and bounded governed WRITE cross the same authority boundary as separately admitted capabilities.

## Next Agent Integration Direction

```text
Governed Core -> provider-neutral agent integration boundary -> external agent systems
```

OpenAI is the first validated model provider, not an OpenAI Agents SDK integration; that SDK remains unimplemented. A Hermes decision artifact was used experimentally to propose one action while AIOS retained execution authority. A production Hermes adapter remains unimplemented. This integration model is separate from the proposed Restack open kernel.

The public diagram does not define a private API, payload schema, deployment topology, or implementation recipe.

## Experimental external decision source

```text
DIRECT:   Hermes -> native tool authority -> filesystem effect
GOVERNED: Hermes -> proposed decision -> AIOS admission/execution
        -> effect observation -> ResultGate
```

The [bounded Hermes pilots](aios-v3/AIOS_V3_POST_CORE_EVIDENCE.md#4-hermes-direct-and-governed-experiments) support this authority separation. They do not demonstrate a production Hermes connection. P3 native multi-agent orchestration is a separate AIOS capability.

## Illustrative Natural-Language Integration

The public integration pattern connects natural-language interpretation to a governed READ and one bounded action proposal, with explicit approval where required, governed execution, result gating, and a final response. The canonical [illustrative public flow](aios-v3/AIOS_V3_ARCHITECTURE.md#illustrative-public-flow) is documented in the V3 architecture. It is not a replica of the private runtime.

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

This list describes integration categories, not validated support for every system. Each integration still needs its own identity, permission, policy, infrastructure, and threat-model review.

## Example Integration Scenarios

### Enterprise assistant using a model and internal API

The agent loop may request inference to interpret a task, then propose an internal API call. Both calls remain governed work. The provider response does not grant authority for the API call; `ExecutionEngine` admits each governed action separately.

### Coding agent modifying files or running tests

A coding agent may propose edits or commands. AIOS can keep path scope, capability, budget, approval, execution identity, result release, and audit inside the governed runtime rather than relying only on model instructions. This is an architectural scenario, not a claim that arbitrary coding-agent writes are validated.

### Support agent updating tickets

The agent can propose a ticket change, but the proposal does not become an update until the governed path admits the action and obtains applicable approval. Conversation state remains separate from the authoritative execution record.

### Data agent querying protected data

A model can propose a query or analyze results while credential egress and content provenance remain governed. `ResultGate` can prevent an otherwise successful call from releasing material that should not leave the boundary.

### Workflow agent resuming after interruption

The agent loop can reopen or resume from persisted state. The runtime uses authoritative execution truth to replay terminal outcomes or stop uncertain effects. This posture avoids blind re-execution within the verified scope; it does not establish distributed exactly-once semantics.

## Validated Real-Execution Scope

P1 public-safe evidence includes:

- governed READ in an admitted scope;
- bounded governed WRITE with applicable authority and approval requirements;
- durable SQLite WRITE in its declared scope;
- one real OpenAI `gpt-5.6-sol` end-to-end pilot;
- a focused pilot gate reporting **10/10 tests PASS**.

In the pilot, the model read allowed state, selected one bounded WRITE, requested explicit approval, and completed through `ExecutionEngine` and governed persistence, trace, controlled execution-context, and result-release boundaries.

This is one observed path. It is not a provider reliability, availability, latency, cost, scale, or security benchmark.

## Execution And Recovery Boundary

An integration must not treat agent intent or conversation state as execution truth.

Within the applicable verified scopes:

- `ExecutionEngine` remains authoritative;
- capabilities remain explicitly admitted and bounded;
- terminal results can be replayed from authoritative state rather than re-executed;
- retry/recovery fail closed;
- `UNKNOWN_EFFECT` blocks blind re-execution when an effect may have occurred;
- durable persistence claims remain tied to the tested identity and storage assumptions.

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
- protected infrastructure and network controls;
- logging, monitoring, and incident response;
- legal, compliance, or domain review;
- environment-specific validation;
- reconciliation for `UNKNOWN_EFFECT`;
- human approval where policy requires it.

## Public Status

P0 and P1 completed in declared scopes; P2.0–P2.7 and R2.7 closed in their scopes. P3 native multi-agent is accepted in its declared scope. The historical P2.7/R2.7 full gate was **2510 passed, 1 skipped, 11350 subtests passed** and its targeted closeout was **5 passed**; the separate P3 `tests_v3` gate was **1753 passed, 1 skipped, 1209 subtests passed**. No unrestricted deployment capability is claimed.

The private runtime source and integration internals are not distributed here. Public materials support architecture review and bounded technical evaluation, not deployment from this repository alone.
