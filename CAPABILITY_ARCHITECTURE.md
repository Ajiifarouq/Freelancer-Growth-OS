# Freelancer Growth OS Capability Architecture

**Status:** Active  
**Architecture phase:** Phase 2B — Capability and Module Architecture  
**Product release status:** Unreleased  
**Requirements baseline:** [PRODUCT_REQUIREMENTS.md](PRODUCT_REQUIREMENTS.md)  
**Governance baseline:** `Ajiifarouq/GrowthOS-Engineering` `v0.1.0` at `7ee056f938e12b5a72d1ee919a27f05ec5297c69`

## Purpose

This document translates the approved Freelancer Growth OS product requirements into stable product capabilities, responsibility boundaries, dependency direction, shared logical contracts, AI/human authority boundaries, knowledge/freshness dependencies, and validation responsibilities.

It defines logical product architecture. It does not select a programming language, framework, database, LLM provider, cloud platform, authentication provider, API protocol, UI framework, or deployment topology.

## Architecture Principles

1. Requirements drive capabilities; capabilities do not manufacture requirements.
2. Product logic remains in Freelancer Growth OS and does not move into GrowthOS Engineering.
3. Stable identifiers use lowercase kebab-case.
4. A capability may be approved product scope without being implemented.
5. Evidence, uncertainty, privacy, security, and freshness controls are shared foundations rather than optional decorations.
6. Consequential external actions remain human-approved under `FGOS-D004`.
7. Direct platform integration is never implied by platform-aware reasoning.
8. Downstream feedback re-enters through evidence intake rather than mutating upstream state invisibly.
9. Logical architecture must remain usable as the product evolves from AI framework/OS to personal application and, only when justified, multi-user SaaS.
10. Technical implementation choices remain deferred to Phase 2C.

## Capability Model

Freelancer Growth OS is organised into eight stable capability boundaries.

| Capability ID | Capability | Product phase | Architecture status | Primary requirements |
|---|---|---|---|---|
| `freelancer-intelligence` | Understand the freelancer, evidence, maturity, goals, and constraints | Growth Acquisition | Initial capability | `FR-001`, `FR-002`, `FR-018`, `FR-021` |
| `positioning-branding` | Turn verified freelancer evidence into credible positioning, profiles, offers, and portfolio alignment | Growth Acquisition | Initial capability | `FR-003`–`FR-009`, `FR-015` |
| `opportunity-intelligence` | Evaluate freelance opportunities for fit, relevance, evidence match, and risk | Growth Acquisition | Initial capability | `FR-010`, `FR-018`, `FR-021`, `FR-022` |
| `conversion` | Support proposals, pricing, negotiation, and movement toward appropriate client next steps | Growth Acquisition | Initial capability | `FR-011`–`FR-014`, `FR-017`, `FR-021`, `FR-022` |
| `evidence-knowledge-assurance` | Provide provenance, consistency, uncertainty, and freshness controls across the product | Shared foundation | Initial cross-cutting capability | `FR-015`, `FR-018`, `FR-021`, `FR-022`; `NFR-001`, `NFR-002`, `NFR-005` |
| `connected-context-action-control` | Retrieve authorised connected context and gate consequential external actions | Shared foundation | Integration-dependent cross-cutting capability | `FR-016`, `FR-017`; `NFR-003`, `NFR-004`, `NFR-011` |
| `client-success` | Preserve the later boundary for onboarding, communication, delivery support, retention, reputation, and upselling | Client Success | Approved later-phase boundary | `FR-019` |
| `business-growth` | Preserve the later boundary for performance, revenue, pipeline, and strategic growth intelligence | Business Growth | Approved later-phase boundary | `FR-020` |

`Architecture status` is not implementation status. Phase 2B defines boundaries and contracts; it does not claim that software modules are deployed or operational.

## Capability 1 — `freelancer-intelligence`

### Purpose

Create an evidence-based understanding of the freelancer before high-confidence recommendations are produced.

### Responsibilities

- receive user-provided or authorised professional evidence;
- distinguish supplied facts from assumptions and unknowns;
- organise skills, experience, qualifications, work history, goals, constraints, pricing context, target services, and target markets;
- assess maturity as Starting, Building, Established, or Scaling;
- identify missing information that materially affects downstream recommendations;
- expose a consistent freelancer-context output to downstream capabilities.

### Non-Goals

- inventing missing experience;
- ranking a user's personal worth;
- deciding technical storage architecture;
- independently performing connected-account writes;
- assigning maturity solely from income, prestige, or unsupported assumptions.

### Primary Inputs

