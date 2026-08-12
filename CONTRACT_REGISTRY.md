# Freelancer Growth OS Contract Registry

**Status:** Active pre-implementation authority  
**Product release status:** Unreleased  
**Initial contract version:** `0.1.0` unless stated otherwise

## Purpose

This registry is the canonical naming and ownership layer for data exchanged among modules, prompts, persistence, CLI/API adapters, validation, and tests.

It resolves naming drift that existed across the Phase 2B module/capability architecture and Phase 4 template/prompt libraries.

When older documents use an alias listed here, implementation must use the canonical contract ID from this registry.

## Contract Rules

- Contract IDs are lowercase kebab-case.
- Every persisted/serialized contract has an explicit version.
- Every contract has exactly one canonical owner ID.
- Runtime contract owners are stable module/capability IDs; repository-governance contracts use one stable named governance authority.
- A contract may have multiple producers, but producer variability never changes canonical ownership.
- Prompt output must identify a canonical contract ID.
- Pydantic model names are implementation details, but their serialized contract ID/version must remain stable.
- Adding optional fields may be backward-compatible; removing/renaming/reinterpreting fields requires compatibility review.
- LLM output is never authoritative until the canonical contract validates.
- Evidence/provenance and sensitivity fields must not be dropped merely for UI convenience.
- Contract aliases are migration aids only; do not create duplicate schemas for aliases.

## Canonical Contract Catalog

| Contract ID | Version | Canonical owner ID | Typical producer(s) | Primary consumers | Persistence |
|---|---:|---|---|---|---|
| `evidence-record` | `0.1.0` | `evidence-traceability` | `evidence-traceability`, `evidence-intake` | assurance, context building | persistent metadata; no secrets |
| `evidence-bundle` | `0.1.0` | `evidence-intake` | `evidence-intake` | most business modules | persistent/snapshot as needed |
| `evidence-gap-report` | `0.1.0` | `evidence-intake` | `evidence-intake` | user, maturity, positioning | derived |
| `freelancer-context` | `0.1.0` | `evidence-intake` | `evidence-intake` | positioning, opportunity, conversion | persistent/versioned |
| `maturity-assessment` | `0.1.0` | `maturity-assessor` | `maturity-assessor` | positioning, user | persistent/versioned |
| `positioning-brief` | `0.1.0` | `professional-positioning-engine` | `professional-positioning-engine` | profile, offer, opportunity, conversion | persistent/versioned |
| `profile-assessment` | `0.1.0` | `marketplace-profile-assessor` | `marketplace-profile-assessor` | profile optimizer, user | persistent/versioned |
| `profile-optimization-draft` | `0.1.0` | `marketplace-profile-optimizer` | `marketplace-profile-optimizer` | user, future publishing flow | persistent/versioned; never publication proof |
| `service-offer-brief` | `0.1.0` | `service-offer-positioner` | `service-offer-positioner` | portfolio, opportunity, conversion | persistent/versioned |
| `portfolio-alignment-plan` | `0.1.0` | `portfolio-positioner` | `portfolio-positioner` | user, opportunity/proposal | persistent/versioned |
| `cross-asset-consistency-report` | `0.1.0` | `cross-asset-consistency-checker` | `cross-asset-consistency-checker` | user, assurance, affected modules | derived/versioned |
| `opportunity-assessment` | `0.1.0` | `opportunity-evaluator` | `opportunity-evaluator` | proposal, pricing, user | persistent/versioned |
| `proposal-input-brief` | `0.1.0` | `opportunity-evaluator` | `opportunity-evaluator` | `proposal-assistant` | derived/versioned |
| `proposal-draft-record` | `0.1.0` | `proposal-assistant` | `proposal-assistant` | user, approval flow | persistent/versioned; never submission proof |
| `pricing-brief` | `0.1.0` | `pricing-advisor` | `pricing-advisor` | negotiation, conversion, user | persistent/versioned |
| `negotiation-plan` | `0.1.0` | `negotiation-preparer` | `negotiation-preparer` | conversion, user | persistent/versioned |
| `conversion-next-step-plan` | `0.1.0` | `client-conversion-assistant` | `client-conversion-assistant` | user, approval flow | persistent/versioned |
| `validation-report` | `0.1.0` | `evidence-traceability` | assurance validators | all modules/user | persistent when material |
| `freshness-requirement` | `0.1.0` | `freshness-escalator` | `freshness-escalator` | research adapter/module | derived |
| `freshness-verification-result` | `0.1.0` | `freshness-escalator` | current-research adapter + `freshness-escalator` orchestration | assurance/business modules | persistent when used as evidence |
| `connected-context-request` | `0.1.0` | `connected-context-retriever` | authorised requesting modules | connector boundary | audit metadata only |
| `connected-context` | `0.1.0` | `connected-context-retriever` | `connected-context-retriever` | authorised requesting module | minimum necessary; avoid raw bulk persistence |
| `permission-boundary-report` | `0.1.0` | `connected-context-retriever` | `connected-context-retriever` | audit/user/module | derived/audit |
| `approval-request` | `0.1.0` | `human-approval-gate` | product modules/action-control | human approval gate | persistent when execution exists |
| `approval-decision-record` | `0.1.0` | `human-approval-gate` | `human-approval-gate` | execution/audit | persistent |
| `execution-result` | `0.1.0` | `human-approval-gate` | execution adapter/action-control | user/audit | persistent |
| `prompt-change-record` | `0.1.0` | `prompt-governance` | prompt governance workflow | maintainers/release review | repository/product metadata |
| `release-candidate-record` | `0.1.0` | `release-process` | release preparation workflow | owner/release process | release metadata |

