# PassRole, permission boundaries, and cross-account access

## iam:PassRole

Treat `iam:PassRole` as delegated authority. Constrain the target role and, where possible, the AWS service receiving it. Review the pass-role caller, target role permissions, and target role trust together.

## Permission boundaries

A permission boundary limits the maximum identity permissions; it does not grant permissions itself. Validate the effective intersection with identity policies and any organization controls.

## Cross-account

For cross-account access, trace both sides:

- caller identity permission;
- target role/resource trust or resource policy;
- organization/SCP restrictions;
- encryption-key policy when encrypted resources are involved.

Avoid account-wide trust without conditions when a narrower principal, organization, external ID, or resource path can express the relationship.
