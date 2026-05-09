# RobyRoy AIOS

<p align="center">
  <img src="assets/aios-demo-hero.png" alt="AIOS demo architecture" width="100%">
</p>

Visual overview of the public AIOS demo architecture and its governed execution path.

_Public architecture, governance model, and technical proofs_

RobyRoy AIOS is presented here as a governed execution architecture for AI-assisted systems.
This public repository explains how the project approaches execution control, tool access mediation, result handling, and auditability.
It does not expose the full private operational codebase.

This repository should be read as a public technical reference and architecture disclosure.
It shows the official backbone, the public/private boundary, a selective set of technical proofs, and a small public mock runtime.
The emphasis is on declared invariants, explicit separations, and public evidence rather than broad architectural claims.
It should not be read as a mini product build, a public copy of the private core, or a wrapper-style demo standing in for the whole system.

The public reason for this repository is straightforward.
Once a system can decide, call tools, cross runtime paths, produce results, and potentially trigger real side effects, output generation alone is not enough.
Tool access mediation, execution clarity, separation between runtime and governance, control over result handling, and auditability become first-class architectural concerns.

This repository exists to make that direction readable in a sober and technical way.
It is not a brochure and it is not a public dump of the internal system.
It is a curated public-facing reference for how RobyRoy AIOS frames governed execution.

## AIOS Governed Execution Architecture

### 1. Why AIOS exists

Modern AI systems can answer users, analyze documents, call APIs, coordinate agents and automate workflows.
This creates real value through speed, productivity and automation.
But the moment AI starts using tools, accessing data or triggering workflows, the problem changes.
The risk is no longer only what the model says.
The risk is what the model-driven process is allowed to do before the final answer reaches the user.

As long as AI writes, the risk is limited. When AI acts, governance becomes necessary.

### 2. The risk shift: from response to action

When AI moves from response generation into operational execution, the system must address a different class of risk:

- Scope: AI can exceed the intended operating scope.
- Tool: AI can use undeclared or unauthorized tools.
- Output: AI can produce ambiguous or unvalidated results.
- Fallback: AI can degrade into silent fallback paths.

When AI uses APIs, data, tools or enterprise workflows, the execution path needs identity, permissions, limits, approval, result gate, and audit.

### 3. The limit of traditional AI architectures

Many AI architectures concentrate too much decision power around the model.
The model may influence tool choice, parameters and operating path.
Controls are often external, partial or applied afterward.
Audit is fragile when it is hard to reconstruct why an action was executed.
This can be powerful, but fragile.

Traditional path:

```text
model -> tool -> output
```

AIOS path:

```text
plan -> governance -> tool -> gate -> auditable result
```

### 4. What AIOS introduces

AIOS does not replace the model.
AIOS governs the path between request, tool and result.

> The model does not act directly. It plans. AIOS governs.

- The model plans.
- AIOS evaluates identity, permissions, policy and limits.
- Tools are accessed only through declared and controlled paths.
- The result passes through validation and result handling before reaching the user.
- The goal is to make AI act within verifiable rules.

### 5. Governed execution path

The public governed backbone is:

```text
request -> planner -> execution_engine -> tool_registry -> runtime_guard -> tool -> result
```

- `request`: the user or system request entering the governed flow
- `planner`: interprets the request and prepares a controlled execution plan
- `execution_engine`: executes planned steps instead of letting the model act directly
- `tool_registry`: exposes only declared and registered tools
- `runtime_guard`: can `ALLOW`, `WARN`, `BLOCK` or require approval before tool execution
- `tool`: executes only inside the governed path
- `result_gate / result handling`: validates, controls or blocks unsafe or invalid output before response
- `result`: the final governed output returned to the user

If you are reading the repository for technical reference, the narrower `Official runtime backbone` section below remains the precise public path statement. This section adds the narrative context for why that path matters.

### 6. From isolated controls to a governed path

The value is not simply having multiple controls.
The value is preventing the system from silently skipping the governed path.

- Before: identity, permissions, policy and budget define the scope.
- During: runtime guard, tool contract and supervision prevent deviations.
- After: result gate and audit replay make the result controlled and reconstructable.

No silent fallback. Skips are blocked or made explicit.

### 7. Enterprise governance layers

