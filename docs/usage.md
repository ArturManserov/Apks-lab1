# Інструкція запуску

## Агент
`/init` у Copilot Chat (агент build-engineer). Повторний запуск безпечний (ідемпотентний).

## Локальна перевірка
```
python scripts/check.py        # перевірка структури, збірки, тестів, workflow
./ci.sh                        # Linux/macOS
ci.bat                         # Windows
```
Очікувано: виконуваний `build/hello` (`build\Release\hello.exe`), тест `Arithmetic.BasicAddition` — Passed.
