# Event sources, networking, and operations

Configure event-source mappings from source semantics:

- batch size and batching window;
- parallelization/concurrency;
- ordering requirements;
- partial failure handling;
- retry/record age;
- poison-record destination or quarantine.

For VPC-connected functions, verify subnet routing, security groups, DNS, required VPC endpoints or NAT, and downstream connection limits.

Use least-privilege execution roles and keep secret retrieval explicit. Do not put secret values in environment examples, logs, artifacts, or deployment output.

Monitor errors, throttles, duration, concurrency, iterator age/backlog where relevant, destination failures, and downstream saturation.

Document replay/redrive procedures for asynchronous or stream/queue sources before production incidents occur.
