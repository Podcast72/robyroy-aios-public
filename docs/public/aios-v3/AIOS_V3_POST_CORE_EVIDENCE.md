# AIOS V3 — Post-Core Evidence

This page summarizes evidence after the frozen P2.7 / R2.7 governed-core baseline, as of 29 September 2026. It is an aggregate public record, not a runtime distribution, audit certificate, or claim of unrestricted production readiness.

## 1. Frozen governed-core baseline

P2.0–P2.7 were accepted in their declared scopes. R2.7 remediation and closeout completed. **P2.7 / R2.7 remains FROZEN; the governed Core remains AGENT-READY.** The recorded complete `tests_v2 + tests_v3` regression for that runtime baseline was **2510 passed, 1 skipped, 11350 subtests passed**. The final documentation-only closeout reported a separate targeted retest of **5 passed**; it did not rerun that complete suite. These are historical P2.7 / R2.7 results, not P3 results.

## 2. External read-only technical review

A separate **external model-assisted read-only technical review / audit** used Hermes with DeepSeek V4 Pro. Its findings were inputs to engineering verification and remediation. The review was not a security certification, penetration-test certification, formal verification, or independent commercial certification. Read-only refers to the review activity; subsequent remediation changed the private runtime through separately validated work.

The documented sequence includes the NF-01 unresolved-effect fence, M-02R controlled READ presentation remediation, P2.6 remaining accepted in its declared scope, and R2.7 filesystem ambiguity/recovery and result-exposure remediation. The R2.7 closeout recorded focused retests after those changes. The named R2.7 filesystem identity/recovery and result-exposure findings were remediated within that scope; a separate residual note remained accepted as a limitation. This page makes no global claim that every high or critical risk in every threat model was eliminated.

## 3. P3 native multi-agent governance

The private acceptance tag is `P3_NATIVE_MULTI_AGENT_LIVE_ACCEPTED` at commit `9c26745c402c589c767d0e82b9b07ed8efa0e5a2` (29 September 2026). Four accepted slices added sequential Coordinator, Analyst, Challenger, and Operator roles inside one AIOS `AgentLoop`, session, root run, and shared budget. Delegation does not grant a new execution authority. Model calls and tools remain governed; only the Coordinator completes the final answer.

The accepted live pilot used OpenAI model `gpt-5.6-sol` on a synthetic task and followed:

```text
Coordinator -> Analyst -> Coordinator -> Challenger -> Coordinator
-> Operator -> governed WRITE -> Operator -> Coordinator -> final
```

It recorded **10 governed model inferences, 10 network calls, 3 governed tool calls** (2 READ, 1 WRITE), **0 retries**, a real READ, a real bounded WRITE after ordinary approval, and one observed effect. Replay of the completed run did not duplicate that WRITE. The first separate pilot attempt failed closed on an invalid control response before any READ, WRITE, or approval; the accepted pilot was a fresh run.

The post-pilot **`tests_v3`** gate on the final runtime/test tree reported **1753 passed, 1 skipped, 1209 subtests passed**, exit 0 (0 failures and 0 errors in JUnit). It is a different suite and date from the P2.7 / R2.7 `tests_v2 + tests_v3` gate; their counts must not be added or compared as a single trend. The separate targeted Slice 1–4 and related gate reported **164 passed, 77 subtests passed**.

The P3.6a `approval_wait_already_resumed` limitation remains open for further steps in the same root run after that distinct bounded wait. The accepted pilot used ordinary approval. It did not inject a live crash or prove distributed exactly-once behavior.

## 4. Hermes direct and governed experiments

The A/B experiment compared authority paths, not model quality or throughput:

```text
DIRECT:   Hermes -> native tool authority -> real filesystem effect
GOVERNED: Hermes -> proposed decision -> AIOS governance -> admitted execution
        -> effect observation -> ResultGate
```

In the direct pilot, Hermes read the task, used its native tools, and produced the filesystem effect directly. AIOS was not on that effect path. In the governed filesystem pilot, the target remained unchanged while AIOS was `AWAITING_APPROVAL`, with zero dispatch and no effect. An initial worker error remained fail-closed without the effect. After a valid approval, the accepted run recorded `SUCCEEDED`, `FINALIZED`, consumed approval, **one filesystem dispatch**, effect observation matching the expected effect, and `ResultGate` `ALLOW`.

**Pilot 03 — Hermes decides, AIOS executes:** Hermes supplied only a decision artifact through an experimental adapter. AIOS retained policy, capability, budget, approval, trust, execution, observation, ResultGate, and authoritative execution evidence. The private evidence reports equal SHA-256 bindings for Hermes proposed content, the admitted tool call, AIOS expected and observed content, and the final filesystem content; `bindings_ok = true`, exit 0.

**An external agent was experimentally used as the decision source while AIOS retained execution authority and produced and verified the admitted effect.** This is experimental integration evidence, not a production Hermes integration or a permanent live Hermes transport.

## Limits and non-claims

Native AIOS multi-agent support, the OpenAI model provider, the unimplemented OpenAI Agents SDK integration, and the experimental Hermes decision-source adapter are distinct. No external SDK runtime was introduced by P3. The evidence does not establish unrestricted production readiness, general agent safety, arbitrary filesystem WRITE, universal provider support, a certified audit, or universal duplicate-effect prevention. The public V2 mock remains V2-shaped. Private source, fixtures, databases, proposal/evidence artifacts, prompts, paths, credentials, traces, and implementation-sensitive mechanisms remain private.
