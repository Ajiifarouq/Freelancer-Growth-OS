# Freelancer Growth OS Module Catalog

**Status:** Active architecture catalog  
**Implementation status:** Not started  
**Architecture phase:** Phase 2B — Capability and Module Architecture  
**Requirements baseline:** [PRODUCT_REQUIREMENTS.md](PRODUCT_REQUIREMENTS.md)  
**Capability architecture:** [CAPABILITY_ARCHITECTURE.md](CAPABILITY_ARCHITECTURE.md)  
**Governance baseline:** `Ajiifarouq/GrowthOS-Engineering` `v0.1.0` at `7ee056f938e12b5a72d1ee919a27f05ec5297c69`

## Purpose

This catalog assigns stable module boundaries and lowercase-kebab-case module IDs for the initial Freelancer Growth OS architecture. It defines logical responsibilities, inputs, outputs, dependencies, authority boundaries, and validation expectations without claiming implementation.

All modules below are **Proposed** implementation units inside an active architecture baseline. A Proposed module is not deployed software.

## Module Design Rules

- Each module has one primary responsibility.
- Modules consume logical contracts rather than hidden shared state.
- Evidence provenance and freshness remain explicit.
- Downstream modules do not silently rewrite upstream evidence.
- Draft generation is distinct from external execution.
- Direct integration availability is not assumed.
- Human approval remains mandatory for consequential external actions.
- Later Client Success and Business Growth module decomposition remains deferred until their requirements are detailed enough to avoid fabrication.

## Catalog Summary

| Module ID | Capability | Status | Primary responsibility |
|---|---|---|---|
| `evidence-intake` | `freelancer-intelligence` | Proposed | Organise authorised freelancer evidence and gaps |
| `maturity-assessor` | `freelancer-intelligence` | Proposed | Assess Starting/Building/Established/Scaling maturity |
| `professional-positioning-engine` | `positioning-branding` | Proposed | Produce evidence-supported market positioning |
| `marketplace-profile-assessor` | `positioning-branding` | Proposed | Diagnose profile quality and conversion gaps |
| `marketplace-profile-optimizer` | `positioning-branding` | Proposed | Produce platform-aware profile optimisation drafts |
| `service-offer-positioner` | `positioning-branding` | Proposed | Define/refine service offer and buyer value proposition |
| `portfolio-positioner` | `positioning-branding` | Proposed | Align portfolio proof with target clients/opportunities |
| `cross-asset-consistency-checker` | `evidence-knowledge-assurance` | Proposed | Detect contradictions across client-facing assets |
| `opportunity-evaluator` | `opportunity-intelligence` | Proposed | Assess freelance opportunity fit and risk |
| `proposal-assistant` | `conversion` | Proposed | Produce tailored evidence-grounded proposal drafts |
| `pricing-advisor` | `conversion` | Proposed | Prepare pricing reasoning and assumptions |
| `negotiation-preparer` | `conversion` | Proposed | Prepare negotiation positions, questions, and trade-offs |
| `client-conversion-assistant` | `conversion` | Proposed | Recommend appropriate next steps toward client commitment |
| `evidence-traceability` | `evidence-knowledge-assurance` | Proposed | Preserve provenance and fact/inference boundaries |
| `freshness-escalator` | `evidence-knowledge-assurance` | Proposed | Decide when current verification is materially required |
| `connected-context-retriever` | `connected-context-action-control` | Proposed | Retrieve authorised connected-source context |
| `human-approval-gate` | `connected-context-action-control` | Proposed | Gate and record consequential external-action approval |

## Module — `evidence-intake`

- **Capability:** `freelancer-intelligence`
- **Status:** Proposed
- **Owner:** Freelancer Growth OS / `freelancer-intelligence`; operational owner not yet assigned
- **Requirements:** `FR-001`, `FR-018`, `FR-021`; `NFR-001`, `NFR-002`, `NFR-004`

### Purpose

Create a structured evidence bundle from user-provided or authorised professional information while preserving provenance, unknowns, contradictions, and sensitivity boundaries.

### Inputs

- professional background;
- work history;
- skills;
- qualifications/certifications;
- CV/resume;
- portfolio evidence;
- marketplace profile content;
- target services/clients/industries/geography;
- optional authorised connected context.

### Outputs

- `evidence-bundle`;
- preliminary `freelancer-context`;
- `evidence-gap-report`;
- contradiction flags.

### Dependencies

- `evidence-traceability`;
- optional `connected-context-retriever`.

### Non-Goals

