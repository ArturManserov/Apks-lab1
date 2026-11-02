#!/usr/bin/env python3
"""Команда check: перевіряє структуру, workflow, складання й тести.

Не змінює файли проєкту (створює лише тимчасовий каталог build/, що в .gitignore).
Код виходу 0 — усе гаразд, 1 — є помилки.
"""
import pathlib
import re
import subprocess
import sys

try:
    import yaml
except ImportError:
    yaml = None

ROOT = pathlib.Path(__file__).resolve().parent.parent
failed = []


def report(ok, text):
    print(("PASS  " if ok else "FAIL  ") + text)
    if not ok:
        failed.append(text)


def read(rel):
    p = ROOT / rel
    return p.read_text(encoding="utf-8") if p.exists() else ""


# 1. manifest
m = read(".github/agents/build-engineer.agent.md")
for section in ("# Роль", "# Заборонені дії", "# Критерії успішного завершення"):
    report(section in m, f"manifest містить розділ «{section}»")

# 2. skills
for s in ("project-scaffold", "build-and-test", "github-actions"):
    t = read(f".github/skills/{s}/SKILL.md")
    for part in ("Коли застосовувати", "Вхідні дані", "Перевірки"):
        report(part in t, f"skill {s}: є «{part}»")

# 3. commands
for c in ("git-init", "create-project", "create-build", "create-actions", "check", "init"):
    report((ROOT / f".github/prompts/{c}.prompt.md").exists(), f"command {c} існує")
init = read(".github/prompts/init.prompt.md")
order = [init.find(f"/{c}") for c in ("git-init", "create-project", "create-build", "create-actions", "check")]
report(all(o >= 0 for o in order) and order == sorted(order), "init викликає commands у правильному порядку")

# 4. workflow
wf = read(".github/workflows/ci.yml")
for os_name in ("ubuntu-latest", "windows-latest", "macos-latest"):
    report(os_name in wf, f"ci.yml містить {os_name}")
report("ci.sh" in wf and "ci.bat" in wf, "ci.yml запускає ci.sh та ci.bat")
report(not re.search(r"\b(cmake|ctest)\b", wf), "ci.yml не містить прямих cmake/ctest")
report("secrets." not in wf, "ci.yml без secrets")
if yaml:
    try:
        yaml.safe_load(wf)
        report(True, "ci.yml — валідний YAML")
    except yaml.YAMLError as e:
        report(False, f"ci.yml — невалідний YAML: {e}")

# 5. gitignore і секрети
gi = read(".gitignore")
report("build/" in gi, ".gitignore містить build/")
for p in ROOT.rglob("*"):
    if p.is_file() and "build" not in p.parts and ".git" not in p.parts:
        if re.search(r"ghp_[A-Za-z0-9]{20,}|BEGIN (RSA|OPENSSH) PRIVATE KEY", p.read_text(errors="ignore")):
            report(False, f"знайдено схожий на секрет вміст: {p.relative_to(ROOT)}")

# 6. складання і тести
def run(cmd):
    return subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)

r = run(["cmake", "-S", ".", "-B", "build", "-DCMAKE_BUILD_TYPE=Release"])
report(r.returncode == 0, "cmake configure")
if r.returncode == 0:
    r = run(["cmake", "--build", "build", "--config", "Release", "--parallel"])
    report(r.returncode == 0, "cmake build")
    exe = [ROOT / "build/hello", ROOT / "build/Release/hello.exe"]
    report(any(p.exists() for p in exe), "виконуваний файл hello створено")
    r = run(["ctest", "--test-dir", "build", "--build-config", "Release", "--output-on-failure"])
    report(r.returncode == 0 and "100% tests passed" in r.stdout, "ctest: 100% tests passed")
    report("Arithmetic.BasicAddition" in run(["ctest", "--test-dir", "build", "-N"]).stdout, "тест BasicAddition знайдено")

print()
if failed:
    print(f"{len(failed)} CHECK(S) FAILED")
    sys.exit(1)
print("ALL CHECKS PASSED")
