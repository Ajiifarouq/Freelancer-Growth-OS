# ADR-0005 — Typer CLI First, FastAPI HTTP Adapter Later

**Status:** Accepted  
**Date:** 2026-08-11

## Decision

Use Typer for the first operator/user interface. Select FastAPI as the HTTP adapter for a later personal web application or remote API, while keeping the application core interface-independent.

## Drivers

- V1 is local-first and does not require a browser/server.
- A CLI lets the architecture be exercised without frontend/authentication complexity.
- Typer uses Python type hints and supports structured CLI applications.
- FastAPI aligns with Python/Pydantic contracts and can expose schema-driven JSON/OpenAPI interfaces later.

## Alternatives

- Web UI first: rejected because it brings frontend, auth, browser security, hosting, and deployment before current requirements require them.
- Desktop GUI first: rejected because no GUI-specific workflow is currently required.
- CLI only forever: rejected because staged-hybrid evolution includes a personal application path.

## Consequences

- CLI commands call application workflows, never databases/providers directly.
- FastAPI is an adapter, not the owner of business logic.
- No frontend framework is selected in Phase 2C.
- Any local HTTP server without remote auth must bind to loopback by default.
