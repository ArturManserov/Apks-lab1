Репозиторій містить AI-агента `build-engineer` (manifest, 3 skills, 6 commands),
який створює й перевіряє кросплатформний проєкт Hello World з CI для Windows, Linux і macOS.

## Запуск агента
1. Відкрити репозиторій у VS Code з GitHub Copilot (Agent mode).
2. У Copilot Chat обрати агента **build-engineer**.
3. Виконати команду `/init` (оркестратор). Окремі кроки: `/git-init`, `/create-project`,
   `/create-build`, `/create-actions`, `/check`.

## Запуск проєкту
- Linux/macOS: `./ci.sh`
- Windows: `ci.bat`
- Лише перевірка: `python scripts/check.py`

Вимоги: CMake ≥ 3.14, C++17-компілятор, Python 3, доступ до github.com (GoogleTest завантажується через FetchContent).
Документація: `docs/architecture.md`, `docs/usage.md`, `docs/ai-log.md`.
