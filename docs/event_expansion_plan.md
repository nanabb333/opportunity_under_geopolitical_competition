# Event Expansion Plan

## Current Event Count

Current event coverage:

- `data/events.csv`: 12 events
- `data/historical_analogue_events.csv`: 12 events

The historical analogue dataset currently mirrors the dissertation event universe. This is useful for transparency, but it is too small and too semiconductor-policy-centred for broad historical comparison.

## Target Event Count

Recommended target count for the next evidence-base expansion:

- Near-term target: 30 events
- Medium-term target: 50 events
- Longer-term research target: 75 to 100 events

The near-term target is the best next sprint scope because it materially improves event-family coverage without turning the project into an uncontrolled collection effort.

## Current Event Family Coverage

Current `historical_analogue_events.csv` families:

| Event family | Current count |
|---|---:|
| `direct_state_support` | 5 |
| `export_control_pressure` | 2 |
| `allied_export_control_pressure` | 1 |
| `broad_policy_support` | 1 |
| `entity_list_pressure` | 1 |
| `implementation_reallocation` | 1 |
| `retaliation_pressure` | 1 |

Current coverage is strongest for semiconductor industrial policy, direct state support, and export-control pressure. It is weakest for military, diplomatic, electoral, sanctions, leadership-meeting, and supply-chain relocation events.

## Missing Event Categories

Priority gaps:

- Military Exercise
- Diplomatic Shock
- Sanction
- Election Event
- Leadership Meeting
- Supply Chain Relocation

Secondary gaps:

- Technology Restriction beyond export controls
- Strategic Investment outside direct subsidy announcements
- Industrial Policy outside the U.S. CHIPS Act context
- Semiconductor Expansion outside current U.S. and Japan/Taiwan examples

## Prioritization Roadmap

### Phase 1: Balanced Analogue Base

Target: 30 total events.

Add approximately 18 carefully sourced events while preserving current dissertation events. Prioritise:

- 4 Military Exercise events
- 3 Diplomatic Shock events
- 3 Sanction events
- 3 Supply Chain Relocation events
- 3 Leadership Meeting events
- 2 Election Event events

Purpose: make scenario retrieval less dependent on export-control and subsidy analogues.

### Phase 2: Cross-Family Robustness

Target: 50 total events.

Expand underrepresented families and add non-U.S. cases where source quality is strong. Prioritise:

- allied industrial-policy actions;
- East Asia security shocks;
- technology restrictions outside semiconductors;
- critical supply-chain relocation cases;
- major sanctions with clear sector exposure.

Purpose: improve historical comparison across support, pressure, and reallocation pathways.

### Phase 3: Research-Grade Historical Analogue Layer

Target: 75 to 100 total events.

Add a screened event log with included and excluded events, source hierarchy, coding confidence, and change history.

Purpose: support a more defensible historical analogue research base while preserving transparency and avoiding post hoc event selection.

## Implementation Rules

- Do not add events without a documented public source.
- Do not code market interpretation from post-event price movement alone.
- Use `TBD` or `Not coded` where evidence is insufficient.
- Preserve current dissertation event IDs and avoid rewriting prior coding unless a documented correction is needed.
- Add events in batches with a short changelog and validation run.
