#!/usr/bin/env python3
"""Generate deterministic analyst briefs from historical scenario evidence."""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]
HISTORICAL_EVENTS_PATH = PROJECT_ROOT / "data" / "historical_analogue_events.csv"
SCENARIO_RESULTS_PATH = PROJECT_ROOT / "results" / "scenario_query_demo_results.json"
OBSERVED_PATHWAYS_PATH = PROJECT_ROOT / "results" / "observed_pathways.json"
OUTPUT_DIR = PROJECT_ROOT / "results"
OUTPUT_PATH = OUTPUT_DIR / "analyst_briefs.json"

LIMITATIONS = [
    "This brief is a deterministic historical evidence synthesis, not a forecast.",
    "Historical analogues are limited to the current coded dataset and may not cover all relevant event types.",
    "Similarity scores describe qualitative feature overlap and do not imply probabilities.",
    "Observed pathways summarise retrieved historical patterns and do not estimate expected returns.",
    "This output is not investment advice, a trading recommendation, or a market-timing tool.",
]


def load_json(path: Path, required_key: str) -> dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(f"Required input missing: {path.relative_to(PROJECT_ROOT)}")

    with path.open(encoding="utf-8") as handle:
        payload = json.load(handle)

    if required_key not in payload or not isinstance(payload[required_key], list):
        raise ValueError(f"{path.relative_to(PROJECT_ROOT)} is missing a '{required_key}' list.")
    return payload


def load_historical_events() -> dict[str, dict[str, str]]:
    if not HISTORICAL_EVENTS_PATH.exists():
        raise FileNotFoundError(f"Required input missing: {HISTORICAL_EVENTS_PATH.relative_to(PROJECT_ROOT)}")

    with HISTORICAL_EVENTS_PATH.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return {
            (row.get("event_id") or "").strip(): row
            for row in reader
            if (row.get("event_id") or "").strip()
        }


