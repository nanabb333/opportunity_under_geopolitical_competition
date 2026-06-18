# Event Collection Protocol V2

## Purpose

This protocol defines how new events should be collected, screened, coded, reviewed, and documented before entering `data/historical_analogue_events.csv`.

## Source Requirements

Preferred sources:

- official government releases;
- regulatory notices;
- company announcements;
- securities filings;
- official agency statements;
- reputable wire services or major newspapers for same-day timing context.

Minimum standard:

- one reliable dated source establishing event existence and timing;
- one additional source when the event family, affected sector, or mechanism is ambiguous;
- source details recorded in the coding worksheet or batch notes.

Avoid:

- unsourced social media;
- opinion-only commentary;
- post-event market recap articles as the primary source;
- sources that do not identify the event date;
- retrospective narratives that blur what was knowable at the time.

## Eligibility Criteria

Include events only when they meet all criteria:

- identifiable public date;
- clear relevance to geopolitical competition, strategic sectors, industrial policy, sanctions, technology restrictions, military activity, diplomacy, elections, or supply-chain relocation;
- assignable dominant event family using `docs/event_family_taxonomy_v2.md`;
- sufficient evidence for a concise `evidence_note`;
- useful comparison value for historical analogue retrieval.

Exclude or defer events when:

- timing is unclear;
- source quality is weak;
- the event is selected only because the market reaction is known;
- the mechanism cannot be coded without speculation;
- the event duplicates an already coded case without adding comparison value.

## Coding Standards

Required coding fields should follow `data/historical_analogue_events.csv`.

Coding rules:

- preserve existing event IDs;
- assign stable new event IDs in sequence;
- code the dominant event family;
- separate state-support signals from restriction or pressure signals;
- use `TBD` or `Not coded` rather than unsupported precision;
- do not invent financial results;
- keep `market_interpretation` as a qualitative mechanism label;
- keep `observed_market_pathway` descriptive, not predictive.

## Review Requirements

Each proposed batch should pass human review before integration.

Review should check:

- source reliability;
- event-date accuracy;
- event-family assignment;
- support and pressure signal coding;
- surprise-level coding;
- pathway label consistency;
- evidence-note traceability;
- duplication risk.

Rejected events should remain outside the approved dataset. Deferred events should retain reviewer notes explaining what evidence is missing.

## Documentation Requirements

Each expansion batch should document:

- number of candidate events reviewed;
- number approved;
- number rejected or deferred;
- event families added;
- regions and sectors added;
- unresolved `TBD` fields;
- validation results;
- coverage changes.

After integration, regenerate:

```bash
python3 scripts/validate_historical_analogue_dataset.py
python3 scripts/dataset_coverage_analysis.py
python3 scripts/run_all_checks.py
```

## Research Boundary

This protocol supports descriptive historical comparison. It does not create forecasts, probability estimates, causal proof, or investment recommendations.
