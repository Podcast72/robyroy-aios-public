# AIOS For Technical And Grant Evaluators

This page provides a time-boxed path through the public AIOS evidence. The repository is a **bounded technical disclosure**: it is intended to support technical evaluation without publishing the private V3 runtime or the internals needed to reconstruct it.

## Restack Proposal Boundary

The proposed **Open Governed Capability Execution Kernel** is future, separately scoped work. It is not the source-private AIOS V3 runtime and does not depend on that runtime. Its proposed funded scope is a standalone, model-neutral capability-execution kernel for general networked software, released in its entirety under the Apache License 2.0; LLM/model development, integration, evaluation, and AI-specific orchestration are excluded.

The detailed separation between existing evidence and proposed work is documented in [Open Governed Capability Execution Kernel](docs/public/restack/OPEN_GOVERNED_CAPABILITY_EXECUTION_KERNEL.md).

## Suggested Review Path

### 2 minutes — orientation

Read the [repository README](README.md) for the current status, public/private split, and the relationship between the executable V2 demonstration and the source-private V3 track.

### 5 minutes — system model

Read [AIOS in 5 Minutes](docs/public/AIOS_IN_5_MINUTES.md) for the authority model, milestone progression, and claim limits.

### 10 minutes — current evidence

Read:

1. [AIOS V3 Current Evidence](docs/public/aios-v3/AIOS_V3_CURRENT_EVIDENCE.md)
2. [AIOS V3 Post-Core Evidence](docs/public/aios-v3/AIOS_V3_POST_CORE_EVIDENCE.md)
3. [AIOS V3 Status and Limits](docs/public/aios-v3/AIOS_V3_STATUS_AND_LIMITS.md)

Together they distinguish the frozen core, P3 native multi-agent, the separate P2 and P3 pilots, external read-only review, Hermes experiments, and explicit limits.

The current status is **P2.7 / R2.7 FROZEN; Governed Core AGENT-READY; P3 native multi-agent accepted in its declared scope**. OpenAI is a validated model provider. OpenAI Agents SDK is unimplemented; Hermes decision-source evidence is experimental.

### Technical deep dive

- [V3 architecture](docs/public/aios-v3/AIOS_V3_ARCHITECTURE.md)
- [Current implemented layers](docs/current-implemented-layers.md)
- [Integration model](docs/public/AIOS_INTEGRATION_MODEL.md)
- [Limitations](docs/limitations.md)
- [Public/private boundary](docs/public-vs-private-boundary.md)
- [Public invariants](reference/invariants.md)

### Historical evidence

- [AIOS V2 public index](docs/public/aios-v2/README.md)
- [At-most-once execution evidence](docs/public/aios-v2/AT_MOST_ONCE_EXECUTION_EVIDENCE.md)
- [ANDY controlled field test](docs/public/field-tests/andy-aios-2026-05-17/README.md)
- [ANDY bypass-attempt field test](docs/public/field-tests/andy-backbone-bypass-2026-05-22/ANDY_BACKBONE_BYPASS_ATTEMPT_EVIDENCE.md)
- [V2 public proof tests](docs/public-proof-tests/README.md)

These artifacts belong to the earlier V2 governed-execution milestone. They remain useful historical evidence and are not presented as V3 implementation evidence.

## What AIOS Is

AIOS is a governed agent runtime and execution layer. Models and agent orchestration can propose work, but they do not become execution authority. Governed model and tool work is admitted through an independent runtime path, with authoritative execution state and result release kept inside that path.

## What Has Been Demonstrated

Public-safe aggregate evidence supports the following bounded statements:

- V3 P0 completed the governed agent-runtime foundation in its declared scope;
- P1 completed the governed real-execution phase in its declared scope;
- P2.0–P2.7 were accepted in declared scopes and R2.7 closeout completed;
- governed READ and bounded governed WRITE were validated in successive milestones;
- a durable SQLite WRITE was validated in its declared scope;
- governed filesystem WRITE was validated in its bounded declared scope;
- retry, replay, reopen, and resume follow a fail-closed posture in their verified scopes;
- one observed OpenAI `gpt-5.6-sol` pilot completed a natural-language-to-bounded-WRITE path with explicit approval;
- the historical P2.7/R2.7 full private regression reported **2510 passed, 1 skipped, 11350 subtests passed**;
- the targeted P2.7/R2.7 closeout retest reported **5 passed**;
- the separate P3 `tests_v3` gate reported **1753 passed, 1 skipped, 1209 subtests passed**;
- the P3 live pilot observed sequential specialist roles, ordinary approval, one effect, and no duplicate effect on replay;
- the Hermes A/B and Pilot 03 experiments support the bounded decision/authority separation described in [Post-Core Evidence](docs/public/aios-v3/AIOS_V3_POST_CORE_EVIDENCE.md).

The full regression preceded the final documentation-only closeout and was not rerun merely for documentation changes. The targeted retests covered relevant filesystem ambiguity/recovery and result-exposure properties at an aggregate level.

## What Is Not Claimed

The published evidence does not establish:

- unrestricted production readiness;
- a security certification or penetration-test certification;
- formal verification;
- universal provider, model, tool, integration, or environment support;
- universal prevention of duplicate external effects;
- distributed exactly-once semantics or independent multi-host correctness;
- that OpenAI Agents SDK or production Hermes integration is implemented;
- that the external read-only model-assisted review is a certification.

## What Is Public And What Remains Private

Public material includes high-level architecture, public invariants, explicit limits, sanitized historical V2 evidence, aggregate V3 milestone results, and a minimal V2-shaped executable mock.

Private material includes V3 source, private test source and fixtures, raw schemas, implementation-sensitive authorization and approval logic, trust-boundary internals, adversarial probes, private prompts, raw logs and traces, deployment configuration, credentials, and operational paths.

The [public/private boundary](docs/public-vs-private-boundary.md) is the controlling disclosure policy for this repository.
