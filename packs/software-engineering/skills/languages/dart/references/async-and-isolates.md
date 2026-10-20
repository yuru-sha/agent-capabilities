# Dart futures, streams and isolates

- `async`/`await` schedules asynchronous work; it does not move CPU-bound work off an isolate. For heavy parsing/processing, consider isolates and measure serialization/copying overhead.
- Every Future/Stream should have clear cancellation, timeout, ownership and error propagation. Avoid dropped Futures and unobserved stream errors.
- Use a single-source-of-truth for state; guard stale results from prior requests with a generation token or cancellation strategy.
- On dispose, cancel subscriptions, timers, outstanding work where possible and close controllers exactly once.
- Implement bounded buffering and backpressure for WebSocket/audio/device streams; define behavior for network loss, replay and duplicate commands.
- Prefer structured result/error contracts over broad catch-all swallowing. Avoid using a synchronous blocking operation on the Flutter UI isolate.
- Test rapid request replacement, stream completion/errors, reconnects, timeout vs completion races and dispose during pending operations.

Official: https://dart.dev/libraries/async/async-await ; https://dart.dev/language/isolates
