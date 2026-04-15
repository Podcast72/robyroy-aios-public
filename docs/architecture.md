# Architecture

RobyRoy AIOS is documented here as a governed execution architecture for AI-assisted systems.
That wording matters.
The public claim is not that the project is simply a collection of agents, and not that it is only a wrapper around tools.

The architectural problem starts when an AI-assisted system does more than generate text.
Once the system can decide on execution steps, access tools, traverse runtime paths, and produce outputs that may shape later actions, the main question changes from "what did the model say?" to "how was execution governed?"

This repository therefore focuses on a narrower and more technical concern:

- how requests enter a governed path
- how execution is delegated
- how tool access is mediated
- how runtime control is made explicit
- how results are handled after tool execution
- how evidence remains reviewable

## Why this is not just assistant logic

A simple assistant flow often collapses planning, tool choice, execution, and output into one opaque step.
That can be acceptable for low-stakes or purely conversational cases.
It becomes weaker when runtime behavior matters.

A governed runtime architecture introduces explicit boundaries instead:

- planning is distinct from execution
- execution is distinct from tool access
- tool access is distinct from runtime gatekeeping
- runtime governance is distinct from post-tool result handling
- governance approval is distinct from runtime application

The point is not bureaucratic layering.
The point is to keep runtime behavior interpretable and constrain where execution authority actually lives.

## Public architectural position

In this public repository, the official reference path is:

```text
request -> planner -> execution_engine -> tool_registry -> runtime_guard -> tool -> result
```

This path is presented as the public backbone because it makes mediation readable.
It shows that tool access is not implicit, that runtime checks happen before tool execution, and that output handling can be discussed without pretending it rewrites the core execution order.

## Separation as a design principle

The repository deliberately separates several categories:

- the official runtime backbone
- additive layers such as result handling
- governance-layer decisions and records
- compat or legacy surfaces that are not promoted to the official path

That separation is important for technical honesty.
Without it, any useful path could be casually described as equivalent to the core architecture, which would make public claims less precise and harder to audit.

## Public scope

This repository documents the architecture, not the entire operational estate.
It uses a selective and public-facing perimeter so that readers can understand the technical direction without exposing private runtime materials, operational memory, internal prompts, bridge layers, or other non-public internals.