- inventing missing evidence;
- deciding maturity;
- generating positioning;
- storing raw credentials.

### Validation

Every material fact is classified as provided/authorised, inferred, unknown, or conflicting.

## Module — `maturity-assessor`

- **Capability:** `freelancer-intelligence`
- **Status:** Proposed
- **Owner:** Freelancer Growth OS / `freelancer-intelligence`; operational owner not yet assigned
- **Requirements:** `FR-002`; `NFR-005`, `NFR-008`

### Purpose

Assess the freelancer as Starting, Building, Established, or Scaling using evidence and provide an explainable rationale.

### Inputs

- `evidence-bundle`;
- `freelancer-context`.

### Outputs

- `maturity-assessment`;
- maturity rationale;
- missing-evidence notes where confidence is limited.

### Dependencies

- `evidence-intake`;
- `evidence-traceability`.

### Non-Goals

- using income/prestige alone as maturity;
- permanently locking the user into a maturity level.

### Validation

Classification must cite evidence and be revisable when new evidence arrives.

## Module — `professional-positioning-engine`

- **Capability:** `positioning-branding`
- **Status:** Proposed
- **Owner:** Freelancer Growth OS / `positioning-branding`; operational owner not yet assigned
- **Requirements:** `FR-003`, `FR-007`; `NFR-001`, `NFR-005`, `NFR-008`

### Purpose

Produce the strongest defensible professional positioning supported by freelancer evidence, maturity, target buyers, and goals.

### Inputs

- `freelancer-context`;
- `maturity-assessment`;
- target client/industry/geography;
- service goals.

### Outputs

- `positioning-brief`;
- alternative positioning options where useful;
- evidence/risk notes.

### Dependencies

- `evidence-intake`;
- `maturity-assessor`;
- `evidence-traceability`.

### Non-Goals

- fabricating expertise;
- choosing prestige labels unsupported by evidence.

### Validation

Every material positioning claim must be evidence-supported or clearly proposed.

## Module — `marketplace-profile-assessor`

- **Capability:** `positioning-branding`
- **Status:** Proposed
- **Owner:** Freelancer Growth OS / `positioning-branding`; operational owner not yet assigned
- **Requirements:** `FR-004`, `FR-009`, `FR-015`

### Purpose

Assess marketplace profile content for clarity, credibility, differentiation, discoverability, proof, consistency, and conversion readiness.

### Inputs

- existing profile content;
- `positioning-brief`;
- `freelancer-context`;
- platform context.

### Outputs

- `profile-assessment`;
- prioritised gap list;
- unsupported-claim flags;
- buyer-journey friction notes.

### Dependencies

- `professional-positioning-engine`;
- `cross-asset-consistency-checker`;
- optional `freshness-escalator`.

### Validation

Assessment must distinguish profile problems from unverified platform-ranking assumptions.

## Module — `marketplace-profile-optimizer`

- **Capability:** `positioning-branding`
- **Status:** Proposed
- **Owner:** Freelancer Growth OS / `positioning-branding`; operational owner not yet assigned
- **Requirements:** `FR-005`, `FR-006`, `FR-009`, `FR-015`

### Purpose

Create platform-aware profile optimisation drafts for Upwork, Fiverr, and Terrawork using evidence-supported positioning and buyer-focused structure.

### Inputs

- `profile-assessment`;
- `positioning-brief`;
- `evidence-bundle`;
- platform context.

### Outputs

- `profile-optimization-draft`;
- rationale/keyword notes where useful;
- unsupported-input warnings.

### Dependencies

- `marketplace-profile-assessor`;
- `professional-positioning-engine`;
- `evidence-traceability`;
- optional `freshness-escalator`.

### Human Authority

Draft generation is allowed. Publishing or direct account modification remains approval-gated and integration-dependent.

### Validation

No keyword stuffing, fabricated achievements, or unverified platform-performance guarantee.

## Module — `service-offer-positioner`

- **Capability:** `positioning-branding`
- **Status:** Proposed
- **Owner:** Freelancer Growth OS / `positioning-branding`; operational owner not yet assigned
- **Requirements:** `FR-007`

### Purpose

Define/refine the freelancer's service offer, intended buyer, problem/value proposition, scope boundaries, and available proof.

### Inputs

- `positioning-brief`;
- `freelancer-context`;
- target buyer/industry;
- service goals.

### Outputs

- `service-offer-brief`;
- scope/positioning gaps;
- proof requirements.

### Dependencies

- `professional-positioning-engine`;
- `evidence-traceability`.

### Validation