- user-supplied professional background;
- CV/resume where provided;
- skills and qualifications;
- portfolio evidence;
- marketplace profile content;
- service goals;
- target client/industry/geography;
- authorised connected context where later supported.

### Primary Outputs

- `evidence-bundle`;
- `freelancer-context`;
- `maturity-assessment`;
- `evidence-gap-report`.

### Dependencies

- uses `evidence-knowledge-assurance` as a validation/provenance service, not as an upstream business-decision owner;
- may use `connected-context-action-control` for authorised reads;
- must not depend on `positioning-branding`, `opportunity-intelligence`, or `conversion` for authoritative source facts.

### Human Authority

Human permission is required before connected private sources are accessed where the connector model requires it. Users may correct evidence and maturity inputs.

### Validation

- material claims map to supplied/authorised evidence or are explicitly marked unknown;
- maturity classification includes rationale;
- conflicting evidence is surfaced rather than silently reconciled.

## Capability 2 — `positioning-branding`

### Purpose

Convert verified freelancer intelligence into credible, differentiated professional positioning and client-facing assets.

### Responsibilities

- recommend evidence-supported professional positioning;
- assess marketplace profiles;
- optimise Upwork, Fiverr, and Terrawork profile content while respecting platform differences;
- support discoverability without keyword stuffing;
- define/refine service and offer positioning;
- align portfolio selection and presentation to target clients/opportunities;
- evaluate client-facing assets against the buyer journey;
- check consistency across positioning, profiles, offers, portfolios, and later proposals.

### Non-Goals

- direct marketplace account modification unless separately verified and approved;
- promising platform ranking or interviews;
- fabricating credentials, clients, testimonials, results, or expertise;
- treating one platform's format as universally applicable.

### Primary Inputs

- `freelancer-context`;
- `maturity-assessment`;
- verified marketplace/profile content;
- portfolio evidence;
- target client/industry/geography;
- platform context;
- freshness signals where platform rules materially affect advice.

### Primary Outputs

- `positioning-brief`;
- `profile-assessment`;
- `profile-optimization-draft`;
- `service-offer-brief`;
- `portfolio-alignment-plan`;
- `cross-asset-consistency-report`.

### Dependencies

- requires `freelancer-intelligence`;
- invokes `evidence-knowledge-assurance` for factuality, consistency, and freshness validation;
- may use `connected-context-action-control` for authorised reads;
- feeds `opportunity-intelligence` and `conversion`.

### Human Authority

Recommendations and drafts may be generated automatically from authorised evidence. Publishing, account modification, or other consequential external writes remain human-approved.

### Validation

- no unsupported positioning claim;
- output remains consistent with verified evidence;
- platform-specific recommendations do not imply unverified API access or ranking guarantees;
- recommended assets have a clear intended client action.

## Capability 3 — `opportunity-intelligence`

### Purpose

Help the freelancer decide whether a freelance opportunity is worth pursuing and how well it matches their evidence and positioning.

### Responsibilities

- parse opportunity requirements from supplied or authorised information;
- compare required outcomes, skills, experience, budget/context, constraints, and evidence match;
- distinguish hard facts from inference;
- identify evidence gaps and material risks;
- produce an explainable fit assessment;
- escalate volatile platform or market claims to freshness verification when material.

### Non-Goals

- guaranteeing a win probability;
- autonomously applying to opportunities;
- fabricating hidden client preferences;
- treating unverified market assumptions as facts.

### Primary Inputs

- `freelancer-context`;
- `positioning-brief`;
- opportunity/job description;
- client brief where available;
- current platform/market context where material.

### Primary Outputs

- `opportunity-assessment`;
- `fit-rationale`;
- `evidence-match-report`;
- `opportunity-risk-report`;
- `proposal-input-brief`.

### Dependencies

- requires `freelancer-intelligence`;
- normally consumes `positioning-branding` outputs;
- invokes `evidence-knowledge-assurance` for validation;
- may use `connected-context-action-control` for authorised context retrieval;
- feeds `conversion`.

### Human Authority

The capability recommends whether/how to pursue; it does not submit applications or make commitments on the user's behalf.

### Validation

- assessment cites known evidence or labels inference;
- no guarantee of success;
- missing opportunity information is surfaced;
- volatile claims are verified or labelled unverified.

## Capability 4 — `conversion`

### Purpose

Support credible movement from a qualified opportunity toward an appropriate client commitment or next step.

### Responsibilities

- generate or refine tailored proposal content;
- support pricing reasoning without invented benchmarks;
- prepare negotiation positions, questions, trade-offs, and response options;
- prepare client-conversion messages and next-step recommendations;
- preserve consistency with freelancer positioning and evidence;
- separate drafts/recommendations from executable external actions.

