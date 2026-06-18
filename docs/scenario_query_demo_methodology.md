# Scenario Query Demo Methodology

## Purpose

The scenario query demo shows how the historical analogue dataset and similarity logic can answer example scenario questions through deterministic historical retrieval. It is a portfolio demonstration of structured analogue reasoning, not a forecasting model.

The script uses three hard-coded questions and maps each one to a coded scenario profile. The profile is then compared against every event in `data/historical_analogue_events.csv`.

## Scenario Profile Coding

Each demo question is converted into the same feature fields used by the historical similarity engine:

- `event_family`
- `affected_sector`
- `strategic_importance_level`
- `state_support_signal`
- `restriction_or_pressure_signal`
- `surprise_level`
- `market_interpretation`
- `observed_market_pathway`

For example, a question about expanded U.S. semiconductor export restrictions is coded as an export-control pressure scenario with no direct state support, high strategic importance, moderate surprise, and a restriction-pressure pathway.

The coding is intentionally simple and visible in `scripts/run_scenario_query_demo.py`. There are no hidden prompts, embeddings, API calls, or model-generated classifications.

## Retrieval Method

For each scenario, the script compares the coded profile against all historical events. Each compared field receives:

- `1.0` point for an exact match;
- `0.5` point for partial textual overlap;
- `0.0` points for no match or unavailable coding such as `TBD` or `Not coded`.

The final score is the total field score divided by the eight compared fields. The script returns the top three historical analogues for each scenario and includes:

- similarity score;
- matched fields;
- different fields;
- observed market pathway;
- evidence note from the historical analogue dataset.

## Connection to the Dissertation Theory

The dissertation theory asks when geopolitical competition is interpreted by markets as opportunity rather than only risk. The scenario demo keeps that distinction visible by separating support-oriented scenarios from pressure-oriented scenarios.

Support scenarios retrieve events where strategic importance is linked to state support. Pressure scenarios retrieve export-control, retaliation, or restriction cases. This supports theory-driven comparison without claiming that any future event will replicate a prior market reaction.

## Why This Is Not Prediction

The demo does not estimate probabilities, returns, causal effects, or investment outcomes. It only retrieves historically similar coded events. Similarity means that event features overlap, not that consequences will match.

The output is evidence-based because each analogue comes from the documented historical event dataset. It remains limited because the dataset is small, qualitative, and focused on semiconductor-related geopolitical and industrial-policy cases.

## Limitations

The current demo uses only three hard-coded questions. Scenario profiles are hand-coded and should be reviewed before use in any research setting. All fields are weighted equally, and partial textual overlap is a simple lexical rule rather than a substantive judgment.

The demo should be treated as a transparent proof of concept for analogue retrieval, not as a decision engine for policy, markets, or investment.
