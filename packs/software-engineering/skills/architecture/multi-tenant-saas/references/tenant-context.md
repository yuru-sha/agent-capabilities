# Tenant Context Flow

Tenant context must be established from an authenticated subject and an authorized membership, then remain explicit through every operation that can access tenant-owned resources. It is not a free-form request parameter and not a substitute for authorization.

## Trace the context

1. Authenticate the user or service identity.
2. Resolve the requested tenant against that identity's active membership or an explicit service authorization grant. If a client selects among memberships, treat that selection only as a lookup input and authorize it server-side.
3. Create an immutable, request-scoped context containing the authorized tenant and the minimum required subject, role, and trace information.
4. Pass the context through service calls and data-access boundaries. Define how service-to-service calls authenticate the originating authority and how revocation/status changes are observed.
5. At every resource boundary, enforce tenant scope independently of resource identifiers. Do not assume a UUID, opaque ID, or earlier gateway check provides isolation by itself.
6. Fail closed when required tenant context is absent, malformed, stale, or inconsistent. Do not silently fall back to a global/default tenant.

Do not put tenant authority in mutable ambient state unless its lifetime and concurrency isolation are guaranteed. Avoid hidden global variables or request-local context leaking across concurrent tasks. Log safe tenant identifiers for diagnosis only where permitted; never log credentials or sensitive payloads.

## Asynchronous propagation

An asynchronous message must carry a stable tenant reference and enough authenticated provenance for the consumer to re-authorize it. Validate the tenant and operation at consumption time against the chosen source of truth; do not trust arbitrary producer-controlled payload fields. Define behavior for suspended/deleted tenants, changed membership, stale entitlements, retries, replay, delayed messages, and dead-letter handling. Preserve context in trace metadata without treating observability metadata as authorization.

For scheduled/system work, use an explicit service identity and a narrowly scoped tenant grant or a separately reviewed cross-tenant operation. Never infer tenant context from whichever record happens to be processed first.

### AWS SaaS Lens basis

AWS [identity and access management](https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/identity-and-access-management.html) recommends binding tenant context to authenticated identity and making it available through the architecture. [Preventing cross-tenant access](https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/preventing-cross-tenant-access.html) illustrates runtime tenant-scoped access. Apply these principles to the system's actual identity and authorization mechanisms; a token claim alone does not authorize access.

### Source basis

The context flow extends the identity and application-plane handoff concepts in [magnus919/agent-skills `control-and-application-planes.md`](https://github.com/magnus919/agent-skills/blob/main/multi-tenant-saas-architecture/references/control-and-application-planes.md).
