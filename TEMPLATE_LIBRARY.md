# Freelancer Growth OS Template Library

**Status:** Active  
**Product release status:** Unreleased  
**Governance baseline:** `Ajiifarouq/GrowthOS-Engineering` `v0.1.0` at `7ee056f938e12b5a72d1ee919a27f05ec5297c69`

## Purpose

This library defines reusable product templates for Freelancer Growth OS. Templates standardize evidence, decisions, module work, AI outputs, validation, and approval handoffs without pretending that a completed template is itself implementation, approval, execution, or release evidence.

Templates inherit the product requirements, architecture, workflow, versioning, security, privacy, factuality, and approval boundaries defined elsewhere in this repository.

## Template Design Rules

Every reusable template must:

- have a stable lowercase-kebab-case template ID;
- distinguish verified facts, inference, proposals, unknowns, and rejected items where relevant;
- identify required inputs and provenance expectations;
- state output/acceptance expectations;
- preserve security/privacy boundaries;
- define human-approval state where consequential actions are involved;
- avoid hidden claims of execution or success;
- be versioned independently only when consumers require a stable reference;
- be reviewed when its owning requirement/module/contract materially changes.

## Catalog

| Template ID | Primary consumer | Purpose |
|---|---|---|
| `product-capability-specification` | capability architecture | Define a capability boundary and responsibility |
| `module-specification` | module architecture/implementation | Define a module contract and validation boundary |
| `implementation-specification` | engineering workflow | Turn approved requirements into implementation-ready scope |
| `evidence-record` | evidence assurance | Record claim provenance and uncertainty |
| `freelancer-context` | freelancer intelligence | Capture user background, goals, constraints, and evidence state |
| `maturity-assessment` | maturity assessor | Record maturity classification and rationale |
| `positioning-brief` | positioning/branding | Define evidence-backed professional positioning |
| `profile-assessment` | marketplace profile assessor | Diagnose profile strengths, gaps, and risks |
| `service-offer-brief` | service offer positioner | Define service, buyer, problem/value proposition, and proof |
| `portfolio-alignment-plan` | portfolio positioner | Align portfolio evidence with target positioning/opportunity |
| `opportunity-assessment` | opportunity evaluator | Assess opportunity fit, gaps, risks, and evidence match |
| `proposal-input-brief` | proposal assistant | Supply verified opportunity-specific proposal inputs |
| `proposal-draft-record` | proposal assistant | Store proposal draft plus evidence/assumption notes |
| `pricing-brief` | pricing advisor | Record pricing reasoning, assumptions, constraints, evidence |
| `negotiation-plan` | negotiation preparer | Record positions, trade-offs, questions, and commitment risks |
| `conversion-next-step-plan` | client conversion assistant | Recommend the next appropriate client action |
| `validation-report` | assurance/validation | Record checks, evidence, failures, limitations, disposition |
| `freshness-requirement` | freshness escalator | State why current verification is required |
| `connected-context-request` | connector boundary | Request minimum authorised read context |
| `approval-request` | approval gate | Describe exact proposed consequential action |
| `approval-decision-record` | approval gate | Record explicit approval/rejection scope |
| `execution-result` | execution/audit | Record verified outcome separately from approval |
| `prompt-change-record` | prompt governance | Track prompt behavior/version/eval compatibility |
| `release-candidate-record` | release preparation | Record proposed version and exact candidate SHA |

## Template — `product-capability-specification`

### Identity

- Capability ID: `[lowercase-kebab-case]`
- Status: `[Draft/Proposed/Active/Deprecated/Retired/Unreleased]`
- Owner: `[owner]`
- Requirements: `[FR/NFR references]`

### Purpose

[What product outcome does this capability own?]

### Responsibilities

[Included responsibilities.]

### Non-Goals

[Explicit exclusions.]

### Inputs and Outputs

[Logical contracts and provenance expectations.]

### Dependencies

