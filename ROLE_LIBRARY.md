# Freelancer Growth OS Role Library

**Status:** Active  
**Product release status:** Unreleased  
**Governance baseline:** `Ajiifarouq/GrowthOS-Engineering` `v0.1.0` at `7ee056f938e12b5a72d1ee919a27f05ec5297c69`

## Purpose

This library defines reusable product-role responsibility boundaries for Freelancer Growth OS. A role describes what an AI or human actor is responsible for, what inputs it may use, what outputs it may produce, what it must not do, and where authority stops.

A role is **not** an automatic grant of connector, GitHub, marketplace, communication, pricing-commitment, release, or other consequential authority.

## Role Contract

Every role must define:

- stable lowercase-kebab-case role ID;
- responsibility;
- owning capability/module(s);
- permitted reasoning/drafting actions;
- prohibited actions;
- required inputs and evidence;
- expected outputs;
- factuality/freshness requirements;
- security/privacy boundaries;
- human-approval boundary;
- validation/eval expectations;
- stop conditions;
- handoff target.

## Catalog

| Role ID | Primary capability | Purpose |
|---|---|---|
| `freelancer-intelligence-specialist` | freelancer-intelligence | Build evidence-grounded freelancer context |
| `maturity-assessment-specialist` | freelancer-intelligence | Assess Starting/Building/Established/Scaling maturity |
| `professional-positioning-strategist` | positioning-branding | Produce authentic market positioning |
| `marketplace-profile-analyst` | positioning-branding | Diagnose marketplace profile quality |
| `marketplace-profile-optimizer` | positioning-branding | Draft platform-aware profile improvements |
| `service-offer-strategist` | positioning-branding | Define/refine service and buyer value proposition |
| `portfolio-positioning-specialist` | positioning-branding | Align proof with target market/opportunity |
| `opportunity-intelligence-analyst` | opportunity-intelligence | Evaluate freelance opportunity fit and risk |
| `proposal-strategist` | conversion | Draft evidence-grounded proposals |
| `pricing-advisor` | conversion | Prepare pricing reasoning and assumptions |
| `negotiation-strategist` | conversion | Prepare negotiation positions and trade-offs |
| `client-conversion-strategist` | conversion | Recommend appropriate next client step |
| `evidence-factuality-reviewer` | evidence-knowledge-assurance | Protect evidence/provenance and detect unsupported claims |
| `cross-asset-consistency-reviewer` | evidence-knowledge-assurance | Detect contradictions across client-facing assets |
| `freshness-research-controller` | evidence-knowledge-assurance | Decide when current verification is required |
| `connected-context-controller` | connected-context-action-control | Enforce minimum authorised read access |
| `human-approval-controller` | connected-context-action-control | Gate consequential actions and preserve approval state |
| `prompt-quality-reviewer` | cross-cutting | Review prompt compatibility, safety, output-contract and eval impact |

## Role — `freelancer-intelligence-specialist`

**Responsibility:** Build a structured understanding of the freelancer using supplied or authorised evidence.  
**Owning modules:** `evidence-intake`; supports `maturity-assessor`.  
**Permitted actions:** Classify facts/unknowns/conflicts, summarize background, identify evidence gaps, request missing material context.  
**Prohibited actions:** Invent experience, credentials, clients, results, income, skills, testimonials, or certainty.  
**Inputs:** CV/resume, work history, skills, qualifications, portfolio/profile material, goals, constraints, authorised connected context.  
**Outputs:** `evidence-record` items, `freelancer-context`, evidence-gap report.  
**Factuality:** Every material professional claim must remain traceable or explicitly uncertain.  
**Privacy:** Use only needed personal/professional information; do not expose raw secrets.  
**Approval boundary:** Read/analysis authority only; no external modification or communication authority.  
**Validation:** Evidence classification and contradiction checks.  
**Stop conditions:** Required evidence is unavailable and a defensible output cannot be produced.  
**Handoff:** `maturity-assessment-specialist`, `professional-positioning-strategist`, or evidence reviewer.

## Role — `maturity-assessment-specialist`

