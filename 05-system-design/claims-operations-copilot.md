# System design case: Claims operations copilot

**Original, hypothetical case; not an official OpenAI interview problem.**

## Customer brief

A mid-sized enterprise wants to reduce repetitive manual reviews of claims. Its employees consult internal policy PDFs, a claims API, and archived decisions. Users complain about inconsistent answers, stale policies, and slow turnaround. Sponsor requests an MVP in **six weeks**.

## Constraints

- 60,000 claims per month; not all require AI assistance.
- Policy documents change weekly; some cases include sensitive customer information.
- A mistake can trigger financial loss or regulatory escalation.
- The system must integrate with existing SSO, claims workflow, and audit systems.
- Human reviewers retain final authority for high-impact decisions.

## Candidate tasks

1. **Discover:** Which users, bottlenecks, workflow steps, quality baselines, and data owners matter?
2. **Scope:** Choose one low-risk sub-workflow for MVP; define explicit exclusions.
3. **Design:** Describe ingestion/versioning, access-filtered retrieval, evidence citations, policy validation, and review UX.
4. **Evaluate:** Propose a gold set and measures for evidence correctness, escalation, freshness, latency, and adoption.
5. **Protect:** Identify data handling, permissions, prompt injection, and approval controls.
6. **Roll out:** Use shadow mode → limited pilot → controlled expansion; name rollback triggers.
7. **Learn:** Summarize product improvements from systematic model failures.

## Architecture sketch

```text
SSO + tenant context -> Reviewer UI -> API / orchestration
                                      |-> scoped retrieval + policy-version check
                                      |-> model proposal (non-authoritative)
                                      |-> deterministic validation
                                      |-> human review for sensitive actions
                                      |-> audit / metrics / feedback
```

## Strong answer indicators

The candidate refuses to equate a demo with a deployment, defines acceptance criteria with the business owner, separates evidence from instructions, handles stale-policy failure, articulates a feasible 6-week cut, and explains measurable adoption and error reporting.

## Pressure follow-ups

- At week 3, retrieval quality is 72% on difficult cases. What changes?
- The compliance team prohibits storing full prompts. How do you debug responsibly?
- A key customer requests automatic approvals before evaluation gates pass. What do you say?
- How would you convey a failure pattern to central product/research teams?