def index_pathways(pathway_payload: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {
        str(row.get("scenario_id", "")).strip(): row
        for row in pathway_payload.get("results", [])
        if str(row.get("scenario_id", "")).strip()
    }


def describe_profile(profile: dict[str, Any]) -> str:
    return (
        f"The scenario is coded as {profile.get('event_family', 'Not coded')} in "
        f"{profile.get('affected_sector', 'Not coded')}, with strategic importance coded as "
        f"{profile.get('strategic_importance_level', 'Not coded')}, support signal coded as "
        f"{profile.get('state_support_signal', 'Not coded')}, pressure signal coded as "
        f"{profile.get('restriction_or_pressure_signal', 'Not coded')}, and surprise level coded as "
        f"{profile.get('surprise_level', 'Not coded')}."
    )


def build_analogue_entry(analogue: dict[str, Any], event_lookup: dict[str, dict[str, str]]) -> dict[str, Any]:
    event_id = str(analogue.get("event_id", "Not coded"))
    source_event = event_lookup.get(event_id, {})
    return {
        "event_id": event_id,
        "event_date": analogue.get("event_date") or source_event.get("event_date", "Not coded"),
        "event_title": analogue.get("event_title") or source_event.get("event_title", "Not coded"),
        "event_family": source_event.get("event_family", "Not coded"),
        "country_or_region": source_event.get("country_or_region", "Not coded"),
        "affected_sector": source_event.get("affected_sector", "Not coded"),
        "similarity_score": analogue.get("similarity_score", "Not coded"),
        "matched_fields": analogue.get("matched_fields", []),
        "different_fields": analogue.get("different_fields", []),
        "observed_market_pathway": analogue.get("observed_market_pathway")
        or source_event.get("observed_market_pathway", "Not coded"),
        "evidence_note": analogue.get("evidence_note") or source_event.get("evidence_note", "No evidence note available."),
    }


def build_pathways(pathway_row: dict[str, Any]) -> list[dict[str, Any]]:
    pathways: list[dict[str, Any]] = []
    for pathway in pathway_row.get("pathway_summary", []):
        pathways.append({
            "pathway_name": pathway.get("pathway_name", "Not coded"),
            "count": pathway.get("count", 0),
            "representative_events": pathway.get("representative_events", []),
            "evidence_notes": pathway.get("evidence_notes", []),
            "analyst_note": pathway.get("analyst_note", "No analyst note available."),
            "limitations_note": pathway.get("limitations_note", "No limitations note available."),
        })
    return pathways


def build_key_evidence(analogues: list[dict[str, Any]], pathways: list[dict[str, Any]]) -> list[str]:
    evidence: list[str] = []
    for analogue in analogues:
        evidence.append(f"{analogue['event_id']}: {analogue['evidence_note']}")

    for pathway in pathways:
        evidence.append(
            f"{pathway['pathway_name']}: {pathway['count']} retrieved analogue(s), represented by "
            f"{', '.join(pathway.get('representative_events', [])) or 'Not coded'}."
        )
    return evidence


def build_caveats(scenario: dict[str, Any], pathways: list[dict[str, Any]]) -> list[str]:
    top_analogues = scenario.get("top_analogues", [])
    return [
        f"The brief uses {len(top_analogues)} retrieved historical analogue(s) from the current scenario demo.",
        f"The observed pathway section contains {len(pathways)} pathway grouping(s).",
        "The scenario profile is a coded comparison input, not an approved historical event.",
        "Evidence notes are qualitative research context, not causal proof.",
    ]


def build_analyst_note(pathways: list[dict[str, Any]]) -> str:
    if not pathways:
        return "No observed pathway grouping is available for this scenario. Treat the brief as incomplete."

    pathway_names = ", ".join(pathway["pathway_name"] for pathway in pathways)
    return (
        f"The retrieved evidence is organised around {pathway_names}. This supports structured scenario "
        "assessment by showing which historical patterns appear in the current evidence base, without "
        "claiming that those patterns will recur."
    )


def build_brief(
    index: int,
    scenario: dict[str, Any],
    pathway_row: dict[str, Any],
    event_lookup: dict[str, dict[str, str]],
) -> dict[str, Any]:
    scenario_id = scenario.get("scenario_id", f"SQ{index:03d}")
    scenario_title = scenario.get("question") or scenario.get("scenario_question") or "Not coded"
    profile = scenario.get("scenario_profile", {})
    analogues = [
        build_analogue_entry(analogue, event_lookup)
        for analogue in scenario.get("top_analogues", [])
    ]
    pathways = build_pathways(pathway_row)

    return {
        "brief_id": f"BRIEF-{scenario_id}",
        "scenario_id": scenario_id,
        "scenario_title": scenario_title,
        "scenario_description": describe_profile(profile),
        "most_relevant_historical_analogues": analogues,
        "observed_historical_pathways": pathways,
        "key_evidence": build_key_evidence(analogues, pathways),
        "analytical_caveats": build_caveats(scenario, pathways),
        "research_limitations": LIMITATIONS,
        "analyst_note": build_analyst_note(pathways),
    }


def generate_briefs(
    scenario_payload: dict[str, Any],
    pathway_payload: dict[str, Any],
    event_lookup: dict[str, dict[str, str]],
) -> dict[str, Any]:
    pathway_lookup = index_pathways(pathway_payload)
    briefs = [
        build_brief(index, scenario, pathway_lookup.get(scenario.get("scenario_id", ""), {}), event_lookup)
        for index, scenario in enumerate(scenario_payload["results"], start=1)
    ]

    return {
        "source_files": {
            "historical_events": str(HISTORICAL_EVENTS_PATH.relative_to(PROJECT_ROOT)),
            "scenario_results": str(SCENARIO_RESULTS_PATH.relative_to(PROJECT_ROOT)),
            "observed_pathways": str(OBSERVED_PATHWAYS_PATH.relative_to(PROJECT_ROOT)),
        },
        "brief_count": len(briefs),
        "method": (
            "Deterministic template synthesis from scenario profiles, retrieved historical analogues, "
            "observed pathway groupings, and event evidence notes."
        ),
        "disclaimer": (
            "Analyst briefs are descriptive historical evidence syntheses only. They are not forecasts, "
            "probability estimates, expected-return estimates, trading tools, or investment advice."
        ),
        "briefs": briefs,
    }


def write_output(payload: dict[str, Any]) -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    with OUTPUT_PATH.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2)
        handle.write("\n")


def print_summary(payload: dict[str, Any]) -> None:
    print("Analyst brief generator")
    print(f"Historical events source: {payload['source_files']['historical_events']}")
    print(f"Scenario source: {payload['source_files']['scenario_results']}")
    print(f"Observed pathway source: {payload['source_files']['observed_pathways']}")
    print(f"Briefs generated: {payload['brief_count']}")

    for brief in payload["briefs"]:
        analogue_ids = ", ".join(
            analogue["event_id"]
            for analogue in brief["most_relevant_historical_analogues"][:3]
        )
        pathway_names = ", ".join(
            pathway["pathway_name"]
            for pathway in brief["observed_historical_pathways"]
        )
        print(f"- {brief['brief_id']}: {brief['scenario_title']}")
        print(f"  Top analogues: {analogue_ids or 'None'}")
        print(f"  Observed pathways: {pathway_names or 'None'}")

    print(f"Output path: {OUTPUT_PATH.relative_to(PROJECT_ROOT)}")


def main() -> int:
    try:
        event_lookup = load_historical_events()
        scenario_payload = load_json(SCENARIO_RESULTS_PATH, "results")
        pathway_payload = load_json(OBSERVED_PATHWAYS_PATH, "results")
        output_payload = generate_briefs(scenario_payload, pathway_payload, event_lookup)
        write_output(output_payload)
        print_summary(output_payload)
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
