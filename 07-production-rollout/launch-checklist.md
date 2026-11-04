# AI deployment readiness and incident playbook

## Before pilot

- [ ] Business owner approved use case, exclusions, and target workflow.
- [ ] Dataset provenance and privacy controls documented.
- [ ] Access controls and tenant isolation tested.
- [ ] Model proposals are separate from trusted tool authorization.
- [ ] Golden eval set versioned; high-severity cases reviewed.
- [ ] Monitoring: p50/p95 latency, error types, cost, unsafe attempts, human-review rate, adoption.
- [ ] Load/timeout/backoff and dependency failure tests complete.
- [ ] On-call owner, rollback switch, and incident communication channel identified.
- [ ] Frontline operators trained; manual fallback documented.

## Production incident drill

**Scenario:** A policy update is not reflected in retrieval. Twenty users received outdated guidance in 30 minutes.

1. Triage and contain: disable the affected workflow or force human review.
2. Assess blast radius: isolate impacted time period, policy version, users, and outputs.
3. Preserve appropriately minimized telemetry, protect customer data.
4. Notify accountable customer and internal stakeholders per agreement.
5. Repair index/policy freshness, replay test cases and run regression suite.
6. Restore in stages only after an explicit release gate.
7. Publish a blameless retrospective: root cause, detection gap, prevention, owner, date.

## Field-to-product feedback memo

**Observed limitation:** ...
**Evidence & sample size:** ...
**Reproduction conditions:** ...
**Customer impact:** ...
**Workaround:** ...
**Reusable product or platform improvement:** ...
**Owner, validation, and next decision:** ...
