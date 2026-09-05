# AIOS V3 Architecture

AIOS V3 P0 is a governed agent runtime in which the model can propose work but cannot grant itself execution authority.

> **Models propose. AIOS governs. AIOS executes.**

## Current P0 Flow

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

This is an architectural disclosure. It intentionally omits private class relationships, schemas, protocol payloads, authorization, approval, and trust-boundary mechanisms, configuration, and deployment wiring.

## Component Roles

| Component | Public role | Authority boundary |
| --- | --- | --- |
| `User` | Supplies the request and receives the final answer. | Does not directly invoke a private runtime capability through this public model. |
| `AgentLoop` | Coordinates turns, requests inference or tool work, and builds the final answer. | Does not possess execution authority and cannot make a proposal self-authorizing. |
| `ModelPort` | Defines the provider-neutral model boundary. | Keeps provider selection separate from runtime authority. |
| `GovernedModelPort` | Routes model work through the governed execution path. | Does not bypass `ExecutionEngine` for provider calls. |
| `ExecutionEngine` | Admits and executes governed model or tool work. | Remains the execution authority. |
| Governed model or tool execution | Performs the admitted capability. | Runs only after the governed path accepts the work. |
| `RunStore` | Holds authoritative execution truth for governed runs. | Is separate from conversation/checkpoint state. Raw schema is private. |
| `ResultGate` | Controls release of governed results. | A successful underlying call does not by itself authorize outward release. |
| Audit | Preserves reviewable execution evidence. | Public docs expose aggregate properties, not raw audit records or trace payloads. |

## One Authority Path For Model And Tool Calls

V3 extends governance to both sides of the agent loop:

- a model call is governed work;
- a tool call is governed work;
- neither call becomes authoritative merely because the `AgentLoop` requested it;
- `ExecutionEngine` remains the common execution authority;
- resulting state and outward content remain subject to the runtime's governed boundaries.

The public architecture does not expose private action formats or adapter wiring.

## Provider-Neutral Model Boundary

`ModelPort` makes the provider replaceable without making the provider the source of execution authority. `GovernedModelPort` places inference on the governed path. OpenAI is the first real provider validated through this boundary; `gpt-5.6-sol` is the exact model validated for the published live evidence.

This is not a claim that all model providers are implemented, equivalent, or certified.

## State And Execution Truth

Conversation state answers questions such as what the agent has seen and where a turn can continue. Execution truth answers questions such as whether governed work was admitted, started, completed, failed, or became uncertain.

V3 keeps those concerns separate. Conversation or checkpoint state cannot silently rewrite authoritative execution history, and replay/resume decisions are based on governed execution truth rather than conversational intent alone.

No raw persistence schema is published here.

## Fail-Closed Retry And Recovery

Retry and recovery remain conservative:

- a safely retryable condition must be established by the governed runtime;
- terminal work is replayed from authoritative state rather than executed again;
- if an external effect may have occurred but cannot be proven, the run converges to `UNKNOWN_EFFECT`;
- `UNKNOWN_EFFECT` blocks blind automatic re-execution and requires reconciliation.

The published persistence/reopen/resume result applies only to the verified synthetic P0 scope. It is not a distributed exactly-once claim.

## Identity, Accounting, Egress, And Provenance

At the public architecture level, V3 P0 binds these properties to the governed path:

- executable and artifact identity;
- authoritative budget accounting;
- credential egress decisions;
- content provenance;
- run persistence and result release.

These are public properties, not a disclosure of private validation logic or enforcement mechanisms.

## Composition Root

The Composition Root assembles the P0 components and their allowed dependencies. Its public significance is architectural: the runtime is composed so that the `AgentLoop`, model provider, and tools do not acquire an alternate execution-authority path.

The Composition Root's code, configuration, dependency construction, and trust-boundary details remain private.

## Relationship To V2

The V2 public backbone remains the historical public demonstration:

```text
request -> planner -> execution_engine -> tool_registry -> runtime_guard -> tool -> result_gate -> result
```

The V3 diagram does not retroactively redefine V2 proof artifacts. It shows how the current P0 carries governed execution into the agent loop and model-provider path.