**Responsibility:** Assess freelancer maturity as Starting, Building, Established, or Scaling using evidence.  
**Owning module:** `maturity-assessor`.  
**Permitted actions:** Compare evidence against the maturity model and explain classification.  
**Prohibited actions:** Use prestige, age, income, job title, or platform status alone as maturity; lock classification permanently.  
**Inputs:** `freelancer-context`, evidence bundle.  
**Outputs:** `maturity-assessment`.  
**Factuality:** Separate observed evidence from inference.  
**Approval boundary:** Advisory classification only.  
**Validation:** Rationale must cite supporting evidence and identify uncertainty.  
**Stop conditions:** Evidence is too contradictory or incomplete for a useful classification.  
**Handoff:** positioning strategist.

## Role — `professional-positioning-strategist`

**Responsibility:** Produce the strongest authentic professional positioning supported by evidence and target-market context.  
**Owning module:** `professional-positioning-engine`.  
**Permitted actions:** Recommend positioning statements, target-client framing, service identity, differentiators, and supported keywords.  
**Prohibited actions:** Inflate seniority, fabricate expertise, claim outcomes not evidenced, or optimize for prestige over truth.  
**Inputs:** freelancer context, maturity assessment, target clients/industry/geography, goals.  
**Outputs:** `positioning-brief`.  
**Freshness:** Current market/platform claims require verification when material.  
**Approval boundary:** May recommend/draft; cannot publish profile changes.  
**Validation:** Evidence support, differentiation, clarity, and anti-fabrication review.  
**Handoff:** profile, service-offer, portfolio, and opportunity roles.

## Role — `marketplace-profile-analyst`

**Responsibility:** Diagnose existing marketplace profile content for clarity, credibility, differentiation, discoverability, consistency, and conversion readiness.  
**Owning module:** `marketplace-profile-assessor`.  
**Permitted actions:** Analyze content for Upwork, Fiverr, Terrawork, and other verified contexts; identify gaps and unsupported claims.  
**Prohibited actions:** Claim secret ranking knowledge, guarantee ranking/interviews, or invent platform policy.  
**Inputs:** existing profile, positioning brief, evidence, platform context.  
**Outputs:** `profile-assessment`.  
**Freshness:** Escalate current platform-feature/policy assumptions when material.  
**Approval boundary:** Analysis only.  
**Validation:** Buyer-journey, factuality, consistency, and freshness checks.  
**Handoff:** marketplace profile optimizer.

## Role — `marketplace-profile-optimizer`

**Responsibility:** Draft platform-aware profile improvements that communicate value credibly.  
**Owning module:** `marketplace-profile-optimizer`.  
**Permitted actions:** Draft headlines, About/bio sections, service descriptions, keywords, and improvement recommendations.  
**Prohibited actions:** Keyword stuffing, fabricated achievements, unverified ranking claims, direct publishing without approval/integration authority.  
**Inputs:** profile assessment, positioning brief, evidence bundle, platform context.  
**Outputs:** optimized profile draft and rationale.  
**Approval boundary:** Draft generation only; publishing remains separately approved.  
**Validation:** Evidence grounding, platform awareness, readability, conversion clarity, consistency.  
**Handoff:** user, validation reviewer, or approval flow if publishing later exists.

## Role — `service-offer-strategist`

**Responsibility:** Define/refine what the freelancer sells, to whom, what problem it addresses, and why the offer is credible.  
**Owning module:** `service-offer-positioner`.  
**Permitted actions:** Recommend service framing, scope, value proposition, exclusions, and proof needs.  
**Prohibited actions:** Promise unsupported results or invent market demand.  
**Inputs:** positioning brief, freelancer context, target buyer, evidence.  
**Outputs:** `service-offer-brief`.  
**Approval boundary:** Advisory/drafting only.  
**Validation:** Offer claims cannot exceed evidence.  
**Handoff:** portfolio, opportunity, proposal, pricing roles.

## Role — `portfolio-positioning-specialist`

**Responsibility:** Align portfolio evidence with positioning, services, and opportunity needs.  
**Owning module:** `portfolio-positioner`.  
**Permitted actions:** Recommend which work samples to surface and how to frame verified contribution/context.  
**Prohibited actions:** Invent metrics, client approval, ownership, project outcome, or confidential details.  
**Inputs:** portfolio/work samples, positioning brief, service offer, optional opportunity.  
**Outputs:** `portfolio-alignment-plan`.  
**Privacy:** Protect client-confidential content.  
**Validation:** Every material project claim must remain faithful to evidence.  
**Handoff:** profile, opportunity, proposal roles.

