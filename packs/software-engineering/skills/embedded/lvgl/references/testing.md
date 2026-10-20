# Embedded UI test matrix

| Scenario | Expected outcome |
| --- | --- |
| Repeated screen entry/exit | no dangling event/timer callbacks, stable heap |
| Touch during DMA/display refresh | input remains responsive, buffers not reused too early |
| Rotation, scaling, low memory | correct touch mapping and graceful allocation failures |
| Concurrent sensor updates | UI owner/lock discipline, no deadlock or starvation |
| Display power sleep/wake | redraw recovery and valid driver lifecycle |

Use pure-model host tests where possible, LVGL simulation for visual logic, and physical HIL to verify timing, buses, DMA and touch. Report LVGL/port/IDF versions, device revision, buffer layout and evidence. Avoid claiming simulation proves hardware safety.

Official: https://docs.lvgl.io/master/
