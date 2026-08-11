# ADR-0002 — CPython 3.14 and uv

**Status:** Accepted  
**Date:** 2026-08-11

## Decision

Use CPython 3.14 as the V1 runtime and `uv` for Python version/dependency/project management with `pyproject.toml` plus a committed `uv.lock`.

## Drivers

- Python is well suited to the product's AI, structured-data, CLI, and automation-heavy runtime.
- Python 3.14 is a current stable Python line at the time of this decision.
- `uv` supports managed Python environments, dependency groups, project metadata, and cross-platform lockfiles.
- One project tool reduces setup friction and supports reproducible environments.

## Alternatives

- JavaScript/TypeScript first: viable for a web-first product, but V1 is not web-first and the AI/data workflow core benefits from Python's ecosystem.
- Poetry/pip-tools/pip-only: workable, but `uv` gives one project/lock/environment workflow.
- Python 3.15 prerelease: rejected for baseline stability.

## Consequences

- Implementation must declare its Python compatibility explicitly.
- Dependencies are locked and reviewed in version control.
- Runtime-specific provider/domain assumptions remain prohibited.
- Future web frontend technology remains independent of the Python core.
