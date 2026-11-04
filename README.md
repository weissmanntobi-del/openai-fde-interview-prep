# OpenAI Forward Deployed Engineer (FDE) Interview Preparation

**Free, hands-on preparation for production AI delivery, evaluation, coding, customer discovery, and technical ownership.**

[![Tests](https://img.shields.io/badge/tests-unittest-blue)](#run-the-free-evaluation-lab) [![Python](https://img.shields.io/badge/python-3.10%2B-blue)](#run-the-free-evaluation-lab) [![Independent](https://img.shields.io/badge/resource-independent-informational)](#disclaimer)

> **Start here:** Try the 20-minute [evaluation lab](examples/eval_lab/README.md), then review the [scoring rubric](08-mock-interviews/scoring-rubric.md) and [7-day plan](09-7-day-plan/README.md).

This independent practice repository is **informed by the publicly listed responsibilities** of the OpenAI Forward Deployed Engineer (FDE) role in San Francisco. It does **not** claim to document the company's interview process or disclose actual interview questions.

OpenAI FDE Interview Preparation :  https://tobiweissmann.gumroad.com/l/wsyhmd

AI FDE Interview Bundle: https://tobiweissmann.gumroad.com/l/bciwd

## Why this repository is different

A successful deployment is not just an impressive model demo. Practice the complete chain:

**Discover workflow → define measurable acceptance criteria → design → implement → evaluate → deploy → drive adoption → feed learning back into the product.**

| Public role expectation | Free practice artifact |
| --- | --- |
| Customer discovery and scoping | [Discovery template and role-play](06-customer-discovery/discovery-workshop.md) |
| Hands-on Python engineering | [Idempotent job processor exercise](02-coding/idempotent-job-processor.md) |
| Evaluation-driven feedback | [Runnable offline eval lab](examples/eval_lab/README.md) |
| Enterprise LLM/agent integration | [Safe tool-use design challenge](04-agentic-systems/agent-approval-gateway.md) |
| Production reliability and rollout | [Deployment and incident playbook](07-production-rollout/launch-checklist.md) |
| Full-stack and architectural trade-offs | [Case study: claims operations copilot](05-system-design/claims-operations-copilot.md) |
| Stakeholder judgment and clear communication | [Mock interview + rubric](08-mock-interviews/README.md) |

## Free learning path

1. **Understand the role:** [Role map](01-role-roadmap/README.md).
2. **Write code:** [Coding prompt](02-coding/idempotent-job-processor.md) with tests/specification.
3. **Evaluate behavior:** run the deterministic local evaluation harness.
4. **Reason about agents:** design tool authorization and human approval.
5. **Design a customer deployment:** work the claims operations case study.
6. **Practice customer delivery:** use the workshop and launch checklist.
7. **Simulate an interview:** use structured practice and score yourself.

## Run the free evaluation lab

No API key, paid SDK, external service, or production customer data required.

```bash
python -m unittest discover -s tests -v
python -m examples.eval_lab.run_eval
```

The fixture evaluates an **illustrative deterministic assistant**, not OpenAI model quality. It measures exact workflow policy decisions, human-review escalation, and tool-authority boundaries. The included example has an intentionally imperfect decision to make failure analysis concrete. See [eval methodology](03-evals/evaluation-framework.md).

## Featured free challenges

### Challenge A — Idempotent ingestion service (45 min)
An enterprise integration receives retries and duplicate webhook events. Design a processing function with durable idempotency, conflict handling, safe retries, and concurrency tests. [Read challenge](02-coding/idempotent-job-processor.md).

### Challenge B — Unsafe agent tool call (40 min)
An agent reads an untrusted support ticket and proposes a refund. Define a **separate trusted policy decision** and approval before executing a money-moving tool. [Read challenge](04-agentic-systems/agent-approval-gateway.md).

### Challenge C — Enterprise claims copilot (60 min)
A customer needs a useful claims-review copilot within 6 weeks, with hard constraints on auditability and accuracy. Make scope/quality/schedule trade-offs and design a phased rollout. [Read case](05-system-design/claims-operations-copilot.md).

## Want deeper, structured practice?

This repository provides **substantial free sample exercises and runnable code**. For a future extended OpenAI FDE preparation pack, potential additions include scored mock interviews, complete reference implementations, additional eval datasets, architecture reviews, incident labs, and a candidate/instructor workbook.

**OpenAI-specific paid bundle:** https://tobiweissmann.gumroad.com/l/wsyhmd


If this repository helps, **star** it and share it with another engineer. For corrections or new practice cases, see [CONTRIBUTING](CONTRIBUTING.md).

## Disclaimer

Independent educational material. **Not affiliated with, sponsored by, or endorsed by OpenAI.** References to OpenAI identify the job profile being studied. Scenarios are original, hypothetical practice cases; not leaked, verified, or official interview prompts. Do not send real credentials or customer information to this repo.

**License:** MIT for repository-authored text and code; see [LICENSE](LICENSE).
