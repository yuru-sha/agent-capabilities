# Android/iOS release and CI checklist

1. Confirm installed Flutter SDK, `pubspec.lock`, target SDKs, Xcode/Gradle/Kotlin compatibility and reproducible CI runner images.
2. CI gates: `flutter pub get`, `dart format --output=none --set-exit-if-changed .`, `flutter analyze`, `flutter test`, plus target-specific build/test steps when toolchains exist.
3. Android: validate application ID, build variants, min/target SDK, AAB/APK, signing keystore, Play requirements and app permissions.
4. iOS: validate bundle ID, supported OS, entitlements, CocoaPods/Swift compatibility, certificates/provisioning, archive/export and privacy manifests where required.
5. Keep signing keystores, private keys, provisioning profiles and passwords out of source control; inject only via authorized secure CI secrets.
6. Require explicit approval before store upload/release, app signing changes, production backend switching or key rotation.
7. Verify release-mode startup, offline fallback, update migration, debug-symbol management, crash reporting redaction and rollback plan.

Official: https://docs.flutter.dev/deployment/android ; https://docs.flutter.dev/deployment/ios ; https://docs.flutter.dev/deployment/cd
