# Toolchain, build and component management

1. Determine chip (`idf.py set-target` may regenerate configuration), board revision, ESP-IDF version, Python environment, compiler toolchain, `IDF_PATH` and firmware flash size. Confirm versions from repository requirements and [Espressif releases](https://github.com/espressif/esp-idf/releases).
2. Use an isolated ESP-IDF installation: follow the official versioned [Get Started guide](https://docs.espressif.com/projects/esp-idf/en/stable/esp32s3/get-started/index.html), then `idf.py --version`, `idf.py build`. Never silently run `set-target` against an existing hardware configuration.
3. Review `CMakeLists.txt`, `main/CMakeLists.txt`, `Kconfig` and `sdkconfig.defaults` for dependencies, configuration switches and reproducibility. Treat `sdkconfig` as target/build-specific and check the repository's tracking policy.
4. Resolve components via `idf_component.yml`, registry version constraints and `dependencies.lock`; audit source trust and transitive versions before regeneration. A lockfile should not be modified just to make one developer's environment work.
5. Compare partition table, bootloader, flash/PSRAM settings and pin assignments with the target hardware. Keep board variants separate; don't force all boards to share a target-specific pinout.
6. For build failure, report the first root-cause diagnostic, compiler/IDF version and exact command. Prefer minimal reproducible builds over global flag changes.

Typical **non-destructive** workflow after setup:
```sh
idf.py --version
idf.py build
```
For a known, connected development board, `idf.py -p <PORT> flash monitor` is a state-changing operation; verify port/board and obtain permission first.

Official references: https://docs.espressif.com/projects/esp-idf/en/stable/esp32s3/api-guides/build-system.html ; https://docs.espressif.com/projects/esp-idf/en/stable/esp32s3/api-reference/kconfig-reference.html ; https://docs.espressif.com/projects/idf-component-manager/en/latest/
StackChan example (pinned v5.5.4 in its README): https://github.com/m5stack/StackChan/blob/main/firmware/README.md
