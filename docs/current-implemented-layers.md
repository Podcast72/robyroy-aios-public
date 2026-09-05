# Current Implemented Layers

This page separates the current private V3 P0 architecture from the preserved V2 public demonstration surface. Status terms describe the declared validation or public-evidence scope, not unrestricted production readiness.

## Current V3 P0 Layers

| Layer | Public status | Role | Authority limit |
| --- | --- | --- | --- |
| AgentLoop | P0 completed and covered by targeted private validation | Coordinates turns, requests governed model/tool work, and produces the final answer | Does not possess execution authority |
| ModelPort / GovernedModelPort | Provider-neutral boundary validated in P0 | Decouples the runtime from a model provider and routes inference through governance | Does not let a provider or agent loop bypass `ExecutionEngine` |
| ExecutionEngine | P0 execution authority | Admits and executes governed model or tool work | Remains the authoritative execution path |
| Governed model/tool execution | Round-trip verified in the P0 scope | Performs admitted inference or capability work | Does not self-authorize |
| RunStore | Persistence/reopen/resume verified in the synthetic P0 scope | Holds authoritative execution truth | Raw schema and internals are not public |
| Conversation/checkpoint state | Present as a separate concern | Supports continuation of the agent interaction | Cannot rewrite execution truth |
| ResultGate | Governed round-trip and live path evidence include result gating | Controls outward result release | Underlying success alone does not authorize release |
| Audit | Aggregate P0 evidence confirms reviewable governed execution | Records evidence for review | Raw audit/log/trace material is private |
| Execution identity and accounting | P0 property validated in the declared scope | Binds executable/artifact identity and authoritative budget accounting to governed execution | Enforcement mechanisms are private |
| Egress and provenance governance | P0 property validated in the declared scope | Governs credential egress and content provenance | Does not support a universal no-leak claim |
| Composition Root | P0 assembly completed | Wires the runtime so authority boundaries remain explicit | Source, configuration, and trust-boundary details remain private |

## Preserved V2 Public Layers

The executable public demonstrations still implement and test the V2 reference path:

`request -> planner -> execution_engine -> tool_registry -> runtime_guard -> tool -> result_gate -> result`

| V2 public layer | Public evidence | Historical role |
| --- | --- | --- |
| Backbone | Documentation, examples, tests, and mock runtime | Makes the governed tool path explicit |
| Runtime Guard | Public examples and mock implementation | Issues `ALLOW`, `WARN`, or `BLOCK` before tool execution |
| Result Gate | Public proof case and documentation | Applies additive post-tool result handling |
| Governance Layer | Public reference case | Keeps governance approval separate from runtime effect |
| Auditability/evidence | Public proofs, invariants, and field-test summaries | Makes selected decisions and ordering reviewable |

The V2 mock runtime is not upgraded into a V3 replica. V3 implementation layers remain source-private.
