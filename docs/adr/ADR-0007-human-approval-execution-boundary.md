# ADR-0007 — Deterministic Human-Approval Execution Boundary

**Status:** Accepted  
**Date:** 2026-08-11

## Decision

Consequential external actions are controlled by a deterministic application state machine. AI modules may create drafts and `ApprovalRequest` objects but cannot directly invoke write/submit/publish executors.

## Drivers

- `FGOS-D004` explicitly chooses Connected but Human-Approved authority.
- External actions can affect money, reputation, client relationships, or remote accounts.
- LLM output is probabilistic and retrieved content may be malicious/prompt-injected.
- Approval must bind to the exact action, not a vague standing permission.

## Required flow

`draft → awaiting-approval → approved/rejected → attempted → verified-succeeded/failed/unknown`

## Alternatives

- Direct model tool execution: rejected for consequential actions.
- Standing broad autonomous permission: rejected under current owner decision.
- Human review of final output without technical enforcement: rejected because UI convention alone is bypassable.

## Consequences

- Action payload/target changes require re-approval.
- Read and write connector scopes remain separate.
- Ambiguous execution becomes `unknown` and requires reconciliation rather than blind retry.
- Execution evidence is stored separately from approval.
