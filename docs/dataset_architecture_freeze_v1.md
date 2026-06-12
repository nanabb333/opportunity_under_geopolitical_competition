# Dataset Architecture Freeze V1

## Purpose

This document freezes the dataset architecture required to test the dissertation theory:

> Geopolitical competition generates positive market reactions when strategically important firms or sectors are expected to receive credible state support that improves future cash flows or reduces downside risk.

This is an architecture document, not a dataset. It specifies the unit of analysis, table structure, linking logic, variables, coding rules, minimum viable dataset, future expansion path, and measurement risks.

## Core Empirical Logic

The project requires three linked datasets:

1. **Event dataset:** policy events involving semiconductor state support or threat-dominant geopolitical restrictions.
2. **Firm/asset dataset:** firms, ETFs, and indices used to observe market reactions.
3. **Event-firm market dataset:** event-firm observations containing returns, abnormal returns, and mechanism exposure.

The master table for analysis should be the **event-firm** table.

## 1. Unit of Analysis

## Primary Unit: Event-Firm

The primary unit of analysis is:

> firm or asset *i* around event *e*

Each row asks:

> Did asset *i* experience a positive market reaction around event *e*, conditional on the type of event and the firm's relationship to state support?

This unit is necessary because the theory is cross-sectional. Geopolitical competition does not affect all firms equally. Some firms are threatened, some are supported, some are indirect peers, and some are broad benchmarks.

## Secondary Units

### Event

Used to code state support, threat dominance, strategic framing, event type, surprise, and source information.

### Asset-Day

Used to store daily returns needed to calculate event-window outcomes.

### Event-Asset Group

Used for interpretation: named beneficiaries, sector peers, broad benchmarks, and threat-exposed firms.

## Reviewer Concern

The event-firm unit may inflate observations because multiple firms are attached to the same event.

## Defense

The dissertation should avoid pretending event-firm rows are fully independent. Main results should be descriptive and event-clustered where possible. The event-firm unit is still necessary because the core theory predicts different reactions within the same event.

## 2. Dataset Structure

## Table A: events.csv

One row per event.

Purpose:

- Define event universe.
- Freeze event dates.
- Code mechanism-relevant event characteristics before observing returns.

Recommended fields:

| Variable | Type | Description |
|---|---|---|
| event_id | string | Unique event identifier |
| event_date | date | Main announcement date |
| event_name | string | Short event label |
| event_type | categorical | support, broad_policy, threat_contrast, mixed |
| policy_subtype | categorical | subsidy_award, legislation, fab_investment, export_control, entity_list, retaliation |
| country_or_region | string | Initiating country or region |
| sector | string | Sector affected; first dataset should mainly be semiconductors |
| geopolitical_competition_link | ordinal 0-3 | Strength of connection to geopolitical competition |
| strategic_importance | ordinal 0-3 | Strategic relevance of the sector/event |
| state_support | ordinal 0-3 | Strength and directness of state support |
| state_support_type | categorical/list | subsidy, procurement, tax_credit, loan, regulation, protection, financing, industrial_policy |
| support_directness | ordinal 0-3 | Whether support is vague, broad, eligible, or named |
| support_credibility | ordinal 0-3 | Whether support is funded, official, specific, and likely to be implemented |
| threat_signal | ordinal 0-3 | Degree of restriction, uncertainty, lost access, or compliance burden |
| opportunity_signal | ordinal 0-3 | Degree of expected support, protection, or opportunity |
| substitution_reallocation | ordinal 0-3 | Degree of substitution or supply-chain reallocation logic |
| anticipation_level | ordinal 0-3 | Degree to which event was likely priced before announcement |
| confound_flag_event | binary | Major event-level confound present |
| source_url | string | Primary source URL |
| coding_notes | text | Event-specific coding rationale |

## Table B: assets.csv

One row per firm, ETF, or index.

Purpose:

