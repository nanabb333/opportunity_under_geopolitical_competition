# Pilot Dataset V1

## Purpose

This pilot does not test the theory. It tests whether the frozen theory, research design, dataset architecture, and research protocol can be operationalised before market returns are collected.

Frozen mechanism:

```text
Geopolitical Competition
-> Strategic Importance
-> Credible State Support
-> Investor Interpretation
-> Positive Market Reaction
```

The pilot sample contains 12 candidate events. The sample intentionally includes:

- Direct semiconductor state-support events.
- Broad semiconductor industrial-policy events.
- State-backed supply-chain relocation events.
- Threat-dominant export-control or restriction events.

The pilot is judged successful if events can be dated, coded, and linked to firms before returns are observed.

## Pilot Sample Summary

| # | Event | Date | Event Class | Main Firms / Assets | Pilot Use |
|---:|---|---|---|---|---|
| 1 | CHIPS and Science Act signed | 2022-08-09 | broad_policy | INTC, TSM, MU, NVDA, AMD, ASML, SMH | Broad state-support baseline |
| 2 | Nvidia discloses AI chip export-license requirement | 2022-08-31 | threat_contrast | NVDA, AMD, SMH, QQQ | Threat-dominant contrast |
| 3 | BIS advanced computing and semiconductor controls | 2022-10-07 | threat_contrast | NVDA, AMD, ASML, AMAT, LRCX, TSM, SMH | Major restriction contrast |
| 4 | YMTC and other Chinese entities added to Entity List | 2022-12-15 | threat_contrast | MU, Samsung, SK Hynix if feasible, SMH | Restriction plus substitution logic |
| 5 | Japan semiconductor-equipment export controls | 2023-03-31 | threat_contrast | ASML, AMAT, LRCX, Tokyo Electron if feasible, SMH | Allied restriction contrast |
| 6 | China restricts Micron procurement | 2023-05-21 | threat_contrast / mixed | MU, Samsung, SK Hynix if feasible, SMH | Retaliation and substitute logic |
| 7 | BAE receives first CHIPS Act manufacturing award | 2023-12-11 | support | BAE if tradable/available, SMH, defence-semiconductor peers | Small direct-support test |
| 8 | TSMC Kumamoto fab opens with Japanese state support | 2024-02-24 | support / relocation | TSM, Sony if feasible, Toyota if relevant, SMH | State-backed reallocation test |
| 9 | Intel CHIPS preliminary terms announced | 2024-03-20 | support | INTC, SMH, SOX, QQQ | Direct named-support test |
| 10 | TSMC Arizona CHIPS preliminary terms announced | 2024-04-08 | support | TSM, INTC, SMH, SOX | Direct named-support and relocation test |
| 11 | Samsung CHIPS preliminary terms announced | 2024-04-15 | support | Samsung if feasible, TSM, INTC, SMH | Direct support with foreign listing challenge |
| 12 | Micron CHIPS preliminary agreement announced | 2024-04-25 | support | MU, SMH, SOX | Direct named-support test |

## Event-Level Pilot Assessment

## 1. CHIPS and Science Act Signed

### Inclusion Rationale

The event is semiconductor-relevant, publicly dated, strategically framed, and directly connected to US industrial policy under technological and supply-chain competition. It qualifies as a broad state-support event.

### Expected Mechanism

Geopolitical competition increases the strategic importance of domestic semiconductor capacity. The Act signals state support through subsidies, tax incentives, and industrial-policy commitment. Investors may interpret this as improving future investment economics for US-linked semiconductor capacity.

### Likely Beneficiary Firms

- INTC: eligible domestic manufacturing beneficiary.
- MU: eligible domestic memory/manufacturing beneficiary.
- TSM: beneficiary through US fab investment eligibility.
- Samsung: beneficiary if US fab eligibility is included.
- SMH/SOX: sector benchmark, not beneficiary.

### Event-to-Firm Linking Decisions

