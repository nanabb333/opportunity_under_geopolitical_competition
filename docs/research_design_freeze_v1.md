# Research Design Freeze V1

## Project Status

The theory is frozen unless a fatal design flaw appears.

Core theory:

> Geopolitical competition generates positive market reactions when strategically important firms or sectors are expected to receive credible state support that improves future cash flows or reduces downside risk.

This design freeze translates that theory into a master's-dissertation proposal. The objective is not to prove the theory true. The objective is to design a test that could plausibly support, weaken, or falsify the State Support mechanism.

## Recommended Design in One Sentence

Use a focused event study of semiconductor state-support announcements, comparing named beneficiaries, sector peers, and broad benchmarks, with export-control events used as a limited threat-dominant contrast group.

## 1. Identification Strategy

### Strongest Design Choice

The strongest identification strategy is a narrow event-study design centred on discrete policy announcements where state support is publicly announced for strategically important semiconductor firms or facilities. The main comparison should be between:

- Named beneficiaries of state support.
- Strategically relevant sector peers not directly named.
- Broad semiconductor benchmarks.
- Broad market benchmarks.

The primary outcome should be abnormal return around short windows: event day, CAR [-1,+1], and CAR [-3,+3]. The core comparison is not "did the whole semiconductor sector rise?" but "did named or clearly eligible state-supported firms outperform relevant peers and benchmarks around credible support announcements?"

### Strongest Reviewer Attack

The event-study design cannot prove causality because policy announcements are anticipated, bundled with other news, and embedded in semiconductor cycles. Reviewers may argue that any positive reaction reflects AI demand, earnings expectations, interest rates, or prior anticipation rather than state support.

### Defence

Do not overclaim causality. Frame the design as a market-expectations test, not a structural causal estimate. Use short windows, sector-adjusted returns, and pre-specified event inclusion rules. Compare named beneficiaries to sector peers to reduce the risk that results are only semiconductor-cycle effects. Flag anticipated and bundled events rather than pretending they are clean shocks.

The defensible claim is:

> If credible state support matters, named or directly eligible firms should show stronger abnormal reactions than broad benchmarks around support announcements, especially when the support is specific, funded, and strategically framed.

## 2. Mechanism Testing

### Strongest Design Choice

The mechanism test should focus on whether market reactions are stronger when state support is direct and credible. Events should be classified before collecting returns into categories such as:

- Direct named support: preliminary funding terms, grants, procurement, named awards.
- Broad policy support: legislation, programme authorisation, eligibility rules.
- Threat-dominant events: export controls, Entity List additions, restrictions without direct support.

The core mechanism is supported if direct state-support events produce more positive reactions for named beneficiaries than broad policy support or threat-dominant events.

### Strongest Reviewer Attack

The mechanism may be indistinguishable from a simpler story: markets like government money. If the project only shows that subsidy recipients rise after subsidy announcements, the theoretical contribution is thin.

### Defence

The dissertation must show that state support matters specifically in strategically important geopolitical sectors, not merely as generic subsidies. The defence is to connect each support event to strategic semiconductor capacity, national-security framing, supply-chain resilience, or technology competition. The thesis should also compare state-support events to restriction-only events in the same sector. If restriction-only events are negative or mixed while support events are positive, the mechanism is sharper than "geopolitics is good."

The mechanism claim should be modest:

> State support is the conversion mechanism through which geopolitical competition becomes investable opportunity for selected strategic firms.

## 3. Event Selection Logic

### Strongest Design Choice

Select events using rule-based criteria before examining returns.

Inclusion criteria:

- Event is publicly announced on an identifiable date.
- Event concerns semiconductors or semiconductor-linked strategic technology.
- Event is connected to geopolitical competition, supply-chain security, national security, or strategic industrial policy.
- Event includes either credible state support or a clear threat-dominant contrast.
- Affected public firms or indices can be identified before observing returns.

Exclusion criteria:

- Pure rhetoric without policy instrument.
- Events with no identifiable market assets.
- Events dominated by firm earnings.
- Events whose announcement date is impossible to identify.
- Events selected only because they are known to have moved markets.