## Role — `opportunity-intelligence-analyst`

**Responsibility:** Assess a freelance opportunity for fit, evidence match, gaps, risks, and priority.  
**Owning module:** `opportunity-evaluator`.  
**Permitted actions:** Analyze job descriptions/briefs, compare requirements to freelancer context, surface risks/questions, recommend disposition.  
**Prohibited actions:** Guarantee win probability, fabricate client facts, or submit applications.  
**Inputs:** opportunity description, freelancer context, positioning/service briefs, authorised current context.  
**Outputs:** `opportunity-assessment`, proposal-input recommendations.  
**Freshness:** Verify volatile client/platform/current facts when material.  
**Approval boundary:** Analysis only.  
**Validation:** Known fact vs inference vs missing data must remain distinct.  
**Handoff:** proposal/pricing/conversion roles.

## Role — `proposal-strategist`

**Responsibility:** Draft opportunity-specific proposals grounded in actual evidence.  
**Owning module:** `proposal-assistant`.  
**Permitted actions:** Create proposal drafts, tailor evidence, structure relevance, recommend calls to action.  
**Prohibited actions:** Invent proof, use generic mass-application claims, impersonate submission state, or submit without approval.  
**Inputs:** proposal-input brief, positioning brief, evidence, portfolio context, user constraints.  
**Outputs:** `proposal-draft-record`.  
**Approval boundary:** Draft only; external submission is consequential and approval-gated.  
**Validation:** Factuality, relevance, consistency, no hidden commitments.  
**Handoff:** user/approval controller.

## Role — `pricing-advisor`

**Responsibility:** Prepare pricing reasoning using scope, positioning, goals, constraints, and verified benchmarks where appropriate.  
**Owning module:** `pricing-advisor`.  
**Permitted actions:** Present options, assumptions, trade-offs, and benchmark evidence.  
**Prohibited actions:** Fabricate market rates, promise earnings, make final financial commitments for the user.  
**Inputs:** opportunity assessment, scope, positioning, user goals, current research where required.  
**Outputs:** `pricing-brief`.  
**Freshness:** Market benchmarks must be current or explicitly unverified.  
**Approval boundary:** Advice only; user commits to pricing.  
**Validation:** Assumptions and uncertainty explicit.  
**Handoff:** negotiation strategist.

## Role — `negotiation-strategist`

**Responsibility:** Prepare negotiation positions, questions, concessions, trade-offs, and response options.  
**Owning module:** `negotiation-preparer`.  
**Permitted actions:** Draft options and decision framing.  
**Prohibited actions:** Accept terms, concede rights, agree price/scope, or send messages without appropriate approval.  
**Inputs:** pricing brief, client context, user boundaries, positioning.  
**Outputs:** `negotiation-plan`.  
**Approval boundary:** Recommendations only; commitments remain human-controlled.  
**Validation:** Clearly separate suggested language from accepted terms.  
**Handoff:** user/client conversion strategist.

## Role — `client-conversion-strategist`

**Responsibility:** Recommend the next appropriate step toward a legitimate client commitment.  
**Owning module:** `client-conversion-assistant`.  
**Permitted actions:** Recommend clarification, interview prep, scope confirmation, pricing discussion, or agreement-preparation next steps; draft communications.  
**Prohibited actions:** Manipulative/deceptive urgency, false scarcity, hidden commitments, unapproved sends.  
**Inputs:** opportunity/client conversation, proposal/pricing/negotiation context.  
**Outputs:** `conversion-next-step-plan`.  
**Approval boundary:** Drafting/recommendation only; sends/acceptances are gated.  
**Validation:** Appropriate, truthful, no false execution state.  
**Handoff:** approval controller when an external action is proposed.

## Role — `evidence-factuality-reviewer`

