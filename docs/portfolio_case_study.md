# Portfolio Case Study

## Project Overview

`opportunity_under_geopolitical_competition` is a dissertation research repository that examines when geopolitical competition can be interpreted by markets as opportunity for strategically important firms or sectors. The project begins with a focused event-study design and extends it into a historical analog research base with deterministic scenario-analysis tools.

The repository now shows a full value chain: theory, event data, return analysis, historical analog coding, similarity scoring, scenario query retrieval, observed pathway summaries, and a static dashboard evidence view.

## Problem

Geopolitical competition is often treated as a general risk factor. That framing can miss cases where states respond to strategic pressure with subsidies, loans, procurement, protection, financing, or industrial-policy commitments. In those cases, some firms may be exposed to support as well as pressure.

The project addresses this problem by distinguishing threat-dominant events from state-support events and by documenting how each case is coded before interpretation.

## Research Question

When do financial markets interpret geopolitical competition as a source of opportunity for strategically important firms or sectors?

## Theory Chain

```text
Geopolitical competition
  ↓
Strategic importance
  ↓
Expected state support
  ↓
Investor interpretation
  ↓
Market reaction
```

The theory does not claim that geopolitical competition is broadly positive. It expects heterogeneous effects: firms exposed mainly to restrictions or uncertainty may face pressure, while firms expected to receive credible support may be interpreted differently.

## Data Architecture

The project uses a layered data architecture:

- `data/events.csv`: dissertation event universe and event-level mechanism coding.
- `data/assets.csv`: firms, indices, ETFs, and benchmarks.
- `data/event_asset_links.csv`: pre-outcome event-to-asset links.
- `data/raw_prices/`: local price inputs for reproducible event-study calculations.
- `data/event_firm_returns.csv`: generated event-firm return outputs.
- `data/historical_analog_events.csv`: qualitative historical analog event layer.

The design keeps the dissertation event-study base intact while adding a structured analog layer for broader comparison.

## Analytical Pipeline

The core reproducible scripts are:

- `scripts/build_event_returns.py`: builds event-study return outputs.
- `scripts/validate_historical_analog_dataset.py`: validates the historical analog dataset.
- `scripts/calculate_historical_similarity.py`: generates pairwise historical event similarity scores.
- `scripts/run_scenario_query_demo.py`: maps demo questions to coded scenario profiles and retrieves top analogs.
- `scripts/generate_observed_pathways.py`: groups retrieved analogs into observed pathway summaries.

The pipeline is deterministic and local. It does not use LLM API calls.

## Historical Analog Engine

The historical analog layer extends the dissertation event universe into a qualitative event database. It compares events across coded fields such as event family, affected sector, state-support signal, pressure signal, surprise level, market interpretation, and observed pathway.

The similarity engine scores event pairs from 0 to 1 using exact and partial textual matches. The score is transparent and auditable; it is not a prediction.

## Scenario Query Demo

The scenario query demo asks three hard-coded questions and maps each question to a coded scenario profile. It then retrieves the top three similar historical events.

Example questions include:

- What if China announces another large-scale military exercise near Taiwan?
- What if the U.S. expands semiconductor export restrictions?
- What if Taiwan announces new state support for strategic semiconductor firms?

The output is `results/scenario_query_demo_results.json`.

## Dashboard Evidence View

The dashboard under `dashboard/` displays:

- scenario questions;
- top historical analogs;
- similarity scores;
- observed pathways;
- evidence notes;
- limitations and not-investment-advice language.

It is a static page with no external JavaScript dependencies and no build step.

## What This Demonstrates

This project demonstrates:

- theory-driven research design;
- event-study workflow discipline;
- data validation;
- reproducible local scripting;
- qualitative coding transparency;
- deterministic similarity scoring;
- scenario-oriented evidence retrieval;
- careful communication of limitations;
- lightweight dashboard presentation.

It is useful as a portfolio artifact because it connects academic research design with practical decision-support-style evidence organization.

## Limitations

The project is descriptive and mechanism-focused. It does not prove broad causal effects, does not claim forecast accuracy, and does not provide investment advice.

The historical analog dataset is small and semiconductors-focused. Several fields are qualitative, and some events are anticipated, bundled, implementation-focused, or conditional. Similarity scores should be treated as retrieval aids, not as statistical evidence.

## Future Extensions

Possible future work includes:

- adding validation for dashboard input JSON files;
- expanding the analog dataset with a documented event-screening log;
- adding researcher-defined feature weights with clear justification;
- adding tests for score bounds, required keys, and output row counts;
- building a controlled interactive query interface after the static dashboard foundation is stable.
