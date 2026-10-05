# Service selection and ownership

Choose AWS services from workload characteristics and operational constraints rather than familiarity alone.

Compare relevant options across:

- delivery and consistency semantics;
- latency and throughput;
- scaling model and quotas;
- availability and recovery;
- operational burden;
- security and network boundaries;
- observability;
- cost shape and idle cost;
- portability requirements.

Keep cross-service ownership explicit. Terraform or another IaC system should own long-lived infrastructure; application deployment tooling should own only the fields intentionally delegated to it.

Avoid multiple controllers mutating the same resource attributes. Document handoff points such as image digest, task definition revision, Lambda alias, database endpoint, queue ARN, or secret reference.
