#!/usr/bin/env python3
"""Calculate deterministic pairwise similarity for historical analogue events."""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = PROJECT_ROOT / "data" / "historical_analogue_events.csv"
OUTPUT_DIR = PROJECT_ROOT / "results"
OUTPUT_PATH = OUTPUT_DIR / "historical_similarity_matrix.csv"

FEATURE_FIELDS = [
    "event_family",
    "affected_sector",
    "strategic_importance_level",
    "state_support_signal",
    "restriction_or_pressure_signal",
    "surprise_level",
    "market_interpretation",
    "observed_market_pathway",
]

FEATURE_WEIGHTS = {
    "event_family": 3,
    "affected_sector": 2,
    "observed_market_pathway": 2,
    "restriction_or_pressure_signal": 2,
    "strategic_importance_level": 1,
    "state_support_signal": 1,
    "surprise_level": 1,
    "market_interpretation": 1,
}

OUTPUT_COLUMNS = [
    "source_event_id",
    "comparison_event_id",
    "similarity_score",
    "matched_fields",
    "different_fields",
    "interpretation_note",
]

NOT_CODED_VALUES = {"", "tbd", "not coded", "none", "na", "n/a"}
TOKEN_PATTERN = re.compile(r"[a-z0-9]+")


def normalize(value: str | None) -> str:
    return (value or "").strip().lower()


def tokenize(value: str | None) -> set[str]:
    normalized = normalize(value)
    if normalized in NOT_CODED_VALUES:
        return set()
    return set(TOKEN_PATTERN.findall(normalized))


def score_field(source_value: str | None, comparison_value: str | None) -> float:
    source_normalized = normalize(source_value)
    comparison_normalized = normalize(comparison_value)

    if source_normalized in NOT_CODED_VALUES or comparison_normalized in NOT_CODED_VALUES:
        return 0.0
    if source_normalized == comparison_normalized:
        return 1.0

    source_tokens = tokenize(source_value)
    comparison_tokens = tokenize(comparison_value)
    if source_tokens and comparison_tokens and source_tokens & comparison_tokens:
        return 0.5
    return 0.0


def build_interpretation_note(score: float, matched_fields: list[str]) -> str:
    if score >= 0.75:
        level = "High similarity"
    elif score >= 0.50:
        level = "Moderate similarity"
    elif score > 0:
        level = "Low similarity"
    else:
        level = "No coded similarity"

    if matched_fields:
        return f"{level} based on overlap in {', '.join(matched_fields)}."
    return f"{level}; no compared fields matched or partially overlapped."


def load_events() -> list[dict[str, str]]:
    if not INPUT_PATH.exists():
        raise FileNotFoundError(f"Input dataset not found: {INPUT_PATH}")

    with INPUT_PATH.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        rows = list(reader)
        fieldnames = reader.fieldnames or []

    missing_fields = [field for field in ["event_id", *FEATURE_FIELDS] if field not in fieldnames]
    if missing_fields:
        raise ValueError(f"Input dataset is missing required fields: {', '.join(missing_fields)}")
    return rows


def calculate_pairs(events: list[dict[str, str]]) -> list[dict[str, str]]:
    pair_rows: list[dict[str, str]] = []
    denominator = sum(FEATURE_WEIGHTS[field] for field in FEATURE_FIELDS)

    for source in events:
        for comparison in events:
            if source["event_id"] == comparison["event_id"]:
                continue

            total_score = 0.0
            matched_fields: list[str] = []
            different_fields: list[str] = []

            for field in FEATURE_FIELDS:
                field_score = score_field(source.get(field), comparison.get(field))
                total_score += field_score * FEATURE_WEIGHTS[field]
                if field_score > 0:
                    matched_fields.append(field)
                else:
                    different_fields.append(field)

            similarity_score = total_score / denominator
            pair_rows.append({
                "source_event_id": source["event_id"],
                "comparison_event_id": comparison["event_id"],
                "similarity_score": f"{similarity_score:.4f}",
                "matched_fields": ";".join(matched_fields) if matched_fields else "None",
                "different_fields": ";".join(different_fields) if different_fields else "None",
                "interpretation_note": build_interpretation_note(similarity_score, matched_fields),
            })

    pair_rows.sort(
        key=lambda row: (
            -float(row["similarity_score"]),
            row["source_event_id"],
            row["comparison_event_id"],
        )
    )
    return pair_rows


def write_output(pair_rows: list[dict[str, str]]) -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    with OUTPUT_PATH.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=OUTPUT_COLUMNS)
        writer.writeheader()
        writer.writerows(pair_rows)


def print_summary(events: list[dict[str, str]], pair_rows: list[dict[str, str]]) -> None:
    print("Historical similarity engine")
    print(f"Events loaded: {len(events)}")
    print(f"Event pairs generated: {len(pair_rows)}")
    print("Feature weights:")
    for field in FEATURE_FIELDS:
        print(f"- {field}: {FEATURE_WEIGHTS[field]}")
    print("Top 10 most similar event pairs:")
    for row in pair_rows[:10]:
        print(
            f"- {row['source_event_id']} -> {row['comparison_event_id']}: "
            f"{row['similarity_score']} ({row['matched_fields']})"
        )
    print(f"Output path: {OUTPUT_PATH}")


def main() -> int:
    try:
        events = load_events()
        pair_rows = calculate_pairs(events)
        write_output(pair_rows)
        print_summary(events, pair_rows)
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: {exc}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
