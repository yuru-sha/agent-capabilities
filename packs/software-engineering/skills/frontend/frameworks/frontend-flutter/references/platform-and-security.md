# Platform channels, native plugins, permissions and secrets

- Examine `android/` (Gradle/Kotlin, manifest, min/target SDK) and `ios/` (Swift, Podfile, Info.plist, entitlements) before editing plugins.
- Prefer maintained platform plugins; use platform channels or FFI when native APIs are required. Document codec/message shapes, threading, error propagation, disposal and SDK availability.
- Request BLE/camera/microphone/location permissions only when features need them; align Android runtime requests and manifest entries with iOS usage descriptions and privacy declarations.
- Handle denied, restricted, permanently denied, revoked and background-limited states without infinite prompts or crashes.
- Store tokens/credentials via appropriate secure OS storage when required; never assume `shared_preferences` is encrypted secret storage.
- Validate any native-originated input and isolate auth/session data from analytics/crash logs. Use TLS and platform-specific certificate trust practices.
- Test repeated plugin init/dispose, lifecycle interruptions, missing hardware, OS-version-specific permissions and unpaired devices.

Official: https://docs.flutter.dev/platform-integration/platform-channels ; https://docs.flutter.dev/platform-integration/android ; https://docs.flutter.dev/platform-integration/ios ; https://developer.android.com/guide/topics/permissions/overview ; https://developer.apple.com/documentation/bundleresources/information_property_list
