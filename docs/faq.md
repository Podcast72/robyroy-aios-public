# FAQ

## What is AIOS now?

AIOS V3 P0 is a governed agent runtime and execution layer.

> **Models propose. AIOS governs. AIOS executes.**

The model can propose work and the `AgentLoop` can coordinate it, but `ExecutionEngine` remains the execution authority.

## What changed from V2 to V3?

AIOS V2 documented and demonstrated a governed tool-execution backbone. V3 P0 extends the same governing principle to the agent loop and model-call path, adds a provider-neutral `ModelPort`, and makes persistence, recovery, execution identity, accounting, egress, and provenance part of the governed runtime boundary.

## Is the V2 backbone still valid?

Yes, for the V2 public demonstration and historical evidence:

```text
request -> planner -> execution_engine -> tool_registry -> runtime_guard -> tool -> result_gate -> result
```

V2 documents, ANDY field tests, proof tests, and public examples remain preserved. They are not relabeled as V3.

## What is the current V3 P0 path?

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

## Is AIOS tied to OpenAI?

The architectural model boundary is provider-neutral through `ModelPort`. OpenAI is the first real provider validated, and `gpt-5.6-sol` is the exact model used for the published live evidence.

That does not mean every provider or model is already supported or validated.

## What V3 evidence is public?

The authorized aggregate evidence includes:

- AIOS V3 P0 completed;
- `AIOS_V3_P0_GATE=PASS`;
- **562/562 targeted P0 tests PASS**;
- Adversarial Remediation Gate: **354/354 PASS**;
- governed model/tool round-trip verified;
- persistence/reopen/resume verified in the synthetic P0 scope;
- one governed live OpenAI invocation returned `AIOS_LIVE_OK`.

## What happened in the live invocation?

The exact model was `gpt-5.6-sol`. The observed run reached RunStore `SUCCEEDED` and ResultGate `ALLOW`, with `model_calls=1`, `tool_calls=0`, `network_calls=1`, and `retries=0`. There was no fallback, no retry, and no raw-secret leak observed.

This is one path validation, not a benchmark or certification.

## What does UNKNOWN_EFFECT mean?

`UNKNOWN_EFFECT` means an external effect may have occurred but the runtime cannot authoritatively prove the outcome. The state blocks blind automatic re-execution and requires reconciliation.

It is a conservative recovery behavior, not a promise that every external outcome can be reconstructed.

## Is this repository the V3 runtime?

No. It is a public documentation and demonstration package. The private V3 runtime, private tests, schemas, mechanisms, and operational configuration are not published here.

## Why is the public mock still V2-shaped?

The mock is intentionally a small demonstration of the previous governed-backbone model. Keeping it small makes the public boundary honest. Expanding it into a V3 replica would violate the bounded technical disclosure model.

## Does P0 complete mean production-ready or security-certified?

No. P0 completion and PASS claims refer to the named validation scopes. They do not establish production readiness, formal verification, security certification, distributed exactly-once behavior, or validation in every environment.

## What does bounded technical disclosure mean?

It means the repository publishes architecture, properties, aggregate evidence, and limitations while withholding private source, tests, schemas, credentials, raw artifacts, and implementation-sensitive internals.
