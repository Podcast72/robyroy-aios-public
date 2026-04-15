# Runtime Backbone

The official public runtime backbone is:

```text
request -> planner -> execution_engine -> tool_registry -> runtime_guard -> tool -> result
```

This sequence is not presented as a loose list of components.
It is the documented reference order for governed execution in the public repository.

## Node roles

| Node | Public role | Why the boundary matters |
| --- | --- | --- |
| `request` | The user or system demand that enters the governed path. | Keeps entry into execution explicit. |
| `planner` | Interprets the request and delegates execution. | Planning does not become direct tool access. |
| `execution_engine` | Primary runtime layer for planned execution. | Planned steps pass through a dedicated execution layer before tool access. |
| `tool_registry` | Official access layer for tools. | Tool invocation stays mediated and discoverable. |
| `runtime_guard` | Pre-tool runtime decision layer. | Tool execution occurs only after explicit runtime assessment. |
| `tool` | The concrete capability being invoked. | The tool is a downstream effect surface, not the first decision point. |
| `result` | Controlled result returned after the official path. | Output remains attached to a governed execution path. |

## Backbone intent

The backbone makes several things legible:

- who delegates execution
- where execution authority lives
- where tool access is mediated
- where runtime decisions happen before side effects
- where the visible result comes from

## What the backbone does not mean

The backbone does not claim that every support layer is shown here.
It does not claim that additive controls do not exist.
It does not claim that the public repository includes the full operational implementation.

Instead, it gives a stable public reference path for reasoning about the system.

## Relationship to additive layers

This repository also documents result handling, governance records, and audit evidence.
Those areas matter, but they are described as additive or adjacent concerns.
They do not replace the official sequence above.

