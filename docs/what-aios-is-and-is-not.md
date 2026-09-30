# What AIOS Is and Is Not

## What AIOS Is

AIOS is a governed agent runtime and execution layer. V3 P0 and P1 completed in declared scopes, P2.0–P2.7 were accepted in declared scopes, and R2.7 closeout completed. **P2.7 / R2.7 remains FROZEN and AGENT-READY; P3 native multi-agent, EA-0A proposal admission, and EA-0B external-host governance are accepted in their declared scopes above that baseline.**

> **Models/agents propose. AIOS governs. AIOS executes admitted actions. AIOS verifies the observed effect.**

The model can propose work and the `AgentLoop` can coordinate a run, but `ExecutionEngine` remains the execution authority. Governed READ and bounded governed WRITE remain separately admitted, explicit approval applies where required, conversation/session state remains separate from authoritative execution truth, and result release remains governed.

The current public architecture is:

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

This is an architecture-level description, not a public implementation map.

P3 native multi-agent is accepted inside AIOS. EA-0A and EA-0B add non-authoritative external proposal admission and a tested external-host boundary for governed READ/WRITE. See [External Host Evidence](public/aios-v3/AIOS_V3_EXTERNAL_HOST_EVIDENCE.md). OpenAI is a validated model provider, while OpenAI Agents SDK is unimplemented. Hermes was an experimental decision source, not a production connector. `ModelPort` separates provider concerns from AIOS / `ExecutionEngine` authority.

## What AIOS Evolved From

AIOS V2 documented the governed execution backbone:

```text
request -> planner -> execution_engine -> tool_registry -> runtime_guard -> tool -> result_gate -> result
```

The V2 public mock runtime, examples, proof tests, ANDY field tests, and at-most-once evidence remain preserved as historical evidence. They are not relabeled as V3.

## What AIOS Is Not

AIOS is not an AI model, chatbot, prompt library, or a claim that a model can govern itself.

This public repository is not:

- the private AIOS V3 runtime;
- a distributable V3 implementation;
- a copy of private source, tests, schemas, prompts, or configuration;
- a disclosure of private authorization, approval, or trust-boundary mechanisms;
- a publication of raw logs, traces, audit records, paths, or credentials;
- a security certification or formal proof;
- unrestricted production-readiness evidence;
- a universal provider, integration, capability, or deployment claim;
- a distributed exactly-once claim;
- a V3 label placed on the smaller V2 public mock.

## Why This Public Repository Exists

The repository provides **bounded technical disclosure**: architecture, properties, aggregate evidence, explicit limitations, and preserved historical demonstrations.

It gives technical reviewers a truthful view of the AIOS evolution without publishing the mechanisms or operational artifacts required to reconstruct the private runtime.
