# Display/touch integration and rendering

- Verify panel controller, resolution, orientation, color depth, SPI/RGB/I80 bus clock, pixel byte order and touch coordinate transform from the board datasheet.
- Select draw-buffer count and size based on internal RAM/PSRAM and DMA-capability constraints. Verify cache flush/alignment and buffer lifetime before asynchronous transfers.
- Ensure flush-ready notification occurs only after the transfer is actually complete; avoid overwriting in-flight DMA buffers.
- Measure frame budget, animation cadence, heap minima, UI task stack and invalidation regions on hardware; tune partial/full render mode only based on evidence.
- Sample/debounce touch inputs, calibrate axis swap/inversion, and test press/drag/release during rotation and sleep transitions.
- Define safe degraded states for display disconnect, bus timeout, allocation failure and repeated resume.

Official: https://docs.lvgl.io/master/details/main-modules/display/setup.html ; https://docs.lvgl.io/master/details/main-modules/indev.html ; https://components.espressif.com/components/espressif/esp_lvgl_port
