# Resources, power and reliability

- Establish target budgets: internal RAM, external PSRAM, flash partitions, per-task stack, CPU time, DMA-capable memory and electrical power. Track high-water marks and fragmentation rather than average heap alone.
- Understand memory capabilities: external RAM may not be DMA-safe or available early in boot; use allocator capabilities appropriate to each buffer. Check every allocation/driver-init result.
- Bound work and watchdog delays; distinguish legitimate long-running operations from deadlocks. Record task CPU load, reset reason, uptime, heap minima, queue depth and stack minimum remaining where supported.
- Avoid logging credentials and excessive writes to flash; batch persistent state with recovery-safe versioning and wear considerations.
- Model low battery, power cuts, Wi-Fi loss, sensor disconnect, brownout, bus timeout and corrupted storage. Define safe fallback states and bounded retries with jitter for network calls.
- Avoid uncontrolled actuation when connectivity or sensors fail. Physical limits, emergency stops and safe startup positions must derive from device documentation, not guesses.
- Profile on the actual target and release build; host benchmarks cannot predict timing, PSRAM cache behavior or power draw.

References: https://docs.espressif.com/projects/esp-idf/en/stable/esp32s3/api-reference/system/mem_alloc.html ; https://docs.espressif.com/projects/esp-idf/en/stable/esp32s3/api-reference/system/wdts.html
