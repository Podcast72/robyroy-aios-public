# Governance Boundary Test 01

This artifact documents a reproducible comparison on a boundary-sensitive file operation using the same prompt against plain Codex and AIOS.
The point of the test is not basic coding ability.
It is whether a direct sensitive side effect requested outside the governed AIOS path is executed or refused.

- [prompt.md](prompt.md)
- [codex-result.md](codex-result.md)
- [aios-result.md](aios-result.md)
- [verdict.md](verdict.md)

This test is relevant because it shows one concrete governance difference on the same task.
The difference is not that AIOS can perform more file operations.
The difference is that AIOS constrains when a sensitive operation is allowed.

