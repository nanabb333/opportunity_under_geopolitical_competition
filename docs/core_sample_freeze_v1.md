# Core Sample Freeze V1

## Purpose

This document freezes the dissertation event universe. The objective is to define the final sample that best matches the theory, survives reviewer scrutiny, and maximizes identification quality.

Frozen theory:

> Geopolitical competition generates positive market reactions when strategically important firms or sectors are expected to receive credible state support that improves future cash flows or reduces downside risk.

Pilot finding:

> The project is operationalisable, but the clean empirical core is narrower than the original event inventory.

Therefore, the core sample should not include every geopolitical semiconductor event. It should focus on events where the mechanism is most observable: **credible, named, semiconductor-related state support with visible public-market beneficiaries**.

## Core Sample Logic

The dissertation should use a three-tier event structure:

1. **Main analysis:** direct named semiconductor state-support events.
2. **Secondary analysis:** broad support or implementation/reallocation events that fit the theory but have weaker identification.
3. **Contrast cases:** threat-dominant semiconductor geopolitical events without direct state support.

Events outside these categories should be excluded from the dissertation sample, even if substantively interesting.

## 1. Main Analysis Events

Main analysis events must satisfy all conditions:

- Semiconductor or semiconductor-linked strategic sector.
- Clear geopolitical, national-security, supply-chain, or strategic industrial-policy framing.
- Direct state support.
- Named beneficiary or clearly named public parent.
- Publicly dated announcement.
- Beneficiary visible in public markets.
- Support plausibly material enough to be market-relevant.

These are the events that best test the frozen State Support mechanism.

| Event | Date | Category | Primary Linked Beneficiary | Main Analysis Decision |
|---|---|---|---|---|
| Intel CHIPS Act preliminary terms announced | 2024-03-20 | Direct named support | INTC | Include |
| TSMC Arizona CHIPS Act preliminary terms announced | 2024-04-08 | Direct named support | TSM | Include |
| Samsung CHIPS Act preliminary terms announced | 2024-04-15 | Direct named support | Samsung | Include if market-data timing is feasible |
| Micron CHIPS Act preliminary agreement announced | 2024-04-25 | Direct named support | MU | Include |

## Intel CHIPS Act Preliminary Terms

### Theoretical Rationale

This is a direct test of the theory. Intel is strategically important to US semiconductor manufacturing capacity, and the event announces credible state support for a named public firm.

### Identification Rationale

The beneficiary is visible, named, and US-listed. The event is more discrete than CHIPS Act signing and less ambiguous than broad industrial-policy rhetoric.

### Likely Reviewer Objection

Intel's reaction may reflect firm-specific turnaround expectations, weakness, or the market's view of Intel's execution problems rather than state support.

### Defence

Use sector-adjusted returns against SMH/SOX and compare Intel to semiconductor peers. If Intel does not outperform sector benchmarks, the theory is weakened for this case.

## TSMC Arizona CHIPS Act Preliminary Terms

### Theoretical Rationale

This event captures state-backed support for strategically important foundry capacity in the United States. It links geopolitical supply-chain concerns to direct public support.

### Identification Rationale

TSMC is named, TSM is traded, and the event is specific. It is a cleaner support event than broad discussions of friend-shoring or Taiwan concentration risk.

### Likely Reviewer Objection

The announcement may only offset high US fab costs rather than create new upside.

### Defence

The theory explicitly allows state support to reduce downside risk. A positive reaction would support the mechanism; a weak or negative reaction would indicate that support was insufficient to offset cost concerns.

## Samsung CHIPS Act Preliminary Terms

### Theoretical Rationale

This event tests whether US state support for allied semiconductor capacity is interpreted as market opportunity beyond US-headquartered firms.

### Identification Rationale

Samsung is a named beneficiary and the support is direct. The case improves theoretical scope within the semiconductor sector.

### Likely Reviewer Objection

Foreign listing, time-zone differences, and market-data access complicate event-window measurement.

### Defence

Include only if the event can be matched to a reliable trading instrument and transparent local-market timing rule. If not feasible, demote to secondary analysis rather than force a weak measurement.

## Micron CHIPS Act Preliminary Agreement

### Theoretical Rationale

Micron is a named US memory-chip beneficiary. The case directly tests state support for a strategically important semiconductor subsector.

### Identification Rationale

