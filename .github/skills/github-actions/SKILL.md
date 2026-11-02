---
name: github-actions
description: Створює .github/workflows/ci.yml з однією job та matrix для Ubuntu, Windows і macOS; workflow лише викликає ci.sh / ci.bat.
---

# github-actions

## Коли застосовувати
Існують `ci.sh` і `ci.bat`, але немає `.github/workflows/ci.yml`.

## Вхідні дані
- гілки-тригери (за замовчуванням `develop`, `master`);
- список ОС (за замовчуванням `ubuntu-latest`, `windows-latest`, `macos-latest`).

## Що створюється
`.github/workflows/ci.yml`:
- тригери `push` та `pull_request` для `develop`, `master`;
- одна job `build-test` з `strategy.matrix.os`;
- кроки: `actions/checkout@v4` → запуск `ci.sh` (Unix) або `ci.bat` (Windows)
  → `actions/upload-artifact@v4` з виконуваним файлом;
- **жодних** команд cmake/ctest безпосередньо у YAML.

## Перевірки
1. YAML парситься (`python -c "import yaml"`).
2. У `matrix.os` рівно три очікувані значення.
3. У файлі відсутні `secrets.` та токени.

## Типова помилка
Використано `bash ci.sh` на Windows-раннері без Git Bash → окремі кроки з `if: runner.os`.
