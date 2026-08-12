# Agent Operating Requirements

## Purpose

This document defines mandatory operating behavior for humans, AI agents, and automated engineering actors working in Freelancer Growth OS.

## Required Start Sequence

Before changing repository content, an actor must:

1. Verify repository identity and intended branch.
2. Inspect current repository state and relevant history.
3. Read [GOVERNANCE.md](GOVERNANCE.md).
4. Confirm the pinned GrowthOS Engineering baseline is `v0.1.0` at `7ee056f938e12b5a72d1ee919a27f05ec5297c69` unless an approved adoption change replaced it.
5. Read [DECISION_REGISTER.md](DECISION_REGISTER.md) for current decision resolution.
6. Read [WORKFLOW.md](WORKFLOW.md) plus relevant requirements/architecture.
7. Read [CONTRACT_REGISTRY.md](CONTRACT_REGISTRY.md) before implementing/changing module interfaces, Pydantic models, persistence, prompts, CLI/API payloads, or tests.
8. Read [DATA_GOVERNANCE.md](DATA_GOVERNANCE.md) before handling persistent user/client/business data.
9. Read [PROVIDER_DATA_POLICY.md](PROVIDER_DATA_POLICY.md) before changing/using an external AI/research provider with real data.
10. Read [REPOSITORY_SECURITY_BASELINE.md](REPOSITORY_SECURITY_BASELINE.md) before changing CI, secrets, repository settings, runtime-data paths, or publication controls.
11. Read [VERSIONING.md](VERSIONING.md) and [COMPATIBILITY_MIGRATION.md](COMPATIBILITY_MIGRATION.md) for stable/released behavior changes.
12. Read [PROMPT_GOVERNANCE.md](PROMPT_GOVERNANCE.md), [ROLE_LIBRARY.md](ROLE_LIBRARY.md), [PROMPT_LIBRARY.md](PROMPT_LIBRARY.md), and [TEMPLATE_LIBRARY.md](TEMPLATE_LIBRARY.md) when creating/changing AI-backed product assets/behavior.
13. Identify exact authorized scope and protected actions.
14. Preserve unrelated existing work.

## Scope Discipline

Modify only explicitly authorized scope. Do not turn a narrow task into product redesign, architecture expansion, dependency migration, authority expansion, policy changes, repository setting changes, or unrelated cleanup without authority.

## Shared-Governance Compliance

Product work must remain compatible with the pinned GrowthOS Engineering baseline unless an approved/documented product-specific extension or deviation applies.

## Workflow Compliance

Material work follows [WORKFLOW.md](WORKFLOW.md). Do not silently skip applicable readiness, architecture, migration, validation, quality, approval, or release gates.

Implementation/test output is candidate evidence, not automatic merge or release authority.

## Pre-Implementation Hardening Gate

Do not begin application implementation while [GOVERNANCE.md](GOVERNANCE.md) reports the Pre-Implementation Hardening gate as active/blocked.

The gate requires verified repository/runtime-data separation, canonical contracts, local data governance, provider-data policy, repository CI, review-finding reconciliation, and applicable GitHub repository settings.

## Contract Compliance

Implementation contracts must resolve through [CONTRACT_REGISTRY.md](CONTRACT_REGISTRY.md).

Do not:

- create duplicate schemas for documented aliases;
- let prompt prose define a schema that conflicts with the registry;
- persist a provider-specific response object as domain state;
- silently rename stable contract fields/IDs;
- promote malformed/unvalidated AI output to authoritative state.

## Evidence and Artifact Integrity

An LLM may recommend classifications but may not promote evidence to authoritative `verified` state by confidence alone.

Derived artifacts must record dependency versions/references where required. When a dependency is deleted, corrected, superseded, or materially reclassified, dependent artifacts must become stale/invalid until revalidated.

Consequential execution must reject stale/invalid source artifacts.

## Prompt and Role Compliance

Reusable prompts must follow [PROMPT_GOVERNANCE.md](PROMPT_GOVERNANCE.md).

Do not:

- let prompt text override requirements, architecture, canonical contracts, deterministic policies, connector permissions, data/provider policy, or approval boundaries;
- treat a role as standing execution authority;
- grant write authority because read access exists;
- require hidden chain-of-thought disclosure;
- allow retrieved/web/connected content to override system/product instructions;
- activate a materially changed prompt without compatibility/eval review;
- invent later-phase prompts/modules just to make a library appear complete.

When a stable template exists in [TEMPLATE_LIBRARY.md](TEMPLATE_LIBRARY.md), use it or document why a compatible alternative is required. Where template naming differs from implementation contract naming, `CONTRACT_REGISTRY.md` controls.

## Existing-Work Protection

