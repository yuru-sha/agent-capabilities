# Authentication and Authorization Boundaries

Bind tenant identity to authenticated identity without conflating authentication, membership, and permission. A valid user token proves an identity according to its issuer; it does not automatically prove current membership, tenant status, or permission to access every resource in a tenant.

## Required decisions

- Identify the identity authority for users, service principals, and operators.
- Define whether a user may belong to multiple tenants and how an active tenant is selected and validated.
- Specify membership roles and resource/action permissions, including least privilege and default-deny behavior.
- Define how membership revocation, tenant suspension, entitlement updates, and token/session revocation take effect, including any accepted propagation delay.
- Separate ordinary tenant operations from support, platform administration, and cross-tenant analytics. Require a distinct authorization path, explicit purpose, audit trail, and bounded privileges for exceptional access.
- For service-to-service calls, identify the originating principal and preserve authorized tenant scope. Do not blindly forward user claims or elevate a service to global access.
- Decide which checks run in the application, data layer, and resource provider. Layered controls must agree on the same authoritative tenant relationship.

Test forged tenant selectors, cross-tenant object references, inactive memberships, stale credentials, privilege escalation, and support/admin routes. Identifier secrecy and client-side route hiding are not authorization controls.

### AWS SaaS Lens basis

The AWS [identity and access management](https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/identity-and-access-management.html) guidance describes a tenant-aware SaaS identity. This reference generalizes the identity-to-tenant binding and does not prescribe Cognito, JWT claims, or another provider-specific mechanism.