- Define analysis assets before observing event-window returns.
- Separate named beneficiaries, peers, benchmarks, and threat-exposed firms.

Recommended fields:

| Variable | Type | Description |
|---|---|---|
| asset_id | string | Unique asset identifier |
| ticker | string | Tradable ticker or index symbol |
| asset_name | string | Firm, ETF, or index name |
| asset_type | categorical | firm, ETF, index |
| country | string | Primary listing or headquarters country |
| sector | string | Main sector |
| subsector | string | Foundry, memory, equipment, AI chips, defense semiconductors, etc. |
| benchmark_role | categorical | none, broad_market, tech_benchmark, sector_benchmark |
| strategic_asset | binary | Whether asset belongs to strategically relevant semiconductor universe |
| public_market_available | binary | Whether daily price data are available |
| notes | text | Listing, ADR, or comparability notes |

## Table C: event_asset_links.csv

One row per event-asset relationship.

Purpose:

- Link events to assets before observing returns.
- Define expected exposure category.

Recommended fields:

| Variable | Type | Description |
|---|---|---|
| event_id | string | Links to events.csv |
| asset_id | string | Links to assets.csv |
| exposure_role | categorical | named_beneficiary, eligible_beneficiary, sector_peer, threat_exposed, substitute, benchmark |
| expected_direction | categorical | positive, negative, mixed, neutral, ambiguous |
| link_strength | ordinal 0-3 | Strength of event-asset connection |
| link_basis | categorical/list | named_in_policy, sector_eligibility, supply_chain_role, benchmark, direct_restriction, substitute_logic |
| pre_outcome_link_notes | text | Why asset is linked before returns are observed |

## Table D: market_returns.csv

One row per asset-day.

Purpose:

- Store daily price and return data used to calculate event-window outcomes.

Recommended fields:

| Variable | Type | Description |
|---|---|---|
| asset_id | string | Links to assets.csv |
| trade_date | date | Trading date |
| close_price_adjusted | numeric | Adjusted close |
| daily_return | numeric | Daily return |
| data_source | string | Market data source |
| trading_calendar_notes | text | ADR, holiday, or non-US market notes |

## Table E: event_firm_returns.csv

One row per event-asset observation.

Purpose:

- Main analysis table.

Recommended fields:

| Variable | Type | Description |
|---|---|---|
| event_id | string | Links to events.csv |
| asset_id | string | Links to assets.csv |
| exposure_role | categorical | Copied from link table |
| event_day_return | numeric | Raw event-day return |
| ar_market_event_day | numeric | Event-day return minus broad market benchmark |
| ar_sector_event_day | numeric | Event-day return minus sector benchmark |
| car_market_m1_p1 | numeric | CAR [-1,+1] minus broad market benchmark |
| car_sector_m1_p1 | numeric | CAR [-1,+1] minus sector benchmark |
| car_market_m3_p3 | numeric | CAR [-3,+3] minus broad market benchmark |
| car_sector_m3_p3 | numeric | CAR [-3,+3] minus sector benchmark |
| car_market_m7_p7 | numeric | CAR [-7,+7], descriptive only |
| earnings_conflict | binary | Firm earnings inside event window |
| macro_conflict | binary | Major macro/Fed event inside event window |
| data_quality_flag | categorical | clean, caution, weak, exclude |
| interpretation_result | categorical | supportive, contradictory, inconclusive |

## 3. Market Dataset Structure

## Required Market Assets

The minimum market universe should include:

- Broad benchmarks: SPY, QQQ.
- Semiconductor benchmark: SMH, and SOX if available.
- Named semiconductor firms: INTC, TSM, MU, Samsung if feasible, ASML, AMD, NVDA.
- Semiconductor equipment peers: AMAT, LRCX, KLAC.
- Optional threat-contrast assets: KWEB or CQQQ for China technology exposure.

## Strongest Design Choice

Use two abnormal-return adjustments:

- Broad market adjustment using SPY.
- Sector adjustment using SMH or SOX.

