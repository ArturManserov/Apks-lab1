---
description: Створити початковий Hello World проєкт через skill project-scaffold.
agent: build-engineer
---
# create-project

**Передумови:** виконано `git-init`.
**Дії:** застосувати skill `project-scaffold` з `language=cpp`, `project_name=hello`.
**Очікувані файли:** `src/main.cpp`, `src/mathops.hpp`, `README.md`, `.gitignore`.
**Перевірка:** `src/main.cpp` існує та містить `main(`.
**Помилка:** якщо `src/main.cpp` вже змінений користувачем — не перезаписувати,
повідомити «main.cpp існує, пропущено».
