#!/usr/bin/env python3
"""Generate deterministic analyst briefs from scenario evidence."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SCENARIO_ANALYSIS_PATH = PROJECT_ROOT / "results" / "interactive_scenario_analysis.json"
OUTPUT_DIR = PROJECT_ROOT / "results"
OUTPUT_PATH = OUTPUT_DIR / "analyst_briefs.json"

LIMITATIONS = [
    "This brief is a deterministic evidence synthesis, not a forecast.",
    "Historical analogs are selected from the current coded dataset and may reflect sample limitations.",
    "Similarity scores summarize qualitative feature overlap and do not imply probabilities.",
    "Observed pathways describe historical patterns in the evidence base and do not estimate expected returns.",
    "This output is not investment advice or a trading recommendation.",
]


def load_scenario_analysis() -> dict[str, Any]:
    if not SCENARIO_ANALYSIS_PATH.exists():
        raise FileNotFoundError(
            f"Scenario analysis file not found: {SCENARIO_ANALYSIS_PATH}. "
            "Run python3 scripts/analyze_scenario_profile.py first."
        )

    with SCENARIO_ANALYSIS_PATH.open(encoding="utf-8") as handle:
        payload = json.load(handle)

    if "results" not in payload or not isinstance(payload["results"], list):
        raise ValueError("Scenario analysis file is missing a results list.")
    return payload


def format_profile(profile: dict[str, str]) -> str:
    return (
        f"Scenario profile codes event family as {profile.get('event_family', 'Not coded')}, "
        f"sector as {profile.get('affected_sector', 'Not coded')}, region as "
        f"{profile.get('country_or_region', 'Not coded')}, strategic importance as "
        f"{profile.get('strategic_importance_level', 'Not coded')}, support signal as "
        f"{profile.get('state_support_signal', 'Not coded')}, pressure signal as "
        f"{profile.get('restriction_or_pressure_signal', 'Not coded')}, and surprise level as "
        f"{profile.get('surprise_level', 'Not coded')}."
    )


def build_analogs(top_analogs: list[dict[str, Any]]) -> list[dict[str, Any]]:
    analogs: list[dict[str, Any]] = []
    for analog in top_analogs:
        analogs.append({
            "event_id": analog.get("event_id", "Not coded"),
            "event_date": analog.get("event_date", "Not coded"),
            "event_title": analog.get("event_title", "Not coded"),
            "similarity_score": analog.get("similarity_score", "Not coded"),
            "observed_market_pathway": analog.get("observed_market_pathway", "Not coded"),
            "matched_fields": analog.get("matched_fields", []),
            "brief_note": (
                f"{analog.get('event_id', 'Not coded')} is included because it shares "
                f"{len(analog.get('matched_fields', []))} coded field(s) with the scenario profile."
            ),
        })
    return analogs


def build_pathway_summary(pathways: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [
        {
            "pathway_name": pathway.get("pathway_name", "Not coded"),
            "count": pathway.get("count", 0),
            "representative_events": pathway.get("representative_events", []),
            "summary_note": (
                f"{pathway.get('pathway_name', 'Not coded')} appears in "
                f"{pathway.get('count', 0)} of the top historical analog(s)."
            ),
        }
        for pathway in pathways
    ]


def build_evidence_notes(top_analogs: list[dict[str, Any]]) -> list[dict[str, str]]:
    return [
        {
            "event_id": analog.get("event_id", "Not coded"),
            "evidence_note": analog.get("evidence_note", "No evidence note available."),
        }
        for analog in top_analogs
    ]


def build_caveats(scenario: dict[str, Any]) -> list[str]:
    top_analogs = scenario.get("top_analogs", [])
    pathway_count = len(scenario.get("observed_pathway_summary", []))
    caveats = [
        f"The brief uses the top {len(top_analogs)} retrieved analog(s) from the current evidence base.",
        f"The pathway summary contains {pathway_count} observed pathway category or categories.",
        "Scenario inputs are predefined coded profiles, not approved historical events.",
        "Evidence notes should be read as qualitative context, not causal proof.",
    ]
    return caveats


def build_brief(scenario: dict[str, Any]) -> dict[str, Any]:
    profile = scenario.get("scenario_profile", {})
    top_analogs = scenario.get("top_analogs", [])
    pathways = scenario.get("observed_pathway_summary", [])

    return {
        "scenario_id": scenario.get("scenario_id", "Not coded"),
        "scenario_question": scenario.get("scenario_question", "Not coded"),
        "scenario_description": {
            "question": scenario.get("scenario_question", "Not coded"),
            "profile_summary": format_profile(profile),
            "analyst_note": scenario.get("analyst_note", "No analyst note available."),
        },
        "most_relevant_historical_analogs": build_analogs(top_analogs),
        "common_observed_pathways": build_pathway_summary(pathways),
        "key_evidence_notes": build_evidence_notes(top_analogs),
        "analytical_caveats": build_caveats(scenario),
        "research_limitations": LIMITATIONS,
    }


def generate_briefs(payload: dict[str, Any]) -> dict[str, Any]:
    briefs = [build_brief(scenario) for scenario in payload["results"]]
    return {
        "source_file": str(SCENARIO_ANALYSIS_PATH.relative_to(PROJECT_ROOT)),
        "brief_count": len(briefs),
        "method": (
            "Deterministic template synthesis from scenario profiles, retrieved historical analogs, "
            "observed pathway summaries, and evidence notes."
        ),
        "disclaimer": "Analyst briefs are descriptive evidence syntheses only. They are not forecasts, probability estimates, expected-return estimates, or investment advice.",
        "briefs": briefs,
    }


def write_output(payload: dict[str, Any]) -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    with OUTPUT_PATH.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2)
        handle.write("\n")


def print_summary(payload: dict[str, Any]) -> None:
    print("Analyst brief generator")
    print(f"Briefs generated: {payload['brief_count']}")
    for brief in payload["briefs"]:
        analogs = ", ".join(
            f"{analog['event_id']}={analog['similarity_score']}"
            for analog in brief["most_relevant_historical_analogs"][:3]
        )
        print(f"- {brief['scenario_id']}: {brief['scenario_question']}")
        print(f"  Top analogs: {analogs}")
    print(f"Output path: {OUTPUT_PATH}")


def main() -> int:
    try:
        source_payload = load_scenario_analysis()
        brief_payload = generate_briefs(source_payload)
        write_output(brief_payload)
        print_summary(brief_payload)
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: {exc}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
