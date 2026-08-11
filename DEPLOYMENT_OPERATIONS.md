# Freelancer Growth OS Deployment and Operations Architecture

**Status:** Active architecture baseline  
**Phase:** Phase 2C — Technical Architecture  
**Implementation status:** Not started

## Purpose

Define how Freelancer Growth OS is developed, tested, run locally, observed, backed up, and later promoted toward remote deployment without pretending a production service already exists.

## V1 Deployment Decision

Version 1 is a **local application**, not a hosted SaaS service.

The supported operational shape is:

```text
User machine
  ├─ Python 3.14 runtime
  ├─ uv-managed environment
  ├─ Freelancer Growth OS CLI
  ├─ local SQLite database
  ├─ local evidence/application-data directory
  └─ runtime-injected provider credentials
```

No cloud provider, DNS, public API, load balancer, Kubernetes cluster, or managed database is required for V1.

## Project Reproducibility

Implementation should use:

- `pyproject.toml` for project metadata/dependencies;
- `uv.lock` committed to Git;
- explicit Python compatibility range anchored on Python 3.14 for V1;
- isolated `.venv` managed by uv;
- deterministic test dependencies through dependency groups;
- migration history committed with code.

The lockfile is part of reproducible development but not a substitute for dependency/security review.

## Local Data Directory

The implementation must define one documented application-data root containing:

- SQLite database;
- application-managed evidence copies, if any;
- exports/backups;
- safe operational metadata.

The exact OS-specific path is an implementation detail. The repository itself must not be used as the normal runtime data directory.

## Configuration

Configuration separates non-secret settings from secrets.

### Non-secret examples

- database path;
- data directory;
- log level;
- default workspace ID/name;
- LLM provider/model selection;
- feature flags;
- local API bind address if enabled.

### Secret examples

- AI provider API key;
- future connector OAuth/token secrets;
- future deployment credentials.

Secrets are runtime-injected and excluded from persistent product configuration.

## Local Startup Expectations

Implementation should provide a small number of operator commands, for example conceptually:

- initialise workspace/database;
- validate configuration;
- run a module/workflow;
- inspect status;
- create backup/export;
- restore/verify backup;
- apply/check migrations;
- optionally run local HTTP adapter later.

Exact command syntax is an implementation detail owned by the Typer CLI.

## CI Architecture

GitHub Actions is selected for repository CI when implementation begins.

### Required PR checks

- repository/lockfile consistency;
- Ruff format check;
- Ruff lint;
- static type check;
- pytest unit tests;
- integration tests using temporary SQLite;
- Alembic migration-to-head test;
- contract/schema tests;
- architecture invariant tests where practical;
- secret scanning or equivalent credential detection.

### AI/external eval jobs

Provider-backed evals must be separated from ordinary deterministic CI because they may:

- require secrets;
- incur cost;
- be slower or rate-limited;
- vary probabilistically.

A pull request should be able to run the deterministic core test suite without any external API key.

## CI Permissions

Workflow permissions should be least privilege.

Default build/test jobs need read-only repository contents unless a specific governed action requires more.

Deployment/publication workflows, if introduced later, are separate protected workflows with explicit permissions and approval gates.

## Secrets in CI

- deterministic tests should require no production secrets;
- external-eval keys, if later configured, use GitHub/environment secrets or another approved secret mechanism;
- deployment should prefer short-lived workload identity/OIDC when the chosen cloud supports it;
- secrets must not be echoed to logs;
- pull requests from untrusted contexts must not receive sensitive secrets automatically.

## Logging

V1 uses structured logs to stdout/stderr and/or an application log file in the local data area.

Recommended fields:

- timestamp;
- severity;
- `run_id`;
- module/workflow ID;
- event type;
- safe status/error code;
- duration;
- provider/model metadata where relevant;
- no raw secret value.

Logs should be useful without requiring storage of full user evidence.

## Audit Records

Governance/security-relevant events are persisted separately from ordinary logs where required, including:

- approval requested;
- approval granted/rejected;
- execution attempted;
- execution result;
- connector binding/revocation;
- migration applied;
- important evidence supersession;
- export/delete operation.

## Metrics

V1 does not require an external metrics platform.

Useful local operational counters may include:

- workflow success/failure counts;
- provider call failures;
- latency summaries;
- token usage/cost metadata where available;
- validation failure counts;
- freshness-verification failures;
- approval/execution outcomes.

Business success metrics remain a separate future product decision and must not be invented from operational telemetry.

## Error Handling

Errors should be classified into stable categories rather than exposing raw stack traces as normal user output.

Examples:

- invalid input;
- missing evidence;
- configuration failure;
- persistence failure;
- provider failure;
- current-source unavailable;
- permission denied;
- approval required;
- approval mismatch;
- execution ambiguous;
- internal error.

Debug traces may be available locally for development but must avoid sensitive content.

## Backup

Before V1 release, document and test:

- database backup;
- application-managed evidence backup where applicable;
- export format;
- backup integrity check;
- restore into a clean environment;
- migration of restored database to current schema;
- secure deletion expectations for old backups.

Backups are sensitive user data.

## Upgrade Procedure

A normal local upgrade should conceptually:

1. verify application version compatibility;
2. create/recommend backup before breaking migration;
3. sync locked dependencies;
4. run Alembic migrations;
5. validate schema head;
6. run application health/config check;
7. preserve user artifacts/evidence IDs.

Breaking migrations require an explicit migration note and rollback/recovery plan.

## Release Packaging

Phase 2C does not choose the final distribution mechanism.

Possible future packaging approaches include:

- Python package/CLI installation;
- self-contained executable packaging;
- local container for advanced users;
- desktop wrapper;
- hosted personal web app.

The first implementation should prioritise a reproducible Python CLI/package. Packaging complexity should be added only when user-distribution requirements justify it.

## Future Personal Web App

When approved, add:

```text
Browser
  |
Web UI
  |
FastAPI
  |
Existing application core
  |
Persistence / AI / connector adapters
```

Before exposing FastAPI remotely, define and implement:

- authentication/session management;
- CSRF/origin strategy as applicable;
- HTTPS termination;
- remote secret management;
- server database strategy if multi-device/concurrent use is required;
- backups;
- production logging/monitoring;
- rate/resource controls.

## Future SaaS Deployment

SaaS architecture is intentionally deferred. Expected changes include:

- PostgreSQL instead of local SQLite;
- authenticated users and workspace membership;
- tenant isolation;
- object storage for files;
- managed secret storage;
- deployment environments;
- background job processing only if measured workloads require it;
- central observability;
- formal backup/recovery objectives;
- release/deployment automation.

Do not introduce Kubernetes, microservices, queues, Redis, or other distributed infrastructure merely because they are common SaaS tools. Each must be justified by real requirements/load.

## Phase 2C Operational Exit Criteria

Architecture is sufficient to enter implementation planning when:

- local V1 runtime is unambiguous;
- configuration/secrets boundary is explicit;
- CI checks are specified;
- deterministic tests require no provider secrets;
- backup/restore expectations exist;
- logging/audit distinction exists;
- future remote deployment has entry gates;
- no cloud/production state is falsely claimed.
