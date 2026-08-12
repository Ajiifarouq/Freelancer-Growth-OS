# Freelancer Growth OS Data Architecture

**Status:** Active architecture baseline  
**Phase:** Phase 2C — Technical Architecture + Pre-Implementation Hardening  
**Implementation status:** Not started  
**Data lifecycle authority:** [DATA_GOVERNANCE.md](DATA_GOVERNANCE.md)  
**Canonical contract authority:** [CONTRACT_REGISTRY.md](CONTRACT_REGISTRY.md)

## Purpose

Define what Version 1 may store, why it stores it, ownership boundaries, lifecycle rules, and the migration path from local SQLite to a future server database without coupling business modules to a specific persistence engine.

Persistent personal/client/business data must not be enabled until the applicable controls and tests in [DATA_GOVERNANCE.md](DATA_GOVERNANCE.md) are implemented.

## Principles

- Store only information needed for active product capabilities.
- Preserve provenance separately from generated recommendations.
- Never store raw credentials in product tables.
- Treat generated outputs as versioned artifacts, not mutable truth.
- Separate source evidence, derived artifacts, approvals, executions, and audit records.
- Use stable opaque IDs.
- Include `workspace_id` from V1 even though the first product is single-user/local.
- Prefer append/version history for material generated assets over destructive overwrite while data is retained.
- Honor deletion rules in `DATA_GOVERNANCE.md`; auditability does not justify silently retaining deleted personal content.
- Database schemas may evolve; canonical product contracts are governed independently in `CONTRACT_REGISTRY.md`.
- Real runtime data never lives inside the Git repository working tree.
- Dependency changes must be able to invalidate/stale downstream artifacts deterministically.
- Persistence mappings for canonical contracts must be lossless for normative fields; storage adapters may normalize fields but must not discard security, provenance, contradiction, freshness, or permission metadata.

## V1 Persistence Choice

SQLite is the local database. SQLAlchemy provides the persistence abstraction and Alembic owns schema migrations.

A future multi-user SaaS may migrate to PostgreSQL. Business/application code must avoid depending on SQLite-only behavior unless isolated inside the SQLite adapter.

Plain SQLite is **not encryption at rest**. Storage/device-protection requirements are governed by `DATA_GOVERNANCE.md` and require a separate ADR before general-user release if application-level encryption is needed.

## Runtime Data Location

The implementation must select an OS user-scoped application data directory outside the repository checkout.

The persistence adapter must fail closed when the configured database/managed-file/log/backup path resolves inside the repository root.

The runtime directory must never be created as a tracked repository folder.

## Core Data Model

### `workspace`

Represents the local Freelancer Growth OS workspace.

Minimum fields:

- `id`
- `name`
- `created_at`
- `updated_at`
- `schema_version` or application compatibility metadata where needed

V1 normally has one workspace. The field exists to avoid baking global-singleton assumptions into every record.

Workspace lifecycle for local V1 is:

`create → use → export/backup → delete`

### `evidence_item`

Represents user-provided, authorised, inferred/proposed, unknown, conflicting, rejected, deleted, or verified evidence state.

Fields/concepts:

- `id`
- `workspace_id`
- `contract_id` = `evidence-record`
- `contract_version`
- `evidence_type`
- `subject_or_claim`
- `source_type`
- `source_reference`
- `title`
- `content_or_location`
- `content_hash` where practical
- `sensitivity_class`
- `evidence_state`
- `allowed_uses_json` or equivalent lossless normalized relation
- `contradictions_json` or equivalent lossless normalized relation
- `captured_at`
- `verified_at` / `verification_time` where applicable
- `supersedes_id` where evidence is replaced
- `deleted_at` where applicable
- timestamps

`allowed_uses` and `contradictions` are normative `evidence-record` fields. Persistence must round-trip them without loss. A database implementation may normalize them into child tables instead of JSON, but serialization back to the canonical contract must preserve the same semantics.

Authoritative evidence states follow `CONTRACT_REGISTRY.md` and `DATA_GOVERNANCE.md`.

An LLM may suggest classification but cannot promote an evidence item to authoritative `verified` state without deterministic policy and qualifying provenance.

Large binaries should remain files/object-like assets referenced by metadata rather than being blindly embedded in SQLite.

### `artifact`

Stores generated or computed product outputs using a typed/versioned envelope.

Fields/concepts:

- `id`
- `workspace_id`
- `contract_id`
- `contract_version`
- `artifact_version`
- `module_id`
- `payload_json`
- `validity_status` (`current`, `stale`, `invalid`, `deleted`)
- `supersedes_id`
- `created_by_run_id`
- timestamps

Examples include canonical contracts such as:

