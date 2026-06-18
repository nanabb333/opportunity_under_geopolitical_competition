# Historical Analogue Dataset Summary

## What Changed

This sprint adds a focused historical-analogue dataset layer to the repository. It does not redesign the dissertation project, remove the event-study framing, or change the validated dissertation results.

New files:

- `data/historical_analogue_events.csv`
- `docs/historical_analogue_dataset_methodology.md`
- `docs/historical_analogue_dataset_summary.md`
- `scripts/validate_historical_analogue_dataset.py`

`README.md` now includes a short section linking to the historical analogue dataset and methodology.

## Event Count

The historical analogue layer currently includes 12 events. The rows are derived from the existing `data/events.csv` event universe so that the new layer remains tied to the dissertation's documented coding base.

## Fields Added

The new dataset uses one row per geopolitical or industrial-policy event and includes the following fields:

- `event_id`
- `event_date`
- `event_title`
- `event_family`
- `country_or_region`
- `affected_sector`
- `strategic_importance_level`
- `state_support_signal`
- `restriction_or_pressure_signal`
- `surprise_level`
- `market_interpretation`
- `observed_market_pathway`
- `linked_primary_case`
- `evidence_note`

These fields make the event universe easier to compare across support signals, pressure signals, surprise levels, and qualitative market pathways.

## Contribution to Decision-Support Analytics

The dissertation evidence base is intentionally narrow and focused on event-study validation. The historical analogue layer moves the repository one step toward decision-support analytics by creating a structured comparison table that can later support:

- filtering by event family;
- comparing support-dominant and pressure-dominant cases;
- identifying primary cases and analogue cases;
- documenting why an event is useful as a historical comparison;
- separating qualitative mechanism coding from measured financial outcomes.

This is only a foundation. It does not yet include a dashboard, scoring engine, predictive model, or investment framework.

## Limitations

The dataset is not a forecast tool and does not provide investment recommendations. It should not be used to claim that a future geopolitical event will produce a specific market reaction.

Several fields remain qualitative. `surprise_level`, `market_interpretation`, and `observed_market_pathway` are coded for research comparison, not statistical prediction. Some events are highly anticipated, broad, bundled, or implementation-focused, which limits their usefulness as clean shocks.

Future work should add a formal change log for any new events, preserve source notes, and distinguish pre-outcome coding from post-outcome interpretation.
