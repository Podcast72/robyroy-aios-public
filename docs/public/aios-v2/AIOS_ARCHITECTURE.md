# AIOS Architecture

AIOS is organized around an explicit governed execution path.

The presentation-level path is:

```text
Model -> AIOS -> Tool -> Result
```

The technical backbone expands that into:

```text
request -> planner -> execution_engine -> tool_registry -> runtime_guard -> tool -> result_gate -> result
```

## Component Roles

| Component | Role | Control value |
| --- | --- | --- |
| `request` | Entry point for a user, system, or normalized external-agent request. | Makes execution entry explicit. |
| `planner` | Prepares intended work for the agent. | Planning is not direct tool authority. |
| `execution_engine` | Runs planned steps through a controlled sequence. | Execution is mediated rather than improvised. |
| `tool_registry` | Lists and resolves declared tools. | Undeclared tool access is outside the public backbone. |
| `runtime_guard` | Decides whether a tool step may proceed. | `ALLOW`, `WARN`, `BLOCK`, or controlled pause semantics happen before tool execution. |
| `tool` | Performs the selected capability. | Tool execution is downstream of governance. |
| `result_gate` | Reviews outward output after tool execution. | Raw output is not automatically released. |
| `result` | Final governed response. | Returned result remains attached to the governed path. |

## Enterprise Architecture State

Enterprise reports confirm that the public backbone is not merely illustrative. Internal/staging documentation describes:

- runtime guard connected before tool execution
- result gate connected after registry/tool response
- optional structured governance preflight before registry/tool execution
- governance decisions recorded into runtime metadata and trace surfaces
- no parallel governance path replacing the backbone
- fail-closed behavior for risky, denied, missing, or unclassifiable control contexts
- result-boundary hardening for invalid, empty, sensitive, or blocked output
- audit/replay-oriented trace events for reconstructing execution order

The public package summarizes these concepts without exposing implementation internals.

## Governance Preflight Categories

When structured governance context is supplied, enterprise reports describe pre-tool checks across:

- policy
- capability
- budget
- approval
- memory
- state
- run supervision

These checks sit before registry/tool execution. The runtime guard remains the final pre-tool safety boundary, and the result gate remains the post-tool result boundary.

## Architectural Difference

| Direct agent execution | AIOS-governed execution |
| --- | --- |
| Model plans and acts through available tools. | Model-facing planning is separated from tool execution. |
| Tool calls can become implicit behavior. | Tools are declared through a registry. |
| Guardrails may be external or after-the-fact. | Runtime control sits in the path before tool execution. |
| Output may be returned without a result boundary. | Result output passes through a result gate. |
| Audit may be incomplete. | The path is designed to be inspectable. |

The value is not isolated controls. The value is preventing tool execution from skipping the governed path.

## Public Boundary

This document describes the public architecture. It does not disclose private source files, private runtime internals, private adapter wiring, hidden prompts, memory internals, package internals, raw test fixtures, or deployment-specific configuration.
