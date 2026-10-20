# Flutter architecture and state lifecycle

- Map widget tree, routing, repositories/services and state ownership; keep business logic testable outside widgets.
- Understand `build` can be called repeatedly: do not perform network calls, create controllers or mutate durable state as an incidental side effect of build.
- Initialize and dispose `AnimationController`, `TextEditingController`, `FocusNode`, subscriptions and plugin sessions in the owning lifecycle.
- Before using `BuildContext` after an async gap, check mounted state where relevant and avoid navigation from unmounted widgets.
- Select local widget state vs shared state based on actual ownership; keep derived state derived and avoid duplicated mutable copies.
- Define app foreground/background/termination behavior for BLE, microphone, camera, audio playback and ongoing network requests.
- Test route replacement, repeated screen entry, hot restart, interruption and state restoration as supported by the app.

Official: https://docs.flutter.dev/app-architecture ; https://api.flutter.dev/flutter/widgets/State/dispose.html
