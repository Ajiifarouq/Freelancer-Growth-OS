# Summary

Describe the requested outcome and the behavior changed by this PR.

## Scope

- Base branch:
- Head branch:
- Requirements served:
- Capabilities/modules affected:
- Explicit non-goals:

## Change Classification

Select all that apply:

- [ ] Documentation
- [ ] Defect correction
- [ ] Internal refactor
- [ ] Product capability change
- [ ] Contract/schema change
- [ ] Database migration
- [ ] Prompt/AI behavior change
- [ ] LLM/provider adapter change
- [ ] Connected-service integration change
- [ ] Security/privacy change
- [ ] Release/operations change
- [ ] Breaking change

## Architecture

- [ ] Existing architecture supports this change.
- [ ] Architecture/ADR update is included because a material long-lived decision changed.
- [ ] Not applicable; explain below.

Architecture notes:

## Compatibility and Migration

Compatibility class:

- [ ] Internal-only
- [ ] Backward-compatible
- [ ] Conditionally compatible
- [ ] Breaking
- [ ] Deprecated-but-supported
- [ ] Retired

Migration/upgrade impact:

Rollback/recovery considerations:

## Contracts, Data, and Prompts

List any changed:

- Pydantic/serialized contracts:
- CLI/API interfaces:
- database schema/Alembic revisions:
- prompt IDs/versions:
- export/import formats:
- integration adapter contracts:

## Security and Privacy

- Secrets/credentials impact:
- Personal/client/business-data impact:
- Permission/read-write boundary impact:
- Human-approval boundary impact:

## Factuality and Freshness

If behavior depends on current external facts, identify the verified source/date or explain why current verification is not material.

AI/evidence/factuality risks:

## Validation Evidence

Record what actually ran. Do not mark unavailable checks as passed.

- [ ] Formatting
- [ ] Linting
- [ ] Static typing
- [ ] Unit tests
- [ ] Contract tests
- [ ] Integration tests
- [ ] Migration tests
- [ ] AI evals
- [ ] Security/privacy checks
- [ ] Approval-state tests
- [ ] Manual acceptance/smoke tests
- [ ] Documentation/link checks

Commands/checks and results:

## Release Impact

- [ ] Release-neutral merged work
- [ ] Candidate for future PATCH
- [ ] Candidate for future MINOR
- [ ] Candidate for future MAJOR
- [ ] Release preparation PR

Version impact rationale:

## Residual Risk / Open Questions

List remaining risks, limitations, blockers, or `None`.

## Approval Boundary

This PR does not by itself authorize merge, tag creation, release publication, deployment, or consequential external product actions. Record required protected-action authorization separately.
