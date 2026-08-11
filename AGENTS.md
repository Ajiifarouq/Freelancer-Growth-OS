# Agent Operating Requirements

## Purpose

This document defines mandatory operating behavior for humans, AI agents, and automated engineering actors working in Freelancer Growth OS.

## Required Start Sequence

Before changing repository content, an actor must:

1. Verify the repository identity and intended branch.
2. Inspect current repository state and relevant history.
3. Read [GOVERNANCE.md](GOVERNANCE.md).
4. Confirm the pinned GrowthOS Engineering baseline is `v0.1.0` at `7ee056f938e12b5a72d1ee919a27f05ec5297c69` unless an approved adoption change has replaced it.
5. Read product governance documents relevant to the requested change.
6. Identify the exact authorized scope and protected actions.
7. Preserve unrelated existing work.

## Scope Discipline

Modify only the explicitly authorized product scope. Do not turn a narrow task into product redesign, architecture expansion, dependency migration, policy changes, or cleanup without authority.

## Shared-Governance Compliance

Product work must remain compatible with the pinned GrowthOS Engineering baseline unless an approved and documented product-specific extension or deviation applies.

Do not copy upstream governance mechanically when a product-specific document should instead reference or extend the shared rule.

## Existing-Work Protection

Do not overwrite, delete, rename, reformat, or supersede unrelated work without authorization. When repository state differs from the expected state, constrain work to the safe subset or stop at the relevant authority boundary.

## Factuality

Do not fabricate product features, customers, users, metrics, integrations, releases, approvals, incidents, tests, deployments, or business evidence. Proposals must be labeled as proposals or planned work.

## Security and Privacy

Do not expose or commit secrets, credentials, tokens, private keys, unnecessary personal data, or sensitive operational information. Do not weaken security controls for convenience.

## Validation

Validate changes against applicable product requirements plus the pinned shared architecture, standards, workflow, security, privacy, factuality, and compatibility requirements.

Validation is evidence; it is not approval.

## Git and Publication Boundaries

Without appropriate authorization, do not:

- commit or push candidate changes;
- create pull requests;
- modify the default branch;
- merge branches or pull requests;
- create or move tags;
- publish releases or artifacts;
- change repository visibility or protected settings;
- rewrite published history;
- modify another repository.

## Reporting

Completion reports must distinguish planned work from verified results. Never claim a remote branch, commit, PR, merge, tag, release, deployment, test result, or adoption state exists without evidence.

## Stop Conditions

Stop when:

- the authorized scope is complete;
- required authority is missing;
- repository identity or baseline is uncertain;
- an operation would affect unrelated work;
- required validation cannot be performed;
- a security, privacy, compatibility, or factuality issue cannot be resolved safely.
