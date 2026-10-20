# Flutter widgets, accessibility and rendering

- Prefer constrained layouts using the Flutter constraint model rather than assuming device pixel dimensions or safe-area insets.
- Provide semantic labels, readable text scaling, adequate target sizes, focus traversal, contrast and screen-reader support.
- Confirm animations obey reduced-motion preferences where practical and keep rendering smooth on lower-end target devices.
- Use list virtualization, image/cache budgets, const widgets where appropriate and selective rebuilds; profile before optimizing.
- Avoid synchronous heavy computation, large decode work or unbounded animations on the UI isolate.
- Verify keyboard insets, orientation, localization, right-to-left layout when required, accessibility services and high text-scale.
- Run performance profiling on a representative physical device in profile/release mode, not only debug/emulators.

Official: https://docs.flutter.dev/ui/accessibility-and-internationalization/accessibility ; https://docs.flutter.dev/perf ; https://docs.flutter.dev/ui/layout/constraints
