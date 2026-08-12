# Freelancer Growth OS Data Governance

**Status:** Active pre-implementation control  
**Product release status:** Unreleased  
**Applies to:** Local-first V1 and all implementation work that handles user, client, business, provider, or connected-source data

## Purpose

This document resolves the minimum retention, deletion, export, workspace-lifecycle, local-storage, backup, and privacy rules required before Freelancer Growth OS may persist personal data.

It does not claim legal compliance certification. Future remote/SaaS deployments require a separate legal/privacy review and additional retention/account-lifecycle rules appropriate to the deployment and jurisdictions involved.

## Core Rule

**No real user/client/business runtime data may be stored in the Git repository or any directory inside the repository working tree.**

The application must fail closed if its configured runtime data directory resolves inside the repository root.

Repository content may contain synthetic fixtures only. Synthetic fixtures must not be copied from real user data by superficial redaction.

## V1 Workspace Model

V1 is a local single-user product. It has workspaces, not online user accounts.

For V1, the account-lifecycle requirement is satisfied by the workspace lifecycle:

`create → use → export/backup → delete`

Remote account creation, suspension, billing, account recovery, or tenant lifecycle remains out of scope until a remote/multi-user product is explicitly approved.

## Data Classes

| Class | Examples | Default persistence |
|---|---|---|
| `PUBLIC` | public marketplace profile text, public job listing | allowed when needed |
| `PROFESSIONAL` | CV facts, skills, work history, certifications | allowed with user intent |
| `PRIVATE_PERSONAL` | private CV fields, personal notes, non-public contact details | local-only; minimise |
| `CLIENT_CONFIDENTIAL` | client briefs, messages, unpublished work, negotiation details | local-only; opt-in persistence |
| `BUSINESS_SENSITIVE` | rates, revenue goals, pipeline, pricing strategy | local-only; opt-in persistence |
| `SECRET` | API keys, passwords, OAuth tokens, private keys | **never domain-persisted** |

## Storage Location

The implementation must use an application data directory outside the repository tree.

Recommended logical layout:

```text
[os-user-data-root]/Freelancer-Growth-OS/
  database/
  managed-files/
  exports/
  backups/
  logs/
```

The exact OS-specific location is an implementation decision, but it must:

- be outside the Git checkout;
- be scoped to the current OS user;
- use restrictive file permissions/ACLs where the OS supports them;
- not be placed in a public/shared/synchronised folder by default;
- never contain raw secrets in normal logs or exports.

## Raw Source Files

By default, V1 should reference user-controlled source files by path plus safe metadata/hash rather than copying them into application storage.

If the user explicitly imports a managed copy:

- the copy must be placed only in the application data directory;
- sensitivity must be recorded;
- deletion/export behavior must be defined;
- the file must not be copied into Git, test fixtures, logs, prompt snapshots, or CI artifacts.

## Retention Rules

### Transient task context

- Keep in process/session memory only unless the user explicitly saves an artifact.
- Do not create hidden durable prompt transcripts merely for convenience.
- Temporary files must be removed after the workflow or application exit where practical.

### Evidence metadata and freelancer context

- Retain until the user removes the evidence item or deletes the workspace.
- Superseded evidence may be retained for local auditability only while the workspace exists.
- If the source is deleted or corrected, downstream artifacts that depend on it must be marked stale until revalidated.

### Derived artifacts

Examples include positioning briefs, profile drafts, proposals, pricing briefs, and assessments.

- Retain only when explicitly saved by the workflow/product policy.
- Preserve version/supersession relationships while retained.
- Delete with the workspace unless explicitly exported by the user first.

### Local application logs

- Default retention: maximum 30 days.
- Logs must omit raw CV contents, client-message bodies, full prompts containing private evidence, credentials, tokens, and secret request/response headers.
- Users must be able to clear local logs without deleting the whole workspace.

### Approval and execution audit records

- Retain while the workspace exists when consequential execution functionality is implemented.
- Store the minimum material action scope, decision, timestamps, and verified result needed for audit/reconciliation.
- Do not duplicate full sensitive message bodies when an artifact hash/reference is sufficient.

### Local backups

- Backups are user-controlled and must be treated as sensitive copies of the workspace.
- The product must not silently create indefinite backup history.
- Default automated rotation, if later implemented: no more than 3 local backups and no backup older than 30 days unless the user explicitly changes the policy.
- Deleting a workspace must clearly warn if separately created backups may still contain the data.

## Deletion Rules

### Delete evidence item

Deleting an evidence item must:

1. remove application-managed content for that evidence item where present;
2. remove/disable its active provenance link;
3. mark dependent derived artifacts stale or invalidated;
4. avoid silently preserving the deleted content inside logs, caches, eval fixtures, or prompt snapshots.

