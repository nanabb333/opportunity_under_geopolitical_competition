# Dataset Update Protocol

## Purpose

This protocol defines how the historical analogue dataset should be maintained as the project evolves toward a continuously updated geopolitical intelligence system. The workflow is designed for research quality, transparency, and reproducibility.

## Weekly Workflow

1. Review priority source categories in `data/source_registry.csv`.
2. Record candidate events in the candidate event template or prototype candidate format.
3. Screen candidates against `docs/event_collection_protocol.md`.
4. Assign provisional event families using `docs/event_family_taxonomy_v2.md`.
5. Code only candidates with sufficient source support.
6. Validate candidate records before integration.
7. If approved events are added, rerun analytical outputs.

Weekly work should emphasize candidate triage and documentation quality over volume.

## Monthly Workflow

1. Review dataset coverage by event family, sector, geography, strategic importance, surprise level, and support signal.
2. Run or refresh dataset coverage outputs.
3. Compare new candidate patterns against the evidence gap assessment.
4. Identify overrepresented and underrepresented event types.
5. Review whether scenario outputs depend too heavily on a narrow subset of events.
6. Update documentation if coding rules or source priorities need clarification.

## Quarterly Audit

1. Audit source registry reliability levels.
2. Review a sample of coded events for consistency.
3. Check whether event-family taxonomy needs revision.
4. Confirm generated results are reproducible from the current dataset.
5. Review all limitations and disclaimers.
6. Consider freezing a dated dataset release if major additions were made.

## Dataset Review Checklist

- Event IDs are unique and non-empty.
- Event dates are documented and consistently formatted.
- Event titles are concise and source-grounded.
- Event family coding follows taxonomy rules.
- Affected sector and geography are specific enough for comparison.
- Support and pressure signals are transparent.
- Surprise level uses conservative coding.
- Evidence notes explain what is known and what remains uncertain.

## Coverage Review Checklist

- Event families are not dominated by one category without explanation.
- Semiconductor and adjacent strategic sectors are distinguishable.
- Geographic coverage is documented.
- Support events and pressure events are both represented.
- Observed pathways include support, pressure, substitution, and capacity reallocation where evidence permits.
- Missing categories are recorded before new collection begins.

## Quality Review Checklist

- No candidate event is treated as approved without human review.
- No financial precision is added without documented calculation.
- No forecast or investment recommendation is inferred from historical analogues.
- Source notes are sufficient for future review.
- Validation scripts pass after dataset changes.
- Generated outputs are refreshed after approved dataset changes.