[Upstream/downstream capabilities and shared controls.]

### Authority Boundary

[What AI may do; what requires human approval.]

### Security / Privacy / Factuality

[Material risks and controls.]

### Validation

[Acceptance criteria and evidence.]

### Compatibility / Migration

[Consumers and breaking-change considerations.]

## Template — `module-specification`

### Identity

- Module ID: `[lowercase-kebab-case]`
- Capability: `[capability-id]`
- Status: `[Draft/Proposed/Active/Deprecated/Retired/Unreleased]`
- Owner: `[owner]`
- Requirements: `[references]`
- Prompt assets: `[prompt IDs if applicable]`

### Purpose

[Single primary responsibility.]

### Inputs

[Required/optional inputs, validation, provenance.]

### Outputs

[Typed/logical output contracts and error states.]

### Dependencies

[Internal/external dependencies.]

### Behavior

[Normal execution and deterministic policies.]

### Non-Goals

[What the module must not own.]

### Failure Handling

[Safe failure, retry limits, stop conditions.]

### AI Authority

[AI actions permitted; consequential actions prohibited or approval-gated.]

### Security / Privacy / Factuality / Freshness

[Required controls.]

### Validation

[Tests/evals/acceptance evidence.]

### Compatibility / Migration

[Stable interfaces and migration needs.]

## Template — `implementation-specification`

- Change ID: `[id]`
- Requested outcome: `[outcome]`
- Requirements: `[references]`
- Capabilities/modules affected: `[ids]`
- Scope: `[included]`
- Non-goals: `[excluded]`
- Inputs/outputs/contracts: `[details]`
- Failure behavior: `[details]`
- Security/privacy impact: `[none/details]`
- Factuality/freshness impact: `[none/details]`
- Compatibility class: `[class]`
- Migration requirement: `[none/details]`
- Tests/evals: `[required evidence]`
- Acceptance criteria: `[criteria]`
- Protected actions expected: `[actions]`
- Residual unknowns/blockers: `[none/details]`

## Template — `evidence-record`

- Evidence ID: `[id]`
- Subject/claim: `[claim]`
- Classification: `[verified/inferred/proposed/unknown/conflicting/rejected]`
- Source type: `[user-provided/connected/current-research/repository/other]`
- Source reference: `[safe reference]`
- Verification time: `[if materially time-sensitive]`
- Sensitivity: `[public/personal/confidential/secret-prohibited]`
- Allowed uses: `[scope]`
- Contradictions: `[none/details]`
- Notes: `[limits]`

Raw secrets must never be placed in this record.

## Template — `freelancer-context`

- Workspace/user reference: `[id]`
- Professional background: `[verified summary]`
- Skills: `[verified/proposed split]`
- Experience: `[verified summary]`
- Qualifications/certifications: `[verified/unknown]`
- Target services: `[known/proposed]`
- Target clients/industries/geography: `[known/proposed]`
- Goals: `[goals]`
- Constraints: `[constraints]`
- Pricing context: `[if supplied]`
- Evidence gaps: `[gaps]`
- Conflicts/unknowns: `[items]`
- Evidence references: `[ids]`

## Template — `maturity-assessment`

- Classification: `[Starting/Building/Established/Scaling]`
- Confidence: `[high/medium/low or defined scale]`
- Evidence supporting classification: `[references]`
- Missing evidence: `[items]`
- Rationale: `[concise explanation]`
- Recommended focus: `[next priorities]`
- Reassessment triggers: `[new evidence/events]`

Maturity must not be inferred from prestige or income alone.

## Template — `positioning-brief`

- Positioning statement: `[draft]`
- Target client: `[who]`
- Client problem/outcome: `[verified/proposed]`
- Core services: `[services]`
- Differentiators: `[evidence-backed]`
- Proof/evidence: `[references]`
- Relevant skills/tools/industries: `[supported terms]`
- Unsupported claims to avoid: `[items]`
- Alternative positioning options: `[optional]`
- Risks/unknowns: `[items]`

