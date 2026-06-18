# Event Expansion Framework

## Purpose

The dataset expansion framework defines how the historical analogue evidence base should grow without weakening research quality. The goal is broader comparison coverage, not false precision or more confident claims.

## Current Dataset

The current approved historical analogue dataset is `data/historical_analogue_events.csv`.

Current size: 12 events.

Current strengths:

- clear link to the dissertation event-study base;
- strong semiconductor and industrial-policy relevance;
- deterministic validation and downstream analytics;
- visible evidence notes and conservative coding.

Current limitations:

- small sample size;
- heavy concentration in U.S. policy events;
- limited event-family diversity;
- limited observed pathway diversity;
- high reliance on semiconductor subsidy and export-control examples.

## Target Dataset

The target dataset should grow in staged milestones:

```text
18 Events
        ↓
50 Events
        ↓
100 Events
```

The target is not a mechanically large dataset. Each expansion stage should improve event-family, geography, sector, and pathway coverage while preserving source traceability.

## Expansion Priorities

Priority 1: Mechanism diversity

- Military Exercise
- Diplomatic Shock
- Sanction
- Technology Restriction
- Supply Chain Relocation

Priority 2: Geography diversity

- Taiwan
- China
- Japan
- South Korea
- European Union
- Netherlands
- India
- Southeast Asia

Priority 3: Sector diversity

- critical minerals
- defence systems
- telecommunications infrastructure
- energy security
- battery and clean-energy supply chains
- cloud and AI infrastructure
- shipping and logistics

## Collection Roadmap

### 18 Events

Goal: add six sourced events that reduce the most visible gaps.

Recommended mix:

- two military exercise or diplomatic shock events;
- one sanctions event;
- one technology restriction event;
- one supply-chain relocation event;
- one non-U.S. industrial-policy or semiconductor expansion event.

Quality standard: every added event should have at least one reliable dated source and a concise evidence note.

### 50 Events

Goal: build enough breadth for meaningful historical analogue retrieval across the V2 taxonomy.

Recommended mix:

- at least five event families represented by five or more events;
- at least five regions represented;
- at least three non-semiconductor strategic sectors represented;
- multiple observed pathway categories beyond restriction pressure and named support.

Quality standard: expansion should occur in reviewed batches with dataset validation and coverage reports regenerated after each batch.

### 100 Events

Goal: create a research-grade historical comparison layer broad enough for portfolio demonstration and analyst-facing scenario review.

Recommended mix:

- broad event-family coverage across the V2 taxonomy;
- balanced pressure, support, relocation, diplomatic, election, and sanctions pathways;
- richer geography coverage;
- stronger sector diversity while retaining clear geopolitical relevance.

Quality standard: the dataset should include batch documentation, source notes, validation checks, and regular quality audits.

## Quality Standards

- Code only sourced, dated public events.
- Keep candidate events separate from approved events.
- Preserve `TBD` and `Not coded` where evidence is incomplete.
- Do not infer returns, causal effects, or future outcomes.
- Do not use LLM-generated claims as evidence.
- Regenerate coverage analytics after every approved batch.
- Update evidence-gap documentation when new coverage changes the roadmap.

## Future Event Targets

Future event targets should be selected because they improve comparison quality:

- event families currently absent from the dataset;
- regions underrepresented in current coverage;
- pathway categories needed for scenario and analyst brief diversity;
- sectors relevant to strategic competition beyond semiconductors.

Expansion should remain conservative. A smaller evidence base with reliable coding is preferable to a larger dataset with weak traceability.
