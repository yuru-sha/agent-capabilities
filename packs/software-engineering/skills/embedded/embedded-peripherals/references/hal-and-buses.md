# HAL, GPIO, I2C, SPI, UART and PWM

- Capture exact board revision, wiring, electrical levels, bus speed and firmware ownership. Do not infer pin mapping from another board variant.
- Define narrowly scoped HAL interfaces with explicit initialization, timeout, transfer, cancellation and cleanup contracts. Keep device protocol separate from bus driver.
- I2C: validate addresses, clock stretching support, pullups, timeout/NACK recovery and shared-bus locking.
- SPI: verify mode, clock, CS ownership, DMA alignment/buffer lifetime, chip-select timing and contention with displays/storage.
- UART: size bounded RX rings, parse framed packets, enforce baud/flow control/CRC and recover from partial reads.
- GPIO/PWM: configure safe boot defaults, pin direction, pullups, timer frequency, duty/pulse bounds and concurrent owner; ensure pins don't glitch during reset.
- Never busy-loop indefinitely on stalled hardware; use bounded retries, error classification and safe driver reinitialization only when recoverable.

Official: https://docs.espressif.com/projects/esp-idf/en/stable/esp32s3/api-reference/peripherals/index.html
