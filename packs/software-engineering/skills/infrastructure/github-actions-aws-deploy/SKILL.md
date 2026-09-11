---
name: github-actions-aws-deploy
description: Use when designing or reviewing GitHub Actions deployments to AWS, OIDC permissions, reusable workflows, or ECS and ecspresso responsibility boundaries.
---

# GitHub Actions to AWS deployment design

This is a deployment-design and review specialist. It does not create
workflows, request reviews, mutate repositories, or deploy AWS resources.

## Rules

- Make triggers, protected environments, approvals, concurrency, cancellation,
  permissions, artifacts, and rollback behavior explicit. Grant id-token: write
  only to the job that needs OIDC and keep all other permissions minimal.
- Prefer short-lived OIDC role sessions over static AWS credentials. Scope the
  role trust to the intended repository, ref, and environment, and make the
  workflow's environment selection visible rather than inferred from a branch
  name alone.
- Keep reusable workflow inputs, outputs, secrets, and permissions explicit.
  Pass only the required secrets; do not use broad secret inheritance as a
  convenience.
- Separate build, test, scan, artifact publication, deployment, health
  verification, and rollback. Promote an immutable image or package digest,
  wait for service health, and retain enough evidence to identify the deployed
  revision.
- Assign one owner to each ECS resource and field. If Terraform owns the
  cluster, service, networking, or baseline task definition, ecspresso must
  not silently manage the same fields; if ecspresso owns application
  deployment, Terraform should expose the handoff instead of fighting it.
  Follow the consumer repository's selected ownership model.
- Make failed deployments safe: prevent overlapping production releases,
  preserve the last known-good revision, surface health-check and migration
  failures, and define who or what performs rollback.

## Verification

Read the actual workflow, reusable-workflow call graph, environment settings,
OIDC trust, artifact path, ECS/ecspresso configuration, and deployment logs or
test evidence. Report missing responsibility ownership and unverified
assumptions separately; do not use this specialist to change GitHub or AWS
state.
