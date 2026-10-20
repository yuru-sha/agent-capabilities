# Flutter test pyramid and diagnostics

- **Unit:** pure Dart state/repository/parsers, error states, cancellations and serialized payloads.
- **Widget:** interactions, validation, focus/semantics, loading/error/empty states, navigation and disposal with injected fakes.
- **Golden:** deterministic fonts, locale, viewport/scale, platform and asset configurations; review intended visual diffs.
- **Integration/HIL:** launch on iOS and Android, permission denial, platform-channel callbacks, BLE reconnect, background/foreground and actual camera/mic behavior if supported.
- Run `flutter analyze` and `flutter test`; use `flutter test integration_test` / device commands only when configured for the repository.
- Collect redacted logs, Flutter error diagnostics and performance traces for failures. Clearly report simulator-only vs physical-device coverage.

Official: https://docs.flutter.dev/testing/overview ; https://docs.flutter.dev/testing/integration-tests ; https://docs.flutter.dev/cookbook/testing/widget/introduction
