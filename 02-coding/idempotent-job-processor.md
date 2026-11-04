# Coding challenge: Idempotent enterprise job processor

**Time:** 45–60 minutes · **Level:** production backend

## Situation

A customer sends webhook events to trigger report generation. Events contain `event_id`, `tenant_id`, `payload_hash`, and `created_at`. Delivery is at least once; consumers run concurrently. An upstream timeout may cause retransmission after the report has already been generated.

## Requirements

Implement an interface `process_event(event, store, generator) -> Result` that:

1. Processes a previously unseen `(tenant_id, event_id)` once.
2. Returns the previously stored result for an identical retry (same payload hash).
3. Rejects reuse of the same event ID with a different payload hash.
4. Prevents concurrent workers from generating duplicate reports.
5. Distinguishes transient failure, terminal failure, and completed processing.
6. Documents crash recovery between external side effect and persistence.

## Constraints and edge cases

- Two tenants may use the same event ID.
- Assume process crashes, slow downstream calls, and out-of-order delivery.
- Do not assume an in-memory lock works across machines.
- Exactly-once *effects* cannot be promised without downstream support; propose an idempotency key or reconciliation strategy.

## Interview discussion

- What unique index and transaction boundary do you use?
- How do you use a lease and fencing token to handle worker death?
- What happens when the external call succeeds but storing its result fails?
- What should retry/backoff and dead-letter policies be?
- Which metrics and alerts prove the system is operating safely?

## Self-assessment (10 points)

- Correct data model and tenant isolation: 2
- Concurrent deduplication / atomicity: 2
- Crash recovery / idempotent external side effects: 2
- Error semantics and tests: 2
- Observability / communication: 2

Avoid asserting that this question is used by OpenAI; it is an original practice prompt inspired by role-relevant engineering.