Offer promises must not exceed verified capability/evidence.

## Module — `portfolio-positioner`

- **Capability:** `positioning-branding`
- **Status:** Proposed
- **Owner:** Freelancer Growth OS / `positioning-branding`; operational owner not yet assigned
- **Requirements:** `FR-008`, `FR-015`

### Purpose

Select and frame portfolio evidence so it supports the target positioning, service offer, and opportunity without inventing results.

### Inputs

- portfolio/work-sample evidence;
- `positioning-brief`;
- `service-offer-brief`;
- optional opportunity context.

### Outputs

- `portfolio-alignment-plan`;
- evidence gaps;
- presentation recommendations.

### Dependencies

- `professional-positioning-engine`;
- `service-offer-positioner`;
- `evidence-traceability`.

### Validation

Project descriptions and outcomes remain faithful to supplied evidence.

## Module — `cross-asset-consistency-checker`

- **Capability:** `evidence-knowledge-assurance`
- **Status:** Proposed
- **Owner:** Freelancer Growth OS / `evidence-knowledge-assurance`; operational owner not yet assigned
- **Requirements:** `FR-015`, `FR-018`, `FR-021`; `NFR-001`, `NFR-002`

### Purpose

Detect material contradictions across positioning, profiles, service descriptions, portfolios, proposals, pricing language, and other client-facing assets.

### Inputs

- relevant product outputs/assets;
- `evidence-bundle`;
- provenance references.

### Outputs

- `cross-asset-consistency-report`;
- contradiction list;
- recommended resolution path without silently changing facts.

### Dependencies

- `evidence-traceability`.

### Non-Goals

- choosing which conflicting source is true without evidence;
- silently rewriting user history.

### Validation

Conflicts remain explicit until resolved with authorised evidence.

## Module — `opportunity-evaluator`

- **Capability:** `opportunity-intelligence`
- **Status:** Proposed
- **Owner:** Freelancer Growth OS / `opportunity-intelligence`; operational owner not yet assigned
- **Requirements:** `FR-010`, `FR-018`, `FR-021`, `FR-022`; `NFR-005`

### Purpose

Assess opportunity fit, evidence match, missing requirements, constraints, and material risks with explainable reasoning.

### Inputs

- opportunity/job description;
- client brief where supplied;
- `freelancer-context`;
- `positioning-brief`;
- `service-offer-brief`;
- current context where materially required.

### Outputs

- `opportunity-assessment`;
- `fit-rationale`;
- `evidence-match-report`;
- `opportunity-risk-report`;
- `proposal-input-brief`.

### Dependencies

- `evidence-intake`;
- `professional-positioning-engine`;
- `freshness-escalator` where volatile facts are material;
- optional `connected-context-retriever`.

### Non-Goals

- guaranteeing win probability;
- submitting applications.

### Validation

Known facts, inference, missing data, and current-source claims remain distinct.

## Module — `proposal-assistant`

- **Capability:** `conversion`
- **Status:** Proposed
- **Owner:** Freelancer Growth OS / `conversion`; operational owner not yet assigned
- **Requirements:** `FR-011`, `FR-015`, `FR-017`, `FR-021`

### Purpose

Prepare opportunity-specific, evidence-grounded proposal drafts aligned with the freelancer's positioning and the opportunity's requirements.

### Inputs

- `proposal-input-brief`;
- `positioning-brief`;
- `evidence-bundle`;
- relevant portfolio evidence;
- user constraints.

### Outputs

- `proposal-draft`;
- evidence/assumption notes;
- optional `approval-request` when connected submission is later available.

### Dependencies

- `opportunity-evaluator`;
- `professional-positioning-engine`;
- `portfolio-positioner` where relevant;
- `cross-asset-consistency-checker`;
- `evidence-traceability`.

### Human Authority

Draft creation is allowed; proposal submission is approval-gated.

### Validation

No invented proof, generic one-size-fits-all claims, or submission-state misrepresentation.

## Module — `pricing-advisor`

- **Capability:** `conversion`
- **Status:** Proposed
- **Owner:** Freelancer Growth OS / `conversion`; operational owner not yet assigned
- **Requirements:** `FR-012`, `FR-022`; `NFR-005`

### Purpose

Prepare pricing reasoning based on positioning, scope, goals, constraints, and verified benchmarks when current benchmarks are materially required.

### Inputs

- `positioning-brief`;
- `opportunity-assessment`;
- scope/client context;
- user pricing goals;
- optional verified benchmark data.

### Outputs