### Strongest Reviewer Attack

The event list may be cherry-picked. If the researcher selects famous CHIPS Act announcements and ignores null cases, results will be biased toward confirming the theory.

### Defence

Create an event log that includes all candidate events considered, including excluded events and reasons for exclusion. Include weaker or smaller support events if they meet inclusion rules. Preserve null and ambiguous events. Do not remove events after seeing returns unless there is a pre-specified exclusion reason, such as overlapping earnings or missing price data.

The proposal should state:

> Event selection will be completed and frozen before abnormal returns are calculated.

## 4. Scope Conditions

### Strongest Design Choice

Limit the first empirical test to semiconductors and semiconductor-linked strategic industrial policy. This is the best fit because semiconductors are:

- Clearly strategically important.
- Central to geopolitical competition.
- Subject to observable state support.
- Represented by public firms and sector ETFs.
- Exposed to both support and threat-dominant events.

### Strongest Reviewer Attack

A semiconductor-only design may not generalize. Reviewers may say the project is really about CHIPS policy or the semiconductor cycle, not a broader theory of geopolitical competition.

### Defence

Accept the limitation. A master's thesis does not need to prove universal generality. The scope condition is part of the theory: the mechanism should work best in strategic sectors where state support is credible and market-relevant. Semiconductors are a hard enough first test because the sector has both positive state-support events and negative export-control shocks.

The thesis should avoid claiming external validity beyond strategic industries. It can say the design tests a plausibility case for the mechanism, not the entire global theory.

## 5. Alternative Explanations

### Strongest Design Choice

Pre-specify the main alternative explanations and build defences into the design:

- AI and semiconductor demand cycle.
- Earnings announcements and firm fundamentals.
- Interest-rate and macro news.
- General risk-on or risk-off market movement.
- Prior anticipation of policy.
- Lobbying or political connections.
- Subsidy as a signal of firm weakness.
- Sector-wide industrial policy optimism.

The strongest empirical defence is to compare supported firms against sector benchmarks and peers, not only against broad market indices.

### Strongest Reviewer Attack

The largest alternative explanation is the semiconductor and AI cycle. From 2022 onward, many semiconductor firms moved because of AI demand, capex cycles, and earnings revisions. State support may be secondary.

### Defence

Use semiconductor-specific benchmarks such as SMH or SOX where feasible. Report both market-adjusted and sector-adjusted abnormal returns. If a named beneficiary outperforms SPY but not SMH, the result should not be interpreted as strong support for the theory. The most credible evidence is beneficiary outperformance relative to the semiconductor sector around a direct support announcement.

## 6. Falsification Criteria

### Strongest Design Choice

State clear falsification conditions before analysis.

The theory is weakened if:

- Named beneficiaries do not outperform broad market or sector benchmarks around direct support events.
- Support events produce no stronger reactions than threat-dominant export-control events.
- Strategic support events are followed by negative abnormal returns after sector adjustment.
- Positive reactions disappear under CAR [-1,+1] and only appear in longer, confounded windows.
- Results are driven by one famous event.
- Opportunity effects are indistinguishable from broad semiconductor rallies.

### Strongest Reviewer Attack

The theory may become unfalsifiable if every negative result is explained away as anticipation, bundling, or market irrationality.

### Defence

Commit to interpreting null or negative sector-adjusted reactions as real evidence against the theory for that event class. Anticipation and bundling may be discussed, but they cannot be used to rescue every failed result. The dissertation should include a table classifying each event as supportive, contradictory, or inconclusive.

## 7. Internal Validity

### Strongest Design Choice

Internal validity depends on tight event windows, pre-specified event dates, relevant benchmarks, and transparent handling of confounds.

Recommended choices:

- Primary window: CAR [-1,+1].
- Secondary windows: event day and CAR [-3,+3].
- Descriptive only: CAR [-7,+7].
- Benchmark 1: SPY for broad market adjustment.
- Benchmark 2: SMH or SOX for semiconductor-sector adjustment.
- Exclude or flag observations with earnings announcements in the event window.
- Flag major macro announcements and Federal Reserve events.