The sector-adjusted return is more important for mechanism testing. A firm that rises only because the entire semiconductor sector rose is weak evidence for state support.

## Reviewer Concern

ETF benchmarks may contain the treated firm, creating mechanical contamination.

## Defense

Report both SPY-adjusted and semiconductor-benchmark-adjusted returns. Acknowledge that sector benchmarks are imperfect but necessary to separate beneficiary-specific moves from sector-wide moves. For large constituents, supplement with peer comparisons where feasible.

## 4. Event-to-Firm Linking Strategy

## Linking Principles

Assets must be linked to events before observing returns.

Each linked asset must fall into one of these roles:

- **named_beneficiary:** firm explicitly named in support announcement.
- **eligible_beneficiary:** firm clearly eligible under announced policy but not named.
- **sector_peer:** firm in same sector but not directly named or clearly eligible.
- **threat_exposed:** firm plausibly harmed by restriction, lost market access, or compliance burden.
- **substitute:** firm plausibly benefits from demand shifting away from restricted actor.
- **benchmark:** ETF or index used for comparison.

## Strongest Design Choice

The main test should prioritize named_beneficiary observations because they have the cleanest event-firm link.

## Reviewer Concern

Named beneficiaries are selected by the state, not randomly assigned. They may be chosen because they are strong, politically connected, weak, or already expected to invest.

## Defense

The design does not claim random assignment. It tests whether markets interpret state selection and support as positive information. Include sector peers and benchmarks to show whether named beneficiaries react differently from comparable assets.

## 5. Mechanism Operationalization

The frozen mechanism is:

> Geopolitical competition -> Strategic Importance -> Credible State Support -> Investor Interpretation -> Positive Market Reaction

The dataset operationalizes this through four blocks:

1. Event context: geopolitical_competition_link and strategic_importance.
2. Mechanism: state_support, support_directness, support_credibility.
3. Exposure: exposure_role and link_strength.
4. Outcome: abnormal returns and CARs.

The mechanism is supported if high state-support events generate positive abnormal returns for named or clearly eligible beneficiaries, especially relative to sector peers and benchmarks.

## 6. Variable Construction and Reviewer Defense

## Event-Level Variables

