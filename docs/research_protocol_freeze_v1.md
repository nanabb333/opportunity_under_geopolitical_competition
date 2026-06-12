# Research Protocol Freeze V1

## Purpose

This protocol specifies how to replicate the project:

> **State-backed opportunity under geopolitical competition**

Core mechanism:

```text
Geopolitical Competition
-> Strategic Importance
-> Credible State Support
-> Investor Interpretation
-> Positive Market Reaction
```

The protocol is designed for dissertation-level transparency. Another researcher should be able to follow the same procedures, reconstruct the event list, reproduce the event-firm links, and audit the coding decisions before examining market outcomes.

This protocol does not change the frozen theory, research design, or dataset architecture.

## Replication Principle

All event inclusion, event exclusion, event dating, beneficiary identification, event-firm linking, and mechanism coding must be completed before calculating abnormal returns.

The project fails its transparency standard if event coding or beneficiary selection is revised after observing market outcomes, except for explicitly documented data-quality corrections.

## 1. Event Inclusion Workflow

## Step 1. Identify Candidate Events

### Procedure

Search for semiconductor-related geopolitical policy events involving:

- State support.
- Strategic industrial policy.
- Semiconductor subsidies.
- Public funding or preliminary funding terms.
- State-backed fab or capacity investment.
- Export controls or Entity List restrictions used as threat-dominant contrast events.

### Rationale

The theory concerns state-backed opportunity in strategically important sectors. Events must therefore involve both geopolitical competition and semiconductor strategic relevance.

### Potential Ambiguity

Some events may be ordinary industrial policy rather than geopolitical competition.

### Dispute Resolution

Include the event only if official sources or pre-event policy context connect it to national security, supply-chain resilience, technological competition, China-related competition, defense relevance, or strategic industrial capacity. If the link is weak, code `geopolitical_competition_link = 1` and flag for review.

## Step 2. Apply Inclusion Criteria

### Procedure

An event is included if all conditions are met:

1. It has an identifiable public announcement date.
2. It concerns semiconductors or semiconductor-linked strategic technology.
3. It is connected to geopolitical competition, national security, supply-chain security, or strategic industrial policy.
4. It includes either credible state support or a clear threat-dominant contrast.
5. Relevant public firms, ETFs, or indices can be identified before observing returns.

### Rationale

These conditions keep the project aligned with the frozen theory and avoid returning to broad geopolitical-risk analysis.

### Potential Ambiguity

Some strategic-policy events involve multiple sectors, such as AI, quantum, defense, and semiconductors.

### Dispute Resolution

Include only if semiconductors or semiconductor-linked infrastructure are a central component of the event. If semiconductors are peripheral, exclude or reserve for future expansion.

## Step 3. Assign Event Class

### Procedure

Classify each included event as one of:

- `support`: direct or named state support.
- `broad_policy`: legislation, program authorization, or broad eligibility.
- `threat_contrast`: export control, Entity List, restriction, or retaliation without direct support.
- `mixed`: event contains both meaningful support and restriction.

### Rationale

The dissertation tests whether state-support events differ from threat-dominant geopolitical events.

### Potential Ambiguity

Many events are mixed. For example, an industrial-policy law may include both support and guardrails.

### Dispute Resolution

Classify by the dominant announcement content. If no dominant content exists, code `mixed` and treat the event as weaker evidence in the main analysis.

## 2. Event Exclusion Workflow

## Step 1. Record All Candidate Events

### Procedure

Every candidate event considered must be recorded in an event-screening log, including excluded events.

Minimum fields:

- candidate_event_name
- candidate_date
- source_url
- initial_reason_considered
- inclusion_decision
- exclusion_reason if excluded
- reviewer_initials
- decision_date

### Rationale

A transparent exclusion log protects against cherry-picking.

### Potential Ambiguity

Researchers may disagree about whether an event was ever seriously considered.

### Dispute Resolution

If a source is opened and assessed for possible inclusion, the candidate must be logged.

## Step 2. Apply Exclusion Criteria

### Procedure

Exclude events if any condition applies:

- No identifiable announcement date.
- No semiconductor or semiconductor-linked relevance.
- No geopolitical, strategic, security, or supply-chain competition link.
- Pure rhetoric without policy instrument.
- No identifiable public-market assets.
- Event primarily concerns firm earnings rather than policy.
- Event selected only because market movement is already known.
- Event is too bundled to classify even as `mixed`.

### Rationale

The design requires policy events that can be dated, coded, linked, and audited before market outcomes.

### Potential Ambiguity

An event may be important but too anticipated or too broad.

### Dispute Resolution

