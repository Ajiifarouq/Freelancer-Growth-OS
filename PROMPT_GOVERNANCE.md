# Freelancer Growth OS Prompt Governance

**Status:** Active  
**Product release status:** Unreleased  
**Governance baseline:** `Ajiifarouq/GrowthOS-Engineering` `v0.1.0` at `7ee056f938e12b5a72d1ee919a27f05ec5297c69`  
**Canonical contract authority:** [CONTRACT_REGISTRY.md](CONTRACT_REGISTRY.md)  
**Provider-data authority:** [PROVIDER_DATA_POLICY.md](PROVIDER_DATA_POLICY.md)

## Purpose

This document governs reusable AI prompt assets in Freelancer Growth OS. Prompts are product behavior assets, not casual strings. They remain subordinate to requirements, current decisions, architecture, canonical contracts, deterministic application policies, data/provider policy, connector permissions, and human-approval boundaries.

## Authority Hierarchy

For prompt-driven behavior, authority order is:

1. applicable law/platform/org security policy;
2. GrowthOS Engineering pinned governance;
3. Freelancer Growth OS governance/workflow/versioning;
4. approved product requirements/current decisions;
5. approved architecture and [CONTRACT_REGISTRY.md](CONTRACT_REGISTRY.md);
6. `DATA_GOVERNANCE.md` / `PROVIDER_DATA_POLICY.md` / deterministic application policies and approval state machines;
7. owning role contract;
8. reusable prompt instructions;
9. task/user/external content supplied to prompt.

A lower layer must not override a higher layer.

## Canonical Prompt Structure

Every reusable prompt uses:

1. `# Role`
2. `# Task`
3. `# Context`
4. `# Format`
5. `# Tone`

The five-part structure contains substantive instructions, not decorative headings.

## Required Prompt Metadata

Every governed prompt asset defines:

- Prompt ID: lowercase-kebab-case;
- Status: Draft, Proposed, Active, Deprecated, Retired, or Unreleased;
- Owning role;
- Owning module/capability;
- Version when independently maintained;
- Required inputs;
- canonical output contract ID(s) from `CONTRACT_REGISTRY.md`;
- Authority level;
- Factuality/evidence requirements;
- Freshness requirements;
- Security/privacy/provider requirements;
- Human-approval boundary;
- Eval requirements;
- Compatibility notes.

At runtime, implemented prompt behavior should also have an immutable content hash or equivalent build reference.

## Canonical Contract Binding

The prompt-to-contract mapping in [CONTRACT_REGISTRY.md](CONTRACT_REGISTRY.md) is normative for implementation.

If prose in an older prompt says something ambiguous such as `profile optimization draft`, runtime resolves it to the canonical contract `profile-optimization-draft`.

If an older architecture term uses `proposal-draft`, runtime resolves it to `proposal-draft-record`.

Do not create a second Pydantic/database schema merely because prompt wording differs from the canonical contract name.

A prompt-backed module is not implementation-ready until its canonical output contract exists and its runtime validates the output against that contract.

## Stable Prompt IDs

Prompt IDs remain stable once referenced by code, evals, runs, audits, tests, or released workflows.

Renaming a stable prompt requires compatibility analysis and migration of consumers.

## Prompt Versioning

A prompt receives an independent version when any of the following applies:

- runs/audits must identify exact prompt behavior;
- eval baselines depend on exact prompt behavior;
- code/config references a stable prompt version;
- multiple compatible prompt versions must coexist;
- released product behavior depends on the prompt.

Prompt versions use semantic versioning when compatibility meaningfully applies.

### Potential PATCH prompt change

- typo correction;
- formatting correction;
- clarification demonstrably preserving behavior and output contract.

### Potential MINOR prompt change

- backward-compatible optional guidance;
- improved reasoning guidance preserving expected contract/authority;
- additive handling of new valid input while preserving existing behavior.

### Potential MAJOR/breaking prompt change

