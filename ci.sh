#!/usr/bin/env bash
# Локальна та CI-збірка для Linux/macOS: configure -> build -> test -> run.
set -euo pipefail

cmake -S . -B build -DCMAKE_BUILD_TYPE=Release
cmake --build build --config Release --parallel
ctest --test-dir build --build-config Release --output-on-failure
./build/hello
