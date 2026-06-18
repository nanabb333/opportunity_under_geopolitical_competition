# Automation and Search Foundation Summary

## What Was Added

This sprint adds the foundation for a more scalable analytics system without claiming full automation.

New artefacts:

- `scripts/event_ingestion_prototype.py`
- `results/event_ingestion_candidates.json`
- `data/candidate_events_template.csv`
- `docs/candidate_event_review_workflow.md`
- `scripts/search_historical_analogues.py`
- `results/latest_search_results.json`

Dashboard upgrades:

- Dataset Coverage Summary section.
- System Workflow section.
- Graceful fallback behaviour for missing coverage data.

## Event Ingestion Prototype

`scripts/event_ingestion_prototype.py` defines a small set of manually written prototype raw items inside the script. It transforms those raw items into standardised candidate records and writes `results/event_ingestion_candidates.json`.

The output is explicitly marked as prototype-only. It is not scraped, not API-generated, not verified historical data, and not approved for integration into `data/historical_analogue_events.csv`.

## Candidate Review Workflow

`docs/candidate_event_review_workflow.md` explains how raw candidates should move through human review:

1. collect raw candidates;
2. screen eligibility;
3. assign event family;
4. code required fields;
5. approve, defer, or reject;
6. integrate approved rows only;
7. validate and regenerate downstream outputs.

Human review remains required because source quality, duplicate detection, and event-family assignment require judgment.

## Historical Analogue Search

`scripts/search_historical_analogues.py` is a command-line search tool for approved events in `data/historical_analogue_events.csv`.

Example:

```bash
python3 scripts/search_historical_analogues.py "export restriction"
```

The search runs across event title, family, sector, geography, market interpretation, observed pathway, and evidence note. It writes the latest search result to `results/latest_search_results.json`.

## Dashboard Upgrade

The dashboard now loads `results/dataset_coverage_report.json` when available and displays:

- event family coverage;
- sector coverage;
- geography coverage.

It also displays the system workflow:

```text
Event Ingestion Candidates
  ↓
Human Review
  ↓
Historical Analogue Dataset
  ↓
Similarity Engine
  ↓
Scenario Query
  ↓
Observed Pathways
  ↓
Dashboard Evidence View
```

If coverage data is missing, the dashboard shows a clear fallback message rather than failing.

## What Remains Manual

The following steps remain manual by design:

- source verification;
- event eligibility decisions;
- event-family assignment review;
- coding of support and pressure signals;
- approval or rejection of candidate rows;
- integration into the approved dataset.

## Future Extensions

Future work could add:

- source watchlists;
- candidate deduplication;
- batch candidate validation;
- review status reports;
- dashboard display of candidate queues;
- stronger tests for search and coverage outputs.

Any future automation should preserve the separation between unverified candidates and approved historical analogue events.