The beneficiary is US-listed, public, and directly named. It also allows comparison with Micron's threat exposure in the China procurement restriction case.

### Likely Reviewer Objection

Micron's market reaction may reflect memory-cycle expectations rather than state support.

### Defence

Use sector benchmarks and, where feasible, memory peers. If Micron's reaction is indistinguishable from the sector or memory cycle, the event is not strong support for the theory.

## 2. Secondary Analysis Events

Secondary analysis events fit the theory but are weaker for identification because they are broad, anticipated, small, implementation-focused, or have market-data complications.

| Event | Date | Category | Main Linked Assets | Secondary Decision |
|---|---|---|---|---|
| CHIPS and Science Act signed | 2022-08-09 | Broad policy support | INTC, MU, TSM, SMH/SOX | Include as broad-policy context |
| BAE receives first CHIPS Act manufacturing award | 2023-12-11 | Direct named support, small award | BAE if feasible | Include as caution case |
| TSMC Kumamoto fab opens with Japanese state support | 2024-02-24 | Implementation / reallocation | TSM | Include as reallocation/implementation case only |

## CHIPS and Science Act Signed

### Theoretical Rationale

The Act is central to state-backed semiconductor opportunity. It legally authorises support and reflects geopolitical industrial policy.

### Identification Rationale

It is useful as a broad policy baseline but not a clean shock. It helps distinguish broad support from direct named support.

### Likely Reviewer Objection

The event was heavily anticipated, and signing is probably not the true information date.

### Defence

Do not use it as a main test. Code high anticipation and interpret as secondary context. Named preliminary terms are the main identification events.

## BAE First CHIPS Manufacturing Award

### Theoretical Rationale

This is direct named state support connected to defence-relevant semiconductor capacity, fitting the theory closely.

### Identification Rationale

The event is specific and official, but the market relevance may be small relative to BAE's overall business.

### Likely Reviewer Objection

The award may be too small to move a diversified defence firm.

### Defence

Include as a caution case only. If no market reaction appears, do not treat it as strong falsification because materiality is weaker.

## TSMC Kumamoto Fab Opening

### Theoretical Rationale

This case reflects state-backed supply-chain reallocation toward allied semiconductor capacity.

### Identification Rationale

It is theoretically relevant but likely not a clean information shock because opening events are anticipated.

### Likely Reviewer Objection

The true information event occurred earlier, when subsidies and investment plans were announced.

### Defence

Use only as secondary evidence on support credibility and reallocation. Do not use it as a primary event-study test unless a better announcement date is separately identified and frozen.

## 3. Contrast Cases

Contrast cases are not expected to support the State Support mechanism directly. They are included to test whether threat-dominant geopolitical events differ from state-support events.

Contrast cases should satisfy:

- Semiconductor or semiconductor-linked relevance.
- Geopolitical restriction, retaliation, or export-control logic.
- No direct state support for the linked firms.
- Identifiable threatened firms or sector benchmarks.

| Event | Date | Category | Main Linked Assets | Contrast Decision |
|---|---|---|---|---|
| Nvidia discloses AI chip export-license requirement | 2022-08-31 | Firm-level threat | NVDA, AMD, SMH, QQQ | Include |
| BIS advanced computing and semiconductor controls | 2022-10-07 | Broad export-control threat | NVDA, AMD, ASML, AMAT, LRCX, TSM, SMH | Include |
| YMTC and other Chinese entities added to Entity List | 2022-12-15 | Entity List / substitution contrast | MU, Samsung/SK Hynix if feasible, SMH | Include as contrast with caution |
| Japan semiconductor-equipment export controls | 2023-03-31 | Allied export-control threat | ASML, AMAT, LRCX, Tokyo Electron if feasible, SMH | Include as contrast with caution |
| China restricts Micron procurement | 2023-05-21 | Retaliation / threat | MU, Samsung/SK Hynix if feasible, SMH | Include |

## Nvidia Export-License Disclosure

### Theoretical Rationale

This is the negative pathway: geopolitical competition creates market-access restrictions without offsetting state support.

### Identification Rationale

The firm-event link is visible because Nvidia disclosed the restriction. It provides a clean contrast against state-support events.

### Likely Reviewer Objection

This is a firm disclosure, not a government announcement.

### Defence

The event is still policy-driven and publicly dated. It should be classified as contrast, not support.