### Non-Goals

- committing the user to terms without approval;
- guaranteeing client conversion;
- inventing urgency, scarcity, social proof, benchmarks, or evidence;
- autonomous outreach or application submission under the current authority model.

### Primary Inputs

- `freelancer-context`;
- `positioning-brief`;
- `opportunity-assessment`;
- client/opportunity context;
- user pricing goals where supplied;
- verified current benchmarks only where materially needed.

### Primary Outputs

- `proposal-draft`;
- `pricing-brief`;
- `negotiation-plan`;
- `conversion-next-step-plan`;
- `approval-request` where connected execution is later available.

### Dependencies

- requires `freelancer-intelligence` and `opportunity-intelligence` for opportunity-specific work;
- consumes `positioning-branding` outputs;
- invokes `evidence-knowledge-assurance` for validation;
- uses `connected-context-action-control` for consequential external execution when implemented.

### Human Authority

Draft generation does not require approval. Consequential external actions, commitments, submissions, or sends require explicit human approval.

### Validation

- proposal remains opportunity-specific and evidence-grounded;
- pricing assumptions are explicit;
- negotiation guidance does not become an unapproved commitment;
- action state clearly distinguishes draft, approved, attempted, and verified-executed states.

## Capability 5 — `evidence-knowledge-assurance`

### Purpose

Provide shared factuality, provenance, uncertainty, consistency, and freshness controls across all product capabilities.

### Responsibilities

- track provenance of material professional/business claims where practical;
- distinguish verified evidence, owner-approved requirements, recommendations, assumptions, and unknowns;
- detect contradictions across client-facing assets;
- flag insufficient evidence;
- decide when volatile information needs current verification;
- return validation reports without silently rewriting source truth;
- preserve traceability for architecture and later implementation.

### Non-Goals

- becoming a generic knowledge management product;
- silently deciding product scope;
- converting inference into verified evidence;
- storing secrets as evidence;
- owning positioning, opportunity-fit, pricing, negotiation, or conversion business decisions.

### Primary Inputs

- evidence references created during intake;
- outputs from product capabilities requiring validation;
- current authoritative sources where freshness verification is needed;
- requirement/evidence references from repository governance.

### Primary Outputs

- `evidence-reference`;
- `validation-report`;
- `uncertainty-report`;
- `freshness-requirement`;
- `freshness-verification-result`;
- `cross-asset-consistency-report`.

### Dependencies

This is a shared validation plane. It does not sit before or after the business flow as a semantic business step and must not depend on downstream recommendations as authoritative source truth.

### Human Authority

No consequential external action authority. It may stop or downgrade confidence when evidence is insufficient.

### Validation

- provenance categories remain distinct;
- uncertain facts are not promoted silently;
- current-source requirements are triggered for materially volatile claims;
- conflicting claims remain visible until resolved through authorised evidence.

## Capability 6 — `connected-context-action-control`

### Purpose

Create a single controlled boundary for future private-source retrieval and consequential external execution.

### Responsibilities

- represent authorised connected-context requests;
- preserve least-privilege read/write separation;
- return connected context with provenance and source boundary metadata;
- generate explicit approval requests for consequential writes/actions;
- record approval decisions when execution is implemented;
- distinguish draft, approved, attempted, succeeded, failed, and unverified execution states;
- support revocation/failure boundaries where integrations technically allow them.

### Non-Goals

- assuming any specific platform integration exists;
- bypassing user approval because an API supports an action;
- storing credentials in repository content;
- granting product modules unrestricted connector access;
- turning the product into an autonomous mass outreach/application agent.

### Primary Inputs

- `connected-context-request`;
- platform/integration capability metadata when verified;
- `approval-request`;
- human `approval-decision`.

### Primary Outputs

- `connected-context`;
- `permission-boundary-report`;
- `approval-decision-record`;
- `execution-result` where later implemented.

### Dependencies

- all integration-specific implementations remain Phase 2C or later decisions;
- uses `evidence-knowledge-assurance` to preserve source provenance;
- serves authorised reads to `freelancer-intelligence`, `positioning-branding`, `opportunity-intelligence`, and `conversion`;
- accepts proposed external actions from relevant product modules.

### Human Authority

Human approval is mandatory for consequential external actions under the current product authority model.

### Validation

- read permission does not imply write permission;
- execution cannot occur without the required approval record;
- connector/platform capability must be verified rather than assumed;
- result status must not claim success without execution evidence.