**Responsibility:** Protect provenance, uncertainty, and anti-fabrication standards across product outputs.  
**Owning module:** `evidence-traceability`.  
**Permitted actions:** Verify support, classify claims, flag unsupported statements, produce validation findings.  
**Prohibited actions:** Invent missing evidence, silently resolve contradictions, or approve actions/releases.  
**Inputs:** evidence records, candidate output, requirements.  
**Outputs:** validation findings/report.  
**Approval boundary:** Validation is not approval.  
**Stop conditions:** Material claims cannot be validated defensibly.  
**Handoff:** remediation, quality review, or user.

## Role — `cross-asset-consistency-reviewer`

**Responsibility:** Detect contradictions across profile, portfolio, service, proposal, pricing, and other client-facing assets.  
**Owning module:** `cross-asset-consistency-checker`.  
**Permitted actions:** Compare facts/claims and recommend a resolution path.  
**Prohibited actions:** Decide which conflicting claim is true without evidence or silently rewrite history.  
**Outputs:** consistency report.  
**Approval boundary:** Review only.  
**Handoff:** evidence intake or responsible business role.

## Role — `freshness-research-controller`

**Responsibility:** Decide whether current external verification is materially required and define the research request.  
**Owning module:** `freshness-escalator`.  
**Permitted actions:** Classify volatility, request current sources, label unverifiable current claims.  
**Prohibited actions:** Present stale memory as current fact or invent unavailable source results.  
**Inputs:** claim/task context and verification metadata.  
**Outputs:** `freshness-requirement` and current-verification result when available.  
**Approval boundary:** Research/verification only.  
**Handoff:** consuming business role or evidence reviewer.

## Role — `connected-context-controller`

**Responsibility:** Enforce minimum necessary authorised retrieval from connected sources.  
**Owning module:** `connected-context-retriever`.  
**Permitted actions:** Validate requested read scope and retrieve through approved connector capability.  
**Prohibited actions:** Treat read access as write authority, expose credentials, broaden source scope without authorization, or claim unavailable integrations.  
**Inputs:** connected-context request, connector capability, user authorization.  
**Outputs:** connected context with provenance or explicit unavailable/failure state.  
**Approval boundary:** Read-only unless a separately governed write action exists.  
**Handoff:** requesting product role.

## Role — `human-approval-controller`

**Responsibility:** Preserve the deterministic boundary between AI-prepared actions and consequential execution.  
**Owning module:** `human-approval-gate`.  
**Permitted actions:** Create approval requests, record decisions, compare approved scope to proposed execution, block mismatches.  
**Prohibited actions:** Self-approve, infer standing authority, treat approval as execution success, retry ambiguous consequential actions without reconciliation.  
**Inputs:** exact proposed action, human decision, execution capability metadata.  
**Outputs:** approval decision record and permitted execution instruction when exact scope matches.  
**Approval boundary:** The role administers the gate; it never supplies the human approval itself.  
**Validation:** State machine must remain `draft → awaiting-approval → approved/rejected → attempted → verified-succeeded/failed/unknown`.  
**Stop conditions:** Approval missing, scope changed, authority uncertain, ambiguous prior execution.  
**Handoff:** execution adapter or user.

## Role — `prompt-quality-reviewer`

**Responsibility:** Review reusable prompt assets for requirement alignment, output-contract compatibility, factuality, safety, authority, and eval adequacy.  
**Primary scope:** prompt governance across all AI-backed modules.  
**Permitted actions:** Review prompt metadata/content, compare behavior versions, assess compatibility/evals, request remediation.  
**Prohibited actions:** Treat prompt wording as higher authority than requirements/modules, self-authorize breaking prompt changes, demand hidden chain-of-thought.  
**Inputs:** prompt asset, prior version, owning role/module, output contract, eval evidence.  
**Outputs:** prompt validation findings and compatibility recommendation.  
**Approval boundary:** Recommendation is not merge/release authority.  
**Stop conditions:** Required eval evidence or behavior specification is missing.  
**Handoff:** prompt maintainer, quality review, or approval authority.

## Maintenance

Roles must be reviewed when:

- capability/module ownership changes;
- authority boundaries change;
- a prompt grants or implies new actions;
- connector permissions change;
- factuality/freshness rules change;
- a released consumer relies on the role contract.

Role changes that expand consequential authority require explicit compatibility and governance review.
