# Research Quality Framework

## Purpose

The research quality framework defines the standards used to keep the historical analogue, scenario, observed pathway, and analyst brief systems academically defensible.

## Completeness

Completeness means the dataset contains the required fields and enough contextual coding to support comparison.

Quality checks:

- required columns are present;
- `event_id` values are populated and unique;
- event dates are recorded;
- `evidence_note` fields explain the source basis;
- missing or uncertain values are marked as `TBD` or `Not coded`.

Completeness does not mean every possible event has been collected.

## Consistency

Consistency means similar events are coded using the same rules.

Quality checks:

- event family follows `docs/event_family_taxonomy_v2.md`;
- support and pressure signals are separated;
- surprise levels are applied conservatively;
- pathway names are reused rather than casually invented;
- British English style is maintained in documentation and user-facing text.

## Transparency

Transparency means users can see how the evidence was selected and processed.

Quality checks:

- methodology documents describe assumptions;
- output files list source inputs;
- scripts are deterministic;
- caveats are visible in dashboard and analyst brief outputs;
- limitations are stated without qualification drift.

## Traceability

Traceability means every analytic output can be linked back to coded event evidence.

Quality checks:

- analyst briefs preserve scenario IDs and event IDs;
- pathway summaries preserve representative events;
- evidence notes remain attached to event IDs;
- candidate events remain separate from approved events until reviewed.

## Reproducibility

Reproducibility means another user can regenerate core outputs from repository files.

Quality checks:

- scripts use repository-relative paths;
- generated outputs are written to `results/`;
- `scripts/run_all_checks.py` runs the core deterministic pipeline;
- `scripts/pipeline_orchestrator.py` runs the broader intelligence workflow;
- dashboard data loads from static JSON files.

## Research Boundaries

The system supports historical evidence synthesis. It does not claim causal proof beyond the research design, forecast future events, estimate expected returns, assign probabilities, or provide investment advice.
