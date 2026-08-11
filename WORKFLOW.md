# Freelancer Growth OS Engineering Workflow

**Status:** Active  
**Product release status:** Unreleased  
**Governance baseline:** `Ajiifarouq/GrowthOS-Engineering` `v0.1.0` at `7ee056f938e12b5a72d1ee919a27f05ec5297c69`

## Purpose

This document defines the product-specific engineering workflow for Freelancer Growth OS. It extends the shared GrowthOS Engineering lifecycle without replacing it.

The governing lifecycle remains:

`Intake → Triage → Architecture Review → Specification → Readiness Review → Implementation → Validation → Quality Review → Human Approval → Release Preparation → Release Execution → Maintenance`

Not every change requires the same depth at every step, but applicable gates may not be silently skipped.

## 1. Change Intake

Every material change should identify:

- requested outcome;
- affected requirements, capabilities, modules, contracts, prompts, data, adapters, or documentation;
- repository scope;
- known risks;
- expected compatibility class;
- whether current external facts must be verified;
- protected actions expected later in the workflow.

Small documentation corrections may use a lightweight intake in the PR description. Larger feature, schema, contract, integration, authority, or release changes require an explicit written specification or issue/decision record.

## 2. Triage

Classify the work as one or more of:

- documentation;
- defect correction;
- internal refactor;
- product capability change;
- contract/schema change;
- database migration;
- prompt/AI-behavior change;
- LLM/provider adapter change;
- connected-service integration change;
- security/privacy change;
- release/operations change;
- breaking change.

Triage must identify whether work belongs in Freelancer Growth OS or the shared GrowthOS Engineering repository.

## 3. Architecture Review

Architecture review is mandatory for changes that materially affect:

- capability/module boundaries;
- application/domain dependency direction;
- Pydantic/public data contracts;
- persistence ownership or database schema;
- CLI/API interfaces;
- LLM provider abstraction;
- research/freshness boundary;
- connected-service read/write boundary;
- human-approval state machine;
- authentication/authorisation;
- deployment topology;
- compatibility or migration strategy.

Architecture review must reference the applicable architecture document or create/update an ADR when the choice is material and long-lived.

## 4. Specification

Implementation-ready work must state:

- requirement(s) served;
- user/system outcome;
- scope and non-goals;
- inputs and outputs;
- error/failure behavior;
- security/privacy implications;
- factuality/freshness implications where relevant;
- acceptance criteria;
- tests/evals required;
- compatibility class;
- migration or rollback need;
- approval boundaries.

AI-driven behavior must also state evidence expectations and prohibited fabrication/failure modes.

## 5. Readiness Review

A change is implementation-ready only when:

- scope is sufficiently specific;
- requirements and architecture are traceable;
- required data/contracts are known;
- acceptance criteria are testable;
- security/privacy boundaries are understood;
- required current facts have been verified or explicitly deferred;
- dependencies are available;
- migration/compatibility implications are known enough to proceed;
- required implementation authority exists.

If any item is materially unknown, mark the change blocked rather than hiding the gap inside implementation.

## 6. Branching

Protected/default branch work uses a dedicated branch.

Recommended branch forms:

- `feature/<short-name>`;
- `fix/<short-name>`;
- `docs/<short-name>`;
- `refactor/<short-name>`;
- `security/<short-name>`;
- `release/<version>`;
- governed phase branches when executing repository-adoption work.

Branch names must be descriptive and lower-kebab-case after the prefix.

Do not develop new product work directly on `main`.

## 7. Implementation Rules

Implementation must:

- stay within approved scope;
- preserve `interfaces → application → domain` dependency direction;
- keep infrastructure behind ports/adapters;
- keep secrets outside domain contracts and repository content;
- preserve explicit evidence/fact/inference boundaries;
- preserve the deterministic human-approval gate for consequential external actions;
- add or update tests/evals proportional to the change;
- update documentation when behavior/contracts change;
- avoid unrelated cleanup unless separately justified.

Candidate implementation is not evidence of correctness, approval, or release.

## 8. Commit Discipline

Commits should be coherent and reviewable.

Preferred message categories include:

