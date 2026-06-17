#!/usr/bin/env python3
"""Validate a single candidate historical analog event record."""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path


REQUIRED_FIELDS = [
    "event_id",
    "event_date",
    "event_title",
    "source",
    "event_family",
    "affected_sector",
    "strategic_importance_level",
    "state_support_signal",
    "restriction_or_pressure_signal",
    "surprise_level",
    "market_interpretation",
    "observed_market_pathway",
    "evidence_note",
]


def load_record(path: Path) -> dict[str, str]:
    if not path.exists():
        raise FileNotFoundError(f"event record not found: {path}")

    if path.suffix.lower() == ".json":
        with path.open(encoding="utf-8") as handle:
            payload = json.load(handle)
        if not isinstance(payload, dict):
            raise ValueError("JSON event record must be a single object.")
        return {str(key): "" if value is None else str(value) for key, value in payload.items()}

    if path.suffix.lower() == ".csv":
        with path.open(newline="", encoding="utf-8") as handle:
            rows = list(csv.DictReader(handle))
        if len(rows) != 1:
            raise ValueError(f"CSV event record must contain exactly one row; found {len(rows)}.")
        return {key: "" if value is None else value for key, value in rows[0].items()}

    raise ValueError("Event record must be a .json or single-row .csv file.")


def validate_record(record: dict[str, str]) -> tuple[list[str], list[str]]:
    missing_fields = [field for field in REQUIRED_FIELDS if field not in record]
    empty_fields = [
        field for field in REQUIRED_FIELDS
        if field in record and not str(record.get(field, "")).strip()
    ]
    return missing_fields, empty_fields


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python3 scripts/validate_event_entry.py path/to/event_record.json")
        print("       python3 scripts/validate_event_entry.py path/to/event_record.csv")
        return 1

    path = Path(sys.argv[1])
    try:
        record = load_record(path)
        missing_fields, empty_fields = validate_record(record)
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: {exc}")
        return 1

    print("Single event entry validation")
    print(f"Record path: {path}")
    print(f"Required fields checked: {len(REQUIRED_FIELDS)}")

    if missing_fields:
        print(f"FAIL: missing required fields: {', '.join(missing_fields)}")
    else:
        print("PASS: all required fields are present")

    if empty_fields:
        print(f"FAIL: empty required fields: {', '.join(empty_fields)}")
    else:
        print("PASS: no required fields are empty")

    if missing_fields or empty_fields:
        print("Validation result: FAILED")
        return 1

    print("Validation result: PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
