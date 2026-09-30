# Glossary

## AIOS V2 — Governed Execution Backbone

The historical public milestone centered on this tool-oriented path:

`request -> planner -> execution_engine -> tool_registry -> runtime_guard -> tool -> result_gate -> result`

Its documentation, mock runtime, proof tests, and field-test evidence remain preserved.

## AIOS V3 P0 — Governed Agent Runtime

The foundational V3 milestone, completed in its declared scope, in which agent coordination, model calls, and tool calls operate through a governed runtime while `ExecutionEngine` remains the execution authority.

## P1 — Governed Real Execution

The completed phase, in its declared scope, that extended the governed V3 path to real admitted capabilities, including governed READ, bounded governed WRITE, and a durable SQLite WRITE.

## P2.0 — Initial natural-language governed interaction

The initial natural-language governed interaction milestone, accepted in its declared scope. The current progression includes accepted P3 native multi-agent, EA-0A, and EA-0B above the frozen P2.7 / R2.7 baseline; P2.0 remains a historical milestone.

## P2.7 — Governed filesystem WRITE

The accepted bounded filesystem WRITE milestone. It does not imply arbitrary filesystem access or universal duplicate-effect prevention.

## AGENT-READY

The frozen P2.7 / R2.7 governed Core baseline on which the accepted P3 native multi-agent work was built. It does not mean OpenAI Agents SDK or production Hermes integration is implemented, or that unrestricted production readiness has been established.

## P3 — Native multi-agent

The accepted sequential Coordinator/Analyst/Challenger/Operator arrangement within one AIOS `AgentLoop`, session, root run, and shared budget. Specialist proposals do not acquire execution authority.

## EA-0A — Preformed proposal admission

Accepted admission of already formed, non-authoritative proposals through existing AIOS governance, without model inference in that path.

## EA-0B — External Host Boundary

Accepted vendor-neutral external process boundary for governed READ, approval-bound WRITE/resume, and tested macOS two-principal isolation in declared scopes. It is not a ready-made vendor adapter, universal sandbox, or exactly-once guarantee.

## Experimental Hermes decision source

A bounded Pilot 03 in which Hermes supplied a decision artifact while AIOS retained execution, approval, observation, ResultGate, and authoritative evidence. This is not a production Hermes integration.

## AgentLoop

The V3 coordinator for turns and requested work. It does not possess execution authority.

## ModelPort

The provider-neutral model boundary. It allows provider integration to change without moving execution authority into the provider.

## GovernedModelPort

The V3 boundary that keeps model work on the governed execution path.

## ExecutionEngine

The execution authority for governed model and tool work. In V2 documents it appears as `execution_engine`; V3 public architecture uses the component name `ExecutionEngine`.

## governed READ

An admitted read capability limited to allowed state and the declared operation scope. It does not mean unrestricted visibility.

## bounded governed WRITE

An admitted mutation constrained by an explicit capability scope, applicable authority, and approval requirements. It does not mean arbitrary write access.

## durable SQLite WRITE

A bounded SQLite mutation observed through the governed durable path in its declared scope. It is not a universal durability or distributed exactly-once claim.

## explicit approval

A required authorization step for an applicable proposed action. Model prose is not approval, and approval does not broaden the action's scope.

## RunStore

The authoritative execution-truth boundary for governed runs. This glossary defines its public role, not its private schema.

## conversation or session state

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

The assembly boundary established in the P0 foundation. Its public meaning is architectural; implementation and configuration remain private.

## execution identity

The governed identity that binds admitted work, executable/artifact identity, accounting, and replay behavior within the verified scope.

## budget accounting

Authoritative consumption accounting attached to governed execution in its declared scope.

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

## synthetic evidence

Controlled validation evidence that isolates runtime properties or failure handling. It is not by itself evidence of a real provider and real admitted effect in one path.

## real end-to-end evidence

An observed path joining a real provider, admitted capability, applicable approval, governed execution, persistence/context boundaries, and result handling. A single observation is not a benchmark or broad deployment claim.

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
