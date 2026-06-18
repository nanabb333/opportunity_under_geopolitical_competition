#!/usr/bin/env python3
"""Validate the historical analogue event dataset."""

from __future__ import annotations

import csv
import sys
from collections import Counter
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATASET = PROJECT_ROOT / "data" / "historical_analogue_events.csv"

REQUIRED_COLUMNS = [
    "event_id",
    "event_date",
    "event_title",
    "event_family",
    "country_or_region",
    "affected_sector",
    "strategic_importance_level",
    "state_support_signal",
    "restriction_or_pressure_signal",
    "surprise_level",
    "market_interpretation",
    "observed_market_pathway",
    "linked_primary_case",
    "evidence_note",
]


def main() -> int:
    if not DATASET.exists():
        print(f"ERROR: dataset not found: {DATASET}")
        return 1

    with DATASET.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        rows = list(reader)
        fieldnames = reader.fieldnames or []

    missing_columns = [column for column in REQUIRED_COLUMNS if column not in fieldnames]
    extra_columns = [column for column in fieldnames if column not in REQUIRED_COLUMNS]

    event_ids = [(row.get("event_id") or "").strip() for row in rows]
    empty_event_id_rows = [index for index, event_id in enumerate(event_ids, start=2) if not event_id]
    duplicate_event_ids = sorted(
        event_id for event_id, count in Counter(event_ids).items() if event_id and count > 1
    )

    missing_values: dict[str, int] = {}
    for column in REQUIRED_COLUMNS:
        missing_values[column] = sum(
            1 for row in rows if not (row.get(column) or "").strip()
        )
    columns_with_missing_values = {
        column: count for column, count in missing_values.items() if count > 0
    }

    print("Historical analogue dataset validation")
    print(f"Dataset: {DATASET}")
    print(f"Rows: {len(rows)}")
    print(f"Required columns present: {'yes' if not missing_columns else 'no'}")
    print(f"Unique non-empty event_id values: {len(set(event_ids)) if not empty_event_id_rows else 'no'}")

    if extra_columns:
        print(f"Extra columns: {', '.join(extra_columns)}")
    if missing_columns:
        print(f"ERROR: missing required columns: {', '.join(missing_columns)}")
    if empty_event_id_rows:
        print(f"ERROR: empty event_id values on CSV rows: {empty_event_id_rows}")
    if duplicate_event_ids:
        print(f"ERROR: duplicate event_id values: {', '.join(duplicate_event_ids)}")

    if columns_with_missing_values:
        print("Missing value counts:")
        for column, count in columns_with_missing_values.items():
            print(f"- {column}: {count}")
    else:
        print("Missing value counts: none")

    if missing_columns or empty_event_id_rows or duplicate_event_ids:
        print("Validation result: FAILED")
        return 1

    print("Validation result: PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
