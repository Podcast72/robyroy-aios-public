# AIOS Public Overview

AIOS is a Governed AI Execution Layer.

It exists because agents do more than answer questions. They plan, call tools, touch data, and may trigger workflows. Once an agent can act, the central engineering question becomes: what was it allowed to do, through which path, with which controls, and with what result boundary?

Current AI systems accelerate answers, analysis, and automation. The more they act, the more control is needed.

## Public Definition

AIOS separates agent planning from governed execution.

Short form:

```text
Model -> AIOS -> Tool -> Result
```

The public backbone is:

```text
request -> planner -> execution_engine -> tool_registry -> runtime_guard -> tool -> result_gate -> result
```

The model does not act directly. It plans. AIOS evaluates. The result passes through the gate.

The agent-facing layer can prepare a plan, but the governed path controls whether a tool can be reached and whether the result can be returned. The goal is to make AI act within verifiable rules.

## Enterprise-Aligned Summary

Current enterprise documentation supports a stronger public message than a concept page:

- the enterprise track has internal/staging evidence for governed runtime behavior
- an expanded enterprise staging gate passed with a non-public-distribution posture
- non-editable package/install checks passed in controlled internal validation
- governance hardening covers policy, capability, approval, budget, memory/state, and supervision categories
- runtime governance wiring was demonstrated through the planned-step execution path
- result-boundary checks and raw-output protection are documented in internal/staging hardening evidence
- audit/replay and trace evidence support reviewable execution order
- connector-readiness work shows external agent intent should be normalized through an adapter before reaching the backbone

## What This Repository Provides

- a public technical package
- a demo/documentation repository
- public architecture and governance docs
- a small public mock runtime
- curated JSON proof cases
- adapted public tests
- aggregate enterprise evidence summaries
- a clear public/private boundary

## Public-Safe Positioning

This repository is prepared for controlled technical review and agent-integration evaluation. It is source-private, and the core runtime is not publicly released here.

The adoption path is controlled pilot, audit, and progressive extension.
