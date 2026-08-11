# Freelancer Growth OS Release Process

**Status:** Active  
**Current product release status:** Unreleased

## Purpose

This document defines how Freelancer Growth OS moves from merged work to an approved, traceable product release.

A merge is not a release. Release preparation, tagging, publication, deployment, and post-release verification are distinct governed actions.

## Release Preconditions

Before a release candidate is prepared:

- intended release scope is known;
- applicable implementation work is merged;
- required tests/evals are complete;
- migration/compatibility review is complete;
- unresolved release-blocking defects are zero or explicitly accepted;
- security/privacy review is complete for applicable changes;
- release version can be justified under [VERSIONING.md](VERSIONING.md).

## 1. Select Proposed Version

Classify all included changes and propose the smallest semantic version that accurately reflects compatibility impact.

Record:

- proposed version;
- rationale;
- included PRs/changes;
- breaking/deprecated items;
- migration requirements.

Version recommendation is preparation, not release approval.

## 2. Establish Exact Release Candidate

A release candidate must identify one immutable commit SHA.

Record:

- version;
- candidate SHA;
- source branch;
- date/time of verification;
- compatibility class summary;
- required migrations;
- known limitations.

If the candidate branch moves, the candidate must be reverified and the new SHA recorded.

## 3. Changelog and Release Notes

Update [CHANGELOG.md](CHANGELOG.md) and prepare release notes describing only verified changes.

Use applicable categories:

- Added;
- Changed;
- Fixed;
- Security;
- Deprecated;
- Removed;
- Migration;
- Known Limitations.

Do not claim users, customers, performance improvements, integrations, or deployment state without evidence.

## 4. Migration and Upgrade Verification

Where applicable verify:

- fresh installation/setup;
- upgrade from the prior supported release;
- Alembic migration path;
- persisted contract/artifact compatibility;
- configuration migration;
- prompt/model migration;
- backup/export before destructive changes;
- rollback/recovery procedure.

For the first release there may be no prior product-version upgrade path, but fresh-install verification is still required.

## 5. Validation Gate

Release validation should include all applicable:

- dependency lock verification;
- formatting/linting;
- static typing;
- unit tests;
- contract tests;
- integration tests;
- database migration tests;
- AI evals for material prompt/model behavior;
- security/privacy checks;
- approval-state tests;
- CLI/API smoke tests where supported;
- local install/backup/export checks;
- documentation/link checks.

If a check is unavailable or not configured, say so explicitly rather than reporting it as passed.

## 6. Quality and Risk Review

Review:

- release scope accuracy;
- unresolved known issues;
- breaking/deprecation impact;
- migration safety;
- security/privacy risk;
- external integration dependencies;
- current-information assumptions;
- rollback/recovery readiness;
- release-note factuality.

Residual risk must be explicit.

## 7. Human Release Approval

An authorized human approves the exact:

- proposed version;
- release candidate SHA;
- known limitations/residual risk;
- publication actions to execute.

Approval of a PR or merge does not automatically approve release publication.

## 8. Release Execution

When explicitly authorized, execute only the named release actions.

Typical sequence:

1. verify candidate SHA still matches the approved candidate;
2. verify repository state and required checks;
3. create immutable tag `vMAJOR.MINOR.PATCH` at the exact candidate SHA;
4. create/publish GitHub Release targeting that tag/SHA;
5. publish any additional artifact only if separately approved;
6. deploy only if deployment is in approved release scope.

Tagging, GitHub Release publication, artifact publication, and deployment remain distinct protected actions.

## 9. Post-Release Verification

Verify as applicable:

- release tag resolves to exact approved SHA;
- GitHub Release is not draft/prerelease unless intended;
- release title/version matches;
- published artifacts match expected version/checksums where relevant;
- deployment reports correct version where deployment exists;
- critical smoke checks succeed;
- changelog/release notes are accessible.

Do not infer publication success solely from the tag existing if release publication is a separate action.

## 10. Failed or Ambiguous Release Execution

If a release action returns an ambiguous result:

- stop blind retries;
- verify remote state read-only;
- reconcile exact tag/release/artifact/deployment state;
- retry only when safe and authorized.

Never move an immutable published tag to hide an error.

## Rollback and Recovery

Rollback depends on what was released:

- application code: redeploy/reinstall prior supported version when compatible;
- database: use tested downgrade or restore/forward-fix strategy;
- prompt/model default: restore prior version/configuration;
- integration: disable/degrade adapter and reconcile ambiguous external actions;
- externally executed client/account action: use domain-specific remediation; software rollback does not automatically reverse external side effects.

## Security Releases

Security corrections may use an accelerated process, but must retain:

- exact scope;
- validation evidence;
- version justification;
- human release authority;
- traceable publication;
- disclosure appropriate to the risk.

Urgency does not authorize fabricated validation or history rewriting.

## Deprecation and Removal Releases

Release notes must clearly distinguish:

- newly deprecated behavior;
- behavior removed after deprecation;
- replacement/migration path;
- breaking version impact.

## Release Withdrawal

If a release must be withdrawn:

- preserve release/tag history;
- mark/document withdrawal rather than deleting history where practical;
- explain reason and scope;
- identify mitigation/replacement;
- provide migration/rollback guidance;
- record approving authority.

## First Release Rule

The first product release must not be created merely because Phase 3 is complete.

A first release requires actual releasable implementation, validation, release preparation, exact human approval, and explicit release execution authority.
