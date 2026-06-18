# Reproducibility Guide

## Python Version Assumption

Use Python 3.10 or newer. The deterministic historical analogue pipeline uses only the Python standard library.

The broader dissertation event-study script may require additional packages such as `pandas` and `yfinance`, depending on the local environment.

## Run Validation

From the repository root:

```bash
python3 scripts/validate_historical_analogue_dataset.py
```

Expected result:

- required columns are present;
- `event_id` values are non-empty and unique;
- missing value counts are reported;
- the script exits successfully if required structure is valid.

## Regenerate Historical Analogue Outputs

Run all deterministic historical analogue checks and outputs with:

```bash
python3 scripts/run_all_checks.py
```

This runs, in order:

1. `scripts/validate_historical_analogue_dataset.py`
2. `scripts/calculate_historical_similarity.py`
3. `scripts/run_scenario_query_demo.py`
4. `scripts/generate_observed_pathways.py`

The runner stops at the first failure and prints PASS/FAIL messages.

## Regenerate Outputs Manually

If you prefer to run each step separately:

```bash
python3 scripts/validate_historical_analogue_dataset.py
python3 scripts/calculate_historical_similarity.py
python3 scripts/run_scenario_query_demo.py
python3 scripts/generate_observed_pathways.py
```

## Launch Dashboard

From the repository root:

```bash
python3 -m http.server 8000
```

Then open:

```text
http://127.0.0.1:8000/dashboard/
```

The dashboard should load:

- `results/scenario_query_demo_results.json`
- `results/observed_pathways.json`

## Expected Output Files

After running the checks, expected outputs include:

- `results/historical_similarity_matrix.csv`
- `results/scenario_query_demo_results.json`
- `results/observed_pathways.json`

Existing dissertation event-study outputs include:

- `data/market_returns.csv`
- `data/event_firm_returns.csv`
- `data/local_price_validation_report.md`

## Troubleshooting Notes

- If `run_all_checks.py` fails at validation, inspect `data/historical_analogue_events.csv` for missing required columns, duplicate `event_id` values, or blank cells.
- If scenario or pathway generation fails, regenerate upstream outputs first by running `scripts/calculate_historical_similarity.py` and `scripts/run_scenario_query_demo.py`.
- If the dashboard does not load JSON files, make sure the HTTP server was started from the repository root, not from inside `dashboard/`.
- If port 8000 is already in use, run `python3 -m http.server 8001` and open `http://127.0.0.1:8001/dashboard/`.
- If the event-study pipeline fails, check whether local Python has the non-standard dependencies required by `scripts/build_event_returns.py`.