INTC, MU, TSM, and Samsung should be coded as `eligible_beneficiary`, not necessarily `named_beneficiary`, because the signing event authorises a programme rather than assigning final support to all firms. SMH/SOX should be benchmarks. NVDA and AMD may be sector peers, not direct beneficiaries, unless eligibility language clearly applies.

### Coding Ambiguities

This event has high state support but low directness. It should not be coded like a named award. It may also impose guardrails and compliance burdens.

### Event-Dating Problems

The signing date is likely anticipated. Legislative passage dates may be more market-relevant. This should be coded with high `anticipation_level`.

### Support Directness and Credibility

- support_directness: moderate, because the Act authorises support but does not name most firms.
- support_credibility: high, because it is enacted legislation with funding authority.

### Reviewer Objections

The strongest objection is that the event was priced before signing. Defence: retain as broad-policy baseline, but do not treat it as the cleanest state-support test.

## 2. Nvidia Discloses AI Chip Export-License Requirement

### Inclusion Rationale

The event is semiconductor-linked, publicly dated through firm disclosure, and directly tied to US export restrictions on advanced chips. It qualifies as a threat-dominant contrast event.

### Expected Mechanism

The event represents the negative pathway: geopolitical competition creates restrictions and market-access risk. It should not be expected to support the State Support mechanism directly.

### Likely Beneficiary Firms

No clean state-support beneficiary. Possible weak substitute logic for AMD is not convincing because AMD may face similar restrictions.

### Event-to-Firm Linking Decisions

NVDA should be `threat_exposed`. AMD may be `threat_exposed` or `sector_peer` depending on whether the disclosure and policy scope clearly apply. SMH and QQQ are benchmarks.

### Coding Ambiguities

The event is firm-specific but policy-driven. It may be difficult to separate company disclosure from policy announcement.

### Event-Dating Problems

Use the firm disclosure date. If the filing was after market close, CAR [-1,+1] should be primary.

### Support Directness and Credibility

- support_directness: none.
- support_credibility: none.

### Reviewer Objections

Reviewer may object that this is not a state-support event. That is correct; it is included only as a threat contrast.

## 3. BIS Advanced Computing and Semiconductor Controls

### Inclusion Rationale

This is a central semiconductor export-control event, publicly dated, geopolitical, and strategically framed. It qualifies as a threat-dominant contrast event.

### Expected Mechanism

The event tests whether threat-dominant restrictions produce different reactions from state-support events. It may also reveal whether investors identify substitute or reallocation beneficiaries.

### Likely Beneficiary Firms

No direct state-support beneficiaries. Possible long-run beneficiaries include allied fabs, non-China supply-chain assets, or compliance providers, but this is not clean enough for primary support coding.

### Event-to-Firm Linking Decisions

NVDA, AMD, ASML, AMAT, LRCX, and TSM may be `threat_exposed` depending on product and market exposure. SMH/SOX are benchmarks. Potential substitutes should be coded cautiously.

### Coding Ambiguities

This is a mixed event in theory: it threatens China-exposed firms but may increase strategic value of allied capacity. However, because no direct support is provided, the primary class should remain `threat_contrast`.

### Event-Dating Problems

The official announcement date is clear, but some expectations may have existed before publication.

### Support Directness and Credibility

- support_directness: none.
- support_credibility: none.

### Reviewer Objections

Reviewer may say this event is too broad and affects too many firms in different directions. Defence: use it only as a contrast case, not as a clean support mechanism test.

## 4. YMTC and Other Chinese Entities Added to Entity List

### Inclusion Rationale

The event is semiconductor-relevant, publicly dated, geopolitical, and a restriction event. It provides a useful contrast case with possible substitution logic in memory chips.

### Expected Mechanism

This primarily tests the negative pathway and the secondary substitution/reallocation pathway. It does not test direct state support.

### Likely Beneficiary Firms

