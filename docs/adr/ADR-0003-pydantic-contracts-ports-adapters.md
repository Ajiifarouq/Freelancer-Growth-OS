# ADR-0003 — Pydantic Contracts with Ports and Adapters

**Status:** Accepted  
**Date:** 2026-08-11

## Decision

Represent product/application contracts with Pydantic v2 models and isolate infrastructure through explicit application ports/adapters.

## Drivers

- Phase 2B defines stable logical contracts that need machine validation.
- LLM outputs must not enter product state as unvalidated free-form objects.
- SQLite, OpenAI, current-research, connector, and future HTTP infrastructure must remain replaceable without changing domain rules.
- The same contracts should support CLI, tests, and later FastAPI JSON interfaces.

## Alternatives

- Plain dictionaries: rejected because they weaken validation, discoverability, and compatibility checks.
- Provider-specific SDK models as domain contracts: rejected because they create vendor coupling.
- Separate JSON-schema-first language: viable but adds an extra schema authoring layer for the Python-first runtime.

## Consequences

- Contracts require stable IDs/schema versions where persisted or shared externally.
- Infrastructure-specific response objects are converted at adapter boundaries.
- Contract-breaking changes require compatibility review/migration.
- Validation failures are explicit workflow failures, not silently coerced product truth.
