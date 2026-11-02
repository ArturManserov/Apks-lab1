---
name: build-and-test
description: Налаштовує CMake, GoogleTest, тест Arithmetic.BasicAddition та скрипти ci.sh / ci.bat.
---

# build-and-test

## Коли застосовувати
Є `src/`, але немає `CMakeLists.txt`, `tests/` або скриптів `ci.sh`/`ci.bat`.

## Вхідні дані
- `project_name` (за замовчуванням `hello`);
- версія GoogleTest (за замовчуванням `v1.14.0`, через `FetchContent`).

## Що створюється
- `CMakeLists.txt`: стандарт C++17, ціль `hello`, ціль `unit_tests`,
  `enable_testing()`, `gtest_discover_tests`;
- `tests/test_basic.cpp`: `TEST(Arithmetic, BasicAddition)` та ще 2 перевірки;
- `ci.sh` (Linux/macOS) і `ci.bat` (Windows): configure → build → ctest → запуск `hello`.

## Перевірки
1. `cmake -S . -B build` завершується з кодом 0.
2. `cmake --build build` створює `hello` та `unit_tests`.
3. `ctest --test-dir build --output-on-failure` → `100% tests passed`.

## Типові помилки
- Немає доступу до GitHub під час `FetchContent` → повідомити про мережу, не підміняти залежність.
- На Windows `gtest` збирається з іншим CRT → у CMake виставлено `gtest_force_shared_crt ON`.

## Ідемпотентність
Не дублювати `add_executable`/`add_test`; перед додаванням шукати існуючий рядок.
