# Freelancer Growth OS Technical Architecture

**Status:** Active architecture baseline  
**Architecture phase:** Phase 2C — Technical Architecture  
**Product release status:** Unreleased  
**Requirements:** [PRODUCT_REQUIREMENTS.md](PRODUCT_REQUIREMENTS.md)  
**Logical architecture:** [CAPABILITY_ARCHITECTURE.md](CAPABILITY_ARCHITECTURE.md)  
**Modules:** [MODULE_CATALOG.md](MODULE_CATALOG.md)  
**Governance baseline:** `Ajiifarouq/GrowthOS-Engineering` `v0.1.0` at `7ee056f938e12b5a72d1ee919a27f05ec5297c69`

## 1. Executive Decision

Version 1 will be a **local-first modular monolith** implemented as a Python application package with a command-line interface. Business modules run in one process and communicate through typed application contracts rather than network calls.

The design deliberately separates domain/application logic from interfaces and infrastructure so the same core can later be exposed through an HTTP API and web application without rewriting the product rules.

### Selected V1 stack

- **Runtime:** CPython 3.14.
- **Project/dependency management:** `uv` with `pyproject.toml` and committed `uv.lock`.
- **Typed contracts and validation:** Pydantic v2.
- **CLI:** Typer.
- **Persistence:** SQLite for the local-first product.
- **Persistence abstraction:** SQLAlchemy 2.0 stable line.
- **Schema migrations:** Alembic.
- **Future HTTP adapter:** FastAPI; not required for the first CLI-only milestone.
- **Testing:** pytest.
- **Formatting/linting:** Ruff.
- **Static type checking:** mypy or an equivalent strict type checker; exact configuration belongs to implementation standards.
- **LLM architecture:** provider port with an OpenAI Responses API reference adapter first; model selection remains configuration rather than a domain dependency.
- **CI:** GitHub Actions when implementation begins.
- **Initial deployment:** local execution; no public production service in V1.

No frontend framework, cloud provider, authentication vendor, vector database, or production SaaS platform is selected in this phase.

## 2. Why Local-First

The approved product form is staged hybrid: AI framework/OS first, personal application later, multi-user SaaS only when justified.

A local-first modular monolith gives V1:

- the smallest operational surface;
- no premature account/authentication system;
- no public network service by default;
- simple private-data ownership;
- inexpensive development and testing;
- direct access to filesystem-based evidence when authorised;
- one codebase that can later serve CLI and HTTP interfaces.

Local-first does **not** mean disposable. Stable contracts, persistence migrations, ports/adapters, audit records, and workspace identifiers are defined from the start so later migration remains controlled.

## 3. Runtime Topology

```text
User
  |
  v
CLI Interface (Typer)
  |
  v
Application Orchestrator / Use Cases
  |
  +--> Freelancer Intelligence Modules
  +--> Positioning & Branding Modules
  +--> Opportunity Intelligence Modules
  +--> Conversion Modules
  |
  +--> Evidence / Freshness Assurance Plane
  |
  +--> Human Approval Gate
  |
  +--> Ports ---------------------------------------------+
        |                                                  |
        +--> Persistence Port --> SQLite Adapter           |
        +--> LLM Port ---------> OpenAI reference adapter  |
        +--> Research Port ----> current-source adapter    |
        +--> Connected Read ---> future connector adapters |
        +--> Action Executor --> future write adapters     |
```

### Later topology

When a personal web application is justified:

```text
Web UI
  |
FastAPI HTTP Adapter
  |
Same Application Core
```

A later SaaS may replace SQLite with PostgreSQL, add identity/tenant enforcement, and horizontally scale runtime components while preserving application contracts.

## 4. Source Layout Target

