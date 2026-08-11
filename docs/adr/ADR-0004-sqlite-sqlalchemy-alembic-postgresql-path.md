# ADR-0004 — SQLite + SQLAlchemy + Alembic with PostgreSQL Migration Path

**Status:** Accepted  
**Date:** 2026-08-11

## Decision

Use SQLite for V1 persistence, SQLAlchemy 2.0 stable line as the persistence abstraction, and Alembic for schema migrations. Treat PostgreSQL as the intended server-database migration target if multi-user SaaS requirements become real.

## Drivers

- V1 is single-user/local and does not require a database server.
- SQLite is self-contained/serverless/zero-configuration and transactional.
- SQLAlchemy supports both SQLite and PostgreSQL while keeping database-specific behavior behind adapters.
- Migration history is required from the first schema.

## Alternatives

- PostgreSQL from day one: rejected as unnecessary operational complexity for local V1.
- JSON/files only: rejected because approvals, audit, provenance, relationships, and migrations require structured transactional persistence.
- Vector database as primary storage: rejected because semantic-retrieval scale has not been demonstrated.

## Consequences

- SQLite transaction behavior must be configured/tested explicitly.
- SQLite-only SQL/quirks stay inside the adapter.
- All workspace-owned records carry `workspace_id` even in single-user V1.
- No vector database is introduced without a later evidence-backed ADR.
- A future PostgreSQL migration requires cross-database integration and tenant-isolation tests.
