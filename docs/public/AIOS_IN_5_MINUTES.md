# AIOS in 5 Minutes

## 1. What AIOS is now

AIOS is a governed agent runtime and execution layer. V3 P0 and P1 completed in declared scopes, P2.0–P2.7 were accepted in declared scopes, and R2.7 closeout completed. **P2.7 / R2.7 is FROZEN; the governed Core is AGENT-READY.**

> **Models propose. AIOS governs. AIOS executes.**

The model can propose the next step and the `AgentLoop` can coordinate a run, but neither owns execution authority. Model calls, READ capabilities, and bounded WRITE capabilities cross the governed execution backbone, with `ExecutionEngine` remaining authoritative.

This repository publishes a bounded technical disclosure of that architecture and evidence. It preserves the earlier V2 public demonstrations but does not publish the private V3 runtime.

## 2. The evolution

```text
AIOS V2 — Governed Execution Backbone
-> AIOS V3 P0 — Governed Agent Runtime
-> P1 — Governed Real Execution
-> P2.0 — Initial natural-language governed interaction
-> P2.1–P2.7 — Accepted in declared scopes
-> R2.7 — Closed; Core FROZEN / AGENT-READY
```

V2 made the governed tool-execution path explicit and publicly testable. P0 carried that principle into the agent loop and model-provider path. P1 validated governed READ, bounded governed WRITE, and durable SQLite WRITE in successive declared scopes.

The next engineering phase is a provider-neutral Agent Integration Architecture, with OpenAI as the first planned external agent integration. That integration is not yet implemented.

## 3. The problem

A model that only returns text can still be wrong. A model or agent that can call providers, tools, files, APIs, databases, or workflows can create effects before a human reviews the final answer.

Direct model-to-tool execution can blur proposal, authorization, approval, execution, state, and result release. AIOS separates them so the model's proposal remains non-authoritative and execution stays governed.

## 4. Current V3 path

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

| Stage | Public meaning |
| --- | --- |
| `User` | Supplies the request and receives the final answer. |
| `AgentLoop` | Coordinates the interaction without owning execution authority. |
| `ModelPort / GovernedModelPort` | Keeps the provider replaceable and inference on the governed path. |
| `ExecutionEngine` | Admits and executes governed model or tool work. |
| Governed execution | Performs only admitted work with applicable authority and approval. |
| `RunStore / ResultGate / audit` | Preserves execution truth, controls release, and keeps evidence reviewable. |

This diagram is deliberately architectural. Private data structures and mechanisms are not disclosed.

## 5. Pilot flow summary

One observed OpenAI `gpt-5.6-sol` pilot connected natural-language interpretation, a governed READ, one bounded WRITE proposal, explicit approval, governed execution, result gating, and a final response. The canonical [illustrative public flow](aios-v3/AIOS_V3_ARCHITECTURE.md#illustrative-public-flow) is documented in the V3 architecture and is not a replica of the private runtime.

## 6. Core properties

- models propose; proposals do not self-authorize;
- conversation/session state is separate from authoritative execution truth;
- READ and WRITE capabilities remain independently admitted and scope-bound;
- approval is explicit where the governed action requires it;
- retry and recovery fail closed;
- `UNKNOWN_EFFECT` blocks blind automatic re-execution;
- terminal work can be replayed from authoritative state rather than executed again;
- `ResultGate` controls outward release;
- persistence claims remain limited to their verified identity and persistence scopes.

## 7. Current evidence

| Evidence | Result |
| --- | --- |
| V3 P0 foundation | Completed in its declared scope |
| P1 governed real execution | Completed in its declared scope |
| P2.0 initial governed interaction | Implemented and validated in its declared scope |
| P2.1–P2.7 and R2.7 | Accepted in declared scopes; remediation and closeout completed |
| Governed READ | Validated |
| Bounded governed WRITE | Validated |
| Durable SQLite WRITE | Validated in its declared scope |
| Governed filesystem WRITE | Validated in its bounded declared scope |
| Real-provider pilot | One governed OpenAI `gpt-5.6-sol` pilot completed |
| Latest recorded full private regression | **2510 passed, 1 skipped, 11350 subtests passed** |
| Targeted P2.7/R2.7 closeout retest | **5 passed** |

The full regression preceded the final documentation-only closeout and was not rerun for documentation changes. The targeted retests covered relevant filesystem ambiguity/recovery and result-exposure properties at an aggregate level.

The historical pilot passed through `ExecutionEngine` and governed persistence, trace, controlled execution-context, and result-release boundaries. That is one observed governed path, not a benchmark, certification, or unrestricted production-readiness claim. It is separate from the planned external OpenAI Agent integration.

## 8. Synthetic and real evidence

Synthetic evidence isolates invariants, state handling, and failure posture under controlled conditions. Real end-to-end evidence adds an observed provider, allowed state, explicit approval, and a bounded durable action in one path.

The two evidence types answer different questions. Neither establishes universal behavior beyond its declared scope.

## 9. Historical V2 public surface

The V2 reference path remains:

```text
request -> planner -> execution_engine -> tool_registry -> runtime_guard -> tool -> result_gate -> result
```

The public mock runtime demonstrates V2-shaped `ALLOW`, `WARN`, and `BLOCK` behavior. The V2 package also preserves public proof tests, ANDY field-test results, and scoped at-most-once evidence. Those artifacts do not publish or reproduce V3.

## 10. Public, private, and claim limits

Public material includes V3 architecture, properties, status, limits, aggregate evidence, and preserved V2 demonstrations.

Private material includes V3 source, private tests and fixtures, raw schemas, logs, traces, audit records, prompts, credentials, configuration, authorization and approval internals, trust-boundary mechanisms, probes, and deployment wiring.

The evidence does not establish security certification, formal verification, universal provider support, arbitrary capability access, distributed exactly-once execution, or validation across every environment.

Start with the [V3 public index](aios-v3/README.md), review the [current evidence](aios-v3/AIOS_V3_CURRENT_EVIDENCE.md), then read the [architecture](aios-v3/AIOS_V3_ARCHITECTURE.md) and [status limits](aios-v3/AIOS_V3_STATUS_AND_LIMITS.md).
