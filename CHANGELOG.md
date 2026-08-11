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
- `.editorconfig` enforcing UTF-8, LF endings, and final-newline hygiene for future text edits.

### Changed

- Repository governance, README, and roadmap now distinguish governed active product assets from historical/external prompt and workflow material.
- Historical Fiverr/Upwork/Terrawork marketplace prompt concepts are mapped into current governed modules, roles, templates, and prompts rather than imported as duplicate authorities.
- Historical LinkedIn profile-optimizer material is explicitly preserved outside current active scope pending a future product decision.
- Historical adoption/release prompts are classified as legacy workflow history rather than product-runtime prompts.
- Prompt behavior changes remain subject to compatibility/eval review and versioning when stable consumers depend on them.

### Security

- Human approval remains mandatory before consequential external actions.
- Prompt text and role assignment cannot grant consequential execution authority.
- Retrieved/connected/external content is treated as untrusted data and cannot override product governance.
- Historical prompt content cannot silently override active requirements, architecture, roles, modules, permissions, or approval gates.
- Secrets remain outside product-domain data and governed prompt context.

### Notes

- Product implementation has not started.
- No direct marketplace/account integrations are claimed.
- No product version has been released.
- Detailed Client Success and Business Growth prompts remain intentionally deferred until their requirements/module contracts are sufficiently specified.
- A minor existing Markdown terminal-newline formatting debt remains documented as non-blocking; `.editorconfig` prevents recurrence in compliant editors/tools.
- This `Unreleased` section is not evidence of a published release.
