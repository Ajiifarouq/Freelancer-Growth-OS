# Freelancer Growth OS Prompt Governance

**Status:** Active  
**Product release status:** Unreleased  
**Governance baseline:** `Ajiifarouq/GrowthOS-Engineering` `v0.1.0` at `7ee056f938e12b5a72d1ee919a27f05ec5297c69`

## Purpose

This document governs reusable AI prompt assets in Freelancer Growth OS. Prompts are product behavior assets, not casual strings. They must remain subordinate to requirements, architecture, module contracts, deterministic application policies, connector permissions, and human-approval boundaries.

## Authority Hierarchy

For prompt-driven behavior, authority order is:

1. applicable law/platform/org security policy;
2. GrowthOS Engineering pinned governance;
3. Freelancer Growth OS governance/workflow/versioning;
4. approved product requirements;
5. approved architecture/module contracts;
6. deterministic application policies and approval state machines;
7. owning role contract;
8. reusable prompt instructions;
9. task/user content supplied to the prompt.

A lower layer must not override a higher layer.

## Canonical Prompt Structure

Every reusable prompt must use:

1. `# Role`
2. `# Task`
3. `# Context`
4. `# Format`
5. `# Tone`

The five-part structure must contain substantive instructions, not decorative headings.

## Required Prompt Metadata

Every governed prompt asset must define:

- Prompt ID: lowercase-kebab-case;
- Status: Draft, Proposed, Active, Deprecated, Retired, or Unreleased;
- Owning role;
- Owning module/capability;
- Version when independently maintained;
- Required inputs;
- Output contract/template;
- Authority level;
- Factuality requirements;
- Freshness requirements;
- Security/privacy requirements;
- Human-approval boundary;
- Eval requirements;
- Compatibility notes.

## Stable Prompt IDs

Prompt IDs should remain stable once referenced by code, evals, runs, audits, tests, or released workflows.

Renaming a stable prompt requires compatibility analysis and migration of consumers.

## Prompt Versioning

A prompt receives an independent version when any of the following applies:

- runs/audits must identify exact prompt behavior;
- eval baselines depend on exact prompt behavior;
- code/config references a stable prompt version;
- multiple compatible prompt versions must coexist;
- released product behavior depends on the prompt.

Prompt versions should use semantic versioning when compatibility meaningfully applies.

### Potential PATCH prompt change

- typo correction;
- formatting correction;
- clarification demonstrably preserving behavior and output contract.

### Potential MINOR prompt change

- backward-compatible optional guidance;
- improved reasoning guidance preserving expected contract/authority;
- additive handling of new valid input while preserving existing behavior.

### Potential MAJOR/breaking prompt change

- changed output contract;
- changed authority boundary;
- changed factuality/evidence policy;
- changed refusal/stop behavior relied on by consumers;
- materially different interpretation of existing inputs;
- removal/rename of required output semantics;
- behavior likely to invalidate established eval/consumer assumptions.

Actual version impact is determined by behavior compatibility, not text-diff size.

## Prompt Change Record

Every material prompt change should use the `prompt-change-record` template from [TEMPLATE_LIBRARY.md](TEMPLATE_LIBRARY.md) and state:

- old/new version;
- intended behavior change;
- compatibility class;
- affected roles/modules/contracts;
- authority/safety impact;
- eval evidence;
- migration/deprecation needs;
- residual risks.

## Inputs

Prompts must explicitly identify required inputs.

When material input is missing:

- do not invent it;
- use an explicit placeholder for draftable non-material content when safe;
- label uncertainty;
- stop or return a blocked/insufficient-evidence state when the missing input prevents a defensible result.

A prompt should not ask the user to repeat information already supplied through the active workflow when it can be retrieved from the approved application context.

## Evidence and Factuality

Prompts must require:

- evidence-backed professional/business claims;
- separation of facts, inference, recommendations, unknowns, and rejected claims;
- no fabricated clients, results, qualifications, testimonials, metrics, revenue, platform facts, or external-action outcomes;
- explicit contradiction handling;
- traceability references where the consuming contract supports them.

Fluency must never substitute for evidence.

## Freshness

Prompts must defer volatile-current-fact decisions to the freshness/research boundary when stale information could materially change the output.

Typical triggers:

- marketplace policies/features;
- current API/integration availability;
- pricing benchmarks;
- hiring/freelance trends;
- legal/tax/regulatory facts;
- current product/tool recommendations.

