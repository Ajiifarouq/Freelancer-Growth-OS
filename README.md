# Freelancer Growth OS

**Status:** Unreleased  
**Maturity:** Governed AI Asset Foundation  
**Repository:** `Ajiifarouq/Freelancer-Growth-OS`

## Purpose

Freelancer Growth OS is the product repository for product-specific requirements, behavior, workflows, modules, prompts, roles, templates, interfaces, data models, implementation choices, and roadmap decisions associated with Freelancer Growth OS.

Shared engineering governance is adopted from the pinned GrowthOS Engineering baseline; product-specific behavior and assets remain in this repository.

## Governance Dependency

- **Upstream repository:** `Ajiifarouq/GrowthOS-Engineering`
- **Released baseline:** `v0.1.0`
- **Pinned commit:** `7ee056f938e12b5a72d1ee919a27f05ec5297c69`

A floating upstream `main` reference must not be used as the governing baseline.

## Source of Truth

- Shared engineering governance: GrowthOS Engineering `v0.1.0` at `7ee056f938e12b5a72d1ee919a27f05ec5297c69`.
- Product requirements: [PRODUCT_REQUIREMENTS.md](PRODUCT_REQUIREMENTS.md).
- Logical architecture: [CAPABILITY_ARCHITECTURE.md](CAPABILITY_ARCHITECTURE.md) and [MODULE_CATALOG.md](MODULE_CATALOG.md).
- Technical architecture: [TECHNICAL_ARCHITECTURE.md](TECHNICAL_ARCHITECTURE.md) and supporting architecture documents.
- Engineering workflow: [WORKFLOW.md](WORKFLOW.md).
- Versioning: [VERSIONING.md](VERSIONING.md).
- Compatibility/migration: [COMPATIBILITY_MIGRATION.md](COMPATIBILITY_MIGRATION.md).
- Release process: [RELEASE_PROCESS.md](RELEASE_PROCESS.md).
- Product templates: [TEMPLATE_LIBRARY.md](TEMPLATE_LIBRARY.md).
- Product roles: [ROLE_LIBRARY.md](ROLE_LIBRARY.md).
- Prompt governance: [PROMPT_GOVERNANCE.md](PROMPT_GOVERNANCE.md).
- Product prompt assets: [PROMPT_LIBRARY.md](PROMPT_LIBRARY.md).
- Change record: [CHANGELOG.md](CHANGELOG.md).

## Completed Foundation

### Phase 1 — Product Governance Entry Layer

Complete.

### Phase 2 — Architecture and Standards Alignment

Complete through Phase 2A requirements, Phase 2B capability/module architecture, and Phase 2C technical architecture.

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

Complete.

Phase 3 established controlled engineering lifecycle, compatibility/migration rules, SemVer, prompt/contract/database versioning, release-candidate discipline, immutable release tags, release execution gates, changelog discipline, and PR/agent controls.

### Phase 4 — Templates, Roles, and Prompts Alignment

Complete once the Phase 4 candidate is merged and verified.

Phase 4 establishes:

- [TEMPLATE_LIBRARY.md](TEMPLATE_LIBRARY.md) with reusable product, evidence, workflow, validation, approval, execution, prompt-change, and release templates;
- [ROLE_LIBRARY.md](ROLE_LIBRARY.md) with explicit AI/human responsibility and authority boundaries;
- [PROMPT_GOVERNANCE.md](PROMPT_GOVERNANCE.md) with prompt hierarchy, metadata, versioning, factuality, freshness, prompt-injection, structured-output, eval, compatibility, and human-approval rules;
- [PROMPT_LIBRARY.md](PROMPT_LIBRARY.md) with 15 initial governed prompt assets mapped to Growth Acquisition and assurance modules.

Prompts for later `client-success` and `business-growth` capabilities remain intentionally deferred until their detailed module requirements are mature enough to avoid fabrication.

## Next Stage

Phase 5 — Existing Product Content Conformance.

Phase 5 will inventory and review existing product content/assets against the governance, requirements, architecture, workflow, versioning, templates, roles, prompt, security, privacy, factuality, and approval baselines.

Product implementation remains **Not started**. Phase 4 defines reusable AI assets and their governance; it does not claim deployed agents or implemented product modules.

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
- [TEMPLATE_LIBRARY.md](TEMPLATE_LIBRARY.md)
- [ROLE_LIBRARY.md](ROLE_LIBRARY.md)
- [PROMPT_GOVERNANCE.md](PROMPT_GOVERNANCE.md)
- [PROMPT_LIBRARY.md](PROMPT_LIBRARY.md)
- [CHANGELOG.md](CHANGELOG.md)
- [`docs/adr/`](docs/adr/)
- [ARCHITECTURE.md](ARCHITECTURE.md)
- [ROADMAP.md](ROADMAP.md)

## Release State

This repository is currently **Unreleased**.

Requirements, architecture, workflow, templates, roles, prompt assets, merged PRs, or release preparation do not imply a published product release. A release requires actual releasable implementation, validation, exact release-candidate approval, and separately authorized release execution.