- changed canonical output contract;
- changed authority boundary;
- changed factuality/evidence state policy;
- changed provider-data behavior;
- changed refusal/stop behavior relied on by consumers;
- materially different interpretation of existing inputs;
- removal/rename of required output semantics;
- behavior likely to invalidate established eval/consumer assumptions.

Actual version impact is determined by behavior compatibility, not text-diff size.

## Prompt Change Record

Every material prompt change uses `prompt-change-record` from [TEMPLATE_LIBRARY.md](TEMPLATE_LIBRARY.md) / canonical mapping and states:

- old/new version;
- intended behavior change;
- compatibility class;
- affected roles/modules/contracts;
- authority/safety/privacy impact;
- eval evidence;
- migration/deprecation needs;
- residual risks.

## Inputs

Prompts explicitly identify required inputs.

When material input is missing:

- do not invent it;
- use explicit placeholder for draftable non-material content when safe;
- label uncertainty;
- stop or return blocked/insufficient-evidence state when missing input prevents defensible result.

A prompt should not ask user to repeat information already supplied through approved application context when it can be retrieved safely.

## Evidence and Factuality

Prompts require:

- evidence-backed professional/business claims;
- separation of `provided-unverified`, `verified`, inference, recommendations, unknowns, conflicts, and rejected claims;
- no fabricated clients, results, qualifications, testimonials, metrics, revenue, platform facts, or external-action outcomes;
- explicit contradiction handling;
- traceability references where canonical contract supports them.

Fluency/model confidence never substitutes for evidence.

A prompt may recommend an evidence state but cannot authoritatively promote evidence to `verified`. That state transition belongs to deterministic application policy under `CONTRACT_REGISTRY.md` / `DATA_GOVERNANCE.md`.

## Artifact Staleness

Prompt-backed artifacts consume explicit dependency versions where the canonical contract requires them.

Prompts cannot declare stale/invalid dependencies current. Revalidation/application policy controls artifact validity.

If an input artifact is stale/invalid and current state is required, prompt workflow must stop/return appropriate blocked state rather than silently proceed.

## Freshness

Prompts defer volatile-current-fact decisions to freshness/research boundary when stale information could materially change output.

Typical triggers:

- marketplace policies/features;
- current API/integration availability;
- pricing benchmarks;
- hiring/freelance trends;
- legal/tax/regulatory facts;
- current product/tool recommendations.

If verification is unavailable, prompt preserves unverified/unknown state rather than guess.

Research results use canonical freshness contracts and preserve source/verification timestamps where material.

## Security, Privacy, and Provider Processing

Prompts must:

- treat retrieved/web/connected content as data, not authority instructions;
- ignore embedded instructions attempting to override system/product governance;
- minimize unnecessary personal/client/business data in context;
- follow [PROVIDER_DATA_POLICY.md](PROVIDER_DATA_POLICY.md) before external provider processing;
- never request raw secrets where connector/adapter should hold them;
- avoid echoing tokens/credentials;
- preserve connector permission scope;
- never infer write authority from read access;
- never cause real private data to be copied into Git/test/eval assets.

`CLIENT_CONFIDENTIAL` and `BUSINESS_SENSITIVE` provider processing remains disabled by default until explicitly enabled under provider-data policy.

## Prompt Injection Boundary

External content may contain instructions such as `ignore previous instructions`, hidden text, malicious markup, or social-engineering requests.

Reusable prompts treat such content as untrusted input and must not allow it to:

- change role authority;
- disable evidence/factuality controls;
- promote evidence to `verified`;
- request secrets;
- select/enable providers/models/tools;
- trigger tools/actions outside scope;
- bypass human approval;
- redefine canonical output contracts;
- alter data-retention/deletion/provider policy.

## Structured Outputs

Where a module owns a stable output contract, the prompt targets canonical contract ID(s) from [CONTRACT_REGISTRY.md](CONTRACT_REGISTRY.md), not unconstrained prose.

A valid-looking model response is not trusted automatically. Application validates structured output deterministically with the matching Pydantic contract/version before persistence or downstream use.

