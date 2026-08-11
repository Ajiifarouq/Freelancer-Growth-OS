# Freelancer Growth OS

**Status:** Unreleased  
**Maturity:** Engineering Workflow & Versioning Foundation  
**Repository:** `Ajiifarouq/Freelancer-Growth-OS`

## Purpose

Freelancer Growth OS is the product repository for product-specific requirements, behavior, workflows, modules, prompts, interfaces, data models, implementation choices, and product roadmap decisions associated with Freelancer Growth OS.

This repository does not redefine shared GrowthOS engineering governance. Shared engineering rules are adopted from the pinned GrowthOS Engineering baseline described below.

## Governance Dependency

This repository adopts:

- **Upstream repository:** `Ajiifarouq/GrowthOS-Engineering`
- **Released baseline:** `v0.1.0`
- **Pinned commit:** `7ee056f938e12b5a72d1ee919a27f05ec5297c69`

The pinned tag and commit are the governance reference for this adoption. A floating `main` reference must not be used as the governing baseline.

## Source of Truth

- Shared engineering governance: GrowthOS Engineering `v0.1.0` at `7ee056f938e12b5a72d1ee919a27f05ec5297c69`.
- Product requirements: [PRODUCT_REQUIREMENTS.md](PRODUCT_REQUIREMENTS.md).
- Logical architecture: [CAPABILITY_ARCHITECTURE.md](CAPABILITY_ARCHITECTURE.md) and [MODULE_CATALOG.md](MODULE_CATALOG.md).
- Technical architecture: [TECHNICAL_ARCHITECTURE.md](TECHNICAL_ARCHITECTURE.md) and supporting architecture documents.
- Product engineering workflow: [WORKFLOW.md](WORKFLOW.md).
- Versioning: [VERSIONING.md](VERSIONING.md).
- Compatibility/migration: [COMPATIBILITY_MIGRATION.md](COMPATIBILITY_MIGRATION.md).
- Release process: [RELEASE_PROCESS.md](RELEASE_PROCESS.md).
- Unreleased/release change record: [CHANGELOG.md](CHANGELOG.md).
- Approved product-specific extensions or deviations: documented in this repository with scope, rationale, compatibility impact, and authorization.

## Completed Foundation

### Phase 1 — Product Governance Entry Layer

Complete.

### Phase 2 — Architecture and Standards Alignment

Complete through:

- Phase 2A — Requirements Consolidation;
- Phase 2B — Capability and Module Architecture;
- Phase 2C — Technical Architecture.

The Version 1 technical blueprint remains:

- local-first modular Python monolith;
- CPython 3.14 + `uv`;
- Pydantic typed contracts and ports/adapters;
- Typer CLI first;
- SQLite + SQLAlchemy + Alembic;
- FastAPI as a later HTTP adapter;
- provider-neutral LLM port with OpenAI Responses as the first reference adapter;
- deterministic human-approval execution boundary.

### Phase 3 — Workflow and Versioning Alignment

Complete once the Phase 3 candidate is merged and verified.

Phase 3 establishes:

- controlled engineering lifecycle from intake through maintenance;
- implementation readiness and PR gates;
- compatibility classification;
- semantic versioning rules;
- database, prompt, contract, CLI/API, provider/model, integration, and configuration migration rules;
- release-candidate and immutable-tag rules;
- controlled release preparation/execution;
- rollback/recovery expectations;
- changelog discipline;
- governed PR checklist and agent operating requirements.

## Next Stage

Phase 4 — Templates, Roles, and Prompts Alignment.

Phase 4 will define the reusable product-specific templates, roles, and prompt assets that will drive the eventual implementation and operational use of Freelancer Growth OS.

Product implementation remains **Not started**. Phase 3 governs how implementation will be performed; it is not implementation itself.

## Foundation Documents

- [GOVERNANCE.md](GOVERNANCE.md)
- [AGENTS.md](AGENTS.md)
- [PRODUCT_REQUIREMENTS.md](PRODUCT_REQUIREMENTS.md)
- [CAPABILITY_ARCHITECTURE.md](CAPABILITY_ARCHITECTURE.md)
- [MODULE_CATALOG.md](MODULE_CATALOG.md)
- [TECHNICAL_ARCHITECTURE.md](TECHNICAL_ARCHITECTURE.md)
- [DATA_ARCHITECTURE.md](DATA_ARCHITECTURE.md)
- [AI_RUNTIME_ARCHITECTURE.md](AI_RUNTIME_ARCHITECTURE.md)
- [SECURITY_INTEGRATION_ARCHITECTURE.md](SECURITY_INTEGRATION_ARCHITECTURE.md)
- [DEPLOYMENT_OPERATIONS.md](DEPLOYMENT_OPERATIONS.md)
- [WORKFLOW.md](WORKFLOW.md)
- [VERSIONING.md](VERSIONING.md)
- [COMPATIBILITY_MIGRATION.md](COMPATIBILITY_MIGRATION.md)
- [RELEASE_PROCESS.md](RELEASE_PROCESS.md)
- [CHANGELOG.md](CHANGELOG.md)
- [`docs/adr/`](docs/adr/)
- [ARCHITECTURE.md](ARCHITECTURE.md)
- [ROADMAP.md](ROADMAP.md)

## Release State

This repository is currently **Unreleased**.

Requirements, architecture, workflow, versioning, changelog entries, merged PRs, or release preparation do not imply a published product release. A release requires actual releasable implementation, validation, exact release-candidate approval, and separately authorized release execution.
