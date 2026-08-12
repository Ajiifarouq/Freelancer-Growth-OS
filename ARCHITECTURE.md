# Freelancer Growth OS Architecture

## Purpose

This document defines product architecture authority and current architecture maturity without confusing architecture decisions with implemented software.

## Shared Governance Baseline

Product architecture is governed by:

- `Ajiifarouq/GrowthOS-Engineering`
- tag `v0.1.0`
- commit `7ee056f938e12b5a72d1ee919a27f05ec5297c69`

Dependency direction:

`Freelancer Growth OS → GrowthOS Engineering`

## Product Responsibility

This repository owns product-specific:

- requirements;
- current product/technical decisions;
- domain behavior;
- product workflows;
- modules and interfaces;
- canonical contracts;
- data lifecycle;
- deployment/runtime decisions;
- product-specific prompts/roles;
- integrations;
- product roadmap.

Listing responsibility categories does not assert implementation.

## Requirements and Decision Baseline

[PRODUCT_REQUIREMENTS.md](PRODUCT_REQUIREMENTS.md) defines the approved requirements baseline.

[DECISION_REGISTER.md](DECISION_REGISTER.md) records current resolution of decisions that were intentionally open in Phase 2A and later resolved through architecture/hardening.

Architecture decisions must trace to requirements, owner decisions, constraints, or explicit current decisions. Architecture must not manufacture requirements merely to justify technology.

## Logical Architecture Baseline

[CAPABILITY_ARCHITECTURE.md](CAPABILITY_ARCHITECTURE.md) defines stable product capabilities, logical data flow, dependency direction, AI/human authority boundaries, knowledge/freshness responsibilities, security/privacy boundaries, and validation ownership.

[MODULE_CATALOG.md](MODULE_CATALOG.md) defines initial stable module IDs and responsibilities.

[CONTRACT_REGISTRY.md](CONTRACT_REGISTRY.md) is the canonical implementation-facing contract authority and resolves older naming aliases.

## Technical Architecture Baseline

[TECHNICAL_ARCHITECTURE.md](TECHNICAL_ARCHITECTURE.md) is the primary technical architecture.

Supporting architecture/control documents:

- [DATA_ARCHITECTURE.md](DATA_ARCHITECTURE.md);
- [DATA_GOVERNANCE.md](DATA_GOVERNANCE.md);
- [AI_RUNTIME_ARCHITECTURE.md](AI_RUNTIME_ARCHITECTURE.md);
- [PROVIDER_DATA_POLICY.md](PROVIDER_DATA_POLICY.md);
- [SECURITY_INTEGRATION_ARCHITECTURE.md](SECURITY_INTEGRATION_ARCHITECTURE.md);
- [REPOSITORY_SECURITY_BASELINE.md](REPOSITORY_SECURITY_BASELINE.md);
- [DEPLOYMENT_OPERATIONS.md](DEPLOYMENT_OPERATIONS.md);
- accepted records under [`docs/adr/`](docs/adr/).

These documents define approved choices/controls, not deployed software.

## Shared Responsibility Boundary

GrowthOS Engineering owns reusable engineering governance. Freelancer Growth OS must not redefine shared governance merely to make product implementation easier.

Product-specific extensions may be introduced only under [GOVERNANCE.md](GOVERNANCE.md).

## Architectural Invariants

- Shared governance remains external and pinned to an immutable released baseline.
- Product-specific behavior stays in this repository.
- Protected human approval boundaries are not implicitly delegated to automation.
- Repository and release state remain traceable.
- Security, privacy, factuality, compatibility, and data lifecycle cannot be bypassed for implementation convenience.
- Architecture claims require requirements or implementation evidence.
- The staged-hybrid product form must not introduce SaaS complexity before requirements support it.
- Consequential connected actions preserve the human-approval authority model.
- Evidence/factuality/freshness controls remain shared foundations rather than hidden business-decision owners.
- Connected-source access remains a controlled boundary rather than direct unrestricted module access.
- Downstream feedback re-enters through explicit evidence ingestion rather than silently mutating upstream truth.
- Domain/application code remains independent of provider, database, CLI, HTTP, and connector SDK implementations.
- Real runtime user/client/business data never lives inside the Git working tree.
- Canonical contract IDs/versions come from `CONTRACT_REGISTRY.md`.
- AI output is untrusted until canonical contract validation succeeds.
- LLM confidence cannot promote evidence to authoritative `verified` state.
- Derived artifacts become stale/invalid when material dependencies change and cannot drive consequential execution until revalidated.
- Approval is bound to exact action payload and must be protected against replay/double execution.

## Current Architecture Status

**Status:** Requirements, logical architecture, technical architecture, and pre-implementation safety controls are established as documentation candidates. Product implementation has not started.

### Phase 2A — Requirements Consolidation

Established product requirements, owner decisions, user/maturity model, capability scope, functional/non-functional requirements, security/privacy requirements, non-goals, and an open-decision register representing Phase 2A's historical state.

### Phase 2B — Capability and Module Architecture

Established eight capability boundaries, seventeen initial module IDs, logical contracts, dependencies, cycle controls, validation ownership, and human/AI authority boundaries.

### Phase 2C — Technical Architecture

Established:

- local-first modular-monolith V1 topology;
- CPython 3.14 + `uv` runtime/project strategy;
- Pydantic contracts with ports/adapters;
- Typer CLI first interface;
- FastAPI as later HTTP adapter;
- SQLite + SQLAlchemy + Alembic persistence/migrations;
- PostgreSQL migration target for justified future SaaS;
- provider-neutral LLM port with OpenAI Responses reference adapter;
- no vector database for V1;
- current-research/freshness port;
- read/write connector separation;
- deterministic human-approval execution state machine;
- secret isolation and prompt-injection controls;
- local deployment/environment strategy;
- GitHub Actions CI strategy;
- structured logging/audit/backup/recovery expectations;
- architecture decision records for material choices.

### Pre-Implementation Hardening

Hardening adds/clarifies:

- canonical contract registry and alias resolution;
- local V1 retention/deletion/export/workspace lifecycle;
- provider data minimization/retention/capability verification;
- repository/runtime-data separation;
- evidence verification authority;
- dependency/staleness invalidation;
- approval payload binding/idempotency/replay protection;
- repository CI and branch/ruleset security target;
- current decision reconciliation.

## Architecture Disposition

Phase 2 architecture is complete historically, but **implementation remains blocked by the Pre-Implementation Hardening gate until the hardening candidate and applicable GitHub settings are verified**.

After hardening passes, the next engineering stage is:

**Implementation Phase 1 — Foundation and First End-to-End Growth Acquisition Vertical Slice.**

That implementation still requires its own specification/readiness review and explicit implementation authorization.

## Out of Scope / Not Claimed

This architecture does not claim:

- completed application code;
- deployed product features;
- customers/users/revenue;
- direct Upwork/Fiverr/Terrawork or other external integrations;
- production SaaS infrastructure;
- a deployed web frontend;
- remote authentication;
- production reliability SLAs;
- encrypted-at-rest application storage until a later ADR selects/validates it;
- a product release.

The repository remains **Unreleased**.
