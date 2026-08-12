# ADR-0006 — LLM Provider Port with OpenAI Responses Reference Adapter

**Status:** Accepted with current-verification requirement  
**Date:** 2026-08-11  
**Provider capability/data-controls last verified:** 2026-08-12

## Decision

Define an `LLMProvider` application port and use OpenAI's Responses API as the first reference adapter, subject to [PROVIDER_DATA_POLICY.md](../../PROVIDER_DATA_POLICY.md). Keep provider/model/tool selection in controlled runtime configuration rather than domain contracts.

## Verified Drivers

Official OpenAI documentation checked on 2026-08-12 supports the architecture's required reference capabilities, including:

- Responses API;
- custom function/tool calling;
- Structured Outputs/JSON Schema for supported model/configurations;
- built-in web search;
- API data controls described in the provider data policy.

Primary sources are recorded in [PROVIDER_DATA_POLICY.md](../../PROVIDER_DATA_POLICY.md), which is the current provider-verification authority.

## Architecture Drivers

- The product needs structured semantic generation/reasoning for approved modules.
- Product logic must remain portable across providers.
- Model quality/cost/capabilities/retention change faster than domain requirements.
- Provider processing of private/client/business data requires explicit minimisation and retention awareness.

## Alternatives

- Hard-code one model/provider throughout modules: rejected because it creates unnecessary vendor/model coupling.
- Multi-agent/provider router in V1: rejected because complexity is not justified by eval evidence.
- LLM-free product: rejected because several approved capabilities require semantic generation/reasoning.

## Consequences

- Domain/application contracts cannot expose provider-specific response classes.
- Canonical outputs validate through [CONTRACT_REGISTRY.md](../../CONTRACT_REGISTRY.md).
- Provider/model/tool names are controlled configuration and must be allowlisted.
- Model/provider/tool changes require capability/privacy reverification and regression evals when material.
- Structured outputs are validated before entering product state.
- Current-source web/search may be implemented through the provider adapter, but business modules depend only on the research port.
- Provider outages/failures return explicit workflow states.
- External-provider processing follows `PROVIDER_DATA_POLICY.md`; `not used for training by default` must not be misrepresented as `not retained`.
- Capability/data-control assumptions are reverified before first credentialed implementation, before release, on material provider changes, and at least every 90 days while provider-backed implementation is active.
