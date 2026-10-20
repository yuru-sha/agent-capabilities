---
name: frontend-flutter
description: Use for Flutter Android/iOS app architecture, widgets, state lifecycle, accessibility, performance, native integrations, permissions, tests and mobile releases.
---

# Flutter

Read `pubspec.yaml`, Flutter/Dart version constraints, chosen state-management conventions, Android Gradle and iOS deployment settings. Compose with `dart` for language behavior.

## References

- [Architecture and lifecycle](references/architecture-and-lifecycle.md)
- [UI, accessibility and performance](references/ui-and-performance.md)
- [Platform integration, permissions and security](references/platform-and-security.md)
- [Testing and diagnostics](references/testing.md)
- [Android/iOS delivery and CI](references/release-and-ci.md)

## Rules

- Preserve existing app architecture; do not impose an additional state-management framework.
- Treat Android, iOS and web/desktop as distinct targets with different capabilities and permissions.
- Do not reuse React or browser DOM-specific patterns as Flutter widget advice.
- Never log or check in signing keys, secrets or production user data.
