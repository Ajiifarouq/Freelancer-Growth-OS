# Freelancer Growth OS Governance

## Purpose

This document defines the product-level governance contract for Freelancer Growth OS and its adoption of shared GrowthOS Engineering governance.

## Authority and Dependency

Freelancer Growth OS adopts the following immutable shared-governance baseline:

- **Repository:** `Ajiifarouq/GrowthOS-Engineering`
- **Tag:** `v0.1.0`
- **Commit:** `7ee056f938e12b5a72d1ee919a27f05ec5297c69`

The dependency direction is:

`Freelancer Growth OS → GrowthOS Engineering`

GrowthOS Engineering remains authoritative for shared engineering governance. This repository remains authoritative for Freelancer Growth OS product-specific requirements and implementation.

## Baseline Pinning Rules

- Do not treat upstream `main` as the governing baseline.
- Governance adoption changes must identify the exact new tag and commit SHA.
- An upstream update does not automatically modify this product repository's governing baseline.
- Compatibility impact must be reviewed before adopting a newer GrowthOS Engineering release.
- Historical released baselines must remain traceable.

## Product-Specific Extensions

This repository may extend shared governance when the extension:

- is explicitly product-specific;
- does not contradict a shared architectural invariant;
- identifies its scope and rationale;
- documents compatibility impact;
- records required approval when the extension changes a protected governance boundary.

## Deviations

A deviation from the pinned shared baseline must document:

- the upstream rule affected;
- the reason for deviation;
- product scope affected;
- risk and compatibility impact;
- compensating controls where relevant;
- approving authority;
- review or exit condition where relevant.

Do not silently override shared governance.

## Protected Actions

The following remain separately authorized actions:

- creating or moving branches used for governed delivery;
- committing or pushing candidate changes;
- creating pull requests;
- modifying the default branch;
- merging pull requests;
- creating or moving tags;
- publishing releases or other artifacts;
- changing repository visibility or security settings;
- destructive history rewrites;
- modifying another repository.

Authorization for one protected action does not automatically authorize another unless the authorization explicitly bundles the named actions and scope.

## Evidence and Factuality

Do not invent product features, customers, users, revenue, integrations, metrics, deployments, approvals, release state, test results, or operational evidence. Distinguish verified repository facts from proposals and placeholders.

## Security and Privacy

Do not commit secrets, credentials, tokens, private keys, unnecessary personal data, or sensitive operational information. Security and privacy controls from the pinned GrowthOS Engineering baseline remain applicable.

## Adoption Lifecycle

The controlled adoption sequence is:

1. Product Governance Entry Layer.
2. Architecture and Standards Alignment.
3. Workflow and Versioning Alignment.
4. Templates, Roles, and Prompts Alignment.
5. Existing Product Content Conformance.
6. Integrated Adoption Audit and Product Release Readiness.

A later stage must not be represented as complete until its required artifacts and verification exist.

## Current Status

Current stage: **Phase 1 — Product Governance Entry Layer**.

No product release is implied by this governance adoption work.
