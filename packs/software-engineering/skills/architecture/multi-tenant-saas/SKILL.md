---
name: multi-tenant-saas
description: Design or review a multi-tenant SaaS architecture across tenant semantics, resource isolation, identity-bound context, PostgreSQL RLS, asynchronous jobs, caches, onboarding, lifecycle, operations, and cross-tenant testing. Use when a product serves multiple customer tenants on shared or mixed infrastructure. Not a substitute for implementation-specific security, database, API, privacy, or capacity review.
---

# Multi-Tenant SaaS Architecture

Design tenant boundaries end to end. A `tenant_id` column alone is not an isolation architecture: requests, database access, asynchronous work, caches, storage, operations, and tests must use a coherent tenant authority and enforcement model.

Use the [AWS SaaS Lens](https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/saas-lens.html) as a design rationale, not as a mandate to use AWS products. Apply its principles provider-neutrally: no universal tenancy model, isolate resources across layers, bind tenant context to authenticated identity, automate repeatable onboarding, and operate with tenant-aware evidence. The Lens is AWS-focused; validate provider-specific choices against current vendor documentation.

## Workflow

1. **Frame the service promise.** Establish customer/account concepts, user and operator roles, regions, data classes, contractual isolation and recovery promises, expected tenant scale and skew, lifecycle states, and unknowns. Separate commitments from assumptions.
2. **Define tenant authority and vocabulary.** Load `references/tenant-model.md`. Identify who owns tenant identity and membership, which system is authoritative, and how account, tenant, user, subscription, entitlement, and resource relate.
3. **Map every tenant-bearing resource.** Load `references/isolation-patterns.md`. For each data store, compute, object, cache, queue, search index, analytics copy, and backup, record its ownership boundary, isolation enforcement, failure blast radius, restore/deletion behavior, and decision owner. Compare pooled, bridge, silo, and hybrid choices per resource; do not choose by tenant count alone.
4. **Trace identity and context end to end.** Load `references/tenant-context.md` and `references/authentication-authorization.md`. Trace authenticated identity to authorized membership, request/service calls, background jobs, and storage operations. Treat tenant context as trusted only after authorization; never accept a caller-supplied tenant selector as proof of access.
5. **Design database enforcement.** For PostgreSQL, load `references/postgresql-rls.md` and compose the PostgreSQL roles/RLS specialist. Treat RLS as a database enforcement layer, not a replacement for application authorization or correct role design.
6. **Model onboarding and lifecycle.** Load `references/onboarding-lifecycle.md`. Cover idempotent provisioning, retries and partial failures, entitlement changes, suspension/reactivation, export, restore, deletion, and cleanup across dependent resources.
7. **Design tenant-aware operations and tests.** Load `references/tenant-aware-operations.md`. Cover queue and cache boundaries, noisy-neighbor controls, tenant-aware observability, and an automated cross-tenant test matrix across every access path.
8. **Record decisions and evidence gaps.** State alternatives, tradeoffs, owners, assumptions, failure behavior, verification evidence, and triggers to revisit. Route detailed controls to the specialist owners listed below.

## Output contract

Produce a concise architecture decision record containing:

- tenant/account vocabulary and authoritative identity/membership source;
- resource-by-resource isolation model and enforcement point;
- request and asynchronous tenant-context flow, including trust boundaries;
- PostgreSQL RLS role, policy, and connection/transaction model when applicable;
- cache key and storage namespace boundaries;
- onboarding and tenant lifecycle states, retries, and cleanup;
- cross-tenant test matrix and evidence still missing;
- operational visibility, noisy-neighbor response, and recovery/deletion scope;
- assumptions, decision owners, alternatives, and revisit triggers.

## Ownership boundaries

- Authentication, authorization, threat modeling, and security evidence: `web-security-review`, `security-review`, and applicable language/database security Skills.
- PostgreSQL roles, grants, RLS, and connection semantics: PostgreSQL database Skills and `database-reviewer`.
- API, event, and webhook contracts: OpenAPI/API specialists.
- Service, job, cache, and storage implementation: relevant language, Redis, and messaging Skills.
- Privacy/legal retention and deletion requirements: project privacy/compliance owner.
- Quantitative capacity, quotas, and unit-cost evidence: capacity/platform specialists.

This Skill owns the cross-layer architecture decisions and their handoffs; it does not prescribe a framework, ORM, tenancy model, or cloud provider.

## Source basis

This Skill adapts the decision-oriented workflow and ownership boundaries of [`magnus919/agent-skills` `multi-tenant-saas-architecture`](https://github.com/magnus919/agent-skills/tree/main/multi-tenant-saas-architecture), distributed under MIT; its copyright and permission notice is included in [`LICENSE.md`](LICENSE.md). It uses the [AWS Well-Architected SaaS Lens](https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/saas-lens.html) as its design rationale. The references here are rewritten for this repository's provider-neutral scope and add explicit PostgreSQL RLS, asynchronous context propagation, cache isolation, and automated cross-tenant testing. Neither source replaces current implementation documentation or project-specific evidence.