## Template — `profile-assessment`

- Platform: `[Upwork/Fiverr/Terrawork/other verified context]`
- Current positioning alignment: `[assessment]`
- Headline/first-impression assessment: `[findings]`
- About/bio assessment: `[findings]`
- Proof/portfolio assessment: `[findings]`
- Discoverability assessment: `[findings without ranking fabrication]`
- Differentiation assessment: `[findings]`
- Consistency findings: `[findings]`
- Unsupported claims: `[items]`
- Buyer-journey friction: `[items]`
- Priority actions: `[ordered actions]`
- Freshness warnings: `[platform facts requiring verification]`

## Template — `service-offer-brief`

- Service/offer: `[name]`
- Intended buyer: `[buyer]`
- Problem: `[problem]`
- Intended value/outcome: `[non-guaranteed outcome]`
- Scope: `[included]`
- Exclusions: `[excluded]`
- Evidence/proof: `[references]`
- Differentiation: `[supported]`
- Open questions: `[items]`

## Template — `portfolio-alignment-plan`

- Target positioning/opportunity: `[reference]`
- Recommended work samples: `[items]`
- Why each sample matters: `[rationale]`
- Evidence available: `[references]`
- Missing proof: `[gaps]`
- Presentation guidance: `[guidance]`
- Claims/results that must not be invented: `[items]`

## Template — `opportunity-assessment`

- Opportunity reference: `[id/source]`
- Known requirements: `[requirements]`
- Freelancer match: `[evidence-backed match]`
- Gaps: `[gaps]`
- Risks/constraints: `[risks]`
- Current facts requiring verification: `[items]`
- Fit disposition: `[strong/conditional/weak or defined scale]`
- Rationale: `[reasoning summary]`
- Questions before proceeding: `[questions]`
- Proposal input recommendations: `[items]`
- No success probability guarantee: `true`

## Template — `proposal-input-brief`

- Opportunity reference: `[id]`
- Client need: `[verified summary]`
- Relevant freelancer evidence: `[references]`
- Relevant portfolio proof: `[references]`
- Positioning/service alignment: `[summary]`
- Client-specific constraints: `[items]`
- Questions/unknowns: `[items]`
- Claims permitted: `[supported claims]`
- Claims prohibited: `[unsupported claims]`
- Desired call to action: `[appropriate next step]`

## Template — `proposal-draft-record`

- Draft ID: `[id]`
- Opportunity reference: `[id]`
- Prompt/version used: `[reference if applicable]`
- Draft content: `[content]`
- Evidence references: `[ids]`
- Assumptions/unknowns: `[items]`
- Validation status: `[status]`
- Submission state: `not-submitted` unless separately verified

## Template — `pricing-brief`

- Opportunity/scope: `[reference]`
- User pricing goals/constraints: `[input]`
- Proposed pricing approach: `[approach]`
- Assumptions: `[assumptions]`
- Verified benchmarks: `[references or unavailable]`
- Freshness status: `[verified/unverified/not-required]`
- Trade-offs: `[trade-offs]`
- Risks: `[risks]`
- User commitment: `none` until explicitly accepted

## Template — `negotiation-plan`

- Objectives: `[objectives]`
- Preferred position: `[position]`
- Minimum/maximum boundaries supplied by user: `[if supplied]`
- Questions to ask: `[questions]`
- Trade-offs/concessions: `[options]`
- Response options: `[options]`
- Commitment risks: `[risks]`
- Items requiring explicit user decision: `[items]`

## Template — `conversion-next-step-plan`

- Current client state: `[state]`
- Recommended next step: `[clarification/interview/scope/pricing/agreement/etc.]`
- Why: `[rationale]`
- Draft communication: `[optional draft]`
- Evidence/assumptions: `[references]`
- Consequential action required: `[yes/no]`
- Approval required: `[yes/no]`

## Template — `validation-report`

