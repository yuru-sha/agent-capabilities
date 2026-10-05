# Schema, governance, and security

Prefer additive schema evolution for shared analytical tables. Treat type changes, field mode changes, and semantic redefinitions as compatibility events.

Use stable field names and document units, time zones, enum domains, nullability, and business definitions.

Apply least privilege at project/dataset/table/view level. Use row-level security, authorized views, and policy tags/column-level controls where access varies by user or data class.

Keep auditability and data lineage in scope for regulated or business-critical datasets.

Avoid copying sensitive data into ad hoc tables without equivalent retention, masking, and access controls.
