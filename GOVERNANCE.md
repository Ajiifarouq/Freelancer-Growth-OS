# Freelancer Growth OS Governance

## Purpose

This document defines the product-level governance contract for Freelancer Growth OS and its adoption of shared GrowthOS Engineering governance.

## Authority and Dependency

Freelancer Growth OS adopts the following immutable shared-governance baseline:

- **Repository:** `Ajiifarouq/GrowthOS-Engineering`
- **Tag:** `v0.1.0`
- **Commit:** `7ee056f938e12b5a72d1ee919a27f05ec5297c69`

The dependency direction is:

`Freelancer Growth OS → GrowthOS Engineering`

GrowthOS Engineering remains authoritative for shared engineering governance. This repository remains authoritative for Freelancer Growth OS product-specific requirements, architecture, implementation, workflow, versioning, and releases.

## Baseline Pinning Rules

- Do not treat upstream `main` as the governing baseline.
- Governance adoption changes must identify the exact new tag and commit SHA.
- An upstream update does not automatically modify this product repository's governing baseline.
- Compatibility impact must be reviewed before adopting a newer GrowthOS Engineering release.
- Historical released baselines must remain traceable.

## Product Requirements Authority

[PRODUCT_REQUIREMENTS.md](PRODUCT_REQUIREMENTS.md) is the authoritative product-requirements baseline.

Requirements approval does not imply implementation or release.

## Product Architecture Authority

Logical architecture is defined by:

- [CAPABILITY_ARCHITECTURE.md](CAPABILITY_ARCHITECTURE.md);
- [MODULE_CATALOG.md](MODULE_CATALOG.md).

Technical architecture is defined by:

- [TECHNICAL_ARCHITECTURE.md](TECHNICAL_ARCHITECTURE.md);
- [DATA_ARCHITECTURE.md](DATA_ARCHITECTURE.md);
- [AI_RUNTIME_ARCHITECTURE.md](AI_RUNTIME_ARCHITECTURE.md);
- [SECURITY_INTEGRATION_ARCHITECTURE.md](SECURITY_INTEGRATION_ARCHITECTURE.md);
- [DEPLOYMENT_OPERATIONS.md](DEPLOYMENT_OPERATIONS.md);
- accepted records under [`docs/adr/`](docs/adr/).

Architecture documents define approved boundaries and technical decisions. They do not themselves prove implementation, deployment, or release.

## Product Workflow Authority

[WORKFLOW.md](WORKFLOW.md) defines the product-specific engineering lifecycle and required implementation, validation, review, approval, release-preparation, release-execution, maintenance, and stop-condition gates.

Applicable workflow gates must not be silently skipped.

Validation is evidence, not approval.

## Product Versioning Authority

[VERSIONING.md](VERSIONING.md) defines semantic versioning, compatibility classes, artifact/prompt/contract versioning, deprecation, retirement, release-candidate, and tag rules.

[COMPATIBILITY_MIGRATION.md](COMPATIBILITY_MIGRATION.md) defines compatibility and migration rules for contracts, data, prompts, provider/model changes, CLI/API behavior, integrations, configuration, approval states, and rollback/recovery.

[RELEASE_PROCESS.md](RELEASE_PROCESS.md) defines controlled release preparation, exact release-candidate verification, human release approval, release execution, post-release verification, rollback, withdrawal, and security-release behavior.

[CHANGELOG.md](CHANGELOG.md) records notable unreleased and released product changes without itself establishing release state.

## Product-Specific Extensions

This repository may extend shared governance when the extension:

- is explicitly product-specific;
- does not contradict a shared architectural invariant;
- identifies its scope and rationale;
- documents compatibility impact;
- records required approval when the extension changes a protected governance boundary.

## Deviations

A deviation from the pinned shared baseline must document:

- upstream rule affected;
- reason;
- product scope;
- risk and compatibility impact;
- compensating controls where relevant;
- approving authority;
- review/exit condition where relevant.

Do not silently override shared governance.

## Protected Actions

The following remain separately authorized actions unless explicit authorization bundles the named actions and scope:

- creating/moving branches for governed delivery;
- committing/pushing candidate changes;
- creating pull requests;
- modifying the default branch;
- merging pull requests;
- creating/moving tags;
- publishing releases or artifacts;
- deploying product releases;
- changing visibility/security settings;
- destructive history rewrites;
- modifying another repository.

Merge approval does not automatically authorize tag creation, release publication, artifact publication, or deployment.

## Evidence and Factuality

Do not invent product features, customers, users, revenue, integrations, metrics, deployments, approvals, release state, test results, or operational evidence.

Distinguish verified repository facts from proposals, planned work, unverified current facts, and placeholders.

## Security and Privacy

Do not commit secrets, credentials, tokens, private keys, unnecessary personal data, or sensitive operational information.

Technical implementation must preserve Phase 2C security architecture, including:

- read/write permission separation;
- prompt-injection boundaries;
- explicit consequential-action approval;
- secret isolation from domain persistence;
- least privilege;
- accurate execution-state reporting.

## Compatibility and Migration

Released/stable behavior changes require compatibility classification and migration analysis.

Breaking changes require affected-consumer analysis where knowable, migration guidance, release-note visibility, version impact, and appropriate human approval.

Published migrations/tags/history must not be rewritten to simulate a cleaner past.

## Adoption Lifecycle

The controlled adoption sequence is:

1. Product Governance Entry Layer.
2. Architecture and Standards Alignment.
3. Workflow and Versioning Alignment.
4. Templates, Roles, and Prompts Alignment.
5. Existing Product Content Conformance.
6. Integrated Adoption Audit and Product Release Readiness.

A later stage must not be represented as complete until its required artifacts and verification exist.

## Current Status

Completed:

- **Phase 1 — Product Governance Entry Layer**.
- **Phase 2 — Architecture and Standards Alignment** (2A, 2B, 2C).
- **Phase 3 — Workflow and Versioning Alignment** once the Phase 3 candidate is merged and verified on `main`.

Next stage:

- **Phase 4 — Templates, Roles, and Prompts Alignment**.

Product implementation remains not started and the repository remains Unreleased. Phase 3 defines how future implementation and releases are governed; it does not constitute implementation or a product release.
