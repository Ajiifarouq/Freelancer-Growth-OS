# ADR-0001 — Local-First Modular Monolith

**Status:** Accepted  
**Date:** 2026-08-11

## Decision

Version 1 will run as a local-first modular monolith in one application process. Business capabilities communicate through typed in-process contracts and application services rather than network calls.

## Drivers

- `FGOS-D001` requires AI framework/OS first, personal app later, SaaS only when justified.
- Current requirements do not require remote multi-user concurrency.
- Private freelancer/client data benefits from a small initial exposure surface.
- Phase 2B already defines stable module boundaries independent of process boundaries.

## Alternatives

- Microservices: rejected for V1 because they add network, deployment, observability, authentication, and distributed-failure complexity without a current requirement.
- Web SaaS first: rejected because it contradicts staged-hybrid sequencing.
- Prompt-only repository with no application core: rejected because Phase 2 requirements require persistence, approvals, traceability, modules, and later interface evolution.

## Consequences

- Simple local execution and testing.
- Modules remain logically separated but share one runtime.
- Later FastAPI/web/SaaS adapters can reuse the core.
- If scale later requires process separation, module contracts provide migration seams.