- MU: possible substitute in memory chips.
- Samsung and SK Hynix: possible substitutes, though data feasibility is more difficult.
- SMH/SOX: benchmarks.

### Event-to-Firm Linking Decisions

YMTC is not publicly usable in the same way as US-listed firms. MU can be coded as `substitute` only if the substitution logic is clearly documented. Samsung/SK Hynix can be included only if market data are feasible.

### Coding Ambiguities

Substitution is plausible but not guaranteed. Capacity, product mix, and China market access complicate beneficiary coding.

### Event-Dating Problems

Official announcement date is usable. Some anticipation may exist due to earlier control escalation.

### Support Directness and Credibility

- support_directness: none.
- support_credibility: none.

### Reviewer Objections

Reviewer may argue that this belongs to sanctions/export-control literature rather than state support. Defence: retain only as contrast and secondary substitution check.

## 5. Japan Semiconductor-Equipment Export Controls

### Inclusion Rationale

The event is semiconductor-equipment relevant, publicly dated, and tied to allied export-control coordination. It is a useful threat-dominant allied-policy contrast.

### Expected Mechanism

The event mainly captures restriction and strategic control. It may support supply-chain reallocation logic, but not the primary State Support mechanism.

### Likely Beneficiary Firms

No clean beneficiary. Domestic Chinese equipment firms may benefit over time but may not be public or included in the master asset universe. Allied equipment firms may be strategically important but also lose China sales.

### Event-to-Firm Linking Decisions

ASML, AMAT, LRCX, and Tokyo Electron if feasible should be linked as `threat_exposed` or sector peers, depending on direct exposure. SMH/SOX are benchmarks.

### Coding Ambiguities

This event may raise long-run strategic value while hurting near-term sales. Expected direction may be mixed or negative.

### Event-Dating Problems

Official announcement date is clear. Implementation timing may differ from announcement timing.

### Support Directness and Credibility

- support_directness: none.
- support_credibility: none.

### Reviewer Objections

Reviewer may ask why this is included if the focus is state support. Defence: it is a clean contrast event showing restrictions without support.

## 6. China Restricts Micron Procurement

### Inclusion Rationale

The event is semiconductor-relevant, publicly dated, and geopolitical. It qualifies as a retaliation/threat event with clearer substitution logic than many export controls.

### Expected Mechanism

This event primarily tests threat dominance for Micron and secondary substitution for memory competitors. It does not test direct state support.

### Likely Beneficiary Firms

- Samsung: possible substitute.
- SK Hynix: possible substitute.
- Domestic Chinese memory firms if feasible, though public-market linkage is difficult.

### Event-to-Firm Linking Decisions

MU should be `threat_exposed`. Samsung/SK Hynix may be `substitute` if included. SMH/SOX are benchmarks.

### Coding Ambiguities

Substitutes may also face geopolitical constraints, and Chinese procurement rules may favor domestic firms rather than non-US foreign firms.

### Event-Dating Problems

The announcement date may fall outside US trading hours. Use CAR [-1,+1] and document time-zone issue.

### Support Directness and Credibility

- support_directness: none.
- support_credibility: none.

### Reviewer Objections

Reviewer may object that foreign-listed substitutes complicate implementation. Defence: if data feasibility is poor, use this event mainly for threat-exposed MU and benchmark comparison.

## 7. BAE Receives First CHIPS Act Manufacturing Award

### Inclusion Rationale

This is a direct, named support event under the CHIPS framework. It is semiconductor-linked and defence-relevant, making it theoretically strong despite small event size.

### Expected Mechanism

Strategic importance is recognised through defence-linked semiconductor capacity. State support is direct and named. Investors may interpret the award as improving expected funding, capacity, or strategic positioning.

### Likely Beneficiary Firms

- BAE Systems, if listed data are feasible.
- Defence-semiconductor supply-chain peers are less clear.
- SMH/SOX and possibly defence benchmarks can be used as benchmarks.

