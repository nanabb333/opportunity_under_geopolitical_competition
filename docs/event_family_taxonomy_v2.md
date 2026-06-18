# Event Family Taxonomy V2

## Purpose

This taxonomy standardises future expansion of `data/historical_analogue_events.csv`. It supports the similarity engine, scenario retrieval, observed pathway summaries, and analyst briefs by making event-family coding explicit and repeatable.

Each event should receive one dominant event family. If an event contains multiple mechanisms, code the dominant public announcement and document secondary mechanisms in `evidence_note`.

## Military Exercise

Definition: Publicly observable military drills, manoeuvres, live-fire activity, blockade simulation, air or naval pressure, or force demonstrations linked to geopolitical competition.

Inclusion rules:

- Include events where the military activity itself is the main public information event.
- Include exercises that plausibly affect supply-chain, regional-security, or strategic-sector risk interpretation.
- Include activity around Taiwan, maritime chokepoints, or strategic production regions when the date and public source are clear.

Exclusion rules:

- Exclude routine exercises with no identifiable geopolitical or strategic-sector relevance.
- Exclude military events selected only because a market movement followed.
- Exclude conflicts or attacks that require a separate crisis-event taxonomy unless they are coded as a specific exercise or mobilisation signal.

Coding examples:

- Taiwan Strait live-fire exercise after a political visit.
- Naval blockade simulation near a strategic shipping corridor.
- Public military drill that raises semiconductor supply-chain concern.

## Diplomatic Shock

Definition: Sudden diplomatic rupture, crisis statement, recognition shift, cancelled talks, ambassador recall, or alliance dispute that changes geopolitical expectations.

Inclusion rules:

- Include events where diplomatic escalation is the dominant mechanism.
- Use official statements or reliable same-day reporting to establish timing.
- Code pressure only when the diplomatic action plausibly changes strategic-sector or geopolitical-risk interpretation.

Exclusion rules:

- Exclude routine statements, speeches, or ceremonial disagreements.
- Exclude diplomatic commentary without a clear dated event.
- Exclude meetings that fit better under `Leadership Meeting`.

Coding examples:

- Abrupt cancellation of high-level security talks.
- Formal diplomatic protest that signals policy escalation.
- Recognition decision with strategic-sector implications.

## Export Restriction

Definition: Formal limits on export, re-export, transfer, licensing, or sale of goods, equipment, components, services, or technology.

Inclusion rules:

- Include export-control packages, licensing requirements, allied export controls, and firm disclosures of new export restrictions.
- Code the restriction signal separately from any state-support signal.
- Use the event date when the restriction became public, not when later commentary appeared.

Exclusion rules:

- Exclude informal policy discussion without a binding or announced restriction.
- Exclude sanctions that are primarily financial or transaction-based; code those as `Sanction`.
- Exclude technology-access restrictions that are not export-control instruments; consider `Technology Restriction`.

Coding examples:

- Advanced-computing chip export controls.
- Semiconductor-equipment export restrictions.
- Firm disclosure of a new export-licence requirement.

## Technology Restriction

Definition: Limits on access to platforms, software, intellectual property, cloud services, data, technical collaboration, equipment, or technology ecosystems.

Inclusion rules:

- Include technology bans, cybersecurity restrictions, data-access restrictions, and collaboration limits.
- Include investment-screening actions when the mechanism is technology access rather than capital flow.
- Record the specific technology domain in `affected_sector`.

Exclusion rules:

- Exclude events that are legally and operationally export controls; code those as `Export Restriction`.
- Exclude broad political statements without an implementable technology restriction.
- Exclude sanctions unless the technology-access mechanism dominates.

Coding examples:

- Ban on use of a strategic platform in public systems.
- Restriction on advanced cloud-computing service access.
- Policy blocking technology transfer to a named strategic entity.

## Strategic Investment

Definition: State-backed, sovereign, public-private, or strategically motivated investment in firms, facilities, infrastructure, or national champions.

Inclusion rules:

- Include capital allocation where investment is the central action.
- Include sovereign or state-linked investment with clear strategic-sector rationale.
- Note whether investment is domestic, allied, or cross-border.

Exclusion rules:

- Exclude broad subsidy programmes unless a specific investment decision is the focal event.
- Exclude ordinary private capital expenditure without geopolitical or industrial-policy relevance.
- Exclude facility openings that are implementation milestones unless they create new information.

Coding examples:

- Sovereign fund investment in a strategic semiconductor facility.
- State-linked capital injection into a national champion.
- Public-private financing package for strategic infrastructure.

## Industrial Policy

Definition: Government policy designed to support strategic sectors through subsidies, tax credits, loans, procurement, regulation, local-content rules, or capacity programmes.

Inclusion rules:

