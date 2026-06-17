# Event Family Taxonomy V2

## Purpose

This taxonomy defines event families for future expansion of `data/historical_analog_events.csv`. It is designed to improve consistency before new events are added.

Each event should be assigned one dominant event family. If an event includes multiple mechanisms, code the dominant public announcement and document the secondary mechanism in `evidence_note`.

## Military Exercise

Definition: Publicly observable military drills, maneuvers, live-fire exercises, blockade simulations, or force demonstrations linked to geopolitical competition.

Coding rules:

- Use when the event communicates military pressure without a direct economic policy instrument.
- Code `restriction_or_pressure_signal` as moderate or strong if the exercise plausibly affects perceived supply-chain, regional, or security risk.
- Do not code state support unless the same announcement includes a direct support instrument.
- Use `surprise_level = Low` if the exercise was scheduled and public in advance.

## Diplomatic Shock

Definition: Sudden diplomatic rupture, crisis statement, recall of ambassadors, cancellation of talks, recognition shift, or major alliance dispute.

Coding rules:

- Use when the main mechanism is political or diplomatic escalation rather than a formal trade, technology, or military instrument.
- Code evidence from official statements or reliable same-day reporting.
- Avoid using market commentary as the basis for mechanism coding.

## Export Restriction

Definition: Formal restrictions on export, re-export, transfer, or licensing of goods, equipment, components, or technology.

Coding rules:

- Use for export-control packages, licensing requirements, and allied controls.
- Code `state_support_signal = No direct support` unless the same event includes a support program.
- Distinguish broad sector controls from firm-specific disclosures in `evidence_note`.

## Technology Restriction

Definition: Restrictions on access to technology, platforms, software, intellectual property, cloud services, chips, equipment, data, or technical collaboration.

Coding rules:

- Use when the restriction is technology-access focused but not primarily an export-control event.
- Include cybersecurity bans, platform restrictions, investment-screening technology limits, or technical collaboration restrictions.
- If the event is legally an export control, prefer `Export Restriction`.

## Strategic Investment

Definition: State-backed or strategically motivated investment in firms, facilities, infrastructure, or national champions.

Coding rules:

- Use when the central action is capital allocation or investment rather than subsidy authorization alone.
- Code whether the investor is public, sovereign, state-linked, or allied-policy-backed.
- Avoid claiming market impact unless measured elsewhere.

## Industrial Policy

Definition: Government policy designed to support strategic sectors through subsidies, tax credits, loans, procurement, regulation, or capacity programs.

Coding rules:

- Use for broad policy programs or named support if industrial-policy design is the dominant event.
- Code direct named awards separately in `state_support_signal`.
- Use `surprise_level = Low` for heavily anticipated legislation.

## Sanction

Definition: Formal sanctions, asset freezes, transaction prohibitions, entity restrictions, or sectoral sanctions imposed by a state or coalition.

Coding rules:

- Use for sanctions that create restriction, compliance, or market-access pressure.
- Distinguish sanctions from export controls when the legal instrument is primarily financial, entity-based, or transaction-based.
- Note whether the sanction targets a firm, sector, country, or individual network.

## Supply Chain Relocation

Definition: Announcements, policies, or facility decisions that relocate production, sourcing, assembly, or strategic capacity across borders.

Coding rules:

- Use when the main mechanism is reallocation of capacity or supply-chain geography.
- Code state support separately if relocation is subsidy-backed.
- Treat facility openings cautiously if they are implementation events rather than new information shocks.

## Election Event

Definition: Election results, major electoral shocks, or candidate outcomes that plausibly alter strategic policy, sanctions, industrial policy, or geopolitical risk.

Coding rules:

- Use only when the event has a clear date and plausible policy relevance.
- Do not code based on campaign rhetoric alone unless the event is the election outcome itself.
- Note if the policy implication is uncertain or requires later confirmation.

## Leadership Meeting

Definition: High-level meetings, summits, visits, or talks between heads of state, ministers, or senior officials that materially affect geopolitical or industrial-policy expectations.

Coding rules:

- Use when the meeting itself is the focal public information event.
- Code pressure or support only if the meeting produces a clear statement, agreement, breakdown, or policy signal.
- Avoid overcoding ceremonial meetings.

## Semiconductor Expansion

Definition: New semiconductor fabs, capacity expansions, advanced packaging investments, foundry commitments, or strategic chip-sector buildouts.

Coding rules:

- Use when the event is primarily about semiconductor capacity expansion.
- Code state support if the expansion is tied to public subsidy, tax credit, loan, or industrial-policy support.
- Distinguish new commitments from facility openings in `evidence_note`.

## Cross-Cutting Coding Standards

- Code the event as it was knowable at the announcement date.
- Prefer official sources for existence, timing, and policy content.
- Use reputable same-day reporting to clarify details when official sources are incomplete.
- Use `TBD` or `Not coded` when the evidence does not support a confident value.
- Do not infer financial outcomes from event-family labels.