### Event-to-Firm Linking Decisions

BAE should be `named_beneficiary` if a usable listed security is included. SMH/SOX are benchmarks. Other firms should not be coded as beneficiaries unless explicitly linked.

### Coding Ambiguities

The event is small relative to BAE's total business and may not be market-relevant. It straddles defence and semiconductor categories.

### Event-Dating Problems

Official announcement date is usable. Check whether announcement occurred during trading hours.

### Support Directness and Credibility

- support_directness: high, because a named recipient is announced.
- support_credibility: high, because it is an official award/preliminary terms announcement.

### Reviewer Objections

Reviewer may argue the event is too small to move a large firm. Defence: include as an operational test of direct support, but classify data quality as caution if market relevance is weak.

## 8. TSMC Kumamoto Fab Opens With Japanese State Support

### Inclusion Rationale

The event concerns state-backed semiconductor capacity in Japan and supply-chain relocation away from concentration risk. It qualifies as support/reallocation.

### Expected Mechanism

Geopolitical competition raises the strategic importance of diversified semiconductor capacity. Japanese support and the physical fab opening signal credible state-backed reallocation.

### Likely Beneficiary Firms

- TSM: public parent of TSMC.
- Sony/Toyota only if the ownership or joint-venture relationship is directly relevant and data are feasible.
- SMH/SOX as benchmarks.

### Event-to-Firm Linking Decisions

TSM can be linked as a beneficiary if the fab is clearly tied to TSMC and state support. Sony/Toyota should be linked only with documented direct involvement. Otherwise, they should be excluded from the pilot asset links.

### Coding Ambiguities

Opening events are often anticipated. The market may have priced the investment earlier. It may test credibility of reallocation more than surprise.

### Event-Dating Problems

Opening date is clear, but investment announcements and subsidy approvals may be better information dates. Record alternative dates.

### Support Directness and Credibility

- support_directness: moderate to high, depending on source specificity.
- support_credibility: high, because physical completion indicates implementation.

### Reviewer Objections

Reviewer may argue this is not an announcement shock. Defence: treat it as a reallocation/support credibility case, not a primary event-study shock unless alternative announcement dates are added.

## 9. Intel CHIPS Act Preliminary Terms Announced

### Inclusion Rationale

This is a direct named support event for a major strategically important semiconductor firm. It is one of the cleanest tests of the State Support mechanism.

### Expected Mechanism

US geopolitical competition increases the strategic importance of domestic fab capacity. The preliminary terms signal credible state support for Intel's manufacturing role. Investors may interpret this as improving future cash flows, financing conditions, or downside protection.

### Likely Beneficiary Firms

- INTC: named beneficiary.
- Semiconductor equipment suppliers may be indirect peers, not beneficiaries.
- SMH/SOX, QQQ, SPY as benchmarks.

### Event-to-Firm Linking Decisions

INTC should be `named_beneficiary`. AMAT, LRCX, KLAC can be sector peers or indirect supply-chain peers, not named beneficiaries. SMH/SOX are benchmarks.

### Coding Ambiguities

State support may signal weakness because Intel needs public help. This is an important rival interpretation.

### Event-Dating Problems

Official announcement date is usable. Need to check for Intel earnings, major firm news, or semiconductor sector news around the same window.

### Support Directness and Credibility

- support_directness: high.
- support_credibility: high, though final award timing may remain conditional.

### Reviewer Objections

Reviewer may say Intel's reaction is driven by firm fundamentals or turnaround expectations. Defence: compare against SMH/SOX and equipment peers; treat underperformance as evidence against the mechanism.

## 10. TSMC Arizona CHIPS Act Preliminary Terms Announced

### Inclusion Rationale

This is a direct named support event for state-backed semiconductor manufacturing capacity in the United States. It fits the mechanism closely.

### Expected Mechanism

