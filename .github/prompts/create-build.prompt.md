---
description: Створити CMakeLists.txt, тести GoogleTest та ci.sh/ci.bat через skill build-and-test.
agent: build-engineer
---
# create-build

**Передумови:** існує `src/main.cpp`.
**Дії:** застосувати skill `build-and-test`.
**Очікувані файли:** `CMakeLists.txt`, `tests/test_basic.cpp`, `ci.sh`, `ci.bat`.
**Перевірка:** `./ci.sh` (або `ci.bat`) створює `hello` і `ctest` показує `100% tests passed`.
**Помилка:** якщо cmake/компілятор не знайдені — вивести, чого саме бракує, і зупинитися.
