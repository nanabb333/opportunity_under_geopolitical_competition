#!/usr/bin/env python3
"""Run deterministic scenario-query demos against historical analog events."""

from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = PROJECT_ROOT / "data" / "historical_analog_events.csv"
OUTPUT_DIR = PROJECT_ROOT / "results"
OUTPUT_PATH = OUTPUT_DIR / "scenario_query_demo_results.json"

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

NOT_CODED_VALUES = {"", "tbd", "not coded", "none", "na", "n/a"}
TOKEN_PATTERN = re.compile(r"[a-z0-9]+")

SCENARIOS = [
    {
        "scenario_id": "SQ001",
        "question": "What if China announces another large-scale military exercise near Taiwan?",
        "scenario_profile": {
            "event_family": "geopolitical_pressure",
            "affected_sector": "semiconductors",
            "strategic_importance_level": "High",
            "state_support_signal": "No direct support",
            "restriction_or_pressure_signal": "Strong geopolitical-pressure context",
            "surprise_level": "Moderate",
            "market_interpretation": "Threat-dominant contrast event for Taiwan concentration and semiconductor supply-chain exposure",
            "observed_market_pathway": "Restriction pressure pathway",
        },
    },
    {
        "scenario_id": "SQ002",
        "question": "What if the U.S. expands semiconductor export restrictions?",
        "scenario_profile": {
            "event_family": "export_control_pressure",
            "affected_sector": "semiconductors",
            "strategic_importance_level": "High",
            "state_support_signal": "No direct support",
            "restriction_or_pressure_signal": "Strong export-control pressure",
            "surprise_level": "Moderate",
            "market_interpretation": "Threat-dominant contrast event for restricted advanced-computing and semiconductor exposure",
            "observed_market_pathway": "Restriction pressure pathway",
        },
    },
    {
        "scenario_id": "SQ003",
        "question": "What if Taiwan announces new state support for strategic semiconductor firms?",
        "scenario_profile": {
            "event_family": "direct_state_support",
            "affected_sector": "semiconductors",
            "strategic_importance_level": "High",
            "state_support_signal": "Strong named subsidy and capacity-support signal",
            "restriction_or_pressure_signal": "Low",
            "surprise_level": "Moderate",
            "market_interpretation": "Primary named-beneficiary support case for strategic semiconductor capacity",
            "observed_market_pathway": "Named support/downside-offset pathway",
        },
    },
]


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


def load_events() -> list[dict[str, str]]:
    if not INPUT_PATH.exists():
        raise FileNotFoundError(f"Input dataset not found: {INPUT_PATH}")

    with INPUT_PATH.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        rows = list(reader)
        fieldnames = reader.fieldnames or []

    required_fields = [
        "event_id",
        "event_date",
        "event_title",
        "observed_market_pathway",
        "evidence_note",
        *FEATURE_FIELDS,
    ]
    missing_fields = [field for field in required_fields if field not in fieldnames]
    if missing_fields:
        raise ValueError(f"Input dataset is missing required fields: {', '.join(missing_fields)}")
    return rows


def compare_scenario_to_event(
    scenario_profile: dict[str, str],
    event: dict[str, str],
) -> dict[str, str | float | list[str]]:
    total_score = 0.0
    matched_fields: list[str] = []
    different_fields: list[str] = []

    for field in FEATURE_FIELDS:
        field_score = score_field(scenario_profile.get(field), event.get(field))
        total_score += field_score
        if field_score > 0:
            matched_fields.append(field)
        else:
            different_fields.append(field)

    similarity_score = total_score / len(FEATURE_FIELDS)
    return {
        "event_id": event["event_id"],
        "event_date": event["event_date"],
        "event_title": event["event_title"],
        "similarity_score": round(similarity_score, 4),
        "matched_fields": matched_fields,
        "different_fields": different_fields,
        "observed_market_pathway": event["observed_market_pathway"],
        "evidence_note": event["evidence_note"],
    }


def run_demo(events: list[dict[str, str]]) -> dict[str, object]:
    scenario_results: list[dict[str, object]] = []

    for scenario in SCENARIOS:
        comparisons = [
            compare_scenario_to_event(scenario["scenario_profile"], event)
            for event in events
        ]
        comparisons.sort(
            key=lambda row: (
                -float(row["similarity_score"]),
                str(row["event_id"]),
            )
        )
        scenario_results.append({
            "scenario_id": scenario["scenario_id"],
            "question": scenario["question"],
            "scenario_profile": scenario["scenario_profile"],
            "top_analogs": comparisons[:3],
        })

    return {
        "method": "Deterministic qualitative feature matching; exact match = 1, partial textual overlap = 0.5, no match or unavailable coding = 0.",
        "source_dataset": str(INPUT_PATH.relative_to(PROJECT_ROOT)),
        "events_loaded": len(events),
        "scenarios_evaluated": len(SCENARIOS),
        "top_n": 3,
        "disclaimer": "Scenario analogs are for historical comparison only. They are not forecasts, trading signals, or investment recommendations.",
        "results": scenario_results,
    }


def write_output(payload: dict[str, object]) -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    with OUTPUT_PATH.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2)
        handle.write("\n")


def print_summary(payload: dict[str, object]) -> None:
    print("Scenario query demo")
    print(f"Events loaded: {payload['events_loaded']}")
    print(f"Scenarios evaluated: {payload['scenarios_evaluated']}")
    for scenario in payload["results"]:
        print(f"- {scenario['scenario_id']}: {scenario['question']}")
        for analog in scenario["top_analogs"]:
            print(
                f"  - {analog['event_id']}: {analog['similarity_score']:.4f} "
                f"({analog['observed_market_pathway']})"
            )
    print(f"Output path: {OUTPUT_PATH}")


def main() -> int:
    try:
        events = load_events()
        payload = run_demo(events)
        write_output(payload)
        print_summary(payload)
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: {exc}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
