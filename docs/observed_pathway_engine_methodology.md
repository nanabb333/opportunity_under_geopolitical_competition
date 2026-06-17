# Observed Pathway Engine Methodology

## Purpose

The observed pathway engine turns retrieved historical analogs into a concise summary of what type of pathway those analogs represent. It builds on the scenario query demo by asking a narrower question:

> Among the closest historical analogs for this scenario, which observed pathways appear most often?

This makes the scenario evidence easier to interpret without adding a dashboard, model, or external data dependency.

## What an Observed Pathway Is

An observed pathway is the qualitative post-event mechanism label already coded in `data/historical_analog_events.csv` and carried through the scenario query output. Examples include:

- `Restriction pressure pathway`
- `Named support pathway`
- `Named support/downside-offset pathway`

The pathway describes how the historical event is useful for interpretation. It is not a measured financial outcome and does not imply that a future case will follow the same route.

## Grouping Method

`scripts/generate_observed_pathways.py` reads `results/scenario_query_demo_results.json`. For each demo scenario, it:

1. reads the top historical analogs returned by the scenario query demo;
2. groups those analogs by `observed_market_pathway`;
3. counts how many analogs fall into each pathway;
4. records representative event IDs;
5. preserves the historical evidence notes;
6. adds a cautious analyst note using fixed deterministic language.

The output is written to `results/observed_pathways.json`.

## Connection to Investor Interpretation and Market Reaction

The dissertation theory distinguishes between geopolitical pressure and state-backed opportunity. The observed pathway engine keeps that distinction visible:

- pressure-oriented scenarios should retrieve analogs tied to restriction, access-loss, or compliance-burden channels;
- support-oriented scenarios should retrieve analogs tied to named state support, capacity support, or downside-offset logic.

This helps connect scenario evidence to the dissertation's mechanism of investor interpretation without turning the result into a market claim.

## Why This Is Descriptive

The engine only summarizes the pathways of historical analogs already returned by the scenario demo. It does not assign probabilities, estimate market effects, or recommend trades. A pathway count means that retrieved historical analogs share a qualitative interpretation label.

The output should be read as structured historical pattern evidence, not as a statement about what will happen in any future case.

## Limitations

The engine depends on the quality of the scenario query output and the original pathway coding. The current demo has only three scenarios and three analogs per scenario. Pathway counts are therefore small and should not be treated as statistical evidence.

Some pathways may combine events with different timing quality, beneficiary visibility, or market relevance. The preserved evidence notes should be read alongside every pathway summary.
