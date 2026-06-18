#!/usr/bin/env python3
"""Run deterministic scenario-query demos against historical analogue events."""

from __future__ import annotations

import csv
import json
import re
import sys
from collections import Counter
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = PROJECT_ROOT / "data" / "historical_analogue_events.csv"
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

TRANSPARENCY_DIMENSIONS = [
    ("event_family", "Event Family"),
    ("affected_sector", "Strategic Sector"),
    ("strategic_importance_level", "Strategic Importance"),
    ("state_support_signal", "State Support Signal"),
    ("restriction_or_pressure_signal", "Geopolitical Context"),
]

CAVEATS = [
    "Historical analogue does not imply future repetition.",
    "Dataset coverage limitations may apply.",
    "Observed pathways are descriptive rather than predictive.",
    "Similarity scores summarise coded feature overlap and are not probability estimates.",
]

NOT_CODED_VALUES = {"", "tbd", "not coded", "none", "na", "n/a"}
TOKEN_PATTERN = re.compile(r"[a-z0-9]+")

SCENARIOS = [
    {
        "scenario_id": "SQ001",
        "question": "What if China announces another large-scale military exercise near Taiwan?",
        "scenario_profile": {
            "event_family": "Military Exercise",
            "affected_sector": "semiconductors",
            "strategic_importance_level": "High",
            "state_support_signal": "No direct support",
            "restriction_or_pressure_signal": "Strong military pressure",
            "surprise_level": "Moderate",
            "market_interpretation": "Military pressure and Taiwan concentration supply-chain exposure",
            "observed_market_pathway": "Military escalation pathway",
        },
    },
    {
        "scenario_id": "SQ002",
        "question": "What if the U.S. expands semiconductor export restrictions?",
        "scenario_profile": {
            "event_family": "Export Restriction",
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
            "event_family": "Industrial Policy",
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


def status_from_score(field_score: float) -> str:
    if field_score == 1.0:
        return "Match"
    if field_score == 0.5:
        return "Partial Match"
    return "Different"


def coverage_classification(event_family: str, family_counts: Counter[str]) -> str:
    family_count = family_counts[event_family]
    if family_count >= 5:
        return "Well represented family"
    if family_count >= 3:
        return "Moderate family coverage"
    return "Limited family coverage"


def build_match_dimensions(
    scenario_profile: dict[str, str],
    event: dict[str, str],
) -> list[dict[str, str]]:
    dimensions: list[dict[str, str]] = []
    for field, label in TRANSPARENCY_DIMENSIONS:
        field_score = score_field(scenario_profile.get(field), event.get(field))
        dimensions.append({
            "field": field,
            "label": label,
            "scenario_value": scenario_profile.get(field, "Not coded"),
            "event_value": event.get(field, "Not coded"),
            "status": status_from_score(field_score),
        })
    return dimensions


def plain_list(values: list[str]) -> str:
    if not values:
        return "no primary dimensions"
    if len(values) == 1:
        return values[0]
    return f"{', '.join(values[:-1])}, and {values[-1]}"


def build_similarity_explanation(match_dimensions: list[dict[str, str]]) -> str:
    matches = [
        dimension["label"].lower()
        for dimension in match_dimensions
        if dimension["status"] in {"Match", "Partial Match"}
    ]
    return f"Retrieved because the scenario and historical event overlap on {plain_list(matches)}."


def build_divergence_explanation(match_dimensions: list[dict[str, str]]) -> str:
    differences = [
        f"{dimension['label'].lower()} ({dimension['scenario_value']} versus {dimension['event_value']})"
        for dimension in match_dimensions
        if dimension["status"] == "Different"
    ]
    if not differences:
        return "No major coded differences appear across the transparency dimensions."
    return f"Important differences remain in {plain_list(differences)}."


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
    family_counts: Counter[str],
) -> dict[str, str | float | list[str]]:
    total_score = 0.0
    matched_fields: list[str] = []
    different_fields: list[str] = []
    denominator = sum(FEATURE_WEIGHTS[field] for field in FEATURE_FIELDS)

    for field in FEATURE_FIELDS:
        field_score = score_field(scenario_profile.get(field), event.get(field))
        total_score += field_score * FEATURE_WEIGHTS[field]
        if field_score > 0:
            matched_fields.append(field)
        else:
            different_fields.append(field)

    similarity_score = total_score / denominator
    match_dimensions = build_match_dimensions(scenario_profile, event)
    return {
        "event_id": event["event_id"],
        "event_date": event["event_date"],
        "event_title": event["event_title"],
        "event_family": event["event_family"],
        "affected_sector": event["affected_sector"],
        "strategic_importance_level": event["strategic_importance_level"],
        "state_support_signal": event["state_support_signal"],
        "restriction_or_pressure_signal": event["restriction_or_pressure_signal"],
        "similarity_score": round(similarity_score, 4),
        "matched_fields": matched_fields,
        "different_fields": different_fields,
        "observed_market_pathway": event["observed_market_pathway"],
        "evidence_note": event["evidence_note"],
        "match_dimensions": match_dimensions,
        "similarity_explanation": build_similarity_explanation(match_dimensions),
        "divergence_explanation": build_divergence_explanation(match_dimensions),
        "evidence_metadata": {
            "event_id": event["event_id"],
            "event_family": event["event_family"],
            "strategic_sector": event["affected_sector"],
            "coverage_classification": coverage_classification(event["event_family"], family_counts),
        },
        "analyst_caveats": CAVEATS,
    }


def run_demo(events: list[dict[str, str]]) -> dict[str, object]:
    scenario_results: list[dict[str, object]] = []
    family_counts = Counter(event["event_family"] for event in events)

    for scenario in SCENARIOS:
        comparisons = [
            compare_scenario_to_event(scenario["scenario_profile"], event, family_counts)
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
            "top_analogues": comparisons[:3],
        })

    return {
        "method": "Deterministic qualitative feature matching; exact match = 1, partial textual overlap = 0.5, no match or unavailable coding = 0.",
        "source_dataset": str(INPUT_PATH.relative_to(PROJECT_ROOT)),
        "events_loaded": len(events),
        "scenarios_evaluated": len(SCENARIOS),
        "top_n": 3,
        "feature_weights": FEATURE_WEIGHTS,
        "disclaimer": "Scenario analogues are for historical comparison only. They are not forecasts, trading signals, or investment recommendations.",
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
        for analogue in scenario["top_analogues"]:
            print(
                f"  - {analogue['event_id']}: {analogue['similarity_score']:.4f} "
                f"({analogue['observed_market_pathway']})"
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
