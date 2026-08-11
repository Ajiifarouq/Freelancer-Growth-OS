# Freelancer Growth OS

**Status:** Unreleased  
**Maturity:** Technical Architecture Foundation  
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
- Freelancer Growth OS product-specific behavior and implementation: this repository.
- Product requirements: [PRODUCT_REQUIREMENTS.md](PRODUCT_REQUIREMENTS.md).
- Capability architecture: [CAPABILITY_ARCHITECTURE.md](CAPABILITY_ARCHITECTURE.md).
- Module catalog: [MODULE_CATALOG.md](MODULE_CATALOG.md).
- Technical architecture: [TECHNICAL_ARCHITECTURE.md](TECHNICAL_ARCHITECTURE.md).
- Approved product-specific extensions or deviations: documented in this repository with scope, rationale, compatibility impact, and authorization.

## Current Scope

Phase 1 — Product Governance Entry Layer is complete.

Phase 2A — Requirements Consolidation is complete.

Phase 2B — Capability and Module Architecture is complete.

Phase 2C — Technical Architecture establishes the implementation blueprint for Version 1:

- local-first modular Python monolith;
- CPython 3.14 + `uv`;
- Pydantic typed contracts and ports/adapters;
- Typer CLI first;
- SQLite + SQLAlchemy 2.0 + Alembic persistence/migrations;
- FastAPI as the later HTTP adapter rather than a V1 frontend requirement;
- provider-agnostic LLM port with OpenAI Responses as the first reference adapter;
- deterministic human-approval execution boundary;
- explicit security, data, research/freshness, deployment, CI, observability, backup, and migration rules.

Phase 2 — Architecture and Standards Alignment is complete once this Phase 2C baseline is merged and verified. The next adoption stage is Phase 3 — Workflow and Versioning Alignment.

Product implementation remains **Not started**. No production deployment, customer/user adoption, direct marketplace integration, or product release is implied by the architecture.

## Foundation Documents

- [GOVERNANCE.md](GOVERNANCE.md) — product governance and upstream adoption contract.
- [AGENTS.md](AGENTS.md) — operating requirements for humans and automated engineering actors.
- [PRODUCT_REQUIREMENTS.md](PRODUCT_REQUIREMENTS.md) — authoritative product requirements, approved product decisions, requirements IDs, constraints, and open-decision history.
- [CAPABILITY_ARCHITECTURE.md](CAPABILITY_ARCHITECTURE.md) — stable capability boundaries, logical contracts, dependency direction, authority boundaries, and validation ownership.
- [MODULE_CATALOG.md](MODULE_CATALOG.md) — stable initial module IDs, responsibilities, inputs, outputs, dependencies, and validation expectations.
- [TECHNICAL_ARCHITECTURE.md](TECHNICAL_ARCHITECTURE.md) — V1 runtime topology, technology decisions, interfaces, persistence, testing, CI, observability, and migration strategy.
- [DATA_ARCHITECTURE.md](DATA_ARCHITECTURE.md) — V1 persistence/data ownership and future PostgreSQL migration path.
- [AI_RUNTIME_ARCHITECTURE.md](AI_RUNTIME_ARCHITECTURE.md) — LLM/provider, prompt, structured-output, freshness, tool, and eval boundaries.
- [SECURITY_INTEGRATION_ARCHITECTURE.md](SECURITY_INTEGRATION_ARCHITECTURE.md) — trust zones, connector permissions, secret handling, prompt-injection controls, and approval/execution architecture.
- [DEPLOYMENT_OPERATIONS.md](DEPLOYMENT_OPERATIONS.md) — local runtime, environments, CI, logging, backups, upgrades, and future deployment gates.
- [`docs/adr/`](docs/adr/) — accepted architecture decision records.
- [ARCHITECTURE.md](ARCHITECTURE.md) — architecture authority and maturity summary.
- [ROADMAP.md](ROADMAP.md) — controlled adoption and product-engineering roadmap.

## Release State

This repository is currently **Unreleased**. Requirements approval, architecture definition, technical selections, file existence, branch state, pull-request state, or technical planning does not imply a product release or implemented product capability.
