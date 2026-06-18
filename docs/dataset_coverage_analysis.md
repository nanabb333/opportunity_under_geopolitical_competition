# Dataset Coverage Analysis

## Dataset Size

The current historical analog dataset contains 12 events.

Source: `data/historical_analog_events.csv`

Generated outputs:

- `results/dataset_coverage_report.json`
- `results/dataset_coverage_summary.csv`

## Event Family Distribution

| Event family | Count |
|---|---:|
| `direct_state_support` | 5 |
| `export_control_pressure` | 2 |
| `allied_export_control_pressure` | 1 |
| `broad_policy_support` | 1 |
| `entity_list_pressure` | 1 |
| `implementation_reallocation` | 1 |
| `retaliation_pressure` | 1 |

## Sector Distribution

| Affected sector | Count |
|---|---:|
| semiconductors | 4 |
| memory chips | 3 |
| foundry | 2 |
| AI chips | 1 |
| defense semiconductors | 1 |
| semiconductor equipment | 1 |

## Geographic Distribution

| Country or region | Count |
|---|---:|
| US | 7 |
| China | 1 |
| Japan | 1 |
| Japan/Taiwan | 1 |
| US/South Korea | 1 |
| US/Taiwan | 1 |

## Other Coverage Fields

Strategic importance:

- `High`: 12

Surprise level:

- `Moderate`: 9
- `Low`: 2
- `TBD`: 1

State-support signal:

- `No direct support`: 5
- `Strong named subsidy and capacity-support signal`: 2
- five other support-signal categories appear once each.

## Coverage Strengths

- Strong coverage of semiconductor-linked industrial policy.
- Several direct state-support cases with named beneficiaries.
- Useful contrast coverage for export-control and restriction-pressure cases.
- All events include high strategic-importance coding, which keeps the dataset aligned with the dissertation theory.

## Coverage Weaknesses

- The dataset is small at 12 events.
- Geographic coverage is U.S.-heavy.
- Sector coverage is concentrated in semiconductors, memory chips, foundry, and related chip subsectors.
- Strategic importance has no variation because all events are coded `High`.
- Military, diplomatic, election, sanctions, leadership-meeting, and broader supply-chain relocation cases are not yet represented.

## Missing Categories

Current missing or underrepresented categories include:

- Military Exercise
- Diplomatic Shock
- Sanction
- Election Event
- Leadership Meeting
- Supply Chain Relocation
- Technology Restriction outside export-control cases
- Strategic Investment outside subsidy awards
- Non-semiconductor strategic sectors

## Recommendations

Near-term expansion should prioritize a 30-event dataset with better family balance. Add sourced events in batches, beginning with underrepresented categories rather than adding more direct semiconductor subsidy cases.

Recommended first collection priorities:

1. Military Exercise
2. Diplomatic Shock
3. Sanction
4. Supply Chain Relocation
5. Leadership Meeting
6. Election Event

Coverage counts are descriptive. They do not imply forecast accuracy, causal strength, or investment relevance.
