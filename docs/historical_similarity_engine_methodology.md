# Historical Similarity Engine Methodology

## Purpose

The historical similarity engine adds a deterministic analytical layer to the historical analogue dataset. Its purpose is to help compare geopolitical and industrial-policy events using coded qualitative features rather than narrative intuition alone.

Similarity scoring is useful because the dissertation event universe contains several different event types: direct state-support announcements, broad policy support, implementation or reallocation events, export controls, entity-list actions, and retaliation cases. A transparent pairwise score makes it easier to identify which events are substantively close enough to be useful analogues, while preserving the repository's academically cautious framing.

## Features Compared

The script compares each event with every other event using eight fields from `data/historical_analogue_events.csv`:

- `event_family`
- `affected_sector`
- `strategic_importance_level`
- `state_support_signal`
- `restriction_or_pressure_signal`
- `surprise_level`
- `market_interpretation`
- `observed_market_pathway`

These fields were selected because they describe event structure and interpretation without importing financial outcomes into the similarity score.

## Scoring Rule

For each compared field:

- exact match: `1.0` point;
- partial textual overlap: `0.5` point;
- no match: `0.0` points;
- `TBD`, `Not coded`, blank, or equivalent unavailable values: `0.0` points.

The final similarity score is:

```text
total field points / 8 compared fields
```

Scores therefore range from `0.0000` to `1.0000`. A score of `1.0000` would mean all eight coded features match exactly. A score near `0.5000` means the pair shares several exact or partial features but should still be interpreted cautiously.

## Determinism and Transparency

The engine is deterministic because it uses only local CSV inputs and fixed scoring rules. It does not use LLM API calls, embeddings, stochastic matching, external data, or market outcomes. The same input dataset should produce the same similarity matrix every time.

The output file records:

- source event;
- comparison event;
- similarity score;
- fields with exact or partial overlap;
- fields with no coded overlap;
- a short interpretation note.

This makes the score auditable and easy to challenge. If a researcher disagrees with a score, the appropriate correction is to revise the underlying coded fields or the documented scoring rule, not to reinterpret the result after observing market performance.

## What This Is Not

The similarity engine is not a prediction model. It does not forecast returns, policy outcomes, firm performance, or investment opportunities. It does not claim that historically similar events will produce similar market reactions.

The engine is a comparison tool for historical research and portfolio presentation. It helps organise analogue reasoning; it does not validate causal claims.

## Limitations

The scores are only as strong as the coded qualitative fields. Short phrases can overlap textually even when the substantive mechanisms differ, and two events can be analytically related despite having low textual overlap. The current method also weights all eight fields equally, even though future research may decide that some features are more important than others.

The output should be read as a structured starting point for historical comparison, not as a final ranking of policy importance or market relevance.