| Variable | Why It Exists Theoretically | How It Is Measured | Reviewer Concerns | Defense |
|---|---|---|---|---|
| event_id | Required to link event tables without ambiguity. | Unique code such as E001. | None substantive. | Use stable identifiers and preserve codebook. |
| event_date | Defines timing of market reaction. | Official announcement date; if after market close, note timing. | True information date may differ due to leaks or anticipation. | Record alternative dates in notes; use short windows and flag anticipation. |
| event_name | Provides transparent event identity. | Short descriptive label. | Labels can bias interpretation. | Keep labels descriptive, not evaluative. |
| event_type | Separates support events from threat contrasts. | Coded as support, broad_policy, threat_contrast, mixed. | Categories may be too coarse. | Use policy_subtype and notes for granularity. |
| policy_subtype | Identifies concrete policy instrument. | subsidy_award, legislation, fab_investment, export_control, entity_list, retaliation. | Subtypes may overlap. | Allow primary subtype plus notes; do not force false separation for bundled events. |
| country_or_region | Identifies state actor providing support or imposing restriction. | Country or region from source. | Multi-country events complicate coding. | Use initiating actor as primary; note secondary actors. |
| sector | Freezes sector scope. | Semiconductor, semiconductor equipment, AI chips, memory, foundry, etc. | Sector definitions may be inconsistent. | Use simple, documented sector categories. |
| geopolitical_competition_link | Ensures event belongs to theory scope. | 0 no link, 1 weak, 2 clear, 3 explicit geopolitical/national-security framing. | Could be subjective. | Use official text and pre-event policy context; preserve notes. |
| strategic_importance | Captures theory scope condition. | 0 none, 1 low, 2 clear, 3 central strategic sector. | Risk of circularity. | Code before returns using policy framing and sector role, not market performance. |
| state_support | Core mechanism variable. | 0 none, 1 indirect, 2 broad/moderate, 3 direct/named support. | "Support" may include too many things. | Keep ordinal anchors strict; separate support_type, directness, and credibility. |
| state_support_type | Identifies form of support. | Categorical/list: subsidy, loan, tax credit, procurement, regulation, protection, financing, industrial_policy. | Multiple types can occur. | Allow multiple values; analysis can collapse to support present/intensity. |
| support_directness | Distinguishes named awards from broad eligibility. | 0 none, 1 rhetoric, 2 eligible group, 3 named firm/facility. | Named support may be anticipated. | Pair with anticipation_level and event-date notes. |
| support_credibility | Captures whether support is likely market-relevant. | 0 none, 1 vague, 2 official but broad, 3 funded/specific/official. | Credibility is subjective. | Code based on official status, funding specificity, and legal/administrative concreteness. |
| threat_signal | Captures negative pathway. | 0 none, 1 weak, 2 moderate, 3 direct restriction/threat. | Threat and support may coexist. | Permit both high threat and high support; theory predicts mixed reactions. |
| opportunity_signal | Captures event-level opportunity content. | 0 none, 1 weak, 2 moderate, 3 direct expected upside. | May duplicate state_support. | Use as descriptive; core mechanism tests should prioritize state_support. |
| substitution_reallocation | Captures secondary mechanism. | 0 none, 1 weak, 2 plausible, 3 strong/explicit. | Could introduce new mechanism creep. | Use only as secondary moderator, not central theory. |
| anticipation_level | Handles expectedness. | 0 surprise, 1 low anticipation, 2 debated/partly expected, 3 highly anticipated. | Hard to know expectations. | Use pre-event news/policy timeline; report sensitivity excluding high-anticipation events. |
| confound_flag_event | Protects internal validity. | 1 if major same-day policy, macro, or sector event exists. | Confounds are hard to exhaustively identify. | Flag obvious confounds; do not claim perfect control. |
| source_url | Allows auditability. | Official or primary source URL where possible. | Sources may change. | Archive or record access date in notes if possible. |
| coding_notes | Preserves reasoning. | Short explanation. | Notes may be inconsistent. | Use structured notes: timing, support, threat, affected assets, caveats. |

## Asset-Level Variables

| Variable | Why It Exists Theoretically | How It Is Measured | Reviewer Concerns | Defense |
|---|---|---|---|---|
| asset_id | Required for clean linkage. | Unique code such as A001. | None substantive. | Stable identifier. |
| ticker | Identifies market asset. | Market ticker. | ADRs and foreign listings may differ. | Note listing type and use consistent trading calendar. |
| asset_name | Interpretable asset label. | Official firm/ETF/index name. | None substantive. | Keep updated in codebook. |
| asset_type | Separates firms, ETFs, and indices. | firm, ETF, index. | ETFs are not firms. | Use ETFs only for benchmarks or sector reactions, not firm-specific claims. |
| country | Captures listing/headquarters context. | Headquarters or primary listing country. | Multinationals complicate country assignment. | Use primary headquarters/listing; note exceptions. |
| sector | Places asset in scope. | Semiconductor, equipment, memory, foundry, broad market, etc. | Sector boundaries are fuzzy. | Use simple categories relevant to design. |
| subsector | Enables peer comparison. | Foundry, equipment, memory, AI chips, logic, broad ETF. | May overfit small sample. | Use descriptively; primary analysis can collapse categories. |
| benchmark_role | Identifies benchmark assets. | broad_market, tech_benchmark, sector_benchmark, none. | Benchmark choice affects results. | Report multiple benchmarks. |
| strategic_asset | Asset-level scope marker. | 1 if asset is in strategic semiconductor universe. | Could be tautological. | Based on sector role before outcomes, not returns. |
| public_market_available | Ensures feasibility. | 1 if daily price data are available. | Excludes private beneficiaries. | Acknowledge public-market selection limitation. |
| notes | Documents listing and comparability issues. | Text. | Inconsistent notes. | Keep short and standardized. |