Strategic dependence on advanced foundry capacity leads to US support for TSMC's US expansion. Investors may interpret funding as reducing cost burdens and strengthening TSMC's strategic position.

### Likely Beneficiary Firms

- TSM: named beneficiary through TSMC.
- INTC as sector peer or potential competitor, not beneficiary.
- SMH/SOX as benchmarks.

### Event-to-Firm Linking Decisions

TSM should be `named_beneficiary`. INTC should be `sector_peer` or competitor/peer, not beneficiary. SMH/SOX are benchmarks.

### Coding Ambiguities

The same event may be positive because of funding but negative because US fab costs are high. Expected direction may be positive but with caution.

### Event-Dating Problems

Official date is usable. Need to document whether the announcement was anticipated by prior negotiations.

### Support Directness and Credibility

- support_directness: high.
- support_credibility: high, though preliminary terms are not identical to final disbursement.

### Reviewer Objections

Reviewer may argue support offsets costs rather than creates opportunity. Defence: the theory allows support to reduce downside risk; positive reaction is not required but is predicted if support is credible.

## 11. Samsung CHIPS Act Preliminary Terms Announced

### Inclusion Rationale

This is a direct named support event for an allied semiconductor producer investing in US capacity. It tests the mechanism outside US-headquartered firms.

### Expected Mechanism

Strategic importance of allied semiconductor capacity leads to US support for Samsung's US investment. Investors may interpret support as improving economics of US expansion.

### Likely Beneficiary Firms

- Samsung Electronics, if tradable data are feasible.
- TSM and INTC as sector peers.
- SMH/SOX as benchmarks.

### Event-to-Firm Linking Decisions

Samsung should be `named_beneficiary` if listing and market data are usable. TSM and INTC should be sector peers, not beneficiaries. If Samsung data are infeasible, this event may remain in the event dataset but be weak for firm-level analysis.

### Coding Ambiguities

Non-US listing and time-zone issues may complicate event-window measurement. The event may also be anticipated.

### Event-Dating Problems

US announcement date may not align cleanly with Korean trading hours. The protocol must specify whether to use Samsung's local trading day or ADR/OTC equivalent if available.

### Support Directness and Credibility

- support_directness: high.
- support_credibility: high.

### Reviewer Objections

Reviewer may say the event is operationally messy because the primary market is outside the US. Defence: include in pilot to test feasibility; exclude from full firm-level sample if trading-calendar problems are too severe.

## 12. Micron CHIPS Act Preliminary Agreement Announced

### Inclusion Rationale

This is a direct named support event for a US memory-chip firm. It is a clean state-support case and also useful because Micron appears in threat-contrast events.

### Expected Mechanism

US support for memory-chip capacity converts strategic importance into expected public assistance for Micron. Investors may interpret this as improving long-run investment economics and reducing downside risk.

### Likely Beneficiary Firms

- MU: named beneficiary.
- Samsung/SK Hynix as sector peers if feasible.
- SMH/SOX as benchmarks.

### Event-to-Firm Linking Decisions

MU should be `named_beneficiary`. Samsung/SK Hynix, if included, should be sector peers or competitors. SMH/SOX are benchmarks.

### Coding Ambiguities

Micron's memory-cycle exposure may dominate policy news. It is important to compare against memory peers and semiconductor benchmarks.

### Event-Dating Problems

Official announcement date is usable. Check for Micron earnings or memory-sector news in the same window.

### Support Directness and Credibility

- support_directness: high.
- support_credibility: high.

### Reviewer Objections

Reviewer may argue market reaction is memory-cycle related. Defence: use SMH/SOX and, if feasible, Samsung/SK Hynix peer comparisons.

## Pilot Audit Report

## 1. Can the Project Be Operationalised?

Yes, but only if the first full dataset stays narrow. Direct CHIPS preliminary terms and named support events are operationally clean. Broad legislation and export controls are useful but less clean. Foreign-listed firms and anticipated events create the largest implementation problems.

