# Logs and Logs Insights

Prefer structured application and platform logs with stable fields for request or trace identity, operation, severity, outcome, latency, and relevant resource identifiers.

Never log credentials, authorization headers, raw secrets, or sensitive payloads without an explicit approved need and redaction policy.

Set log-group retention intentionally. Indefinite retention should be a conscious compliance or forensic requirement, not an accidental default.

For Logs Insights, write queries around known fields and bounded time ranges. Save or document high-value operational queries for recurring incidents.

If downstream log subscriptions or centralization are used, define delivery failure handling and ownership rather than assuming log export is lossless.
