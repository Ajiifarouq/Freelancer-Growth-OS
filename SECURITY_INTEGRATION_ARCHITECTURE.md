# Freelancer Growth OS Security and Integration Architecture

**Status:** Active architecture baseline  
**Phase:** Phase 2C — Technical Architecture  
**Implementation status:** Not started

## Purpose

Define trust boundaries, secret handling, connected-source access, human approval, execution safety, prompt-injection resistance, privacy controls, and the architecture for future external-service adapters.

## Trust Zones

### Zone A — User / Local Workspace

Trusted to express user intent, but individual files/content may still be malformed or contain untrusted third-party text.

### Zone B — Product Core

Trusted application/domain code enforcing:

- typed contracts;
- approval state machine;
- data-sensitivity rules;
- connector/executor boundaries;
- audit state;
- persistence transactions.

### Zone C — AI Provider

External processing boundary. Receives only task-relevant authorised context. It is not trusted with product authority or secrets beyond the provider credential required by its adapter.

### Zone D — Current Research / External Content

Untrusted information boundary. Webpages, job listings, marketplace content, client messages, emails, documents, and other retrieved material may contain prompt injection or deceptive content.

### Zone E — Connected Services

External account/data boundary. Permissions may differ by service and must be verified rather than assumed.

### Zone F — Consequential Execution

Highest-risk operational boundary: sends, submissions, publishing, account changes, commitments, or other external side effects.

## Fundamental Security Rules

1. Read permission never implies write permission.
2. Connector availability never implies user authorisation.
3. AI draft generation never implies execution approval.
4. Approval never implies execution succeeded.
5. External content never determines tool permissions.
6. Product modules never receive raw connector credentials.
7. Secrets are never normal domain data.
8. Execution state requires independently recorded evidence.
9. Least privilege applies per connector, workflow, and action.
10. An ambiguous consequential-action result fails to `unknown`, not `success`.

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
ApprovalRequest
  |
HumanApprovalGate
  |
approved exact payload hash
  |
ActionExecutor
  |
Service-specific Write Adapter
  |
External Service
  |
ExecutionResult
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
- human approval requirements;
- revocation path;
- failure modes;
- verification strategy for execution success;
- terms/policy risks where relevant.

Do not infer API capabilities from website UI features.

## Credential Handling

### V1 local

- credentials are injected into adapter configuration at runtime;
- environment variables may be used for local development;
- `.env` files must be gitignored and never committed;
- credentials are not written to SQLite;
- credentials are not passed through Pydantic business contracts;
- logs redact authentication headers/tokens.

### Future deployed environments

Prefer platform-native secret management and short-lived workload identity/OIDC where supported. Long-lived deployment credentials should be avoided where a short-lived mechanism exists.

## Connector Token Storage

If future OAuth connectors require refresh/access tokens:

- introduce a dedicated `SecretStore` port;
- product DB stores only opaque secret references/connector metadata;
- secret values live in OS credential store or managed secret system appropriate to the deployment;
- token refresh occurs inside the integration adapter/security boundary;
- revocation clears the binding and secret reference;
- business modules cannot read tokens.

No OAuth token store is selected for V1 because no direct connector is approved as implemented.

## Approval Request Contract

An approval request must contain enough information for a human to understand exactly what is proposed:

- action type;
- external target/account;
- destination/recipient where applicable;
- material content or parameters;
- financial/contractual values where applicable;
- service/connector;
- reason/workflow context;
- payload hash;
- expiry where appropriate.

Approval is bound to the exact material action. A material target/content/price/scope change invalidates the approval and requires a new decision.

## Approval State Machine

