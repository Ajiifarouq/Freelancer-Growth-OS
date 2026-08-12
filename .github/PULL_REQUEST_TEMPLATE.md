# Summary

Describe the requested outcome and the behavior changed by this PR.

## Scope

- Base branch:
- Head branch:
- Requirements served:
- Current decisions served/changed:
- Capabilities/modules affected:
- Canonical contracts affected:
- Explicit non-goals:

## Change Classification

Select all that apply:

- [ ] Documentation
- [ ] Defect correction
- [ ] Internal refactor
- [ ] Product capability change
- [ ] Contract/schema change
- [ ] Database migration
- [ ] Data retention/deletion/export change
- [ ] Prompt/AI behavior change
- [ ] LLM/provider adapter change
- [ ] Connected-service integration change
- [ ] Security/privacy change
- [ ] Approval/execution change
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

- `CONTRACT_REGISTRY.md` contract IDs/versions:
- Pydantic/serialized models:
- CLI/API interfaces:
- database schema/Alembic revisions:
- prompt IDs/versions/content hashes:
- export/import formats:
- integration adapter contracts:

Contract alias/duplicate-schema risk:

Artifact dependency/staleness impact:

## Data Governance

- Data classes handled:
- Real or synthetic data used in development/tests/evals:
- Runtime data directory/location impact:
- Retention impact:
- Deletion impact:
- Export impact:
- Backup/restore impact:
- Logging/telemetry impact:
- Encryption/device-protection impact:

If real user/client/business data is involved, identify the evidence that `DATA_GOVERNANCE.md` controls are implemented and tested.

## Provider / External Processing

- Provider(s)/model(s)/tools affected:
- Data categories sent externally:
- Minimum-necessary disclosure applied:
- Provider capability verification source/date:
- Provider retention/data-control review:
- Third-party/MCP processing impact:
- Eval/compatibility evidence:

Use `Not applicable` only when no external provider processes product data.

## Security and Privacy

- Secrets/credentials impact:
- Personal/client/business-data impact:
- Permission/read-write boundary impact:
- Human-approval boundary impact:
- Prompt-injection/untrusted-content impact:
- Repository `.gitignore`/secret-scanning impact:

## Evidence / Factuality / Freshness

If behavior depends on current external facts, identify the verified primary source/date or explain why current verification is not material.

Evidence-state transitions affected:

AI/evidence/factuality risks:

## Consequential Action Safety

If external writes/actions are possible:

- Payload fingerprint binding:
- Idempotency/action identity:
- Approval-decision reference:
- Replay/double-execution protection:
- Stale-artifact rejection:
- Ambiguous-result reconciliation:

If no consequential execution exists, state `Not applicable`.

## Validation Evidence

Record what actually ran. Do not mark unavailable checks as passed.

- [ ] Repository governance safety CI
- [ ] Formatting
- [ ] Linting
- [ ] Static typing
- [ ] Unit tests
- [ ] Contract/schema tests
- [ ] Integration tests
- [ ] Migration tests
- [ ] Data deletion/export tests
- [ ] Backup/restore tests
- [ ] AI evals
- [ ] Security/privacy checks
- [ ] Secret scanning
- [ ] Approval/idempotency tests
- [ ] Stale-artifact tests
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

List remaining risks, limitations, blockers, manual repository settings, or `None`.

## Approval Boundary

This PR does not by itself authorize merge, tag creation, release publication, deployment, repository visibility/ruleset changes, or consequential external product actions. Record required protected-action authorization separately unless the owner explicitly bundled the named actions and scope.