- `freelancer-context`;
- `maturity-assessment`;
- `positioning-brief`;
- `profile-assessment`;
- `profile-optimization-draft`;
- `service-offer-brief`;
- `portfolio-alignment-plan`;
- `cross-asset-consistency-report`;
- `opportunity-assessment`;
- `proposal-draft-record`;
- `pricing-brief`;
- `negotiation-plan`;
- `conversion-next-step-plan`;
- `validation-report`.

The JSON payload must validate against the corresponding canonical Pydantic contract before persistence.

### `artifact_evidence_link`

Many-to-many provenance link between generated artifacts and supporting evidence.

Fields:

- `artifact_id`
- `evidence_item_id`
- `evidence_version/state reference` where needed
- `relationship_type`
- optional note/claim path

This supports traceability without copying the full source into every artifact.

### `artifact_dependency_link`

Tracks generated-artifact dependency edges and the exact source version used.

Minimum fields/concepts:

- dependent artifact ID/version;
- upstream artifact/evidence ID/version;
- dependency type;
- created_at.

Examples:

`proposal-draft-record → positioning-brief`

`proposal-draft-record → opportunity-assessment`

When a material dependency is deleted, corrected, superseded, or reclassified, application policy must mark affected derived artifacts stale/invalid until revalidated.

### `run`

Represents one application workflow/module execution.

Fields/concepts:

- `id`
- `workspace_id`
- `workflow_id`
- `module_id`
- `status`
- `started_at`
- `finished_at`
- `provider`
- `model`
- `provider_configuration_reference` where safe/useful
- `prompt_asset_id`
- `prompt_version`
- `prompt_content_hash` or immutable build/reference when AI-generated behavior must be reproducible
- `input_artifact_ids/versions`
- `output_artifact_ids/versions`
- `contract_ids/versions`
- usage metadata where supplied by provider
- error category/code
- validation/freshness result metadata

Raw prompts and raw sensitive evidence must not be duplicated into telemetry by default.

### `source_verification`

Records a current-information check and must round-trip the canonical `freshness-verification-result` contract without loss.

Fields/concepts:

- `id`
- `workspace_id`
- `contract_id` = `freshness-verification-result`
- `contract_version`
- `freshness_requirement_id` / request reference
- `claim_or_task`
- `reason`
- `source_references_json` or normalized source-reference rows
- `source_quality_classification`
- `verified_at`
- `verified_facts_json` or normalized fact rows
- `conflicts_limitations_json` or normalized conflict/limitation rows
- `result_status` / disposition (`verified`, `conflicting`, `unavailable`, `insufficient`)
- `evidence_item_id` where captured
- expiration/recheck hint where policy defines one

A single-source schema is insufficient because a verification result may depend on multiple authoritative sources or contain conflicts. The persistence adapter must preserve all normative source, quality, fact, limitation, and request-link fields.

No universal freshness TTL is assumed; volatility is domain-specific.

### `connector_binding`

Stores connector metadata, never raw secrets.

Fields/concepts:

- `id`
- `workspace_id`
- `connector_type`
- `external_account_reference`
- `status`
- `read_scopes`
- `write_scopes`
- `secret_reference` only if a future secret manager exposes a non-secret identifier
- `created_at`
- `revoked_at`

V1 may have zero rows because no connector is assumed implemented.

### `approval_request`

Represents an exact consequential action awaiting human decision.

Fields:

- `id`
- `workspace_id`
- `action_type`
- `target_reference`
- `action_payload_json`
- `payload_hash`
- `idempotency_key` or deterministic action identity
- `source_artifact_ids/versions`
- `source_staleness_status`
- `requested_by_module`
- `status`
- `created_at`
- `expires_at` where appropriate

Any material payload/target/parameter change creates a new approval request rather than mutating an approved request invisibly.

Stale/invalid source artifacts cannot create an executable approved instruction.

### `approval_decision`

Fields:

- `id`
- `approval_request_id`
- `decision` (`approved`, `rejected`, `cancelled`)
- `decided_at`
- `decision_actor`
- optional note
- `approved_payload_hash`
- `expires_at` where applicable

Approval does not mean execution occurred.

### `execution_attempt`

Fields:

- `id`
- `approval_request_id`
- `approval_decision_id`
- `idempotency_key`
- `attempt_number`
- `executor_id`
- `executed_payload_hash`
- `status` (`attempted`, `verified-succeeded`, `failed`, `unknown`)
- `started_at`
- `finished_at`
- external request/result reference
- safe error metadata
- reconciliation status

Rules:

- an execution payload must match the approved payload hash;
- the same approval/idempotency identity cannot silently execute twice;
- ambiguous timeout/result requires reconciliation before retry;
- a retry is a governed state transition, not an automatic loop.

### `audit_event`

Records security/governance-relevant events.

Fields/concepts:

- `id`
- `workspace_id`
- `event_type`
- `actor_type`
- `actor_reference`
- `resource_type`
- `resource_id`
- `result`
- `timestamp`
- safe metadata

