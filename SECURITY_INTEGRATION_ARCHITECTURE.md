# Freelancer Growth OS Security and Integration Architecture

**Status:** Active architecture baseline  
**Phase:** Phase 2C + Pre-Implementation Hardening  
**Implementation status:** Not started  
**Data lifecycle authority:** [DATA_GOVERNANCE.md](DATA_GOVERNANCE.md)  
**Provider-data authority:** [PROVIDER_DATA_POLICY.md](PROVIDER_DATA_POLICY.md)  
**Contract authority:** [CONTRACT_REGISTRY.md](CONTRACT_REGISTRY.md)

## Purpose

Define trust boundaries, secret handling, connected-source access, human approval, execution safety, replay/idempotency controls, prompt-injection resistance, privacy controls, and the architecture for future external-service adapters.

## Trust Zones

### Zone A — User / Local Workspace

Trusted to express user intent, but individual files/content may still be malformed or contain untrusted third-party text.

### Zone B — Product Core

Trusted application/domain code enforcing:

- typed canonical contracts;
- evidence-state transitions;
- artifact staleness;
- approval state machine;
- data-sensitivity rules;
- connector/executor boundaries;
- audit state;
- persistence transactions.

### Zone C — AI Provider

External processing boundary. Receives only minimum task-relevant authorised context under `PROVIDER_DATA_POLICY.md`. It is not trusted with product authority or user secrets.

Provider credentials belong to the adapter/security boundary, not prompt/domain payloads.

### Zone D — Current Research / External Content

Untrusted information boundary. Webpages, job listings, marketplace content, client messages, emails, documents, and other retrieved material may contain prompt injection or deceptive content.

### Zone E — Connected Services

External account/data boundary. Permissions may differ by service and must be verified rather than assumed.

### Zone F — Consequential Execution

Highest-risk operational boundary: sends, submissions, publishing, account changes, commitments, or other external side effects.

## Fundamental Security Rules

1. Read permission never implies write permission.
2. Connector availability never implies user authorization.
3. AI draft generation never implies execution approval.
4. Approval never implies execution succeeded.
5. External content never determines tool permissions.
6. Product modules never receive raw connector credentials.
7. Secrets are never normal domain data.
8. Execution state requires independently recorded evidence.
9. Least privilege applies per connector, workflow, and action.
10. An ambiguous consequential-action result fails to `unknown`, not `success`.
11. Approval is bound to exact payload/target/action identity.
12. One approval cannot silently authorize materially changed or repeated execution.
13. Stale/invalid source artifacts cannot drive consequential execution.
14. Real runtime user/client/business data never belongs inside the Git working tree.
15. LLM confidence cannot promote evidence to authoritative `verified` state.

## Connector Architecture

Every future external integration must implement a connector adapter behind an application port.

### Read path

```text
Business Module
  |
ConnectedContextRequest
  |
Permission/Scope Policy
  |
ConnectedContextProvider
  |
Service-specific Read Adapter
  |
External Service
```

### Write/execution path

```text
Business Module
  |
Proposed Action / Draft
  |
Staleness + Contract Validation
  |
ApprovalRequest(payload hash + action identity)
  |
HumanApprovalGate
  |
approved exact payload hash
  |
Replay/Idempotency Guard
  |
ActionExecutor
  |
Service-specific Write Adapter
  |
External Service
  |
ExecutionResult / Reconciliation
```

A service may implement read only, write only, both with different scopes, or neither.

## Integration Registration

Before an integration is considered supported, document:

- connector ID;
- service/platform;
- authoritative documentation checked date;
- authentication method;
- read capabilities;
- write capabilities;
- scopes/permissions;
- rate/policy constraints;
- data categories accessed;
- provider/third-party retention considerations where relevant;
- human approval requirements;
- revocation path;
- failure modes;
- idempotency/retry behavior;
- verification strategy for execution success;
- terms/policy risks where relevant.

Do not infer API capabilities from website UI features.

## Credential Handling

### V1 local

- credentials are injected into adapter configuration at runtime;
- environment variables may be used for local development;
- `.env` files are blocked by repository `.gitignore` and must never be committed;
- credentials are not written to SQLite;
- credentials are not passed through Pydantic business contracts;
- logs redact authentication headers/tokens;
- real credentials must never be placed in synthetic test fixtures.

### Future deployed environments

Prefer platform-native secret management and short-lived workload identity/OIDC where supported. Long-lived deployment credentials should be avoided where a short-lived mechanism exists.