- `feat:` capability behavior;
- `fix:` defect correction;
- `docs:` documentation;
- `refactor:` behavior-preserving internal change;
- `test:` test/eval-only change;
- `chore:` tooling/maintenance;
- `security:` security-focused change;
- `release:` release preparation.

Commit prefixes support readability but do not determine semantic version impact automatically. Compatibility analysis controls versioning.

## 9. Pull Request Gate

Every implementation PR must identify:

- exact base/head scope;
- requirements/modules affected;
- summary of behavior change;
- changed contracts/schemas/prompts where applicable;
- tests/evals executed;
- migration/compatibility impact;
- security/privacy impact;
- current-information verification when relevant;
- residual risks or open questions;
- whether the PR is release-neutral or part of a release candidate.

Draft PRs are preferred until the author believes the candidate is ready for formal review.

## 10. Validation

Validation is proportional to risk and may include:

- format/lint checks;
- static typing;
- unit tests;
- contract/schema tests;
- SQLite/integration tests;
- Alembic migration tests;
- deterministic approval-state tests;
- connector adapter tests with fakes/mocks;
- prompt/AI evals;
- factuality/provenance checks;
- prompt-injection/abuse tests;
- security/privacy review;
- documentation/link checks;
- manual acceptance testing.

Validation results are evidence. They do not self-authorize merge or release.

## 11. Quality Review

Review must check:

- requirement fit;
- architecture fit;
- maintainability;
- failure modes;
- contract/data compatibility;
- migration safety;
- factuality and uncertainty handling;
- AI authority boundaries;
- security/privacy;
- test/eval adequacy;
- operational impact;
- release-note relevance.

A failed review returns work to the earliest stage necessary to correct the issue.

## 12. Human Approval

Human approval is required where governance, repository controls, architecture authority, connected-action authority, or release policy requires it.

Automation may validate and prepare evidence but must not convert validation into human approval.

## 13. Merge Gate

Before merge:

- PR head SHA must be reverified;
- required checks/reviews must be complete or an explicit documented exception must exist;
- unresolved blocking review threads must be zero;
- migration compatibility must be understood;
- protected merge authority must exist.

If automated checks do not exist, report that accurately rather than claiming CI passed.

## 14. Release Preparation

Release preparation is separate from merge.

It includes as applicable:

- proposed semantic version;
- release candidate commit SHA;
- changelog/release notes;
- compatibility classification;
- migration/upgrade instructions;
- database migration verification;
- prompt/model behavior notes where material;
- security/privacy notes;
- backup/rollback guidance;
- artifact verification;
- known limitations.

Preparation does not authorize tagging or publication.

## 15. Release Execution

Release execution may include separately protected actions such as:

- merge of release-preparation work;
- immutable `vMAJOR.MINOR.PATCH` tag creation;
- GitHub Release publication;
- artifact publication;
- deployment.

Each action requires its applicable authorization. A successful merge is not automatically a release.

## 16. Maintenance

Defects, feedback, compatibility issues, dependency upgrades, prompt regressions, migrations, deprecations, and security findings re-enter the controlled lifecycle at the earliest appropriate stage.

Urgency may shorten ceremony but does not erase traceability, validation, or authority requirements.

## Change Classes and Minimum Gates

| Change | Minimum expected gates |
|---|---|
| Documentation-only clarification | Intake → Implementation → Validation → Review → Approval/Merge |
| Internal refactor | Intake → Triage → Readiness → Implementation → Validation → Review → Approval/Merge |
| Feature/module behavior | Full lifecycle through merge; release gates when publishing |
| Contract/schema/database change | Full lifecycle + compatibility/migration review |
| Prompt/AI behavior change | Full lifecycle + eval/factuality review |
| Connected write/integration change | Full lifecycle + security/privacy + approval-state review |
| Breaking change | Full lifecycle + migration guidance + explicit breaking-change approval |
| Release | All applicable gates through Release Execution |

## Stop Conditions

Stop when:

- authorization is missing;
- scope becomes materially ambiguous;
- required evidence/current verification is unavailable;
- architecture or compatibility impact is unresolved;
- migration safety cannot be established;
- security/privacy risk is not adequately controlled;
- exact branch/PR/release target cannot be verified;
- the next action crosses a protected boundary not covered by authorization.