```text
src/freelancer_growth_os/
  domain/
    contracts/
    enums/
    errors/
    policies/
  application/
    workflows/
    services/
    ports/
  modules/
    evidence_intake/
    maturity_assessor/
    professional_positioning/
    marketplace_profile_assessor/
    marketplace_profile_optimizer/
    service_offer_positioner/
    portfolio_positioner/
    cross_asset_consistency/
    opportunity_evaluator/
    proposal_assistant/
    pricing_advisor/
    negotiation_preparer/
    client_conversion/
    evidence_traceability/
    freshness_escalator/
    connected_context/
    human_approval/
  adapters/
    persistence/
      sqlite/
    llm/
      openai/
    research/
    connectors/
    execution/
  interfaces/
    cli/
    api/
  config/
  telemetry/

tests/
  unit/
  contract/
  integration/
  evals/
  migration/

docs/adr/
```

The exact package names may be refined during implementation, but dependency direction must remain equivalent.

## 5. Dependency Rules

Allowed direction:

`interfaces → application → domain`

`adapters → application ports/domain contracts`

`modules → domain/application contracts`

Prohibited:

- domain code importing FastAPI, Typer, SQLite, SQLAlchemy, OpenAI SDK, or connector SDKs;
- business modules reading environment variables directly;
- product modules receiving raw credentials;
- direct module-to-module mutation of hidden shared state;
- LLM provider objects becoming domain models.

Cross-module communication must use typed contracts or application-service calls.

## 6. Application Workflow Pattern

A product operation follows:

1. Interface receives user intent/input.
2. Pydantic contract validates input.
3. Application workflow loads required evidence/artifacts.
4. Evidence/freshness policy determines whether current verification is required.
5. Relevant business module executes.
6. LLM output, when used, is parsed into a strict typed contract.
7. Assurance checks factuality, provenance, consistency, and uncertainty.
8. Result is persisted as an immutable/versioned artifact where required.
9. If an external consequential action is proposed, create an approval request.
10. Only an approved request may reach an execution adapter.
11. Execution outcome is recorded separately from the generated draft.

## 7. Contract Representation

Logical contracts from Phase 2B become Pydantic models with:

- stable contract ID;
- schema version;
- typed fields;
- validation rules;
- evidence/provenance references where applicable;
- explicit unknown/uncertain state where needed;
- timestamps as UTC-aware values;
- opaque identifiers generated outside business logic.

Examples:

- `EvidenceBundle`
- `FreelancerContext`
- `MaturityAssessment`
- `PositioningBrief`
- `OpportunityAssessment`
- `ProposalDraft`
- `PricingBrief`
- `ApprovalRequest`
- `ApprovalDecisionRecord`
- `ExecutionResult`

JSON is the external serialisation format for contracts. Python objects are the in-process representation.

## 8. Persistence Strategy

V1 uses SQLite through SQLAlchemy rather than embedding SQLite-specific queries throughout business code.

Persistence is divided into repositories/ports such as:

- `EvidenceRepository`
- `ArtifactRepository`
- `RunRepository`
- `ApprovalRepository`
- `AuditRepository`
- `ConnectorMetadataRepository`

Alembic owns schema migration history from the first implementation migration.

The database design is specified in [DATA_ARCHITECTURE.md](DATA_ARCHITECTURE.md).

## 9. API Strategy

The CLI is the first required interface.

FastAPI is selected as the later HTTP adapter because the architecture already uses Python type models and needs schema-driven JSON APIs. HTTP endpoints must call application workflows rather than business modules or database tables directly.

No public API is required for the first implementation milestone.

If the API adapter is started locally before authentication exists:

- bind to loopback only by default;
- do not expose it to a LAN/WAN/public network;
- do not treat hidden API documentation as a security control.

## 10. AI Runtime Strategy

LLMs are infrastructure collaborators, not the source of product authority.

The domain interacts through an `LLMProvider` port. The first provider adapter uses OpenAI's Responses API, but:

- provider/model IDs are configuration;
- prompts are versioned product assets;
- structured outputs are validated against Pydantic contracts;
- business rules and approval state machines remain deterministic application code;
- tests use fake/deterministic provider adapters where possible;
- the architecture must allow a different provider without changing domain contracts.

See [AI_RUNTIME_ARCHITECTURE.md](AI_RUNTIME_ARCHITECTURE.md).

## 11. Current Research / Freshness Strategy

