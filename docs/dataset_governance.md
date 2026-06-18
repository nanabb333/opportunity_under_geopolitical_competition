# Dataset Governance

## Purpose

Dataset governance defines how approved event records are versioned, reviewed, and reproduced. The goal is to make the historical analog dataset scalable without weakening research controls.

## Version Control

All approved dataset changes should be tracked through Git. Dataset updates should be committed with related documentation and regenerated outputs when possible.

Recommended update grouping:

- approved dataset row changes
- dataset change log entry
- regenerated analytical outputs
- updated coverage documentation if needed

Candidate queue updates may be committed separately from approved dataset changes.

## Update History

`data/dataset_change_log.csv` records dataset-level changes. Each update should include:

- `update_id`
- `update_date`
- `event_count_before`
- `event_count_after`
- `events_added`
- `reviewer`
- `notes`

The change log should not replace Git history. It provides a human-readable governance record for analysts and reviewers.

## Reproducibility

After approved dataset changes, rerun:

```bash
python3 scripts/pipeline_orchestrator.py
```

At minimum, validation and generated outputs should be reproducible from the committed data files and scripts.

The pipeline should regenerate:

- dataset coverage outputs
- historical similarity outputs
- scenario outputs
- observed pathway outputs
- system health report

## Review Accountability

Each approved event should have a documented reviewer or review note. Review accountability matters because event coding includes qualitative judgment.

Reviewers are responsible for:

- checking source reliability
- preserving uncertainty
- avoiding unsupported interpretation
- maintaining evidence notes
- ensuring candidate records do not become approved events without review

## Governance Boundaries

The dataset remains a descriptive historical evidence base. Governance controls do not convert the system into a forecast model, expected-return model, or investment recommendation system.
