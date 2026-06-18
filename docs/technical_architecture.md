# Technical Architecture

## Architecture Diagram

```text
data/
  ↓
scripts/
  ↓
results/
  ↓
dashboard/
```

## Data Inputs

Core dissertation inputs:

- `data/events.csv`: event universe and mechanism coding.
- `data/assets.csv`: firms, ETFs, indices, and benchmark assets.
- `data/event_asset_links.csv`: pre-outcome event-to-asset relationships.
- `data/raw_prices/*.csv`: local price inputs for event-study calculations.

Historical analogue input:

- `data/historical_analogue_events.csv`: qualitative historical analogue event layer.

## Scripts

- `scripts/build_event_returns.py`: builds market-return and event-firm return outputs.
- `scripts/validate_historical_analogue_dataset.py`: checks required columns, unique event IDs, and missing values.
- `scripts/calculate_historical_similarity.py`: compares historical events pairwise and writes similarity scores.
- `scripts/run_scenario_query_demo.py`: evaluates hard-coded scenario questions against the analogue dataset.
- `scripts/generate_observed_pathways.py`: groups retrieved scenario analogues by observed pathway.
- `scripts/generate_dissertation_figures.py`: generates dissertation figure artefacts.

## Outputs

Event-study outputs:

- `data/market_returns.csv`
- `data/event_firm_returns.csv`
- `data/local_price_validation_report.md`
- `data/first_results_memo.md`

Historical analogue and scenario outputs:

- `results/historical_similarity_matrix.csv`
- `results/scenario_query_demo_results.json`
- `results/observed_pathways.json`

Documentation outputs:

- methodology and summary documents under `docs/`;
- portfolio-facing package documents under `docs/`.

## Dashboard Files

The dashboard is static and has no build step:

- `dashboard/index.html`
- `dashboard/styles.css`
- `dashboard/app.js`

It loads:

- `results/scenario_query_demo_results.json`
- `results/observed_pathways.json`

Run locally from the repository root:

```bash
python3 -m http.server 8000
```

Then open:

```text
http://127.0.0.1:8000/dashboard/
```

## Validation Flow

Run the current historical analogue and scenario checks in order:

```bash
python3 scripts/validate_historical_analogue_dataset.py
python3 scripts/calculate_historical_similarity.py
python3 scripts/run_scenario_query_demo.py
python3 scripts/generate_observed_pathways.py
```

Expected behaviour:

- the historical analogue dataset validates successfully;
- the similarity engine generates 132 ordered event pairs from 12 events;
- the scenario query demo evaluates 3 scenarios;
- the observed pathway engine summarises 3 scenario outputs.

## Design Constraints

The analytical layers are deterministic and local. They do not use LLM API calls, external JavaScript libraries, or a dashboard build system. The outputs are descriptive and evidence-oriented rather than predictive.
