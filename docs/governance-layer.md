# Governance Layer

The governance layer is documented here as a distinct concern from runtime execution.
Its role is to record, review, approve, deny, or revoke governance decisions without pretending that those decisions automatically become runtime actions.

## Public scope

Within the perimeter of this repository, governance covers topics such as:

- audit trail references
- decision memory
- controlled override requests
- approvals, denials, revocations, and review context

## Separation from runtime execution

The public boundary is deliberate.
Governance can authorize a governance decision, record the decision, and preserve its context.
That does not mean the same decision becomes an automatic runtime bypass.

A governance approval does not silently become runtime application.

This matters because otherwise the repository would blur together:

- approval at the governance layer
- execution authority at runtime
- tool access in the official backbone

Those are related concerns, but they are not interchangeable.

## Controlled override

The public example in this repository uses a governance override case with an intentionally conservative interpretation:

- the request is reviewed
- the status may become `approved`
- the approval scope remains governance-only
- runtime effect remains `none`
- the official backbone remains unchanged

This is not presented as a loophole around the runtime guard.
It is presented as evidence that governance decisions can be explicit without silently rewriting runtime execution.

## Public references

- [`examples/governance-override-example.json`](../examples/governance-override-example.json)
- [`docs/auditability.md`](auditability.md)
- [`docs/official-vs-compat-paths.md`](official-vs-compat-paths.md)

