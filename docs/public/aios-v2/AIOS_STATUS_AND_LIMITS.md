# AIOS Status And Limits

This repository is a public technical package for AIOS.

## Public Status

| Area | Public status |
| --- | --- |
| Repository type | Demo and documentation repository |
| Runtime core | Source-private, not published here |
| Public demo | Small public/demo tests, mock runtime proof tests and proof cases |
| Enterprise alignment | Public-safe summary of internal/staging evidence |
| Enterprise staging gate | Passed in internal reports with a non-public-distribution posture |
| Package/installability | Controlled non-editable package/install checks passed internally |
| Governance wiring | E2E enforcement demonstrated internally through planned-step runtime path |
| Result boundary | Internal/staging reports document result-gate hardening and raw-output protection |
| Audit/replay | Internal/staging reports document minimal audit/replay and trace evidence |
| Connector posture | Adapter-based external-agent evaluation prepared; real third-party integration not started |
| Review posture | Prepared for controlled technical review |
| Integration posture | Prepared for controlled agent-integration evaluation |

## Evidence Supported

- enterprise-staging-ready documentation/demo package
- small public test surface plus selected public-safe evidence summaries
- package/installability checks passed in controlled internal validation
- latest read enterprise report records 927 passing tests + 6525 subtests in the private enterprise/staging validation scope
- runtime hardening and result-boundary evidence exists internally
- policy/capability/approval/budget/memory/state/supervision governance categories are documented internally
- allow/warn/block, fail-closed, and no-silent-fallback behavior are covered in internal/staging evidence
- audit/replay-oriented trace evidence exists internally
- connector-readiness audit and minimal connector shape support controlled pilot evaluation

## At-Most-Once Execution Semantics

The current private enterprise runtime has been adversarially validated for at-most-once execution semantics within a declared persistent-runtime scope.

Public-safe state model:

ABSENT -> PREPARED -> AUTHORIZED -> RUNNING -> SUCCEEDED | FAILED | UNKNOWN_EFFECT

`UNKNOWN_EFFECT` is intentionally conservative. It represents a case where execution may already have produced an external side effect, but the runtime cannot prove the final effect state. AIOS does not automatically retry from this state.

Verified public-safe properties include:

- duplicate callers cannot acquire duplicate execution ownership for the same logical execution identity
- claim and budget reservation remain coherent under tested concurrent access
- terminal states are not reopened
- successful terminal execution is replayed without another tool call
- uncertain post-execution failure converges to `UNKNOWN_EFFECT`
- blind retry from `UNKNOWN_EFFECT` is blocked
- repeated race validation completed **125/125** checks successfully
- the current private enterprise suite records **927 passing tests + 6525 subtests**

### Declared scope

The verification applies to callers that share the same persistent runtime state and the same logical execution/request identity.

It does not claim:

- correctness after loss of the persistent RunStore
- independent multi-host execution without shared authoritative storage
- distributed exactly-once semantics
- unrestricted production readiness

### Accounting and audit limit

`ACCOUNTING_AUDIT_CONVERGENCE = PARTIAL`

A narrow crash window remains around external audit delivery: an audit sink may complete an external write before the runtime records the acknowledgement.

AIOS does not automatically resend that audit because blind resend could create a duplicate audit record.

A stronger future guarantee would require a transactional outbox and an idempotent audit sink. That is documented as an architectural evolution path, not as a current mandatory remediation.

AT_MOST_ONCE_VERIFIED = YES
ACCOUNTING_AUDIT_CONVERGENCE = PARTIAL

See [At-Most-Once Execution Evidence](AT_MOST_ONCE_EXECUTION_EVIDENCE.md).

## What This Status Supports

- public architecture discussion
- public demo inspection
- public proof-case review
- controlled technical review
- controlled agent-integration evaluation
- comparison of governed and direct agent execution patterns

## What This Status Does Not Support

- treating this repository as the private runtime core
- assuming private source code is published here
- treating mock artifacts as full operational evidence
- assuming unrestricted deployment maturity
- assuming every private subsystem is represented one-to-one
- assuming external security, legal, compliance, or customer-environment validation
- assuming real third-party agent integration is already complete

## Public Limits

- The public mock runtime is intentionally minimal.
- Public examples are curated.
- Public tests are adapted to stand alone outside private internals.
- The 927 passing tests + 6525 subtests belong to the internal enterprise/staging validation scope, not this public repository.
- Enterprise reports are summarized rather than copied.
- Private runtime files, prompts, memory surfaces, package internals, and environment wiring are not included.
- Raw logs, raw traces, raw test files, machine paths, and implementation internals are not public material.
- Any external evaluation should keep the public/private boundary intact.
