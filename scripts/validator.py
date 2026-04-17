#!/usr/bin/env python3
"""Validate every stack.json under /sectors against the root schema.json.

Usage:
    python scripts/validator.py

Exit codes:
    0 — all files valid
    1 — one or more validation failures
    2 — setup error (schema missing, jsonschema not installed, etc.)
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

try:
    from jsonschema import Draft202012Validator
except ImportError:
    print("ERROR: jsonschema is not installed. Run: pip install jsonschema", file=sys.stderr)
    sys.exit(2)


REPO_ROOT = Path(__file__).resolve().parent.parent
SCHEMA_PATH = REPO_ROOT / "schema.json"
SECTORS_DIR = REPO_ROOT / "sectors"
TEMPLATE_DIR_NAME = "_template"


def load_schema() -> dict:
    if not SCHEMA_PATH.exists():
        print(f"ERROR: schema not found at {SCHEMA_PATH}", file=sys.stderr)
        sys.exit(2)
    with SCHEMA_PATH.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def find_stack_files() -> list[Path]:
    if not SECTORS_DIR.exists():
        print(f"ERROR: sectors directory not found at {SECTORS_DIR}", file=sys.stderr)
        sys.exit(2)
    return [
        path
        for path in SECTORS_DIR.rglob("stack.json")
        if TEMPLATE_DIR_NAME not in path.parts
    ]


def validate_file(validator: Draft202012Validator, path: Path) -> list[str]:
    try:
        with path.open("r", encoding="utf-8") as handle:
            data = json.load(handle)
    except json.JSONDecodeError as exc:
        return [f"invalid JSON: {exc.msg} (line {exc.lineno}, column {exc.colno})"]

    errors = sorted(validator.iter_errors(data), key=lambda err: list(err.absolute_path))
    messages: list[str] = []
    for error in errors:
        location = ".".join(str(part) for part in error.absolute_path) or "<root>"
        messages.append(f"{location}: {error.message}")

    expected_industry = path.parent.parent.name
    actual_industry = data.get("industry") if isinstance(data, dict) else None
    if actual_industry and actual_industry != expected_industry:
        messages.append(
            f"industry mismatch: file is under /sectors/{expected_industry}/ "
            f"but declares industry '{actual_industry}'"
        )

    return messages


def main() -> int:
    schema = load_schema()
    validator = Draft202012Validator(schema)

    stack_files = find_stack_files()
    if not stack_files:
        print("No stack.json files found under /sectors (excluding templates). Nothing to validate.")
        return 0

    failures = 0
    for path in stack_files:
        relative = path.relative_to(REPO_ROOT)
        errors = validate_file(validator, path)
        if errors:
            failures += 1
            print(f"FAIL  {relative}")
            for message in errors:
                print(f"      - {message}")
        else:
            print(f"OK    {relative}")

    print()
    print(f"Validated {len(stack_files)} file(s), {failures} failure(s).")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