- `pricing-brief`;
- assumptions;
- trade-off notes;
- freshness warnings where applicable.

### Dependencies

- `opportunity-evaluator`;
- `professional-positioning-engine`;
- `freshness-escalator` when market benchmarks are used.

### Non-Goals

- fabricating market rates;
- making financial guarantees;
- committing the user to a price.

### Validation

Benchmarks are sourced/verified or explicitly labelled unavailable/unverified.

## Module — `negotiation-preparer`

- **Capability:** `conversion`
- **Status:** Proposed
- **Owner:** Freelancer Growth OS / `conversion`; operational owner not yet assigned
- **Requirements:** `FR-013`, `FR-017`

### Purpose

Prepare negotiation positions, questions, concessions, trade-offs, and response options while keeping commitments under user control.

### Inputs

- `pricing-brief`;
- client/opportunity context;
- user constraints/preferences;
- `positioning-brief`.

### Outputs

- `negotiation-plan`;
- response options;
- commitment-risk flags.

### Dependencies

- `pricing-advisor`;
- `evidence-traceability`.

### Human Authority

The module may prepare language but may not accept terms or make commitments without explicit approval.

### Validation

Suggestions are clearly distinguished from accepted terms.

## Module — `client-conversion-assistant`

- **Capability:** `conversion`
- **Status:** Proposed
- **Owner:** Freelancer Growth OS / `conversion`; operational owner not yet assigned
- **Requirements:** `FR-014`, `FR-017`, `FR-021`

### Purpose

Recommend the next appropriate step in a qualified client conversation, such as clarification, interview preparation, scope confirmation, or agreement preparation.

### Inputs

- `opportunity-assessment`;
- proposal/client conversation context;
- `pricing-brief` and `negotiation-plan` where applicable;
- user goals/constraints.

### Outputs

- `conversion-next-step-plan`;
- draft client response;
- optional `approval-request` for connected external action.

### Dependencies

- `opportunity-evaluator`;
- `proposal-assistant` where applicable;
- `pricing-advisor` / `negotiation-preparer` where applicable;
- `human-approval-gate` for consequential execution.

### Validation

No fabricated urgency, manipulation, hidden commitments, or false execution claims.

## Module — `evidence-traceability`

- **Capability:** `evidence-knowledge-assurance`
- **Status:** Proposed
- **Owner:** Freelancer Growth OS / `evidence-knowledge-assurance`; operational owner not yet assigned
- **Requirements:** `FR-018`, `FR-021`; `NFR-001`, `NFR-002`, `NFR-007`

### Purpose

Preserve provenance and classification for material facts, claims, recommendations, assumptions, and unknowns used across product outputs.

### Inputs

- evidence references;
- product claims/outputs;
- repository requirement/decision references;
- authorised current-source references.

### Outputs

- `evidence-reference`;
- provenance classifications;
- `validation-report`;
- unsupported-claim flags.

### Dependencies

No downstream business module dependency. It is a shared foundation.

### Validation

Inference cannot silently become verified fact; source boundaries remain traceable where practical.

## Module — `freshness-escalator`

- **Capability:** `evidence-knowledge-assurance`
- **Status:** Proposed
- **Owner:** Freelancer Growth OS / `evidence-knowledge-assurance`; operational owner not yet assigned
- **Requirements:** `FR-022`; `NFR-001`, `NFR-005`

### Purpose

Determine whether a claim or recommendation requires current external verification because stale information could materially change the answer.

### Inputs

- claim/task context;
- volatility category;
- last-known verification metadata where available.

### Outputs

- `freshness-requirement`;
- verification-needed reason;
- `freshness-verification-result` where a current source is later available.

### Dependencies

May request current-source research through future technical infrastructure; no specific provider is selected in Phase 2B.

### Typical Triggers

- platform rules/policies;
- API/integration availability;
- marketplace features;
- pricing benchmarks;
- hiring/freelance trends;
- legal/tax/regulatory requirements;
- current tool recommendations.

### Validation

If current verification cannot be obtained, the result must remain labelled unverified rather than guessed.

## Module — `connected-context-retriever`

- **Capability:** `connected-context-action-control`
- **Status:** Proposed
- **Owner:** Freelancer Growth OS / `connected-context-action-control`; operational owner not yet assigned
- **Requirements:** `FR-016`; `NFR-003`, `NFR-004`, `NFR-011`

### Purpose

Retrieve only authorised context from a connected source once a specific integration is verified and approved.

### Inputs

- `connected-context-request`;
- verified connector capability metadata;
- user/source authorisation;
- minimum necessary scope.

