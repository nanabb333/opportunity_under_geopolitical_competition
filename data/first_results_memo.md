# First Results Memo

## Scope

This memo reports the first frozen core event-study outputs only. It does not discuss publication potential and does not generalize beyond the three main eligible support events.

## Evidence Classification Rule

- Primary evidence variable: car_sector_m1_p1.
- Supportive evidence: car_sector_m1_p1 > 0.25 percentage points and data_quality_flag is clean.
- Weak evidence: car_sector_m1_p1 > 0.25 percentage points but data quality or benchmark coverage is not clean.
- Null evidence: car_sector_m1_p1 is between -0.25 and +0.25 percentage points.
- Theory-weakening evidence: car_sector_m1_p1 < -0.25 percentage points.
- Pending: primary outcome cannot be calculated from available local price files.

## Event Results

### E009 / INTC

- Event description: Intel CHIPS Act preliminary terms announced (2024-03-20); named beneficiary asset: Intel Corporation.
- Event trading date used: 2024-03-20.
- Raw return: 0.36%.
- Market-adjusted return: -0.57% event-day; -2.48% CAR [-1,+1] versus SPY.
- Sector-adjusted return: -1.25% event-day; -4.32% CAR [-1,+1] versus SMH.
- Benchmark comparison: SPY CAR adjustment -2.48%; QQQ CAR adjustment -2.58%; SMH CAR adjustment -4.32%.
- Immediate interpretation: The beneficiary underperformed the semiconductor-sector benchmark in the primary window, which is inconsistent with the expected state-support opportunity reaction for this event.
- Evidence category: theory-weakening evidence.
- Calculation status: clean; all requested windows covered; t0=2024-03-20; first trading day on or after event date.

### E010 / TSM

- Event description: TSMC Arizona CHIPS Act preliminary terms announced (2024-04-08); named beneficiary asset: Taiwan Semiconductor Manufacturing Company ADR.
- Event trading date used: 2024-04-08.
- Raw return: 1.01%.
- Market-adjusted return: 0.96% event-day; 2.84% CAR [-1,+1] versus SPY.
- Sector-adjusted return: 0.82% event-day; 2.15% CAR [-1,+1] versus SMH.
- Benchmark comparison: SPY CAR adjustment 2.84%; QQQ CAR adjustment 2.48%; SMH CAR adjustment 2.15%.
- Immediate interpretation: The beneficiary outperformed the semiconductor-sector benchmark in the primary window, which is consistent with investors pricing credible state support as firm-specific opportunity.
- Evidence category: supportive evidence.
- Calculation status: clean; all requested windows covered; t0=2024-04-08; first trading day on or after event date.

### E012 / MU

- Event description: Micron CHIPS Act preliminary agreement announced (2024-04-25); named beneficiary asset: Micron Technology.
- Event trading date used: 2024-04-25.
- Raw return: -0.18%.
- Market-adjusted return: 0.20% event-day; 1.62% CAR [-1,+1] versus SPY.
- Sector-adjusted return: -2.18% event-day; -2.54% CAR [-1,+1] versus SMH.
- Benchmark comparison: SPY CAR adjustment 1.62%; QQQ CAR adjustment 0.74%; SMH CAR adjustment -2.54%.
- Immediate interpretation: The beneficiary underperformed the semiconductor-sector benchmark in the primary window, which is inconsistent with the expected state-support opportunity reaction for this event.
- Evidence category: theory-weakening evidence.
- Calculation status: clean; all requested windows covered; t0=2024-04-25; first trading day on or after event date.

## Guardrails

- The memo evaluates consistency with the frozen State Support mechanism only.
- It does not claim causal proof from three events.
- It does not interpret missing price rows as evidence.
