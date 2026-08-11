# Freelancer Growth OS Architecture

## Purpose

This document defines the product architecture authority and records the current architecture maturity without confusing architecture decisions with implemented software.

## Shared Governance Baseline

Product architecture work is governed by:

- `Ajiifarouq/GrowthOS-Engineering`
- tag `v0.1.0`
- commit `7ee056f938e12b5a72d1ee919a27f05ec5297c69`

The shared dependency direction is:

`Freelancer Growth OS → GrowthOS Engineering`

## Product Responsibility

This repository owns product-specific:

- requirements;
- domain behavior;
- product workflows;
- modules and interfaces;
- data models;
- deployment and runtime decisions;
- product-specific prompts and roles;
- integrations;
- product roadmap.

Listing these responsibility categories does not assert that particular implementations already exist.

## Requirements Baseline

[PRODUCT_REQUIREMENTS.md](PRODUCT_REQUIREMENTS.md) defines the approved requirements inputs for product architecture.

Architecture decisions must trace back to verified requirements, approved product decisions, constraints, or explicitly unresolved decisions. Architecture must not manufacture requirements merely to justify a preferred technology.

## Logical Architecture Baseline

[CAPABILITY_ARCHITECTURE.md](CAPABILITY_ARCHITECTURE.md) defines stable product capabilities, logical data contracts, dependency direction, AI/human authority boundaries, knowledge/freshness responsibilities, security/privacy boundaries, and validation ownership.

[MODULE_CATALOG.md](MODULE_CATALOG.md) defines the initial stable module IDs and their logical responsibilities, inputs, outputs, dependencies, non-goals, and validation expectations.

## Technical Architecture Baseline

[TECHNICAL_ARCHITECTURE.md](TECHNICAL_ARCHITECTURE.md) is the primary technical architecture.

Supporting technical architecture:

- [DATA_ARCHITECTURE.md](DATA_ARCHITECTURE.md);
- [AI_RUNTIME_ARCHITECTURE.md](AI_RUNTIME_ARCHITECTURE.md);
- [SECURITY_INTEGRATION_ARCHITECTURE.md](SECURITY_INTEGRATION_ARCHITECTURE.md);
- [DEPLOYMENT_OPERATIONS.md](DEPLOYMENT_OPERATIONS.md);
- accepted records under [`docs/adr/`](docs/adr/).

These documents define approved technical choices and migration paths, not deployed software.

## Shared Responsibility Boundary

GrowthOS Engineering owns reusable engineering governance. Freelancer Growth OS must not redefine shared governance merely to make product implementation easier.

Product-specific extensions may be introduced only under [GOVERNANCE.md](GOVERNANCE.md).

## Architectural Invariants

- Shared governance remains external and pinned to an immutable released baseline.
- Product-specific behavior stays in this repository.
- Protected human approval boundaries are not implicitly delegated to automation.
- Repository and release state remain traceable.
- Security, privacy, factuality, and compatibility requirements cannot be bypassed for implementation convenience.
- Architecture claims require requirements or implementation evidence.
- The staged-hybrid product form must not be used to introduce SaaS complexity before requirements support it.
- Consequential connected actions preserve the human-approval authority model.
- Evidence/factuality/freshness controls remain shared foundations rather than hidden business-decision owners.
- Connected-source access remains a controlled boundary rather than direct unrestricted module access.
- Downstream feedback re-enters through explicit evidence ingestion rather than silently mutating upstream truth.
- Domain/application code remains independent of provider, database, CLI, HTTP, and connector SDK implementations.

## Current Architecture Status

**Status:** Requirements, logical architecture, and technical architecture established. Product implementation not started.

### Phase 2A — Requirements Consolidation

Established product requirements, approved product decisions, user/maturity model, capability scope, functional/non-functional requirements, security/privacy requirements, non-goals, and decision register.

### Phase 2B — Capability and Module Architecture

Established eight capability boundaries, seventeen initial module IDs, logical contracts, dependencies, cycle controls, validation ownership, and human/AI authority boundaries.

### Phase 2C — Technical Architecture

Established:

- local-first modular-monolith V1 topology;
- CPython 3.14 + `uv` runtime/project strategy;
- Pydantic v2 contracts with ports/adapters;
- Typer CLI first interface;
- FastAPI as later HTTP adapter;
- SQLite + SQLAlchemy 2.0 + Alembic persistence/migrations;
- PostgreSQL migration target for justified future multi-user SaaS;
- provider-agnostic LLM port with OpenAI Responses reference adapter;
- no vector database for V1;
- current-research/freshness port;
- read/write connector separation;
- deterministic human-approval execution state machine;
- secret isolation and prompt-injection controls;
- local deployment/environment strategy;
- GitHub Actions CI strategy for implementation;
- structured logging/audit/backup/recovery expectations;
- architecture decision records for material choices.

## Phase 2 Disposition

Phase 2 — Architecture and Standards Alignment is complete after the Phase 2C change is merged and verified.

The next governed stage is **Phase 3 — Workflow and Versioning Alignment**.

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
- a product release.

The repository remains **Unreleased**.
