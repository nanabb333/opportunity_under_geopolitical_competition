# Scenario Query Demo Summary

## Demo Questions

Sprint 3 adds a deterministic scenario query demo with three hard-coded questions:

1. What if China announces another large-scale military exercise near Taiwan?
2. What if the U.S. expands semiconductor export restrictions?
3. What if Taiwan announces new state support for strategic semiconductor firms?

The demo output is written to `results/scenario_query_demo_results.json`.

## Top Analogues Returned

| Scenario | Top analogues |
|---|---|
| China announces another large-scale military exercise near Taiwan | E003 at 0.8125; E002 at 0.6875; E005 at 0.6875 |
| U.S. expands semiconductor export restrictions | E003 at 0.9375; E002 at 0.8125; E005 at 0.6875 |
| Taiwan announces new state support for strategic semiconductor firms | E009 at 0.8750; E007 at 0.7500; E011 at 0.7500 |

The first two scenarios retrieve restriction-pressure pathways. The third scenario retrieves named state-support pathways.

## What This Demonstrates

The demo shows how the repository can move from a static historical analogue dataset to a simple queryable research artefact. A user can ask a predefined scenario question, the script maps it to a coded profile, and the system retrieves similar historical events with documented evidence notes.

This is useful as a portfolio-friendly example of decision-support analytics because the logic is transparent, deterministic, and tied to the dissertation's theory of state support under geopolitical competition.

## Limitations

The scenario demo is not a forecasting model and does not provide investment advice. It does not claim that similar events will produce similar financial outcomes. The current version uses only three predefined questions and a small historical event base.

Scores should be read as retrieval aids, not as evidence of causal similarity or market prediction.

## Next Step

A useful next sprint would add a validation script for `results/scenario_query_demo_results.json`, checking that each scenario returns three analogues, scores remain between 0 and 1, required fields are present, and the disclaimer is included.
