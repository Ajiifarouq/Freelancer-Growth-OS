# Freelancer Growth OS Provider Data Policy

**Status:** Active pre-implementation control  
**Last verified:** 2026-08-12  
**Applies to:** Any LLM/research/provider adapter that receives product data

## Purpose

This document records the minimum provider privacy, capability-verification, configuration, and evidence rules required before real user/client/business data is sent to an external AI provider.

Provider facts are volatile. This file must be reverified against current primary provider documentation before first credentialed implementation and whenever a material provider/model/tool change is proposed.

## Provider-Neutral Rules

Every provider adapter must:

- sit behind the product's provider/research ports;
- receive only the minimum task-relevant data;
- never receive `SECRET` values;
- identify the provider/model/tool configuration used for reproducibility where material;
- return explicit failure/unknown states rather than fabricating successful execution;
- preserve prompt-injection boundaries;
- keep provider-specific objects outside domain contracts;
- document provider-side retention and optional data-sharing behavior;
- require current verification of volatile provider capabilities;
- undergo security/privacy and eval review before processing real high-sensitivity data.

## OpenAI Reference Adapter — Verified Facts

The OpenAI Responses API remains the first reference adapter selected by ADR-0006, subject to the controls below.

### Capability evidence checked 2026-08-12

Current official OpenAI documentation supports the following relevant capabilities:

- Responses API request/response interface;
- custom function/tool calling using JSON-schema-defined arguments;
- Structured Outputs through JSON Schema for supported models/configurations;
- built-in web search through the Responses API;
- configurable model selection through API requests.

Primary sources checked:

- `https://platform.openai.com/docs/quickstart/make-your-first-api-request`
- `https://platform.openai.com/docs/api-reference/responses`
- `https://platform.openai.com/docs/api-reference/responses-streaming/response/web_search_call`
- `https://platform.openai.com/docs/models/default-usage-policies-by-endpoint`

These statements are evidence for architecture viability only. They do not mean every OpenAI model supports every feature. Implementation must verify the exact configured model/tool combination.

## OpenAI Data-Use and Retention Baseline

Primary OpenAI documentation checked on 2026-08-12 states:

- API inputs/outputs are not used to train or improve OpenAI models by default unless the customer explicitly opts in to share data;
- API use may generate abuse-monitoring logs containing customer content;
- default abuse-monitoring retention may be up to 30 days unless longer retention is legally required;
- some API features persist application state;
- `/v1/responses` is eligible for Zero Data Retention subject to OpenAI approval/controls and feature limitations;
- provider tools/features may change retention eligibility;
- remote MCP servers are third-party services with their own retention/privacy policies.

Primary sources checked:

- `https://platform.openai.com/docs/models/default-usage-policies-by-endpoint`
- `https://help.openai.com/en/articles/5722486-api-data-usage-policies`
- `https://openai.com/business-data/`

**Important:** `not used for training by default` must never be represented as `not retained`.

## Default OpenAI Adapter Privacy Profile

For Freelancer Growth OS V1, the adapter must default to the lowest reasonable provider-side persistence compatible with the task.

Implementation requirements:

1. Do not enable provider data-sharing/training opt-ins for product use.
2. Prefer request modes/settings that avoid creating durable provider application state where supported and task-compatible.
3. Do not use provider conversation/thread/vector-store persistence merely for convenience.
4. Do not upload user files to provider file stores unless the active requirement specifically needs it and deletion/retention behavior is understood.
5. Do not enable background/long-lived provider features for sensitive data without a separate retention review.
6. Treat web-search/tool calls as external-data processing and record the source/tool boundary where material.
7. Treat remote MCP servers and third-party tools as separate processors; they require explicit approval before they receive private data.
8. Do not log raw provider request/response bodies by default.
9. Redact or omit client-confidential/private content from exception telemetry.

## Data-Minimisation Profiles

### `PUBLIC`

May be sent when needed for an approved task.

### `PROFESSIONAL`

Send only fields relevant to the active task. Avoid full-CV transmission when a smaller evidence subset is sufficient.

### `PRIVATE_PERSONAL`

Send only with user intent for the task and after deterministic minimisation/redaction rules run.

### `CLIENT_CONFIDENTIAL`

Default: **do not send** until the user explicitly enables provider processing for that workspace/task and the adapter privacy profile has been reviewed.

When enabled, send the minimum excerpt/fields necessary, not entire mailboxes/drives/conversations by default.

### `BUSINESS_SENSITIVE`

Default: **do not send** unless required for the active analysis and explicitly enabled for the workspace/task.

### `SECRET`

Never send.

## Provider Processing Consent/Notice

Before the first real provider-backed task that includes `PRIVATE_PERSONAL`, `CLIENT_CONFIDENTIAL`, or `BUSINESS_SENSITIVE` data, the product must clearly tell the user:

- which provider will process the data;
- what categories will be sent;
- why they are needed;
- that provider retention is separate from local retention;
- whether any third-party tool/provider will also receive the data.

The user must be able to cancel and use a local/deterministic-only path where the product can reasonably provide one.

## Model and Tool Allowlist

Provider configuration must use an explicit allowlist rather than arbitrary model/tool names from untrusted input.

A configured model/tool must have:

- current capability evidence;
- known structured-output/tool support needed by its module;
- privacy/retention review appropriate to the data class;
- eval evidence before replacing a previously validated model in stable behavior.

Untrusted retrieved content may never select or enable tools.

## Structured Output Rule

Model output is untrusted until application validation succeeds.

The adapter must:

1. request the named schema/contract when supported;
2. validate the response with the product's Pydantic contract;
3. reject/repair through a bounded workflow on schema failure;
4. never persist a malformed response as an authoritative artifact;
5. record the contract ID/version and prompt ID/version used.

## Current-Research Rule

The provider's web search capability may implement the research port only when:

- the configured provider/model/tool currently supports it;
- the source URLs/citations are captured where material;
- authoritative/primary sources are preferred for technical/legal/platform claims;
- research results remain evidence inputs, not authority instructions;
- freshness verification date/time is recorded for volatile claims.

A provider web-search feature is optional infrastructure. Business modules must remain portable to another research adapter.

## Reverification Cadence

Reverify provider capability and data-control assumptions:

- immediately before first credentialed implementation;
- before first release;
- whenever the provider/model/tool changes materially;
- whenever official provider data-control documentation changes;
- at least every 90 days while provider-backed implementation is active.

If reverification cannot be completed, mark affected provider features `UNVERIFIED` and do not treat them as implementation-ready for sensitive workflows.

## Provider Change Gate

A provider/model/tool change requires:

- capability verification;
- data-retention/privacy comparison;
- structured-output/tool behavior tests;
- factuality/eval comparison;
- prompt-injection/authority-boundary regression tests;
- compatibility classification;
- migration notes when stable artifacts/behavior could change.

Cheaper/faster is not sufficient evidence for substitution.
