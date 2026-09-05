# AIOS in 5 Minutes

## 1. What AIOS is now

AIOS V3 P0 is a governed agent runtime and execution layer.

> **Models propose. AIOS governs. AIOS executes.**

The model can propose the next step and the `AgentLoop` can coordinate the run, but neither owns execution authority. Model calls and tool calls cross the governed execution backbone, with `ExecutionEngine` remaining authoritative.

This repository publishes a bounded technical disclosure of that architecture and preserves the earlier V2 public demonstrations and evidence.

## 2. The evolution

```text
AIOS V2 — Governed Execution Backbone
->
AIOS V3 P0 — Governed Agent Runtime
```

V2 made the governed tool-execution path explicit and testable through a small public mock runtime, curated examples, proof tests, and ANDY field tests.

V3 P0 carries that principle into the agent loop and model-provider path. It adds a provider-neutral model boundary, governed model and tool round trips, authoritative execution persistence, fail-closed recovery, and Composition Root assembly.

V2 remains historical evidence. It is not relabeled as V3.

## 3. The problem

A model that only returns text can still be wrong. A model or agent that can call providers, tools, files, APIs, databases, or workflows can create effects before a human reviews the final answer.

Direct model-to-tool execution can blur proposal, authorization, execution, state, and result release. AIOS separates them so the model's proposal remains non-authoritative and execution stays governed.

## 4. Current V3 P0 path

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
| Governed execution | Performs only work accepted by the authority path. |
| `RunStore / ResultGate / audit` | Preserves execution truth, controls release, and keeps evidence reviewable. |
| `AgentLoop` | Continues from governed outcomes and produces the final answer. |

The diagram is deliberately architectural. Private data structures and mechanisms are not disclosed.

## 5. Core P0 properties

- conversation/checkpoint state is separate from authoritative execution truth;
- retry and recovery fail closed;
- `UNKNOWN_EFFECT` blocks blind automatic re-execution;
- terminal work is replayed rather than executed again;
- executable and artifact identity are bound to the governed path;
- budget accounting is authoritative in the verified scope;
- credential egress and content provenance are governed;
- persistence, reopen, replay, and resume avoid duplicate execution in the verified synthetic P0 scope;
- the Composition Root assembles P0 without becoming a public implementation contract.

## 6. Provider model

`ModelPort` is provider-neutral. OpenAI is the first real provider validated through it. The exact model used for the published live evidence is `gpt-5.6-sol`.

Provider-neutral describes the boundary, not universal provider support.

## 7. P0 evidence

| Evidence | Result |
| --- | --- |
| Milestone | AIOS V3 P0 completed |
| Gate | `AIOS_V3_P0_GATE=PASS` |
| Targeted P0 tests | **562/562 PASS** |
| Adversarial Remediation Gate | **354/354 PASS** |
| Governed model/tool round-trip | Verified |
| Persistence/reopen/resume | Verified in the synthetic P0 scope |
| Live provider path | One governed OpenAI invocation passed |

The live invocation used `gpt-5.6-sol`, returned `AIOS_LIVE_OK`, reached RunStore `SUCCEEDED`, and produced ResultGate `ALLOW`. Observed accounting was `model_calls=1`, `tool_calls=0`, `network_calls=1`, and `retries=0`. There was no fallback, no retry, and no raw-secret leak observed.

This is one governed live-path result, not a benchmark or certification.

## 8. Historical V2 public surface

The V2 reference path remains:

```text
request -> planner -> execution_engine -> tool_registry -> runtime_guard -> tool -> result_gate -> result
```

The public mock runtime demonstrates V2-shaped `ALLOW`, `WARN`, and `BLOCK` behavior. The V2 package also preserves public proof tests, 13/13 and 8/8 ANDY field-test results, and scoped at-most-once evidence.

Those artifacts remain useful, but they do not publish or reproduce V3.

## 9. What is public and private

Public:

- V3 architecture, properties, status, limits, and aggregate evidence;
- V2 documentation, public examples, mock runtime, proof tests, and sanitized field-test evidence;
- version-aware glossary and invariants.

Private:

- V3 source and private test fixtures;
- raw schemas, logs, traces, audit records, prompts, paths, credentials, and configuration;
- private authorization, approval, and trust-boundary mechanisms;
- detailed adversarial probes, deployment internals, and private operator internals.

## 10. Claim limit

AIOS V3 P0 is complete in its declared validation scope. That does not mean production readiness, security certification, formal verification, universal provider support, distributed exactly-once execution, or validation across every environment.

Start with the [V3 public index](aios-v3/README.md), read the [architecture](aios-v3/AIOS_V3_ARCHITECTURE.md), then review the [evidence](aios-v3/AIOS_V3_P0_EVIDENCE.md) and [status limits](aios-v3/AIOS_V3_STATUS_AND_LIMITS.md).
