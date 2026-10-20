# Reproducible tests and HIL matrix

| Scenario | Verify |
| --- | --- |
| Silence, low speech, noisy room, echo | wake/VAD accuracy, false triggers, AEC behavior |
| Wrong codec rate/channels, truncated Opus or PCM | rejected frames, bounded memory, graceful errors |
| Burst network jitter/packet loss | bounded buffers, intelligible playback, no stale response |
| User barge-in during TTS | timely stop, stale chunks discarded, correct new turn |
| Reconnect or expired token mid-turn | new session identity, no duplicate tool execution |
| Ring buffer full, PSRAM shortage, task starvation | instrumentation, fallback, no watchdog loop |
| Microphone denied/muted or device unplugged | no unauthorized capture or cloud upload |
| Power loss during playback, reboot | safe restart, no phantom recording or replay |

- Unit-test turn state machines, sample-format validation, queue bounds and cancellation using fake clocks and audio frames.
- Test offline simulation for ASR/TTS failures and malformed server messages. HIL-test real codec/I2S clocks, CPU/heap/stack budgets, speaker feedback and end-to-end latency.
- Report P50/P95/P99 capture-to-first-audio latency separately from speech recognition and TTS generation, plus measured test device and sample conditions.
- Test under simultaneous UI, BLE/Wi-Fi, display DMA and sensor workloads; simulation alone cannot validate real-time timing.
