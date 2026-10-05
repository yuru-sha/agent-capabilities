# Roles, trust, and STS

A role requires both permission to assume it and a trust policy that accepts the caller.

Review:

- principal and trust relationship;
- `sts:AssumeRole` or web-identity action;
- external ID or source identity where applicable;
- session duration;
- session tags and transitive tags;
- MFA or organizational conditions when required;
- chained-role session limits.

Prefer short-lived sessions. Do not store role session credentials as durable application secrets.

For OIDC providers, verify issuer, audience, and subject/claim restrictions. Workflow-specific GitHub Actions OIDC design belongs in `github-actions-aws-deploy`, while the role trust policy remains an IAM concern.
