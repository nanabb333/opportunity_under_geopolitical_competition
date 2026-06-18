# Event Coding Workflow

## Purpose

This workflow turns the event expansion protocol into a repeatable production process. It is designed for careful dataset growth, not rapid collection. The goal is to add historical analogue events in a way that preserves transparency, source quality, and reproducibility.

## Stage 1: Event Identification

Identify candidate geopolitical, industrial-policy, military, sanctions, technology, supply-chain, or election-related events from reliable sources.

Outputs:

- candidate event title;
- candidate event date;
- candidate source link or citation;
- short reason the event may belong in the historical analogue dataset.

Rules:

- Do not select events because a market move is already known.
- Prefer official or same-day sources.
- Keep candidates that are uncertain in a screening list rather than forcing inclusion.

## Stage 2: Eligibility Screening

Apply the inclusion and exclusion criteria from `docs/event_collection_protocol.md`.

Minimum eligibility requirements:

- identifiable public event date;
- geopolitical, strategic, industrial-policy, technology, military, sanctions, or supply-chain relevance;
- reliable dated source;
- enough information to assign a dominant event family;
- useful historical comparison value.

Screening outcomes:

- `include`;
- `defer`;
- `exclude`.

Document the reason for every deferred or excluded event.

## Stage 3: Event Family Assignment

Assign one dominant event family using `docs/event_family_taxonomy_v2.md`.

Required behaviour:

- choose the dominant public announcement mechanism;
- document secondary mechanisms in `evidence_note`;
- avoid overcoding ceremonial, rhetorical, or ambiguous events;
- use `TBD` where family assignment remains uncertain.

## Stage 4: Coding

Complete the fields in `docs/event_coding_template.md`.

Required fields:

- `event_id`
- `event_date`
- `event_title`
- `source`
- `event_family`
- `affected_sector`
- `strategic_importance_level`
- `state_support_signal`
- `restriction_or_pressure_signal`
- `surprise_level`
- `market_interpretation`
- `observed_market_pathway`
- `evidence_note`

Coding rules:

- code only what the source supports;
- separate support signals from pressure signals;
- do not invent financial outcomes;
- use `TBD` or `Not coded` when evidence is insufficient.

## Stage 5: Quality Review

Review each coded event before integration.

Checklist:

- source is dated and reliable;
- event date matches the public information release;
- event family follows the V2 taxonomy;
- support and pressure signals are not conflated;
- `evidence_note` explains the coding basis;
- no market outcome is inferred from narrative context;
- fields are complete or explicitly marked `TBD` / `Not coded`.

Recommended reviewer action:

- validate one event record with `scripts/validate_event_entry.py`;
- compare against adjacent existing events for consistency;
- record unresolved coding issues before integration.

## Stage 6: Dataset Integration

Integrate approved records into `data/historical_analogue_events.csv` in batches.

Integration rules:

- do not reuse event IDs;
- preserve existing dissertation-linked IDs;
- add events in a documented batch;
- avoid changing prior coding unless correcting a documented error;
- note any taxonomy updates before changing event-family names.

## Stage 7: Validation

Run validation after integration:

```bash
python3 scripts/validate_historical_analogue_dataset.py
python3 scripts/run_all_checks.py
```

Expected outputs:

- dataset structure passes;
- similarity matrix regenerates;
- scenario query demo regenerates;
- observed pathway summaries regenerate.

If validation fails, fix only the event row or documented schema issue that caused the failure.
