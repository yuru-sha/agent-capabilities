# Permissions, pull, and operations

Grant CI only the actions required to authenticate and push to intended repositories. Runtime roles should only pull required images.

Review repository policies for cross-account pulls separately from caller IAM.

Use VPC endpoints where private image pull paths are required and verify related S3/network dependencies.

Monitor failed pushes/pulls, scan findings, replication failure, repository growth, and lifecycle effects.
