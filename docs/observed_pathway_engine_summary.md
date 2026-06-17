# Observed Pathway Engine Summary

## What Changed

Sprint 4 adds an observed pathway engine that summarizes the historical pathways represented in the scenario query demo results.

New files:

- `scripts/generate_observed_pathways.py`
- `results/observed_pathways.json`
- `docs/observed_pathway_engine_methodology.md`
- `docs/observed_pathway_engine_summary.md`

`README.md` now links to the observed pathway engine and output.

## Pathway Summaries

| Scenario question | Observed pathway summary |
|---|---|
| What if China announces another large-scale military exercise near Taiwan? | `Restriction pressure pathway`: 3 analogs, represented by E003, E002, and E005 |
| What if the U.S. expands semiconductor export restrictions? | `Restriction pressure pathway`: 3 analogs, represented by E003, E002, and E005 |
| What if Taiwan announces new state support for strategic semiconductor firms? | `Named support pathway`: 2 analogs, represented by E007 and E011; `Named support/downside-offset pathway`: 1 analog, represented by E009 |

## What This Adds Beyond Similarity Scoring

The similarity engine identifies close event analogs. The scenario query demo retrieves those analogs for example questions. The observed pathway engine adds an interpretation layer by grouping the retrieved analogs into qualitative historical patterns.

This helps answer: when similar events are retrieved, are they mostly pressure cases, support cases, or mixed support/downside-offset cases?

## Limitations

This sprint remains descriptive. It does not assign probabilities, estimate market effects, or provide investment guidance. The current pathway summaries are based on only three analogs per scenario, so counts should be treated as scenario evidence rather than statistical results.

The preserved evidence notes remain important because events within the same pathway can differ in timing, market relevance, and identification quality.

## Next Step

A useful next sprint would add validation for `results/observed_pathways.json`, including required-key checks, pathway-count checks, and confirmation that every pathway summary includes representative events, evidence notes, analyst notes, and limitation notes.
