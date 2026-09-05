# Invariants

The public invariants are version-aware. V3 is the current architecture milestone; V2 remains the historical public demonstration.

## Current V3 P0 Invariants

1. Models propose; proposals do not self-authorize.
2. `AgentLoop` coordinates work and does not possess execution authority.
3. Model calls and tool calls traverse the governed execution backbone.
4. `ModelPort` remains provider-neutral, and provider integration does not become execution authority.
5. `ExecutionEngine` remains the execution authority.
6. Conversation/checkpoint state remains separate from authoritative execution truth.
7. Retry and recovery fail closed.
8. `UNKNOWN_EFFECT` blocks blind automatic re-execution and requires reconciliation.
9. Executable/artifact identity and authoritative budget accounting remain bound to the governed path.
10. Credential egress and content provenance remain governed.
11. Persistence, replay, reopen, and resume must not create duplicate execution within the verified identity and persistence scope.
12. `ResultGate` controls outward release after governed execution.
13. The Composition Root must not create an alternate authority path for the agent loop, provider, or tools.
14. Public V3 claims remain aggregate, scoped, conservative, and non-certifying.
15. The private V3 implementation is not reconstructed in the public repository.

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
