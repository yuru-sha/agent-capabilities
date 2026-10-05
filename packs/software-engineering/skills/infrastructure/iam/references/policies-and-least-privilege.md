# Policies and least privilege

Start from required API actions and resources observed in code, deployment definitions, or documented workflows.

Prefer resource-scoped permissions when the API supports them. Use conditions for account, organization, tags, source identity, encryption context, VPC endpoint, or other bounded context when they materially reduce exposure.

Review wildcard actions and resources separately. Some AWS APIs require broader resource scope, but that should be documented rather than normalized as a default.

Distinguish explicit deny from implicit deny. Include resource-based policies, SCPs, permission boundaries, session policies, and service-specific authorization when troubleshooting an unexpected decision.

Do not infer security from policy document size; a short wildcard policy can be far more privileged than a longer explicit policy.