## BIS Advanced Computing and Semiconductor Controls

### Theoretical Rationale

This event captures threat-dominant semiconductor geopolitical competition. It helps test whether positive reactions require state support.

### Identification Rationale

It is official, dated, and central to the semiconductor geopolitical environment.

### Likely Reviewer Objection

The event is broad, bundled, and affects firms differently.

### Defence

Use it only as a contrast case. Do not infer mechanism from it alone. Treat heterogeneous exposure carefully.

## YMTC Entity List Additions

### Theoretical Rationale

This event tests whether restrictions without state support create substitution opportunities, especially in memory chips.

### Identification Rationale

It is a useful contrast to Micron state-support events, but substitute coding is weaker than named-beneficiary coding.

### Likely Reviewer Objection

Substitution beneficiaries are speculative.

### Defence

Use as secondary contrast. Do not let substitution results drive the main conclusion.

## Japan Semiconductor-Equipment Controls

### Theoretical Rationale

This event tests allied restriction without direct support. It helps distinguish strategic importance from market opportunity.

### Identification Rationale

It is official and sector-specific, but affected firms may be foreign-listed and timing may be complicated.

### Likely Reviewer Objection

Foreign listing and mixed exposure reduce clean inference.

### Defence

Use as contrast with caution. If Tokyo Electron data are difficult, rely on US-traded equipment peers and sector benchmarks.

## China Restricts Micron Procurement

### Theoretical Rationale

This is a direct threat to a strategically important US memory firm and a potential substitution case for memory competitors.

### Identification Rationale

Micron is public and directly affected. The event provides a useful negative contrast to Micron's later state-support announcement.

### Likely Reviewer Objection

Substitute beneficiaries may be foreign-listed and politically constrained.

### Defence

Use MU as the clean threat-exposed firm. Treat substitute analysis as secondary and conditional on feasible data.

## 4. Excluded Events

These events should be excluded from the dissertation core sample, even if they are substantively interesting.

| Event | Exclusion Decision | Reason |
|---|---|---|
| FY2019 NDAA Huawei/ZTE federal procurement restrictions | Exclude | Telecom-focused, early, less semiconductor-centred |
| Executive order securing ICT supply chain | Exclude | Broad telecom/ICT, not semiconductor-specific enough |
| Huawei added to Entity List | Exclude from dissertation core | Important but telecom-centred and outside narrowed semiconductor state-support sample |
| Huawei foreign direct product rule | Exclude from dissertation core | Useful historically but widens sample toward Huawei/telecom controls |
| Further Huawei chip restrictions | Exclude | Redundant with broader export-control contrast logic |
| SMIC added to Entity List | Exclude or reserve | Semiconductor-relevant but expands contrast set beyond manageable core |
| Russia invades Ukraine | Exclude | Broad war shock, severe macro confounding |
| Germany Zeitenwende defence fund | Exclude | Defence support, not semiconductor-focused |
| US-Japan-Netherlands reported equipment-control agreement | Exclude | Media-report event, less official than Japan formal controls |
| China gallium/germanium export controls | Exclude | Critical minerals/input shock, not clean semiconductor state-support test |
| US outbound investment order | Exclude | Financial restriction, weak direct support channel |
| BIS October 2023 export-control update | Exclude or reserve | Repetition event; useful later but not needed for core contrast |
| Biren/Moore Threads Entity List additions | Exclude | Same-day bundling with BIS update creates separability problem |
| Polar Semiconductor CHIPS preliminary terms | Exclude or reserve | Smaller award; can be added if main support-event count is too low |
| Rocket Lab CHIPS preliminary terms | Exclude or reserve | Dual-use/space semiconductor case; smaller and less comparable |
| BIS September 2024 quantum/advanced tech controls | Exclude | Broader advanced technology, weaker beneficiary logic |
| BIS December 2024 expanded controls | Exclude or reserve | Repetition event; not needed for core contrast |
| China critical-mineral export restrictions | Exclude | Critical minerals rather than state support in semiconductors |
| AI Diffusion rule | Exclude | AI/export-control event, heavily confounded by AI market cycle |

## Exclusion Rationale by Type

## Telecom-Centreed Huawei Events

### Theoretical Rationale

Huawei events are central to geopolitical technology competition, but the frozen dissertation design is now semiconductor state support, not telecom vendor substitution.

