# Dataset Coverage Analysis

## Dataset Size

The current historical analogue dataset contains 12 events.

Source: `data/historical_analogue_events.csv`

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

## Geographic Distribution

| Country or region | Count |
|---|---:|
| US | 7 |
| China | 1 |
| Japan | 1 |
| Japan/Taiwan | 1 |
| US/South Korea | 1 |
| US/Taiwan | 1 |

## Sector Distribution

| Affected sector | Count |
|---|---:|
| semiconductors | 4 |
| memory chips | 3 |
| foundry | 2 |
| AI chips | 1 |
| defence semiconductors | 1 |
| semiconductor equipment | 1 |

## Strategic Importance Distribution

| Strategic importance | Count |
|---|---:|
| High | 12 |

All current events are coded as high strategic importance. This keeps the dataset aligned with the dissertation mechanism, but it limits variation for future comparison.

## Surprise Distribution

| Surprise level | Count |
|---|---:|
| Moderate | 9 |
| Low | 2 |
| TBD | 1 |

## Pathway Distribution

| Observed pathway | Count |
|---|---:|
| Restriction pressure pathway | 4 |
| Named support/downside-offset pathway | 3 |
| Named support pathway | 2 |
| Broad policy support context | 1 |
| Capacity reallocation pathway | 1 |
| Restriction/substitution pathway | 1 |

## Coverage Strengths

- Strong coverage of semiconductor-linked industrial policy.
- Several direct state-support cases with named beneficiaries.
- Useful contrast coverage for export-control and restriction-pressure cases.
- All rows include strategic-importance coding.
- Pathway coverage distinguishes pressure, named support, and capacity reallocation mechanisms.

## Coverage Weaknesses

- The dataset is small at 12 events.
- Geographic coverage is U.S.-heavy.
- Sector coverage is concentrated in semiconductors and chip subsectors.
- Strategic importance has no variation because all events are coded `High`.
- Military, diplomatic, sanctions, election, leadership-meeting, technology-restriction, strategic-investment, and broader supply-chain relocation cases remain thin or absent.

## Generated Evidence Gaps

The coverage script now generates evidence-gap lists in `results/dataset_coverage_report.json`.

Current high-priority gaps:

- Event family gap: Military Exercise
- Event family gap: Diplomatic Shock
- Event family gap: Technology Restriction
- Event family gap: Strategic Investment
- Event family gap: Sanction
- Event family gap: Supply Chain Relocation
- Pathway gap: military-pressure pathway
- Pathway gap: diplomatic-shock pathway
- Pathway gap: sanctions-pressure pathway
- Pathway gap: election-policy uncertainty pathway

These are collection priorities, not analytical findings.

## Recommendations

Near-term expansion should prioritise an 18-event dataset that improves event-family and pathway diversity before scaling to 50 and 100 events.

Recommended first collection priorities:

1. Military Exercise
2. Diplomatic Shock
3. Sanction
4. Technology Restriction
5. Supply Chain Relocation
6. Strategic Investment

Coverage counts are descriptive. They do not imply forecast accuracy, causal strength, or investment relevance.
