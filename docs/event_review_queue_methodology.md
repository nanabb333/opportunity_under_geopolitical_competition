# Event Review Queue Methodology

## Purpose

`data/event_review_queue.csv` is the operating queue for candidate geopolitical and industrial-policy events. It separates unapproved candidate events from the approved historical analogue dataset.

The queue supports a semi-automated workflow, but it does not approve events automatically. Human review remains required before any candidate enters `data/historical_analogue_events.csv`.

## Queue Lifecycle

1. A candidate item is identified from a monitored source category.
2. The item is added to the queue with a stable `queue_id`.
3. The candidate receives an initial `candidate_status`.
4. A reviewer is assigned.
5. The reviewer checks source quality, event significance, date clarity, and coding fit.
6. The reviewer records `review_status`, `review_date`, `final_decision`, and `notes`.
7. Approved items move to dataset integration. Rejected items remain in the queue for auditability.

## Review Process

Review should check:

- whether the source is reliable enough for event coding
- whether the event is specific and dateable
- whether it fits an existing event family
- whether the affected sector and geography can be coded
- whether support or pressure signals are evident
- whether uncertainty should be marked as `TBD` or `Not coded`

The queue is allowed to contain incomplete candidate records. The approved dataset is not.

## Approval Process

A candidate may be approved when:

- source documentation is sufficient
- event date and title are clear
- event-family coding is defensible
- evidence notes are transparent
- the event improves the historical analogue evidence base

Approval does not require a known market result. The project should not invent financial precision.

## Rejection Process

A candidate should be rejected or deferred when:

- the source cannot be verified
- the item is too vague or routine
- the date is unclear
- the event is outside the project scope
- coding would require unsupported assumptions

Rejected candidates should keep a reviewer note explaining the decision.

## Audit Trail

The queue preserves operational accountability through:

- stable queue IDs
- source name and URL
- assigned reviewer
- review date
- final decision
- notes

The audit trail helps distinguish candidate intelligence from approved historical evidence.
