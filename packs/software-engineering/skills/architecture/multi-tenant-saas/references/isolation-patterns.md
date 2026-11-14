# Resource Isolation Patterns

Choose isolation for each resource class against the service promise, not with one global choice. A product can pool application compute, isolate selected data, and reserve dedicated resources for a defined tier or regulatory requirement.

| Pattern | Typical tradeoff to evaluate |
|---|---|
| Pooled | Shared resources can improve utilization and fleet-wide operations; require enforceable tenant context, fairness, and scoped recovery. |
| Bridge | Shared and dedicated components are combined; placement, identity, and cross-resource consistency become more complex. |
| Silo | Dedicated resources can narrow some blast radii and meet specific promises; provisioning, upgrades, cost, and fleet variation grow. |
| Hybrid | Different patterns fit different resource classes or tiers; governance and migration paths must prevent policy drift. |

For each resource—primary database, object storage, cache, queue, search, analytics, encryption keys, backups, and runtime compute—record:

- tenant ownership and authoritative identifier;
- enforcement point and denied-access behavior;
- whether the resource is shared, dedicated, or partitioned;
- blast radius, noisy-neighbor behavior, and operational owner;
- export, restore, deletion, and tenant-move implications;
- cost attribution and the evidence or promise supporting the choice.

Evaluate actual constraints: contractual and regulatory commitments, data sensitivity, traffic and data skew, residency, recovery objectives, support model, team capabilities, and unit economics. Tenant count alone is not a sufficient decision rule. Neither pooled nor siloed resources are automatically secure; verify the controls and operational paths in either model.

### AWS SaaS Lens basis

The [general design principles](https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/general-design-principles.html), [isolation mindset](https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/isolation-mindset.html), and [tier-based isolation](https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/tier-based-isolation.html) emphasize that isolation is resource-specific and that architecture should reflect tenant tiers and isolation requirements. AWS service examples are not provider-neutral prescriptions.

### Source basis

Adapted from [magnus919/agent-skills `tenancy-and-data-partitioning-models.md`](https://github.com/magnus919/agent-skills/blob/main/multi-tenant-saas-architecture/references/tenancy-and-data-partitioning-models.md).
