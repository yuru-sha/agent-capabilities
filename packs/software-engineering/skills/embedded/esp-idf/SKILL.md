---
name: esp-idf
description: Use for Espressif ESP-IDF firmware, target/board configuration, CMake components, FreeRTOS integration, build/flash/monitor, partitions, NVS and OTA troubleshooting.
---

# ESP-IDF

Inspect `idf.py --version`, `IDF_PATH`, `sdkconfig`, `sdkconfig.defaults`, `dependencies.lock`, component manifests, partitions and exact target/board before suggesting commands. Prefer the repository's pinned IDF toolchain, not an assumed latest release.

## Reference routing

- Reproducible setup, targets and CMake: [build-and-components](references/build-and-components.md)
- FreeRTOS tasks, ISR and hardware memory: [freertos-and-memory](references/freertos-and-memory.md)
- Flash partitioning, NVS and firmware update: [storage-and-ota](references/storage-and-ota.md)
- Debugging, firmware safety and verification: [debug-and-test](references/debug-and-test.md)

## Boundaries

- Combine with `embedded-cpp` for C/C++ semantics and platform-neutral resource ownership.
- ESP-IDF documentation is target and version specific. Confirm the selected version and chip target in official docs before using an API.
- This is not an LVGL, servo-control or ESP-NOW protocol skill; compose separately when relevant.
- Reading guidance never authorizes connecting to a real device, erasing flash, burning eFuses, changing secure boot keys or operating actuators.
