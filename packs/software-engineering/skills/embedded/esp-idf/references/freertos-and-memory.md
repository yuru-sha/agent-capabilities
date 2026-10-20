# ESP-IDF FreeRTOS and memory

- ESP-IDF FreeRTOS behavior differs from vanilla FreeRTOS (including SMP semantics on supported targets). Use the selected **IDF version and SoC** documentation to verify stack sizes, affinity, task notifications and critical-section behavior.
- Map tasks, priorities, core affinity, queues, event groups, mutexes and callbacks before making concurrency changes. Make thread ownership explicit; define task teardown and watchdog responsibilities.
- Use ISR-safe API variants only where permitted, propagate wake flags correctly and never block in interrupts. Validate peripheral-driver callback context before interacting with locks or UI/audio processing.
- Inspect `heap_caps_malloc` allocations: PSRAM vs internal, DMA-capable, executable and retention constraints vary by SoC/IDF. Check failures; measure heap minima and task stack high-water marks on device.
- Avoid long critical sections, CPU starvation, wait-for-self deadlocks and indefinite waits while holding resources. Treat watchdog resets as evidence to diagnose, not a reason to globally disable the watchdog.
- Account for sleep/wakeup, clock changes, UART timing, bus ownership and cache-disabled intervals.

Verification: bounded task/queue stress tests; repeated init/deinit; resource instrumentation; interrupts during shutdown; brownout; Wi-Fi reconnect with heap pressure.

Primary docs: https://docs.espressif.com/projects/esp-idf/en/stable/esp32s3/api-reference/system/freertos_idf.html ; https://docs.espressif.com/projects/esp-idf/en/stable/esp32s3/api-reference/system/mem_alloc.html ; https://docs.espressif.com/projects/esp-idf/en/stable/esp32s3/api-reference/system/wdts.html
