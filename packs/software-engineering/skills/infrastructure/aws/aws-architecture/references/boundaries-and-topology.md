# Boundaries and topology

Model the architecture from explicit trust and failure boundaries:

- AWS account and organization boundary;
- Region and Availability Zone placement;
- VPC, subnet, route, endpoint, internet/NAT, and DNS boundaries;
- public edge versus private application/data planes;
- workload identity and cross-account trust;
- encryption and data-classification boundaries.

Do not copy a generic three-tier diagram without tracing the actual request and data paths. Show where traffic enters, which services can initiate connections, where credentials are assumed, and which path is used for egress.

Keep environment separation explicit. Development and test defaults must not silently reuse production resources, credentials, state, queues, buckets, or databases.

When a service-specific concern dominates the decision, route to the corresponding service Skill instead of duplicating its rules here.