Historical tombstones may retain only non-content metadata required to explain that an item was deleted, not the deleted personal/client content itself.

### Delete derived artifact

Delete the stored artifact content and its active references. Minimal non-content audit metadata may remain only when required to preserve execution/approval integrity.

### Delete workspace

A full workspace deletion must remove:

- workspace-owned database rows;
- application-managed evidence copies;
- derived artifacts;
- connected-source metadata/tokens references stored in domain data;
- local application logs scoped to that workspace where technically separable;
- local caches/temp files under application control.

A workspace deletion may leave only non-personal operational metadata that cannot reconstruct the deleted content. V1 has no legal/business requirement to retain deleted personal content.

## Export Rules

Before first release, V1 must support a documented machine-readable export covering:

- freelancer context;
- evidence metadata/provenance excluding secrets;
- saved derived artifacts;
- relevant approval/execution records where implemented;
- schema/version metadata required to interpret the export.

Exports inherit the highest sensitivity of the included data and must be created outside the repository tree.

## Encryption and Device Protection

### Runtime database and managed files

Application-level database encryption is not yet selected. Until it is selected, V1 must:

- store data only in the OS user-scoped application data directory;
- recommend OS/device full-disk encryption for any workspace containing `PRIVATE_PERSONAL`, `CLIENT_CONFIDENTIAL`, or `BUSINESS_SENSITIVE` data;
- provide a clear warning when users choose to persist high-sensitivity data;
- never claim that plain SQLite provides encryption at rest.

Before a release intended for general users, an ADR must decide whether OS-level protection is sufficient for supported platforms or whether application-level encrypted storage is required.

### Backups and exports

Backups/exports containing `PRIVATE_PERSONAL`, `CLIENT_CONFIDENTIAL`, or `BUSINESS_SENSITIVE` data must either:

- reside on an encrypted filesystem/device under the user's control; or
- use an approved encrypted archive/export mechanism.

The product must never label an unencrypted backup as secure merely because it is local.

## Provider/LLM Data Boundary

Before sending private evidence to any model provider, the implementation must apply [PROVIDER_DATA_POLICY.md](PROVIDER_DATA_POLICY.md).

Minimum requirements:

- send only the minimum evidence needed for the task;
- never send `SECRET` values;
- preserve provider/source provenance;
- record which provider/model configuration processed the artifact where reproducibility requires it;
- do not enable optional provider data-sharing/training features by default;
- treat provider retention as separate from local retention.

## Connected Sources

A connected-source read must not cause automatic persistent copying of all retrieved content.

Persist only the minimum authorised fields/references needed for the active workflow. Connector credentials remain outside the product database.

## Evidence-State Authority

An LLM may suggest evidence classifications, but only deterministic application policy may transition a claim into the authoritative `verified` state.

The canonical evidence-state enum is owned by [CONTRACT_REGISTRY.md](CONTRACT_REGISTRY.md) and consists of:

- `provided-unverified`;
- `verified`;
- `inferred`;
- `proposed`;
- `unknown`;
- `conflicting`;
- `rejected`;
- `superseded`;
- `deleted`.

No persistence/model layer may invent an additional evidence state or omit one of these states without a governed contract change.

Verification must record provenance appropriate to the claim. Model confidence alone is never verification evidence.

## Staleness and Dependency Invalidation

Every persisted derived artifact must be able to identify the evidence/artifact versions it depends on.

When a dependency is deleted, corrected, superseded, or materially reclassified:

- dependent artifacts become `stale` until revalidated;
- stale artifacts must not be silently presented as current authoritative output;
- consequential execution must reject stale source artifacts.

## Tests Required Before Persistent Personal Data Is Enabled

Implementation must prove:

- runtime data directory cannot be placed inside the Git repository;
- workspace export works from a clean fixture;
- evidence deletion removes managed content and invalidates dependents;
- workspace deletion removes workspace-owned content;
- logs do not contain configured secret/private test markers;
- backup and restore preserve schema/provenance invariants;
- backup files are not tracked by Git;
- `SECRET` fields cannot enter normal persisted domain models;
- evidence states and transitions conform to `CONTRACT_REGISTRY.md`;
- stale artifacts cannot pass consequential-action validation.

Use synthetic fixtures only.

## Future SaaS Gate

Before remote/SaaS storage of personal data, separately define and approve:

- account lifecycle;
- remote retention schedules;
- deletion timing and backup purge behavior;
- identity/authentication/recovery;
- tenant isolation;
- subprocessors/providers;
- privacy notices/consent where applicable;
- jurisdiction/legal obligations;
- incident response;
- production encryption/key management;
- data portability;
- production backup/recovery objectives.

Local V1 rules must not be copied into SaaS and presented as legally sufficient without review.
