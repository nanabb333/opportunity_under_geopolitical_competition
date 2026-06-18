# System Architecture

## Purpose

The Geopolitical Intelligence Automation System is designed as a structured intelligence operations platform. Its purpose is to move geopolitical information through a controlled workflow that preserves source traceability, human judgement, dataset quality, and decision-support clarity.

The system does not forecast geopolitical outcomes, estimate returns, or provide investment recommendations.

## Architecture Overview

```text
Information Sources
        |
        v
Candidate Event Queue
        |
        v
Human Review
        |
        v
Approved Intelligence Records
        |
        v
Historical Analogue Search
        |
        v
Evidence Synthesis
        |
        v
Analyst Brief
        |
        v
Dashboard
```

## Component Roles

### Information Sources

Information sources include official statements, regulatory notices, company disclosures, reputable reporting, specialist research, and other documented materials. Sources are recorded in `data/source_registry.csv`.

The source registry is not a scraping configuration. It is a controlled catalogue for future monitoring and review.

### Candidate Event Queue

Potentially relevant events enter `data/candidate_events.csv`. Candidate records are not approved intelligence. They require human review before entering the approved dataset.

### Human Review

Human review checks source reliability, event significance, date clarity, event-family fit, evidence quality, and uncertainty. The reviewer decides whether to approve, reject, or defer the candidate.

### Approved Intelligence Records

Approved records are stored in `data/approved_events.csv`. These records form the evidence base for historical analogue search and evidence synthesis.

### Historical Analogue Search

Historical analogue search compares a scenario or new event against approved intelligence records. The goal is structured comparison, not prediction.

### Evidence Synthesis

Evidence synthesis combines retrieved analogues, observed pathways, evidence notes, and caveats into a structured analyst-ready form.

### Analyst Brief

Analyst briefs are stored in `data/analyst_briefs.csv` or generated into `results/` in future phases. They provide a concise, traceable decision-support summary.

### Dashboard

The dashboard presents reviewed evidence, operational status, analyst briefs, and limitations. It should not present outputs as forecasts or investment guidance.

## Design Principles

- Evidence first.
- Human review before approval.
- Transparent source traceability.
- Deterministic workflow where possible.
- Clear distinction between candidate and approved records.
- British English in all repository-facing language.
- No trading, forecasting, or investment recommendation claims.
