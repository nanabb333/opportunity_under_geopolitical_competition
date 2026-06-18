# Historical Analogue Dataset Methodology

## Purpose

This sprint adds `data/historical_analogue_events.csv` as a structured historical-analogue layer on top of the existing dissertation event-study files. The goal is to preserve the dissertation's narrow empirical framing while making the event universe easier to compare across broader geopolitical and industrial-policy patterns.

The existing dissertation dataset is built for event-study analysis: events are linked to assets, and the main outcome is a sector-adjusted cumulative abnormal return. The historical analogue dataset does not replace that design. It adds a qualitative event-level table that can be used to compare event families, support signals, pressure signals, surprise levels, and observed pathways without claiming more precision than the evidence supports.

## Connection to the Dissertation Theory

The dissertation theory argues that geopolitical competition can generate positive market reactions for selected firms when strategic importance is converted into credible state support. The historical analogue layer supports that theory-building task by separating several mechanisms that can otherwise be conflated:

- broad strategic industrial-policy support;
- direct named state support;
- allied capacity or implementation events;
- export-control or entity-list pressure;
- retaliation or procurement restrictions;
- possible substitution or reallocation pathways.

This structure helps compare state-support cases with threat-dominant contrast cases while keeping the dissertation's core finding intact: the evidence is mixed, and the project should not claim that geopolitical competition is broadly positive for markets.

## Coding Rules

### `event_family`

`event_family` groups events by the dominant policy mechanism visible in the event record. It is coded from the existing event type and policy subtype where possible.

- `broad_policy_support`: legislation or broad support programs that authorise or frame support but are not firm-specific shocks.
- `direct_state_support`: named awards, preliminary terms, subsidies, loans, or other direct support for a firm or facility.
- `implementation_reallocation`: facility openings or capacity moves where support is present but the event may reflect implementation rather than new information.
- `export_control_pressure`: export controls or license requirements that mainly restrict access to products, customers, or technology.
- `entity_list_pressure`: Entity List or similar designation events.
- `allied_export_control_pressure`: allied restrictions that reinforce a broader geopolitical control regime.
- `retaliation_pressure`: retaliatory procurement, market-access, or security actions.

### `surprise_level`

`surprise_level` is qualitative and should not be interpreted as a measured market surprise. It reflects the likely information content of the event date based on anticipation and event-date confidence in the underlying dissertation files.

- `Low`: event was highly anticipated, implementation-focused, or likely already incorporated into expectations.
- `Moderate`: event had a clear public announcement date but may have been partly anticipated.
- `High`: reserved for events with strong evidence of an unanticipated policy shock.
- `TBD`: used when the current dataset does not support a defensible coding.

### `state_support_signal`

`state_support_signal` describes whether the event communicates credible public support for a strategically important firm, sector, or capacity base.

- Strong signals include named subsidies, loans, funded awards, tax credits, direct capacity support, or statutory programs.
- Weak or broad signals include general industrial-policy authorisation without a clean firm-specific announcement.
- `No direct support` is used for threat-dominant events.

### `restriction_or_pressure_signal`

`restriction_or_pressure_signal` records whether the event primarily communicates pressure, restriction, market-access loss, compliance burden, procurement limitation, or geopolitical guardrails.

This field is intentionally separate from `state_support_signal` because some events can contain both support and pressure. For example, a state-support event may still include guardrails or cost-offset concerns, while a restriction event may create possible substitution opportunities for other firms.

### `observed_market_pathway`

`observed_market_pathway` is a qualitative mechanism label, not a coded financial result. It identifies the pathway that the event is most useful for studying:

- `Broad policy support context`;
- `Named support pathway`;
- `Named support/downside-offset pathway`;
- `Capacity reallocation pathway`;
- `Restriction pressure pathway`;
- `Restriction/substitution pathway`.

The field should not be read as evidence that a market reaction occurred. Actual return evidence remains in the event-study outputs.

## What the Dataset Can Support

This dataset can support:

- transparent comparison of event families;
- qualitative historical analogue selection;
- robustness discussion around support versus pressure cases;
- identification of cases that are primary, secondary, contrast, or still `TBD`;
- future expansion into decision-support analytics, provided additional coding and validation are performed.

## What the Dataset Cannot Support

This dataset cannot support:

- causal claims about policy effects;
- precise financial performance claims;
- forecasts of future market reactions;
- investment recommendations;
- claims that state support always produces positive market outcomes;
- claims that all geopolitical pressure creates investable opportunity.

The dataset is a historical comparison layer. It is not a prediction model, trading signal, or investment-advice product.

## Research Integrity Notes

The dataset is intentionally conservative. Where the existing repository does not support a precise value, fields should use `TBD` or `Not coded`. Financial outcomes should not be invented or inferred from narrative impressions. Any future expansion should preserve source notes, distinguish pre-outcome coding from post-outcome interpretation, and document changes before using the dataset for analysis.
