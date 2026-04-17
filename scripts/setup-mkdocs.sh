#!/usr/bin/env bash
# Bootstraps a local Python venv and installs MkDocs + dependencies for this repo.
# Run from anywhere — the script resolves paths relative to itself.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

echo "=== tz-stack-registry — MkDocs setup ==="

if ! command -v python3 >/dev/null 2>&1; then
    echo "ERROR: python3 is required but not found on PATH." >&2
    exit 1
fi

if [ ! -d ".venv" ]; then
    echo "[1/3] Creating virtual environment at .venv ..."
    python3 -m venv .venv
else
    echo "[1/3] Virtual environment already exists — skipping."
fi

# shellcheck disable=SC1091
source .venv/bin/activate

echo "[2/3] Installing dependencies from requirements.txt ..."
pip install --upgrade pip >/dev/null
pip install -r requirements.txt

echo "[3/3] Verifying MkDocs build (strict) ..."
mkdocs build --strict

echo ""
echo "=== Setup complete ==="
echo "To preview locally:   source .venv/bin/activate && mkdocs serve"
echo "To deploy:            ./scripts/deploy.sh"