## Event-Asset Link Variables

| Variable | Why It Exists Theoretically | How It Is Measured | Reviewer Concerns | Defense |
|---|---|---|---|---|
| exposure_role | Central cross-sectional exposure concept. | named_beneficiary, eligible_beneficiary, sector_peer, threat_exposed, substitute, benchmark. | Role assignment may be subjective. | Assign before returns using source documents and predefined rules. |
| expected_direction | Records ex ante prediction. | positive, negative, mixed, neutral, ambiguous. | Can become hindsight-biased. | Freeze before return calculation and preserve original coding. |
| link_strength | Captures directness of event-firm relationship. | 0 none, 1 weak, 2 moderate, 3 direct/named. | May be subjective. | Anchor 3 to named firms or direct restrictions; use notes. |
| link_basis | Explains why asset is linked. | named_in_policy, sector_eligibility, supply_chain_role, benchmark, direct_restriction, substitute_logic. | Multiple bases possible. | Allow multiple bases; prioritize named_in_policy for main tests. |
| pre_outcome_link_notes | Anti-hindsight audit trail. | Text written before returns. | Notes may be rationalizations. | Timestamp or freeze the link table before market data collection. |

## Market and Outcome Variables

| Variable | Why It Exists Theoretically | How It Is Measured | Reviewer Concerns | Defense |
|---|---|---|---|---|
| daily_return | Input for market reaction. | Percent/log return from adjusted close. | Different return formulas. | Use one formula consistently; report choice. |
| event_day_return | Immediate market reaction. | Asset return on event date. | Event may occur after close. | Use CAR [-1,+1] as primary if timing uncertain. |
| ar_market_event_day | Controls broad market movement. | Asset return minus SPY return. | SPY may be insufficient for tech firms. | Also use QQQ and sector adjustment. |
| ar_sector_event_day | Controls semiconductor-sector movement. | Asset return minus SMH or SOX return. | Benchmark may include treated firm. | Use as conservative benchmark; compare with peers. |
| car_market_m1_p1 | Primary broad-market-adjusted outcome. | Sum abnormal returns from t-1 to t+1. | Three-day window may include confounds. | Still primary because policy timing may be uncertain; flag confounds. |
| car_sector_m1_p1 | Primary mechanism outcome. | Sum sector-adjusted returns from t-1 to t+1. | Sector benchmark contamination. | Stronger than broad benchmark; report alongside raw and SPY-adjusted returns. |
| car_market_m3_p3 | Secondary broader window. | Sum broad-adjusted returns from t-3 to t+3. | More confounding. | Use robustness only. |
| car_sector_m3_p3 | Secondary sector-adjusted window. | Sum sector-adjusted returns from t-3 to t+3. | More confounding. | Use robustness only. |
| car_market_m7_p7 | Descriptive slow-reaction window. | Sum broad-adjusted returns from t-7 to t+7. | Too confounded for causal claims. | Label descriptive only. |
| earnings_conflict | Controls firm-news confounding. | 1 if firm earnings occur inside event window. | Earnings calendars can be incomplete. | Flag obvious cases; sensitivity excluding them. |
| macro_conflict | Controls macro-news confounding. | 1 if major Fed/CPI/jobs event occurs in window. | Macro confounds can be missed. | Use major published macro calendar; discuss limitations. |
| data_quality_flag | Prevents overinterpretation. | clean, caution, weak, exclude. | Could be used to drop inconvenient observations. | Assign before analysis or based on documented data issues only. |
| interpretation_result | Proposal-defense summary. | supportive, contradictory, inconclusive after returns. | Subjective post-outcome label. | Use only for summary, not as independent variable. |

## 7. Coding Rules

## Pre-Outcome Rule

