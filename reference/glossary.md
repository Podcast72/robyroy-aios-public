# Glossary

## AIOS V2 — Governed Execution Backbone

The historical public milestone centered on this tool-oriented path:

`request -> planner -> execution_engine -> tool_registry -> runtime_guard -> tool -> result_gate -> result`

Its documentation, mock runtime, proof tests, and field-test evidence remain preserved.

## AIOS V3 P0 — Governed Agent Runtime

The current milestone in which agent coordination, model calls, and tool calls operate through a governed runtime while `ExecutionEngine` remains the execution authority.

## AgentLoop

The V3 coordinator for turns and requested work. It does not possess execution authority.

## ModelPort

The provider-neutral model boundary. It allows provider integration to change without moving execution authority into the provider.

## GovernedModelPort

The V3 boundary that keeps model work on the governed execution path.

## ExecutionEngine

The execution authority for governed model and tool work. In V2 documents it appears as `execution_engine`; V3 public architecture uses the component name `ExecutionEngine`.

## RunStore

The authoritative execution-truth boundary for governed runs. This glossary defines its public role, not its private schema.

## conversation state

State used to continue the agent interaction or checkpoint. It remains separate from authoritative execution truth.

## execution truth

Authoritative state about whether governed work was admitted, executed, completed, failed, or became uncertain.

## ResultGate

The outward result-release boundary. A successful underlying call does not by itself authorize release.

## UNKNOWN_EFFECT

A terminal uncertainty state used when an external effect may have occurred but the runtime cannot prove the outcome. It blocks blind automatic re-execution and requires reconciliation.

## provider-neutral

An architectural property of `ModelPort`: the provider can be replaced behind the boundary without becoming the execution authority. It does not mean every provider is implemented or validated.

## Composition Root

The assembly boundary that wires P0 components and their allowed dependencies. Its public meaning is architectural; implementation and configuration remain private.

## execution identity

The governed identity that binds admitted work, executable/artifact identity, accounting, and replay behavior within the verified scope.

## budget accounting

Authoritative consumption accounting attached to governed execution in the declared P0 scope.

## credential egress

Governance over whether and how credentials may reach an external provider or capability. Public docs describe the property, not private enforcement mechanisms.

## content provenance

Governed information about the origin and handling of content across model and tool boundaries.

## fail-closed

A posture in which missing, invalid, exhausted, or uncertain authority does not silently fall back to ungoverned execution.

## replay

Returning or reconstructing an authoritative prior terminal outcome without executing the same governed work again.

## resume

Continuing a persisted run according to authoritative execution truth rather than conversational intent alone.

## runtime_guard

The V2 public pre-tool decision layer that can issue `ALLOW`, `WARN`, or `BLOCK`.

## tool_registry

The V2 public tool-access layer in the historical backbone.

## governance

The controls and decisions that determine whether proposed work can proceed and what result can be released. Governance does not itself become an alternate execution path.

## result handling

Post-execution control over outward material, such as validation, redaction, shaping, or blocking of release.

## audit trail

Reviewable evidence about governed execution. Raw V3 audit data is not part of the public disclosure.

## bounded technical disclosure

The repository policy of publishing architecture, properties, aggregate evidence, and limits without publishing private implementation mechanisms or raw internal artifacts.

## compat path

A non-core path that remains outside the applicable governed reference path and must stay distinguishable from it.

## proof area

A bounded repository area in which a specific public claim is supported by curated, version-scoped evidence.
