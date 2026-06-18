# Analyst Workbench Guide

## Purpose

This guide describes how an analyst should operate the repository as a geopolitical intelligence workbench. The workflow keeps candidate discovery, event coding, validation, analytics, and dashboard publication separate.

## 1. Identify Events

Review source categories in `data/source_registry.csv` and monitoring priorities in `docs/event_monitoring_framework.md`. Record potentially relevant developments as candidate events only.

Candidate events should include:

- event title
- event date
- source name
- source URL if available
- raw summary
- initial reviewer note

## 2. Review Sources

Prefer primary or official sources when available. Use reputable press, trade press, and analytical reports for discovery and context, but corroborate major claims before dataset integration.

Check whether the event has:

- a clear date
- an identifiable actor
- a relevant strategic sector
- a state support or pressure signal
- enough documentation for transparent coding

## 3. Code Events

Use `docs/event_family_taxonomy_v2.md` and `docs/event_coding_template.md`.

Code conservatively:

- use `TBD` or `Not coded` when evidence is insufficient
- avoid false precision
- distinguish source evidence from analyst interpretation
- preserve uncertainty in the evidence note

## 4. Validate Entries

Before adding an event to the approved dataset, validate the candidate record:

```bash
python3 scripts/validate_event_entry.py path/to/event_record.json
```

After adding approved rows to `data/historical_analog_events.csv`, validate the dataset:

```bash
python3 scripts/validate_historical_analog_dataset.py
```

## 5. Update Dataset

Only approved events should enter `data/historical_analog_events.csv`. Candidate events should remain separate until they pass review.

When integrating a row:

- assign a stable event ID
- preserve source-grounded evidence notes
- avoid changing historical rows unless correcting documented errors
- record unresolved coding uncertainty explicitly

## 6. Rerun Analytics

After dataset updates, regenerate outputs:

```bash
python3 scripts/run_all_checks.py
python3 scripts/analyze_scenario_profile.py
python3 scripts/dataset_coverage_analysis.py
```

These commands refresh validation, similarity outputs, scenario outputs, observed pathways, and coverage analysis.

## 7. Publish Dashboard Updates

Launch the static dashboard locally:

```bash
python3 -m http.server 8000
```

Open:

```text
http://127.0.0.1:8000/dashboard/
```

Review whether the dashboard reflects the regenerated evidence files and whether limitations remain visible. The dashboard should communicate historical analogs, observed pathways, and evidence notes without implying prediction or investment advice.
