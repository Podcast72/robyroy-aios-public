# AIOS in 5 Minutes

## 1. What AIOS is now

AIOS is a governed agent runtime and execution layer. V3 P0 and P1 completed in declared scopes, P2.0–P2.7 were accepted in declared scopes, and R2.7 closeout completed. **P2.7 / R2.7 remains FROZEN and AGENT-READY; P3 native multi-agent, EA-0A admission, and EA-0B external-host governance are accepted in their declared scopes above that baseline.**

> **Models/agents propose. AIOS governs. AIOS executes admitted actions. AIOS verifies the observed effect.**

The model can propose the next step and the native `AgentLoop` can coordinate sequential roles, but neither owns execution authority. Model calls, READ capabilities, and bounded WRITE capabilities cross the governed execution backbone, with `ExecutionEngine` remaining authoritative.

This repository publishes a bounded technical disclosure of that architecture and evidence. It preserves the earlier V2 public demonstrations but does not publish the private V3 runtime.

## 2. The evolution

```text
AIOS V2 — Governed Execution Backbone
-> AIOS V3 P0 — Governed Agent Runtime
-> P1 — Governed Real Execution
-> P2.0 — Initial natural-language governed interaction
-> P2.1–P2.7 — Accepted in declared scopes
-> R2.7 — Closed; Core FROZEN / AGENT-READY
-> P3 — Native multi-agent ACCEPTED in its declared scope
-> EA-0A — Governed preformed proposal admission ACCEPTED
-> EA-0B — External-host governance READ/WRITE and tested OS isolation ACCEPTED
```

V2 made the governed tool-execution path explicit and publicly testable. P0 carried that principle into the agent loop and model-provider path. P1 validated governed READ, bounded governed WRITE, and durable SQLite WRITE in successive declared scopes.

P3 implemented native sequential multi-agent orchestration within AIOS. OpenAI is a validated model provider, while OpenAI Agents SDK remains unimplemented. An experimental Hermes decision source was tested separately; it is not a production integration. EA-0B separately lets an external process propose bounded READ/WRITE through AIOS while AIOS retains approval, execution, replay, recovery, and result authority. In a tested macOS two-principal configuration, direct host access to the protected AIOS resources covered by the pilot was denied. See [External Host Evidence](aios-v3/AIOS_V3_EXTERNAL_HOST_EVIDENCE.md).

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

### Practical components

| Component | What it does |
| --- | --- |
| `GovernedActionPort` | Carries agent intent to the governed action boundary. |
| `ExecutionEngine` / ExecutionAuthority | AIOS admits and executes the action; model text grants no authority. |
| Policy | Defines what is allowed for the configured run. |
| Capability | Defines the admitted action surface. |
| Budget | Limits admitted model, tool, and action work. |
| Approval | Holds sensitive work pending authorization where required. |
| Approval one-shot | Consumes the grant only for its admitted binding. |
| `TrustPlane` | Keeps host-owned authority separate from agent claims. |
| `RunStore` | Preserves authoritative execution truth. |
| Effect observation | Checks the real effect within the validated capability scope. |
| `ResultGate` | Prevents an unverified result from being released as success. |
| Recovery / reconciliation | Treats uncertain effects conservatively. |
| Replay safety | Avoids blind duplicate execution in validated scopes. |
| Session / checkpoint | Supports bounded pause, resume, and recovery. |
| Native multi-agent | Coordinates specialists under the same governed authority and root budget. |

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
| Historical P2.7/R2.7 full private regression | **2510 passed, 1 skipped, 11350 subtests passed** |
| Targeted P2.7/R2.7 closeout retest | **5 passed** |
| P3 native multi-agent pilot | One governed effect in a sequential specialist run |
| P3 `tests_v3` gate | **1753 passed, 1 skipped, 1209 subtests passed** |
| EA-0A preformed proposal admission | Accepted with zero inference and AIOS authority retained |
| EA-0B external READ/WRITE and tested OS isolation | Accepted in declared scopes |
| EA-0B Slice 3 canonical full-repository gate | **2,888 collected, 2,887 passed, 1 skipped, 0 failed/errors, 12,407 subtests passed** |

The P2.7/R2.7 full regression preceded its documentation-only closeout. The separate P3 `tests_v3` gate reported **1753 passed, 1 skipped, 1209 subtests passed** after its live pilot; the two scopes must not be combined.

The historical pilot passed through `ExecutionEngine` and governed result-release boundaries. The later P3 multi-agent pilot used the same governance for sequential specialist roles. Neither pilot is a benchmark, certification, or unrestricted production-readiness claim.

## 8. Synthetic and real evidence

Synthetic evidence isolates invariants, state handling, and failure posture under controlled conditions. Real end-to-end evidence adds an observed provider, allowed state, explicit approval, and a bounded durable action in one path.

The two evidence types answer different questions. Neither establishes universal behavior beyond its declared scope.

## 9. Post-core experiments and limits

The [Post-Core Evidence](aios-v3/AIOS_V3_POST_CORE_EVIDENCE.md) summarizes the external read-only Hermes/DeepSeek review, remediation, P3 live multi-agent pilot, and the Hermes direct-versus-governed experiments. The Hermes decision-source adapter is experimental; OpenAI Agents SDK is not implemented. EA-0B is a vendor-neutral boundary, not a ready-made vendor adapter or security certification.

## 10. Historical V2 public surface

The V2 reference path remains:

```text
request -> planner -> execution_engine -> tool_registry -> runtime_guard -> tool -> result_gate -> result
```

The public mock runtime demonstrates V2-shaped `ALLOW`, `WARN`, and `BLOCK` behavior. The V2 package also preserves public proof tests, ANDY field-test results, and scoped at-most-once evidence. Those artifacts do not publish or reproduce V3.

## 11. Public, private, and claim limits

Public material includes V3 architecture, properties, status, limits, aggregate evidence, and preserved V2 demonstrations.

Private material includes V3 source, private tests and fixtures, raw schemas, logs, traces, audit records, prompts, credentials, configuration, authorization and approval internals, trust-boundary mechanisms, probes, and deployment wiring.

The evidence does not establish security certification, formal verification, universal provider support, arbitrary capability access, distributed exactly-once execution, or validation across every environment.

Start with the [V3 public index](aios-v3/README.md), review the [current evidence](aios-v3/AIOS_V3_CURRENT_EVIDENCE.md), then read the [architecture](aios-v3/AIOS_V3_ARCHITECTURE.md) and [status limits](aios-v3/AIOS_V3_STATUS_AND_LIMITS.md).
