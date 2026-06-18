# Intelligence System Architecture

## Purpose

This document defines the foundation for a continuously updated geopolitical intelligence system built on the existing dissertation research base. The system is designed to collect candidate information, review and code event records, update the historical analog dataset, and regenerate deterministic analytics.

It does not automate source collection yet. It does not forecast outcomes, estimate returns, or provide investment advice.

## System Flow

```text
Raw Information Sources
        |
        v
Candidate Events
        |
        v
Human Review
        |
        v
Historical Analog Dataset
        |
        v
Similarity Engine
        |
        v
Scenario Analysis
        |
        v
Observed Pathways
        |
        v
Dashboard
```

## Data Flow

1. Raw information sources are monitored for geopolitical, industrial-policy, military, and supply-chain developments.
2. Potentially relevant items are recorded as candidate events, not approved events.
3. Analysts screen candidates against the event collection protocol and event family taxonomy.
4. Approved events are coded into `data/historical_analog_events.csv`.
5. Validation checks confirm required fields, non-empty event IDs, uniqueness, and missing-value status.
6. Similarity, scenario, pathway, and coverage scripts regenerate analytical outputs.
7. The static dashboard reads generated JSON and CSV outputs.

## Validation Flow

Validation occurs at four checkpoints:

- Candidate record completeness before review.
- Event coding completeness before dataset integration.
- Dataset validation after integration.
- Output regeneration after the dataset changes.

The core validation command remains:

```bash
python3 scripts/run_all_checks.py
```

New event entries should also be checked with:

```bash
python3 scripts/validate_event_entry.py path/to/event_record.json
```

## Update Cycle

### Weekly

- Review source registry priorities.
- Record candidate events.
- Screen candidates for eligibility.
- Code high-priority candidates that have sufficient source support.
- Run validation after any dataset update.

### Monthly

- Review event-family coverage.
- Update evidence gap assessment.
- Check whether scenario outputs are overly dependent on a small number of analogs.
- Confirm dashboard outputs still reflect the current generated files.

### Quarterly

- Audit source reliability assumptions.
- Review coding consistency across event families.
- Reassess taxonomy gaps.
- Freeze a dated dataset release if the evidence base has materially changed.

## Human Review Checkpoints

Human review remains required before any candidate becomes an approved historical event. Reviewers should verify:

- source reliability
- event date and title
- event family assignment
- affected sector
- support and pressure signals
- surprise level
- observed pathway coding
- evidence note quality
- distinction between event evidence and interpretation

The system is scalable because candidate discovery, coding, validation, and analytics are separated. It is academically conservative because no candidate enters the approved dataset without review.
