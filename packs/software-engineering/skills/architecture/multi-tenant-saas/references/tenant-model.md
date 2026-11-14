# Tenant Model and Authority

Start from the customer promise and domain vocabulary, not from a `tenant_id` column. A tenant is the boundary whose data, policy, usage, and service experience are managed together; it may be called an organization, account, workspace, or another domain object. Use the term consistently and make its authority explicit.

## Define the domain

For each concept, document its owner, identifier, cardinality, lifecycle authority, audit needs, and cross-tenant visibility:

- **Tenant:** customer boundary, status, region, and service commitments.
- **Account or organization:** commercial payer, operating group, or both; whether it can own multiple tenants.
- **User and membership:** whether identity is global or tenant-local; how multiple memberships and tenant switching are authorized.
- **Subscription and entitlement:** which authority defines plan state, feature access, limits, and effective dates.
- **Resource:** tenant-owned, platform-owned, or intentionally shared; ownership and transfer rules.
- **Environment:** production, test, or regional environments and their distinct data/lifecycle promises.

A global identity provider does not make application authorization global. Membership and its active status remain an explicit authorization decision. Avoid deriving tenant ownership from mutable display names, email domains, or user-provided identifiers.

## Boundary questions

- Can every tenant-owned resource be mapped to one authoritative tenant or an explicitly modeled shared-access policy?
- Who can create, suspend, transfer, restore, export, and delete a tenant?
- What operator/support access exists, how is it authorized, audited, and time-bounded?
- What happens when membership, tenant status, subscription, or entitlement changes while work is in flight?
- Which promises apply to data residency, backup, restore, retention, and deletion?

Keep detailed schema mechanics with the relevant data specialist and API contracts with the API owner. Do not let storage layout silently define product semantics.

## Source basis

Adapted from the domain-boundary approach in [magnus919/agent-skills `tenant-domain-model-and-boundaries.md`](https://github.com/magnus919/agent-skills/blob/main/multi-tenant-saas-architecture/references/tenant-domain-model-and-boundaries.md). The AWS [SaaS Lens identity and access management](https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/identity-and-access-management.html) guidance treats tenant context as part of the SaaS identity; this reference applies that principle without requiring AWS services.
