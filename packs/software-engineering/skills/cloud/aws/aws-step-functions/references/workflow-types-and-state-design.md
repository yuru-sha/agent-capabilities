# Workflow Types And State Design

Choose Standard for durable auditable potentially long-running workflows and Express for high-volume short-duration workloads when its semantics fit. Keep state payloads bounded and state names readable. Prefer native workflow states over opaque orchestration hidden inside Lambda when possible.
