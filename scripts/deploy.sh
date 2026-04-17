#!/usr/bin/env bash
# Builds the MkDocs site and (after confirmation) deploys it to the gh-pages branch.
# Requires: scripts/setup-mkdocs.sh has been run at least once.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

if [ ! -d ".venv" ]; then
    echo "ERROR: .venv not found. Run ./scripts/setup-mkdocs.sh first." >&2
    exit 1
fi

if [ -z "${VIRTUAL_ENV:-}" ]; then
    # shellcheck disable=SC1091
    source .venv/bin/activate
fi

echo "Building site (strict) ..."
mkdocs build --strict

if [ ! -d ".git" ]; then
    echo ""
    echo "NOTE: This repository is not a git repo yet. 'mkdocs gh-deploy' requires git and a remote."
    echo "      Run 'git init' + add a remote before deploying. Site is built locally at ./site/."
    exit 0
fi

echo ""
read -r -p "Deploy to GitHub Pages (gh-pages branch) now? [y/N] " confirm
case "$confirm" in
    [yY]|[yY][eE][sS])
        echo "Deploying to gh-pages ..."
        mkdocs gh-deploy
        echo "Done."
        ;;
    *)
        echo "Skipped deploy. Built site is available at ./site/."
        ;;
esac
