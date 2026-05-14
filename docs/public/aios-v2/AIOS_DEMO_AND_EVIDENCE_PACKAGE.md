# AIOS Demo And Evidence Package

This repository contains a bounded public demo and evidence package for AIOS.

It is now aligned with enterprise documentation at a public-safe level: the public repo demonstrates the model directly, while enterprise evidence is summarized as aggregate status and capability categories.

## Public Demo Surface

| Artifact | Purpose |
| --- | --- |
| [public_mock_runtime/](../../../public_mock_runtime/) | Small executable simulation of mediated tool execution. |
| [examples/](../../../examples/) | Public JSON cases for `ALLOW`, `WARN`, `BLOCK`, result redaction, and governance separation. |
| [tests/](../../../tests/) | Adapted public tests for backbone and boundary consistency. |
| [backbone_public_test/](../../../backbone_public_test/) | Guide for the public backbone validation suite. |
| [docs/public-proof-tests/](../../public-proof-tests/) | Public proof artifacts for governance-boundary cases. |
| [AIOS_TEST_HIGHLIGHTS.md](AIOS_TEST_HIGHLIGHTS.md) | Public-safe highlights from broader private enterprise/staging validation. |

## What Can Be Tested Publicly

- `ALLOW` reaches tool execution through the mediated path
- `WARN` remains visible while preserving mediation
- `BLOCK` stops before tool execution
- result handling remains additive to the backbone
- governance approval does not automatically apply a runtime effect
- public docs and examples retain the canonical backbone

## Enterprise Evidence Summarized

The public repository does not contain the full enterprise test suite. It includes small public/demo tests, mock runtime proof tests, readable evidence summaries, and selected public-safe test highlights.

| Evidence category | Public-safe summary |
| --- | --- |
| Enterprise staging gate | Expanded gate passed with an explicit non-public-distribution posture. |
| Package/installability | Non-editable wheel/install checks passed in controlled internal validation. |
| Enterprise/staging validation | Latest read enterprise report records 516 passing tests in the private enterprise/staging validation scope. |
| Runtime hardening | Runtime guard, result gate, operational safety, logging, and access baselines are documented internally. |
| Governance hardening | Policy, capability, approval, budget, memory/state, and supervision categories are covered internally. |
| Runtime governance wiring | E2E enforcement demonstrated through the planned-step runtime path. |
| Result boundary | Invalid, empty, sensitive, or blocked output handling is covered in internal/staging hardening evidence. |
| Audit/replay | Internal reports document trace and audit/replay-oriented evidence for reconstructing execution order. |
| Allow/warn/block | Internal/staging evidence covers allow, warn, block, fail-closed, and no-silent-fallback behavior. |
| Connector readiness | Audit and minimal connector work support controlled adapter-based evaluation; real third-party agent target integration remains future work. |
| Boundary review | Raw source, raw tests, commands, logs, traces, local paths, and package internals remain private. |

For a concise validation overview, see [AIOS Test Highlights](AIOS_TEST_HIGHLIGHTS.md).

## Suggested Local Commands

```bash
python3 public_mock_runtime/mock_runtime.py public_mock_runtime/examples/allow.json
python3 public_mock_runtime/mock_runtime.py public_mock_runtime/examples/warn.json
python3 public_mock_runtime/mock_runtime.py public_mock_runtime/examples/block.json
python3 -m unittest discover -s public_mock_runtime/proof_tests -p 'test_*.py'
python3 -m unittest discover -s tests -p 'test_*_public.py'
```

The blocked mock request is a controlled stop condition. Its CLI behavior may signal an error because the expected result is that the tool did not run.

## Evidence Limits

The public demo is intentionally small. It demonstrates the control shape, not the private runtime core. Enterprise evidence is summarized only as sanitized status and capability categories. Public evidence should be read as bounded technical evidence for controlled review, not as unrestricted operational proof.

The public tests make the concept inspectable. The enterprise validation evidence shows that AIOS is not only a concept page.
