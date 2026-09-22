# Open Governed Capability Execution Kernel

## Status

This document describes a **proposed future Restack project**. It does not claim that the project or its deliverables are already implemented, funded, selected, or available in this repository.

## Proposed Purpose

The proposed project would develop a small, standalone capability-execution kernel for networked software. Its purpose would be to make security-sensitive operations explicit, bounded, reviewable, and recoverable without tying execution authority to an application, automation framework, model provider, or proprietary runtime.

The kernel would be designed for ordinary software and service workflows. A caller would request a declared capability; the kernel would validate the request against explicit authority, maintain authoritative execution state, control result release, and preserve evidence for audit and recovery.

## Model-Neutral And Non-AI Scope

The proposed kernel would not require or embed:

- a large language model or other generative model;
- an agent framework;
- OpenAI or another model provider;
- model training, fine-tuning, inference, integration, or evaluation;
- AI-specific planning or orchestration;
- the private AIOS V3 runtime.

An AI-enabled application could be one possible external caller, just as a conventional web service, command-line tool, scheduler, deployment system, or administrative application could be. No caller would obtain execution authority merely by proposing an action.

## Standalone Open-Source Boundary

If the proposal is selected, the funded project results would be developed publicly and published in their entirety under a recognised free/libre/open source licence. This would include the kernel implementation, public interfaces, tests, specifications, documentation, examples, and reproducible validation material produced within the funded scope.

The proposed kernel would remain usable, testable, and maintainable without access to private AIOS V3 source, private fixtures, internal schemas, private services, or proprietary model APIs. No private component would be required to build, run, validate, or extend the funded result.

## Relationship To Existing AIOS Work

AIOS is existing work concerned with governed execution in agent and AI-assisted systems. The public material in this repository provides background, terminology, historical evidence, and bounded engineering experience.

The proposed Restack project is different:

| Existing AIOS material | Proposed Restack project |
| --- | --- |
| AI and agent-runtime context | General networked-software context |
| Private V3 implementation with aggregate public evidence | Fully public implementation and validation material |
| Existing milestones and historical results | Future work performed only after selection and agreement |
| Model and tool execution within an agent runtime | Model-neutral capability execution independent of agents |

Existing AIOS functionality would not be rebilled as new Restack work. The proposed work would have its own public implementation, issue history, tests, documentation, milestones, and acceptance evidence.

## Proposed Technical Boundary

Subject to final agreement with NLnet, the proposed work would concentrate on reusable, non-AI infrastructure such as:

- declarative capability descriptions and stable public interfaces;
- explicit authorization and request binding;
- deterministic admission and execution-state transitions;
- bounded execution adapters for conventional software operations;
- audit records and controlled result release;
- fail-closed retry, replay, and uncertain-effect handling;
- conformance tests, documentation, packaging, and reproducible examples.

These are proposed work areas, not statements of completed deliverables.

## Licensing And Governance Intent

The repository currently uses the MIT License. The precise recognised free/libre/open source licence for the proposed kernel would be confirmed before funded implementation begins and applied to the complete funded result. Contributions would be accepted only where the project has the rights needed to publish and redistribute them under that licence.

No patent grant, third-party right, contributor agreement, or ownership fact beyond the contents of the applicable licence is asserted by this document.

## Restack Relevance

The proposal is intended as reusable trust and security infrastructure for an open internet stack: a small independent layer that can help different applications and services constrain operational capabilities, separate requests from execution authority, preserve reviewable evidence, and fail closed when effects are uncertain.

Its value would depend on interoperability, independent reuse, complete open-source availability, and the absence of any dependency on a single vendor, model provider, closed application, or private AIOS component.
