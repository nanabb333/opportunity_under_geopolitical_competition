# Interactive Scenario Assistant v1 Methodology

## Purpose

The interactive scenario assistant extends the historical analogue research layer into a simple decision-support demonstration. It allows a user to select a predefined geopolitical or industrial-policy scenario and retrieve similar historical analogues from the coded evidence base.

The assistant is deterministic and static. It does not call an LLM API, scrape websites, estimate returns, assign probabilities, or make investment recommendations.

## Scenario Profiles

Scenario profiles are stored in `data/sample_scenario_profiles.csv`. Each row describes a hypothetical scenario using the same qualitative coding language used by the historical analogue dataset where possible.

The scenario profile fields are:

- `scenario_id`
- `scenario_question`
- `event_family`
- `affected_sector`
- `country_or_region`
- `strategic_importance_level`
- `state_support_signal`
- `restriction_or_pressure_signal`
- `surprise_level`
- `analyst_note`

The scenario rows are not approved historical events. They are coded comparison inputs used to retrieve historical analogues.

## Historical Analogue Retrieval

`scripts/analyse_scenario_profile.py` compares each scenario profile with every row in `data/historical_analogue_events.csv`.

The comparison uses these fields:

- `event_family`
- `affected_sector`
- `country_or_region`
- `strategic_importance_level`
- `state_support_signal`
- `restriction_or_pressure_signal`
- `surprise_level`

Scoring is intentionally simple:

- Exact match: `1.0`
- Partial textual overlap: `0.5`
- No match, `TBD`, or `Not coded`: `0.0`

The final similarity score is the total score divided by the number of comparable fields. Each scenario returns the top five historical analogues.

## Observed Pathway Summary

For each scenario, the assistant groups the top analogues by `observed_market_pathway`. The pathway summary reports:

- pathway name
- count among the top analogues
- representative event IDs

This turns retrieved analogues into a compact description of observed historical patterns in the current evidence base.

## Connection to the Dissertation Theory

The dissertation theory chain links geopolitical competition, strategic importance, expected state support, investor interpretation, and market reaction. The assistant operationalises that chain as a structured comparison tool:

- scenarios encode geopolitical or industrial-policy pressure/support conditions
- historical analogues provide coded evidence from prior events
- observed pathways summarise how similar cases were interpreted in the dataset

The assistant is therefore an applied layer on top of the dissertation evidence, not a replacement for the research design.

## What It Can Support

The assistant can support:

- transparent scenario comparison
- retrieval of historically similar coded events
- evidence-based discussion of observed pathways
- portfolio demonstration of deterministic analytics

## What It Cannot Support

The assistant cannot support:

- forecast accuracy claims
- probability estimates
- expected-return estimates
- trading or investment recommendations
- causal proof beyond the limitations of the underlying research design

The output should be read as descriptive historical evidence, not a prediction.
