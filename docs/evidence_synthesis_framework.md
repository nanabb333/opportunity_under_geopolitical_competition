# Evidence Synthesis Framework

## Purpose

The evidence synthesis layer converts structured scenario evidence into analyst briefs. It summarises historical analogues, observed pathways, evidence notes, caveats, and research limitations.

This layer is descriptive. It does not forecast outcomes, assign probabilities, estimate returns, or provide investment advice.

## How Evidence Is Combined

Evidence is combined from the static scenario analysis output:

- scenario profile fields
- retrieved historical analogues
- similarity scores
- matched fields
- observed pathway summaries
- evidence notes
- limitations notes

`scripts/generate_analyst_briefs.py` applies deterministic templates to these fields. No LLM API is used.

## How Analogues Are Selected

Analogues are selected before synthesis by `scripts/analyse_scenario_profile.py`. Each scenario profile is compared with the historical analogue dataset across coded qualitative fields.

The brief generator does not change the scoring. It preserves the top analogues already retrieved and adds explanatory text about why they appear in the brief.

## How Pathway Evidence Is Summarised

Observed pathway evidence is summarised by grouping the top analogues by `observed_market_pathway`. The brief reports:

- pathway name
- count among top analogues
- representative event IDs
- a short deterministic summary note

Pathway counts describe the retrieved evidence base. They are not probability estimates.

## How Uncertainty Is Communicated

Uncertainty is communicated through:

- explicit analytical caveats
- research limitations
- evidence notes attached to specific event IDs
- wording that distinguishes historical pattern from prediction
- preservation of `TBD` or `Not coded` values when evidence is incomplete

The synthesis layer should not smooth over uncertainty. If the evidence base is limited, that limitation remains visible in the brief.

## Traceability

Every brief links back to:

- the scenario ID
- historical event IDs
- similarity scores
- matched fields
- evidence notes

This makes the brief auditable and keeps the analyst output connected to the coded evidence base.

## Why This Is Not Prediction

The synthesis layer reports what the current historical evidence base contains. It does not estimate future event likelihood, assign scenario probabilities, or claim that a pathway will recur. Similarity scores are qualitative matching summaries, not predictive confidence scores.

## Why This Is Not Investment Advice

The briefs are designed for research and portfolio communication. They do not recommend trades, securities, allocations, or timing decisions. Evidence notes and pathway summaries should be read as historical context for scenario assessment.
