# FAQ

## What is AIOS now?

AIOS is a governed agent runtime and execution layer. V3 P0 and P1 completed in declared scopes, P2.0–P2.7 were accepted in declared scopes, and R2.7 closeout completed. **P2.7 / R2.7 remains FROZEN and AGENT-READY; P3 native multi-agent is accepted in its declared scope above that baseline.**

> **Models/agents propose. AIOS governs. AIOS executes admitted actions. AIOS verifies the observed effect.**

The model can propose work and the `AgentLoop` can coordinate it, but `ExecutionEngine` remains the execution authority.

## What changed from V2 through P1?

AIOS V2 documented and demonstrated a governed tool-execution backbone. V3 P0 extended the same governing principle to the agent loop and model-call path. P1 then validated governed READ, bounded governed WRITE, and durable SQLite WRITE in successive declared scopes.

## Is the V2 backbone still valid?

Yes, for the V2 public demonstration and historical evidence:

```text
request -> planner -> execution_engine -> tool_registry -> runtime_guard -> tool -> result_gate -> result
```

V2 documents, ANDY field tests, proof tests, and public examples remain preserved. They are not relabeled as V3.

## What is the current V3 path?

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

This is a public architecture view, not a private API or implementation map.

## Does AgentLoop execute model or tool calls directly?

No. `AgentLoop` coordinates the run but does not possess execution authority. Model calls and tool calls traverse the governed execution backbone.

## What real capabilities have been validated?

Public-safe aggregate evidence supports governed READ, bounded governed WRITE, durable SQLite WRITE, and governed filesystem WRITE in their declared scopes. It does not support unrestricted visibility, arbitrary mutation, or universal durability.

## Is AIOS tied to OpenAI?

The architectural model boundary is provider-neutral through `ModelPort`. OpenAI is the first real provider validated, and `gpt-5.6-sol` is the exact model used for the published pilot evidence.

P3 native multi-agent is implemented and accepted inside AIOS. OpenAI is the first validated model provider, while OpenAI Agents SDK is not implemented. Hermes supplied a decision in an experimental adapter pilot, not through a production integration; AIOS / `ExecutionEngine` retained execution authority.

## What happened in the end-to-end pilot?

One real `gpt-5.6-sol` pilot read allowed state, selected one bounded WRITE, requested explicit approval, executed through `ExecutionEngine`, traversed governed persistence, trace, controlled execution context, and result-release boundaries, and completed the end-to-end path. The focused pilot gate reported **10/10 tests PASS**.

This is one observed governed pilot, not a benchmark or certification.

## What is the P2 and P3 status?

P2.0–P2.7 were accepted in declared scopes. R2.7 remediation and closeout completed. The Core is frozen and agent-ready, which does not establish unrestricted deployment readiness. The historical P2.7/R2.7 full private regression was **2510 passed, 1 skipped, 11350 subtests passed**; targeted closeout retests were **5 passed**. The P2.7/R2.7 full regression preceded its documentation-only closeout. The separate later P3 `tests_v3` gate was **1753 passed, 1 skipped, 1209 subtests passed**. The suites have different scopes and are not additive.

## Is native multi-agent the same as OpenAI Agents SDK?

No. P3 uses AIOS native sequential specialist roles within one root run. It did not introduce the OpenAI Agents SDK or an external agent runtime. The P3 live pilot and `tests_v3` gate are documented in [Post-Core Evidence](public/aios-v3/AIOS_V3_POST_CORE_EVIDENCE.md).

## What did the Hermes experiments show?

The direct pilot let Hermes use its own tools to create an effect outside AIOS. In the governed experiments Hermes proposed a decision while AIOS admitted, executed, observed, and result-gated the effect. This is bounded experimental evidence, not production Hermes integration or certification.

## What does UNKNOWN_EFFECT mean?

`UNKNOWN_EFFECT` means an external effect may have occurred but the runtime cannot authoritatively prove the outcome. The state blocks blind automatic re-execution and requires reconciliation.

It is a conservative recovery posture, not a promise that every external outcome can be reconstructed.

## Is this repository the V3 runtime?

No. It is a public documentation and demonstration package. The private V3 runtime, private tests, schemas, mechanisms, and operational configuration are not published here.

## Why is the public mock still V2-shaped?

The mock is intentionally a small demonstration of the previous governed-backbone model. Expanding it into a V3 replica would violate the bounded technical disclosure model.

## Do completed milestones mean production-ready or security-certified?

No. P0, P1, and P2 milestone claims and PASS results refer to named scopes. They do not establish production readiness, formal verification, security certification, distributed exactly-once behavior, or validation in every environment.

## What does bounded technical disclosure mean?

It means the repository publishes architecture, properties, aggregate evidence, and limitations while withholding private source, tests, schemas, credentials, raw artifacts, and implementation-sensitive internals.