## Connector Token Storage

If future OAuth connectors require refresh/access tokens:

- introduce a dedicated `SecretStore` port;
- product DB stores only opaque secret references/connector metadata;
- secret values live in OS credential store or managed secret system appropriate to deployment;
- token refresh occurs inside the integration adapter/security boundary;
- revocation clears the binding and secret reference;
- business modules cannot read tokens.

No OAuth token store is selected for V1 because no direct connector is approved as implemented.

## Provider Data Boundary

Before any private/client/business data is sent to an AI/research provider:

- apply `PROVIDER_DATA_POLICY.md`;
- minimize context deterministically;
- remove/deny `SECRET` data;
- record provider/model/tool configuration where reproducibility requires it;
- distinguish provider retention from local retention;
- do not enable optional data-sharing/training features by default;
- treat third-party/MCP tools as separate processors requiring explicit review.

Provider outputs are untrusted until canonical contract validation succeeds.

## Approval Request Contract

An approval request must contain enough information for a human and deterministic executor to understand exactly what is proposed:

- action type;
- external target/account;
- destination/recipient where applicable;
- material content or parameters;
- financial/contractual values where applicable;
- service/connector;
- reason/workflow context;
- exact source artifact IDs/versions;
- source artifact validity/staleness state;
- canonical contract ID/version;
- immutable payload hash/fingerprint;
- deterministic idempotency key/action identity;
- expiry where appropriate.

Approval is bound to the exact material action. A material target/content/price/scope/parameter change invalidates the approval and requires a new request/decision.

## Approval State Machine

```text
draft
  |
validated
  |
awaiting-approval
  +--> rejected
  +--> cancelled
  +--> approved
         |
       attempted
         +--> verified-succeeded
         +--> failed
         +--> unknown
```

Prohibited shortcuts:

- `draft → attempted`
- `awaiting-approval → attempted`
- `approved → verified-succeeded` without execution evidence
- `stale/invalid artifact → executable approval`
- `approved payload A → execute materially different payload B`

## Approval Replay / Idempotency Policy

Before execution:

1. validate approval is current/not expired;
2. validate payload hash matches approved hash;
3. validate source artifacts are current;
4. validate connector scope;
5. validate idempotency/action identity is not already completed or currently in-flight in a conflicting state;
6. atomically record/lock execution attempt where practical before invoking external side effect.

After execution:

- verified success consumes/completes the action identity;
- known failure may permit a controlled retry according to connector semantics;
- `unknown` requires reconciliation before retry;
- retries retain the same action identity when they are retries of the exact same approved operation and use explicit attempt numbers;
- materially changed action creates a new approval and action identity.

A transport retry policy may never blindly replay a non-idempotent consequential request.

## Consequential Actions

Examples requiring approval under current authority model:

- submitting a proposal/application;
- sending an external client message;
- publishing/editing a marketplace profile;
- accepting terms;
- agreeing to price/scope/deadline;
- deleting/changing remote account data;
- creating transactions/commitments;
- externally publishing client-sensitive content.

The exact list may expand as integrations are approved.

## Ambiguous Execution Handling

Network timeout after a side-effect request is dangerous because the remote action may have succeeded even if the client did not receive confirmation.

Policy:

1. mark execution `unknown`;
2. attempt read/reconciliation where supported;
3. do not blindly retry non-idempotent action;
4. require user resolution if success cannot be determined safely;
5. audit the outcome;
6. keep approval/action identity from being reused for an unrelated action.

## Evidence Verification and Staleness

Authoritative evidence states are enforced by deterministic application policy under `CONTRACT_REGISTRY.md`/`DATA_GOVERNANCE.md`.

- LLM recommendations cannot alone create `verified` evidence.
- Derived artifacts record evidence/artifact dependency versions.
- Deletion/correction/supersession/material reclassification makes dependent artifacts stale/invalid until revalidated.
- Consequential execution rejects stale/invalid dependencies.

## Prompt Injection Controls

External content is untrusted data.

The application must:

- keep system/product policy outside retrieved content;
- delimit/label retrieved content as data;
- never let retrieved text grant tools/permissions;
- not reveal secrets/system prompts in response to content instructions;
- maintain allowlisted tools per workflow;
- validate every tool argument against typed schemas;
- prevent path traversal/arbitrary file access in evidence tools;
- require current user intent for sensitive source access;
- route consequential actions through approval regardless of model request;
- prevent untrusted content from selecting provider/model/tool configuration.