```text
draft
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

## Consequential Actions

Examples requiring approval under the current authority model:

- submitting a proposal/application;
- sending an external client message;
- publishing/editing a marketplace profile;
- accepting terms;
- agreeing to price/scope/deadline;
- deleting or changing remote account data;
- creating transactions or commitments;
- externally publishing client-sensitive content.

The exact list may expand as integrations are approved.

## Ambiguous Execution Handling

Network timeout after a side-effect request is dangerous because the remote action may have succeeded even if the client did not receive confirmation.

Policy:

1. mark execution `unknown`;
2. attempt a read/reconciliation check where the service supports one;
3. do not blindly retry non-idempotent actions;
4. require user resolution if success cannot be determined safely;
5. audit the outcome.

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
- route consequential action through approval regardless of model request.

## File/Local Evidence Security

Local evidence access must:

- use explicit user-selected or application-managed locations;
- avoid recursively scanning the entire device by default;
- normalise/validate paths;
- reject unsupported/suspicious paths where needed;
- preserve file provenance;
- not modify source files unless a separately authorised feature explicitly requires it;
- treat downloaded/external files as untrusted content.

## Privacy by Data Minimisation

Before sending context to an AI/research provider:

1. identify the active module need;
2. select only relevant evidence;
3. exclude secrets;
4. minimise client/private data;
5. prefer summaries/references when raw content is unnecessary;
6. retain provenance locally;
7. avoid logging provider payloads by default.

## Sensitive Data Logging Policy

Logs should contain:

- opaque IDs;
- statuses;
- module/workflow names;
- safe error codes;
- latency/usage metadata;
- connector type;
- action type.

Logs should not contain by default:

- API keys/tokens;
- full CVs;
- full client messages;
- proposal/private content;
- confidential portfolio assets;
- raw LLM prompts containing sensitive evidence.

## Local API Security

If the future FastAPI adapter is implemented before full authentication:

- bind to `127.0.0.1`/loopback only by default;
- fail startup if configured for public binding without an explicit security mode;
- do not rely on obscured docs/endpoints;
- use strict request/response models;
- apply size/content limits where applicable;
- enable browser-facing CORS only for explicit trusted origins;
- do not expose debug traces containing secrets.

## Future Multi-User Security

Before SaaS/remote multi-user release:

- authentication is mandatory;
- every resource is scoped to a workspace/tenant;
- authorisation enforced in application services/repositories;
- server database replaces local SQLite for concurrent remote use;
- per-tenant isolation tests are mandatory;
- PostgreSQL row-level security may be added as defence in depth;
- central secrets manager and encryption controls are required;
- remote data retention/deletion/export policies must be completed;
- security review/threat model must be updated.

## Threat Model Summary

### T1 — Fabricated professional evidence

Control: evidence provenance + validation + no silent unknown-to-fact promotion.

### T2 — Prompt injection in job/client/web content

Control: data/instruction separation + tool allowlists + deterministic permissions.

### T3 — Connector over-permission

Control: least privilege + read/write separation + explicit connector scopes.

### T4 — Unapproved external action

Control: approval state machine + payload hash + execution adapter enforcement.

### T5 — Duplicate action after timeout

Control: `unknown` state + reconciliation + no blind non-idempotent retry.

### T6 — Credential leakage

Control: no secret persistence in domain DB + runtime injection + log redaction.

### T7 — Sensitive data over-sharing with LLM/provider

Control: context minimisation + adapter boundary + safe telemetry.

### T8 — Cross-user data leak in future SaaS

Control: workspace scoping + app authorisation + tenant tests + optional DB RLS.

### T9 — Stale external information

Control: freshness escalation + current-source verification + explicit unverified state.

## Security Validation Before Release

V1 implementation cannot be considered release-ready until tests demonstrate:

- secret scanning/no committed credentials;
- approval bypass is impossible through normal interfaces;
- changed approved payload requires re-approval;
- invalid connector scope is denied;
- prompt-injection evals do not grant tools/authority;
- ambiguous execution is not reported as success;
- sensitive logs are redacted/minimised;
- path/evidence access is constrained;
- database records are workspace-scoped;
- current-source failure produces explicit uncertainty.
