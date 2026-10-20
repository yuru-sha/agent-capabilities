# Language, ABI and ownership

1. Read `CMakeLists.txt`, compiler version, `-std`, warning/sanitizer flags, linker map, board configuration and third-party C interfaces before changing source.
2. Respect C vs C++ linkage (`extern "C"`), alignment, strict aliasing, integer widths, endianness and struct padding at wire, NVS or register boundaries. Prefer explicit serialization to casting packets into structs.
3. Every peripheral, DMA buffer, descriptor, file handle, mutex and callback must have exactly one documented owner and teardown path. Use RAII in C++ where compatible with the target's exceptions/RTTI policy; use paired initialization/cleanup in C.
4. Check stack vs heap allocation, task-local buffers, lifetimes of asynchronous callbacks and pointer validity after reconfiguration.
5. Validate indexes, lengths, signedness, integer overflow and alignment before parsing or copying untrusted data.
6. Avoid dynamic allocation in hard real-time/ISR paths; if allocation is required elsewhere, handle failures without unbounded retries. Do not rely on C++ exceptions if disabled in the build.
7. Keep hardware-specific drivers behind small HAL contracts that can be faked on the host. Preserve reproducibility of board- and compiler-specific behavior.

Review evidence: point to build settings, call sites, ownership/cleanup paths, and specific target behaviors. Never infer thread safety from `volatile`; use atomics or RTOS synchronization appropriate to the memory model.

Sources: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines ; https://en.cppreference.com/w/c/language ; https://gcc.gnu.org/onlinedocs/
