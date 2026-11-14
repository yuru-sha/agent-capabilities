# Tenant Onboarding and Lifecycle

Treat onboarding and lifecycle actions as explicit, auditable state transitions across systems, not as one assumed atomic signup transaction. Identify the authority, retry behavior, and user-visible outcome for each step.

## Provisioning path

1. Validate the account, intended tenant, region, plan, owner, and required service commitments.
2. Establish identity and membership through the selected identity authority.
3. Create tenant desired state and provision dependent resources using idempotency keys or equivalent duplicate protection.
4. Initialize policy, configuration, entitlements, and tenant-specific resource placement.
5. Confirm readiness and publish the tenant as usable only when required steps succeed.
6. Reconcile partial failure, retries, timeouts, and duplicate events; compensate or resume safely rather than leaving untracked resources.

## Lifecycle coverage

Model at least pending/provisioning, active, suspended, reactivating, deleting, and deleted states as applicable. For each transition define who may trigger it, required approval, side effects, retry semantics, in-flight request/job behavior, audit record, and recovery path.

- **Plan or entitlement change:** define authority, effective time, propagation, and behavior when policy systems disagree.
- **Suspension/reactivation:** specify new request and job behavior, data retention, access restoration, and queued work disposition.
- **Tenant move:** plan placement changes, consistency checks, rollback, and preservation of identity and external references.
- **Export/restore:** enumerate primary and derived resources, verify tenant scope and completeness, and protect temporary artifacts.
- **Deletion:** cover databases, object storage, caches, queues, indexes, replicas, backups, logs, and derived data; distinguish deletion from retention/legal hold obligations.

Use background orchestration where actions span systems, with observable progress and reconciliation. Avoid claiming cross-system atomicity without a mechanism that provides it.

### AWS SaaS Lens basis

AWS [general design principles](https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/general-design-principles.html) call for repeatable automated onboarding and tenant-aware operation. Lifecycle authority and idempotent recovery are derived design requirements, not a prescribed AWS workflow.

### Source basis

Adapted from the lifecycle and handoff framing in [magnus919/agent-skills `onboarding-identity-entitlements-metering-billing.md`](https://github.com/magnus919/agent-skills/blob/main/multi-tenant-saas-architecture/references/onboarding-identity-entitlements-metering-billing.md). Pricing and financial modeling remain outside this Skill.
