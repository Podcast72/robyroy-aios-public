# Current Implemented Layers

This page summarizes the layers that the public repository documents as implemented, demonstrated, or materially present in the public reference perimeter.
It does not claim to list the full private system.

| Layer | Status | Role | What it does | What it does not do |
| --- | --- | --- | --- | --- |
| Backbone | Documented, test-backed, and reflected in the public mock runtime | Defines the official governed execution path | Keeps the reference sequence explicit: `request -> planner -> execution_engine -> tool_registry -> runtime_guard -> tool -> result` | Does not claim to expose every private support surface or every internal branch |
| Architectural Enforcement / pre-delegation enforcement | Documented as an architectural boundary, not published as a standalone public module | Keeps delegation and tool access on the official governed path before execution reaches the tool | Separates planning, execution, and tool access so the system is not framed as direct tool invocation | Does not replace `runtime_guard`, and is not published here as a separate private enforcement engine |
| Runtime Guard | Documented, example-backed, and implemented in the public mock runtime | Governs runtime before tool execution | Issues `ALLOW`, `WARN`, or `BLOCK` before the tool runs, and stops blocked requests before tool execution | Does not perform post-tool output release control and does not turn governance records into runtime execution |
| Result Gate / post-tool output enforcement | Documented publicly as additive result handling and backed by a public proof case | Validates or constrains outward output after tool execution | Supports post-tool inspection, redaction, or blocking of release when returned material should not be exposed as-is | Does not redefine the backbone, does not move `runtime_guard` after the tool, and does not grant tool access |
| Governance Layer | Documented with a public reference case | Records, reviews, and scopes governance decisions | Preserves approvals, denials, revocations, and controlled override context as governance-layer actions | Does not automatically become runtime application, does not bypass the guard, and does not rewrite the backbone |
| Auditability / evidence layer | Documented and supported by public proofs, invariants, and adapted tests | Observes and preserves reviewable evidence | Makes events, ordering, and decision points inspectable after the run | Does not decide runtime permission, does not validate release by itself, and does not modify the backbone |

No learning loop is listed here because the current public repository does not document one as a public implemented layer.