`freshness-escalator` produces a `FreshnessRequirement` when stale information could materially affect output.

The application then calls a `CurrentResearchPort`. The initial implementation may use provider-supported web/search tooling where available, but the research port remains independent of the business modules.

A failed or unavailable current-source lookup returns an explicit unverified state. It must never silently fall back to stale memory and present it as current fact.

## 12. Connected-Service Strategy

Connected services use two separate ports:

- `ConnectedContextProvider` for read-only authorised retrieval;
- `ActionExecutor` for consequential writes/actions.

A read connector cannot automatically be used as a write connector.

Execution adapters require an approved `ApprovalDecisionRecord` matching the exact action scope.

No Upwork, Fiverr, Terrawork, Gmail, Drive, LinkedIn, or other external adapter is claimed as implemented by this architecture.

See [SECURITY_INTEGRATION_ARCHITECTURE.md](SECURITY_INTEGRATION_ARCHITECTURE.md).

## 13. Authentication and Identity

### V1 local product

- single local operator/workspace;
- no product login screen;
- operating-system account/filesystem boundary provides the local machine boundary;
- records still carry a stable `workspace_id` so future multi-workspace migration does not require rewriting every data model.

### Personal web application

Remote/network exposure requires a real identity and session boundary before release. Authentication technology/vendor remains a later implementation decision because no remote application is being deployed in V1.

### Future SaaS

SaaS requires:

- authenticated user identity;
- workspace/tenant membership;
- server-side authorisation on every resource;
- per-tenant data isolation;
- auditability;
- PostgreSQL or another server database suitable for multi-user concurrency;
- optional database row-level controls as defence in depth.

## 14. Secret Handling

V1 secrets such as an LLM API key are injected at runtime and are never stored in the product database or committed to Git.

Rules:

- environment injection is acceptable for local development;
- `.env` files, if used locally, must be ignored and never committed;
- logs must redact sensitive headers/tokens;
- product/domain contracts must never contain raw credentials;
- deployed environments later use platform secret-management or short-lived identity mechanisms;
- connector tokens belong behind integration adapters, not in business modules.

## 15. Observability and Audit

V1 uses structured application logging plus persisted audit/run records.

Each run should have:

- `run_id`;
- workspace;
- workflow/module IDs;
- status;
- start/end timestamps;
- input/output artifact references rather than unnecessary raw content;
- provider/model metadata where an LLM is used;
- token/usage metadata when available;
- error category;
- freshness/validation status.

Consequential actions additionally record:

- approval request;
- approval decision;
- executor attempt;
- verified success/failure/unknown state.

Do not log hidden chain-of-thought or unnecessary sensitive evidence.

## 16. Reliability and Recovery

For V1:

- SQLite database and user-owned evidence files are local assets;
- schema migrations must be reversible where practical and tested;
- the application must fail closed on malformed contracts and approval mismatch;
- external calls use bounded retry only for retry-safe/transient failures;
- no automatic retry of consequential external actions after an ambiguous outcome without reconciliation;
- local backup/export procedure is required before calling V1 releasable;
- migration tests must prove a fresh database can reach current schema head.

No uptime SLA is declared for the local-first V1.

## 17. Testing Architecture

Required categories:

### Unit tests

Deterministic rules, state machines, validators, business calculations, evidence policy.

### Contract tests

Pydantic schema compatibility, provider adapters, persistence ports, connector/executor adapters.

### Integration tests

SQLite transactions, migrations, workflow orchestration, LLM-adapter parsing using mocks/fakes.

### AI evals

Representative cases for:

- hallucination/factuality;
- maturity classification;
- positioning quality;
- opportunity-fit reasoning;
- proposal evidence use;
- pricing assumption disclosure;
- prompt-injection resistance;
- approval-boundary preservation;
- current-information escalation.

AI quality changes must be evaluated; a syntactically valid response is not enough.

## 18. CI Strategy

When code implementation begins, GitHub Actions should run on pull requests and protected branch updates:

1. dependency lock verification;
2. formatting check;
3. linting;
4. static typing;
5. unit tests;
6. integration/migration tests that do not require secrets;
7. architecture/contract checks where automated;
8. secret-free test environment by default.

