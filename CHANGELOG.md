# Changelog

All notable Freelancer Growth OS product changes should be recorded here once release versioning becomes active.

The format preserves an `Unreleased` section for merged work that has not been published as a product release.

## Unreleased

### Added

- Product governance foundation.
- Product requirements baseline.
- Capability and module architecture.
- Technical architecture and architecture decision records.
- Product engineering workflow.
- Product versioning policy.
- Compatibility and migration policy.
- Controlled release process.
- Product template library for evidence, specifications, outputs, validation, approvals, execution results, prompt changes, and release candidates.
- Product role library with explicit responsibility and authority boundaries.
- Prompt governance for hierarchy, metadata, versioning, factuality, freshness, prompt injection, structured outputs, evals, compatibility, and human approval.
- Initial governed prompt library with 15 prompt assets mapped to Growth Acquisition and assurance modules.
- Product content conformance register mapping current, historical, duplicate, superseded, legacy, proposed, and out-of-scope content.
- Phase 5 adoption/conformance report.
- Phase 6 integrated adoption and product release-readiness audit.
- `.editorconfig` enforcing UTF-8, LF endings, and final-newline hygiene for future text edits.
- `.gitignore` excluding local secrets, databases, runtime/user data, exports, backups, logs, and common local tooling artifacts.
- CODEOWNERS repository-owner boundary.
- Governance/repository safety CI and deterministic repository validation script.
- `DECISION_REGISTER.md` reconciling current decisions with historical Phase 2A open-state records.
- `CONTRACT_REGISTRY.md` defining canonical product contracts, aliases, versions, prompt mappings, evidence state, and artifact staleness.
- `DATA_GOVERNANCE.md` defining local workspace lifecycle, retention, deletion, export, backup, storage-location, and real-data gates.
- `PROVIDER_DATA_POLICY.md` defining provider data minimization, retention awareness, current OpenAI capability verification, and reverification requirements.
- `REPOSITORY_SECURITY_BASELINE.md` defining branch/ruleset/secret/review enforcement targets.
- `PRE_IMPLEMENTATION_HARDENING_REPORT.md` reconciling late Phase 6 findings and broader pre-implementation risks.

### Changed

- Repository governance, README, architecture, and roadmap now distinguish governed active product assets from historical/external prompt/workflow material and from the active pre-implementation hardening gate.
- Historical Fiverr/Upwork/Terrawork marketplace prompt concepts remain mapped into current governed modules, roles, templates, and prompts rather than imported as duplicate authorities.
- Historical LinkedIn profile-optimizer material remains outside current active scope pending a future product decision.
- Historical adoption/release prompts remain legacy workflow history rather than product-runtime prompts.
- Prompt behavior changes remain subject to compatibility/eval review and versioning when stable consumers depend on them.
- The six-phase governance-adoption sequence remains complete, but routine implementation is now explicitly blocked until pre-implementation hardening is merged/verified and applicable repository settings are configured.
- Phase 2A open decisions that were later resolved are reconciled through the current decision register rather than left ambiguous for implementation agents.
- Contract/output synonyms are resolved through a canonical registry rather than allowing duplicate Pydantic/persistence schemas.
- Evidence verification, derived-artifact staleness, and consequential approval replay/idempotency controls are explicit deterministic boundaries.

### Security

- Human approval remains mandatory before consequential external actions.
- Prompt text and role assignment cannot grant consequential execution authority.
- Retrieved/connected/external content is treated as untrusted data and cannot override product governance.
- Historical prompt content cannot silently override active requirements, architecture, contracts, roles, modules, permissions, or approval gates.
- Secrets remain outside product-domain data and governed prompt context.
- Real user/client/business runtime data is prohibited from the Git working tree regardless of repository visibility.
- External provider processing is subject to minimum-necessary disclosure and provider-retention awareness.
- Stale/invalid artifacts cannot drive consequential execution.
- Approval must bind to the exact action payload and support replay/double-execution protection when execution is implemented.

### Notes

- Product implementation has not started.
- Repository governance CI now exists as a hardening candidate; application CI/runtime tests/database migrations/AI eval execution/backup-restore validation still do not exist because implementation has not started.
- Real personal/client/business data must not be used for implementation/evals until required data/security controls are implemented and tested; synthetic fixtures should be used first.
- No direct marketplace/account integrations are claimed.
- No product version has been released.
- Detailed Client Success and Business Growth prompts remain intentionally deferred until their requirements/module contracts are sufficiently specified.
- Existing Markdown terminal-newline debt remains detectable by governance CI and should be normalized rather than hidden.
- Repository license, visibility/IP strategy, Wiki status, branch protection/rulesets, secret scanning/push protection, and unwanted automated-review settings are tracked as manual/owner settings in issue #9.
- This `Unreleased` section is not evidence of a published release.
