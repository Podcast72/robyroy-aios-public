# Public vs Private Boundary

This repository is intentionally selective.
It is designed to make the public architecture understandable without collapsing the difference between what is disclosed here and what remains outside the public perimeter.

## What is public in this repository

The public side of this repository includes the material needed to explain the architecture in a technical and inspectable way:

- architecture and backbone documentation
- boundary documents for runtime, governance, result handling, and compat surfaces
- a public mock runtime that demonstrates the mediated execution flow
- proof-oriented JSON examples that show specific boundary cases
- adapted public tests that validate the published invariants
- glossary, invariants, and other reference documentation that make the public claims readable

In other words, what is public here is a bounded technical disclosure:
enough to explain the governed execution model, its backbone, and some proof-oriented behavior without pretending to publish the whole operational estate.

## What is intentionally not public here

This repository does not publish the complete private operational system.
The non-public side includes, among other things:

- the full private runtime core and its wider operational estate
- private orchestration and support surfaces that are not required for the public explanation
- sensitive internal details, configurations, and environment-specific runtime material
- unpublished internal memory, prompts, bridge flows, and operational wiring
- internal surfaces that exist in practice but are not part of the public disclosure perimeter

That absence should not be read as a claim that those surfaces do not exist.
It means they are not being published here.

## Why the boundary exists

The boundary exists for architectural honesty.
Without it, a public reference repository can easily be mistaken for a complete operational system, a reduced product build, or a public copy of the private core.

Keeping the boundary explicit helps this repository stay credible:

- the public proofs remain tied to what is actually shown
- the mock runtime remains a public illustration rather than a claim of full exposure
- the public repository remains a technical reference, not a confusing substitute for the internal system

The purpose of the boundary is therefore clarity, not mystique.
It keeps the public disclosure precise and prevents readers from conflating the public repo with the complete private system.
