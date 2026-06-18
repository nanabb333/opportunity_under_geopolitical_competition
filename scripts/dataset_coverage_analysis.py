#!/usr/bin/env python3
"""Analyse coverage of the historical analogue event dataset."""

from __future__ import annotations

import csv
import json
import sys
from collections import Counter
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATASET = PROJECT_ROOT / "data" / "historical_analogue_events.csv"
RESULTS_DIR = PROJECT_ROOT / "results"
REPORT_JSON = RESULTS_DIR / "dataset_coverage_report.json"
SUMMARY_CSV = RESULTS_DIR / "dataset_coverage_summary.csv"

COVERAGE_FIELDS = [
    ("event_family", "Event Family Coverage"),
    ("country_or_region", "Geography Coverage"),
    ("affected_sector", "Sector Coverage"),
    ("strategic_importance_level", "Strategic Importance Coverage"),
    ("surprise_level", "Surprise Level Coverage"),
    ("observed_market_pathway", "Pathway Coverage"),
]

REQUIRED_FIELDS = ["event_id", *[field for field, _label in COVERAGE_FIELDS]]

TARGET_EVENT_FAMILIES = [
    "Military Exercise",
    "Diplomatic Shock",
    "Export Restriction",
    "Technology Restriction",
    "Strategic Investment",
    "Industrial Policy",
    "Sanction",
    "Supply Chain Relocation",
    "Election Event",
    "Leadership Meeting",
    "Semiconductor Expansion",
]

TARGET_SECTORS = [
    "critical minerals",
    "defence systems",
    "telecommunications infrastructure",
    "energy security",
    "battery and clean-energy supply chains",
    "cloud and AI infrastructure",
    "shipping and logistics",
]

TARGET_REGIONS = [
    "Taiwan",
    "China",
    "Japan",
    "South Korea",
    "European Union",
    "Netherlands",
    "India",
    "Southeast Asia",
]

TARGET_PATHWAYS = [
    "military-pressure pathway",
    "diplomatic-shock pathway",
    "sanctions-pressure pathway",
    "election-policy uncertainty pathway",
    "leadership-meeting escalation pathway",
    "supply-chain relocation pathway",
]

TARGET_ALIASES = {
    "Export Restriction": ["export_control_pressure", "allied_export_control_pressure"],
    "Industrial Policy": ["direct_state_support", "broad_policy_support"],
    "Semiconductor Expansion": ["implementation_reallocation", "Capacity reallocation pathway"],
    "China": ["China", "US/Taiwan", "Japan/Taiwan"],
    "Japan": ["Japan", "Japan/Taiwan"],
    "South Korea": ["US/South Korea"],
    "Taiwan": ["US/Taiwan", "Japan/Taiwan"],
}


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


def normalise(value: str) -> str:
    return value.strip().lower().replace("_", " ").replace("-", " ")


def existing_values(rows: list[dict[str, str]], field: str) -> set[str]:
    return {normalise(row.get(field, "")) for row in rows if row.get(field, "").strip()}


def target_is_present(target: str, existing: set[str]) -> bool:
    aliases = [target, *TARGET_ALIASES.get(target, [])]
    return any(
        normalise(alias) in value or value in normalise(alias)
        for alias in aliases
        for value in existing
    )


def missing_targets(rows: list[dict[str, str]], field: str, targets: list[str]) -> list[str]:
    existing = existing_values(rows, field)
    return [target for target in targets if not target_is_present(target, existing)]


def build_evidence_gaps(rows: list[dict[str, str]]) -> dict[str, object]:
    missing_families = missing_targets(rows, "event_family", TARGET_EVENT_FAMILIES)
    missing_sectors = missing_targets(rows, "affected_sector", TARGET_SECTORS)
    missing_regions = missing_targets(rows, "country_or_region", TARGET_REGIONS)
    missing_pathways = missing_targets(rows, "observed_market_pathway", TARGET_PATHWAYS)

    high_priority = [
        f"Event family gap: {family}"
        for family in missing_families[:6]
    ] + [
        f"Pathway gap: {pathway}"
        for pathway in missing_pathways[:4]
    ]

    medium_priority = [
        f"Sector gap: {sector}"
        for sector in missing_sectors[:5]
    ] + [
        f"Region gap: {region}"
        for region in missing_regions[:4]
    ]

    low_priority = [
        "Additional U.S. semiconductor subsidy cases",
        "Additional broad policy-support cases",
        "Additional implementation-only facility-opening cases",
    ]

    return {
        "high_priority": high_priority,
        "medium_priority": medium_priority,
        "low_priority": low_priority,
        "missing_event_families": missing_families,
        "missing_sectors": missing_sectors,
        "missing_regions": missing_regions,
        "missing_pathways": missing_pathways,
        "note": "Evidence gaps are generated from target coverage categories and current dataset labels. They are collection priorities, not analytical findings.",
    }


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
        "evidence_gaps": build_evidence_gaps(rows),
        "notes": [
            "Coverage counts are descriptive only.",
            "Counts do not imply forecast accuracy, causal strength, or investment relevance.",
            "Low-count categories should be prioritised for future sourced event collection.",
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
    gaps = report["evidence_gaps"]
    assert isinstance(gaps, dict)
    print("\nHigh Priority Evidence Gaps:")
    for gap in gaps["high_priority"]:
        print(f"- {gap}")
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
