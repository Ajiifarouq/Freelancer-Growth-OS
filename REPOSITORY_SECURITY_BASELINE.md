# Freelancer Growth OS Repository Security Baseline

**Status:** Active  
**Repository:** `Ajiifarouq/Freelancer-Growth-OS`

## Purpose

This document defines repository-level controls required before implementation work becomes routine.

Repository policy documents are not sufficient by themselves. GitHub settings and automated checks should enforce the most important controls wherever the platform supports them.

## Public Repository Safety Model

The repository is currently public.

Public visibility is compatible with the project only if the following rule is absolute:

**Git contains no real runtime user/client/business data or credentials.**

Allowed:

- product code;
- public architecture/governance documentation;
- schemas/contracts;
- synthetic test/eval fixtures;
- non-secret configuration examples;
- public dependency lockfiles.

Prohibited:

- `.env` files with secrets;
- API/OAuth tokens;
- SQLite/runtime databases;
- CVs or private user files;
- client briefs/messages unless synthetic;
- real proposals/pricing histories;
- logs containing private prompts/content;
- exports/backups;
- copied Gmail/Drive/LinkedIn/private marketplace content;
- real-user eval fixtures.

A future switch to private visibility does not make Git an approved data store.

## Main Branch Protection Target

Before implementation PRs are merged routinely, configure `main` using a GitHub ruleset/branch protection equivalent with these minimum controls:

- require a pull request before merging;
- require at least one approving review by the repository owner or approved maintainer;
- require review from CODEOWNERS where supported;
- dismiss stale approvals when new commits materially change the PR;
- require conversation/review-thread resolution before merge;
- require status checks to pass before merge;
- require `Governance and Repository Safety / governance-safety`;
- later require implementation CI jobs when they exist;
- block force pushes;
- block branch deletion;
- apply rules to administrators unless an explicit emergency exception process is used.

Do not configure a rule that permits an automated reviewer to satisfy the required human approval boundary.

## Merge Race Protection

Before every merge:

1. record the exact PR head SHA reviewed;
2. refresh PR review threads after the latest automated/human review window;
3. confirm no unresolved blocking thread exists;
4. confirm required checks apply to that exact head SHA;
5. merge with an exact-head SHA guard where the tool/API supports it.

A review performed earlier in time is not proof that no later review finding exists.

## Automated Review Tools

Automated review output is advisory evidence unless explicitly promoted by governance.

If an automated reviewer such as Codex is enabled:

- it must not count as the required human owner approval;
- its review must complete before the final merge gate;
- unresolved findings must be dispositioned before merge;
- late-arriving automated findings must trigger a re-review rather than being ignored.

If the repository owner does not want a given automated reviewer, disable it in the relevant GitHub/App/integration settings. This repository intentionally does not rely on Codex for implementation authority.

## Required GitHub Actions

Current hardening workflow:

- `.github/workflows/governance-ci.yml`

It checks tracked-file safety, secret-like patterns, Markdown structure, local links, and text-file final newlines.

When implementation begins, add deterministic implementation CI covering at least:

- locked dependency consistency;
- formatting/linting;
- static typing;
- unit tests;
- contract/schema tests;
- integration tests;
- Alembic migration-to-head test;
- data deletion/export tests;
- approval-state/idempotency tests;
- architecture invariants where practical;
- dedicated secret scanning.

Provider-backed paid evals should not be required for every deterministic PR unless cost/reliability has been deliberately accepted; stable prompt/model changes still require controlled eval evidence.

## Secret Management

- `.gitignore` blocks local `.env` and common private/runtime artifacts.
- Use environment variables or approved OS secret storage during local development.
- Keep `.env.example` secret-free; use placeholder names only.
- Never store raw credentials in SQLite/domain models.
- Never print secrets in CI output, logs, exceptions, screenshots, or fixtures.
- Rotate any credential immediately if it is ever committed, even if the commit is later removed.

## GitHub Secret Scanning

Enable GitHub secret scanning/push protection if available for the repository/account plan.

Because connector access cannot currently verify or configure these settings, enabling them is a repository-settings action that must be completed manually and verified afterward.

Secret scanning complements `.gitignore`; it does not replace it.

## Repository Settings Hygiene

Recommended settings:

- disable GitHub Wiki unless it is intentionally governed, to avoid a second uncontrolled documentation source;
- keep GitHub Pages disabled unless later needed;
- keep auto-merge disabled until required checks/rules are proven reliable;
- delete merged feature branches after verification, or enable automatic branch deletion if that fits the owner's workflow;
- keep force-push/history rewrite prohibited for `main`;
- periodically review collaborators/apps with repository write access.

## Historical Branches

Historical Phase 1–6 branches are useful traceability but should not be mistaken for active development bases.

After the hardening correction is merged and verified, either:

- delete already-merged phase branches; or
- retain them intentionally and document them as historical read-only references.

New work must branch from current `main`, not an old phase branch.

## License Boundary

The repository currently has no license.

Do not infer that public visibility means open-source permission. Choose a license only after the owner decides whether the intended model is:

- proprietary/source-visible;
- permissive open source;
- copyleft open source;
- dual/commercial licensing.

This is a business/legal distribution decision, not an implementation-detail default.

## Incident Rule for Accidental Data Commit

If real sensitive data or a credential is committed:

1. stop further publication/merge work;
2. revoke/rotate credentials immediately where applicable;
3. identify all affected commits/branches/forks/artifacts;
4. remove the data from active branches;
5. assess whether history rewriting is necessary and explicitly authorize it because history rewrite is destructive;
6. treat exposed personal/client data as a privacy incident and document response;
7. do not claim deletion from GitHub/forks/caches until verified.

For secrets, rotation is mandatory even when repository history is cleaned.

## Manual GitHub Settings Checklist

These settings cannot currently be changed by the available GitHub connector and require the repository owner to apply them in GitHub UI/settings:

- [ ] Protect `main` / create repository ruleset.
- [ ] Require PR before merge.
- [ ] Require owner/CODEOWNER human review.
- [ ] Require conversation resolution.
- [ ] Require governance CI status check.
- [ ] Block force pushes and `main` deletion.
- [ ] Enable secret scanning and push protection if available.
- [ ] Disable unwanted automated Codex review/integration for this repository.
- [ ] Disable Wiki unless intentionally governed.
- [ ] Decide merged-branch deletion policy.
- [ ] Decide repository visibility for IP/business strategy.
- [ ] Decide license before public reuse/contribution.

Implementation readiness is not considered fully hardened until the branch/check/secret settings that are available on the owner's GitHub plan are configured and verified.
