# AIOS Public Documentation Index

AIOS is presented publicly as **a governed execution layer for AI agents**.

This folder is the main public documentation package for the AIOS demo repository. It is aligned with current enterprise documentation and reports at a public-safe level: architecture, governance surfaces, internal/staging evidence, package/install checks, connector-readiness boundaries, and known limits.

## Canonical Backbone

```text
request -> planner -> execution_engine -> tool_registry -> runtime_guard -> tool -> result_gate -> result
```

## Current Public-Safe Reading

| Area | Public-safe reading |
| --- | --- |
| Enterprise track | Enterprise-staging-ready public demo/docs package, backed by internal/staging evidence. |
| Gate evidence | Expanded enterprise staging gate passed in internal reports. |
| Package evidence | Non-editable package/install checks passed in controlled internal validation. |
| Test evidence | Enterprise reports include a passing full suite, latest read report showing 516 tests OK. |
| Governance evidence | Runtime hardening, governance hardening, and runtime governance wiring are documented internally. |
| Connector evidence | Connector-readiness audit completed; minimal connector shape demonstrated; real external-agent target integration remains future work. |
| Public boundary | Source-private core; no private runtime source or raw internal reports published here. |

## Documents

| Document | Purpose |
| --- | --- |
| [AIOS_PUBLIC_OVERVIEW.md](AIOS_PUBLIC_OVERVIEW.md) | Short explanation of what AIOS is and current public-safe enterprise alignment. |
| [AIOS_ARCHITECTURE.md](AIOS_ARCHITECTURE.md) | Component-level view of the governed execution path. |
| [AIOS_GOVERNANCE_MODEL.md](AIOS_GOVERNANCE_MODEL.md) | Public governance surfaces and control semantics. |
| [AIOS_DEMO_AND_EVIDENCE_PACKAGE.md](AIOS_DEMO_AND_EVIDENCE_PACKAGE.md) | What can be run publicly and what enterprise evidence is summarized. |
| [AIOS_AGENT_INTEGRATION_READINESS.md](AIOS_AGENT_INTEGRATION_READINESS.md) | How external agent integration can be evaluated safely. |
| [AIOS_STATUS_AND_LIMITS.md](AIOS_STATUS_AND_LIMITS.md) | Public status, boundaries, and claim limits. |
| [AIOS_PUBLIC_ROADMAP.md](AIOS_PUBLIC_ROADMAP.md) | Public-facing roadmap for documentation and demo hardening. |
| [AIOS_FAQ.md](AIOS_FAQ.md) | Public Q&A for technical reviewers. |
| [AIOS_PUBLIC_UPDATE_LOG.md](AIOS_PUBLIC_UPDATE_LOG.md) | Public update trail for this demo package. |

## Public Scope

This folder documents:

- the public AIOS backbone
- the control model for tool execution
- public mock-runtime behavior
- public proof cases and adapted tests
- internal/staging evidence categories, summarized without raw private material
- the public/private boundary
- review and integration-evaluation posture

It does not publish the private AIOS runtime core, private source code, private package internals, private orchestration internals, private prompts, private memory surfaces, raw logs, raw traces, raw test files, or private environment wiring.

## Intended Reader

This package is written for technical reviewers, agent-framework evaluators, integration partners, and engineering teams who need to understand the AIOS control model before any controlled private integration discussion.
