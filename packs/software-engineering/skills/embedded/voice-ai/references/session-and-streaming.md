# Session lifecycle, barge-in and cancellation

Suggested conversation states: idle → armed/listening → capturing → processing → speaking → idle. Any active state can enter interrupted/reconnecting/stopped, with explicit safe cleanup.

- Define session ID, turn ID and generation token. Ignore late ASR/LLM/TTS data from superseded turns.
- On barge-in (user speaking during playback), stop or duck output according to UX policy, cancel the prior synthesis/stream, flush stale audio buffers and open a new turn only once.
- Treat transport message receipt, ASR completion, TTS chunk availability and audible playback completion as separate milestones.
- Bound queues and durations; prefer explicit backpressure and cancellation to unchecked buffering, leaked futures/tasks or endless reconnection loops.
- On network interruption, reconcile remote session state and prevent replay of non-idempotent tool/device actions. Rotate or reauthenticate expired credentials.
- Distinguish user-initiated microphone mute from lost connectivity and maintain correct microphone/recording indicators.
- Test race conditions: double wake, cancel while TTS chunk arrives, reconnect after old session closes, audio device hot reset and simultaneous app/device interactions.

WebSocket transport-specific references belong to `device-websocket`; avoid duplicating its low-level handshake implementation.