Tests that require paid/external providers should be separate explicit jobs or controlled eval runs, not a hidden requirement for every unit-test execution.

## 19. Environments

### `dev`

Developer local environment; synthetic or intentionally supplied test data.

### `test`

Automated isolated SQLite databases and fake external adapters.

### `local`

User-operated V1 with real local workspace/evidence and explicitly configured provider credentials.

### Future `staging` / `production`

Not created until remote deployment is approved. Those environments require explicit identity, database, secret-management, backup, monitoring, and deployment decisions.

## 20. Technology Decision Register

| Decision | Result | ADR |
|---|---|---|
| V1 application topology | Local-first modular monolith | `ADR-0001` |
| Runtime/tooling | CPython 3.14 + uv | `ADR-0002` |
| Contracts/dependency architecture | Pydantic + ports/adapters | `ADR-0003` |
| Persistence | SQLite + SQLAlchemy 2.0 + Alembic; PostgreSQL migration path | `ADR-0004` |
| Interface | Typer CLI first; FastAPI HTTP adapter later | `ADR-0005` |
| LLM | Provider port; OpenAI Responses reference adapter first | `ADR-0006` |
| Consequential actions | Explicit approval/execution boundary | `ADR-0007` |
| CI/ops/secrets | GitHub Actions + structured audit + runtime secrets | `ADR-0008` |

## 21. Resolved Phase 2A Open Decisions

Phase 2C resolves or narrows the earlier open decisions as follows:

- `FGOS-OD001` — RESOLVED: CLI/local application is first interface; FastAPI adapter is the next interface boundary.
- `FGOS-OD002` — RESOLVED for V1: local relational persistence for product artifacts, evidence metadata, runs, approvals, and audits.
- `FGOS-OD003` — RESOLVED for V1: no product authentication because no remote service; remote auth remains future-required.
- `FGOS-OD004` — NARROWED: direct marketplace integration not assumed; adapter architecture defined, platform verification still required per integration.
- `FGOS-OD005` — NARROWED: connected-source architecture defined; individual services remain separate product/integration approvals.
- `FGOS-OD006` — PARTIAL: local export/delete/backup requirements established; detailed remote retention policy remains future work.
- `FGOS-OD007` — RESOLVED: Python 3.14 modular application architecture.
- `FGOS-OD008` — RESOLVED for V1: SQLite; no vector DB. PostgreSQL is the intended SaaS migration target when justified.
- `FGOS-OD009` — RESOLVED at architecture level: provider abstraction with OpenAI Responses reference adapter; model remains configuration.
- `FGOS-OD010` — RESOLVED for V1: local execution; no cloud host selected.
- `FGOS-OD011` — DEFERRED: SaaS billing remains future product decision.
- `FGOS-OD012` — DEFERRED: product/business analytics metrics remain later scope.
- `FGOS-OD013` — DEFERRED until a user-facing application UI exists; accessibility remains mandatory design concern.
- `FGOS-OD014` — PARTIAL: local reliability/recovery rules defined; service-level targets remain future deployment work.

## 22. Phase 2C Exit Criteria

Phase 2C is complete when the technical architecture, supporting domain-specific architecture documents, ADRs, and repository status updates are merged to `main` and verification confirms:

- V1 topology is unambiguous;
- technology selections have rationale and migration paths;
- logical modules remain technology-independent at the domain boundary;
- data ownership and persistence are defined;
- LLM/provider responsibilities are separated from deterministic authority;
- freshness and connected-service ports are defined;
- consequential action approval remains enforceable;
- secrets and sensitive data have explicit boundaries;
- deployment/environment strategy is defined without false production claims;
- CI/test/observability expectations are defined;
- no direct external integration is falsely claimed;
- product implementation status remains not started;
- product release status remains Unreleased.

After Phase 2C, Phase 2 — Architecture and Standards Alignment is complete. The repository may then advance to Phase 3 — Workflow and Versioning Alignment before product implementation/release work proceeds through the broader governed adoption roadmap.