### Identification Rationale

Including Huawei would expand the sample toward telecom, sanctions, and substitution rather than state support.

### Likely Reviewer Objection

Reviewers may ask why canonical technology-competition events are excluded.

### Defence

The project is intentionally narrowed. Huawei can motivate the broader literature but does not belong in the main dissertation event universe.

## Broad War and Defence Events

### Theoretical Rationale

Defence events fit state support but are outside the semiconductor-focused scope.

### Identification Rationale

War shocks introduce severe macro confounding and would weaken internal validity.

### Likely Reviewer Objection

Defence spending is a clean state-support case.

### Defence

It is clean substantively but not aligned with the semiconductor empirical focus. It belongs in future cross-sector work, not this dissertation.

## Critical Minerals and AI Diffusion Events

### Theoretical Rationale

These events are relevant to strategic supply chains, but they widen the project beyond the clean semiconductor support mechanism.

### Identification Rationale

They introduce commodity dynamics, input shocks, AI-cycle confounding, and broader technology policy.

### Likely Reviewer Objection

Excluding them may reduce external validity.

### Defence

External validity is secondary for a master's dissertation. Internal validity and theoretical fit take priority.

## Small or Peripheral CHIPS Awards

### Theoretical Rationale

Small awards may fit state support but may not be market-relevant.

### Identification Rationale

If the support is too small relative to firm value, absence of a market reaction is hard to interpret.

### Likely Reviewer Objection

Excluding small awards could bias toward large, market-moving support.

### Defence

Small awards can be reserved for robustness or appendix analysis. The main sample should test events with plausible market relevance.

## 5. Anticipation Rules

Anticipation should affect evidentiary weight, not automatic inclusion.

## Include but Downgrade

Include anticipated events if they are theoretically central and publicly dated, but treat them as secondary or weak evidence.

Examples:

- CHIPS Act signing.
- TSMC Kumamoto opening.

## Prefer Cleaner Dates

Prefer named preliminary terms, awards, or firm-specific support announcements over:

- broad legislative signing dates
- strategy documents
- facility openings
- reported negotiations

## Reviewer Objection

Anticipated events may show no market reaction even if the theory is true.

## Defence

The dissertation should not rely on anticipated events for the main test. Main analysis uses direct named support announcements, which are more discrete.

## 6. Beneficiary Visibility Rules

Beneficiary visibility should strongly affect inclusion.

## High Visibility

Main analysis eligible:

- named public firm
- named public parent of subsidiary/facility
- reliable public trading instrument

## Medium Visibility

Secondary analysis:

- named foreign-listed firm with manageable trading-calendar issue
- clearly eligible but unnamed firms

## Low Visibility

Exclude or reserve:

- private firms
- unclear ownership links
- broad supply-chain beneficiaries
- speculative substitutes

## Reviewer Objection

This may bias the sample toward large public firms.

## Defence

The dependent variable is public-market reaction. Public-market visibility is not a flaw; it is required by the research question.

## 7. Support Credibility Rules

Support credibility determines sample tier.

## High Credibility

Main analysis:

- official named preliminary terms
- named awards
- official funding commitments
- enacted support with firm-specific implementation

## Medium Credibility

Secondary analysis:

- enacted broad legislation
- programme authorisation
- facility opening or implementation event

## Low Credibility

Exclude:

- speeches
- strategy papers without money
- reports of possible future support
- negotiations without official terms

## Reviewer Objection

Preliminary terms are not final disbursements.

## Defence

Markets price expectations. Preliminary terms are official, firm-specific, and materially more credible than rumors or broad policy aspirations. They are appropriate event-study dates.

## 8. Best Sample Definition for Theory Match

The best theoretical sample is:

> Direct named state-support announcements for strategically important semiconductor firms, supplemented by broad-policy support events and threat-dominant semiconductor restrictions.

This definition matches the frozen theory because it captures:

- geopolitical competition
- strategic importance
- credible state support
- visible investor interpretation
- positive or negative market reaction

## 9. Best Sample Definition for Reviewer Scrutiny

The most defensible reviewer-facing sample is:

> A narrow sample of semiconductor policy events from 2022-2024, divided ex ante into direct support events, broad support events, and threat-dominant contrast events, with event-firm links frozen before returns are calculated.

This survives scrutiny because it avoids:

