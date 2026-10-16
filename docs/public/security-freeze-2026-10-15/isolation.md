# How Hermes, AIOS and the operator are separated

[Overview](README.md) · **Role separation** · [Evidence and limits](evidence-and-limits.md)

**Scope: the macOS laboratory preserved on 15 October 2026.** “Isolation” here means specific separations of responsibility and OS access, backed by the observations described below.

## Different roles, different authority

Think of a proposed file change as a request that must pass through an accountable decision process. Writing a convincing request does not grant permission to carry it out.

| Role | Responsibility | Boundary |
| --- | --- | --- |
| **Hermes — the proposer** | Interprets the task and submits requests through the governed integration. | Its text does not grant policy permission or human approval. |
| **AIOS — the governed runtime** | Applies the rules, holds work that requires approval, executes admitted actions and records observed results. | AIOS retains execution and result-release authority on this path. |
| **Human operator — the decision maker** | Reviews requests that require a human decision through a separate administrative console. | Approval or rejection is a distinct event, outside the agent's narrative. |
| **macOS — the OS boundary** | Enforces the tested accounts' access to processes, directories and files. | OS access checks are separate from application policy decisions. |

The installation used distinct standard OS accounts for the agent and the AIOS host. The operator console was a separate administrative route to the existing host. This does not claim three isolated OS accounts: the separation of the operator is a decision and administration boundary.

## Application rules and OS protection answer different questions

**AIOS policy asks: “Is this requested action allowed?”** The preserved record contains three policy-denied writes to a protected resource, correlated with the active policy and authoritative execution history. The tool did not execute for those requests. These denials were application decisions.

**macOS asks: “May this process access this protected location?”** Separate direct rename and create attempts under the tested agent identity were denied by the OS. Checks under the host identity found the original unchanged. These observations concern the tested account, protected location and operations.

Keeping those results separate matters. An application denial does not prove that the OS blocked a direct attempt. An OS denial does not prove that a particular Hermes tool was exercised. The retained OS observations are not Hermes move/create tool tests.

The two forms of evidence support separate layers in the tested arrangement. They do not establish protection for every Hermes tool, every path, arbitrary network traffic, or every possible compromised process.

## A human decision is an event, not a sentence

For the approval-controlled resource, the preserved sequence was:

1. A proposed change entered an approval wait.
2. The operator rejected the request through the separate console.
3. The persistent execution record identified operator rejection and no resume.

An agent saying “approved” would not substitute for that decision. In this record, no positive approval grant was present, so a successful approved write is not claimed.

Another request remained waiting beyond its deadline when captured. Preserving it does not mean it was approved, resumed, automatically reconciled or cleanly closed. The freeze did not alter the state to make the record appear complete.

## Why the console uses the existing host

The preserved laboratory procedure connects the operator console to the host that already owns execution state. It does not create a second runtime for the same pending work. This keeps observation and operator decisions tied to the existing execution authority.

That is an architectural explanation, not an operating recipe. Commands, sockets, account identifiers, policy bindings and deployment details remain private under the [disclosure boundary](../../public-vs-private-boundary.md).

## What another Mac would need

The private rebuild procedure describes a new installation using verified copies and the actual installed package, with the documented corrections distinguished from the earlier provisioning archive. It is a preserved procedure; the freeze did not perform that future rebuild.

A new installation must resolve its own identities and permissions, create fresh credentials and filesystem bindings, and verify the installed bytes and applicable boundaries. Old account numbers, file identities or approvals cannot be treated as authority on another machine. Sanitized forensic snapshots cannot restore the original authenticated state.

**The earlier PASS results do not transfer automatically to another Mac, volume, package or deployment.** The evidence page explains exactly what was preserved and what remains outside qualification.

[Read the evidence and limits](evidence-and-limits.md) · [Back to overview](README.md) · [Repository home](../../../README.md)