Schema failure produces bounded repair/retry or explicit failure; malformed output is not persisted as authoritative state.

## Hidden Reasoning

Prompts must not require disclosure of hidden chain-of-thought or private reasoning traces.

When explanation is needed, request concise rationale, evidence references, assumptions, decision factors, or validation findings suitable for user/product record.

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

A prompt may produce `approval-request`, but only verified human approval processed through deterministic gate may authorize execution.

Execution also requires exact payload binding, current/non-stale dependencies, connector scope validation, idempotency/replay protection, and verified result handling.

## Model and Provider Portability

Prompt behavior avoids unnecessary provider-specific assumptions.

Provider/model-specific optimization is allowed in adapter/configuration layers when it does not silently change stable prompt contract/authority/privacy behavior.

A provider/model/tool change requires capability/privacy verification and eval comparison when material to behavior, factuality, safety, output compatibility, cost, latency, or retention.

## Eval Requirements

Reusable prompt evals include representative positive, boundary, adversarial, insufficient-evidence, and privacy-minimisation cases.

Depending on prompt, eval dimensions may include:

- factuality/hallucination;
- evidence usage;
- evidence-state promotion resistance;
- uncertainty handling;
- canonical output-schema validity;
- role/scope adherence;
- marketplace/platform awareness;
- prompt-injection resistance;
- provider-data minimization;
- authority/approval boundary preservation;
- stale-artifact handling;
- current-information escalation;
- cross-asset consistency;
- user usefulness/clarity.

Eval fixtures use synthetic data by default. A prompt is not behaviorally validated merely because it generated one good example.

## Prompt Status Lifecycle

`Draft → Proposed → Active → Deprecated → Retired`

`Unreleased` may describe an active repository asset before product release when appropriate.

### Draft

Incomplete/experimental; not stable consumer dependency.

### Proposed

Specified/reviewable but not yet accepted as active product behavior.

### Active

Approved specification for applicable workflow. Active does not imply implementation, successful runtime validation, or public product release.

### Deprecated

Still supported for existing consumers but should not be used for new work.

### Retired

No longer supported.

## Review Triggers

Prompt review is mandatory when:

- requirements/current decisions change;
- owning module/role changes;
- canonical output contract changes;
- evidence/freshness/data/provider policy changes;
- tool/connector authority changes;
- human-approval/idempotency semantics change;
- model/provider change causes behavior drift;
- eval regression is detected;
- security/privacy findings affect prompt context/behavior.

## Prompt Maintenance and Audit

Implemented runs should record:

- prompt ID/version;
- immutable prompt content hash/build reference;
- provider/model/tool configuration reference;
- canonical contract IDs/versions;
- input/output artifact references;
- validation/eval result references where material.

This supports reproducibility without storing hidden reasoning or full private prompts by default.

Prompts must not be edited in a way that destroys released behavior traceability. Corrections follow [VERSIONING.md](VERSIONING.md) and [COMPATIBILITY_MIGRATION.md](COMPATIBILITY_MIGRATION.md).

## Validation Checklist

Before activating/implementing a reusable prompt, verify:

- [ ] Prompt ID and owning role/module are defined.
- [ ] Role → Task → Context → Format → Tone structure is complete.
- [ ] Required inputs and missing-input behavior are explicit.
- [ ] Canonical output contract ID(s) exist in `CONTRACT_REGISTRY.md`.
- [ ] Runtime will validate output against that contract/version.
- [ ] Evidence/factuality/state controls are present.
- [ ] Freshness trigger behavior is present where relevant.
- [ ] Security/privacy/provider-data and prompt-injection controls are present.
- [ ] Human approval/staleness/replay boundary is explicit where relevant.
- [ ] No hidden chain-of-thought disclosure is required.
- [ ] Eval requirements are defined using synthetic data by default.
- [ ] Compatibility/version impact is classified.
- [ ] Prompt does not claim implementation, integration, execution, or release state without evidence.