- post hoc event selection
- overbroad geopolitical risk claims
- mixing defence, energy, telecom, AI, and minerals
- relying on speculative beneficiaries
- treating anticipated legislation as clean shock evidence

## 10. Best Sample Definition for Identification Quality

The highest-identification sample is:

> Named CHIPS preliminary terms and awards for public semiconductor firms, analysed against sector peers and semiconductor benchmarks, with export-control events used only as contrast.

This maximizes identification because:

- event dates are clearer
- beneficiaries are visible
- support directness is high
- support credibility is high
- public-market outcomes are measurable
- sector benchmarks are available

## Complete Core Sample Freeze V1

## Final Event Categories

## Category A: Main Analysis

Use for primary hypothesis tests.

| Event | Date | Beneficiary | Include? |
|---|---|---|---|
| Intel CHIPS Act preliminary terms | 2024-03-20 | INTC | Yes |
| TSMC Arizona CHIPS Act preliminary terms | 2024-04-08 | TSM | Yes |
| Samsung CHIPS Act preliminary terms | 2024-04-15 | Samsung | Yes, if market timing feasible |
| Micron CHIPS Act preliminary agreement | 2024-04-25 | MU | Yes |

## Category B: Secondary Analysis

Use for contextual or robustness discussion, not primary mechanism claims.

| Event | Date | Role |
|---|---|---|
| CHIPS and Science Act signed | 2022-08-09 | Broad policy baseline |
| BAE first CHIPS manufacturing award | 2023-12-11 | Small direct-support caution case |
| TSMC Kumamoto fab opening | 2024-02-24 | Implementation/reallocation case |

## Category C: Contrast Cases

Use to compare state-support events against threat-dominant events.

| Event | Date | Role |
|---|---|---|
| Nvidia export-license disclosure | 2022-08-31 | Firm-level restriction contrast |
| BIS October 7 advanced computing controls | 2022-10-07 | Broad export-control contrast |
| YMTC Entity List additions | 2022-12-15 | Restriction/substitution contrast |
| Japan semiconductor-equipment controls | 2023-03-31 | Allied restriction contrast |
| China restricts Micron procurement | 2023-05-21 | Retaliation contrast |

## Category D: Excluded or Reserved

Do not include in main dissertation sample unless the committee demands expansion.

| Event Type | Treatment |
|---|---|
| Huawei telecom-centred restrictions | Exclude |
| Broad war/defence shocks | Exclude |
| Critical minerals export controls | Exclude |
| AI Diffusion rule and broad AI controls | Exclude |
| Repeated late export-control updates | Reserve |
| Small peripheral CHIPS awards | Reserve |
| Media-reported pre-official agreements | Exclude unless no official event exists |

## Final Inclusion Rules

Include in main analysis only if:

- event is semiconductor-relevant
- event is linked to geopolitical competition or strategic industrial policy
- event provides direct state support
- beneficiary is named
- beneficiary has observable public-market data
- support is credible and official
- event date is identifiable
- event-firm link can be frozen before returns are collected

## Final Exclusion Rules

Exclude from core sample if:

- event lacks direct state support and is not needed as contrast
- event lacks a visible public-market beneficiary
- event is mainly telecom, defence, energy, AI, or critical minerals rather than semiconductors
- event is purely rhetorical
- event is only a reported negotiation without official support terms
- event is too small or peripheral for plausible market relevance, unless retained as a caution case
- event is too bundled to classify

## Recommended Dissertation Sample

The recommended dissertation sample should contain:

- 4 main support events.
- 3 secondary support/reallocation events.
- 5 contrast events.

Total: **12 events**.

This sample is small, but defensible for a master's dissertation because the objective is not large-N causal inference. The objective is a transparent, mechanism-focused event study of whether named state support in a strategic semiconductor sector produces market reactions consistent with the frozen theory.

## Final Reviewer-Facing Justification

The sample is intentionally narrow. It prioritises internal validity over breadth. The dissertation does not claim to explain all geopolitical competition or all market opportunity. It tests a precise mechanism in a most-likely sector:

> Do financial markets react positively when strategically important semiconductor firms receive credible, named state support under geopolitical competition?

If the answer is no, the broader theory is weakened. If the answer is yes, the evidence supports a narrow but meaningful claim: geopolitical competition can produce positive market reactions when states convert strategic importance into credible economic support.
