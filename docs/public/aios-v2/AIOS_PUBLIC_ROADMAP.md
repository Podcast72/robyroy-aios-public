# AIOS Public Roadmap

This roadmap presents a conservative public interpretation of the AIOS V2 direction represented in this repository.

It is not a release roadmap. It is a governance-oriented progression for a technical pilot.

## Near-Term Public Priorities

1. Keep the canonical governed backbone stable in public documentation.
2. Clarify the role of the major governance surfaces without exposing private implementation detail.
3. Maintain disciplined public status language around `V2_STAGING_GATE_PASSED / STAGING_NON_VERIFIED`.
4. Expand public evidence only when it can be disclosed without leaking internal code or operational internals.

## Technical Pilot Direction

The current public documentation points toward a staged path:

1. architecture clarity
2. governed control semantics
3. bounded staged design and pilot evidence
4. controlled execution review
5. later runtime-grade validation only after explicit review

## Documentation Priorities

- keep architecture explanations readable for external technical readers
- keep governance claims narrower than the internal design ambition
- separate public principles from private implementation mechanics
- preserve public/private boundaries as part of the architecture itself

## Public Risk Discipline

The public/demo repository should continue to avoid:

- stronger maturity language than the evidence supports
- publication of private operator instructions
- exposure of runtime injection or adapter internals
- direct reuse of staging-only commands and file-system assumptions

## Recommended Public Next Step

Continue improving the public narrative around governed execution and enterprise control surfaces, while only releasing additional technical evidence that remains bounded, non-destructive, and clearly marked as pilot-stage material.
