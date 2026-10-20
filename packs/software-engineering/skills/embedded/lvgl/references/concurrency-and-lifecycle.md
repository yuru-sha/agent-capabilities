# UI task ownership and lifecycle

- Locate the LVGL tick source, timer handler, UI task, display/input drivers and lock model for the specific LVGL major version and port.
- LVGL is generally not thread-safe: funnel state changes into the owning UI context, or use the port's documented lock consistently. Do not acquire UI locks inside callbacks that already hold them.
- ISR and DMA completion callbacks must only signal/defer work when required. Keep callback execution bounded, and avoid drawing or blocking driver operations from interrupts.
- Register/delete timers, event callbacks, screens, styles, images and input devices with explicit owners. Cancel stale asynchronous updates when screens are replaced.
- Define init/reinit/shutdown order and guard animation callback use-after-free. Avoid recursive event updates and callbacks that acquire bus locks in inverse order.
- Verify scheduling and concurrency assumptions on LVGL v8 vs v9; do not copy symbols across major versions.

Official: https://docs.lvgl.io/master/details/integration/overview/threading.html ; https://docs.lvgl.io/master/details/main-modules/event.html
