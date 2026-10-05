# Concurrency, performance, and lifecycle

Measure cold and warm behavior separately when startup latency matters.

Tune memory with the understanding that CPU/network allocation and cost change with it. Avoid optimizing memory from anecdotal invocation samples.

Use reserved concurrency for isolation or hard caps; use provisioned concurrency when predictable low-latency startup justifies its operational and cost overhead.

Define timeout below any upstream request timeout and downstream lease/visibility constraints so failure is observable and recoverable.

Use published versions and aliases for immutable rollout points. Coordinate alias traffic shifting with health metrics and rollback procedures.

Keep initialization reusable outside the handler when safe, but never cache request-specific credentials or mutable tenant state across invocations.
