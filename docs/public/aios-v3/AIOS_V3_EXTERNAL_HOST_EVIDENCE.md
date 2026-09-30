# External Host Governance

EA-0A and EA-0B are accepted in their declared scopes. This page records aggregate evidence through EA-0B Slice 3 as of 30 September 2026. The V3 runtime and its validation artifacts remain private.

> **External agents can propose. AIOS remains the execution authority.**

## Why this milestone matters

P3 accepted native sequential specialists coordinated inside one AIOS run. EA-0A and EA-0B extend the entry path: an external agent or harness can form a proposal outside AIOS and submit it to a governed boundary. The external process does not acquire policy, capability, budget, approval, execution, recovery, or result-release authority. EA-0B establishes the bounded host-side governance boundary needed before vendor-specific adapters are added.

## EA-0A — Preformed Proposal Admission

EA-0A accepted already formed host proposals into the existing AIOS governed execution path. The proposal remains non-authoritative; AIOS applies its normal governance and verifies the observed result. The accepted READ and approval-required WRITE/replay paths preserved their governance invariants with **zero model inference** in this entry path. EA-0A did not itself establish an external process gateway.

```text
External host forms a proposal
        ↓
AIOS admits it as a proposal, not as authority
        ↓
Existing governed execution path
```

## EA-0B Slice 1 — External READ

Slice 1 introduced a **vendor-neutral, versioned external-host admission boundary** across a real process boundary, with durable proposal identity and binding, governed READ, and observational status. Claimed host provenance does not grant authority. In the accepted bounded pilot, one READ dispatch was observed, with zero model inference. After restart, replay returned the historical governed result without silently rereading the changed target or creating another dispatch.

Here, *vendor-neutral* describes the contract, not ready-made support for every agent framework or transport.

## EA-0B Slice 2 — External WRITE / Approval / Resume

Slice 2 extended the boundary to a bounded external WRITE proposal:

```text
External WRITE proposal
  → durable approval wait; zero dispatch before approval
  → authoritative AIOS approval
  → external resume by proposal identity
  → same durable action
  → one observed governed dispatch in the accepted pilot
```

The external host cannot approve its own action or pass approval authority through the proposal or resume. AIOS retains one-shot approval, canonical target binding, execution, and result authority. Tested replay and restart continued the same action without a second effect in the accepted pilot; canonical target drift was blocked. This path used zero model inference. Ambiguous work retained a fail-closed recovery posture. These are replay-safe observations in the tested scope, not a universal exactly-once guarantee.

## EA-0B Slice 3 — Tested OS Isolation

The accepted pilot ran on macOS with **two distinct OS principals**. In the tested configuration, the external host principal could not directly access the protected AIOS resources covered by the pilot; the tested READ and WRITE operations used the EA-0B governed channel. Direct access and bypass attempts within that perimeter were denied by the operating system. The final hostile probe observed **487 denied operations** and an unchanged protected tree before and after. A final leakage audit checked **31 host-visible files against 60 private values** and observed no leakage.

Governed READ and WRITE, approval/resume, replay, restart, canonical-target drift blocking, and ambiguous-recovery fencing retained the observed fail-closed posture in their tested scopes. At the final checkpoint, no existing SQLite WAL, SHM, or journal sidecar was present, so this evidence does **not** claim verified denial of access to an existing sidecar.

The OS result is limited to the tested macOS two-principal configuration and protected resources. It is not a universal sandbox or security certification.

## Authority Model

```text
External Agent / Harness
        ↓ proposal
AIOS External Host Boundary
        ↓
Governed Core (policy, capability, budget, approval)
        ↓
ExecutionEngine
        ↓
Observed effect / ResultGate
```

The host proposes. AIOS decides authority, approval, execution, recovery, and outward result. Native AIOS agents use the governed Core from inside AIOS; external hosts reach it through the bounded external-host entry.

## Validation Snapshot

| Private gate | Recorded result | Scope |
| --- | --- | --- |
| EA-0B Slice 1 full repository | 2,843 collected; 2,842 passed; 1 skipped; 0 failed; 12,240 subtests passed | External governed READ baseline |
| EA-0B Slice 2 full repository | 2,880 collected; 2,879 passed; 1 skipped; 0 failed; 12,282 subtests passed | Adds governed WRITE/approval/resume |
| **EA-0B Slice 3 canonical full repository** | **2,888 collected; 2,887 passed; 1 skipped; 0 failed/errors; 12,407 subtests passed** | Latest complete gate; **469 monitored source/test files byte-stable during the gate** |

These are separate private runs and must not be added together. The Slice 3 canonical gate followed a separate full run that failed in a command-sandbox environment because its broker could not bind a local socket; that failed run is not presented as a green gate. The canonical repeat passed in the intended environment. These private gates cannot be reproduced from the public V2-shaped mock runtime. Historical P2 and P3 gates are recorded separately in [Current Evidence](AIOS_V3_CURRENT_EVIDENCE.md).

## Limits

This evidence does not establish unrestricted production readiness, universal external-agent compatibility, ready-made Hermes/Codex/OpenCode/Anthropic adapters, MCP integration, universal provider support, a universal sandbox, security certification, general hostile-process containment, resistance to root/admin compromise or kernel exploits, every filesystem or storage configuration, universal crash recovery, or distributed exactly-once effects. A different host, identity, tool, deployment, or threat model needs its own validation.

Hermes direct-versus-governed and decision-source pilots are earlier experimental evidence, described in [Post-Core Evidence](AIOS_V3_POST_CORE_EVIDENCE.md). They are distinct from EA-0B. The public documents disclose aggregate properties, results, and limits, not private contracts, schemas, mechanisms, probes, or raw records. See [Status and Limits](AIOS_V3_STATUS_AND_LIMITS.md) and the [Public/Private Boundary](../../public-vs-private-boundary.md).
