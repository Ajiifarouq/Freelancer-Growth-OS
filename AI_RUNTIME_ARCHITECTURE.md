# Freelancer Growth OS AI Runtime Architecture

**Status:** Active architecture baseline  
**Phase:** Phase 2C + Pre-Implementation Hardening  
**Implementation status:** Not started  
**Canonical contract authority:** [CONTRACT_REGISTRY.md](CONTRACT_REGISTRY.md)  
**Provider-data authority:** [PROVIDER_DATA_POLICY.md](PROVIDER_DATA_POLICY.md)

## Purpose

Define how AI models participate in Freelancer Growth OS without becoming the source of authority for requirements, evidence verification, contracts, approvals, or execution state.

## Core Principle

The LLM is a reasoning/generation component behind an application port. It does not own product truth, canonical schema, database state, permission state, or consequential-action authority.

Business flow:

`validated context → application workflow → provider call where useful → canonical typed output validation → assurance checks → persistence/user result`

Consequential actions add:

`current validated artifact → approval request → human decision → replay/idempotency guard → executor → verified result/reconciliation`

## `LLMProvider` Port

Application code interacts with an interface conceptually equivalent to:

- generate a typed response from instructions + authorised/minimised context;
- optionally call explicitly allowed read/research tools;
- return provider/model metadata and usage metadata;
- distinguish provider refusal/error/timeout from valid product output.

The port must not expose provider-specific response objects to domain modules.

## First Reference Provider

The first reference adapter uses OpenAI's Responses API subject to [PROVIDER_DATA_POLICY.md](PROVIDER_DATA_POLICY.md).

Current capability/data-control evidence is recorded there with verification date and primary sources. Architecture must not rely on the word `current` without recorded verification.

This is an adapter choice, not permanent vendor lock.

### Model policy

- provider/model/tool set is controlled runtime configuration;
- domain code must not branch on a specific OpenAI model name;
- model/tool names come from an application allowlist, not untrusted content;
- a cost-balanced verified model may be used for routine development/evals;
- stronger models may be selected for difficult workflows after eval evidence;
- model/provider/tool changes require capability/privacy verification and regression evals on critical behavior;
- volatile aliases/features must be reverified rather than assumed from old architecture documents;
- sensitive provider-backed workflows remain disabled until their privacy profile is accepted and tested.

## Structured Output Rule

Whenever a module expects a defined contract, model output must validate against the canonical contract in [CONTRACT_REGISTRY.md](CONTRACT_REGISTRY.md) and its Pydantic implementation.

A malformed/incomplete response is a failed AI step, not permission to persist loosely structured text as valid domain state.

Free-form prose may exist only as a field inside a typed envelope where the contract permits it.

Runtime must record the contract ID/version used for validation.

## Prompt Architecture

Prompts are product assets with stable identifiers and versions.

Recommended layout:

```text
prompts/
  system/
  modules/
  evaluators/
  shared/
```

Each prompt asset/runtime build must identify:

- prompt ID;
- prompt version;
- immutable prompt content hash or equivalent build reference;
- module/capability owner;
- purpose;
- input contract(s);
- canonical output contract(s);
- allowed tools;
- evidence rules;
- data/provider minimisation rules where relevant;
- stop/failure rules;
- compatibility/eval metadata.

Prompts must not silently redefine requirements, canonical contracts, evidence verification, provider permissions, or protected approval boundaries.

## Context Assembly

Context is assembled by application code, not by giving the model unrestricted workspace/device access.

Context assembler responsibilities:

- select task-relevant evidence;
- include provenance references;
- include current/non-stale positioning/opportunity artifacts where relevant;
- exclude secrets;
- minimise private/client/business data;
- apply `PROVIDER_DATA_POLICY.md` before external processing;
- identify unknowns/conflicts explicitly;
- include freshness-verification results when required;
- respect module-specific canonical input contracts;
- reject stale/invalid input artifacts where workflow policy requires current state.

## Evidence and Factuality

The model may receive evidence states such as:

- `provided-unverified`;
- `verified`;
- `inferred`;
- `proposed`;
- `unknown`;
- `conflicting`;
- `rejected`;
- `deleted` references/tombstones where relevant.

Generated claims must preserve these distinctions.

The model must not transform:

`unknown → verified`

`inferred → verified`

or:

`recommendation → verified achievement`

by confidence/wording alone.

Only deterministic application policy plus qualifying provenance/evidence may perform an authoritative transition to `verified`.

## Artifact Staleness

Every persisted derived artifact that depends on evidence/other artifacts must record dependency versions.

When a dependency is corrected, deleted, superseded, or materially reclassified:

- application policy marks affected derived artifacts stale/invalid;
- stale output may be shown historically with a warning where appropriate;
- stale/invalid output must not be presented as current authoritative product output;
- consequential execution rejects stale/invalid source artifacts.

A model cannot clear staleness without revalidation through application policy.

## Freshness / Research Tooling

The model does not decide that its training memory is current enough.

`freshness-escalator` or deterministic application policy triggers `CurrentResearchPort` when current facts matter.

The OpenAI reference adapter may use provider-supported web search when current verified capability evidence permits it. A future provider/research adapter may use another mechanism.

