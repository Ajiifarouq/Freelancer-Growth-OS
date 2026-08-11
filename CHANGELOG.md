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

### Changed

- Repository governance, agent rules, and roadmap now treat reusable templates, roles, and prompts as governed product assets rather than informal text.
- Prompt behavior changes are explicitly subject to compatibility/eval review and versioning when stable consumers depend on them.

### Security

- Human approval remains mandatory before consequential external actions.
- Prompt text and role assignment cannot grant consequential execution authority.
- Retrieved/connected/external content is treated as untrusted data and cannot override product governance.
- Secrets remain outside product-domain data and governed prompt context.

### Notes

- Product implementation has not started.
- No direct marketplace/account integrations are claimed.
- No product version has been released.
- Detailed Client Success and Business Growth prompts remain intentionally deferred until their requirements/module contracts are sufficiently specified.
- This `Unreleased` section is not evidence of a published release.
