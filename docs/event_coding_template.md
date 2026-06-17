# Event Coding Template

Use this template for one candidate historical analog event before adding it to `data/historical_analog_events.csv`.

## Event Record

```yaml
event_id: TBD
event_date: YYYY-MM-DD
event_title: TBD
source: TBD
event_family: TBD
affected_sector: TBD
strategic_importance_level: TBD
state_support_signal: TBD
restriction_or_pressure_signal: TBD
surprise_level: TBD
market_interpretation: TBD
observed_market_pathway: TBD
evidence_note: TBD
```

## Field Guidance

| Field | Coding guidance |
|---|---|
| `event_id` | Stable unique ID. Do not reuse existing IDs. |
| `event_date` | Public information release date in `YYYY-MM-DD` format. |
| `event_title` | Short descriptive event name. |
| `source` | Reliable dated source used for event existence and timing. |
| `event_family` | Dominant family from `docs/event_family_taxonomy_v2.md`. |
| `affected_sector` | Sector most directly implicated by the event. |
| `strategic_importance_level` | Qualitative strategic relevance, such as `High`, `Medium`, `Low`, or `TBD`. |
| `state_support_signal` | Support signal visible in the source, or `No direct support`. |
| `restriction_or_pressure_signal` | Restriction, pressure, compliance, military, diplomatic, or supply-chain pressure signal. |
| `surprise_level` | `Low`, `Moderate`, `High`, or `TBD`; do not infer from price movement. |
| `market_interpretation` | Qualitative mechanism interpretation, not a financial result. |
| `observed_market_pathway` | Research pathway label, such as restriction pressure, named support, or capacity relocation. |
| `evidence_note` | Concise source-based coding rationale. |

## Review Checklist

- Source is reliable and dated.
- Event date is defensible.
- Event family follows the taxonomy.
- Support and pressure signals are coded separately.
- Any uncertain value is marked `TBD` or `Not coded`.
- No return, forecast, or investment implication is invented.
