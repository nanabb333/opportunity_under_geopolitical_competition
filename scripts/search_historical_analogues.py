#!/usr/bin/env python3
"""Search approved historical analogue events from the command line."""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATASET = PROJECT_ROOT / "data" / "historical_analogue_events.csv"
OUTPUT_PATH = PROJECT_ROOT / "results" / "latest_search_results.json"

SEARCH_FIELDS = [
    "event_title",
    "event_family",
    "affected_sector",
    "country_or_region",
    "market_interpretation",
    "observed_market_pathway",
    "evidence_note",
]

OUTPUT_FIELDS = [
    "event_id",
    "event_date",
    "event_title",
    "event_family",
    "observed_market_pathway",
    "evidence_note",
]


def load_events() -> list[dict[str, str]]:
    if not DATASET.exists():
        raise FileNotFoundError(f"Dataset not found: {DATASET}")

    with DATASET.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        rows = list(reader)
        fieldnames = reader.fieldnames or []

    required = sorted(set(["event_id", "event_date", *SEARCH_FIELDS, *OUTPUT_FIELDS]))
    missing = [field for field in required if field not in fieldnames]
    if missing:
        raise ValueError(f"Dataset missing required fields: {', '.join(missing)}")
    return rows


def matching_fields(event: dict[str, str], terms: list[str]) -> list[str]:
    fields: list[str] = []
    for field in SEARCH_FIELDS:
        value = (event.get(field) or "").lower()
        if any(term in value for term in terms):
            fields.append(field)
    return fields


def search_events(events: list[dict[str, str]], query: str) -> list[dict[str, object]]:
    terms = [term for term in query.lower().split() if term]
    if not terms:
        return []

    results: list[dict[str, object]] = []
    for event in events:
        combined_text = " ".join((event.get(field) or "") for field in SEARCH_FIELDS).lower()
        if all(term in combined_text for term in terms):
            result = {field: event[field] for field in OUTPUT_FIELDS}
            result["matching_fields"] = matching_fields(event, terms)
            results.append(result)

    results.sort(key=lambda row: (str(row["event_date"]), str(row["event_id"])))
    return results


def write_results(query: str, results: list[dict[str, object]]) -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "query": query,
        "result_count": len(results),
        "source_dataset": str(DATASET.relative_to(PROJECT_ROOT)),
        "results": results,
    }
    with OUTPUT_PATH.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2)
        handle.write("\n")


def print_results(query: str, results: list[dict[str, object]]) -> None:
    print("Historical analogue search")
    print(f"Query: {query}")
    print(f"Matches: {len(results)}")
    if not results:
        print("No approved historical analogue events matched this query.")
        print(f"Output path: {OUTPUT_PATH}")
        return

    for result in results:
        print("")
        print(f"{result['event_id']} | {result['event_date']} | {result['event_title']}")
        print(f"Family: {result['event_family']}")
        print(f"Observed pathway: {result['observed_market_pathway']}")
        print(f"Evidence note: {result['evidence_note']}")
        print(f"Matching fields: {', '.join(result['matching_fields'])}")
    print(f"\nOutput path: {OUTPUT_PATH}")


def main() -> int:
    if len(sys.argv) < 2:
        print('Usage: python3 scripts/search_historical_analogues.py "search terms"')
        return 1

    query = " ".join(sys.argv[1:]).strip()
    try:
        events = load_events()
        results = search_events(events, query)
        write_results(query, results)
        print_results(query, results)
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: {exc}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