Do not exclude solely because an event is anticipated. Include it but code high `anticipation_level`. Exclude only if the event date cannot plausibly represent any public information release.

## Step 3. Preserve Exclusion Notes

### Procedure

Every excluded event receives a one- to three-sentence explanation.

### Rationale

Exclusion notes allow a reviewer to judge whether the dataset was narrowed legitimately.

### Potential Ambiguity

Researchers may write vague exclusions such as "not relevant."

### Dispute Resolution

Exclusion notes must identify the failed criterion: date, scope, source, market asset, policy instrument, or excessive bundling.

## 3. Event Dating Rules

## Rule 1. Use the First Public, Authoritative Announcement Date

### Procedure

The primary event date is the first date on which the policy action or support announcement became publicly available through an official source or highly reliable public report.

### Rationale

Event studies require the date when investors could plausibly update expectations.

### Potential Ambiguity

Official publication may occur after the market first learns through reports, leaks, votes, or company filings.

### Dispute Resolution

Use this hierarchy:

1. Official announcement date if not clearly preceded by market-moving public information.
2. Company filing date if the firm discloses the policy before official publication.
3. Legislative passage date if market-relevant support becomes legally credible before signing.
4. Major credible news report date only if it clearly precedes official announcement and contains the substantive information.

Record all alternative dates in `coding_notes`.

## Rule 2. Handle After-Hours Announcements Transparently

### Procedure

If an event occurs after market close, keep the calendar event date but flag timing. In analysis, CAR [-1,+1] is preferred over event-day return.

### Rationale

The market may react on the next trading day.

### Potential Ambiguity

The exact release time may be unavailable.

### Dispute Resolution

If release time cannot be verified, set `date_timing_certainty = low` in notes and rely on CAR [-1,+1] rather than event-day return.

## Rule 3. Treat Legislative Events Carefully

### Procedure

For legislation, record multiple possible dates:

- introduction or proposal
- major vote or passage
- final passage
- signing
- implementation or named award

Designate one primary date based on when the market-relevant support became most credible.

### Rationale

Legislation is often anticipated. Signing dates are rarely clean shocks.

### Potential Ambiguity

Researchers may prefer different legislative milestones.

### Dispute Resolution

For the main analysis, favor named awards or preliminary funding terms over broad signing dates. Legislative signing events can remain in the dataset but should be marked high anticipation and interpreted cautiously.

## 4. Beneficiary Identification Rules

## Rule 1. Named Beneficiary

### Procedure

Code an asset as `named_beneficiary` only if the firm, facility, parent company, or publicly traded entity is explicitly named in the support announcement.

### Rationale

Named beneficiaries provide the cleanest test of the State Support mechanism.

### Potential Ambiguity

An announcement may name a subsidiary, joint venture, or facility rather than the public parent.

### Dispute Resolution

Link to the public parent only if ownership/control is clear and economically meaningful. Document the ownership link in `pre_outcome_link_notes`.

## Rule 2. Eligible Beneficiary

### Procedure

Code an asset as `eligible_beneficiary` if the policy clearly applies to a defined class of firms and the asset belongs to that class, even if not named.

### Rationale

Some support policies create expectations for eligible firms before awards are named.

### Potential Ambiguity

Eligibility may be broad or uncertain.

### Dispute Resolution

If eligibility is plausible but not explicit, code as `sector_peer`, not `eligible_beneficiary`. Eligibility requires direct policy criteria or official program language.

## Rule 3. Threat-Exposed Firm

### Procedure

Code an asset as `threat_exposed` if the event plausibly harms the firm through lost market access, restricted customers, controlled products, input disruption, or compliance burden.

### Rationale

Threat-exposed firms are needed to test the negative pathway and contrast state-support events.

### Potential Ambiguity

Many firms have indirect China or supply-chain exposure.

### Dispute Resolution

Require a clear product, market, customer, or supply-chain connection. Do not classify broad exposure as threat-exposed without a documented basis.

## Rule 4. Sector Peer

### Procedure

Code an asset as `sector_peer` if it belongs to the same semiconductor subsector or relevant comparison group but is not named, clearly eligible, directly threatened, or a substitute.

### Rationale

Peers provide a comparison against sector-wide movement.

### Potential Ambiguity

Subsector boundaries are fuzzy.

### Dispute Resolution

Use broad categories consistently: AI chips, foundry, memory, equipment, broad semiconductor ETF. If unsure, use broader semiconductor peer status rather than specific subsector peer status.

## Rule 5. Substitute

### Procedure

Code an asset as `substitute` only if the event plausibly redirects demand from a restricted or disadvantaged actor to the asset.

### Rationale

Substitution is a secondary pathway and should not be over-coded.

### Potential Ambiguity

