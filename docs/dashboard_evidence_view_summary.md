# Dashboard Evidence View Summary

## What the Dashboard Shows

Sprint 5 adds a static dashboard evidence view under `dashboard/`. The page displays:

- the dissertation theory chain;
- scenario query demo questions;
- top historical analogs;
- similarity scores;
- observed pathways;
- evidence notes;
- limitations and not-investment-advice language.

The dashboard reads from:

- `results/scenario_query_demo_results.json`
- `results/observed_pathways.json`

## Connection to Decision-Support Analytics

The dashboard connects the dissertation research base to decision-support analytics by making the evidence chain easier to inspect. It shows how scenario questions map to historical analogs and how those analogs group into observed pathways.

This remains a research and portfolio artifact. The dashboard organizes evidence; it does not generate forecasts, probabilities, or investment recommendations.

## What It Does Not Do

The dashboard does not use external JavaScript libraries, LLM API calls, market-data APIs, or a build step. It does not estimate expected returns, recommend trades, or claim forecast accuracy.

Similarity scores and pathway counts are descriptive summaries of coded historical evidence.

## How to Run Locally

From the repository root, run:

```bash
python3 -m http.server 8000
```

Then open:

```text
http://127.0.0.1:8000/dashboard/
```

If the JSON files are missing or the page is opened without a local server, the dashboard shows a clear evidence-file loading message.
