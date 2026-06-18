# Event Collection Protocol

## Purpose

This protocol defines how future events should be collected for the historical analogue dataset. The goal is to expand the evidence base without weakening transparency, source quality, or academic honesty.

## Inclusion Criteria

An event may be included if all conditions are met:

- The event has an identifiable public date.
- The event is relevant to geopolitical competition, strategic sectors, supply-chain security, industrial policy, sanctions, technology restrictions, or military/diplomatic pressure.
- The event can be assigned a dominant event family using `docs/event_family_taxonomy_v2.md`.
- The event has at least one reliable source.
- The event can be described without relying on post hoc market movement.
- The event adds useful historical comparison value beyond duplicating an already coded event.

## Exclusion Criteria

Exclude or defer events when:

- The date is unclear or cannot be tied to a public information release.
- The event is only rumor, speculation, or unsourced commentary.
- The event is selected only because a market move is already known.
- The event lacks a geopolitical, strategic, industrial-policy, military, sanctions, or supply-chain connection.
- The event is too broad to code even as a dominant family.
- The event cannot be sourced without relying on retrospective interpretation.

## Coding Standards

Required coding behaviour:

- Use stable event IDs and do not reuse IDs.
- Preserve the existing dissertation event IDs.
- Code only what the source supports.
- Use `TBD` or `Not coded` when evidence is insufficient.
- Keep `evidence_note` concise but specific.
- Separate support signals from pressure signals.
- Do not invent financial results or implied market impacts.

## Source Requirements

Preferred sources:

- official government releases;
- regulatory filings;
- company announcements;
- official agency notices;
- reputable wire services or major newspapers for same-day timing context.

Minimum source standard:

- one reliable dated source for event existence and timing;
- additional source if the event family, affected sector, or mechanism is ambiguous.

Avoid:

- unsourced social media;
- opinion-only commentary;
- post-event market recap articles as the primary basis for event coding;
- sources that do not clearly identify the event date.

## Documentation Requirements

Each added event should document:

- event title;
- event date;
- event family;
- country or region;
- affected sector;
- state-support signal;
- restriction or pressure signal;
- surprise level or `TBD`;
- market interpretation as a qualitative mechanism label;
- observed pathway;
- evidence note with source basis.

For each expansion batch, add a short note to the relevant methodology or summary document explaining:

- number of events added;
- event families added;
- source standard used;
- unresolved `TBD` fields;
- any changes to taxonomy or coding rules.

## Batch Expansion Workflow

1. Identify candidate events from source lists.
2. Screen candidates against inclusion and exclusion criteria.
3. Assign event family using the V2 taxonomy.
4. Draft event rows with conservative coding.
5. Validate the dataset.
6. Regenerate similarity, scenario, and observed pathway outputs.
7. Document the batch and any unresolved coding issues.

## Quality Guardrail

Dataset expansion should improve historical comparison, not create false precision. A smaller batch with strong sources is preferable to a larger batch with weak or ambiguous coding.
