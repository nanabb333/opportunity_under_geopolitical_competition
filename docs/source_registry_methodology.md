# Source Registry Methodology

## Purpose

`data/source_registry.csv` defines the source categories that should guide future event monitoring. The registry is not a scraping configuration and does not authorise automated collection. It is a research-control document for source selection, review priorities, and reliability assessment.

## Source Selection

Sources should be selected when they can support at least one of the following tasks:

- identify geopolitical or industrial-policy events
- verify official event timing
- clarify affected sectors or firms
- document state support or restriction signals
- provide context for historical interpretation

Primary sources should be preferred when available. News and analytical sources are useful for discovery and context, but major event coding should be corroborated before integration into the approved dataset.

## Reliability Assessment

Reliability levels should be assigned conservatively:

- `High`: official government releases, regulatory notices, statutory records, sanctions databases, stock-exchange filings, or company primary disclosures.
- `Medium-High`: source classes with strong domain authority but possible interpretation or timing issues, such as defence briefings or company investor-relations materials.
- `Medium`: reputable financial press, specialised industry press, think-tank analysis, or research reports that require corroboration before event integration.
- `Low`: social media, unsourced commentary, rumor-driven reporting, or claims that cannot be verified. Low-reliability sources should not be used as the sole basis for event coding.

## Update Priorities

Update priority should be based on:

- strategic relevance to semiconductors, AI chips, defence technology, industrial policy, or supply-chain relocation
- likely event-family coverage gap
- source reliability
- clarity of event date
- whether the item changes support, pressure, or market-interpretation coding

High-priority categories include export restrictions, major subsidy awards, military activity near semiconductor supply-chain nodes, sanctions, and strategic investment announcements.

## Inclusion Standards

A source category belongs in the registry if it is useful for repeatable monitoring. A specific candidate event belongs in the dataset only after human review confirms:

- event-level significance
- source documentation
- codeable date and title
- event-family fit
- clear support or pressure signal
- transparent evidence note

The registry should not be treated as a claim that every listed source item is relevant or dataset-ready.
