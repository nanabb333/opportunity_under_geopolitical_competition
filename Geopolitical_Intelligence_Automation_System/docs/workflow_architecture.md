# Workflow Architecture

## Purpose

This document defines the operational workflow for moving geopolitical information from raw sources to dashboard-ready analyst outputs.

## Workflow

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

## Step 1: Information Sources

Sources are registered with basic metadata:

- source identity
- source type
- coverage region
- coverage theme
- reliability level
- review frequency
- access method
- notes

The workflow starts with source awareness, not automated scraping.

## Step 2: Candidate Event Queue

Candidate events are entered when a source item appears relevant to geopolitical risk, industrial policy, sanctions, military activity, supply-chain relocation, or strategic technology.

Candidate records should preserve uncertainty. Missing values should remain blank or be marked for review rather than being inferred.

## Step 3: Human Review

Reviewers check whether the candidate is:

- relevant
- dateable
- source-supported
- strategically meaningful
- suitable for coding
- distinct from previously approved events

Human review is the main control against noisy automation.

## Step 4: Approved Intelligence Records

Approved records are integrated into the intelligence dataset only after review. The approved dataset should be stable, auditable, and suitable for historical comparison.

## Step 5: Historical Analogue Search

Historical analogue search compares a scenario or approved event against prior approved records. Matching should use transparent coded features and documented scoring rules.

## Step 6: Evidence Synthesis

Evidence synthesis combines:

- scenario description
- most relevant historical analogues
- observed pathways
- evidence notes
- caveats
- limitations

It should not add unsupported facts or claims.

## Step 7: Analyst Brief

The analyst brief converts structured evidence into a readable decision-support artefact. It should be concise, traceable, and conservative.

## Step 8: Dashboard

The dashboard presents current pipeline status, approved evidence, analyst briefs, and limitations. It is a communication layer, not a prediction engine.

## Workflow Boundaries

This architecture supports structured intelligence operations. It does not provide:

- forecasts
- probability claims
- trading signals
- investment advice
- automated approval of events
