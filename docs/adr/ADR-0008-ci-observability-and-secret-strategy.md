# ADR-0008 — GitHub Actions CI, Structured Audit, Runtime Secret Injection

**Status:** Accepted and partially implemented for repository governance  
**Date:** 2026-08-11  
**Hardening update:** 2026-08-12

## Decision

Use GitHub Actions for repository/application CI, structured local logs plus persisted audit/run metadata for V1 observability, and runtime-injected secrets rather than product-database secret storage.

The pre-implementation hardening package adds repository-governance CI before product code exists. Application CI expands when implementation begins.

## Drivers

- The repository uses GitHub governance/PR workflow.
- Deterministic tests should run without paid/external provider credentials.
- Approval/execution history requires product-level audit records distinct from console logs.
- Secrets must remain outside domain persistence.
- Repository rules should be enforced automatically where practical rather than relying only on documentation.

## Current Repository-Governance CI

- `.github/workflows/governance-ci.yml`
- `.github/scripts/governance_check.py`

Current checks include:

- forbidden tracked `.env` files;
- forbidden runtime/private-data directories;
- database/secret artifact suffixes;
- common secret-like token/private-key patterns;
- Markdown H1 structure;
- repository-local Markdown links;
- final newline for tracked text files.

## Application CI Baseline

When implementation begins, expand/require:

- lockfile/dependency consistency;
- Ruff format/lint;
- static typing;
- pytest unit/integration tests;
- canonical contract tests;
- Alembic migration-to-head tests;
- data deletion/export/backup tests;
- approval/idempotency/staleness tests;
- dedicated secret detection/scanning.

Provider-backed evals remain separate controlled jobs unless a later workflow decision changes that rule.

## Secret Policy

- `.gitignore` now blocks local `.env` and common secret/runtime-data artifacts;
- local development may inject secrets through environment variables or a future approved OS secret store;
- `.env.example` may contain placeholder variable names only, never real values;
- product DB stores no raw credentials;
- provider/connector prompts/contracts receive no raw secrets;
- future deployments use managed secrets or short-lived workload identity where supported;
- workflow permissions remain least privilege;
- GitHub secret scanning/push protection should be enabled in repository settings when available.

If a credential is ever committed, rotate/revoke it immediately even if Git history is later cleaned.

## Observability / Audit Consequences

- No external telemetry vendor is required for V1.
- Logs must minimise sensitive content and follow `DATA_GOVERNANCE.md` retention.
- Audit records use opaque references/hashes rather than duplicating private payloads where practical.
- Prompt/provider run metadata may record IDs/versions/content hashes, but not hidden chain-of-thought or full private provider payloads by default.

## Repository Enforcement Consequences

- `main` should require repository-governance CI and later application CI through branch/ruleset protection.
- CODEOWNERS identifies the repository owner boundary.
- Manual GitHub setting requirements are defined in `REPOSITORY_SECURITY_BASELINE.md` and tracked in issue #9.
- Future deployment CI/CD remains separately governed from build/test CI.
- Cloud vendor and production monitoring vendor remain unselected.
