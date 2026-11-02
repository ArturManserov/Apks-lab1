# Архітектура агента

## Яку проблему вирішує агент
Ручне створення C++-проєкту з CMake, тестами та CI на трьох ОС відтворюється з помилками.
Агент задає єдиний процес із перевірками й забороненими діями.

## Відповідність файлів ролям (GitHub Copilot / VS Code)
| Файл | Роль |
|---|---|
| `.github/agents/build-engineer.agent.md` | manifest: роль, правила, заборони, критерії завершення |
| `.github/skills/*/SKILL.md` | skills: project-scaffold, build-and-test, github-actions |
| `.github/prompts/*.prompt.md` | commands: git-init, create-project, create-build, create-actions, check; init — оркестратор |
| `scripts/check.py` | виконуваний бекенд команди check |
| `ci.sh`, `ci.bat` | локальна й CI-збірка |
| `.github/workflows/ci.yml` | matrix-job, що лише викликає ci.sh/ci.bat |

## Потік даних
`git-init` (.gitignore) → `create-project` (src/, README) → `create-build` (CMakeLists, tests, ci.*)
→ `create-actions` (ci.yml) → `check` (звіт PASS/FAIL, код виходу).

## Обробка помилок оркестратором
Зупинка на першому FAIL, виведення причини й назви command для повторного запуску.
`ALL CHECKS PASSED` друкується лише при коді виходу 0 від `check`.
