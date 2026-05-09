# AIOS V2 Public Technical Notes

This folder provides public AIOS V2 technical notes for this repository.

It keeps the architectural direction, governance model, staging status, and public limitations while removing or generalizing internal project instructions, absolute paths, execution commands, low-level implementation notes, and migration-only material.

Current public status:

- `V2_STAGING_GATE_PASSED`
- `STAGING_NON_VERIFIED`

What this layer is for:

- explain the AIOS V2 architecture in public/demo-safe terms
- preserve the governed execution model and design philosophy
- document the current staging posture without overstating maturity
- provide a small public update trail for technical readers

What this layer is not:

- a publication of private implementation code
- a production verification package
- a release note set
- a claim that all runtime safety questions are resolved

## Documents

- [AIOS V2 Public Architecture Snapshot](AIOS_V2_PUBLIC_ARCHITECTURE_SNAPSHOT.md)
- [AIOS Governed Runtime Envelope Overview](AIOS_GOVERNED_RUNTIME_ENVELOPE_OVERVIEW.md)
- [AIOS Staging Status And Limits](AIOS_STAGING_STATUS_AND_LIMITS.md)
- [AIOS Public Roadmap](AIOS_PUBLIC_ROADMAP.md)
- [AIOS Public Update Log](AIOS_PUBLIC_UPDATE_LOG.md)

## Canonical Backbone

```text
request -> planner -> execution_engine -> tool_registry -> runtime_guard -> tool -> result_gate -> result
```

This remains the canonical public backbone for AIOS V2.
