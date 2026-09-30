# AIOS V3 Architecture

AIOS V3 is a governed agent runtime in which the model can propose work but cannot grant itself execution authority. P0 and P1 completed in declared scopes; P2.0–P2.7 were accepted in declared scopes; R2.7 closeout completed. **P2.7 / R2.7 remains FROZEN and AGENT-READY; P3 native multi-agent, EA-0A admission, and EA-0B external-host governance are accepted in their declared scopes above that baseline.**

> **Models/agents propose. AIOS governs. AIOS executes admitted actions. AIOS verifies the observed effect.**

## Current High-Level Flow

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
| External Host Boundary | Admits a bounded proposal from another process and exposes observational status. | Host claims and provenance do not grant AIOS authority. |
| `AgentLoop` | Coordinates turns, requests inference or tool work, and builds the final answer. | Does not possess execution authority and cannot make a proposal self-authorizing. |
| `ModelPort` | Defines the provider-neutral model boundary. | Keeps provider selection separate from runtime authority. |
| `GovernedModelPort` | Routes model work through the governed execution path. | Does not bypass `ExecutionEngine` for provider calls. |
| `ExecutionEngine` | Admits and executes governed model or tool work. | Remains the execution authority. |
| Governed model or tool execution | Performs the admitted capability. | Runs only after the governed path accepts the work and applicable approval is present. |
| `RunStore` | Holds authoritative execution truth for governed runs. | Is separate from conversation/checkpoint state. Raw schema is private. |
| `ResultGate` | Controls release of governed results. | A successful underlying call does not by itself authorize outward release. |
| Audit | Preserves reviewable execution evidence. | Public docs expose aggregate properties, not raw audit records or trace payloads. |

## Illustrative Public Flow

The following is an **illustrative public flow**, not a replica, API contract, or reconstruction of the private runtime:

```text
Natural-language request
  -> model interpretation
  -> governed READ
  -> bounded action proposal
  -> explicit approval where required
  -> ExecutionEngine
  -> evidence / ResultGate
  -> final response
```

The observed pilot followed this shape for one allowed READ and one bounded WRITE. The implementation-specific action representation, approval binding, persistence schema, trace structure, and trust boundaries remain private.

## One Authority Path For Model And Tool Calls

V3 extends governance to both sides of the agent loop:

- a model call is governed work;
- a tool call is governed work;
- READ and WRITE capabilities remain separately admitted and scope-bound;
- neither call becomes authoritative merely because the `AgentLoop` requested it;
- `ExecutionEngine` remains the common execution authority;
- resulting state and outward content remain subject to the runtime's governed boundaries.

The public architecture does not expose private action formats or adapter wiring.

## Provider-Neutral Model Boundary

`ModelPort` keeps model/provider concerns separate from execution authority. `GovernedModelPort` places inference on the governed path. OpenAI is the first real model provider validated through this boundary; `gpt-5.6-sol` was used in the historical pilot evidence. Authority remains with AIOS / `ExecutionEngine`.

This is not a claim that all model providers are implemented, equivalent, or certified.

## External Agent Integration Boundary

The current public entry model is:

```text
Native AgentLoop / Multi-Agent → native proposal ─────────────┐
External Agent / Harness      → external proposal             │
                               ↓                             │
                       External Host Boundary                 │
                               └──────────────┬──────────────┘
                                              ↓
                                         Governed Core
                                              ↓
                                   ExecutionEngine / authority
                                              ↓
                                  observed effect / ResultGate
```

EA-0A admits an externally formed proposal as non-authoritative. EA-0B supplies the vendor-neutral external process boundary for governed READ and approval-bound WRITE. Host provenance does not create authority; approval, execution, replay/recovery, and outward result remain AIOS responsibilities. OpenAI is a validated model provider; OpenAI Agents SDK is **not implemented**. Earlier Hermes decision-source evidence is experimental, not a production adapter. Vendor-specific adapters and MCP integration remain future work. See [External Host Evidence](AIOS_V3_EXTERNAL_HOST_EVIDENCE.md). This is separate from the proposed Restack open kernel.

## Native multi-agent authority

P3 coordinates Coordinator, Analyst, Challenger, and Operator roles sequentially inside one AIOS `AgentLoop`, session, root run, and root budget. Delegation changes the active specialist and allowed task surface; it does not create a new authority principal. The bounded live pilot followed Coordinator → Analyst → Coordinator → Challenger → Coordinator → Operator → governed WRITE → Operator → Coordinator → final. [Post-Core Evidence](AIOS_V3_POST_CORE_EVIDENCE.md) records its gates and limits.

## State And Execution Truth

Conversation state answers questions such as what the agent has seen and where a turn can continue. Execution truth answers questions such as whether governed work was admitted, started, completed, failed, or became uncertain.

V3 keeps those concerns separate. Conversation or checkpoint state cannot silently rewrite authoritative execution history, and replay/resume decisions are based on governed execution truth rather than conversational intent alone.

No raw persistence or session schema is published here.

## Fail-Closed Retry And Recovery

Retry and recovery remain conservative:

- a safely retryable condition must be established by the governed runtime;
- terminal work is replayed from authoritative state rather than executed again;
- if an external effect may have occurred but cannot be proven, the run converges to `UNKNOWN_EFFECT`;
- `UNKNOWN_EFFECT` blocks blind automatic re-execution and requires reconciliation.

These statements apply only to the verified identity and persistence scopes. They do not establish distributed exactly-once semantics.

## P1 Real-Execution Boundary

P1 adds public-safe evidence for governed READ, bounded governed WRITE, and durable SQLite WRITE. These are capability claims, not implementation disclosures. Each remains limited to its admitted operation, approval posture, persistence assumptions, and observed scope.

The architecture does not claim arbitrary write access, universal transactional guarantees, or correctness across independent hosts.

P2.7 added governed filesystem WRITE in a bounded declared scope. R2.7 remediation and closeout completed. The public architectural claim is limited to governed admission, effect observation, fail-closed uncertainty, and controlled result exposure. It does not disclose private mechanisms or imply arbitrary filesystem WRITE.

## Identity, Accounting, Egress, And Provenance

At the public architecture level, V3 binds these properties to the governed path:

- executable and artifact identity;
- authoritative budget accounting;
- credential egress decisions;
- content provenance;
- run persistence and result release.

These are public properties, not a disclosure of private validation logic or enforcement mechanisms.

## Composition Root

The Composition Root assembles the governed runtime components and their allowed dependencies. Its public significance is architectural: the runtime is composed so that the `AgentLoop`, model provider, and tools do not acquire an alternate execution-authority path.

The Composition Root's code, configuration, dependency construction, and trust-boundary details remain private.

## Relationship To V2

The V2 public backbone remains the historical public demonstration:

```text
request -> planner -> execution_engine -> tool_registry -> runtime_guard -> tool -> result_gate -> result
```

The V3 diagrams do not retroactively redefine V2 proof artifacts. They show how the current V3 track carries governed execution into the agent loop, model-provider path, and bounded real-execution capabilities.