`prompt-governance` and `release-process` are stable repository-governance authority IDs for non-runtime governance contracts; they are not product runtime modules.

## Canonical Alias Resolution

The following older architecture terms are not separate contracts:

| Older/ambiguous term | Canonical treatment |
|---|---|
| `proposal-draft` | alias of `proposal-draft-record` |
| `profile optimization draft` | `profile-optimization-draft` |
| `consistency validation report` | `cross-asset-consistency-report` |
| `evidence-reference` | an ID/reference to `evidence-record`, not a second schema |
| `fit-rationale` | field inside `opportunity-assessment` |
| `evidence-match-report` | field/section inside `opportunity-assessment` |
| `opportunity-risk-report` | field/section inside `opportunity-assessment` |
| `contradiction flags` | field inside `evidence-bundle` and/or `evidence-gap-report` |
| `provenance classifications` | fields/records inside `evidence-record` / `validation-report` |
| `unsupported-claim flags` | field inside `validation-report` or owning output contract |

Implementation must not create independent Pydantic/database schemas merely because an older document used one of these terms.

## Required Contract Shapes

The exact Pydantic field syntax will be defined during implementation, but the following minimum semantic fields are normative.

### `evidence-record`

- `evidence_id`
- `subject_or_claim`
- `state`
- `source_type`
- `source_reference`
- `verification_time` when material
- `sensitivity`
- `allowed_uses`
- `contradictions`
- `supersedes_id` where applicable
- `deleted_at` where applicable

`SECRET` content is prohibited.

Persistence must round-trip `allowed_uses` and `contradictions` without loss. Storage may normalize them, but re-serialization to `evidence-record` must preserve the same restrictions and conflict metadata.

### `evidence-bundle`

- bundle ID/version
- workspace reference
- evidence-record references
- known/unknown/conflicting summary
- sensitivity summary
- source/provenance summary
- creation/update time

### `evidence-gap-report`

- missing information
- why each gap matters
- affected downstream modules/contracts
- conflict list
- recommended user clarification/evidence request

### `freelancer-context`

Use the existing `freelancer-context` template fields plus:

- contract ID/version
- artifact ID/version
- dependency/evidence references
- staleness state

### `profile-optimization-draft`

Minimum fields:

- platform
- source `profile-assessment` reference/version
- source `positioning-brief` reference/version
- drafted profile fields as labeled name/value pairs
- keyword/discoverability notes where supported
- evidence references
- assumptions/unknowns
- unsupported-input warnings
- freshness warnings
- validation status
- `publication_state: not-published`
- prompt ID/version/content hash where AI-generated
- model/provider run reference where AI-generated

Publication state may change only through a separately verified external execution flow.

### `cross-asset-consistency-report`

Minimum fields:

- assets/artifact versions compared
- evidence references used
- contradictions
- severity/impact per contradiction
- facts that cannot be reconciled automatically
- recommended resolution path
- freshness issues where relevant
- validation disposition

The report must never silently pick a conflicting source as true without evidence.

### `opportunity-assessment`

Minimum fields include the existing template plus:

- `fit_rationale`
- `evidence_match`
- `opportunity_risks`
- source/freshness metadata
- dependency versions

No numeric win probability is permitted unless a future requirement/evidence model explicitly authorises one.

### `proposal-draft-record`

Minimum fields use the existing template and include:

- contract ID/version
- draft ID/version
- opportunity reference
- prompt ID/version/content hash if AI-generated
- model/provider run reference if AI-generated
- draft content
- evidence references
- assumptions/unknowns
- validation status
- staleness status
- `submission_state: not-submitted` until separately verified

### `freshness-verification-result`

- request/freshness-requirement reference
- claim/task
- source URLs/references
- source quality classification
- verification timestamp
- verified facts
- conflicts/limitations
- expiry/recheck trigger where useful
- disposition: `verified`, `conflicting`, `unavailable`, or `insufficient`

