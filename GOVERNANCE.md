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

GrowthOS Engineering remains authoritative for shared engineering governance. This repository remains authoritative for Freelancer Growth OS product-specific requirements, current decisions, architecture, implementation, workflow, versioning, contracts, data governance, templates, roles, prompts, content conformance, repository security, and releases.

## Baseline Pinning Rules

- Do not treat upstream `main` as the governing baseline.
- Governance adoption changes must identify the exact new tag and commit SHA.
- An upstream update does not automatically modify this product repository's governing baseline.
- Compatibility impact must be reviewed before adopting a newer GrowthOS Engineering release.
- Historical released baselines must remain traceable.

## Product Requirements Authority

[PRODUCT_REQUIREMENTS.md](PRODUCT_REQUIREMENTS.md) is the authoritative product-requirements baseline.

Requirements approval does not imply implementation or release.

## Current Decision Authority

[DECISION_REGISTER.md](DECISION_REGISTER.md) records the current resolution status of owner/product/technical decisions that evolved after Phase 2A.

The Phase 2A open-decision table is historical evidence of what was unresolved at that time. When a later governed architecture/ADR/hardening decision resolved an item, the current decision register governs implementation status without rewriting history.

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

## Product Contract Authority

[CONTRACT_REGISTRY.md](CONTRACT_REGISTRY.md) is the canonical implementation-facing authority for logical/serialized contract IDs, aliases, ownership, versions, prompt-to-contract mapping, evidence-state transitions, and artifact-staleness semantics.

Where earlier architecture/template/prompt wording uses a documented alias, implementation must resolve it through the canonical contract registry rather than creating duplicate schemas.

An LLM-generated object is not authoritative product state until the canonical contract validates and deterministic application policy accepts the state transition.

## Data Governance Authority

[DATA_GOVERNANCE.md](DATA_GOVERNANCE.md) defines the mandatory local V1 data lifecycle before persistent personal/client/business data may be enabled.

It governs:

- repository/runtime-data separation;
- workspace lifecycle;
- retention;
- deletion and export;
- backups;
- local log minimization;
- encryption/device-protection expectations;
- evidence state;
- dependency invalidation/staleness;
- persistent-data readiness tests.

Real runtime user/client/business data must never be stored in the Git repository working tree.

Future SaaS/remote data governance requires a separate approved extension; local V1 rules are not automatically sufficient for remote legal/privacy requirements.

## Provider Data Authority

[PROVIDER_DATA_POLICY.md](PROVIDER_DATA_POLICY.md) governs external AI/research provider data minimization, volatile capability verification, provider-side retention awareness, tool allowlisting, structured-output validation, and sensitive-data processing boundaries.

Provider statements such as `not used for training by default` must not be represented as `not retained`.

## Repository Security Authority

[REPOSITORY_SECURITY_BASELINE.md](REPOSITORY_SECURITY_BASELINE.md), `.gitignore`, CODEOWNERS, and repository CI define the minimum repository hardening target.

Repository policy is not a substitute for GitHub-enforced branch/ruleset settings. Where the connector cannot configure settings, manual owner configuration remains an explicit readiness item.

## Product Workflow and Versioning Authority

[WORKFLOW.md](WORKFLOW.md) defines the controlled product lifecycle. [VERSIONING.md](VERSIONING.md), [COMPATIBILITY_MIGRATION.md](COMPATIBILITY_MIGRATION.md), [RELEASE_PROCESS.md](RELEASE_PROCESS.md), and [CHANGELOG.md](CHANGELOG.md) govern compatibility, migrations, versions, release candidates, release execution, and change history.

Validation is evidence, not approval. Merge, tag creation, release publication, artifact publication, and deployment remain separate protected actions unless explicit authorization bundles them.

## Product Template Authority

[TEMPLATE_LIBRARY.md](TEMPLATE_LIBRARY.md) defines reusable product templates for capability/module specifications, evidence, freelancer context, positioning, opportunities, proposals, pricing, validation, connected context, approvals, execution results, prompt changes, and release candidates.

Templates standardize information and handoffs. A filled template does not itself prove implementation, approval, execution, or release.

When a template name differs from the canonical implementation contract name, [CONTRACT_REGISTRY.md](CONTRACT_REGISTRY.md) controls alias resolution and implementation identity.

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

Prompt instructions remain subordinate to requirements, architecture, canonical contracts, deterministic policies, role contracts, connector permissions, data/provider policy, and human approval. A prompt cannot grant itself authority by wording.

## Product Content Conformance Authority

[PRODUCT_CONTENT_CONFORMANCE_REGISTER.md](PRODUCT_CONTENT_CONFORMANCE_REGISTER.md) records how current, historical, duplicate, adjacent, superseded, legacy, and out-of-scope product material relates to the authoritative repository system.

[ADOPTION_PHASE_5_REPORT.md](ADOPTION_PHASE_5_REPORT.md) records the Phase 5 evidence and completion disposition.

