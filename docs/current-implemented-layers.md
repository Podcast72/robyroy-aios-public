# Current Implemented Layers

This page separates the source-private V3 architecture and capability evidence from the preserved V2 public demonstration surface. Status terms describe declared validation scopes, not unrestricted production readiness.

## Current Private V3 Layers And Capabilities

| Layer or capability | Public status | Role | Authority limit |
| --- | --- | --- | --- |
| AgentLoop | P0 foundation completed; exercised in the real pilot | Coordinates turns, requests governed model/tool work, and produces the final answer | Does not possess execution authority |
| ModelPort / GovernedModelPort | Provider-neutral boundary validated with OpenAI | Decouples the runtime from a model provider and routes inference through governance | Does not let a provider or agent loop bypass `ExecutionEngine` |
| ExecutionEngine | Execution authority across the declared P0/P1 scopes | Admits and executes governed model or tool work | Remains the authoritative execution path |
| Governed READ | Validated in a real-execution milestone | Reads only admitted state within the capability scope | Does not imply unrestricted visibility |
| Bounded governed WRITE | Validated in a later real-execution milestone | Performs one admitted mutation within a bounded action scope | Does not self-authorize or imply arbitrary write access |
| Durable SQLite WRITE | Validated in its declared scope | Persists an admitted bounded change durably | Does not establish universal durability or distributed exactly-once semantics |
| Approval path | Explicit approval observed for the pilot WRITE | Separates proposed action from authorization to execute | Implementation and policy internals remain private |
| RunStore | Authoritative execution-truth boundary | Supports governed state and fail-closed replay/recovery decisions | Raw schema and internals are not public |
| Conversation/checkpoint state | Exercised in the end-to-end pilot at an aggregate level | Supports interaction continuity without replacing execution truth | Raw state structures are private |
| ResultGate | Exercised in governed round trips and the real pilot | Controls outward result release | Underlying success alone does not authorize release |
| Structured trace / audit | Aggregate evidence confirms reviewable governed execution | Preserves evidence for review | Raw audit, log, and trace material is private |
| Recovery / replay / resume | Verified in the declared synthetic scope | Replays terminal truth and stops uncertain effects | No universal exactly-once claim |
| Composition Root | P0 assembly foundation completed | Wires the runtime so authority boundaries remain explicit | Source, configuration, and trust-boundary details remain private |

Persistence/reopen/replay/resume recovery evidence remains synthetic and scope-bound. Later real-execution evidence is limited to a bounded durable SQLite WRITE and the focused end-to-end pilot; it does not extend the recovery claim.

P2.0 — initial natural-language governed interaction — is implemented and validated in its declared scope. Further P2 work remains in progress; no broad P2 completion claim is made.

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