Many firms could theoretically benefit from a rival's restriction.

### Dispute Resolution

Substitute coding requires identifiable product overlap, customer overlap, or market-position overlap. If the substitute logic is speculative, code link_strength no higher than 1.

## 5. Event-to-Firm Linking Protocol

## Step 1. Create Initial Asset Universe

### Procedure

Before event-level linking, create a fixed asset universe containing:

- broad benchmarks
- semiconductor benchmark assets
- likely named beneficiaries
- semiconductor sector peers
- possible threat-exposed firms
- possible substitutes

### Rationale

Predefining the asset universe reduces ex post selection.

### Potential Ambiguity

Newly discovered named beneficiaries may not be in the initial universe.

### Dispute Resolution

Add new assets only if they are named in an included event or required as a benchmark. Record the addition date and reason.

## Step 2. Link Assets to Each Event

### Procedure

For every event, assign relevant assets to exposure roles:

- named_beneficiary
- eligible_beneficiary
- sector_peer
- threat_exposed
- substitute
- benchmark

### Rationale

The theory predicts cross-sectional differences within event windows.

### Potential Ambiguity

An asset can plausibly fit multiple roles.

### Dispute Resolution

Use priority order:

1. named_beneficiary
2. threat_exposed
3. eligible_beneficiary
4. substitute
5. sector_peer
6. benchmark

If dual roles are substantively important, record the secondary role in notes.

## Step 3. Assign Expected Direction

### Procedure

Before observing returns, assign expected market direction:

- positive
- negative
- mixed
- neutral
- ambiguous

### Rationale

Expected direction creates an ex ante prediction that can be falsified.

### Potential Ambiguity

Mixed events may create both support and threat for the same firm.

### Dispute Resolution

Use `mixed` if both positive and negative channels are strong. Use `ambiguous` if evidence is insufficient to make a directional prediction.

## 6. Source Hierarchy

## Source Priority

Use sources in this order:

1. Official government announcement, agency release, or legal text.
2. Official company filing or company press release.
3. Official legislative record.
4. Regulator notice or public rulemaking document.
5. Major wire service or reputable financial press for timing or pre-official reports.
6. Secondary commentary only for background, not for coding core variables.

## Rationale

Core coding should be based on sources available at the event date and least likely to reflect later market narratives.

## Potential Ambiguity

Official sources may be vague, while news reports may contain more operational detail.

## Dispute Resolution

Use official sources for event existence and core coding. Use reputable same-day or pre-event news only to clarify timing, affected firms, or policy details. Do not use post-event market reaction commentary to code mechanism variables.

## 7. Coding Workflow

## Step 1. Independent Coding

### Procedure

At least two coders independently code:

- event inclusion
- event date
- event type
- strategic_importance
- state_support
- support_directness
- support_credibility
- threat_signal
- substitution_reallocation
- anticipation_level
- event-asset links
- expected_direction

### Rationale

Independent coding is necessary because several variables require judgment.

### Potential Ambiguity

Coders may interpret state support or strategic importance differently.

### Dispute Resolution

Use the coding manual anchors. If disagreement remains, record both original scores and adjudicated final score.

## Step 2. Intercoder Reliability Check

### Procedure

Before market returns are collected, calculate agreement on core ordinal variables and binary collapsed versions.

Core variables:

- strategic_importance
- state_support
- support_directness
- support_credibility
- threat_signal
- exposure_role
- expected_direction

### Rationale

The project depends on ex ante coding credibility.

### Potential Ambiguity

Small samples make reliability statistics unstable.

### Dispute Resolution

Report both formal reliability statistics and disagreement tables. If reliability is poor, collapse ordinal scales into binary or low/high categories before analysis.

## Step 3. Adjudication

### Procedure

A senior coder or supervisor resolves disagreements using only allowed sources.

### Rationale

Final analysis requires one frozen coding value per variable.

### Potential Ambiguity

Adjudication may introduce supervisor bias.

### Dispute Resolution

Preserve original coder values, final adjudicated value, adjudicator name, and adjudication reason.

## Step 4. Freeze Pre-Outcome Files

### Procedure

Before collecting or calculating returns, freeze:

- `events.csv`
- `assets.csv`
- `event_asset_links.csv`
- event-screening log
- source archive or source list
- coding disagreement log

### Rationale

This is the core anti-hindsight safeguard.

### Potential Ambiguity

Minor typo corrections may be needed later.

### Dispute Resolution

Post-freeze corrections are allowed only through a change log. Corrections must specify whether they affect coding, linking, or only formatting.

## 8. Documentation Requirements

## Required Documents

The project folder should include:

- theory freeze document
- research design freeze document
- dataset architecture freeze document
- research protocol freeze document
- coding manual
- event-screening log
- included-events table
- excluded-events table
- source list
- source archive notes
- coder assignment sheet
- coder disagreement log
- adjudication log
- change log
- final replication notes

## Rationale

The project is vulnerable to hindsight and cherry-picking. Documentation is not administrative overhead; it is part of the research design.

## Potential Ambiguity

Some documents may overlap.

## Dispute Resolution

Do not merge documents if merging reduces auditability. Redundancy is acceptable when it helps a reviewer trace decisions.

## 9. Audit Trail Requirements

## Required Audit Fields

Every event decision must preserve:

- who coded it
- when it was coded
- source used
- inclusion decision
- event date decision
- beneficiary-link decision
- original coder scores
- final adjudicated scores
- reason for any change
- whether change occurred before or after return collection

## Rationale

A reviewer must be able to distinguish ex ante theory-driven decisions from ex post corrections.

## Potential Ambiguity

Researchers may not know when a coding change becomes substantively important.

## Dispute Resolution

Treat any change to event inclusion, event date, exposure role, expected direction, or mechanism variable as substantive. Record it in the change log.

## 10. Replication Standards

## Minimum Replication Package

A replication package should include:

- frozen event list
- frozen asset list
- frozen event-asset link table
- source URLs and access dates
- coding manual
- protocol
- coder and adjudication logs
- market data source description
- abnormal-return construction notes
- final analysis table
- explanation of excluded events

## Rationale

Another researcher should be able to reconstruct the event selection and coding even if they use a different market-data provider.

## Potential Ambiguity

Some market data sources are proprietary.

## Dispute Resolution

If raw data cannot be shared, provide tickers, dates, return formulas, source name, download date, and enough metadata for another researcher to reproduce the pull from a licensed source.

## 11. Complete Research Protocol Freeze V1

## Frozen Workflow

1. Build candidate event list from official and reputable sources.
2. Log every candidate event considered.
3. Apply inclusion and exclusion criteria.
4. Assign event dates using source hierarchy and dating rules.
5. Code event-level variables independently.
6. Build fixed asset universe.
7. Link events to firms and benchmarks before observing returns.
8. Assign exposure roles and expected directions.
9. Conduct intercoder reliability checks.
10. Adjudicate disagreements and preserve original scores.
11. Freeze all pre-outcome files.
12. Only then collect market returns and calculate abnormal returns.
13. Flag earnings, macro, anticipation, and event-bundling issues.
14. Interpret results using the frozen falsification criteria.

## Frozen Inclusion Standard

An event enters the dataset only if it is semiconductor-relevant, policy-relevant, publicly dated, linked to geopolitical competition, and connected either to credible state support or threat-dominant contrast.

## Frozen Exclusion Standard

An event is excluded if it lacks a public date, lacks semiconductor relevance, lacks geopolitical/strategic relevance, lacks a policy instrument, lacks identifiable public-market assets, or cannot be classified even as a mixed event.

## Frozen Dating Standard

Use the first public authoritative announcement date, with alternative dates documented. For legislation, prioritize the date when support becomes market-credible; for named awards, use the award or preliminary terms announcement date.

## Frozen Beneficiary Standard

Named beneficiaries are firms explicitly named in official support announcements. Eligible beneficiaries require direct policy eligibility. Sector peers and substitutes must be assigned before returns are observed.

## Frozen Linking Standard

Event-to-firm links must be justified by named policy text, eligibility criteria, direct restriction, supply-chain role, substitute logic, or benchmark role. Link notes must be written before return calculation.

## Frozen Source Standard

Official government and legal sources dominate. Company filings are used for firm-specific disclosures. Reputable news can clarify timing but cannot replace official evidence for core coding when official evidence exists.

## Frozen Coding Standard

At least two coders independently code core variables. Disagreements are logged, adjudicated, and preserved. Poor reliability requires collapsing categories or revising the coding manual before analysis.

## Frozen Audit Standard

Any post-freeze change to event inclusion, event date, exposure role, expected direction, or mechanism coding must be recorded as substantive. No undocumented post-outcome recoding is allowed.

## Frozen Replication Standard

A replicating researcher should be able to reproduce:

- which events were considered
- why each was included or excluded
- how each event was dated
- which assets were linked
- why each asset was linked
- how each mechanism variable was coded
- when coding was frozen
- how market outcomes were calculated

## Final Transparency Position

The central risk in this project is not technical complexity. It is hindsight bias. The protocol therefore prioritizes freezing the event universe, coding, and event-firm links before market returns are observed. If that rule is violated, the project loses much of its credibility as a test of the State Support mechanism.
