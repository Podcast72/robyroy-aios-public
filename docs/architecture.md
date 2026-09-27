# Architecture

AIOS is documented as a **governed agent runtime and execution layer**.

> **Models propose. AIOS governs. AIOS executes.**

The public narrative has evolved through these stages:

```text
AIOS V2 — Governed Execution Backbone
-> AIOS V3 P0 — Governed Agent Runtime
-> P1 — Governed Real Execution
-> P2.0 — Initial natural-language governed interaction
-> P2.1–P2.7 — Accepted in declared scopes
-> R2.7 — Closed; Core FROZEN / AGENT-READY
```

P0 and P1 completed in their declared scopes. P2.0–P2.7 were accepted in declared scopes; R2.7 remediation and closeout completed. The next phase is provider-neutral Agent Integration Architecture, with OpenAI as the first planned external agent integration. That integration is not yet implemented.

## Current V3 Architecture

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

- `AgentLoop` coordinates work but does not own execution authority.
- Model calls and tool calls traverse the governed execution backbone.
- Governed READ and bounded governed WRITE are separately admitted and scope-bound.
- Explicit approval is required where the governed action requires it.
- `ModelPort` keeps model/provider concerns separate from execution authority.
- `ExecutionEngine` remains the execution authority.
- `ResultGate` controls outward result release.
- Conversation/session state remains separate from authoritative execution truth.

A model proposal is input to the governed runtime. It is not authorization.

## Governed Runtime Properties

The public architecture describes these properties without exposing their private mechanisms:

- retry and recovery fail closed;
- `UNKNOWN_EFFECT` prevents blind automatic re-execution when an effect may have occurred;
- terminal outcomes can be replayed from authoritative state within the verified scope;
- durable SQLite WRITE has been validated in a bounded declared scope;
- governed filesystem WRITE has been validated in a bounded declared scope;
- persistence and recovery claims do not establish distributed exactly-once semantics;
- executable identity, accounting, credential egress, content provenance, and result release remain governed.

The planned direction is `Governed Core -> provider-neutral agent integration boundary -> external agent systems`. Future external agents cannot grant themselves execution authority; AIOS / `ExecutionEngine` remains authoritative.

## Historical V2 Public Backbone

The canonical V2 public reference path remains:

```text
request -> planner -> execution_engine -> tool_registry -> runtime_guard -> tool -> result_gate -> result
```

That path remains valid for the V2 public mock runtime, curated examples, and public invariant tests. V3 extends the governing model; it does not relabel the V2 artifacts.

## Public Scope

This repository publishes architectural roles, properties, aggregate evidence, and limits. It does not publish private V3 source, schemas, authorization or approval mechanisms, trust-boundary internals, test fixtures, probes, prompts, local paths, credentials, raw logs or traces, configuration, or deployment wiring.

See [AIOS V3 Architecture](public/aios-v3/AIOS_V3_ARCHITECTURE.md), [Current Evidence](public/aios-v3/AIOS_V3_CURRENT_EVIDENCE.md), and [Public vs Private Boundary](public-vs-private-boundary.md).