All event variables, asset links, exposure roles, expected directions, and mechanism coding must be completed before market returns are calculated.

## No-Hindsight Rule

Coders may not use:

- Stock returns.
- Analyst commentary after the event.
- Later subsidy implementation outcomes.
- Later firm performance.
- Later policy revisions, unless coding a later event separately.

## Directness Rule

Named firm support receives stronger coding than broad sector eligibility.

## Credibility Rule

Official, funded, firm-specific, or legally enacted support receives stronger coding than speeches, strategy documents, or vague policy goals.

## Contrast Rule

Threat-dominant events should remain in the dataset even if they do not produce positive returns. They are needed to test whether state support differs from restriction-only geopolitical shocks.

## Confound Rule

Confounded observations are flagged, not automatically deleted. Deletion requires a documented rule such as missing market data or earnings exactly overlapping the event window.

## 8. Minimum Viable Dissertation Dataset

## Minimum Event Count

For a master's dissertation, the minimum viable event universe is:

- 10-15 semiconductor state-support events.
- 5-8 threat-dominant semiconductor contrast events.
- Total: approximately 15-23 events.

This is enough for descriptive event-study evidence and simple comparisons. It is not enough for complex causal modeling.

## Minimum Asset Universe

Required:

- SPY.
- QQQ.
- SMH or SOX.
- INTC.
- TSM.
- MU.
- ASML.
- AMAT.
- LRCX.
- KLAC.
- NVDA.
- AMD.

Optional:

- Samsung listing if feasible.
- CQQQ or KWEB as China-tech contrast.
- SOXX as alternate semiconductor ETF.

## Minimum Analysis Table

The final event_firm_returns table should include:

- Each named beneficiary for each support event.
- At least three sector peers for each event where feasible.
- SPY, QQQ, and SMH/SOX for every event.
- Threat-exposed firms for contrast events.

## Minimum Claims Allowed

The minimum dataset can support:

- Whether named beneficiaries outperform broad and sector benchmarks around state-support events.
- Whether direct support events differ from threat-dominant events.
- Whether results are consistent with the State Support mechanism.

It cannot support:

- Strong causal proof.
- Welfare claims.
- Long-run policy success.
- General claims about all geopolitical competition.

## 9. Expansion Path for PhD-Level Research

## Expansion 1: Cross-Sector Comparison

Add defense, energy security, critical minerals, telecom infrastructure, and AI infrastructure.

Purpose:

- Test external validity.
- Determine whether state support travels beyond semiconductors.

## Expansion 2: Cross-Country State Capacity

Add US, EU, Japan, South Korea, Taiwan, China, and selected emerging markets.

Purpose:

- Test whether credible state support depends on fiscal capacity, industrial-policy institutions, and alliance position.

## Expansion 3: Text-Based Investor Interpretation

Add earnings calls, firm releases, financial news, and analyst summaries.

Purpose:

- Test whether investors and firms explicitly interpret state support as opportunity.

## Expansion 4: Longer-Horizon Performance

Add revenue forecasts, analyst revisions, capex changes, contract awards, and valuation multiples.

Purpose:

- Test whether short-run market reactions correspond to durable expectations or only temporary excitement.

## Expansion 5: Network and Supply-Chain Exposure

Add supply-chain links, customer exposure, China revenue share, and procurement data.

Purpose:

- Improve identification of strategic exposure and substitution/reallocation pathways.

## 10. Potential Measurement Problems

## Problem 1: Anticipation

State support is often debated before announcement.

Risk:

- Event-window returns understate market reaction.

Response:

- Code anticipation_level.
- Prefer discrete firm-specific preliminary terms over broad legislative milestones.
- Use alternative event dates for legislation.

## Problem 2: Sector Cycle Confounding

Semiconductors move with AI demand, interest rates, capex cycles, and earnings.

Risk:

- Positive reactions may reflect sector rally, not state support.

Response:

- Use sector-adjusted returns.
- Compare named beneficiaries to peers.
- Treat broad sector movement as weak evidence.

