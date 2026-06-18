# Dataset Validation Framework

## Purpose

The dataset validation framework defines how the repository checks data quality before historical analogue events are used in similarity scoring, scenario retrieval, observed pathway summaries, analyst briefs, or dashboard views.

## Completeness Checks

Required checks:

- all required columns exist;
- `event_id` is non-empty;
- `event_id` values are unique;
- required event metadata fields are populated or explicitly coded as `TBD` or `Not coded`;
- generated outputs exist after pipeline runs.

Current implementation:

- `scripts/validate_historical_analogue_dataset.py`
- `scripts/dataset_coverage_analysis.py`
- `scripts/run_all_checks.py`
- `scripts/pipeline_orchestrator.py`

## Consistency Checks

Required checks:

- event-family labels are consistent with the V2 taxonomy;
- pathway labels are reused consistently;
- dates use ISO format where possible;
- qualitative signal fields use conservative wording;
- coding does not introduce unsupported financial claims.

Future validation can add controlled vocabularies once the dataset is larger.

## Transparency Checks

Required checks:

- every row includes an `evidence_note`;
- outputs state their source files;
- methodology documents explain scoring and synthesis rules;
- dashboard and README disclaimers remain visible.

## Traceability Checks

Required checks:

- scenario outputs include retrieved event IDs;
- observed pathways include representative events;
- analyst briefs preserve event IDs, evidence notes, and limitations;
- coverage reports identify the source dataset.

## Reproducibility Checks

Core commands:

```bash
python3 scripts/validate_historical_analogue_dataset.py
python3 scripts/dataset_coverage_analysis.py
python3 scripts/run_all_checks.py
python3 scripts/pipeline_orchestrator.py
```

Expected generated outputs:

- `results/dataset_coverage_report.json`
- `results/dataset_coverage_summary.csv`
- `results/historical_similarity_matrix.csv`
- `results/scenario_query_demo_results.json`
- `results/observed_pathways.json`
- `results/analyst_briefs.json`
- `results/system_health_report.json`

## Review Standard

Validation can detect structural problems, but it cannot replace human review. Source quality, event relevance, and coding judgement must still be checked before new events enter the approved dataset.
