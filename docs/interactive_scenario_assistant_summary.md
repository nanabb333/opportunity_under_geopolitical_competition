# Interactive Scenario Assistant v1 Summary

## What Was Added

This sprint added a static interactive scenario assistant layer:

- `data/scenario_profiles_template.csv`
- `data/sample_scenario_profiles.csv`
- `scripts/analyze_scenario_profile.py`
- `results/interactive_scenario_analysis.json`
- dashboard support for selecting a predefined scenario

The assistant compares coded scenario profiles with the historical analog dataset and returns the top five historical analogs per scenario.

## Sample Scenarios

The sample scenario file includes five predefined scenario comparison profiles:

1. New Taiwan Strait military exercise
2. Expanded U.S. semiconductor export restriction
3. Taiwan semiconductor state support package
4. China industrial policy escalation
5. Supply-chain relocation announcement

These are not approved historical events. They are scenario comparison inputs.

## Dashboard Behavior

The dashboard now includes an `Interactive Scenario Assistant v1` section. Users can select a sample scenario from a dropdown and view:

- coded scenario profile
- top historical analogs
- similarity scores
- matched fields
- observed pathway summary
- evidence notes
- limitations note

The dashboard uses static JSON only. There is no backend, no API, and no LLM call.

## Limitations

The assistant is descriptive and evidence-based. It does not forecast market reactions, assign probabilities, estimate returns, or provide investment advice.

The evidence base remains limited. Similarity scores are sensitive to qualitative coding choices, the current sample size, and the available historical analog rows.

## Future Extensions

Future versions could add:

- more approved historical events
- more balanced event-family coverage
- user-authored local scenario profile files
- stronger coding review workflow for new scenarios
- richer pathway summaries after dataset expansion

These extensions should preserve the distinction between scenario inputs and approved historical event records.
