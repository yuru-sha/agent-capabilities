# Networking, storage, and runtime

Fargate tasks/pods receive workload-level networking. Account for subnet IP capacity, security groups, DNS, NAT or VPC endpoints, and private registry/service connectivity.

Avoid public IP assignment by default unless the workload is intentionally internet-facing and the exposure model is justified.

Ephemeral storage is finite. Size temporary files, decompression, build/runtime caches, and log buffering explicitly.

Use EFS or application-level remote storage when durable shared filesystem semantics are required; do not treat local ephemeral storage as durable state.

Keep secrets out of images and plaintext environment examples. Use approved secret injection/retrieval paths.
