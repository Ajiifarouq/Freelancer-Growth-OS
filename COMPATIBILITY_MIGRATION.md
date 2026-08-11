# Freelancer Growth OS Compatibility and Migration Policy

**Status:** Active  
**Product release status:** Unreleased

## Purpose

This document defines how Freelancer Growth OS evaluates compatibility and safely migrates contracts, persisted data, prompts, interfaces, integrations, and configuration.

## Compatibility Principle

A change is compatible only when supported consumers can continue operating as documented without unsafe hidden behavior changes.

Compatibility is evaluated against released or intentionally stable behavior, not against every internal implementation detail.

## Compatibility Review Questions

For every material change ask:

1. What existing consumer, data, workflow, prompt, adapter, or user behavior could be affected?
2. Can old persisted data still be read safely?
3. Can old clients/workflows still use the new behavior?
4. Can new data be interpreted by older supported versions?
5. Does meaning change even if the schema shape does not?
6. Does the change alter authority, privacy, factuality, or security expectations?
7. Is a migration, fallback, feature gate, or deprecation period required?
8. What is the rollback/recovery path if deployment or migration fails?

## Contract Changes

### Normally Backward-Compatible

- adding an optional field with a safe default/absence behavior;
- adding a new output artifact that existing consumers can ignore;
- broadening accepted input where prior input remains valid;
- adding a new command without changing existing command semantics.

### Potentially Conditional

- adding enum values when consumers may use exhaustive matching;
- changing ordering where consumers may depend on it;
- changing default behavior while preserving schema shape;
- adding fields that increase privacy/security obligations;
- changing model/provider behavior under the same product contract.

### Normally Breaking

- removing or renaming required fields;
- changing a field type incompatibly;
- changing field meaning while retaining the same name;
- rejecting previously valid persisted input;
- removing supported CLI/API behavior;
- changing approval semantics so previously safe workflows act differently;
- changing identifiers that stable assets reference;
- removing export/import compatibility without migration.

## Database Migration Rules

Alembic revisions are append-only migration history after release.

Each data-affecting migration must define as applicable:

- forward schema change;
- data backfill/transformation;
- validation after migration;
- behavior during partial failure;
- backup requirement;
- downgrade path or explicit reason downgrade is unsafe;
- recovery procedure;
- compatibility window when old/new application versions may coexist.

### Expand/Contract Preference

For future remote or multi-process deployments, prefer expand/contract migration:

1. add new schema in a backward-compatible way;
2. deploy code capable of old + new representation when needed;
3. migrate/backfill data;
4. verify;
5. switch readers/writers;
6. remove old representation only in a later approved breaking/deprecation step.

For local V1, simpler one-step migrations are acceptable only when backup and upgrade behavior remain safe.

## Artifact and Evidence Migration

Generated artifacts and evidence records must preserve provenance.

Migration must not:

- rewrite an AI recommendation into user-provided evidence;
- silently upgrade unknown/inferred content into verified fact;
- erase source references needed for audit;
- convert draft/approval/execution states inaccurately.

If a format change cannot preserve meaning, retain the old artifact and create a migrated derivative with explicit linkage.

## Approval-State Migration

The state machine:

`draft → awaiting-approval → approved/rejected → attempted → verified-succeeded/failed/unknown`

is safety-sensitive.

Changes to approval or execution state meaning require:

- architecture review;
- security review;
- migration analysis for persisted approval records;
- tests proving no unapproved action becomes executable;
- explicit breaking-change treatment if released semantics change.

Never map `approved` to `verified-succeeded` during migration.

## Prompt Migration

A material prompt revision must identify:

- old prompt ID/version;
- new prompt ID/version;
- modules/workflows affected;
- intended behavior change;
- output/contract implications;
- eval comparison;
- rollback prompt/version;
- compatibility class.

Historical run records should retain the exact prompt version/reference used when practical for reproducibility and audit.

## LLM Provider/Model Migration

Provider/model changes use the provider port and must preserve domain contracts.

Before changing the default provider/model for released behavior:

- run representative evals;
- compare factuality, schema adherence, refusal/error behavior, approval-boundary preservation, latency/cost where relevant;
- document material regression risk;
- retain a rollback configuration when practical.

Model substitution is not assumed compatible merely because both models produce text.

## CLI Migration

When CLI behavior becomes released/stable:

- avoid silently changing command names or option meaning;
- use deprecation aliases where practical;
- document changed defaults;
- treat exit-code/structured-output changes as compatibility concerns for automation consumers.

## API Migration

When the future HTTP API becomes released/stable:

- version only when consumer compatibility requires it;
- prefer additive compatible changes;
- document error-schema and authorization changes;
- do not use URL versioning as a substitute for compatibility analysis;
- breaking API changes require an explicit migration path.

## Integration Adapter Migration

External integrations depend on third-party capabilities that may change independently.

Each adapter must track:

- verified platform capability;
- permission model;
- read/write scope;
- external API/version where relevant;
- failure/revocation semantics;
- current verification date/source where material.

If a platform removes or changes a capability, mark the adapter degraded/unsupported rather than pretending compatibility.

## Configuration Migration

Configuration changes must distinguish:

- new optional setting;
- changed default;
- renamed/removed setting;
- secret/credential change;
- provider/model change;
- environment/path change.

Breaking configuration changes require upgrade instructions and safe detection of obsolete configuration.

## Rollback and Recovery

Rollback strategy depends on change type:

- code-only compatible change: revert/redeploy prior code;
- database change: use tested downgrade only when safe, otherwise restore/forward-fix;
- prompt/model change: restore prior version/configuration;
- integration change: disable adapter/feature and preserve queued/ambiguous actions for reconciliation;
- consequential action already executed externally: do not claim software rollback reverses the external action; use domain-specific remediation.

## Migration Evidence

A migration is not complete because a command exited successfully.

Evidence may include:

- schema head verification;
- row/count/invariant checks;
- contract round-trip tests;
- fixture upgrade tests;
- artifact provenance checks;
- approval-state invariants;
- user-visible smoke tests;
- backup/restore test results where applicable.

## Breaking-Change Approval

Breaking changes require:

- affected-consumer analysis where knowable;
- migration guidance;
- versioning impact;
- release-note visibility;
- explicit approval appropriate to the risk;
- recovery/rollback consideration.
