# Governance Memory Boundary Test 03

This artifact documents a comparison on the same prompt against plain Codex and AIOS when the request targets a canonical memory area with a direct mutative maintenance action.
The point of the test is not general file-system skill.
It is whether the system treats the request as executable maintenance or refuses it before mutation at a governed memory boundary.

- [prompt.md](prompt.md)
- [codex-result.md](codex-result.md)
- [aios-result.md](aios-result.md)
- [verdict.md](verdict.md)

This test focuses on the same prompt and a different execution posture.
It is not a general benchmark and it does not claim broad model superiority.
