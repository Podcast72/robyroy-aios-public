# AIOS V2 Public Architecture Snapshot

AIOS V2 is documented here as a separated staging architecture built around a governed execution model.

The key architectural claim is limited and specific: AIOS does not treat tool use as a direct continuation of model output. It treats execution as a controlled path with declared boundaries, runtime checkpoints, and result handling.

Current public status remains:

- `V2_STAGING_GATE_PASSED`
- `STAGING_NON_VERIFIED`

## Canonical Backbone

```text
request -> planner -> execution_engine -> tool_registry -> runtime_guard -> tool -> result_gate -> result
```

## Public Reading Of The Backbone

- `request`: a user or system request enters the governed path
- `planner`: prepares an intended course of action instead of turning model output into immediate execution
- `execution_engine`: runs the planned path in a controlled runtime sequence
- `tool_registry`: exposes only declared tools that belong to the governed surface
- `runtime_guard`: evaluates whether a tool step may proceed, should warn, or must stop
- `tool`: executes only after the governed path allows it
- `result_gate`: checks or transforms output before it becomes the outward-facing result
- `result`: the final returned response after control surfaces have been applied

## Why The V2 Direction Matters

Modern AI systems can answer questions, analyze documents, call APIs, and coordinate workflows. Once the same system starts using tools or touching operational surfaces, the problem changes from content quality alone to execution control.

AIOS V2 addresses that shift by separating:

- model planning
- runtime execution
- governance decisions
- result validation
- audit-oriented reconstruction

This is the public architecture value of the V2 track. It is not a claim that all runtime questions are already resolved. It is a claim that the execution path is being shaped around explicit control boundaries rather than direct model-to-tool shortcuts.

## Enterprise Control Surfaces

The imported V2 material consistently describes ten governance surfaces that matter in enterprise settings:

| Surface | Public meaning |
| --- | --- |
| Agent Identity | the system should know who is acting |
| Capability Permissions | access should be granted by capability, not assumed |
| Budget & Limits | allowed scope should include consumption limits |
| State Control | state may inform execution but should not authorize it |
| Approval Gates | some sensitive actions should pause rather than proceed |
| Memory Governance | memory is a controlled surface, not an implicit right |
| Tool Contract | tools should be declared with clear constraints |
| Run Supervision | the trajectory of a run should remain visible |
| Audit Replay | decisions should be reconstructable |
| Policy Packs | posture can change without redefining the core runtime |

## Public Boundary

This public snapshot intentionally stays above private implementation detail. It does not expose internal source layout, hidden prompts, internal harnesses, or migration-only procedures. It presents architecture, not a full runtime disclosure.

## Status Interpretation

`V2_STAGING_GATE_PASSED / STAGING_NON_VERIFIED` should be read carefully.

It means the separated staging direction has documented evidence and a coherent governance model for a technical pilot or demo.
It does not mean runtime verification is complete, side effects are fully proven, or the system should be described with stronger final-state claims.
