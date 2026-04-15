# Glossary

## backbone

The official public runtime reference path:
`request -> planner -> execution_engine -> tool_registry -> runtime_guard -> tool -> result`

## planner

The layer that interprets a request and delegates execution.

## execution_engine

The primary runtime execution layer for planned steps in the public backbone.

## tool_registry

The official tool access layer in the documented backbone.

## runtime_guard

The pre-tool runtime decision layer that can issue `ALLOW`, `WARN`, or `BLOCK`.

## governance

The layer that records and reviews decisions without automatically becoming runtime execution.

## result handling

Additive post-tool control over returned output, such as redaction or blocking of release.

## audit trail

Structured evidence that supports later review of what happened and in what order.

## decision memory

Stored governance context or decision records used for traceability and later review.

## controlled override

A governance-layer request and decision process that is documented separately from runtime application.

## compat path

A non-core path that remains outside the official backbone and must stay distinguishable from it.

## official path

The documented public runtime backbone used as the reference execution model.

## proof area

A bounded part of the repository where an architectural claim is supported by curated public evidence.

