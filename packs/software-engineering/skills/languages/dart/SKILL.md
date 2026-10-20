---
name: dart
description: Use for Dart language implementation, refactoring, async/isolate behavior, null safety, serialization, dependencies and testing; load focused references.
---

# Dart

Check `pubspec.yaml`, Dart SDK constraints, analyzer options and repository conventions first. Keep guidance language-specific and load only needed references.

## References

- [Language and null safety](references/language-and-types.md)
- [Async, streams and isolates](references/async-and-isolates.md)
- [Errors, API and serialization](references/api-and-errors.md)
- [Dependencies and testing](references/testing-and-tooling.md)

## Rules

- Preserve sound null safety and typed contracts; validate external input at trust boundaries.
- Distinguish UI-isolate responsiveness from concurrent execution and asynchronous I/O.
- Never guess current package or SDK versions; check resolved lockfiles and official release notes.
- Compose with `flutter` for widget/platform concerns; do not duplicate Flutter architecture here.
