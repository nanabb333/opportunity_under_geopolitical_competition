# Opportunity Under Geopolitical Competition

This repository contains a research portfolio on how geopolitical competition can create market opportunity for selected firms and sectors. The project focuses on cases where strategic importance and credible state support may lead investors to price geopolitical pressure as more than downside risk.

## Research Question

When do financial markets interpret geopolitical competition as a source of opportunity for strategically important firms or sectors?

## Puzzle

Geopolitical competition is usually treated as a source of risk: uncertainty, restrictions, supply-chain disruption, and market-access loss. Yet some firms and sectors may gain when states respond with subsidies, procurement, protection, financing, or industrial-policy commitments. The puzzle is why markets sometimes price geopolitical pressure as opportunity for selected actors rather than only as aggregate risk.

## Mechanism

The proposed mechanism is state-backed opportunity:

```text
Geopolitical competition
        |
        v
Strategic importance
        |
        v
Expected state support
        |
        v
Investor interpretation
        |
        v
Market reaction
```

The theory does not claim that geopolitical competition is broadly positive for markets. It expects heterogeneous effects: firms exposed mainly to restrictions or uncertainty may lose value, while firms expected to receive credible support may experience positive reactions.

## Research Design

The current design uses a focused event-study approach in semiconductors and semiconductor-linked strategic industrial policy. It compares named beneficiaries, eligible sector peers, threat-exposed firms, and market benchmarks around support and restriction events. The main outcomes are event-day returns and short-window cumulative abnormal returns.

## Current Status

The repository contains frozen theory, research design, dataset, and event-asset coding files. The event-study pipeline is operational, and initial empirical outputs for the focal event sample have been validated.

## Reproducibility

Run the event-study pipeline with:

```bash
python3 scripts/build_event_returns.py
```

Required inputs:

- `data/events.csv`
- `data/assets.csv`
- `data/event_asset_links.csv`
- `data/raw_prices/*.csv`

Expected outputs:

- `data/market_returns.csv`
- `data/event_firm_returns.csv`
- `data/local_price_validation_report.md`

## Repository Structure

- `docs/`: frozen research design, protocol, theory, sample, and pilot documents.
- `data/`: event, asset, and event-asset link tables, plus local raw price inputs when available.
- `scripts/`: reproducible scripts for building market return and event-study files.
