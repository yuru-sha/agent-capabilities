# Debug, flashing and verification

## Workflow

1. Reproduce with the repository's specified IDF, target, `sdkconfig` and lockfile. Capture exact `idf.py build` output, warnings and ELF/map information.
2. Run host-side logic tests where possible; use ESP-IDF Unity tests and HIL tests for target-bound components. Compare debug/release flags, task stack metrics and partition fit.
3. For runtime faults, collect reset reason, decoded backtrace/panic, task watchdog logs, queue/heap minima and selected core. Use supported monitor, GDB/OpenOCD or tracing only for a verified board.
4. For field errors, test brownout, reconnect, NVS corruption, failed OTA, power loss, full queue and resource exhaustion; ensure diagnostics don't expose keys.
5. Distinguish tests requiring hardware from build-only checks; document what was not executed and why.

## Safety gates

- `idf.py build` does not flash a board. `idf.py flash` / `erase-flash` / `espefuse` are hardware-changing operations requiring matching device and explicit authorization.
- Before writing flash, confirm target/chip, port, flash size, partition layout and any data persistence requirements. Never erase calibration/provisioning as an implicit fix.
- Restore safe device behavior after failures; keep a recovery UART/USB or alternate boot path available.

Official docs: https://docs.espressif.com/projects/esp-idf/en/stable/esp32s3/api-guides/unit-tests.html ; https://docs.espressif.com/projects/esp-idf/en/stable/esp32s3/api-guides/fatal-errors.html ; https://docs.espressif.com/projects/esp-idf/en/stable/esp32s3/api-guides/jtag-debugging/index.html