## Problem 3: Benchmark Contamination

Sector ETFs include treated firms.

Risk:

- Sector-adjusted abnormal returns may understate beneficiary effects.

Response:

- Report multiple benchmarks.
- Use peer comparisons.
- Interpret sector-adjusted results conservatively.

## Problem 4: Public-Firm Selection Bias

Some beneficiaries are private, foreign-listed, or hard to trade.

Risk:

- Dataset observes only public-market reactions, not all economic opportunity.

Response:

- State that the dependent variable is public-market reaction.
- Do not infer total economic impact.

## Problem 5: State Support as Weakness Signal

Markets may read support as evidence a firm needs help.

Risk:

- Positive theory fails for distressed or underperforming firms.

Response:

- Treat negative beneficiary reactions as meaningful contradiction, not nuisance.
- Discuss support-as-weakness as rival interpretation.

## Problem 6: Event Bundling

Announcements may combine support, restrictions, strategy, and political rhetoric.

Risk:

- Mechanism cannot be isolated.

Response:

- Code event_type and policy_subtype carefully.
- Flag mixed events.
- Use direct named support events as strongest tests.

## Problem 7: Strategic Importance Circularity

Strategic importance might be inferred from state support.

Risk:

- The theory becomes tautological.

Response:

- Code strategic importance from pre-event sector role and policy context.
- Treat it as scope condition, not primary causal variable.

## Complete Dataset Architecture Freeze V1

## Frozen Empirical Architecture

The dissertation will use a relational dataset with five linked tables:

1. `events.csv`
2. `assets.csv`
3. `event_asset_links.csv`
4. `market_returns.csv`
5. `event_firm_returns.csv`

## Frozen Unit of Analysis

The main analytical unit is the event-firm observation.

## Frozen Mechanism Variables

Primary mechanism:

- state_support
- support_directness
- support_credibility

Scope condition:

- strategic_importance
- geopolitical_competition_link

Negative pathway:

- threat_signal

Secondary pathway:

- substitution_reallocation

Exposure linkage:

- exposure_role
- link_strength
- link_basis

## Frozen Outcome Variables

Primary:

- car_sector_m1_p1

Secondary:

- car_market_m1_p1
- ar_sector_event_day
- ar_market_event_day
- car_sector_m3_p3
- car_market_m3_p3

Descriptive only:

- car_market_m7_p7

## Frozen Comparison Strategy

Main comparison:

- Named state-support beneficiaries versus semiconductor sector benchmark and sector peers.

Secondary comparison:

- State-support events versus threat-dominant export-control events.

Robustness comparison:

- Broad-market-adjusted returns versus sector-adjusted returns.

## Frozen Minimum Viable Dataset

Minimum:

- 15-23 events.
- 10-15 state-support events.
- 5-8 threat-dominant contrast events.
- 10-12 core market assets.
- Event-firm links frozen before returns are calculated.

## Frozen Interpretation Standard

The State Support mechanism receives support only if:

- Named beneficiaries show positive abnormal returns around direct state-support events.
- Results hold relative to sector benchmarks or sector peers.
- Threat-dominant events do not produce the same pattern.
- Findings are not driven by one event or broad semiconductor rallies.

The mechanism is weakened if:

- Named beneficiaries do not outperform sector benchmarks.
- State-support events look no different from threat-dominant events.
- Positive results appear only in long, confounded windows.
- Strategic importance and state support cannot be coded independently of market outcomes.

## Final Methodological Position

This architecture is deliberately modest. It does not promise clean causal identification or universal external validity. It is designed to test whether the frozen theory has empirical traction in the most plausible master's-level setting: semiconductor state-support events under geopolitical competition.

If the mechanism fails in this architecture, the broader theory should be narrowed or abandoned. If it survives, the result should be interpreted as evidence of a plausible market-expectations mechanism, not proof that geopolitical competition is economically beneficial.
