# Peripheral resource and HIL checklist

| Fault | Expected behavior |
| --- | --- |
| Bus NACK/timeout or device removed | bounded timeout and safe reinit or disabled feature |
| DMA buffer missing/alignment error | fail without corrupting memory |
| Two clients access bus | serialized ownership with bounded wait |
| Low heap/stack or PSRAM exhausted | observable failure and graceful degradation |
| Power-cycle mid-transfer | recovery without corrupting persistent configuration |
| Sensor stale or malformed | invalid state propagated, no unsafe action |

Measure stack high-water marks, queue depths, DMA-compatible heap and power draw on the actual board. Use host fake drivers for state logic, simulated faults for bus interfaces and HIL for electrical/timing assumptions. Record what was not physically tested.

Official: https://docs.espressif.com/projects/esp-idf/en/stable/esp32s3/api-reference/system/mem_alloc.html
