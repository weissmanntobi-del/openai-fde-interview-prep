# Evaluation framework for a deployed AI workflow

**Goal:** determine if a system is safe and useful for a particular customer's workflow, not merely whether responses sound plausible.

## 1. Define a contract

Example: A support copilot may recommend a refund of at most $100, but must never execute it without an independent policy check; restricted situations require human review. Model-generated text is untrusted input to the action layer.

## 2. Build a representative dataset

Sample from real workflows only with authorization and appropriate de-identification. Include common cases, rare high-severity cases, policy changes, out-of-distribution requests, multilingual inputs, and adversarial content. Track source, consent, version, and slices. The bundled synthetic samples contain no sensitive customer data.

## 3. Measure multiple dimensions

| Metric | Definition | Example release gate (illustrative, not universal) |
| --- | --- | --- |
| Decision accuracy | Correct decisions / cases | >= 90% on held-out routine cases |
| High-risk recall | Correctly escalated high-risk cases / total high-risk | 100% in explicitly enumerated critical test cases |
| Unsafe authorization | Executed unauthorized actions | 0 in test suite, plus independent enforcement |
| p95 latency | 95th percentile of end-to-end request times | customer-defined SLA |
| Human-review rate | Escalations / requests | track by task slice |
| Cost per completed workflow | total measured expense / completed workflows | compared with baseline |
| Business impact | saved handling time or fewer errors | validated with customer trial |

**Caution:** zero failures in a small test suite cannot guarantee real-world safety. Runtime authorization and monitoring are necessary.

## 4. Analyze failures

For each failure, record case ID, context, expected vs. actual action, severity, model/prompt/config version, likely root cause, and corrective action. Slice by policy category, customer segment, and data recency. Re-run the unchanged regression suite when prompts, retrieval, models, or tools change.

## 5. Release decision

Ship only if quality gates, action authorization, stakeholder sign-off, incident ownership, rollback strategy, data protections, and adoption measurement are satisfied. Record exceptions as explicit risk acceptance, not invisible scope reductions.

## Local example

Run `python -m examples.eval_lab.run_eval` and inspect the failing case. Modify the policy logic in `examples/eval_lab/policy.py`, then re-run tests and compare the report. The simulator has no LLM connection; it isolates measurable workflow logic.
