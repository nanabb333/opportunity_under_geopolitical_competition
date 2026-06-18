# Analyst Brief Methodology

## Purpose

The analyst brief system converts historical event evidence into a structured intelligence brief for scenario review. It is designed to make the evidence chain readable without adding forecasts, probability estimates, expected-return estimates, or investment advice.

## Inputs

The brief generator uses three repository artefacts:

- `data/historical_analogue_events.csv`
- `results/scenario_query_demo_results.json`
- `results/observed_pathways.json`

The historical analogue dataset provides approved event metadata and evidence notes. The scenario query output provides scenario profiles and retrieved analogues. The observed pathway output provides grouped pathway evidence for each scenario.

## Processing Logic

`scripts/generate_analyst_briefs.py` applies deterministic rules:

1. Load approved historical analogue events and index them by `event_id`.
2. Load scenario query results and preserve the retrieved top analogues.
3. Load observed pathway groupings for each scenario.
4. Enrich analogue records with approved event metadata where available.
5. Build a structured brief using fixed templates.
6. Write the output to `results/analyst_briefs.json`.

The script does not call an LLM, scrape websites, alter similarity scores, or create new factual claims beyond the coded evidence.

## Output Structure

Each brief contains:

- `brief_id`
- `scenario_title`
- `scenario_description`
- `most_relevant_historical_analogues`
- `observed_historical_pathways`
- `key_evidence`
- `analytical_caveats`
- `research_limitations`
- `analyst_note`

The output is intended for analyst-facing review. It keeps event IDs, evidence notes, and limitations visible so that users can trace each claim back to the source evidence.

## Limitations

The system is descriptive. It cannot prove causality, forecast outcomes, assign probabilities, or support investment recommendations. The current evidence base is limited and semiconductors-focused, so briefs should be treated as structured historical comparison rather than comprehensive geopolitical intelligence coverage.

## Future Improvements

Future work should focus on expanding the approved historical analogue dataset, strengthening source review, adding quality checks for brief completeness, and improving coverage across event families. Any future automation should preserve human review before candidate events enter the approved dataset.
