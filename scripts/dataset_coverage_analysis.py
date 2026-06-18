#!/usr/bin/env python3
"""Analyze coverage of the historical analog event dataset."""

from __future__ import annotations

import csv
import json
import sys
from collections import Counter
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATASET = PROJECT_ROOT / "data" / "historical_analog_events.csv"
RESULTS_DIR = PROJECT_ROOT / "results"
REPORT_JSON = RESULTS_DIR / "dataset_coverage_report.json"
SUMMARY_CSV = RESULTS_DIR / "dataset_coverage_summary.csv"

COVERAGE_FIELDS = [
    ("event_family", "Event Family Coverage"),
    ("affected_sector", "Sector Coverage"),
    ("country_or_region", "Geography Coverage"),
    ("strategic_importance_level", "Strategic Importance Coverage"),
    ("surprise_level", "Surprise Level Coverage"),
    ("state_support_signal", "State Support Coverage"),
]

REQUIRED_FIELDS = ["event_id", *[field for field, _label in COVERAGE_FIELDS]]


def load_events() -> list[dict[str, str]]:
    if not DATASET.exists():
        raise FileNotFoundError(f"Dataset not found: {DATASET}")

    with DATASET.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        rows = list(reader)
        fieldnames = reader.fieldnames or []

    missing_fields = [field for field in REQUIRED_FIELDS if field not in fieldnames]
    if missing_fields:
        raise ValueError(f"Dataset missing required fields: {', '.join(missing_fields)}")
    return rows


def count_field(rows: list[dict[str, str]], field: str) -> list[dict[str, int | str]]:
    counts = Counter((row.get(field) or "Not coded").strip() or "Not coded" for row in rows)
    return [
        {"value": value, "count": count}
        for value, count in sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    ]


def build_report(rows: list[dict[str, str]]) -> dict[str, object]:
    coverage = {
        field: {
            "label": label,
            "counts": count_field(rows, field),
        }
        for field, label in COVERAGE_FIELDS
    }

    return {
        "source_dataset": str(DATASET.relative_to(PROJECT_ROOT)),
        "dataset_size": len(rows),
        "coverage": coverage,
        "notes": [
            "Coverage counts are descriptive only.",
            "Counts do not imply forecast accuracy, causal strength, or investment relevance.",
            "Low-count categories should be prioritized for future sourced event collection.",
        ],
    }


def write_report(report: dict[str, object]) -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    with REPORT_JSON.open("w", encoding="utf-8") as handle:
        json.dump(report, handle, indent=2)
        handle.write("\n")

    with SUMMARY_CSV.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["coverage_type", "field", "value", "count"])
        writer.writeheader()
        coverage = report["coverage"]
        assert isinstance(coverage, dict)
        for field, payload in coverage.items():
            label = payload["label"]
            for row in payload["counts"]:
                writer.writerow({
                    "coverage_type": label,
                    "field": field,
                    "value": row["value"],
                    "count": row["count"],
                })


def print_summary(report: dict[str, object]) -> None:
    print("Dataset coverage analysis")
    print(f"Dataset: {report['source_dataset']}")
    print(f"Dataset size: {report['dataset_size']}")
    coverage = report["coverage"]
    assert isinstance(coverage, dict)
    for field, payload in coverage.items():
        print(f"\n{payload['label']}:")
        for row in payload["counts"]:
            print(f"- {row['value']}: {row['count']}")
    print(f"\nJSON output: {REPORT_JSON}")
    print(f"CSV output: {SUMMARY_CSV}")


def main() -> int:
    try:
        rows = load_events()
        report = build_report(rows)
        write_report(report)
        print_summary(report)
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: {exc}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
