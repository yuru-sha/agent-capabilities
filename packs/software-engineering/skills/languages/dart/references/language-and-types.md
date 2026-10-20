# Dart language, types and ownership

- Read `environment.sdk`, `analysis_options.yaml` and project conventions before changing code. Check language features against the selected Dart SDK.
- Prefer exhaustive sealed-class/pattern handling where supported; distinguish nullable `T?`, `late`, and runtime null assertions. Avoid `!` without an established invariant.
- Treat collections exposed by APIs as potentially mutable; document ownership, copying, immutability and object lifecycle.
- Use extensions, records, generics and mixins only when they simplify a real contract. Avoid `dynamic` and unsafe casts at boundaries.
- Make resource cleanup explicit (`StreamSubscription.cancel`, `dispose`, file/socket closure); add `try/finally` when lifecycle spans failures.
- Review `==` and `hashCode`, value equality, ordering, time zones and numeric/UTF conversions in persisted data.
- Validate JSON schema and unknown enum values; do not silently coerce incompatible remote payloads.

Official: https://dart.dev/language ; https://dart.dev/null-safety
