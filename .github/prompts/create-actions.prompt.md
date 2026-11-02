---
description: Створити .github/workflows/ci.yml через skill github-actions.
agent: build-engineer
---
# create-actions

**Передумови:** існують `ci.sh` та `ci.bat`.
**Дії:** застосувати skill `github-actions`.
**Очікувані файли:** `.github/workflows/ci.yml`.
**Перевірка:** YAML валідний; matrix містить `ubuntu-latest`, `windows-latest`, `macos-latest`;
у файлі немає `cmake`/`ctest` та `secrets.`.
**Помилка:** якщо відсутній `ci.sh`/`ci.bat` — зупинитися й запропонувати `create-build`.
