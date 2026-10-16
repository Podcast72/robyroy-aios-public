# Security freeze — 15 October 2026

**Evidence preservation completed for the documented macOS laboratory.** This is a public account of what was observed, what was kept, and where the conclusions stop.

The practical question was simple: when an AI agent asks to change a protected file, who actually has the authority to let that change happen?

In this laboratory, Hermes proposed work, AIOS applied the rules, and a human operator handled decisions requiring approval through a separate console. macOS also enforced account and filesystem boundaries. The preserved record shows policy denials, an operator rejection, and direct OS access denials in the specific cases tested.

The result is a traceable record of those boundaries and the packages preserved with it. It is not a new product release or a security certification.

## Start here

| Page | What it explains |
| --- | --- |
| [How the roles are separated](isolation.md) | Hermes, AIOS, the human operator, and the separate role of macOS protection. |
| [Evidence and qualification limits](evidence-and-limits.md) | Observations, verified preservation counts, provenance, the freeze tag, and what remains unqualified. |
| [Existing release qualification record](../aios-v3/AIOS_V3_RELEASE_QUALIFICATION.md) | The separate RM-21 offline decision and RM-22's open gates. |

## What happened

The laboratory used synthetic local files. One protected resource had a rule that denied writes. Another required a separate operator decision before a proposed change could proceed.

| Question | Preserved result | Meaning for a reader |
| --- | --- | --- |
| Could Hermes write to the resource whose policy denied changes? | Three write requests were denied by policy, with no tool execution recorded for those requests. | An agent's request did not override the active rule. |
| Could a request requiring human approval proceed on the agent's word alone? | A request waited for approval and was then rejected through the operator console; the stored decision records that rejection without resume. | The human decision remained separate from the agent's proposal. |
| Could the tested agent account directly rename or create files in the protected location? | The OS denied the tested operations; checks found the protected original unchanged. | macOS added a separate boundary in that account/path/operation profile. |
| Was the tested environment preserved precisely enough to inspect later? | Evidence copies, an existing complete provisioning archive, installed-package comparisons and sanitized logical database snapshots were verified and retained privately. | Later review can distinguish the observed installation from earlier packages and the repository checkout. |

**No positive approval or successful write is established by this 15 October record.** An additional request remained waiting with an elapsed deadline and no resume at capture; the freeze preserved that state rather than resolving it. Intermediate failures were retained as failures.

## Why preserve the evidence?

A conversational answer is not an execution record. Likewise, a package version label does not prove that two installations contain the same bytes.

The freeze brought together recorded outcomes, operator decisions, OS observations, file fingerprints, package identities and provenance. A fingerprint is a value calculated from file contents to detect a difference. It supports comparison with the preserved reference; it does not by itself prove that software is secure.

The archives retain the exact installed package separately from the earlier delivered package and the repository source. This matters because those artifacts differ. Treating them as interchangeable would attach evidence to software it did not qualify.

## What “freeze” means here

The private tag `security-freeze-20261015-macos-resource-isolation` identifies the preserved dossier and archived packages. It does **not** automatically qualify the product code at the tag's commit, the current checkout, RM-21 or RM-22.

- **RM-21:** the existing acceptance remains limited to its identified corrected offline candidate.
- **RM-22:** remains blocked before LIVE; this freeze closes neither its deployment nor its provider/authorization gates.
- **Another installation:** requires its own identity, configuration and applicable qualification evidence.

Preservation reused existing observations and added archival verification. It did not introduce a new behavioral qualification or invoke the provider again. The [14 October real-provider demonstration](../../demos/hermes-aios-2026-10-14/README.md) is a separate experiment; its successful approved write is not imported into this laboratory record.

## What is public

These pages publish a deliberately limited explanation and aggregate results derived from the private freeze dossier and its laboratory-rebuild document. They do not publish that document, its operating commands, account identities, private paths, credentials, configuration, raw databases, logs, probes or runtime source.

Public readers can assess the clarity and limits of these claims. They cannot independently rerun the private V3 qualification from this repository. The [public V2 demonstration](../../../public_mock_runtime/README.md) remains a separate, runnable illustration.

[Continue: role separation](isolation.md) · [Evidence and limits](evidence-and-limits.md) · [Public/private boundary](../../public-vs-private-boundary.md) · [Repository home](../../../README.md)
