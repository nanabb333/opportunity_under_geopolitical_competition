# Evidence Synthesis Framework

## Purpose

The evidence synthesis layer converts structured scenario evidence into analyst briefs. It summarizes historical analogs, observed pathways, evidence notes, caveats, and research limitations.

This layer is descriptive. It does not forecast outcomes, assign probabilities, estimate returns, or provide investment advice.

## How Evidence Is Combined

Evidence is combined from the static scenario analysis output:

- scenario profile fields
- retrieved historical analogs
- similarity scores
- matched fields
- observed pathway summaries
- evidence notes
- limitations notes

`scripts/generate_analyst_brief.py` applies deterministic templates to these fields. No LLM API is used.

## How Analogs Are Selected

Analogs are selected before synthesis by `scripts/analyze_scenario_profile.py`. Each scenario profile is compared with the historical analog dataset across coded qualitative fields.

The brief generator does not change the scoring. It preserves the top analogs already retrieved and adds explanatory text about why they appear in the brief.

## How Pathway Evidence Is Summarized

Observed pathway evidence is summarized by grouping the top analogs by `observed_market_pathway`. The brief reports:

- pathway name
- count among top analogs
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
