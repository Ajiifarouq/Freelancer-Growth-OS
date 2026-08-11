# Freelancer Growth OS Versioning Policy

**Status:** Active  
**Product release status:** Unreleased  
**Governance baseline:** `Ajiifarouq/GrowthOS-Engineering` `v0.1.0` at `7ee056f938e12b5a72d1ee919a27f05ec5297c69`

## Purpose

This document defines semantic versioning, compatibility classification, artifact versioning, deprecation, release tags, and version-authority rules for Freelancer Growth OS.

## Product Semantic Versioning

Formal product releases use:

`MAJOR.MINOR.PATCH`

- **MAJOR** — approved breaking change to a released product contract or supported behavior.
- **MINOR** — backward-compatible capability addition or materially expanded supported behavior.
- **PATCH** — backward-compatible defect correction, security correction, documentation correction tied to released behavior, or non-breaking compatibility fix.

Version impact is determined by compatibility, not commit-message prefix alone.

## Pre-1.0 Policy

Before `1.0.0`, compatibility still matters.

Pre-1.0 does not mean arbitrary breaking change. Breaking changes must still be:

- explicitly identified;
- reviewed for consumers/data/migrations;
- documented in release notes;
- supplied with migration guidance where applicable;
- approved through the normal release process.

## Unreleased State

Until the first product release is explicitly approved and published:

- repository state is `Unreleased`;
- merged architecture/workflow documentation is not a product release;
- no version number should be presented as released merely because implementation exists;
- tags must not be created as placeholders for future releases.

## Compatibility Classes

Every material change should be classified as one of:

- `backward-compatible`;
- `conditionally-compatible`;
- `breaking`;
- `deprecated-but-supported`;
- `retired`;
- `internal-only` when no supported external/product contract changes.

## What Counts as a Product Contract

Compatibility review applies to any released or intentionally stable consumer-facing boundary, including as applicable:

- CLI commands/options/output relied on by users or automation;
- HTTP/API schemas and semantics;
- persisted data required across upgrades;
- Pydantic contract schemas exported beyond one internal implementation detail;
- module IDs/capability IDs referenced by stable assets;
- prompt IDs/versioned prompt behavior when consumers rely on them;
- integration adapter semantics;
- approval-state semantics;
- export/import formats;
- documented supported workflows.

Internal implementation detail is not automatically a public compatibility promise.

## Artifact Versioning

Artifacts may have independent versions only when consumers need stable references.

Potentially versioned artifacts include:

- product release;
- data contracts;
- prompts;
- module interfaces;
- export/import schemas;
- integration adapter contracts.

Do not add independent versions simply for decoration.

## Contract Versioning

Stable serialized contracts should carry a schema/contract version when backward compatibility across persisted or exchanged data requires it.

Rules:

- additive optional fields are normally backward-compatible;
- removing/renaming required fields is normally breaking;
- changing field meaning without changing representation can still be breaking;
- enum narrowing is breaking for previously valid values;
- enum expansion may be conditionally compatible if consumers use exhaustive matching;
- changed validation that rejects previously accepted persisted input requires compatibility review.

Detailed treatment is defined in [COMPATIBILITY_MIGRATION.md](COMPATIBILITY_MIGRATION.md).

## Database Schema Versioning

Database changes use ordered Alembic revisions rather than semantic version numbers per migration.

Release notes must identify migrations required by the release where applicable.

Rules:

- never edit an already-shipped migration to rewrite history;
- add a new migration for corrections;
- migrations affecting existing data require upgrade validation;
- destructive migrations require explicit compatibility analysis and backup/recovery guidance;
- migration status must not be inferred from application version alone without verification.

## Prompt Versioning

Prompts become independently versioned when prompt behavior is treated as a stable product asset or when eval/audit/reproducibility requires an exact prompt reference.

Prompt changes are classified by behavior impact, not text diff size.

Examples:

- typo/format correction with no behavior change: potentially patch-level artifact change;
- new optional guidance preserving prior outputs: potentially backward-compatible;
- changed authority, factuality, output schema, or expected behavior: requires compatibility/eval review and may be breaking for consumers.

Every material prompt behavior change should record:

- prompt ID/version;
- intended behavior change;
- eval evidence;
- affected modules/workflows;
- compatibility classification.

## Model and Provider Changes

Model/provider IDs are configuration behind the LLM port and do not by themselves define product version impact.

However, a model/provider change that materially changes supported behavior, output compatibility, safety/factuality, or cost/latency expectations may require:

- eval comparison;
- release note entry;
- configuration migration;
- product version change depending on user-visible impact.

## Dependency Updates

Dependency updates must be assessed by actual compatibility/security impact.

- patch dependency bumps do not automatically imply product PATCH release;
- a dependency change that modifies product behavior may require a product version change;
- security updates may justify a patch release when they affect released software;
- runtime minimum-version changes may be breaking for supported installations.

## Deprecation

A deprecated contract or feature remains supported for an explicitly documented period or until a named future release when practical.

Deprecation notices should include:

- deprecated item;
- replacement;
- reason;
- migration guidance;
- earliest intended removal version/timeframe if known;
- affected users/consumers where knowable.

## Retirement

Retirement ends supported use.

Retirement requires:

- prior deprecation where reasonably possible;
- compatibility analysis;
- migration/replacement guidance;
- release-note visibility;
- approval appropriate to the impact.

## Git Tags

Release tags use:

`vMAJOR.MINOR.PATCH`

Rules:

- tags represent approved release points only;
- the exact release-candidate commit SHA must be known before tag creation;
- published release tags are immutable;
- do not move a published tag to correct a mistake;
- corrections normally require a new release;
- release tag creation is a protected action separate from merge.

## Release Candidates

A release candidate is identified by an exact commit SHA and proposed semantic version.

The phrase `release candidate` does not create a Git tag and does not imply publication.

Release candidate preparation must include compatibility/migration evidence and pass the gates in [RELEASE_PROCESS.md](RELEASE_PROCESS.md).

## Version Authority

Automation may:

- calculate a recommended version;
- classify changes;
- prepare changelog/release notes;
- verify candidate state.

Automation may not self-authorize:

- a breaking version decision where human approval is required;
- tag creation;
- release publication;
- deployment.

## Release Withdrawal

If a released version must be withdrawn:

- preserve tag/release history;
- explain reason and affected scope;
- identify mitigation/replacement;
- provide upgrade/downgrade guidance where possible;
- record approving authority.

Do not erase history to simulate that a release never existed.