## Capability 7 — `client-success`

### Purpose

Preserve the approved later product boundary for onboarding, client communication, delivery support, retention, reputation/testimonial support, and upselling.

### Architecture Status

Approved product scope; detailed module decomposition deferred.

### Why Decomposition Is Deferred

`PRODUCT_REQUIREMENTS.md` establishes this as later-phase scope but does not yet define enough user journeys, data contracts, integration requirements, or acceptance criteria to create detailed modules without guessing.

### Dependency Direction

Expected to consume verified acquisition/conversion context and produce new client evidence back through explicit evidence ingestion rather than mutating upstream positioning state directly.

### Human Authority

Any external client communication or consequential action remains subject to the current human-approval model unless later changed by an explicit owner decision.

## Capability 8 — `business-growth`

### Purpose

Preserve the approved later product boundary for performance analytics, revenue intelligence, pipeline intelligence, and strategic growth planning.

### Architecture Status

Approved product scope; detailed module decomposition deferred.

### Why Decomposition Is Deferred

The requirements baseline intentionally leaves analytics metrics, persistence, revenue/pipeline data models, retention rules, and runtime architecture unresolved. Defining detailed modules now would fabricate implementation requirements.

### Dependency Direction

Expected to consume verified historical acquisition/client-success evidence and analytics data once those data models are approved. It must not manufacture business metrics when evidence is absent.

## Shared Logical Data Contracts

These are conceptual architecture contracts, not programming-language types or database schemas.

| Contract ID | Produced by | Typical consumers | Purpose |
|---|---|---|---|
| `evidence-bundle` | `freelancer-intelligence` | most product capabilities / assurance | Normalised set of authorised evidence references and known/unknown boundaries |
| `freelancer-context` | `freelancer-intelligence` | positioning, opportunity, conversion | Stable product-level view of freelancer background, goals, constraints, and evidence |
| `maturity-assessment` | `freelancer-intelligence` | positioning, later growth capabilities | Starting/Building/Established/Scaling classification with rationale |
| `positioning-brief` | `positioning-branding` | profile, opportunity, conversion | Evidence-supported market positioning and target-client framing |
| `profile-assessment` | `positioning-branding` | profile optimisation | Gaps, strengths, credibility, differentiation, discoverability, conversion issues |
| `profile-optimization-draft` | `positioning-branding` | user / future publishing action | Platform-aware profile draft; never proof of publication |
| `service-offer-brief` | `positioning-branding` | opportunity, conversion | Service, intended buyer, problem/value proposition, evidence |
| `portfolio-alignment-plan` | `positioning-branding` | user / opportunity | Recommended proof selection and presentation |
| `opportunity-assessment` | `opportunity-intelligence` | conversion | Fit, rationale, evidence match, gaps, and risks |
| `proposal-input-brief` | `opportunity-intelligence` | proposal module | Structured opportunity-specific inputs for proposal drafting |
| `proposal-draft` | `conversion` | user / approval flow | Tailored proposal content, not proof of submission |
| `pricing-brief` | `conversion` | user / negotiation | Pricing rationale, assumptions, constraints, optional verified benchmarks |
| `negotiation-plan` | `conversion` | user | Positions, questions, trade-offs, response options |
| `conversion-next-step-plan` | `conversion` | user / approval flow | Recommended next client action |
| `validation-report` | `evidence-knowledge-assurance` | all capabilities/user | Factuality, uncertainty, consistency, provenance, freshness findings |
| `freshness-requirement` | assurance plane | research/current-source layer | Declares why current verification is materially required |
| `connected-context` | connected-context control | authorised capability | Read-only authorised source context with provenance metadata |
| `approval-request` | product module / action control | human approval gate | Proposed consequential action plus exact scope |
| `approval-decision-record` | action control | execution boundary/audit | Approved/rejected decision and action scope |
| `execution-result` | action control | user/audit | Attempted action outcome; must distinguish verified success from failure/unknown |

## Dependency Architecture

### Core Business Flow

`freelancer-intelligence`
→ `positioning-branding`
→ `opportunity-intelligence`
→ `conversion`

This is the semantic business flow. Each downstream step consumes explicit contracts from the prior step and may request reassessment rather than rewriting upstream truth.

### Assurance Plane

`evidence-knowledge-assurance`
↔ validation/provenance/freshness checks
↔ every relevant business capability

The assurance plane is cross-cutting, not a semantic first or last step. It validates evidence and outputs without owning the business decisions being validated.

### Connected Context Plane

`connected-context-action-control`
→ authorised read context
→ relevant business capability