Persistence must round-trip the request reference, all source references, source-quality classification, verified facts, and conflicts/limitations without loss.

### `connected-context`

- request ID
- service/source
- fields/content actually returned
- permission/scope used
- provenance
- retrieval timestamp
- sensitivity
- persistence permission/expiry

No credentials/tokens are valid contract payloads.

### `permission-boundary-report`

- connector/service
- requested capability
- granted read scopes
- granted write scopes
- missing/denied scopes
- revocation/expiry information where available
- human-approval requirement
- risk notes

### `approval-request`

In addition to the template:

- immutable payload hash/fingerprint
- idempotency key or deterministic action identity when execution is possible
- artifact dependency versions
- staleness check status
- single-use execution policy

### `approval-decision-record`

In addition to the template:

- approved payload hash/fingerprint
- decision actor identity/reference
- decision timestamp
- expiration if applicable
- consumed/executed state kept separately from decision value

### `execution-result`

In addition to the template:

- idempotency key/action identity
- attempt number
- provider/external request identifier where available
- exact approval-decision reference
- exact payload hash executed
- state: `verified-succeeded`, `failed`, or `unknown`
- reconciliation status

## Evidence-State Machine

The authoritative evidence-state transitions are deterministic application policy. Canonical states are:

- `provided-unverified`
- `verified`
- `inferred`
- `proposed`
- `unknown`
- `conflicting`
- `rejected`
- `superseded`
- `deleted`

```text
unknown
  ├─> provided-unverified when new source evidence is supplied
  ├─> inferred
  ├─> proposed
  ├─> verified only through new qualifying evidence
  ├─> conflicting
  ├─> rejected
  └─> deleted

provided-unverified
  ├─> verified
  ├─> conflicting
  ├─> rejected
  ├─> superseded
  └─> deleted

inferred
  ├─> provided-unverified when source evidence is supplied
  ├─> verified only through new qualifying evidence
  ├─> conflicting
  ├─> rejected
  └─> deleted

proposed
  ├─> provided-unverified when source evidence is supplied
  ├─> verified only through new qualifying evidence
  ├─> conflicting
  ├─> rejected
  └─> deleted

verified
  ├─> conflicting
  ├─> superseded
  └─> deleted

conflicting
  ├─> provided-unverified when conflict is narrowed but not resolved
  ├─> verified only through qualifying conflict-resolution evidence
  ├─> rejected
  ├─> superseded
  └─> deleted

rejected
  ├─> provided-unverified only when genuinely new evidence reopens the claim
  └─> deleted

superseded
  └─> deleted
```

An LLM may recommend a state but cannot perform the authoritative transition to `verified` by confidence or wording alone.

## Artifact Staleness Contract

Every persisted derived artifact must record dependency artifact/evidence IDs and versions.

Minimum artifact validity state:

- `current`
- `stale`
- `invalid`
- `deleted`

A dependency correction, deletion, supersession, or material reclassification must mark dependents stale/invalid according to deterministic policy.

Consequential execution rejects `stale` or `invalid` source artifacts.

## Prompt-to-Contract Mapping

| Prompt ID | Canonical output contract(s) |
|---|---|
| `build-freelancer-context` | `freelancer-context` + `evidence-record` + `evidence-gap-report` |
| `assess-freelancer-maturity` | `maturity-assessment` |
| `create-professional-positioning` | `positioning-brief` |
| `assess-marketplace-profile` | `profile-assessment` |
| `optimize-marketplace-profile` | `profile-optimization-draft` |
| `position-service-offer` | `service-offer-brief` |
| `align-portfolio-evidence` | `portfolio-alignment-plan` |
| `evaluate-freelance-opportunity` | `opportunity-assessment` + `proposal-input-brief` |
| `draft-evidence-grounded-proposal` | `proposal-draft-record` |
| `prepare-pricing-brief` | `pricing-brief` |
| `prepare-negotiation-plan` | `negotiation-plan` |
| `recommend-client-next-step` | `conversion-next-step-plan` |
| `review-evidence-factuality` | `validation-report` |
| `review-cross-asset-consistency` | `cross-asset-consistency-report` |
| `decide-freshness-requirement` | `freshness-requirement` |

For `build-freelancer-context`, the prompt's material claim classifications are serialized as `evidence-record` items and its evidence-gaps/conflicts output is serialized as the canonical `evidence-gap-report`; no untyped parallel gap schema is permitted.

## Implementation Gate

Before a module is implemented:

1. its input/output contract IDs must exist here;
2. Pydantic models must declare/map the contract version;
3. serialization and schema tests must exist;
4. prompt-backed outputs must validate against the same contract;
5. persistence must not invent a second shape for the same contract;
6. incompatible contract changes must follow `COMPATIBILITY_MIGRATION.md`.
