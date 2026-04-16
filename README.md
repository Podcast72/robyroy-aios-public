# RobyRoy AIOS

_Public architecture, governance model, and technical proofs_

RobyRoy AIOS is presented here as a governed execution architecture for AI-assisted systems.
This public repository explains how the project approaches execution control, tool access mediation, result handling, and auditability.
It does not expose the full private operational codebase.

The public reason for this repository is straightforward.
Once a system can decide, call tools, cross runtime paths, produce results, and potentially trigger real side effects, output generation alone is not enough.
Tool access mediation, execution clarity, separation between runtime and governance, control over result handling, and auditability become first-class architectural concerns.

This repository exists to make that direction readable in a sober and technical way.
It is not a brochure and it is not a public dump of the internal system.
It is a curated public-facing reference for how RobyRoy AIOS frames governed execution.

## What this repository is

- A public technical repository for architecture, governance model, and technical proofs.
- A curated explanation of the official runtime backbone used as the public reference path.
- A selective set of examples and adapted public tests that make key invariants inspectable.
- A public-facing description of why governed execution matters for AI-assisted systems.

## What this repository is not

- It is not the full RobyRoy AIOS private operational codebase.
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

Result handling is documented here as an additive post-tool control surface.
It does not replace the official backbone and it does not move `runtime_guard` after the tool.

## Why this matters

Many AI discussions stop at model output.
That framing becomes too weak when systems can access tools, traverse runtime paths, and interact with real-world state.

The public thesis behind this repository is that governed execution matters because:

- tool access should not be implicit
- runtime decisions should not be opaque
- execution and governance should stay distinct
- result handling should be explicit rather than accidental
- official paths and compat paths should not be conflated
- auditability improves interpretability, reviewability, and operational trust

## Repository map

- [`docs/architecture.md`](docs/architecture.md): Public framing of RobyRoy AIOS as a governed execution architecture.
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

- Public example of an `ALLOW` decision in the official backbone.
- Public example of a `WARN` decision that still preserves mediated execution.
- Public example of a `BLOCK` decision where tool execution does not occur.
- Public proof of result redaction as a post-tool additive control.
- Public-facing governance override case where runtime effect remains `none`.
- Adapted public tests that keep the backbone wording and boundary conditions consistent.

## Reproducible proofs

- [Public proof tests](docs/public-proof-tests/README.md): Small public validation artifacts showing how generic execution and AIOS-governed execution differ on boundary-sensitive requests.
- [Public mock runtime](public_mock_runtime/README.md): Executable public simulation of the mediation flow with `ALLOW`, `WARN`, and `BLOCK` examples.

## Declared limitations

- This repository is selective by design.
- Not every internal component, runtime branch, or support module is published here.
- Compat and legacy surfaces are documented as boundaries, not promoted as official backbone paths.
- Public examples are curated and proof-oriented; they are not presented as full live dumps of the private system.
- The public tests are adapted for public release and focus on architectural meaning rather than internal implementation breadth.

## License

This repository is released under the [MIT License](LICENSE).