### Strongest Reviewer Attack

Even short windows may be contaminated because policy announcements are anticipated or released after market close. Event dates may not capture the true information shock.

### Defence

Use alternative event dates for major legislative events where necessary: passage, signing, and award announcements. Treat highly anticipated legislation as weaker evidence than named preliminary funding terms. The strongest events are firm-specific funding announcements because they are more discrete than broad legislative milestones.

## 8. External Validity

### Strongest Design Choice

External validity should be presented cautiously. The design tests the mechanism in a strategically important, policy-salient, public-market sector. It does not test all geopolitical competition.

The theory may travel best to:

- Defence procurement.
- Energy security investment.
- Critical minerals.
- AI infrastructure.
- Telecommunications trusted-vendor policy.
- Supply-chain chokepoints with state-backed relocation.

### Strongest Reviewer Attack

Semiconductors are exceptional. The sector has unusual capital intensity, strategic salience, AI exposure, public subsidies, and globally traded firms. Results may not travel.

### Defence

Frame semiconductors as a most-likely case for the State Support mechanism. If the mechanism does not appear there, the broader theory is in trouble. If it appears there, the thesis establishes plausibility, not universality. Later work can test defence, energy, and critical minerals.

## 9. Reviewer Criticisms

### Criticism 1: This is just an event study of subsidies.

Defence:

The project is not about subsidies in general. It is about state support in strategically important sectors under geopolitical competition. The design includes threat-dominant contrast events and strategic framing to test whether state support converts geopolitical risk into market opportunity.

### Criticism 2: Markets anticipated the announcements.

Defence:

Anticipation is real. The design codes anticipated events as weaker tests and emphasizes discrete firm-specific awards or preliminary terms. The thesis will not treat broad legislative signing dates as clean shocks.

### Criticism 3: Semiconductor stocks moved because of AI, not geopolitics.

Defence:

Use sector-adjusted returns and compare named beneficiaries to semiconductor peers. If results disappear after sector adjustment, the theory is weakened.

### Criticism 4: Strategic importance is circular.

Defence:

Strategic importance is not inferred from returns. It is established before outcomes using policy framing, sector role, and national-security relevance. It is treated as a scope condition, not the dependent variable.

### Criticism 5: State support may signal weakness, not opportunity.

Defence:

That is a valid rival interpretation and should be treated as a falsification pathway. If supported firms underperform peers, the thesis should conclude that state support was interpreted as weakness, burden, or insufficient compensation.

### Criticism 6: Positive market reactions may be temporary or irrational.

Defence:

The theory concerns market reactions and expectations, not long-run policy success. Persistence can be discussed as a limitation or extension, but the master's thesis should not claim durable welfare gains.

## 10. What Would Genuinely Support the State Support Mechanism?

The evidence would be genuinely supportive if several conditions appear together:

- Direct state-support announcements produce positive abnormal returns for named or clearly eligible beneficiaries.
- Those returns are positive relative to both broad market and semiconductor-sector benchmarks.
- Sector peers that are not named or less directly eligible react less strongly.
- Threat-dominant export-control events produce negative or mixed reactions for exposed firms.
- Support events generate clearer positive reactions than restriction-only events.
- Results are not driven by one event.
- The strongest positive reactions occur when support is specific, funded, and strategically framed.
- Event notes show that support plausibly affects future cash flows, capital costs, capacity expansion, or downside protection.

The minimum credible finding is:

> Named beneficiaries of semiconductor state-support announcements show positive short-window abnormal returns relative to semiconductor benchmarks, while threat-dominant semiconductor restriction events do not produce comparable positive effects for exposed firms.

## Complete Research Design Freeze V1 Outline

## Proposed Dissertation Title

**State-Backed Opportunity Under Geopolitical Competition: Strategic Importance and Positive Market Reactions**

## Research Question

