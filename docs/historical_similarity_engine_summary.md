# Historical Similarity Engine Summary

## What the Script Produces

`scripts/calculate_historical_similarity.py` reads `data/historical_analog_events.csv` and produces `results/historical_similarity_matrix.csv`.

The output contains one ordered comparison for each source event against every other event. Each row includes:

- `source_event_id`
- `comparison_event_id`
- `similarity_score`
- `matched_fields`
- `different_fields`
- `interpretation_note`

## Event Pairs Generated

The current dataset contains 12 events. The engine generated 132 ordered event pairs, excluding self-comparisons.

## High-Similarity Examples

The highest-scoring examples from the current run were:

| Source | Comparison | Score | Interpretation |
|---|---:|---:|---|
| E002 | E003 | 0.8125 | Closely related export-control pressure cases with shared restriction and pathway coding |
| E003 | E002 | 0.8125 | Reverse ordered comparison of the same high-similarity pair |
| E002 | E006 | 0.7500 | Threat-dominant pressure cases with shared support absence and restriction-pathway logic |
| E004 | E006 | 0.7500 | Restriction and retaliation cases linked by pressure, memory-chip relevance, and substitution/threat logic |
| E007 | E009 | 0.7500 | Direct state-support cases with overlapping named-support and strategic-importance coding |
| E009 | E012 | 0.7500 | Primary direct state-support cases for named semiconductor beneficiaries |

These examples should be treated as research prompts, not proof that the events had the same market effect.

## Analytical Contribution

Sprint 1 created a structured historical analog dataset. Sprint 2 turns that dataset into a simple analytical engine by calculating reproducible event-to-event similarity scores.

This advances the repository from a static historical comparison table toward decision-support analytics while preserving academic guardrails. The engine helps identify analog candidates, organize support-versus-pressure comparisons, and document why a pair of events appears similar.

## Limitations and Next Step

The current engine is intentionally simple. It uses equal field weights and phrase-level textual overlap. It does not use financial outcomes, causal estimates, forecasts, or investment signals.

The next step should be a small validation layer for the similarity output, such as checking expected row counts, score bounds, unique ordered pairs, and required output columns. A later sprint could add researcher-defined feature weights, but only with clear documentation and without converting the tool into a forecasting model.
