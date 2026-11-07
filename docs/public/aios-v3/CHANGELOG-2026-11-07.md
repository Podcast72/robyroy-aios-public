# Five governed filesystem capabilities — 7 November 2026

**LIVE_PASS · 5/5.** One bounded OpenAI GPT-4.1 campaign passed CREATE, READ, REPLACE, MOVE and DELETE on AIOS V3 Enterprise in the tested synthetic macOS profile with separate agent and Core principals.

## What changed since the previous public update

| Evidence | Recorded outcome |
| --- | --- |
| Five-capability OpenAI campaign | All five capabilities passed in one campaign. AIOS verified policy decisions, operator approvals for REPLACE and MOVE, a rejected CREATE, denied DELETE cases, observed results and persistent Core receipts. |
| OpenAI usage and cost | `gpt-4.1-2025-04-14` on `aios-live-agent` · 9 requests · 1,683 input tokens · 156 output tokens · **0.004614 USD** reconciled against the official OpenAI cost export for formal closeout. |
| Canonical OFFLINE baseline, 6 November | **3,961 PASS / 0 FAIL / 1 historical SKIP**, recorded separately from installed and provider-live testing. |
| Earlier LIVE campaigns | R7.1 Hermes/DeepSeek CREATE, MOVE and DELETE and the earlier RM-22 READ and REPLACE results retain their respective candidate and campaign scopes. |

## Provenance and verification level

This update summarizes the maintainer's closed campaign record, retained qualification evidence and OpenAI project usage and cost records. The local SHA-256 manifest was verified for this publication. The public repository contains aggregate results. Its executable tests cover the V2 demonstration and public package.

The verdict is limited to the tested profile and filesystem capabilities. General security certification and universal production readiness remain outside its scope. `shell.execute` remains `CONTAINMENT_UNAVAILABLE`.

[Qualification record](AIOS_V3_RELEASE_QUALIFICATION.md#unified-files-policy-governance) · [Status and limits](AIOS_V3_STATUS_AND_LIMITS.md)
