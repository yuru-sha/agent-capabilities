---
name: embedded-cpp
description: Use for embedded C or C++ firmware design, code review, resource ownership, concurrency, hardware boundaries and host testing; load only relevant references.
---

# Embedded C and C++

Use for constrained bare-metal or RTOS firmware, independent of chip vendor. Check the repository's language dialect, toolchain, ABI, target MCU, build flags and memory layout first. Load only the needed references.

## Reference routing

- Language, ABI and ownership: [language-and-ownership](references/language-and-ownership.md)
- Interrupts, task synchronization and lifecycle: [concurrency-and-isr](references/concurrency-and-isr.md)
- Memory, power, timing and diagnosability: [resource-and-reliability](references/resource-and-reliability.md)
- Host, simulator and on-device verification: [testing-and-safety](references/testing-and-safety.md)

## Boundaries

- This skill owns embedded C/C++ semantics and resource constraints; it is not a generic desktop C++ style guide.
- Compose with `esp-idf` for ESP32-specific configuration, FreeRTOS APIs, flashing and OTA.
- Do not invent pin mappings, electrical ratings, safety limits or device capabilities. Verify board revision and schematics.
- Never treat a successful host test as proof of electrical or real-time safety.
