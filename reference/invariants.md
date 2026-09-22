# Invariants

The public invariants are version-aware. V3 is the current source-private architecture and evidence track; V2 remains the historical public demonstration.

## Current V3 Invariants

1. Models propose; proposals do not self-authorize.
2. `AgentLoop` coordinates work and does not possess execution authority.
3. Model calls and tool calls traverse the governed execution backbone.
4. `ModelPort` remains provider-neutral, and provider integration does not become execution authority.
5. `ExecutionEngine` remains the execution authority.
6. Governed READ and bounded governed WRITE remain separately admitted and scope-bound.
7. A WRITE that requires approval does not execute without the applicable explicit approval.
8. Approval for one proposal does not imply authority for a different action or broader scope.
9. Conversation/session state remains separate from authoritative execution truth.
10. Retry and recovery fail closed.
11. `UNKNOWN_EFFECT` blocks blind automatic re-execution and requires reconciliation.
12. Persistence, replay, reopen, and resume claims remain limited to their verified identity and persistence assumptions.
13. Durable SQLite WRITE evidence does not establish universal durability or distributed exactly-once semantics.
14. `ResultGate` controls outward release after governed execution.
15. Composition must not create an alternate authority path for the agent loop, provider, or tools.
16. Public V3 claims remain aggregate, scoped, conservative, and non-certifying.
17. The private V3 implementation is not reconstructed in the public repository.

## Preserved V2 Public Invariants

1. The V2 path remains explicit:
   `request -> planner -> execution_engine -> tool_registry -> runtime_guard -> tool -> result_gate -> result`
2. `planner` delegates execution and does not become the official tool access layer.
3. `tool_registry` remains the tool access layer in the documented V2 backbone.
4. `runtime_guard` remains before tool execution in the V2 public model.
5. `BLOCK` means the V2 public mock tool does not execute.
6. Result handling does not replace V2 execution governance or redefine its backbone.
7. Governance approval does not silently become runtime application.
8. V2 public proofs remain selective, curated, and bounded by their declared limitations.
9. V2 public artifacts are historical evidence and are not relabeled as V3 implementation evidence.
