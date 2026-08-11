# Agent Operating Requirements

## Purpose

This document defines mandatory operating behavior for humans, AI agents, and automated engineering actors working in Freelancer Growth OS.

## Required Start Sequence

Before changing repository content, an actor must:

1. Verify the repository identity and intended branch.
2. Inspect current repository state and relevant history.
3. Read [GOVERNANCE.md](GOVERNANCE.md).
4. Confirm the pinned GrowthOS Engineering baseline is `v0.1.0` at `7ee056f938e12b5a72d1ee919a27f05ec5297c69` unless an approved adoption change has replaced it.
5. Read [WORKFLOW.md](WORKFLOW.md) and the product architecture/requirements documents relevant to the requested change.
6. Read [VERSIONING.md](VERSIONING.md) and [COMPATIBILITY_MIGRATION.md](COMPATIBILITY_MIGRATION.md) when the change affects a stable/released contract, schema, prompt, data, CLI/API, integration, configuration, migration, or release behavior.
7. Identify the exact authorized scope and protected actions.
8. Preserve unrelated existing work.

## Scope Discipline

Modify only the explicitly authorized product scope. Do not turn a narrow task into product redesign, architecture expansion, dependency migration, policy changes, or cleanup without authority.

## Shared-Governance Compliance

Product work must remain compatible with the pinned GrowthOS Engineering baseline unless an approved and documented product-specific extension or deviation applies.

Do not copy upstream governance mechanically when a product-specific document should instead reference or extend the shared rule.

## Workflow Compliance

Material work follows the controlled product lifecycle in [WORKFLOW.md](WORKFLOW.md).

Do not silently skip applicable readiness, architecture, migration, validation, quality, approval, or release gates.

A successful implementation or test run is candidate evidence, not automatic authorization to merge or release.

## Existing-Work Protection

Do not overwrite, delete, rename, reformat, or supersede unrelated work without authorization. When repository state differs from the expected state, constrain work to the safe subset or stop at the relevant authority boundary.

## Factuality

Do not fabricate product features, customers, users, metrics, integrations, releases, approvals, incidents, tests, deployments, or business evidence. Proposals must be labeled as proposals or planned work.

Current/volatile platform, API, pricing, legal, regulatory, or tool claims must be verified when materially relevant or explicitly labeled unverified.

## Security and Privacy

Do not expose or commit secrets, credentials, tokens, private keys, unnecessary personal data, or sensitive operational information. Do not weaken security controls for convenience.

Preserve read/write connector separation, least privilege, prompt-injection boundaries, and deterministic human approval before consequential external actions.

## Compatibility and Migration

Before changing stable/released behavior, classify compatibility under [VERSIONING.md](VERSIONING.md) and apply [COMPATIBILITY_MIGRATION.md](COMPATIBILITY_MIGRATION.md).

Do not:

- rewrite released migration history;
- silently change contract meaning;
- promote inferred/unknown evidence into verified fact during migration;
- treat model substitution as automatically compatible;
- change approval-state meaning without security/migration review.

## Validation

Validate changes against applicable product requirements plus the pinned shared architecture, standards, workflow, security, privacy, factuality, and compatibility requirements.

Validation is proportional to risk and may include tests, contract checks, migrations, AI evals, security/privacy review, factuality checks, and manual acceptance.

Validation is evidence; it is not approval.

## Git and Publication Boundaries

Without appropriate authorization, do not:

- commit or push candidate changes;
- create pull requests;
- modify the default branch;
- merge branches or pull requests;
- create or move tags;
- publish releases or artifacts;
- deploy product releases;
- change repository visibility or protected settings;
- rewrite published history;
- modify another repository.

Merge, tag creation, release publication, artifact publication, and deployment remain separate protected actions unless an explicit authorization bundles the named actions and scope.

## Pull Request Reporting

PRs should use `.github/PULL_REQUEST_TEMPLATE.md` or provide equivalent information, including:

- requirements/modules affected;
- change classification;
- compatibility/migration impact;
- security/privacy impact;
- validation actually performed;
- release impact;
- residual risk.

Do not mark unavailable checks as passed.

## Release Discipline

Follow [RELEASE_PROCESS.md](RELEASE_PROCESS.md) for release preparation/execution.

Do not create placeholder release tags. Published tags are immutable. A merged PR is not a release.

## Reporting

Completion reports must distinguish planned work from verified results. Never claim a remote branch, commit, PR, merge, tag, release, deployment, test result, integration, or adoption state exists without evidence.

For consequential external actions, distinguish `draft`, `awaiting-approval`, `approved/rejected`, `attempted`, and `verified-succeeded/failed/unknown` states accurately.

## Stop Conditions

Stop when:

- the authorized scope is complete;
- required authority is missing;
- repository identity or baseline is uncertain;
- an operation would affect unrelated work;
- required validation cannot be performed;
- compatibility/migration impact is unresolved;
- a security, privacy, compatibility, or factuality issue cannot be resolved safely;
- an exact release/merge/action target cannot be verified.
