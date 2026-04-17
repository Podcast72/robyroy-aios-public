# Backbone Public Test

`backbone_public_test/` documents the public backbone validation suite for this repository.

It is not a runtime.
It is not the executable `public_mock_runtime/` demo.
It is not the `docs/public-proof-tests/` artifact collection.

## Where The Tests Live

The suite uses these repository-level tests:

- `tests/test_backbone_public.py`
- `tests/test_runtime_guard_public.py`
- `tests/test_result_handling_public.py`

These files stay in `tests/` because they validate repository-wide public backbone guarantees.

## What They Validate

- the official backbone path remains consistent across core public documents
- curated public examples keep the same official path
- `ALLOW`, `WARN`, and `BLOCK` stay behaviorally distinct
- `BLOCK` stops execution before the tool step
- result handling stays additive and does not replace the backbone

## What They Demonstrate

This suite gives a fast public check that the documented backbone is still coherent across docs and curated examples.
It is a consistency layer for the public reference path, not a simulation of a live runtime.

## What It Is Not

- not the full AIOS runtime
- not the public mock runtime demo
- not an enterprise integration or governance engine
- not a replacement for the `docs/public-proof-tests/` public artifacts

## Run The Backbone Public Test

From the repository root:

```bash
python3 -m unittest discover -s tests -p 'test_*_public.py'
```

## Expected Outcome

All tests should pass without extra setup.
The passing result confirms the documented backbone path, public example traces, and `BLOCK`-before-tool behavior remain intact.
