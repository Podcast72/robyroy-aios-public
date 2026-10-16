# Evidence, preservation and qualification limits

[Overview](README.md) · [Role separation](isolation.md) · **Evidence and limits**

**Record date: 15 October 2026.** The results below summarize retained private evidence. This public documentation update did not rerun private runtime tests, operate the laboratory or make a provider call.

## Observations and their boundaries

| Observation | What the preserved record supports | What it does not establish |
| --- | --- | --- |
| **Policy denial** | Three writes to a denied resource were blocked by the active policy, with committed internal audit evidence and no tool execution for those requests. | A denial of every possible action, or an OS-level access denial. |
| **Human rejection** | An approval wait, a separate console rejection and the stored operator-rejection outcome were correlated; no resume was recorded for that request. | A positive approval grant, consumed approval or successful write in this record. |
| **OS access denial** | Direct rename and create attempts were denied under the tested agent identity; host-side checks found the protected original unchanged. | Hermes move/create tool coverage, a universal sandbox or protection on other machines. |
| **Pending state** | An additional request remained waiting, with an elapsed deadline and no resume at capture. | Approval, execution or completed reconciliation of that request. |
| **Historical failures** | Intermediate resource-context failures remain in the record. | A claim that every attempt passed or every error was repaired. |

The policy, console and stored execution evidence serve different purposes. Correlating them makes the conclusion stronger than relying on a screenshot or the agent's final answer alone. The private record remains the source; these tables are a public summary, not the raw evidence.

## Verified preservation counts

These are archival and identity checks recorded at closeout. **They are not behavioral test totals, do not measure overall security, and must not be added together.**

| Verified item | Recorded result | How to read the number |
| --- | --- | --- |
| Acquired evidence copies | **7,851 file copies verified** | A preservation check against the archived references; not 7,851 security tests or unique security properties. |
| Existing complete provisioning archive | **23,857 entries verified; no mismatches** | The pre-existing source/dependency/interpreter archive was checked against its original manifest and reused. It predates documented installed corrections. |
| Installed AIOS package | **94/94 package files matched in each of the two account environments** | Matches against package installation records, the preserved current candidate and the repaired package. This does not attest the historical process's complete loaded memory. |
| Logical database snapshots | **Five sanitized snapshots; all integrity checks OK; zero foreign-key violations** | Each store was captured in a read-only transaction. Structural consistency is not restoration or cryptographic audit re-verification. |

File fingerprints and package installation records support identity and copy checks. A matching fingerprint does not establish a new behavioral qualification. The installation's package version label is insufficient to identify the qualified bytes.

## What was kept, and where

The private preservation set includes the original observations, decision and execution evidence, package comparisons, version/provenance records, sanitized state captures, available logs, and a laboratory rebuild procedure. The exact installed package is retained separately from the earlier delivered package and the repository checkout. Pre-existing local work was preserved rather than absorbed into the dossier's commits.

The complete provisioning archive and the installed package have different roles: the archive supplies the retained setup materials, while the installed-package comparison identifies the later corrected bytes. Reusing the earlier archive without accounting for those differences would not reproduce the documented installation.

The five database exports are **sanitized forensic logical snapshots, not restorable backups**. Sensitive fields were excluded during acquisition. They do not recreate credentials, original approvals or authenticated runtime state. Committed database changes were included per store, but the captures do not establish a single atomic backup across all stores. No new cryptographic integrity-tag verification is claimed.

Raw sensitive databases, credentials and runtime key files were not committed to Git. The forensic exports and private evidence archives remain outside this public repository. Available terminal buffers were preserved privately; content discarded before capture cannot be reconstructed.

## Provenance of this public account

The account is derived from the private freeze overview and completion record, the final preservation verification, installed-version and provisioning-archive comparisons, acquisition and governance summaries, the original OS evidence verification, the final publication receipt, and **LAB-REBUILD.md**.

The attached rebuild document was compared with the document stored at the private freeze commit and matched byte for byte. The branch and annotated tag were checked remotely; the tag resolves to the dossier commit recorded by the final publication receipt. These checks establish the source used for this summary, not public independent validation of the underlying runtime.

No private document, source file, raw evidence artifact, personal path, account identifier, credential, operating command or deployment configuration is reproduced here. The private tag is named for identification; there is no public link that promises access to confidential material.

## What the tag qualifies

The tag `security-freeze-20261015-macos-resource-isolation` is an **evidence-preservation marker**. It identifies the documented dossier and exact archived packages. It does **not** automatically qualify:

- the product source at the tag's commit or any current checkout;
- an earlier delivered package or a later modified package;
- RM-21 beyond its existing corrected-candidate offline acceptance;
- RM-22 as LIVE, accepted for release or production-ready;
- a new installation, Mac, volume or deployment profile.

The freeze reused historical behavioral evidence and performed preservation checks. Separate earlier test groups keep their original dates and scopes; there is no new combined suite result on the current checkout.

The [14 October Hermes × AIOS demonstration](../../demos/hermes-aios-2026-10-14/README.md) remains a distinct real-provider experiment. Its approved write does not change the observed outcome of this 15 October laboratory, and neither record closes LIVE RM-22.

## What remains outside the claim

There is no security certification, formal proof, universal hostile-worker protection, global network-egress guarantee, distributed exactly-once guarantee or unrestricted production-readiness claim. The OS denials cover the tested operations and location; they do not establish denial on untested storage sidecars or unrelated resources.

A future rebuild needs fresh identities, secrets and filesystem bindings, verified installation provenance and its own applicable qualification. The preserved recipe is not evidence that the rebuild has happened. Future provider work also needs its own authorization; this freeze grants none.

The existing [release qualification record](../aios-v3/AIOS_V3_RELEASE_QUALIFICATION.md) remains authoritative for the published RM milestone narrative: **RM-21 accepted offline for its identified corrected candidate; RM-22 blocked before LIVE.**

[Back to overview](README.md) · [Role separation](isolation.md) · [Public/private boundary](../../public-vs-private-boundary.md) · [Repository home](../../../README.md)
