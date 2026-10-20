# Host and hardware verification

## Test layers

1. Host unit tests: pure parsing, motion coordinate math, state machines and serialization; compile with strict warnings and host sanitizers where available.
2. Platform simulation / fakes: simulate queue overflow, timeout, reconnect, allocation and driver failures. Assertions about timing should use injectable clocks.
3. On-device tests: validate peripheral startup/shutdown, heap/stack minima, reset reasons, watchdog behavior, partition layout and flash persistence.
4. HIL/manual safety tests: check physical motion range, current draw, brownout, disconnects, OTA recovery and repeated power cycles with supervised hardware.

A host-only green test does **not** establish ISR correctness, target ABI fidelity, DMA safety or actuator safety.

## Before flash or actuation

- Confirm board model, revision, chip target, serial port and power configuration.
- Preserve backups for calibration, keys, partition/NVS state and known-good firmware; never overwrite production provisioning as a test shortcut.
- Require explicit confirmation before destructive erase, eFuse writes, security-feature provisioning or irreversible flash configuration.
- Keep the device in a safe, accessible state throughout HIL testing. Do not command actuators outside documented limits.

StackChan example: https://github.com/m5stack/StackChan/blob/main/firmware/README.md
