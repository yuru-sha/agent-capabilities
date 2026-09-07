---
name: postgresql-roles-rls
description: "Use when PostgreSQL roles, grants, default privileges, row-level security, SECURITY DEFINER, or tenant isolation change."
---

# PostgreSQL Roles and RLS

Use with `postgresql-review`, `postgresql-transactions`, and the security
reviewer for every authorization boundary.

## Check

- Map application, migration, owner, read-only, administrative, and maintenance roles; verify least privilege and default privileges for future objects.
- Check RLS enablement, policies, `USING`/`WITH CHECK`, role inheritance, table owners, `BYPASSRLS`, and fail-closed behavior.
- Audit `SECURITY DEFINER` functions, fixed `search_path`, executable privileges, dynamic SQL, and role switching.
- Test cross-tenant reads, writes, joins, views, functions, background jobs, and migrations with real role identities.
- Document backup, restore, replication, connection-pool, and local-development implications of the access model.

