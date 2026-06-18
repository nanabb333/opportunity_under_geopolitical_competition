# Repository Quality Audit

Audit date: 2026-06-17

## README Clarity

- PASS: `README.md` explains the dissertation framing, research question, theory chain, validated results, historical analogue layer, similarity engine, scenario query demo, observed pathway engine, dashboard view, and portfolio value chain.
- PASS: The README links to portfolio-facing documents, technical architecture, project limitations, data files, scripts, results, and dashboard files.
- WARNING: The README is now comprehensive and long. This is acceptable for a portfolio repository, but future changes should preserve scannability.

## Data Availability

- PASS: Core dissertation inputs are present under `data/`: `events.csv`, `assets.csv`, `event_asset_links.csv`, and raw local price files.
- PASS: Historical analogue input is present at `data/historical_analogue_events.csv`.
- PASS: Generated event-study outputs are present: `data/market_returns.csv`, `data/event_firm_returns.csv`, and `data/local_price_validation_report.md`.
- WARNING: `data/first_results_memo.md` is present but appears untracked in the current working tree. Decide whether it should be committed as a generated research artefact.

## Script Reproducibility

- PASS: The historical analogue validation, similarity, scenario query, and observed pathway scripts run locally with repository-relative paths.
- PASS: `scripts/run_all_checks.py` provides a single release-readiness command for the deterministic historical analogue pipeline.
- WARNING: `scripts/build_event_returns.py` uses additional dependencies such as `pandas` and `yfinance`; this audit did not add dependency management.
- WARNING: Citation-editing scripts are present as untracked files and appear outside the historical analogue release path.

## Results Availability

- PASS: `results/historical_similarity_matrix.csv` is present.
- PASS: `results/scenario_query_demo_results.json` is present.
- PASS: `results/observed_pathways.json` is present.
- PASS: Results regenerate from local scripts without external API calls.

## Dashboard Run Instructions

- PASS: Dashboard files are present under `dashboard/`: `index.html`, `styles.css`, and `app.js`.
- PASS: README and `docs/dashboard_evidence_view_summary.md` explain how to run the dashboard with `python3 -m http.server 8000`.
- PASS: Dashboard JavaScript includes graceful evidence-file loading messages for missing or unreadable JSON files.

## Documentation Completeness

- PASS: Methodology and summary documents exist for the historical analogue dataset, similarity engine, scenario query demo, observed pathway engine, and dashboard evidence view.
- PASS: Portfolio packaging documents exist: `portfolio_case_study.md`, `recruiter_summary.md`, `technical_architecture.md`, and `project_limitations.md`.
- PASS: Research design freeze documents remain available under `docs/`.

## Limitations / Disclaimers

- PASS: README, methodology documents, scenario outputs, observed pathway outputs, dashboard copy, and project limitations clearly state that the repository does not provide forecasts or investment advice.
- PASS: The project states that findings are descriptive and mechanism-focused, not broad causal proof.
- PASS: Qualitative coding, limited sample size, anticipation, bundling, and market-data limits are documented.

## Repo Hygiene

- PASS: Core project directories are organised: `data/`, `scripts/`, `results/`, `docs/`, `dashboard/`, and `dissertation_results/`.
- WARNING: There is no top-level `figures/` directory; figures are stored under `dissertation_results/figures/`.
- WARNING: Several manuscript/citation artefacts and helper scripts are currently untracked. They should be committed intentionally, ignored, or moved out of the release branch before a final public portfolio release.
- PASS: No dashboard build artefacts or external JavaScript dependencies were introduced.

## Overall Status

PASS with warnings. The repository is portfolio-ready for the historical analogue research workflow, provided the current untracked artefacts are handled intentionally before final release.
