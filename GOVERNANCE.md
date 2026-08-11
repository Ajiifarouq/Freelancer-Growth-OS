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

GrowthOS Engineering remains authoritative for shared engineering governance. This repository remains authoritative for Freelancer Growth OS product-specific requirements, architecture, implementation, workflow, versioning, templates, roles, prompts, and releases.

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

## Product Workflow and Versioning Authority

[WORKFLOW.md](WORKFLOW.md) defines the controlled product lifecycle. [VERSIONING.md](VERSIONING.md), [COMPATIBILITY_MIGRATION.md](COMPATIBILITY_MIGRATION.md), [RELEASE_PROCESS.md](RELEASE_PROCESS.md), and [CHANGELOG.md](CHANGELOG.md) govern compatibility, migrations, versions, release candidates, release execution, and change history.

Validation is evidence, not approval. Merge, tag creation, release publication, artifact publication, and deployment remain separate protected actions unless explicit authorization bundles them.

## Product Template Authority

[TEMPLATE_LIBRARY.md](TEMPLATE_LIBRARY.md) defines reusable product templates for capability/module specifications, evidence, freelancer context, positioning, opportunities, proposals, pricing, validation, connected context, approvals, execution results, prompt changes, and release candidates.

Templates standardize information and handoffs. A filled template does not itself prove implementation, approval, execution, or release.

## Product Role Authority

[ROLE_LIBRARY.md](ROLE_LIBRARY.md) defines reusable responsibility and authority boundaries for product AI/human roles.

A role may describe permitted reasoning, drafting, validation, or connector-control responsibilities, but a role does not grant standing authority to:

- execute consequential external actions;
- expand connector permissions;
- change product evidence;
- approve its own output;
- merge/tag/release/deploy;
- bypass deterministic approval gates.

## Product Prompt Authority

[PROMPT_GOVERNANCE.md](PROMPT_GOVERNANCE.md) defines prompt hierarchy, metadata, lifecycle, versioning, compatibility, factuality, freshness, prompt-injection, structured-output, eval, privacy/security, and human-approval requirements.

[PROMPT_LIBRARY.md](PROMPT_LIBRARY.md) defines governed reusable product prompt assets.

Prompt instructions remain subordinate to requirements, architecture, deterministic policies, role contracts, connector permissions, and human approval. A prompt cannot grant itself authority by wording.

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
- consequential external client/account actions;
- changing visibility/security settings;
- destructive history rewrites;
- modifying another repository.

## Evidence and Factuality

Do not invent product features, customers, users, revenue, integrations, metrics, deployments, approvals, release state, test results, professional evidence, or operational evidence.

Product prompts/roles must distinguish verified facts from inference, recommendations, unknowns, conflicts, rejected claims, and planned work.

## Security and Privacy

Do not commit secrets, credentials, tokens, private keys, unnecessary personal data, or sensitive operational information.

Preserve:

- read/write connector separation;
- prompt-injection boundaries;
- explicit consequential-action approval;
- secret isolation from domain persistence and prompt context;
- least privilege;
- accurate execution-state reporting;
- data minimization and source-specific access boundaries.

## Compatibility and Migration

Released/stable behavior changes require compatibility classification and migration analysis.

This includes material changes to prompts, role authority, templates used as stable contracts, output schemas, connector semantics, approval states, and AI provider/model behavior.

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
- **Phase 2 — Architecture and Standards Alignment**.
- **Phase 3 — Workflow and Versioning Alignment**.
- **Phase 4 — Templates, Roles, and Prompts Alignment** once the Phase 4 candidate is merged and verified on `main`.

Next stage:

- **Phase 5 — Existing Product Content Conformance**.

Product implementation remains not started and the repository remains Unreleased. Reusable templates, roles, and prompt definitions are governed product assets; they do not imply deployed AI agents or implemented software capabilities.