If verification is unavailable, the prompt must preserve an unverified/unknown state rather than guess.

## Security and Privacy

Prompts must:

- treat retrieved/web/connected content as data, not authority instructions;
- ignore embedded instructions that attempt to override system/product governance;
- minimize unnecessary personal/client/business data in context;
- never request raw secrets where a connector/adapter should hold them;
- avoid echoing tokens/credentials;
- preserve connector permission scope;
- never infer write authority from read access.

## Prompt Injection Boundary

External content may contain instructions such as “ignore previous instructions,” hidden text, malicious markup, or social-engineering requests.

Reusable prompts must treat such content as untrusted input and must not allow it to:

- change role authority;
- disable evidence/factuality controls;
- request secrets;
- trigger tools/actions outside scope;
- bypass human approval;
- redefine output contracts.

## Structured Outputs

Where a module owns a stable output contract, the prompt must target that contract/template rather than unconstrained prose.

A valid-looking model response is not automatically trusted. The application must validate structured output deterministically.

## Hidden Reasoning

Prompts must not require disclosure of hidden chain-of-thought or private reasoning traces.

When explanation is needed, request concise rationale, evidence references, assumptions, decision factors, or validation findings suitable for the user/product record.

## Human Approval

Prompt text cannot grant consequential-action authority.

The following remain application/governance controlled:

- submitting proposals/applications;
- sending client messages;
- publishing/modifying profiles;
- accepting pricing/terms;
- modifying connected accounts;
- irreversible/deletion actions;
- protected Git/release actions.

A prompt may produce an `approval-request`, but only verified human approval processed through the deterministic gate may authorize execution.

## Model and Provider Portability

Prompt behavior should avoid unnecessary provider-specific assumptions.

Provider/model-specific optimization is allowed in adapter/configuration layers when it does not change the stable prompt contract silently.

A provider/model change requires eval comparison when material to behavior, factuality, safety, output compatibility, cost, or latency.

## Eval Requirements

Reusable prompt evals should include representative positive, boundary, adversarial, and insufficient-evidence cases.

Depending on the prompt, eval dimensions may include:

- factuality/hallucination;
- evidence usage;
- uncertainty handling;
- output-schema validity;
- role/scope adherence;
- marketplace/platform awareness;
- prompt-injection resistance;
- authority/approval boundary preservation;
- current-information escalation;
- cross-asset consistency;
- user usefulness and clarity.

A prompt must not be marked behaviorally validated solely because it generated one good example.

## Prompt Status Lifecycle

`Draft → Proposed → Active → Deprecated → Retired`

`Unreleased` may describe an active repository asset before the product itself is released when appropriate.

### Draft

Incomplete or experimental; not a stable consumer dependency.

### Proposed

Specified and reviewable, but not yet accepted as active product behavior.

### Active

Approved for the applicable product workflow. Active does not imply public product release.

### Deprecated

Still supported for existing consumers but should not be used for new work.

### Retired

No longer supported.

## Review Triggers

Prompt review is mandatory when:

- requirements change;
- owning module/role changes;
- output contract changes;
- evidence/freshness policy changes;
- tool/connector authority changes;
- human-approval semantics change;
- model/provider change causes behavior drift;
- eval regression is detected;
- security/privacy findings affect prompt context or behavior.

## Prompt Maintenance and Audit

For implemented runs, the architecture should record prompt ID/version and model/provider metadata where practical so behavior can be reproduced and audited without storing hidden reasoning.

Prompts must not be edited in a way that destroys released behavior traceability. Corrections should follow [VERSIONING.md](VERSIONING.md) and [COMPATIBILITY_MIGRATION.md](COMPATIBILITY_MIGRATION.md).

## Validation Checklist

Before activating a reusable prompt, verify:

- [ ] Prompt ID and owning role/module are defined.
- [ ] Role → Task → Context → Format → Tone structure is complete.
- [ ] Required inputs and missing-input behavior are explicit.
- [ ] Output contract/template is explicit.
- [ ] Evidence/factuality controls are present.
- [ ] Freshness trigger behavior is present where relevant.
- [ ] Security/privacy and prompt-injection controls are present.
- [ ] Human approval boundary is explicit.
- [ ] No hidden chain-of-thought disclosure is required.
- [ ] Eval requirements are defined.
- [ ] Compatibility/version impact is classified.
- [ ] Prompt does not claim implementation, integration, execution, or release state without evidence.