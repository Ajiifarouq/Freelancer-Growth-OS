# Freelancer Growth OS

**Status:** Unreleased  
**Maturity:** Capability Architecture Foundation  
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
- Approved product-specific extensions or deviations: documented in this repository with scope, rationale, compatibility impact, and authorization.

## Current Scope

Phase 1 — Product Governance Entry Layer is complete.

Phase 2A — Requirements Consolidation is complete.

Phase 2B — Capability and Module Architecture establishes the logical product blueprint: eight stable capability boundaries, seventeen initial module IDs, shared logical data contracts, dependency direction, validation ownership, freshness/evidence controls, and the human-approval boundary for consequential connected actions.

The next architecture substage is Phase 2C — Technical Architecture, where implementation topology and technology choices may be derived from the approved requirements and logical module boundaries.

No programming language, framework, database, cloud provider, LLM provider, authentication provider, deployment topology, or direct marketplace integration is implied by Phase 2B.

## Foundation Documents

- [GOVERNANCE.md](GOVERNANCE.md) — product governance and upstream adoption contract.
- [AGENTS.md](AGENTS.md) — operating requirements for humans and automated engineering actors.
- [PRODUCT_REQUIREMENTS.md](PRODUCT_REQUIREMENTS.md) — authoritative product requirements, approved product decisions, requirements IDs, constraints, and open decisions.
- [CAPABILITY_ARCHITECTURE.md](CAPABILITY_ARCHITECTURE.md) — stable capability boundaries, logical contracts, dependency direction, authority boundaries, and validation ownership.
- [MODULE_CATALOG.md](MODULE_CATALOG.md) — stable initial module IDs, responsibilities, inputs, outputs, dependencies, and validation expectations.
- [ARCHITECTURE.md](ARCHITECTURE.md) — product architecture boundary and current architecture status.
- [ROADMAP.md](ROADMAP.md) — controlled adoption and product-engineering roadmap.

## Release State

This repository is currently **Unreleased**. Requirements approval, architecture definition, file existence, branch state, pull-request state, or technical planning does not imply a product release or implemented product capability.