- Include legislation, subsidy awards, preliminary terms, procurement commitments, and strategic-sector programmes.
- Code named support separately in `state_support_signal`.
- Distinguish broad policy support from firm-specific support in `evidence_note`.

Exclusion rules:

- Exclude general economic policy not tied to strategic sectors.
- Exclude market commentary about possible support unless a policy event is public.
- Exclude pure export restrictions unless support policy is dominant.

Coding examples:

- CHIPS-style subsidy award.
- Strategic-sector loan and grant package.
- Industrial-policy legislation for semiconductors or defence supply chains.

## Sanction

Definition: Formal sanctions, asset freezes, transaction prohibitions, entity restrictions, financial restrictions, or sectoral sanctions imposed by a state or coalition.

Inclusion rules:

- Include sanctions with clear legal authority and public date.
- Note target type: firm, sector, country, individual network, or technology ecosystem.
- Code pressure signal according to likely compliance, access, or transaction burden.

Exclusion rules:

- Exclude export controls that are not sanctions.
- Exclude informal threats of sanctions unless formal action follows.
- Exclude entity-list actions if the project codes them separately as export-control pressure, unless the sanction mechanism dominates.

Coding examples:

- Sectoral sanctions on strategic energy or defence firms.
- Asset freeze on a strategic technology entity.
- Transaction ban affecting a strategic supply chain.

## Supply Chain Relocation

Definition: Announcements, policies, or facility decisions that relocate production, sourcing, assembly, logistics, or strategic capacity across borders.

Inclusion rules:

- Include reshoring, friend-shoring, near-shoring, and risk-driven capacity relocation events.
- Include facility announcements when location choice is the central strategic signal.
- Code state support separately if relocation is subsidy-backed.

Exclusion rules:

- Exclude ordinary capacity expansion with no relocation logic.
- Exclude implementation openings if the information was already public and fully anticipated.
- Exclude company strategy commentary without a dated decision.

Coding examples:

- Strategic fab relocation to an allied market.
- Supply-chain rerouting announcement after geopolitical pressure.
- Government-backed production shift away from a high-risk region.

## Election Event

Definition: Election outcomes, major electoral shocks, or leadership transitions through electoral processes that plausibly alter strategic policy, sanctions, industrial policy, or geopolitical risk.

Inclusion rules:

- Include final results or major confirmed electoral outcomes with clear policy relevance.
- Code policy implications conservatively and note uncertainty.
- Use the public result date or certified outcome date, depending on information timing.

Exclusion rules:

- Exclude campaign promises without an election outcome.
- Exclude opinion polling.
- Exclude routine elections with no identifiable strategic-sector or geopolitical relevance.

Coding examples:

- Election result shifting industrial-policy direction.
- Election outcome changing expected sanctions policy.
- Leadership transition affecting Taiwan, semiconductor, or defence policy expectations.

## Leadership Meeting

Definition: High-level meetings, summits, visits, or talks between heads of state, ministers, regulators, or senior officials that materially affect geopolitical or industrial-policy expectations.

Inclusion rules:

- Include meetings that produce a clear statement, agreement, breakdown, or policy signal.
- Use the meeting date or communique date as appropriate.
- Code pressure or support only when the meeting output supports that interpretation.

Exclusion rules:

- Exclude ceremonial meetings without substantive policy signal.
- Exclude routine scheduled meetings unless a new public commitment or rupture occurs.
- Exclude broad diplomatic shocks where the meeting itself is not the focal event.

Coding examples:

- Bilateral summit producing technology-control cooperation.
- Failed security talks that increase pressure interpretation.
- Leadership meeting announcing strategic-sector coordination.

## Semiconductor Expansion

Definition: New semiconductor fabs, advanced-packaging facilities, capacity expansions, foundry commitments, equipment investments, or strategic chip-sector buildouts.

Inclusion rules:

- Include new capacity announcements where semiconductor expansion is the main information event.
- Code state support if public subsidy, tax credit, loan, or procurement support is attached.
- Distinguish announcement, award, construction, and opening milestones.

Exclusion rules:

- Exclude routine production updates without strategic or geopolitical relevance.
- Exclude facility openings if they only implement a long-known decision and add no new information.
- Exclude broad industrial policy where the facility decision is not the focal event.

Coding examples:

- New advanced-node fab announcement.
- State-supported packaging facility expansion.
- Cross-border foundry investment tied to supply-chain resilience.

## Cross-Cutting Coding Rules

- Code only what was knowable at the public event date.
- Prefer official sources for existence, timing, and policy content.
- Use reputable reporting only to clarify timing or context when official sources are incomplete.
- Use `TBD` or `Not coded` when evidence is insufficient.
- Do not infer financial outcomes from event-family labels.
- Do not treat event-family labels as forecasts or investment signals.