Historical user files, prompt drafts, release prompts, project-development prompts, external notes, and legacy artifacts are not automatically active product authority. They must be mapped through the conformance register or separately adopted through requirements/governance change control before they can override or extend active product behavior.

A historical asset may remain useful evidence even when classified `SUPERSEDED`, `LEGACY`, `DUPLICATE`, or `OUT-OF-SCOPE`.

## Integrated Adoption Audit Authority

[ADOPTION_PHASE_6_REPORT.md](ADOPTION_PHASE_6_REPORT.md) records the original integrated adoption and release-readiness audit.

Phase 6 completion means the adopted governance/product-design foundation was audited as a coherent whole. It does **not** mean application implementation, runtime validation, release-candidate approval, product release, publication, or deployment occurred.

Late review findings on PR #8 identified additional pre-implementation gaps after the initial audit disposition. Those findings are not hidden or treated as resolved by the merge. They are superseded only by verified corrective evidence in the approved hardening change.

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

Product prompts/roles must distinguish verified facts from inference, recommendations, unknowns, conflicts, rejected claims, planned work, and historical source material.

An LLM may recommend an evidence classification but cannot promote evidence to authoritative `verified` state through confidence/wording alone.

## Security and Privacy

Do not commit secrets, credentials, tokens, private keys, unnecessary personal data, runtime databases, user exports/backups, or sensitive operational information.

Preserve:

- repository/runtime data separation;
- read/write connector separation;
- prompt-injection boundaries;
- explicit consequential-action approval;
- secret isolation from domain persistence and prompt context;
- least privilege;
- accurate execution-state reporting;
- data minimization and source-specific access boundaries;
- dependency/staleness tracking;
- deletion/export/retention policy;
- provider-data boundary.

## Approval and Execution Integrity

Consequential execution must bind approval to the exact material action.

Implementation must provide:

- immutable payload fingerprint/hash;
- deterministic/idempotent action identity;
- exact approval-decision reference;
- rejection of stale/invalid source artifacts;
- reapproval after material content/target/parameter changes;
- reconciliation before retry when execution result is ambiguous;
- protection against double execution/replay.

`approved` is never equivalent to `attempted` or `verified-succeeded`.

## Compatibility and Migration

Released/stable behavior changes require compatibility classification and migration analysis.

This includes material changes to prompts, role authority, canonical contracts/templates, output schemas, connector semantics, approval states, evidence states, provider/model behavior, and data-retention/deletion semantics.

Historical-source classification by itself does not change stable runtime behavior. Importing or activating a historical asset later may require requirements, compatibility, migration, and prompt-eval review.

Published migrations/tags/history must not be rewritten to simulate a cleaner past.

## Adoption Lifecycle

The controlled governance-adoption sequence is complete through:

1. Product Governance Entry Layer.
2. Architecture and Standards Alignment.
3. Workflow and Versioning Alignment.
4. Templates, Roles, and Prompts Alignment.
5. Existing Product Content Conformance.
6. Integrated Adoption Audit and Product Release Readiness.

After Phase 6, normal product engineering proceeds through [WORKFLOW.md](WORKFLOW.md). The pre-implementation hardening gate corrects audit/review findings before implementation starts; it is not a seventh governance-adoption phase.

## Pre-Implementation Hardening Gate

Implementation Phase 1 must not begin until the hardening candidate is reviewed/merged/verified and these conditions are satisfied:

- `.gitignore`/runtime data exclusions exist;
- repository governance CI exists and passes;
- canonical contracts are established;
- local V1 data governance is established;
- provider-data/capability verification policy is established;
- Phase 6 late review findings are dispositioned with evidence;
- current decision status is reconciled;
- stale-artifact/evidence-state/approval-replay controls are explicit;
- GitHub branch/ruleset/secret settings available to the owner are manually configured and verified, or an explicit documented exception exists.

## Current Status

Completed:

- **Phase 1 — Product Governance Entry Layer**.
- **Phase 2 — Architecture and Standards Alignment**.
- **Phase 3 — Workflow and Versioning Alignment**.
- **Phase 4 — Templates, Roles, and Prompts Alignment**.
- **Phase 5 — Existing Product Content Conformance**.
- **Phase 6 — Integrated Adoption Audit and Product Release Readiness**.

Current gate:

- **Pre-Implementation Hardening — ACTIVE / IMPLEMENTATION BLOCKED UNTIL VERIFIED**.

Next lifecycle after the hardening gate passes:

- **Implementation Phase 1 — Foundation and First End-to-End Growth Acquisition Vertical Slice**, subject to implementation specification/readiness review and explicit implementation authority.

Product implementation remains not started and the repository remains Unreleased. Adoption completion or hardening documentation does not imply implemented software, deployed AI agents, marketplace integrations, test/eval success, or product release.