Read access is optional and integration-dependent. Business modules must still work with direct user-supplied inputs where requirements permit.

### Consequential Action Flow

`business module`
→ `approval-request`
→ `connected-context-action-control`
→ `human approval`
→ optional verified execution

### Later Lifecycle Flow

`conversion`
→ `client-success`
→ `business-growth`

Feedback from later phases must return as new evidence through explicit intake/provenance processing. Later capabilities must not silently mutate the source evidence used to justify earlier outputs.

## Cycle Prevention Rules

- assurance validation edges are not semantic business-flow dependencies and must not be used to create circular business ownership;
- `conversion` must not rewrite `freelancer-intelligence` evidence directly;
- `opportunity-intelligence` may use positioning but must not redefine authoritative positioning without returning a reassessment request;
- assurance modules may validate any output but must not become owners of business decisions;
- connected-context control may transport authorised data/actions but must not decide positioning, opportunity fit, pricing, or negotiation strategy;
- later Client Success and Business Growth capabilities may contribute new evidence only through explicit evidence ingestion/provenance handling.

## AI Authority Boundaries

### May Operate Without Consequential-Action Approval

Within authorised data boundaries, the AI may:

- analyse supplied evidence;
- classify maturity with rationale;
- recommend positioning;
- assess profiles;
- generate drafts;
- evaluate opportunities;
- prepare proposals;
- reason about pricing;
- prepare negotiation options;
- run consistency/factuality checks;
- identify freshness requirements;
- produce approval-ready action drafts.

### Requires Human Approval

The following remain approval-gated when technically supported:

- sending/submitting client communications;
- submitting proposals/applications;
- publishing or modifying marketplace profiles;
- accepting or committing to pricing/terms;
- writing to connected external systems in consequential ways;
- other actions that materially affect a user's account, client relationship, money, reputation, or external commitments.

## Knowledge and Freshness Boundaries

Each capability must label information as one of:

- user-provided/authorised evidence;
- repository-approved product requirement/decision;
- verified current external fact;
- inference/recommendation;
- unknown/unverified.

Freshness verification is required when stale information could materially change advice, including marketplace policies, platform features, integration capabilities, pricing benchmarks, hiring/freelance trends, legal/tax/regulatory requirements, and current tool recommendations.

## Security and Privacy Boundaries

- capabilities receive only the data needed for their active responsibility;
- connected credentials are never product-domain inputs;
- secret handling belongs to later technical architecture and must use a dedicated security boundary;
- private/client/business data is not public by default;
- connected reads and connected writes are separate permissions;
- multi-user isolation remains a future technical requirement if SaaS is justified;
- architecture must preserve source provenance and user authorisation.

## Validation Ownership

| Validation concern | Primary capability | Product modules remain responsible for |
|---|---|---|
| Evidence provenance | `evidence-knowledge-assurance` | Providing source/evidence references |
| Factuality | `evidence-knowledge-assurance` | Not introducing unsupported business claims |
| Cross-asset consistency | `evidence-knowledge-assurance` + positioning module | Domain-specific interpretation of conflicts |
| Freshness | `evidence-knowledge-assurance` | Declaring when current facts materially affect output |
| Maturity rationale | `freelancer-intelligence` | Evidence-based classification |
| Opportunity-fit rationale | `opportunity-intelligence` | Separating fact from inference |
| Proposal/pricing/negotiation consistency | `conversion` + assurance | Maintaining alignment with evidence and positioning |
| Connected permissions | `connected-context-action-control` | Requesting only necessary context/action scope |
| Human approval | `connected-context-action-control` | Never treating draft creation as execution approval |

Validation provides evidence; it does not silently grant approval for consequential actions.

## Phase 2B Completion Criteria

Phase 2B is complete when this capability architecture and [MODULE_CATALOG.md](MODULE_CATALOG.md) are merged to `main` and verification confirms:

- stable capability IDs exist;
- initial modules have stable lowercase-kebab-case IDs;
- responsibilities do not overlap ambiguously;
- inputs and outputs are defined at logical-contract level;
- business dependency direction is explicit and cycles are controlled;
- assurance and connected-context planes remain cross-cutting boundaries rather than hidden business owners;
- AI versus human authority boundaries are explicit;
- evidence/factuality/freshness responsibilities are traceable;
- later Client Success and Business Growth boundaries are preserved without invented module detail;
- no technical stack is selected prematurely;
- no direct external integration is claimed without verification;
- product release status remains Unreleased.

The next substage is **Phase 2C — Technical Architecture**, where implementation topology and technology decisions may be derived from these approved logical boundaries.