| Layer | Meaning |
| --- | --- |
| Agent Identity | who is acting |
| Capability Permissions | what it can do |
| Budget & Limits | how much it can consume |
| State Control | state is not authorization |
| Approval Gates | sensitive actions can be paused |
| Memory Governance | memory access remains controlled |
| Tool Contract | tools must be declared and bound |
| Run Supervision | loops, retries and escalation stay visible |
| Audit Replay | runs can be reconstructed |
| Policy Packs | different operational postures can be applied |

Every AI action should be authorized, limited, traceable and validatable.

### 8. Technical difference from traditional AI solutions

| Traditional AI approach | AIOS governed approach |
| --- | --- |
| The model decides and acts | The model plans, AIOS governs |
| Tools can be called directly | Tools are accessed through the registry |
| Controls are external or partial | Controls are inside the runtime path |
| Output may be weakly validated | Result Gate before the response |
| Audit may be partial or missing | Trace and replay of the run |
| Fallbacks can be ambiguous | Fail-closed behavior and explicit blocks |

The difference is not “more AI”. The difference is AI under control.

### 9. Example business use case

A user asks AI to analyze business documents and prepare an operational result.

Without AIOS:

- the model interprets the request
- may use tools
- produces an output
- but it may be hard to know which steps were authorized, validated or blocked

With AIOS:

- identity is checked
- permissions are evaluated
- available tools are limited to declared tools
- policy, budget and tool contracts are applied
- violations can be blocked
- the result is validated
- the run trace is saved or reconstructable

The customer does not just get an answer. They get a governed answer.

### 10. Benefits for companies and teams

From an architectural perspective, AIOS is valuable because it separates decision generation from authorization and execution. That creates a clearer control surface for pilots where organizations need to understand which actions are allowed, which are blocked, and how results are handled.

- Control: separation between model, authorization and execution
- Security: explicit blocks, runtime policy and fail-closed behavior
- Audit: reconstructable run showing who, what, why and with which limits
- Scalability: common foundation for business agents, tools and workflows

This repository presents that value as a governance model and a controlled pilot direction, not as a claim that every layer is already fully deployed in the same way everywhere.

### 11. Adoption path

The right path is not to start from everything at once, but from a governable scope.

1. Choose a controllable use case.
2. Define policy, permissions, limits and operating posture.
3. Connect declared tools.
4. Run controlled demos or pilot runs.
5. Audit, correct and extend progressively.

Progressive adoption means first governing one scope well, then extending only after audit and validation.

### 12. Visual architecture presentation

AIOS is also documented through a visual architecture presentation for readers who cannot run the internal or private demo. The presentation explains the risk shift from AI responses to AI actions, the governed execution path, the enterprise governance layers, the difference from direct AI tool use, and the controlled pilot direction.

[Download the AIOS Governed AI Execution Layer PDF](docs/public/AIOS_Governed_AI_Execution_Layer.pdf)

## Start here

- [`docs/what-aios-is-and-is-not.md`](docs/what-aios-is-and-is-not.md): Clear definition of what AIOS is, what it is not, and why this public repository exists.
- [`docs/public-vs-private-boundary.md`](docs/public-vs-private-boundary.md): Explicit boundary between what is published here and what is intentionally not public.
- [`docs/current-implemented-layers.md`](docs/current-implemented-layers.md): Short view of the currently documented public layers and what each one does or does not do.

## What this repository is

- A public technical repository for architecture, governance model, invariants, and technical proofs.
- A public technical reference and selective architecture disclosure rather than a product-style repository.
- A curated explanation of the official runtime backbone used as the public reference path.
- A selective set of examples and adapted public tests that make key invariants inspectable rather than rhetorical.
- A public-facing description of why governed execution matters for AI-assisted systems.

## What this repository is not

- It is not the full RobyRoy AIOS private operational codebase.
- It is not a mini standalone product build or a public clone of the private core.
- It is not a complete export of internal runtime modules, prompts, memory, bridge flows, or support layers.
- It is not a claim that every internal flow is published or proven here in the same way.
- It is not a marketing repository built around vague claims.

## Official runtime backbone

The official public reference path is:

```text
request -> planner -> execution_engine -> tool_registry -> runtime_guard -> tool -> result
```

This backbone is the architectural center of the public documentation.
In this repository:

- `planner` prepares and delegates execution.
- `execution_engine` is the primary runtime execution layer for planned steps.
- `tool_registry` is the official tool access layer.
- `runtime_guard` stands before tool execution and issues `ALLOW`, `WARN`, or `BLOCK`.
- `result` is the controlled output after the official path completes.

