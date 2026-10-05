# Rotation, multi-Region, and operations

Define rotation strategy from key origin/type and compliance requirements; do not assume all keys support the same automatic/on-demand behavior.

Multi-Region keys are separate Regional resources with related key material and independent policies/grants/aliases. Use them only when cross-Region cryptographic interoperability is required.

Treat key disable and scheduled deletion as dangerous operations with dependency discovery and recovery planning.

Monitor access-denied, disabled-key, throttling, grant, rotation, and policy-change events.