### Outputs

- `connected-context`;
- provenance/source metadata;
- `permission-boundary-report`;
- explicit failure/unavailable result.

### Dependencies

- `evidence-traceability`;
- technical integration adapter to be selected/designed in Phase 2C or later.

### Non-Goals

- assuming Upwork/Fiverr/Terrawork/Gmail/Drive/LinkedIn integration exists;
- using read permission as write authority;
- exposing credentials to product modules.

### Validation

Source, permission scope, and retrieval outcome must be explicit.

## Module — `human-approval-gate`

- **Capability:** `connected-context-action-control`
- **Status:** Proposed
- **Owner:** Freelancer Growth OS / `connected-context-action-control`; operational owner not yet assigned
- **Requirements:** `FR-017`; `NFR-003`, `NFR-011`

### Purpose

Create a single explicit boundary between AI-prepared consequential actions and external execution.

### Inputs

- `approval-request` containing exact proposed action, target, material content/parameters, and scope;
- human `approval-decision`;
- verified execution capability when implemented.

### Outputs

- `approval-decision-record`;
- permitted execution instruction when approved;
- rejected/cancelled state when not approved;
- `execution-result` when later integrated.

### Dependencies

- technical execution adapters remain Phase 2C/later;
- `evidence-traceability` for audit/provenance.

### Required State Model

`draft → awaiting-approval → approved/rejected → attempted → verified-succeeded/failed/unknown`

Skipping `awaiting-approval` or treating `approved` as `verified-succeeded` is prohibited.

### Validation

- exact action scope matches the approval;
- changed content/target requires re-approval when materially different;
- execution success requires evidence;
- no default standing authority is inferred from connector availability.

## Deferred Later-Phase Module Decomposition

### `client-success`

Detailed module IDs are intentionally **not yet assigned** for onboarding, communication, delivery support, retention, reputation/testimonials, and upselling because Phase 2A does not yet provide enough detailed journeys, data contracts, or acceptance criteria to decompose them safely.

Phase 2C must not invent these module details as a side effect of technical design. They require later product-requirement refinement when implementation approaches.

### `business-growth`

Detailed module IDs are intentionally **not yet assigned** for performance analytics, revenue intelligence, pipeline intelligence, and strategic growth planning because persistence, analytics metrics, business data models, and product success measures remain unresolved.

## Module Dependency Summary

### Evidence and Intelligence

`evidence-traceability`
→ `evidence-intake`
→ `maturity-assessor`
→ `professional-positioning-engine`

### Positioning and Assets

`professional-positioning-engine`
→ `marketplace-profile-assessor`
→ `marketplace-profile-optimizer`

`professional-positioning-engine`
→ `service-offer-positioner`
→ `portfolio-positioner`

`cross-asset-consistency-checker` validates outputs across this chain without owning source facts.

### Opportunity and Conversion

`professional-positioning-engine` + `service-offer-positioner` + `evidence-intake`
→ `opportunity-evaluator`
→ `proposal-assistant`

`opportunity-evaluator`
→ `pricing-advisor`
→ `negotiation-preparer`
→ `client-conversion-assistant`

### Shared Controls

`freshness-escalator` may be invoked by any module whose output depends materially on volatile information.

`connected-context-retriever` may supply authorised read context to product modules but does not own business decisions.

`human-approval-gate` is the mandatory boundary before consequential external execution.

## Compatibility and Change Rules

- Stable module IDs should not be renamed casually once referenced by prompts, tests, interfaces, or other modules.
- A module responsibility change that materially alters inputs, outputs, authority, or dependency direction requires compatibility review.
- Splitting or merging modules must preserve requirement traceability and document migration impact.
- Technical implementation may refine internal algorithms without changing these contracts when behaviour remains compatible.
- GrowthOS Engineering remains the shared governance dependency; these product modules must not become upstream shared-governance requirements.

## Phase 2B Validation Checklist

- [x] Initial capability modules have stable lowercase-kebab-case IDs.
- [x] Every initial module maps to an approved requirement or cross-cutting control.
- [x] Inputs and outputs are defined logically.
- [x] Dependency direction is explicit.
- [x] Human approval is separated from draft generation.
- [x] Evidence/factuality/freshness controls are cross-cutting.
- [x] Direct integrations are not assumed.
- [x] Later Client Success and Business Growth detail remains deferred rather than fabricated.
- [x] No programming language, framework, database, LLM provider, cloud platform, or deployment stack is selected.
- [x] Product implementation and release remain unclaimed.
