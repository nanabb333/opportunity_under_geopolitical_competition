# Intelligence Lifecycle

## Purpose

The intelligence lifecycle describes how information becomes reviewed, structured, and usable for decision support.

## Lifecycle Stages

### 1. Source Registration

Sources are recorded in `data/source_registry.csv`. Each source receives a reliability level and review frequency.

### 2. Information Monitoring

Analysts or future automation review registered sources for potentially relevant geopolitical developments.

Monitoring may include:

- military activity
- export restrictions
- sanctions
- industrial policy
- strategic investment
- supply-chain relocation
- diplomatic meetings
- election events
- technology restrictions

### 3. Candidate Capture

Potential events enter `data/candidate_events.csv`. This stage is intentionally broad. Candidate status does not imply approval.

### 4. Review and Triage

Human reviewers assess relevance, source quality, duplicate risk, coding clarity, and uncertainty.

Possible decisions:

- approve
- reject
- defer
- request more source evidence

### 5. Dataset Integration

Approved candidates enter `data/approved_events.csv`. The approved dataset is the only source for historical analogue search.

### 6. Historical Analogue Retrieval

New scenarios or approved records are compared with historical records to identify similar cases. The comparison is descriptive and transparent.

### 7. Evidence Synthesis

Retrieved analogues and observed pathways are combined into a structured brief. Evidence synthesis should preserve caveats and source notes.

### 8. Dashboard Publication

Dashboard outputs show the current evidence base, operational status, analyst briefs, and limitations.

## Quality Controls

- Candidate and approved datasets are separate.
- Human review is required for approval.
- Source IDs remain linked to approved records.
- Evidence notes are mandatory for approved records.
- Briefs must include caveats and limitations.

## Lifecycle Boundary

The lifecycle is designed for evidence management and decision support. It does not automate judgement, forecast outcomes, or recommend investments.
