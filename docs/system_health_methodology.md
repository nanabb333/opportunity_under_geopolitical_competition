# System Health Methodology

## Purpose

`scripts/system_health_report.py` creates `results/system_health_report.json`, a local operations summary for the intelligence pipeline.

The report is designed for reproducibility and operational monitoring. It does not forecast events, estimate returns, or provide investment advice.

## Included Checks

The health report includes:

- dataset status
- review queue status
- coverage status
- validation status
- dashboard status

## Dataset Status

Dataset status reports whether `data/historical_analogue_events.csv` exists, how many approved rows it contains, and the latest update date recorded in `data/dataset_change_log.csv`.

## Queue Status

Queue status reports whether `data/event_review_queue.csv` exists and counts:

- total queue size
- reviewed events
- pending events

The queue may be empty. An empty queue is acceptable when no candidate events are under review.

## Coverage Status

Coverage status checks whether `results/dataset_coverage_report.json` exists and whether its dataset size matches the current historical analogue dataset size.

If coverage is stale or missing, the report returns a warning rather than inventing a coverage result.

## Validation Status

Validation status runs:

```bash
python3 scripts/validate_historical_analogue_dataset.py
```

The health report records the return code and final validation message.

## Dashboard Status

Dashboard status checks for required static dashboard files and key generated result files. It does not perform browser rendering or visual QA.

## Status Logic

- `PASS`: required files exist and checks are current.
- `WARNING`: a noncritical output is missing or stale.
- `FAIL`: a required validation or critical dataset check failed.

The report is intentionally conservative. It describes operational readiness, not analytical certainty.
