#!/usr/bin/env python3
"""Analyse coded scenario profiles against historical analogue events."""

from __future__ import annotations

import csv
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SCENARIO_PATH = PROJECT_ROOT / "data" / "sample_scenario_profiles.csv"
EVENT_PATH = PROJECT_ROOT / "data" / "historical_analogue_events.csv"
OUTPUT_DIR = PROJECT_ROOT / "results"
OUTPUT_PATH = OUTPUT_DIR / "interactive_scenario_analysis.json"

COMPARISON_FIELDS = [
    "event_family",
    "affected_sector",
    "country_or_region",
    "strategic_importance_level",
    "state_support_signal",
    "restriction_or_pressure_signal",
    "surprise_level",
]

SCENARIO_REQUIRED_FIELDS = [
    "scenario_id",
    "scenario_question",
    *COMPARISON_FIELDS,
    "analyst_note",
]

EVENT_REQUIRED_FIELDS = [
    "event_id",
    "event_date",
    "event_title",
    *COMPARISON_FIELDS,
    "observed_market_pathway",
    "evidence_note",
]

NOT_CODED_VALUES = {"", "tbd", "not coded", "none", "na", "n/a"}
TOKEN_PATTERN = re.compile(r"[a-z0-9]+")

LIMITATIONS_NOTE = (
    "Scenario comparison is deterministic and descriptive. It retrieves historical "
    "analogues from the current evidence base and does not forecast outcomes or "
    "provide investment advice."
)


def normalize(value: str | None) -> str:
    return (value or "").strip().lower()


def tokenize(value: str | None) -> set[str]:
    normalized = normalize(value)
    if normalized in NOT_CODED_VALUES:
        return set()
    return set(TOKEN_PATTERN.findall(normalized))


def score_field(scenario_value: str | None, event_value: str | None) -> float:
    scenario_normalized = normalize(scenario_value)
    event_normalized = normalize(event_value)

    if scenario_normalized in NOT_CODED_VALUES or event_normalized in NOT_CODED_VALUES:
        return 0.0
    if scenario_normalized == event_normalized:
        return 1.0

    scenario_tokens = tokenize(scenario_value)
    event_tokens = tokenize(event_value)
    if scenario_tokens and event_tokens and scenario_tokens & event_tokens:
        return 0.5
    return 0.0


def load_csv(path: Path, required_fields: list[str]) -> list[dict[str, str]]:
    if not path.exists():
        raise FileNotFoundError(f"Required file not found: {path}")

    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        rows = list(reader)
        fieldnames = reader.fieldnames or []

    missing_fields = [field for field in required_fields if field not in fieldnames]
    if missing_fields:
        raise ValueError(f"{path} is missing required fields: {', '.join(missing_fields)}")
    return rows


def compare_scenario_to_event(
    scenario: dict[str, str],
    event: dict[str, str],
) -> dict[str, Any]:
    total_score = 0.0
    matched_fields: list[str] = []
    different_fields: list[str] = []

    for field in COMPARISON_FIELDS:
        field_score = score_field(scenario.get(field), event.get(field))
        total_score += field_score
        if field_score > 0:
            matched_fields.append(field)
        else:
            different_fields.append(field)

    similarity_score = total_score / len(COMPARISON_FIELDS)
    return {
        "event_id": event["event_id"],
        "event_date": event["event_date"],
        "event_title": event["event_title"],
        "event_family": event["event_family"],
        "affected_sector": event["affected_sector"],
        "country_or_region": event["country_or_region"],
        "similarity_score": round(similarity_score, 4),
        "matched_fields": matched_fields,
        "different_fields": different_fields,
        "observed_market_pathway": event["observed_market_pathway"],
        "evidence_note": event["evidence_note"],
    }


def summarise_pathways(top_analogues: list[dict[str, Any]]) -> list[dict[str, Any]]:
    pathway_counts = Counter(
        analogue.get("observed_market_pathway") or "Not coded"
        for analogue in top_analogues
    )
    representative_events: dict[str, list[str]] = defaultdict(list)

    for analogue in top_analogues:
        pathway = analogue.get("observed_market_pathway") or "Not coded"
        representative_events[pathway].append(str(analogue["event_id"]))

    return [
        {
            "pathway_name": pathway,
            "count": count,
            "representative_events": representative_events[pathway],
        }
        for pathway, count in pathway_counts.most_common()
    ]


def analyse_scenarios(
    scenarios: list[dict[str, str]],
    events: list[dict[str, str]],
    top_n: int = 5,
) -> dict[str, Any]:
    results: list[dict[str, Any]] = []

    for scenario in scenarios:
        comparisons = [
            compare_scenario_to_event(scenario, event)
            for event in events
        ]
        comparisons.sort(
            key=lambda row: (
                -float(row["similarity_score"]),
                str(row["event_date"]),
                str(row["event_id"]),
            )
        )
        top_analogues = comparisons[:top_n]
        results.append({
            "scenario_id": scenario["scenario_id"],
            "scenario_question": scenario["scenario_question"],
            "scenario_profile": {
                field: scenario[field]
                for field in COMPARISON_FIELDS
            },
            "analyst_note": scenario["analyst_note"],
            "top_analogues": top_analogues,
            "observed_pathway_summary": summarise_pathways(top_analogues),
            "evidence_notes": [
                {
                    "event_id": analogue["event_id"],
                    "evidence_note": analogue["evidence_note"],
                }
                for analogue in top_analogues
            ],
            "limitations_note": LIMITATIONS_NOTE,
        })

    return {
        "source_scenarios": str(SCENARIO_PATH.relative_to(PROJECT_ROOT)),
        "source_events": str(EVENT_PATH.relative_to(PROJECT_ROOT)),
        "scenario_count": len(scenarios),
        "event_count": len(events),
        "top_n": top_n,
        "comparison_fields": COMPARISON_FIELDS,
        "method": (
            "Deterministic qualitative feature matching; exact match = 1, partial "
            "textual overlap = 0.5, no match or unavailable coding = 0. Scores are "
            "divided by the number of comparable scenario fields."
        ),
        "limitations_note": LIMITATIONS_NOTE,
        "results": results,
    }


def write_output(payload: dict[str, Any]) -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    with OUTPUT_PATH.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2)
        handle.write("\n")


def print_summary(payload: dict[str, Any]) -> None:
    print("Interactive scenario analysis")
    print(f"Scenarios loaded: {payload['scenario_count']}")
    print(f"Historical events loaded: {payload['event_count']}")
    print(f"Top analogues per scenario: {payload['top_n']}")
    for scenario in payload["results"]:
        print(f"- {scenario['scenario_id']}: {scenario['scenario_question']}")
        for analogue in scenario["top_analogues"][:3]:
            print(
                f"  - {analogue['event_id']}: {analogue['similarity_score']:.4f} "
                f"({analogue['observed_market_pathway']})"
            )
    print(f"Output path: {OUTPUT_PATH}")


def main() -> int:
    try:
        scenarios = load_csv(SCENARIO_PATH, SCENARIO_REQUIRED_FIELDS)
        events = load_csv(EVENT_PATH, EVENT_REQUIRED_FIELDS)
        payload = analyse_scenarios(scenarios, events)
        write_output(payload)
        print_summary(payload)
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: {exc}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
