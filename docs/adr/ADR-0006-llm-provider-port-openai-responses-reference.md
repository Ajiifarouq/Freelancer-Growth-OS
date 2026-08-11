# ADR-0006 — LLM Provider Port with OpenAI Responses Reference Adapter

**Status:** Accepted  
**Date:** 2026-08-11

## Decision

Define an `LLMProvider` application port and implement OpenAI's Responses API as the first reference adapter. Keep provider and model selection in runtime configuration rather than domain contracts.

## Drivers

- The product needs structured generation, semantic reasoning, and controlled tool use.
- Current OpenAI Responses-capable models support function calling and structured outputs, and selected models support provider tools such as web search.
- Product logic must remain portable across providers.
- Model quality/cost changes faster than domain requirements.

## Alternatives

- Hard-code one model/provider throughout modules: rejected because it creates unnecessary vendor and model coupling.
- Multi-agent/provider router in V1: rejected because complexity is not yet justified by eval evidence.
- LLM-free system: rejected because several approved product capabilities require semantic generation/reasoning.

## Consequences

- Domain/application contracts cannot expose provider-specific response classes.
- Model names are configuration and require evals when changed.
- Structured outputs are validated before entering product state.
- Current-source web/search may be implemented through the provider adapter, but business modules depend only on the research port.
- Provider outages/failures return explicit workflow states.