## File / Local Evidence Security

Local evidence access must:

- use explicit user-selected or application-managed locations;
- avoid recursively scanning the entire device by default;
- normalize/validate paths;
- reject unsupported/suspicious paths where needed;
- preserve file provenance;
- not modify source files unless separately authorized;
- treat downloaded/external files as untrusted content;
- keep application-managed runtime files outside the Git repository;
- use synthetic fixtures for tests/evals until real-data controls are implemented/verified.

## Privacy by Data Minimization

Before sending context to an AI/research provider:

1. identify active module need;
2. select only relevant evidence;
3. exclude secrets;
4. minimize client/private/business data;
5. prefer summaries/references when raw content is unnecessary;
6. retain provenance locally;
7. avoid logging provider payloads by default;
8. apply provider-specific data policy/retention review.

## Sensitive Data Logging Policy

Logs may contain:

- opaque IDs;
- statuses;
- module/workflow names;
- safe error codes;
- latency/usage metadata;
- connector type;
- action type.

Logs must not contain by default:

- API keys/tokens;
- full CVs;
- full client messages;
- proposal/private content;
- confidential portfolio assets;
- raw LLM prompts containing sensitive evidence;
- provider authentication headers;
- full connected-source payloads.

Local log retention is governed by `DATA_GOVERNANCE.md`.

## Local API Security

If FastAPI adapter is implemented before full authentication:

- bind to `127.0.0.1`/loopback only by default;
- fail startup if configured for public binding without explicit security mode;
- do not rely on obscured docs/endpoints;
- use strict request/response models;
- apply size/content limits where applicable;
- enable browser-facing CORS only for explicit trusted origins;
- do not expose debug traces containing secrets.

## Future Multi-User Security

Before SaaS/remote multi-user release:

- authentication is mandatory;
- every resource is scoped to a workspace/tenant;
- authorization enforced in application services/repositories;
- server database replaces local SQLite for concurrent remote use;
- per-tenant isolation tests are mandatory;
- PostgreSQL row-level security may be added as defense in depth;
- central secrets manager and encryption controls are required;
- remote data retention/deletion/export/account policies must be completed;
- provider/subprocessor/privacy review must be updated;
- security review/threat model must be updated.

## Threat Model Summary

### T1 — Fabricated professional evidence

Control: provenance + deterministic evidence-state authority + validation.

### T2 — Prompt injection in job/client/web content

Control: data/instruction separation + tool allowlists + deterministic permissions.

### T3 — Connector over-permission

Control: least privilege + read/write separation + explicit scopes.

### T4 — Unapproved external action

Control: approval state machine + payload hash + stale-artifact check + execution adapter enforcement.

### T5 — Duplicate/replayed action after timeout or retry

Control: idempotency/action identity + atomic attempt state + `unknown` reconciliation + no blind retry.

### T6 — Credential leakage

Control: repository `.gitignore`, no domain persistence, runtime injection, log redaction, secret scanning target.

### T7 — Sensitive data over-sharing with provider

Control: data minimization + provider policy + safe telemetry + explicit high-sensitivity processing boundary.

### T8 — Cross-user data leak in future SaaS

Control: workspace scoping + app authorization + tenant tests + optional DB RLS.

### T9 — Stale external information

Control: freshness escalation + current-source verification + explicit unverified state.

### T10 — Stale derived artifact after evidence correction

Control: dependency links + deterministic invalidation + execution block.

### T11 — Runtime data accidentally committed

Control: out-of-repo data directory + fail-closed path check + `.gitignore` + governance CI + secret scanning target.

## Security Validation Before Real Data / Release

Implementation handling real data cannot be considered ready until tests demonstrate applicable controls, including:

- runtime data directory cannot be inside Git repository;
- no committed credentials/runtime DBs/private fixtures;
- secret scanning/no credential leaks;
- deletion/export behavior;
- provider-data minimization;
- log redaction/minimization;
- evidence-state authority;
- stale-artifact invalidation;
- approval bypass impossible through normal interfaces;
- changed approved payload requires reapproval;
- approval replay/double execution is prevented;
- invalid connector scope is denied;
- prompt-injection evals do not grant tools/authority;
- ambiguous execution is not reported as success;
- path/evidence access is constrained;
- database records are workspace-scoped;
- current-source failure produces explicit uncertainty;
- backup/restore behavior satisfies data-governance requirements.