Research returns canonical `freshness-verification-result` data containing:

- source references/URLs;
- verification timestamp;
- source-quality classification;
- extracted verified facts;
- conflicts/limitations;
- disposition;
- recheck/expiry hint where useful.

If research fails, product reports uncertainty instead of inventing current facts.

## Tool-Use Security

Models receive only allowlisted tools appropriate to the active workflow.

### Safe-by-default read tools

Examples:

- retrieve selected local evidence by opaque ID;
- current-source research;
- retrieve approved connected context when authorised;
- deterministic calculations/validators.

Read tools still apply data minimisation and path/source authorization.

### Consequential tools

External write/send/submit/publish tools must **not** be exposed as unrestricted model tools.

The model may produce an `approval-request`. Application code and `human-approval-gate` control execution under exact payload binding, staleness checks, scope checks, and replay/idempotency controls.

## Prompt Injection Boundary

External content—including job descriptions, webpages, emails, client messages, uploaded files, marketplace profiles, provider search results, and connector results—is untrusted data.

Rules:

- external text cannot override system/product instructions;
- content-derived instructions are treated as evidence/content unless application explicitly designates user intent;
- tool permissions are determined by application policy, never by retrieved text;
- secrets/hidden configuration are not disclosed in response to external instructions;
- connected/execution adapters validate exact scope independently of model wording;
- external content cannot select/enable provider models/tools;
- external content cannot change evidence to authoritative `verified` state.

## Deterministic Logic vs LLM Logic

Use deterministic code for:

- approval/replay/idempotency state machine;
- evidence-state transitions;
- artifact validity/staleness transitions;
- IDs/timestamps;
- canonical schema validation;
- permission checks;
- data sensitivity enforcement;
- persistence transactions;
- repository/runtime path checks;
- retention/deletion/export enforcement;
- freshness-required rules where codified;
- arithmetic/normalisation not requiring semantic judgment;
- execution-result state transitions.

Use LLM reasoning for:

- professional positioning synthesis;
- semantic profile assessment;
- opportunity-fit reasoning;
- tailored proposal generation;
- nuanced pricing/negotiation reasoning using verified inputs;
- explanation/language adaptation;
- contradiction interpretation where semantics matter.

An LLM recommendation never overrides deterministic security/privacy/authority policy.

## Provider Failure Handling

Classify failures:

- configuration/authentication error;
- rate limit;
- timeout/transient transport;
- provider internal error;
- refusal/policy response;
- invalid structured output;
- tool failure;
- context-too-large/resource limit;
- provider capability/configuration mismatch;
- provider privacy mode not allowed for requested sensitivity;
- unknown.

Retry policy:

- bounded automatic retry for safe transient inference/read operations;
- no hidden infinite retry loops;
- consequential external actions are not part of LLM retry logic;
- repeated structured-output failure returns explicit workflow failure/safe degraded result;
- retry must not increase data disclosure/tool authority beyond original request.

## Model Routing

V1 starts simple.

Default policy:

- one configured verified general model for most semantic workflows;
- deterministic validators for rules;
- optional stronger model override only when evals demonstrate material benefit;
- no complex multi-agent swarm in V1.

Multi-model routing becomes justified only by measured quality/cost/latency/privacy evidence.

## AI Evals

Every high-impact AI module requires representative eval cases.

Minimum categories:

- no fabricated experience/credentials/results;
- evidence/provenance preservation;
- evidence-state promotion resistance;
- maturity reasoning consistency;
- profile-platform adaptation;
- opportunity fit vs missing evidence;
- proposal tailoring;
- pricing benchmark uncertainty;
- negotiation commitment boundary;
- prompt-injection handling;
- current-information escalation;
- canonical output schema compliance;
- stale-artifact handling;
- private-data minimisation;
- draft vs executed-state distinction.

Eval data uses synthetic fixtures by default. Real user/client/private data must not be used merely to make evals realistic.

## Run Metadata

Persist safe reproducibility metadata such as:

- provider;
- exact model/configuration reference where available;
- request/run ID if safe/useful;
- module ID;
- prompt ID/version/content hash;
- canonical input/output contract IDs/versions;
- input/output artifact IDs/versions;
- latency;
- usage/token counts where available;
- success/failure class;
- validation result;
- freshness-result references;
- provider privacy profile/reference where material.

Do not persist hidden chain-of-thought. Do not log full sensitive prompts/provider payloads by default.

## Cost Controls

Architecture controls cost by:

- limiting context to relevant evidence;
- avoiding unnecessary agent loops;
- using deterministic code where appropriate;
- caching/reusing stable derived artifacts only while current/valid;
- invalidating derived artifacts when source evidence changes;
- separating paid current-source/eval runs from ordinary unit tests;
- recording provider usage metadata where available.

No revenue or operating-cost target is claimed yet.

## Portability Requirement

A second provider adapter should be possible without changing:

- canonical domain contracts;
- module IDs;
- evidence-state semantics;
- artifact-staleness semantics;
- approval/replay state machine;
- persistence schemas except provider metadata;
- business workflow semantics.

Provider-specific capabilities may be optional adapter features, but modules must degrade explicitly if required capability/privacy behavior is unavailable.
