# AIOS in 5 Minutes

## 1. What AIOS is

AIOS is a governed execution layer for AI agents.

Its purpose is to control the path between an AI-generated plan and any tool, workflow, data access, or business action that may follow. AIOS separates planning, authorization, execution, result handling, and evidence so that agent activity can be inspected and constrained instead of treated as an opaque model-to-tool call.

In this public repository, AIOS is presented through documentation, public-safe summaries, a small mock runtime, examples, and proof tests.

## 2. What AIOS is not

AIOS is not an AI model, chatbot, prompt library, agent framework replacement, or generic automation script.

This repository is also not the private AIOS runtime core. It does not publish private source code, private orchestration internals, private prompts, private memory surfaces, raw logs, raw traces, or raw internal test material.

The public mock runtime is intentionally minimal. It demonstrates the control shape; it is not a full copy of the private runtime.

## 3. The problem

AI agents become more useful when they can act, but action changes the risk profile.

A model that only answers a question can still be wrong. A model that can call tools, read files, update systems, trigger workflows, or touch customer operations can create effects before a human sees the final answer. Direct model-to-tool patterns are easy to prototype, but they can be hard to review, limit, or reconstruct later.

AIOS addresses that execution boundary. The core question is not only "what did the model say?" It is also "what was the agent allowed to do, through which tool, under which policy, and what result was allowed back out?"

## 4. The governed execution path

The canonical public AIOS path is:

```text
request -> planner -> execution_engine -> tool_registry -> runtime_guard -> tool -> result_gate -> result
```

Each stage has a distinct role:

| Stage | Public meaning |
| --- | --- |
| `request` | A user, system, or external-agent request enters the governed path. |
| `planner` | The planning layer prepares intended work. |
| `execution_engine` | Planned work is run through a controlled execution sequence. |
| `tool_registry` | Only declared tools are exposed to the governed path. |
| `runtime_guard` | Execution is allowed, warned, blocked, or paused before the tool runs. |
| `tool` | The selected capability runs only after the governed path permits it. |
| `result_gate` | Tool output is checked, shaped, redacted, or blocked before release. |
| `result` | The final response is returned with the governed path preserved. |

The important point is that the tool is not called directly from the model. It is reached through a controlled path.

## 5. ALLOW / WARN / BLOCK in practice

The public mock runtime includes simple examples:

| Verdict | Example behavior | Public meaning |
| --- | --- | --- |
| `ALLOW` | A public config read proceeds through the mock reader. | The request is permitted and the tool can run. |
| `WARN` | A simulated `.env` read remains visible and returns a redacted mock result. | The action is sensitive enough to surface, but the demo still permits a controlled result. |
| `BLOCK` | A destructive delete request stops before the mock delete tool runs. | The guard interrupts execution before tool side effects occur. |

This is a small public demonstration, not a complete policy system. Its value is that the mediation chain is visible and testable.

## 6. What is public in this repository

This repository includes:

- a public documentation package;
- the canonical governed execution backbone;
- architecture, governance, status, limits, and FAQ documents;
- a small public mock runtime;
- curated JSON examples;
- public proof artifacts;
- adapted public tests;
- public-safe summaries of internal/staging evidence categories.

The public surface is designed for technical review of the AIOS control model and public/private boundary.

## 7. What remains private

The private AIOS runtime core remains private.

This repository does not include private runtime source, private package internals, private orchestration logic, private prompts, private memory surfaces, private environment wiring, raw enterprise reports, raw logs, raw traces, raw test files, or local machine paths.

Public documents may summarize internal/staging evidence categories, but those summaries do not publish the underlying private material.

## 8. Current public-safe status

The current public-safe reading is conservative:

- this is a public demo and documentation repository;
- the private runtime core is not published here;
- the public mock runtime and tests make the governed path inspectable;
- internal/staging evidence is summarized only at a public-safe level;
- the repository is suitable for bounded technical review and controlled agent-integration evaluation discussions.

This status should not be read as a shipped runtime, broad deployment evidence, third-party assurance conclusion, or legal/compliance conclusion.

## 9. Current limits

The public package has intentional limits:

- the mock runtime is minimal;
- public examples are curated;
- public tests are adapted for a source-private boundary;
- internal/staging validation material is summarized rather than copied;
- real third-party agent integration remains future work;
- private runtime behavior cannot be fully inferred from the public mock.

These limits are part of the public/private boundary. They keep the repository useful for review without exposing private implementation material.

## 10. Why this matters

Enterprise AI agents need more than fluent answers. They need controlled execution.

When agents can call tools, the enterprise question becomes whether actions are authorized, limited, traceable, and result-gated. AIOS focuses on that governed execution layer: a place where planning is separated from tool use, tool access is explicit, guard decisions happen before execution, and outputs pass through a result boundary.

For technical reviewers, this repository is a fast way to inspect the AIOS model without access to the private core: read the backbone, run the mock cases, review the public proof tests, and evaluate whether the execution boundary addresses the risks of direct agent-to-tool automation.