## 2. Do the Events Qualify Under the Protocol?

Most pilot events qualify. The strongest cases are:

- Intel CHIPS preliminary terms.
- TSMC Arizona CHIPS preliminary terms.
- Samsung CHIPS preliminary terms, conditional on market-data feasibility.
- Micron CHIPS preliminary agreement.

The weakest cases are:

- CHIPS Act signing, because of anticipation.
- TSMC Kumamoto fab opening, because the opening may not be the true information shock.
- BAE award, because market relevance may be small.

## 3. Can Likely Beneficiaries Be Identified?

Yes for direct support events. Beneficiary identification is strongest when official announcements name the firm.

Strong links:

- INTC for Intel CHIPS terms.
- TSM for TSMC Arizona terms.
- MU for Micron CHIPS agreement.
- Samsung for Samsung CHIPS terms if data are feasible.

Weak or difficult links:

- BAE if listed-market data and semiconductor-specific relevance are weak.
- Sony/Toyota for Kumamoto unless direct ownership/economic relevance is documented.
- Substitutes in restriction events, because substitution is plausible but often indirect.

## 4. Can Event-to-Firm Linking Be Done Before Returns?

Yes. Named support events are straightforward. The protocol works best when linking is based on official source naming rather than inferred beneficiary status.

The main rule should be:

> The primary analysis should privilege named_beneficiary links. Eligible_beneficiary and substitute links should be secondary.

## 5. Main Coding Ambiguities

## Broad Policy Versus Direct Support

The CHIPS Act signing is support, but not named support. It should not be treated as equivalent to preliminary funding terms.

## Support Versus Weakness Signal

Intel may receive state support because it is strategically important, but the market may also interpret support as evidence of execution problems.

## Support Versus Cost Offset

TSMC Arizona support may offset high US fab costs rather than create net upside.

## Substitution Coding

YMTC and Micron restriction events create plausible substitutes, but substitute coding can easily become speculative.

## Foreign Listing Problems

Samsung and Tokyo Electron may be theoretically relevant but operationally difficult due to trading calendars, currency, and data access.

## 6. Event-Dating Problems

## Anticipated Legislation

CHIPS Act signing is not a clean shock. Use it as broad-policy context, not a main causal test.

## Preliminary Terms Versus Final Awards

CHIPS preliminary terms are strong information events, but final awards and disbursements may occur later.

## Opening Versus Announcement

TSMC Kumamoto opening is observable but may be less market-relevant than earlier investment or subsidy announcements.

## Time-Zone Alignment

Samsung and Japan-related events require careful trading-day alignment.

## 7. Can Support Directness Be Coded Consistently?

Yes. The pilot shows clear anchors:

- High directness: named preliminary terms or named award.
- Moderate directness: broad legislation or eligibility.
- Low/none: export controls without support.

The directness variable appears reliable.

## 8. Can Support Credibility Be Coded Consistently?

Mostly yes, but credibility needs strict rules.

High credibility:

- official named preliminary terms
- official awards
- enacted legislation
- completed state-backed facility opening

Lower credibility:

- strategy documents
- reported negotiations
- broad rhetorical commitments

Potential issue:

Preliminary terms are credible but not final disbursements. They should be coded high but with notes.

## 9. Are Mechanism Variables Observable in Practice?

## Geopolitical Competition Link

Observable through official national-security, supply-chain, technology competition, or strategic-capacity language.

## Strategic Importance

Observable for semiconductors, but may lack variation because nearly all pilot events are strategic. It works as a scope condition, not as a differentiating variable.

## State Support

Highly observable for CHIPS preliminary terms and awards.

## Support Directness

Highly observable.

## Support Credibility

Observable, but requires judgment about preliminary versus final support.

## Investor Interpretation

Not directly observed in this pilot. The event-study outcome only infers market interpretation. Text evidence would be needed later if the dissertation wants stronger interpretation evidence.

