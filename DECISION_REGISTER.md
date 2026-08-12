# Freelancer Growth OS Current Decision Register

**Status:** Active  
**Purpose:** Current resolution status for product and technical decisions across phases

## Authority Rule

`PRODUCT_REQUIREMENTS.md` preserves the Phase 2A decision state as it existed when requirements were approved. Later architecture/governance decisions legitimately resolved some of those open items.

This register is the current-status companion. When a Phase 2A `FGOS-ODxxx` row says `UNKNOWN` but this register says `RESOLVED`, implementation must follow the later approved decision and its cited architecture/ADR.

This register does not silently change the original product scope; it records decisions already made through governed later phases or this approved hardening package.

## Owner Product Decisions

| ID | Current status | Decision |
|---|---|---|
| `FGOS-D001` | APPROVED | Staged Hybrid: AI OS/framework first → personal application → SaaS only when justified |
| `FGOS-D002` | APPROVED | Beginner + established freelancers with adaptive maturity |
| `FGOS-D003` | APPROVED | Full Freelancer Growth Lifecycle vision; Growth Acquisition first |
| `FGOS-D004` | APPROVED | Connected but Human-Approved AI authority |

## Phase 2A Open Decisions — Current Resolution

| ID | Current status | Current decision / remaining boundary |
|---|---|---|
| `FGOS-OD001` | RESOLVED FOR V1 | Local-first application with Typer CLI as first interface; FastAPI may be added later as an HTTP adapter |
| `FGOS-OD002` | RESOLVED FOR V1 | Local persistence through SQLite behind SQLAlchemy; Alembic migrations; persistence governed by `DATA_GOVERNANCE.md` |
| `FGOS-OD003` | RESOLVED FOR LOCAL V1 / OPEN FOR REMOTE | No remote user authentication is required for single-user local V1. Remote/web/SaaS auth remains a future decision |
| `FGOS-OD004` | OPEN / NOT REQUIRED FOR V1 | Direct Upwork/Fiverr/Terrawork integration availability and scope remain unverified and are not part of the first implementation slice |
| `FGOS-OD005` | OPEN / PROPOSED | Gmail, Google Drive, LinkedIn, and other connected-source inclusion remains use-case-specific and requires explicit adoption/integration review |
| `FGOS-OD006` | RESOLVED FOR LOCAL V1 / OPEN FOR REMOTE | Local retention, deletion, export, workspace lifecycle, backup, and privacy baseline defined in `DATA_GOVERNANCE.md`; remote/SaaS policy remains future work |
| `FGOS-OD007` | RESOLVED FOR V1 | CPython 3.14 + `uv`; modular monolith; Pydantic contracts; Typer CLI; FastAPI later if justified |
| `FGOS-OD008` | RESOLVED FOR V1 | SQLite + SQLAlchemy + Alembic. No vector database in V1; PostgreSQL is a future SaaS migration target when justified |
| `FGOS-OD009` | RESOLVED FOR V1 | Provider-neutral `LLMProvider` port; OpenAI Responses API is the first reference adapter subject to `PROVIDER_DATA_POLICY.md` and evals |
| `FGOS-OD010` | RESOLVED FOR V1 | Local deployment only. Cloud/remote deployment deferred |
| `FGOS-OD011` | OPEN | Billing/subscription model remains future SaaS work |
| `FGOS-OD012` | OPEN | Product analytics model and approved business success metrics remain future Business Growth/product-operations work |
| `FGOS-OD013` | OPEN / RELEASE-CONDITIONAL | Formal accessibility target must be defined before shipping a user-facing interface for which an accessibility standard applies |
| `FGOS-OD014` | OPEN / MEASUREMENT-CONDITIONAL | Concrete runtime reliability/SLO targets must be defined after an implemented runtime can be measured and before production remote deployment |

## Hardening Decisions

### `FGOS-HD001` — Repository/runtime data separation

**Status:** Active

Real runtime user/client/business data, SQLite databases, logs, exports, backups, imported private documents, and credentials must never live inside the Git repository working tree.

### `FGOS-HD002` — Canonical contract registry

**Status:** Active

`CONTRACT_REGISTRY.md` is the canonical naming/ownership/version authority for implementation contracts. Older architecture aliases resolve through that registry.

### `FGOS-HD003` — Evidence verification authority

**Status:** Active

An LLM may recommend evidence classification but cannot deterministically promote a claim to authoritative `verified` state without qualifying evidence/provenance and application policy.

### `FGOS-HD004` — Stale-artifact execution block

**Status:** Active

Derived artifacts must identify dependencies. Material dependency changes make dependent artifacts stale/invalid until revalidated. Consequential execution rejects stale/invalid source artifacts.

### `FGOS-HD005` — Provider data minimisation

**Status:** Active

Real private/client/business evidence may reach an external provider only under `PROVIDER_DATA_POLICY.md`, with minimum necessary disclosure and no secret values.

### `FGOS-HD006` — Approval replay protection

**Status:** Active architecture requirement

Consequential approval/execution implementation must bind approval to an immutable payload fingerprint and deterministic/idempotent action identity. Material payload changes require reapproval; one approval may not be reused for an unrelated or modified action.

### `FGOS-HD007` — Public repository safety model

**Status:** Active

The GitHub repository may contain product code, public documentation, synthetic fixtures, schemas, and tests. It must not contain real runtime/private data. Repository visibility does not change this rule: even a private Git repository is not an approved runtime-data store.

### `FGOS-HD008` — Branch/check enforcement target

**Status:** Active target; GitHub setting enforcement pending manual configuration

`main` should require pull requests, required status checks, conversation resolution, and owner review before merge. Repository file-level CI is provided by `.github/workflows/governance-ci.yml`; GitHub branch/ruleset enforcement must be enabled in repository settings.

## Owner Decisions Still Needed Before Public Distribution

### Repository license

No license is currently selected. This does not block private development, but it should be resolved before inviting external reuse/contribution or presenting the repository as an open-source project.

Do not add a license merely by guessing the owner's intended commercial/open-source strategy.

### Repository visibility

The repository is currently public. Because real runtime data is prohibited from Git regardless of visibility, privacy safety does not rely on changing visibility.

The owner may still choose private visibility for product/IP strategy. Visibility is a product/business decision and should not be silently changed by an engineering agent.

## Reconciliation Rule

Whenever an implementation specification sees conflicting chronology:

1. owner-approved product decisions and current governance control scope;
2. this current decision register for later resolutions;
3. accepted architecture/ADRs;
4. historical Phase 2A open-state text for traceability only.

If genuine substantive conflict remains, stop and create an explicit decision record rather than guessing.
