# At-Most-Once Execution Evidence

This document summarizes public-safe evidence for AIOS at-most-once execution semantics in the current private enterprise runtime.

It does not publish private source code, raw tests, local paths, internal fixtures, or implementation details.

## Why This Matters

AI agents can perform actions with real side effects.

A difficult failure case occurs when an action may already have completed but the runtime crashes before it can persist a final acknowledgement.

Blind retry in that situation can duplicate the side effect.

AIOS therefore treats uncertain post-execution failure conservatively.

## Public State Model

ABSENT -> PREPARED -> AUTHORIZED -> RUNNING -> SUCCEEDED | FAILED | UNKNOWN_EFFECT

### ABSENT

No authoritative execution record exists yet.

### PREPARED

Execution ownership and required accounting reservation have been established.

### AUTHORIZED

Required authorization has been accepted for the governed execution.

### RUNNING

The runtime has persisted that execution is entering the side-effect-capable phase.

### SUCCEEDED

Execution completed successfully. Replay returns the recorded terminal result without another tool invocation.

### FAILED

Execution failed in a state that can be represented authoritatively as terminal.

### UNKNOWN_EFFECT

The runtime cannot safely prove whether the external side effect occurred.

This state is intentionally non-retryable by default.

## Verified Properties

| Property | Public-safe result |
| --- | --- |
| Duplicate execution protection | Verified in declared scope |
| Atomic execution ownership | Verified |
| Budget/accounting consistency | Verified under tested concurrency |
| Concurrent caller exclusion | Verified |
| Recovery before possible effect | Conservative terminal handling |
| Recovery after possible effect | `UNKNOWN_EFFECT` |
| Terminal replay semantics | No second tool call |
| Blind retry from uncertain effect | Blocked |

## Adversarial Validation

Public-safe validation included:

- concurrent owner and recovery races
- multiple callers competing for the same logical execution
- a tangible filesystem append used as a real side-effect probe
- failure after the possible side effect and before normal finalization
- audit failure after successful run finalization
- repeated race stress validation: **125/125 passed**
- current private enterprise suite: **927 tests passed + 6525 subtests passed**

The purpose of these tests was not only to exercise happy paths, but to attempt to falsify the at-most-once guarantee under timing and failure conditions.

## Important Limit

`ACCOUNTING_AUDIT_CONVERGENCE = PARTIAL`

A narrow ambiguity remains for external audit delivery.

An external audit sink may complete its write before the runtime records the acknowledgement. If the runtime crashes in that window, it cannot safely distinguish:

- audit not written
- audit written but acknowledgement not persisted

AIOS therefore does not automatically resend the audit, because blind resend could duplicate the record.

A stronger future model could use a transactional outbox together with an idempotent audit sink.

This is an architectural evolution path, not a current production-readiness claim.

## Scope

The at-most-once verification applies within the declared current runtime scope:

- callers share the same authoritative persistent RunStore
- callers use the same logical execution/request identity
- concurrent access was tested against the current runtime
- terminal execution identity is not silently reopened

The evidence does not claim:

- correctness after loss of the authoritative database
- independent multi-host execution without shared authoritative state
- distributed exactly-once semantics
- unrestricted production readiness
- universal behavior outside the tested runtime boundary

## Current Result

AT_MOST_ONCE_VERIFIED = YES

ACCOUNTING_AUDIT_CONVERGENCE = PARTIAL

The public interpretation is deliberately conservative:

AIOS governs not only whether an action may execute, but also how uncertain execution outcomes are handled under concurrency, retries, crashes, and partial failures.
