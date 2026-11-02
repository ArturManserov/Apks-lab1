@echo off
rem Локальна та CI-збірка для Windows: configure -> build -> test -> run.
setlocal

cmake -S . -B build || exit /b 1
cmake --build build --config Release || exit /b 1
ctest --test-dir build --build-config Release --output-on-failure || exit /b 1
build\Release\hello.exe || exit /b 1