In the public reference path, governed execution is fail-closed at the documented control decision:
when `BLOCK` holds, the tool does not execute.
The official path is not described as silently degrading into an ambiguous fallback on governed paths.

Result handling is documented here as an additive post-tool / pre-return control surface.
It does not replace the official backbone and it does not move `runtime_guard` after the tool.
It exists to reduce raw leakage, unsafe outward results, or unreviewed tool output after execution.

## Why AIOS is different

The architectural difference described here is not that tools exist, but how sensitive paths are bounded, separated, and evidenced.

- Governed execution is not treated as generic tool use; the official path keeps pre-tool mediation explicit and fail-closed on documented `BLOCK` conditions.
- The governed path is not presented as silently degrading into unofficial fallback behavior when a required control step fails.
- Governance and runtime stay separate: governance can observe, record, review, approve, deny, or revoke without becoming the runtime execution layer.
- `approved` does not mean `applied`: a governance approval can remain governance-only while runtime effect stays `none`.
- Result protection continues after the tool: post-tool / pre-return controls can inspect, redact, or block what is externally returned.
- Compat or legacy surfaces may exist, but they remain non-core and are not promoted as substitutes for the official public backbone.

## Repository map

- [`docs/architecture.md`](docs/architecture.md): Public framing of RobyRoy AIOS as a governed execution architecture.
- [`docs/what-aios-is-and-is-not.md`](docs/what-aios-is-and-is-not.md): Direct statement of what AIOS is, what it is not, and why this public repo exists.
- [`docs/public-vs-private-boundary.md`](docs/public-vs-private-boundary.md): Boundary between the public reference repo and the non-public operational estate.
- [`docs/current-implemented-layers.md`](docs/current-implemented-layers.md): Concise view of the layers currently documented in the public perimeter.
- [`docs/runtime-backbone.md`](docs/runtime-backbone.md): Node-by-node explanation of the official runtime path.
- [`docs/runtime-guard.md`](docs/runtime-guard.md): Public scope of `ALLOW`, `WARN`, and `BLOCK`.
- [`docs/result-handling.md`](docs/result-handling.md): Additive post-tool controls and redaction-oriented handling.
- [`docs/governance-layer.md`](docs/governance-layer.md): Governance records, approvals, and separation from runtime application.
- [`docs/auditability.md`](docs/auditability.md): Traceability, append-only style evidence, and public proof artifacts.
- [`docs/official-vs-compat-paths.md`](docs/official-vs-compat-paths.md): Boundary between the official backbone and non-core surfaces.
- [`docs/technical-proofs.md`](docs/technical-proofs.md): Public examples, adapted tests, and proof labels.
- [`reference/glossary.md`](reference/glossary.md): Key public terms.
- [`reference/invariants.md`](reference/invariants.md): Short list of public architectural invariants.
- [`examples/`](examples): Curated JSON cases for public discussion.
- [`tests/`](tests): Adapted public tests that validate documented invariants.

## Current proof areas

- This repository adopts a proof posture rather than a marketing posture: it states invariants, keeps boundaries explicit, and ties claims to public examples or adapted tests.
- Public example of an `ALLOW` decision in the official backbone.
- Public example of a `WARN` decision that still preserves mediated execution.
- Public example of a `BLOCK` decision where tool execution does not occur and the governed path does not silently continue as if it were cleared.
- Public proof of result redaction as a post-tool additive control.
- Public-facing governance override case where status may become `approved` while runtime effect remains `none`.
- Adapted public tests that keep the backbone wording, invariants, and boundary conditions consistent.

## Reproducible proofs

- [Public proof tests](docs/public-proof-tests/README.md): Small public validation artifacts showing how generic execution and AIOS-governed execution differ on boundary-sensitive requests.
- [Public mock runtime](public_mock_runtime/README.md): Executable public simulation of the mediation flow with `ALLOW`, `WARN`, and `BLOCK` examples.
- [Backbone public test](backbone_public_test/README.md): Documented public test suite that validates backbone order, public example behavior, and `BLOCK` before tool execution.

## Declared limitations

- This repository is selective by design.
- Not every internal component, runtime branch, or support module is published here.
- Compat and legacy surfaces are documented as boundaries, not promoted as official backbone paths.
- Public examples are curated and proof-oriented; they are not presented as full live dumps of the private system.
- The public tests are adapted for public release and focus on architectural meaning rather than internal implementation breadth.

## License

This repository is released under the [MIT License](LICENSE).
