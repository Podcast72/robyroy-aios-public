# What AIOS Is and Is Not

This public repository documents AIOS in technical terms and with a deliberately limited scope.
The goal is to make the architecture readable without presenting the public perimeter as the full private system.

## What AIOS is

AIOS is presented here as a governed execution architecture for AI-assisted systems.
In practical terms, it is a control-plane model for how requests move through a controlled path, how execution is delegated, how tool access is mediated, and how results remain reviewable.

In this public repository, the official reference backbone is:

```text
request -> planner -> execution_engine -> tool_registry -> runtime_guard -> tool -> result
```

That backbone is the central public reference because it makes the execution order explicit and keeps planning, execution, tool mediation, runtime decisions, and result handling distinguishable.

This repository also shows selective public evidence around that model:

- backbone documentation
- runtime guard behavior
- additive post-tool result handling
- governance and runtime separation
- public proofs and adapted public tests
- a public mock runtime that illustrates the mediation flow

## What AIOS is not

AIOS is not presented here as a simple chatbot.
It is not described as a thin prompt layer or a cosmetic wrapper placed on top of a model.

This public repository is also not the full private RobyRoy AIOS operational codebase.
It does not publish the complete internal runtime, private orchestration surfaces, internal memory estate, or other non-public operational layers.

It should also not be read as:

- a mini product build that happens to be incomplete
- a fake mock standing in for a system that does not exist
- a marketing wrapper around vague claims
- a 1:1 public copy of the private core

The public claim is narrower and more technical:
this repository discloses the governed execution pattern, selected architectural boundaries, and a bounded set of proofs that can be inspected in public.

## Why this public repo exists

This repository exists as a public technical reference and disclosure.
Its purpose is to show the backbone, boundary definitions, selected proofs, and some runnable public artifacts without misrepresenting the public perimeter as the full private system.