Sensitive payloads should be referenced/hash-bound, not copied wholesale into audit events.

## Artifact Immutability and Deletion Model

Generated outputs normally use:

`draft v1 → draft v2 → approved/current`

rather than overwriting retained history.

A later artifact may set `supersedes_id` to the prior version. Consumers resolve current active versions through deterministic application policy.

However, retention history is not permission to defeat deletion. `DATA_GOVERNANCE.md` controls when personal/client content must be removed. Minimal non-content tombstones may remain only where needed for integrity and cannot reconstruct deleted content.

## Data Sensitivity Classes

Logical classes:

- `PUBLIC`
- `PROFESSIONAL`
- `PRIVATE_PERSONAL`
- `CLIENT_CONFIDENTIAL`
- `BUSINESS_SENSITIVE`
- `SECRET`

`SECRET` values are not valid normal product-persistence payloads. Credentials belong outside the product database.

## File/Binary Storage

For V1:

- SQLite stores metadata and structured contracts;
- user documents remain in user-controlled local filesystem locations by default;
- managed copies are opt-in and live only in the application data directory;
- store content hashes where practical to detect changes;
- avoid duplicating large files automatically;
- do not persist a private source merely because the application can read it;
- never copy real user documents into the Git repository, fixtures, CI artifacts, or logs.

A future remote product may replace file references with object-storage identifiers behind a storage port.

## Retention, Deletion, and Export

[DATA_GOVERNANCE.md](DATA_GOVERNANCE.md) is normative for V1 retention, deletion, export, local logs, backups, and workspace lifecycle.

Before persistent personal-data storage is enabled, implementation must demonstrate the applicable data-governance tests.

Before V1 release, implementation must support at least:

- workspace data export in a documented machine-readable format;
- evidence deletion/removal and dependent-artifact invalidation;
- deletion of derived artifacts;
- full local workspace deletion;
- connector revocation metadata where connectors exist;
- local database backup/restore procedure;
- log clearing;
- protection against runtime storage inside the Git working tree.

Remote/SaaS retention/legal policies remain future decisions and require separate approval.

## Backup and Recovery

V1 requires:

- documented SQLite backup/export workflow;
- safe handling of active database writes during backup;
- migration restoration test;
- ability to initialize a clean database and migrate to schema head;
- backup files treated as sensitive user data;
- backup location outside Git;
- encryption/device-protection behavior consistent with `DATA_GOVERNANCE.md`.

## SQLite Transaction Policy

Implementation must explicitly configure/test SQLite transaction behavior through the persistence adapter rather than relying on accidental driver defaults.

Write workflows involving multiple related rows—such as artifact + provenance links or approval + audit/execution record—must execute transactionally.

Approval/idempotency state updates must be concurrency-safe enough to prevent duplicate execution within the supported local runtime model.

## PostgreSQL Migration Path

When remote multi-user requirements justify migration:

1. Preserve domain/application repository interfaces.
2. Add PostgreSQL persistence adapter/configuration.
3. Run cross-database contract/integration tests.
4. Migrate schema through Alembic.
5. Add real identity/workspace membership.
6. Enforce resource-level authorization at application layer.
7. Consider PostgreSQL row-level security only as defense in depth, not replacement for application authorization.
8. Replace local file references with approved object storage when needed.
9. Define/approve remote retention/account lifecycle/legal/privacy controls before migrating real personal data.

## No Vector Database in V1

A vector database is deliberately not selected.

V1 evidence volumes/requirements do not justify embedding infrastructure. Retrieval starts with structured metadata, explicit provenance, deterministic filters, and direct evidence selection.

If evidence scale or semantic retrieval quality later demonstrates a real requirement, an ADR must compare relational full-text/search, embeddings inside PostgreSQL, and external vector stores using measured evals.

## Validation Requirements

Implementation tests must cover:

- schema migration from empty database to head;
- rollback/recovery behavior where supported;
- canonical artifact JSON contract validation;
- evidence-record persistence round-trip preserving `allowed_uses` and contradictions;
- freshness-verification persistence round-trip preserving all sources, source quality, verified facts, conflicts/limitations, and request reference;
- approval/execution referential integrity;
- payload-hash/idempotency replay protection;
- no secret fields in persisted domain models;
- workspace scoping on all workspace-owned records;
- provenance link integrity;
- evidence-state transition authority;
- stale/superseded artifact resolution;
- stale artifact rejection from consequential execution;
- evidence deletion and dependent invalidation;
- full workspace deletion;
- export round-trip where defined;
- transaction failure behavior;
- backup/restore procedure;
- runtime data path cannot reside inside repository;
- logs do not capture designated secret/private test markers.

Use synthetic fixtures for development/evals until real-data controls are implemented and verified.
