# Freelancer Growth OS Data Architecture

**Status:** Active architecture baseline  
**Phase:** Phase 2C — Technical Architecture  
**Implementation status:** Not started

## Purpose

Define what Version 1 stores, why it stores it, ownership boundaries, lifecycle rules, and the migration path from local SQLite to a future server database without coupling business modules to a specific persistence engine.

## Principles

- Store only information needed for active product capabilities.
- Preserve provenance separately from generated recommendations.
- Never store raw credentials in product tables.
- Treat generated outputs as versioned artifacts, not mutable truth.
- Separate source evidence, derived artifacts, approvals, executions, and audit records.
- Use stable opaque IDs.
- Include `workspace_id` from V1 even though the first product is single-user/local.
- Prefer append/version history for material generated assets over destructive overwrite.
- Database schemas may evolve; domain contracts remain versioned independently.

## V1 Persistence Choice

SQLite is the local database. SQLAlchemy provides the persistence abstraction and Alembic owns schema migrations.

A future multi-user SaaS may migrate to PostgreSQL. Business/application code must therefore avoid depending on SQLite-only behavior unless isolated inside the SQLite adapter.

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

### `evidence_item`

Represents user-provided, authorised, or verified evidence.

Fields/concepts:

- `id`
- `workspace_id`
- `evidence_type`
- `source_type`
- `source_reference`
- `title`
- `content_or_location`
- `content_hash` where practical
- `sensitivity_class`
- `provenance_status`
- `verification_status`
- `captured_at`
- `verified_at` where applicable
- `supersedes_id` where evidence is replaced
- timestamps

Large binaries should remain files/object-like assets referenced by metadata rather than being blindly embedded in SQLite.

### `artifact`

Stores generated or computed product outputs using a typed/versioned envelope.

Fields/concepts:

- `id`
- `workspace_id`
- `artifact_type`
- `contract_version`
- `module_id`
- `payload_json`
- `status`
- `supersedes_id`
- `created_by_run_id`
- timestamps

Examples include:

- freelancer context;
- maturity assessment;
- positioning brief;
- profile assessment/draft;
- service-offer brief;
- portfolio-alignment plan;
- opportunity assessment;
- proposal draft;
- pricing brief;
- negotiation plan;
- conversion-next-step plan;
- validation report.

The JSON payload must validate against the corresponding Pydantic contract before persistence.

### `artifact_evidence_link`

Many-to-many provenance link between generated artifacts and supporting evidence.

Fields:

- `artifact_id`
- `evidence_item_id`
- `relationship_type`
- optional note/claim path

This supports traceability without copying the full source into every artifact.

### `artifact_dependency_link`

Tracks generated-artifact dependency edges.

Examples:

`proposal-draft → positioning-brief`

`proposal-draft → opportunity-assessment`

This helps detect stale derived outputs after upstream evidence changes.

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
- `prompt_asset_id/version`
- `input_artifact_ids`
- `output_artifact_ids`
- usage metadata where supplied by provider
- error category/code
- validation/freshness result metadata

Raw prompts and raw sensitive evidence should not be duplicated into telemetry by default.

### `source_verification`

Records a current-information check.

Fields/concepts:

- `id`
- `workspace_id`
- `claim/topic`
- `reason`
- `source_type`
- `source_reference`
- `verified_at`
- `result_status`
- `evidence_item_id` where captured
- expiration/freshness hint where policy defines one

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
- `requested_by_module`
- `status`
- `created_at`
- `expires_at` where appropriate

Any material payload/target change creates a new approval request rather than mutating an approved request invisibly.

### `approval_decision`

Fields:

- `id`
- `approval_request_id`
- `decision` (`approved`, `rejected`, `cancelled`)
- `decided_at`
- `decision_actor`
- optional note
- approved payload hash

### `execution_attempt`

Fields:

- `id`
- `approval_request_id`
- `approval_decision_id`
- `executor_id`
- `status` (`attempted`, `verified-succeeded`, `failed`, `unknown`)
- `started_at`
- `finished_at`
- external result reference
- safe error metadata

An ambiguous timeout must not be converted automatically into success or retried as though no side effect occurred.

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

Sensitive payloads should be referenced, not copied wholesale into audit events.

## Artifact Immutability Model

Generated product outputs should normally use:

`draft v1 → draft v2 → approved/current`

rather than overwriting history.

A later artifact may set `supersedes_id` to the prior version. Consumers should resolve the current active version through application policy.

Evidence correction follows the same principle: preserve the prior record when auditability matters and create a superseding evidence item.

## Data Sensitivity Classes

Recommended logical classes:

- `PUBLIC`
- `PROFESSIONAL`
- `PRIVATE_PERSONAL`
- `CLIENT_CONFIDENTIAL`
- `BUSINESS_SENSITIVE`
- `SECRET`

`SECRET` values are not valid normal product-persistence payloads. Credentials belong outside the product database.

## File/Binary Storage

For V1:

- SQLite stores metadata and references;
- user documents may remain in user-controlled local filesystem locations or an application-managed data directory;
- store content hashes where practical to detect changes;
- avoid duplicating large files automatically;
- do not persist a private source merely because the application can read it.

A future remote product may replace file references with object-storage identifiers behind a storage port.

## Deletion and Export

Before V1 release, implementation must support at least:

- workspace data export in a documented machine-readable format;
- deletion of derived artifacts;
- deletion/removal of user evidence metadata and application-managed copies where present;
- connector revocation metadata;
- local database backup/restore procedure.

Detailed remote retention/legal policies remain future decisions.

## Backup and Recovery

V1 requires:

- a documented SQLite backup/export command or workflow;
- safe handling of active database writes during backup;
- migration restoration test;
- ability to initialise a clean database and migrate to schema head;
- backup files treated as sensitive user data.

## SQLite Transaction Policy

Implementation must explicitly configure and test SQLite transaction behavior through the persistence adapter rather than relying on accidental driver defaults.

Write workflows involving multiple related rows—such as artifact + provenance links or approval + audit record—must execute transactionally.

## PostgreSQL Migration Path

When remote multi-user requirements justify migration:

1. Preserve domain/application repository interfaces.
2. Add PostgreSQL persistence adapter/configuration.
3. Run cross-database contract/integration tests.
4. Migrate schema through Alembic.
5. Add real identity/workspace membership.
6. Enforce resource-level authorisation at application layer.
7. Consider PostgreSQL row-level security only as defence in depth, not as a replacement for application authorisation.
8. Replace local file references with approved object storage when needed.

## No Vector Database in V1

A vector database is deliberately not selected.

V1 evidence volumes and requirements do not yet justify embedding infrastructure. Retrieval starts with structured metadata, explicit provenance, deterministic filters, and direct evidence selection.

If evidence scale or semantic retrieval quality later demonstrates a real requirement, an ADR must compare relational full-text/search, embeddings inside PostgreSQL, and external vector stores using measured evals.

## Validation Requirements

Implementation tests must cover:

- schema migration from empty database to head;
- rollback/recovery behavior where supported;
- artifact JSON contract validation;
- approval/execution referential integrity;
- no secret fields in persisted domain models;
- workspace scoping on all workspace-owned records;
- provenance link integrity;
- stale/superseded artifact resolution;
- transaction failure behavior;
- backup/restore procedure.