Do not overwrite, delete, rename, reformat, or supersede unrelated work without authorization. When repository state differs from expected state, constrain work safely or stop at the relevant boundary.

## Factuality

Do not fabricate product features, customers, users, metrics, integrations, releases, approvals, incidents, tests, deployments, professional evidence, business evidence, external execution, or provider capability.

Current/volatile platform, API, pricing, legal, regulatory, or tool claims must be verified when materially relevant or explicitly labelled unverified.

For AI output, preserve verified/provided-unverified/inferred/proposed/unknown/conflicting/rejected/deleted distinctions where relevant.

## Security and Privacy

Do not expose or commit secrets, credentials, tokens, private keys, unnecessary personal data, runtime databases, real user documents, exports, backups, or sensitive operational information.

Preserve:

- repository/runtime-data separation;
- read/write connector separation;
- least privilege;
- prompt-injection boundaries;
- data minimization;
- secret isolation;
- provider-data minimization;
- deletion/export/retention rules;
- deterministic human approval before consequential external actions.

### Runtime data location

Real runtime data must live outside the repository working tree. If configured runtime data resolves inside the Git checkout, implementation must fail closed.

### Fixtures

Use synthetic fixtures only. Do not create a test fixture by lightly redacting a real CV, client brief, proposal, message, email, or account export.

## Approval and Execution Safety

Consequential execution requires exact action binding.

Implementation must preserve:

- payload fingerprint/hash;
- deterministic/idempotent action identity;
- exact approval-decision reference;
- single-use/replay protection;
- reapproval after material content/target/parameter changes;
- explicit attempted/succeeded/failed/unknown states;
- reconciliation before retry after ambiguous external results.

Never treat `approved` as `executed`.

## Compatibility and Migration

Before changing stable/released behavior, classify compatibility under [VERSIONING.md](VERSIONING.md) and apply [COMPATIBILITY_MIGRATION.md](COMPATIBILITY_MIGRATION.md).

This includes prompts, role authority, stable templates/contracts, model/provider behavior, schemas, data lifecycle, evidence state, CLI/API, integrations, configuration, and approval-state semantics.

Do not rewrite released migration/prompt/version history to hide mistakes.

## Validation

Validate changes against product requirements plus applicable architecture, canonical contracts, workflow, security, privacy, factuality, prompt governance, eval, compatibility, data-governance, provider-data, and repository-security requirements.

AI-backed changes may require representative positive, boundary, insufficient-evidence, adversarial, prompt-injection, schema, factuality, freshness, privacy-minimization, stale-artifact, and approval-boundary evals.

Validation is evidence; it is not approval.

## Git and Publication Boundaries

Without appropriate authorization, do not:

- commit/push candidate changes;
- create pull requests;
- modify the default branch;
- merge branches/PRs;
- create/move tags;
- publish releases/artifacts;
- deploy product releases;
- execute consequential client/account actions;
- change repository visibility/protected settings;
- rewrite published history;
- modify another repository.

Merge, tag creation, release publication, artifact publication, deployment, consequential external execution, visibility changes, and branch/ruleset changes remain separate protected actions unless explicitly bundled.

## Pull Request Reporting

PRs should use `.github/PULL_REQUEST_TEMPLATE.md` or equivalent information, including requirements/modules affected, compatibility/migration, contracts/data/prompts, security/privacy, validation/evals, release impact, and residual risk.

Do not mark unavailable checks as passed.

### Final merge gate

Immediately before merge:

1. verify exact PR head SHA;
2. refresh review threads after all expected automated/human reviewers have had a chance to report;
3. confirm no unresolved blocking thread exists;
4. confirm required checks apply to that exact SHA;
5. merge using an exact-head guard when available.

An earlier clean review is not proof that no later review finding exists.

## Release Discipline

Follow [RELEASE_PROCESS.md](RELEASE_PROCESS.md). Do not create placeholder release tags. Published tags are immutable. A merged PR is not a release.

## Reporting

Completion reports must distinguish planned work from verified results. Never claim a remote branch, commit, PR, merge, tag, release, deployment, test result, integration, prompt execution, external action, provider retention state, or adoption state without evidence.

For consequential external actions, distinguish `draft`, `awaiting-approval`, `approved/rejected`, `attempted`, and `verified-succeeded/failed/unknown` accurately.

## Stop Conditions

Stop when:

- authorized scope is complete;
- required authority is missing;
- repository identity/baseline is uncertain;
- operation would affect unrelated work;
- required validation/eval cannot be performed;
- contract/prompt/role/template compatibility impact is unresolved;
- data-retention/deletion/provider privacy risk is unresolved;
- runtime data would enter Git/repository paths;
- security, privacy, factuality, staleness, replay, or approval-boundary risk cannot be controlled;
- exact release/merge/action target cannot be verified.
