---
name: mysql-roles-privileges
description: "Use when MySQL users, roles, grants, DEFINER security context, authentication, TLS, or least-privilege boundaries change."
---

# MySQL Roles and Privileges

Use with `mysql-review` and the security reviewer for every database access
boundary.

## Check

- Map application, migration, read-only, reporting, replication, backup, and administrative accounts; verify least privilege and host matching.
- Review roles, default roles, dynamic/static privileges, grant inheritance, `SHOW GRANTS`, and privilege changes as migration artifacts.
- Audit views, routines, triggers, and events that execute with `DEFINER` or invoker context; constrain dynamic SQL and definer account lifecycle.
- Do not assume PostgreSQL-style native row-level security; keep tenant predicates or protected procedure boundaries explicit and test bypass paths.
- Check password/authentication plugins, TLS requirements, secret rotation, logging, and connector behavior without exposing credentials.

