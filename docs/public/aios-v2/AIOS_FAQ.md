# AIOS FAQ

## What is AIOS?

AIOS is presented here as a governed execution layer for AI agents. It separates agent planning from controlled tool execution and result release.

In presentation terms: the model plans, AIOS governs, the tool runs only through the governed path, and the result passes through a gate.

## What is the canonical backbone?

```text
request -> planner -> execution_engine -> tool_registry -> runtime_guard -> tool -> result_gate -> result
```

## Is this repository only a concept page?

No. It is a public-facing demo and documentation package aligned with internal/staging enterprise evidence. It includes a public mock runtime, public examples, adapted tests, proof artifacts, and sanitized evidence summaries.

## Is this repository the private AIOS source?

No. This is a public demo and documentation package. The private runtime core is not published here.

## What enterprise evidence is summarized publicly?

Public-safe summaries include enterprise staging gate pass status, non-editable package/install checks, full-suite pass evidence, runtime/governance hardening categories, runtime governance wiring, connector-readiness work, and public/private boundary review.

They also include result-boundary, audit/replay, allow/warn/block, fail-closed, and no-silent-fallback evidence categories.

## What can I test?

You can run the public mock runtime, inspect JSON proof cases, and run adapted public tests for backbone consistency, guard behavior, result handling, and governance separation.

## Does `BLOCK` mean the tool ran and output was hidden?

No. In the public model, `BLOCK` is a pre-tool decision. The tool does not execute.

## What does the result gate do?

The result gate controls outward output after tool execution. It can validate, shape, redact, or block material before the final result is returned.

## Is governance the same as runtime application?

No. Governance decisions are recorded and scoped separately. Approval does not automatically become a runtime effect.

## Can a raw external agent call tools directly?

No. Enterprise connector-readiness docs support an adapter-based model: external intent must be normalized and governed before it reaches the runtime backbone.

## Why is the runtime core private?

The public goal is to disclose the governed execution model and a bounded demo surface without publishing private runtime internals, package internals, operational wiring, prompts, memory surfaces, or environment configuration.

## Who is this repository for?

Technical reviewers, agent-framework evaluators, and engineering teams assessing whether the AIOS governed execution model is a useful integration pattern.
