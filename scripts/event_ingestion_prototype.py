#!/usr/bin/env python3
"""Prototype a future event-ingestion workflow without scraping or APIs."""

from __future__ import annotations

import json
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_PATH = PROJECT_ROOT / "results" / "event_ingestion_candidates.json"


RAW_EVENT_ITEMS = [
    {
        "event_title": "Prototype candidate: military exercise affecting a strategic technology supply route",
        "event_date": "TBD",
        "source_name": "Manual prototype placeholder",
        "source_url": "not_applicable_prototype",
        "raw_summary": (
            "Synthetic example used to demonstrate how a future collection process could capture "
            "a military-exercise candidate before human source review."
        ),
    },
    {
        "event_title": "Prototype candidate: export restriction on advanced technology equipment",
        "event_date": "TBD",
        "source_name": "Manual prototype placeholder",
        "source_url": "not_applicable_prototype",
        "raw_summary": (
            "Synthetic example used to demonstrate how a future workflow could route an export "
            "restriction candidate into review without treating it as verified data."
        ),
    },
    {
        "event_title": "Prototype candidate: public investment in strategic semiconductor capacity",
        "event_date": "TBD",
        "source_name": "Manual prototype placeholder",
        "source_url": "not_applicable_prototype",
        "raw_summary": (
            "Synthetic example used to demonstrate how a future workflow could identify a strategic "
            "investment candidate for human coding."
        ),
    },
]


def assign_event_family(raw_item: dict[str, str]) -> str:
    text = f"{raw_item['event_title']} {raw_item['raw_summary']}".lower()
    if "military exercise" in text:
        return "Military Exercise"
    if "export restriction" in text:
        return "Export Restriction"
    if "investment" in text:
        return "Strategic Investment"
    return "TBD"


def transform_raw_items(raw_items: list[dict[str, str]]) -> list[dict[str, str]]:
    candidates: list[dict[str, str]] = []
    for index, raw_item in enumerate(raw_items, start=1):
        candidates.append({
            "candidate_id": f"CAND{index:03d}",
            "event_title": raw_item["event_title"],
            "event_date": raw_item["event_date"],
            "source_name": raw_item["source_name"],
            "source_url": raw_item["source_url"],
            "raw_summary": raw_item["raw_summary"],
            "eligibility_status": "needs_human_review",
            "assigned_event_family": assign_event_family(raw_item),
            "reviewer_note": "Prototype candidate only; not verified and not approved for dataset integration.",
            "integration_status": "not_integrated",
        })
    return candidates


def build_payload() -> dict[str, object]:
    candidates = transform_raw_items(RAW_EVENT_ITEMS)
    return {
        "prototype_status": "manual_simulation_only",
        "disclaimer": (
            "These are synthetic workflow examples. They are not verified historical events, "
            "not scraped records, and not approved rows for data/historical_analogue_events.csv."
        ),
        "candidate_count": len(candidates),
        "candidates": candidates,
    }


def write_payload(payload: dict[str, object]) -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_PATH.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2)
        handle.write("\n")


def print_summary(payload: dict[str, object]) -> None:
    print("Event ingestion prototype")
    print(f"Prototype status: {payload['prototype_status']}")
    print(f"Candidate records generated: {payload['candidate_count']}")
    for candidate in payload["candidates"]:
        print(
            f"- {candidate['candidate_id']}: {candidate['assigned_event_family']} | "
            f"{candidate['integration_status']} | {candidate['event_title']}"
        )
    print(f"Output path: {OUTPUT_PATH}")


def main() -> int:
    try:
        payload = build_payload()
        write_payload(payload)
        print_summary(payload)
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: {exc}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
