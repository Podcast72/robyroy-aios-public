# Invariants

The public architectural invariants of this repository are intentionally short and explicit.

1. The official path remains explicit:
   `request -> planner -> execution_engine -> tool_registry -> runtime_guard -> tool -> result`
2. `planner` delegates execution and does not become the official tool access layer.
3. `tool_registry` remains the official path for tool access in the documented backbone.
4. `runtime_guard` remains before tool execution and stays mandatory in the official path.
5. `BLOCK` means the tool does not execute.
6. Result handling does not replace execution governance or redefine the backbone.
7. Governance does not silently become runtime bypass or runtime application.
8. Compat or legacy surfaces are not the official backbone.
9. Public proofs remain selective, curated, and bounded by declared limitations.

