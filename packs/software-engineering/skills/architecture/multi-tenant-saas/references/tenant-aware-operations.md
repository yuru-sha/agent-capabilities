# Tenant-Aware Operations, Caches, and Tests

Operational readiness must account for individual tenant behavior, not only fleet averages. Define tenant-aware metrics and actions without exposing sensitive tenant data or turning tenant identifiers into high-cardinality labels without a deliberate policy.

## Caches and derived resources

- Include the authorized tenant boundary in every cache key for tenant-owned values. Include other isolation dimensions when needed, such as environment, region, principal, permission/entitlement version, locale, or representation.
- Prevent cache reads, writes, invalidation, and stampede coordination from crossing tenant boundaries. Review shared caches, negative caches, CDN behavior, and cache warming separately.
- Treat tenant identifiers from callers as untrusted until authorized. Namespace object-storage keys and search/index records by authoritative ownership, then enforce access at the resource boundary; path naming alone is not an access control.
- Define invalidation and expiry behavior when membership, tenant status, entitlements, or data changes. Test stale and reused entries across tenant switches.
- Track queued jobs and derived artifacts back to their tenant and lifecycle state; ensure retries and cleanup do not operate on another tenant's resources.

## Automated cross-tenant test matrix

Build reusable fixtures for at least two distinct tenants and identities with different membership states. Add automated tests that attempt allowed and denied behavior across:

- reads, creates, updates, deletes, list/search, joins/relations, bulk operations, and raw SQL;
- direct object references, tenant switching, missing or forged tenant context, and stale membership;
- async producers/consumers, retry and replay, delayed work, scheduled tasks, and dead-letter handling;
- cache hit/miss, key separation, invalidation, and context reuse under concurrent requests;
- object storage, search, exports, admin/support routes, and tenant suspension/deletion where applicable;
- PostgreSQL RLS using the real application role, including absent context and transaction/connection reuse paths.

Tests should prove both isolation (tenant A cannot read or mutate B's resources) and legitimate behavior (each tenant can access its own permitted resources). Run them in CI and keep the fixtures representative of actual role and execution identities. Add new cases when resource types or access paths are introduced.

## Operational scenarios

Record detection and response for a hot tenant/noisy neighbor, tenant-scoped restore, export/deletion, placement change, cache or queue backlog, and tenant-level cost anomaly. State metric owner, decision threshold source, customer/support communication, and recovery authority; do not invent universal thresholds. Make administrative cross-tenant access auditable and exceptional.

### AWS SaaS Lens basis

AWS [general design principles](https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/general-design-principles.html) call for tenant-aware operational views, tenant metrics, cost visibility, and resource isolation. This guidance is provider-neutral and supplements, rather than replaces, the service's operational and privacy policies.

### Source basis

Adapted from the scenarios in [magnus919/agent-skills `tenant-aware-operations-capacity-and-cost.md`](https://github.com/magnus919/agent-skills/blob/main/multi-tenant-saas-architecture/references/tenant-aware-operations-capacity-and-cost.md).