When does geopolitical competition generate positive market reactions for strategically important firms or sectors through expected state support?

## Theory

Geopolitical competition increases the strategic importance of selected firms and sectors. Strategic importance alone does not create positive market reactions. Positive reactions become more likely when governments provide credible state support through subsidies, procurement, financing, protection, or industrial policy. Investors may interpret such support as improving expected cash flows or reducing downside risk.

## Empirical Focus

Semiconductor state-support and strategic industrial-policy announcements, with export-control events used as a limited threat-dominant contrast group.

## Unit of Analysis

Firm-event, supplemented by index-event comparisons.

## Event Universe

Primary events:

- CHIPS Act milestones.
- Named semiconductor subsidy or preliminary funding announcements.
- State-backed fab or capacity investment announcements.
- Semiconductor strategic industrial-policy announcements.

Contrast events:

- Export controls.
- Entity List additions.
- Restriction-only semiconductor policy shocks.

## Main Comparison Groups

- Named beneficiaries of state support.
- Semiconductor sector peers.
- Broad semiconductor benchmarks.
- Broad market benchmarks.
- Exposed firms in threat-dominant events.

## Dependent Variables

- Event-day abnormal return.
- CAR [-1,+1] as the primary outcome.
- CAR [-3,+3] as a secondary outcome.
- CAR [-7,+7] as descriptive only.

## Benchmarks

- SPY for broad market adjustment.
- QQQ for technology adjustment.
- SMH or SOX for semiconductor-sector adjustment.

## Hypotheses

H1 State Support Hypothesis:
State-support announcements will produce positive abnormal returns for named or clearly eligible beneficiaries.

H2 Strategic Importance Scope Hypothesis:
State-support effects will be strongest in strategically important semiconductor firms or capacity-linked firms.

H3 Threat Dominance Hypothesis:
Restriction-only geopolitical events will produce negative or mixed reactions for directly exposed firms.

H4 Substitution / Reallocation Hypothesis:
Restrictions may produce positive reactions for credible substitutes or trusted-location beneficiaries, but only where beneficiaries are identifiable before observing returns.

H5 Adaptation / Learning Hypothesis:
Repeated policy sequences may produce more differentiated reactions between threatened firms and supported beneficiaries.

## Identification Strategy

Use short-window event studies with pre-specified event dates, pre-specified assets, sector-adjusted returns, and transparent confound flags. Interpret results as evidence of market expectations, not definitive causal proof of long-term economic effects.

## Mechanism Test

The State Support mechanism is supported if direct, credible, strategically framed support announcements generate stronger positive abnormal returns for named beneficiaries than for sector peers, broad benchmarks, or threat-dominant contrast events.

## Alternative Explanations

- AI and semiconductor cycle.
- Earnings announcements.
- Macro and interest-rate news.
- Anticipation.
- Lobbying or political connections.
- Firm fundamentals.
- Subsidy as weakness signal.
- Broad risk-on market movement.

## Internal Validity Plan

- Freeze event list before collecting returns.
- Use narrow windows.
- Use sector benchmarks.
- Flag earnings and macro confounds.
- Keep null and ambiguous events.
- Avoid ex post beneficiary selection.

## External Validity Position

This is a most-likely test in semiconductors. Results may plausibly travel to defence, energy security, critical minerals, AI infrastructure, and telecom, but the dissertation will not claim universal generality.

## Falsification Conditions

The theory is weakened if named beneficiaries do not outperform sector benchmarks, if support events look no different from threat-dominant events, or if all positive results are explained by broad semiconductor rallies, earnings, or AI-cycle effects.

## Expected Contribution

The project contributes a narrower mechanism to geopolitical risk and political economy research:

> Markets may price geopolitical competition positively for selected strategic firms when states convert strategic importance into credible economic support.

## Proposal Defence Position

The dissertation should be defended as a modest, mechanism-focused event study. It does not prove that geopolitical competition is good, that state support succeeds, or that market reactions are rational. It tests whether credible state support is a visible channel through which geopolitical competition can generate positive market reactions for strategically important firms.
