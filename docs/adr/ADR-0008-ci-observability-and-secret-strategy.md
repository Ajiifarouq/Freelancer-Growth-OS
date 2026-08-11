# ADR-0008 — GitHub Actions CI, Structured Audit, Runtime Secret Injection

**Status:** Accepted  
**Date:** 2026-08-11

## Decision

Use GitHub Actions for repository CI when implementation begins, structured local logs plus persisted audit/run metadata for V1 observability, and runtime-injected secrets rather than product-database secret storage.

## Drivers

- The repository already uses GitHub governance/PR workflow.
- Deterministic tests should run without paid/external provider credentials.
- Approval/execution history requires product-level audit records distinct from console logs.
- Secrets must remain outside domain persistence.

## CI baseline

- lockfile/dependency consistency;
- Ruff format/lint;
- static typing;
- pytest unit/integration tests;
- Alembic migration-to-head test;
- contract tests;
- secret detection.

Provider-backed evals remain separate controlled jobs.

## Secret policy

- local development may inject secrets through environment variables;
- local `.env` files are untracked/ignored;
- product DB stores no raw credentials;
- future deployments use managed secrets or short-lived workload identity where supported;
- workflow permissions remain least privilege.

## Consequences

- No external telemetry vendor is required for V1.
- Logs must minimise sensitive content.
- Future deployment CI/CD is separately governed from build/test CI.
- Cloud vendor and production monitoring vendor remain unselected.
