#!/bin/bash
set -euo pipefail

cd "$(dirname "$0")"

SOLUTION_PY=./solution.py

if [[ ! -f "$SOLUTION_PY" ]]; then
    echo "ERROR: $SOLUTION_PY not found"
    exit 1
fi

python3 ./runner.py "$SOLUTION_PY" ./tests/translation
