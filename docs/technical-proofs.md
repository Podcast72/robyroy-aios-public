# Technical Proofs

This repository publishes selective technical proofs rather than a complete dump of the private operational system.
Each proof area is labeled conservatively so readers can understand what kind of evidence is being shown.

## Proof labels used in this repository

- `public example`: a curated public-facing example meant to explain an architectural case.
- `public proof`: a public artifact that demonstrates a specific documented control property.
- `adapted public test`: a public test derived from a real invariant but rewritten to stand alone outside the private codebase.
- `public-facing reference case`: a documented example used to clarify a boundary or architectural interpretation.

## Published proof areas

### 1. `ALLOW` through the official backbone

- Artifact: [`examples/allow-case.json`](../examples/allow-case.json)
- Label: `public example`
- What it shows: the request follows the official backbone, the runtime guard returns `ALLOW`, and the tool executes.

### 2. `WARN` without bypassing mediation

- Artifact: [`examples/warn-case.json`](../examples/warn-case.json)
- Label: `public example`
- What it shows: the runtime guard returns `WARN`, the path remains official, and execution still stays mediated.

### 3. `BLOCK` before tool execution

- Artifact: [`examples/block-case.json`](../examples/block-case.json)
- Label: `public proof`
- What it shows: a blocked request does not execute the tool and still closes in a controlled way.

### 4. Result redaction after tool execution

- Artifact: [`examples/result-redaction-case.json`](../examples/result-redaction-case.json)
- Label: `public proof`
- What it shows: result handling can redact returned material after the tool runs, while the official backbone remains unchanged.

### 5. Governance override with no automatic runtime effect

- Artifact: [`examples/governance-override-example.json`](../examples/governance-override-example.json)
- Label: `public-facing reference case`
- What it shows: governance can approve a decision while runtime effect remains `none`, so governance is not misdescribed as an automatic runtime bypass.

## Adapted public tests

The public tests in [`tests/`](../tests) are adapted for public release.
They do not depend on the private operational modules.
Instead, they validate the architectural meaning that the repository claims in public:

- backbone wording remains stable
- guard verdict semantics remain clear
- blocked runs do not execute the tool
- result handling stays additive
- governance does not silently become runtime execution

## Why the proof set is selective

This repository values clarity over volume.
A smaller proof set is preferable to a larger but ambiguous publication if the smaller set makes the architectural claims more readable and more defensible.

