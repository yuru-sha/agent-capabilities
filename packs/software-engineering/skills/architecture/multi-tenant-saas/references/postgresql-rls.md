# PostgreSQL Row-Level Security for Tenant Isolation

Use PostgreSQL Row-Level Security (RLS) as one enforcement layer for tenant-owned rows, alongside application authentication and authorization. Compose this reference with the repository's PostgreSQL roles/RLS, transaction, and review Skills. Verify all behavior against the PostgreSQL version and actual connection driver in use.

## Design and verify

- Inventory tenant-owned tables and explicitly classify global or shared tables. Review views, partitions, functions, procedures, and indirect access paths as well as base tables.
- Define policies for every relevant command. Check both row visibility (`USING`) and accepted row values (`WITH CHECK`) for reads, inserts, updates, and deletes as appropriate.
- Verify behavior with the actual application role, table owner, migration role, read-only role, and administrative role. Check table ownership, role inheritance, `BYPASSRLS`, `FORCE ROW LEVEL SECURITY`, grants, and policy combinations; superuser or bypass testing does not prove tenant isolation.
- Set tenant context only after authentication and membership authorization. If using a transaction-local setting, set it inside the same explicit transaction and use the same checked-out connection for every query in that unit of work.
- Verify missing, malformed, and stale context denies access. Use a setting and cast/policy strategy that fails closed under the application's actual behavior; test it rather than assuming a missing setting returns an empty result.
- Verify commit, rollback, exceptions, cancellation, retries, and pool return paths. Transaction-local context should not be treated as persistent connection state; ensure every code path ends its transaction before the connection is reused.
- Keep migration and maintenance privileges separate from normal application roles. Explicitly review any cross-tenant admin operation and its separate authorization and audit path; do not add a broad bypass role to routine request paths.
- Exercise raw SQL, joins, nested access, background workers, exports, and any ORM-generated queries. RLS does not fix incorrect tenant authorization or unsafe privileged functions.

Do not use opaque identifiers as a substitute for authorization. Do not assume that enabling RLS alone protects table owners, privileged roles, views, functions, or code paths outside the intended transaction.

### AWS SaaS Lens basis

The AWS [SaaS Lens tenant isolation](https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/tenant-isolation.html) and [preventing cross-tenant access](https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/preventing-cross-tenant-access.html) topics establish isolation as a resource-level security requirement. The PostgreSQL controls above are database-specific implementation considerations, not AWS requirements.
