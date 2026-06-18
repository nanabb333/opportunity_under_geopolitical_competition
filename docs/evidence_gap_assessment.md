# Evidence Gap Assessment

## Purpose

This assessment identifies where the historical analog dataset is currently thin. It supports future event collection by showing which event families, sectors, regions, and pathway types need additional sourced evidence.

## Underrepresented Event Families

Current event-family coverage is concentrated in:

- `direct_state_support`: 5 events
- `export_control_pressure`: 2 events

All other represented families have only one event each. Several planned taxonomy families have zero current coverage.

Highest-priority gaps:

- Military Exercise
- Diplomatic Shock
- Sanction
- Election Event
- Leadership Meeting
- Supply Chain Relocation

These categories should be prioritized because they would broaden scenario retrieval beyond subsidy and export-control analogs.

## Underrepresented Sectors

Current sector coverage is concentrated in semiconductor-linked categories:

- semiconductors
- memory chips
- foundry
- AI chips
- semiconductor equipment
- defense semiconductors

Underrepresented sectors for future collection:

- critical minerals;
- defense systems;
- energy security;
- telecommunications infrastructure;
- shipping and logistics;
- battery and clean-energy supply chains;
- cloud, AI infrastructure, and data-center capacity.

These sectors should be added only when events meet the source and coding standards in `docs/event_collection_protocol.md`.

## Underrepresented Regions

Current geography is U.S.-heavy:

- US: 7 events
- all other country or region labels: 1 event each

Future collection should improve coverage of:

- Taiwan;
- China;
- Japan;
- South Korea;
- European Union;
- Netherlands;
- India;
- Southeast Asia;
- Middle East energy-security cases, where relevant to strategic supply chains.

The goal is not geographic breadth for its own sake. New regions should be added when they improve historical comparison for strategic-sector or geopolitical-pressure mechanisms.

## Underrepresented Pathway Types

Current pathway coverage is strongest for:

- restriction pressure;
- named support;
- named support/downside-offset.

Underrepresented pathway types:

- capacity relocation;
- diplomatic shock pathway;
- sanctions pressure pathway;
- election-policy uncertainty pathway;
- leadership-meeting de-escalation or escalation pathway;
- supply-chain rerouting pathway.

## Prioritized Collection Plan

Near-term collection should focus on categories that improve diversity of mechanisms:

1. Add military exercise events connected to Taiwan or strategic supply-chain risk.
2. Add sanctions events with clear sector or firm exposure.
3. Add diplomatic shock events with identifiable dates and policy relevance.
4. Add leadership meeting events only when the meeting produced a clear policy signal.
5. Add supply-chain relocation events with documented facility, sourcing, or capacity implications.
6. Add election events only where the policy implication is clear enough to code conservatively.

## Quality Guardrails

- Do not add events only because they are famous.
- Do not add events because the market reaction is already known.
- Do not expand into weakly sourced geopolitical narratives.
- Do not treat pathway counts as probabilities.
- Preserve `TBD` and `Not coded` where evidence is insufficient.

The highest-value next dataset is not the largest one. It is the one with enough family, sector, and geography diversity to support meaningful historical comparison while remaining transparent and source-based.
