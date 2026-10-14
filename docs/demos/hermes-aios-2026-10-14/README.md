# Live Demonstration — Hermes × AIOS

**14 October 2026 · Real provider · Bounded local experiment**

[![Hermes proposes; AIOS checks scope, requires human approval, executes and verifies the effect.](demo-flow.svg)](evidence-summary.md)

AIOS doesn't trust what an AI agent says it did.
It verifies what actually happened.

## What happened

Hermes **0.21.0**, using DeepSeek **`deepseek-v4-flash`**, submitted requests through the existing **AIOS governed adapter**. The experiment combined a real model provider with a bounded synthetic report in a local laboratory. AIOS controlled the tool operations forwarded through that adapter.

| Step | Observed outcome |
| --- | --- |
| Authorized READ | **ALLOWED** — AIOS returned the in-scope report with a total of 2. |
| Out-of-scope READ | **BLOCKED BY GUARD** — the runtime guard rejected the attempted read; no external content was returned. |
| WRITE proposal | **WAITING_APPROVAL** — the proposed change remained suspended and the report still contained a total of 2. |
| Explicit human approval | **APPROVED** — the operator separately approved the corrected proposal and its digest. |
| Governed resume | **WRITE COMPLETED** — AIOS executed the approved change; the gateway reported `COMPLETED` and 26 bytes written. |
| Independent effect verification | **EXECUTION VERIFIED** — the actual file matched the approved request and recorded result; RunStore reported `SUCCEEDED` / `COMMITTED` / `FINALIZED`, and ResultGate returned `ALLOW`. |

The blocked READ was a **runtime guard rejection**. Policy admitted the request to the next check; the evidence does **not** show a policy `DENY` for that read. The infographic uses human-readable outcome labels; the [evidence summary](evidence-summary.md) distinguishes them from recorded runtime states.

## Agent response and execution truth

After the governed resume, Hermes encountered an error in its final response and did not produce its final conversational summary. By that point, AIOS had already independently verified the file change through filesystem evidence, RunStore and ResultGate.

The observed response error does **not** establish a DeepSeek rate limit. No cause is asserted without evidence. The verification did not retry the WRITE or send another provider request.

## Limits

- This is a **demo with a real provider** on a bounded synthetic local task.
- It is **not a security certification** or a production-readiness claim.
- It is **not the LIVE RM-22 qualification**; RM-22 remains blocked before LIVE.
- It provides **no evidence of isolation between macOS users**.
- **Only the AIOS tools used in this experiment are governed**. Other Hermes tools and arbitrary agent actions are outside this demonstration's governance claim.
- READ and WRITE used separate runtimes and RunStores; this is not evidence of a single unified deployment.

## Evidence and disclosure

This page summarizes the original operator report dated 14 October 2026 and its documented checks. It does not rerun the experiment or expose the private runtime. [Read the sanitized evidence summary](evidence-summary.md).

The private Core and adapter were used as they existed. This publication adds documentation only. Private source, personal directories, credentials, databases, full logs and confidential configuration are excluded.

[Repository homepage](../../../README.md) · [Public/private disclosure boundary](../../public-vs-private-boundary.md)
