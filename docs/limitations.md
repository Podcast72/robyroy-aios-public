# Limitations

AIOS V3 P0 is complete in its declared validation scope, but this public repository and the evidence it publishes remain intentionally limited.

## Milestone Limit

`AIOS_V3_P0_GATE=PASS`, **562/562 targeted P0 tests PASS**, and **354/354 Adversarial Remediation Gate PASS** describe named private validation scopes.

They do not mean:

- unrestricted production or release readiness;
- security certification or formal verification;
- universal provider, model, tool, or integration support;
- elimination of every failure, bypass, or adversarial condition;
- correctness in every deployment environment.

The named test counts are separate gate results and are not presented as one combined unique-test total.

## Live Provider Limit

One real OpenAI provider invocation through the governed path used exact model `gpt-5.6-sol` and returned `AIOS_LIVE_OK`.

That observation is not a latency, cost, scale, availability, reliability, or provider-security benchmark. “No raw-secret leak observed” applies only to that observed path; it is not a universal no-leak guarantee.

## Persistence And Recovery Limit

Persistence, reopen, replay, and resume were verified in the synthetic P0 scope. The result depends on the tested execution identity and authoritative persistence assumptions.

`UNKNOWN_EFFECT` prevents blind automatic re-execution when an external effect may have occurred but cannot be proven. It does not guarantee that the external outcome can always be reconstructed. The public evidence does not claim distributed exactly-once semantics or independent multi-host correctness.

## Public Implementation Limit

The private V3 runtime is not distributed here. This repository does not publish:

- V3 source or implementation-sensitive details;
- private test source or fixtures;
- raw `RunStore` schema;
- private authorization, approval, and trust-boundary mechanisms;
- exploit or adversarial probe details;
- private prompts or operator internals;
- local paths, credentials, raw audit/log/trace data, private configuration, or deployment internals.

As a result, the V3 gate evidence cannot be reproduced from this public repository alone.

## Public Demonstration Limit

The runnable public mock and public invariant tests remain intentionally V2-shaped. They demonstrate the earlier governed-backbone model:

`request -> planner -> execution_engine -> tool_registry -> runtime_guard -> tool -> result_gate -> result`

They are not a reduced V3 runtime and must not be used to infer private V3 implementation details.

## Historical Evidence Limit

The V2 field tests, proof tests, at-most-once evidence, and enterprise-suite snapshots retain the claim limits stated in their own documents. V3 does not broaden those historical results.

## Disclosure Model

The repository uses **bounded technical disclosure**: enough architecture, properties, aggregate evidence, and limits for public review without publishing the mechanisms required to replicate the private runtime.