- Candidate/artifact: `[reference]`
- Requirements checked: `[references]`
- Checks performed: `[actual checks]`
- Evidence: `[results]`
- Failures: `[none/details]`
- Security/privacy findings: `[none/details]`
- Factuality/freshness findings: `[none/details]`
- Compatibility findings: `[none/details]`
- Limitations: `[limitations]`
- Disposition: `[pass/pass-with-risk/fail/blocked]`
- Approval statement: `Validation is evidence, not approval.`

## Template — `freshness-requirement`

- Claim/task: `[subject]`
- Volatile fact category: `[platform-policy/API/pricing/legal/trend/tool/etc.]`
- Why freshness matters: `[impact]`
- Required source quality: `[authoritative/primary/etc.]`
- Last verified: `[date/unknown]`
- Current verification result: `[verified/unavailable/not-yet-run]`
- Fallback behavior: `[state uncertainty; do not guess]`

## Template — `connected-context-request`

- Request ID: `[id]`
- Consumer module: `[module]`
- Source/service: `[service]`
- Purpose: `[specific purpose]`
- Minimum data required: `[fields/scope]`
- Read/write: `read`
- User authorization evidence: `[reference]`
- Sensitivity: `[classification]`
- Expiry/revocation context: `[if applicable]`

A read request never implies write authority.

## Template — `approval-request`

- Approval request ID: `[id]`
- Proposed action type: `[send/submit/publish/update/accept/etc.]`
- Target: `[exact target]`
- Material content/parameters: `[exact content/scope]`
- Originating module: `[module]`
- Draft/artifact reference: `[id]`
- Risks/irreversibility: `[details]`
- Execution adapter required: `[adapter/unknown]`
- State: `awaiting-approval`

## Template — `approval-decision-record`

- Approval request ID: `[id]`
- Decision: `[approved/rejected/cancelled]`
- Approved exact scope: `[scope]`
- Decision authority: `[verified actor/reference]`
- Decision time: `[timestamp]`
- Conditions: `[none/details]`
- Material changes require re-approval: `true`

## Template — `execution-result`

- Approval request/decision reference: `[ids]`
- Executor: `[adapter]`
- Attempt time: `[timestamp]`
- State: `[verified-succeeded/failed/unknown]`
- External evidence/reference: `[safe evidence]`
- Error/reconciliation status: `[details]`
- Retry permitted: `[yes/no/needs-reconciliation]`

`approved` must never be represented as `verified-succeeded`.

## Template — `prompt-change-record`

- Prompt ID: `[id]`
- Prior version: `[version]`
- Candidate version: `[version]`
- Owning module/role: `[ids]`
- Intended behavior change: `[change]`
- Compatibility class: `[class]`
- Output-contract impact: `[none/details]`
- Authority/safety impact: `[none/details]`
- Evals executed: `[actual evidence]`
- Regression findings: `[none/details]`
- Migration/deprecation: `[none/details]`
- Approval required: `[yes/no + boundary]`

## Template — `release-candidate-record`

- Proposed product version: `[MAJOR.MINOR.PATCH]`
- Exact candidate SHA: `[40-hex SHA]`
- Compatibility summary: `[summary]`
- Required migrations: `[none/details]`
- Changelog/release notes: `[reference]`
- Validation evidence: `[references]`
- Known limitations: `[items]`
- Approval state: `[not-approved/approved]`
- Tag state: `[not-created/verified-created]`
- Release-publication state: `[not-published/verified-published]`
- Deployment state: `[not-deployed/verified-deployed/not-applicable]`

## Maintenance

Templates must be reviewed when:

- their owning contract or module changes materially;
- prompt behavior changes the required input/output shape;
- a security/privacy/factuality rule changes;
- the approval state model changes;
- a released consumer depends on the template shape.

A template must not silently redefine product behavior. Behavior belongs to requirements, architecture, modules, prompts, and deterministic application policies.
