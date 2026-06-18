#!/usr/bin/env python3
"""Summarise observed pathways from scenario-query analogue results."""

from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = PROJECT_ROOT / "results" / "scenario_query_demo_results.json"
OUTPUT_DIR = PROJECT_ROOT / "results"
OUTPUT_PATH = OUTPUT_DIR / "observed_pathways.json"


def load_scenario_results() -> dict[str, Any]:
    if not INPUT_PATH.exists():
        raise FileNotFoundError(f"Scenario query results not found: {INPUT_PATH}")
    with INPUT_PATH.open(encoding="utf-8") as handle:
        payload = json.load(handle)
    if "results" not in payload or not isinstance(payload["results"], list):
        raise ValueError("Scenario query results must contain a list under 'results'.")
    return payload


def analyst_note_for_pathway(pathway_name: str, count: int, total: int) -> str:
    share_text = f"{count} of {total} retrieved analogues"
    lowered = pathway_name.lower()

    if "restriction pressure" in lowered:
        return (
            f"{share_text} fall into a restriction-pressure historical pattern. "
            "This supports reading the scenario evidence through pressure, access-loss, "
            "or compliance-burden channels rather than direct state-support channels."
        )
    if "named support/downside-offset" in lowered:
        return (
            f"{share_text} fall into a named-support/downside-offset historical pattern. "
            "This suggests the closest analogues centre on credible support for strategically "
            "important firms, while still requiring case-specific interpretation."
        )
    if "named support" in lowered:
        return (
            f"{share_text} fall into a named-support historical pattern. "
            "This points to state-support logic, but the retrieved analogues may differ in "
            "market relevance, timing quality, or beneficiary visibility."
        )
    return (
        f"{share_text} fall into this observed pathway. The pathway should be treated as "
        "descriptive scenario evidence and checked against the underlying event notes."
    )


def limitations_note() -> str:
    return (
        "This pathway summary is descriptive. It groups the top analogues returned by the "
        "scenario demo and does not assign probabilities, estimate market effects, or "
        "provide trading or investment guidance."
    )


def summarise_pathways(payload: dict[str, Any]) -> dict[str, Any]:
    scenario_summaries: list[dict[str, Any]] = []

    for scenario in payload["results"]:
        top_analogues = scenario.get("top_analogues", [])
        grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
        for analogue in top_analogues:
            pathway = analogue.get("observed_market_pathway", "Not coded")
            grouped[pathway].append(analogue)

        pathway_summary: list[dict[str, Any]] = []
        total = len(top_analogues)
        for pathway_name, analogues in sorted(
            grouped.items(),
            key=lambda item: (-len(item[1]), item[0]),
        ):
            pathway_summary.append({
                "pathway_name": pathway_name,
                "count": len(analogues),
                "representative_events": [analogue.get("event_id", "Not coded") for analogue in analogues],
                "evidence_notes": [
                    {
                        "event_id": analogue.get("event_id", "Not coded"),
                        "evidence_note": analogue.get("evidence_note", "Not coded"),
                    }
                    for analogue in analogues
                ],
                "analyst_note": analyst_note_for_pathway(pathway_name, len(analogues), total),
                "limitations_note": limitations_note(),
            })

        scenario_summaries.append({
            "scenario_id": scenario.get("scenario_id", "Not coded"),
            "scenario_question": scenario.get("question", "Not coded"),
            "pathway_summary": pathway_summary,
        })

    return {
        "method": "Groups each scenario's top historical analogues by observed_market_pathway and preserves representative event evidence.",
        "source_file": str(INPUT_PATH.relative_to(PROJECT_ROOT)),
        "scenarios_summarised": len(scenario_summaries),
        "results": scenario_summaries,
    }


def write_output(payload: dict[str, Any]) -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    with OUTPUT_PATH.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2)
        handle.write("\n")


def print_summary(payload: dict[str, Any]) -> None:
    print("Observed pathway engine")
    print(f"Scenarios summarised: {payload['scenarios_summarised']}")
    for scenario in payload["results"]:
        print(f"- {scenario['scenario_id']}: {scenario['scenario_question']}")
        for pathway in scenario["pathway_summary"]:
            events = ", ".join(pathway["representative_events"])
            print(f"  - {pathway['pathway_name']}: {pathway['count']} analogue(s): {events}")
    print(f"Output path: {OUTPUT_PATH}")


def main() -> int:
    try:
        source_payload = load_scenario_results()
        output_payload = summarise_pathways(source_payload)
        write_output(output_payload)
        print_summary(output_payload)
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: {exc}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
