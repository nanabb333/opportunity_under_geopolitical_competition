# Local Price Validation Report

## Scope

This report validates the local manually downloaded price-data pathway only. It does not interpret returns.

## Local Price Directory

- Expected directory: /Users/NaNabb/Documents/Opportunity Under Geopolitical Competition/data/raw_prices

## Frozen Core Rows Re-Run

- E009 / INTC: Intel CHIPS Act preliminary terms announced
- E010 / TSM: TSMC Arizona CHIPS Act preliminary terms announced
- E012 / MU: Micron CHIPS Act preliminary agreement announced

## Files Found

- A001 SPY: 84 rows
- A002 QQQ: 84 rows
- A003 SMH: 84 rows
- A005 INTC: 84 rows
- A006 TSM: 84 rows
- A007 MU: 84 rows

## Missing or Unusable Files

- No required local price files are missing.

## Output Counts

- market_returns.csv rows: 504
- event_firm_returns.csv rows: 3
- rows with primary outcome car_sector_m1_p1 calculated: 3
- rows still missing primary outcome car_sector_m1_p1: 0

## Event-Window Coverage

- All core rows have requested event-window coverage.

## Rows Successfully Calculated

- E009/A005: car_sector_m1_p1 calculated; t0=2024-03-20
- E010/A006: car_sector_m1_p1 calculated; t0=2024-04-08
- E012/A007: car_sector_m1_p1 calculated; t0=2024-04-25

## Rows Still Missing

- None.

## Schema and Key Validation

- No schema/key integrity issues detected before local return construction.

## Post-Freeze Guardrails

- No theory, event-universe, or frozen sample-logic changes were made.
- This run is limited to E009/INTC, E010/TSM, and E012/MU plus SMH, SPY, and QQQ price inputs.
- Adj Close is used when available; Close is used only when Adj Close is absent.
