# Freelancer Growth OS AI Runtime Architecture

**Status:** Active architecture baseline  
**Phase:** Phase 2C — Technical Architecture  
**Implementation status:** Not started

## Purpose

Define how AI models participate in Freelancer Growth OS without becoming the source of authority for requirements, evidence, approvals, or execution state.

## Core Principle

The LLM is a reasoning/generation component behind an application port. It does not own product truth, database state, permission state, or consequential-action authority.

Business flow:

`validated context → application workflow → LLM/provider call where useful → typed output validation → assurance checks → persistence/user result`

Consequential actions add:

`draft → approval request → human decision → executor → verified result`

## `LLMProvider` Port

Application code interacts with an interface conceptually equivalent to:

- generate a typed response from instructions + authorised context;
- optionally call explicitly allowed read/research tools;
- return provider/model metadata and usage metadata;
- distinguish provider refusal/error/timeout from valid product output.

The port must not expose provider-specific response objects to domain modules.

## First Reference Provider

The first reference adapter uses OpenAI's Responses API because the current API supports function calling, structured outputs, and tool-capable model workflows.

This is an adapter choice, not a permanent vendor lock.

### Model policy

- provider/model is runtime configuration;
- domain code must not branch on a specific OpenAI model name;
- a cost-balanced current model may be used for routine development/evals;
- stronger models may be selected for difficult workflows after eval evidence;
- model changes require regression evals on critical product behaviors;
- volatile model aliases/features must be verified before deployment rather than assumed from old architecture documents.

## Structured Output Rule

Whenever a module expects a defined contract, model output must be parsed/validated into the matching Pydantic model.

A malformed or incomplete response is a failed AI step, not an excuse to persist loosely structured text as if it were valid domain state.

Free-form prose may exist as a field inside a typed envelope.

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

Each prompt asset should identify:

- prompt ID;
- module/capability owner;
- purpose;
- input contract;
- expected output contract;
- allowed tools;
- evidence rules;
- stop/failure rules;
- version/changelog metadata.

Prompts must not silently redefine product requirements or protected approval boundaries.

## Context Assembly

Context should be assembled by application code, not by giving the model unrestricted access to the entire workspace.

Context assembler responsibilities:

- select task-relevant evidence;
- include provenance references;
- include current positioning/opportunity artifacts where relevant;
- exclude secrets;
- minimise unnecessary private/client data;
- identify unknowns explicitly;
- include freshness-verification results when required;
- respect module-specific input contracts.

## Evidence and Factuality

The model receives evidence classifications such as:

- verified user/authorised evidence;
- verified current external fact;
- approved product decision;
- inference/recommendation;
- unknown/unverified.

Generated claims must preserve those distinctions.

The model must not transform:

`unknown → fact`

or:

`recommendation → verified achievement`

without new evidence.

## Freshness / Research Tooling

The model does not decide that its training memory is current enough.

`freshness-escalator` or application policy triggers a `CurrentResearchPort` call when current facts matter.

The initial OpenAI adapter may use provider-supported web/search tooling as one implementation of that port. A future provider may use a different current-source mechanism.

Research results must return:

- source reference;
- checked/observed timestamp where available;
- extracted claim/result;
- verification status;
- failure/unavailable state.

If research fails, the product reports uncertainty instead of inventing current facts.

## Tool-Use Security

Models may receive only allowlisted tools appropriate to the active workflow.

### Safe-by-default read tools

Examples:

- retrieve selected local evidence by opaque ID;
- current-source research;
- retrieve approved connected context when authorised;
- deterministic calculations/validators.

### Consequential tools

External write/send/submit/publish tools must **not** be exposed as unrestricted model tools.

The model may produce an `ApprovalRequest`. Application code and the `human-approval-gate` control whether an executor becomes callable.

## Prompt Injection Boundary

External content—including job descriptions, webpages, emails, client messages, uploaded files, and marketplace profiles—is untrusted data.

Rules:

- external text cannot override system/product instructions;
- content-derived instructions are treated as evidence/content unless the application explicitly designates them as user intent;
- tool permissions are determined by application policy, never by text inside retrieved content;
- secrets and hidden configuration are not disclosed in response to external instructions;
- connected/execution adapters validate exact action scope independently of model wording.

## Deterministic Logic vs LLM Logic

Use deterministic code for:

- approval state machine;
- IDs/timestamps;
- schema validation;
- permission checks;
- data sensitivity enforcement;
- persistence transactions;
- freshness-required policy rules where codified;
- arithmetic/normalisation that does not require semantic judgment;
- execution result state transitions.

Use LLM reasoning for:

- professional positioning synthesis;
- semantic profile assessment;
- opportunity-fit reasoning;
- tailored proposal generation;
- nuanced pricing/negotiation reasoning using verified inputs;
- explanation and language adaptation;
- contradiction interpretation where semantics matter.

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
- unknown.

Retry policy:

- bounded automatic retry for safe transient inference/read operations;
- exponential/backoff strategy may be implemented later;
- no hidden infinite retry loops;
- consequential external actions are not part of LLM retry logic;
- repeated structured-output failure returns explicit workflow failure or safe degraded response.

## Model Routing

V1 should start simple.

Default policy:

- one configured general model for most semantic workflows;
- deterministic validators for rules;
- optional stronger model override only for workflows proven by evals to benefit materially;
- no complex multi-agent swarm architecture in V1.

Multi-model routing becomes justified only by measured quality/cost/latency evidence.

## AI Evals

Every high-impact AI module requires representative eval cases.

Minimum categories:

- no fabricated experience/credentials/results;
- evidence citation/provenance preservation;
- maturity reasoning consistency;
- profile-platform adaptation;
- opportunity fit vs missing evidence;
- proposal tailoring;
- pricing benchmark uncertainty;
- negotiation commitment boundary;
- prompt-injection handling;
- current-information escalation;
- draft vs executed-state distinction.

Eval data must avoid unnecessary real client/private data; synthetic or consented/redacted examples are preferred.

## Run Metadata

Persist safe metadata such as:

- provider;
- model;
- request/run ID if safe/useful;
- module/prompt version;
- latency;
- usage/token counts where available;
- success/failure class;
- input/output artifact references;
- validation result.

Do not persist hidden chain-of-thought. Do not log full sensitive prompts by default.

## Cost Controls

Architecture controls cost by:

- limiting context to relevant evidence;
- avoiding unnecessary agent loops;
- using deterministic code where appropriate;
- caching/reusing stable derived artifacts where valid;
- invalidating derived artifacts when source evidence changes;
- separating paid current-source/eval runs from ordinary unit tests;
- recording provider usage metadata where available.

No revenue or operating-cost target is claimed yet.

## Portability Requirement

A second provider adapter should be possible without changing:

- Pydantic domain contracts;
- module IDs;
- approval state machine;
- persistence schemas except provider metadata;
- business workflow semantics.

Provider-specific capabilities may be optional adapter features, but modules must degrade explicitly if a required feature is unavailable.
