# Dart tooling and tests

1. Check `dart --version`, SDK constraints, `pubspec.lock` and configured analyzer/linter; do not auto-upgrade packages.
2. Use `dart format --output=none --set-exit-if-changed .`, `dart analyze`, `dart test` where applicable to the repository and installed tooling.
3. Keep pure Dart logic independently testable with fakes and deterministic clocks; test null cases, serialization, stream lifecycle and error propagation.
4. Add regression tests for canceled futures, duplicate messages, isolate failures and resource cleanup.
5. For package releases, validate dependency constraints, API compatibility, examples, licensing and `dart pub publish --dry-run` before publishing; publication requires explicit authorization.

Official: https://dart.dev/tools/dart-analyze ; https://dart.dev/tools/dart-test ; https://dart.dev/tools/pub/dependencies