## 10. Protocol Failures Discovered

## Failure 1: Foreign-Listed Beneficiary Handling Is Underspecified

Samsung, Tokyo Electron, Sony, and SK Hynix create trading-calendar and listing problems.

Recommended revision:

Add a protocol rule for foreign-listed assets:

> Use the first local trading day after the event if the announcement occurs after the local market close; document currency, listing, and time-zone treatment.

## Failure 2: Facility Opening Events Are Not Always Information Events

TSMC Kumamoto's opening may not be a market shock.

Recommended revision:

Add a distinction between:

- support announcement date
- funding commitment date
- implementation/opening date

Use implementation events only as secondary evidence unless they introduce new information.

## Failure 3: Broad Legislation Is Too Anticipated for Primary Tests

CHIPS Act signing is useful but not clean.

Recommended revision:

Full dataset should prioritise named preliminary terms and awards over legislative signing dates.

## Failure 4: Substitute Links Are Weaker Than Named Beneficiary Links

Substitution can be coded, but it is often speculative.

Recommended revision:

Use substitute observations as secondary, not central, evidence unless product overlap and market substitution are clear.

## Failure 5: Market-Relevance Threshold Is Missing

Small awards like BAE may be theoretically clean but too small to move market prices.

Recommended revision:

Add a `market_relevance_caution` flag for events where the policy amount or affected segment is small relative to firm size.

## 11. Recommended Revisions Before Full Dataset Construction

1. Prioritise direct named support events for the primary sample.
2. Treat broad policy events as contextual or secondary.
3. Add a foreign-listed asset timing rule.
4. Add an implementation-event rule.
5. Add a market-relevance caution flag.
6. Use substitute coding only as secondary evidence.
7. Require source notes for every named-beneficiary link.
8. Freeze the pilot asset universe before collecting returns.

## 12. Pilot Dataset V1 Candidate Sample

## Recommended Primary Pilot Events

These should be retained for the first operational build:

| Event | Keep? | Reason |
|---|---|---|
| Intel CHIPS preliminary terms | Yes | Clean named support, US-listed firm. |
| TSMC Arizona CHIPS preliminary terms | Yes | Clean named support, US-traded ADR. |
| Micron CHIPS preliminary agreement | Yes | Clean named support, US-listed firm. |
| Samsung CHIPS preliminary terms | Conditional | Clean event but foreign-listing issue. |
| BAE first CHIPS award | Conditional | Clean direct support but possibly low market relevance. |
| CHIPS Act signing | Secondary | Broad support but anticipated. |
| TSMC Kumamoto opening | Secondary | Strong reallocation but weak information shock. |
| Nvidia export-license disclosure | Contrast | Clean threat-dominant contrast. |
| BIS October 7 controls | Contrast | Major threat-dominant contrast. |
| YMTC Entity List additions | Contrast | Threat plus substitution, but coding harder. |
| Japan equipment controls | Contrast | Useful allied restriction contrast. |
| China Micron restriction | Contrast | Useful retaliation/substitution case. |

## Recommended Full-Dataset Direction After Pilot

The full dataset should be built around:

- Direct CHIPS preliminary terms and awards as primary support events.
- Broad CHIPS legislation as secondary policy context.
- Export controls and Entity List additions as contrast events.
- Foreign-listed firms only when timing and data access are manageable.

## Final Pilot Verdict

The project is operationalisable, but the pilot reveals that the cleanest empirical test is narrower than the original event inventory. The primary dataset should not try to cover every geopolitical semiconductor event. It should centre on direct named state-support announcements and use threat-dominant events as a structured contrast.

The mechanism variables are observable in practice, especially `state_support`, `support_directness`, and `support_credibility`. The weakest parts are substitution coding, foreign-listed asset handling, and identifying true information dates for broad legislation or facility openings.

The project should proceed to full dataset construction only after the protocol is revised to address foreign listings, implementation events, and market-relevance caution flags.
