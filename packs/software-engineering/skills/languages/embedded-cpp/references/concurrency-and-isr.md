# Concurrency, interrupts and lifecycle

- Trace producers, consumers and task priorities for every shared object. State whether each API can block, allocate or run from an ISR.
- Keep ISRs short: acknowledge the source, capture minimal state and defer work using the RTOS's ISR-safe queue/notification APIs. Never use task-context APIs from an interrupt. Use the correct higher-priority-task-woken/yield conventions.
- Bound queues and message sizes; define drop/coalesce/backpressure policy. A queue send failing is normal under load and must be handled.
- Guard multi-step invariants with a well-defined mutex/critical section; avoid holding locks around I/O, calls to user callbacks or indefinite waits. Audit lock ordering and priority inversion.
- Define shutdown and reconnection: stop new work, signal cancellation, join/drain tasks, then free memory and drivers. Prevent stale callbacks updating newly recreated devices.
- Distinguish atomic flag visibility, ordering, interrupt masking and actual hardware synchronization. `volatile` is for peripheral observation, not inter-task synchronization.
- Test priority starvation, queue saturation, timeout boundaries, double initialization, cancellation while busy and interleaving on device.

Consult the *actual* RTOS and target SDK documentation for API names and supported ISR context; see https://docs.espressif.com/projects/esp-idf/en/stable/esp32s3/api-reference/system/freertos_idf.html for ESP-IDF-specific behavior.
