#!/usr/bin/env python3
"""
validate_schema.py

Validate one or more OpenPrint3D instance files (printer/filament/process)
against a given JSON Schema.

Usage:
    python validate_schema.py schema/filament.schema.json filament/Polymaker/PolyLite-PLA.json
    python validate_schema.py schema/printer.schema.json printer/Elegoo/Centauri-Carbon.json
    python validate_schema.py schema/process.schema.json process/Standard/0.20mm-quality.json

Requires:
    pip install jsonschema
"""

import argparse
import json
import sys
from pathlib import Path

from jsonschema import Draft7Validator, exceptions as jsonschema_exceptions


def load_json(path: Path):
    """Load a JSON file and return the parsed object."""
    try:
        with path.open("r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"[ERR] File not found: {path}", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"[ERR] Invalid JSON in {path}: {e}", file=sys.stderr)
        sys.exit(1)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Validate OpenPrint3D instance files against a JSON Schema."
    )
    parser.add_argument(
        "schema",
        type=Path,
        help="Path to the JSON Schema file (e.g. schema/printer.schema.json)",
    )
    parser.add_argument(
        "instances",
        type=Path,
        nargs="+",
        help="One or more instance files to validate (printer/filament/process JSON files).",
    )

    args = parser.parse_args()

    schema_path: Path = args.schema
    instance_paths: list[Path] = args.instances

    schema = load_json(schema_path)

    try:
        validator = Draft7Validator(schema)
    except jsonschema_exceptions.SchemaError as e:
        print(f"[ERR] The schema file is not a valid JSON Schema: {schema_path}", file=sys.stderr)
        print(f"      {e}", file=sys.stderr)
        sys.exit(1)

    exit_code = 0

    for instance_path in instance_paths:
        instance = load_json(instance_path)
        errors = sorted(validator.iter_errors(instance), key=lambda e: list(e.path))

        if not errors:
            print(f"[ OK ] {instance_path}")
            continue

        print(f"[FAIL] {instance_path} is not valid:")
        for err in errors:
            # Build a dotted path to the offending location, if available
            path_str = ".".join(str(p) for p in err.path) if err.path else "<root>"
            print(f"   - at {path_str}: {err.message}")
        exit_code = 1

    sys.exit(exit_code)


if __name__ == "__main__":
    main()
