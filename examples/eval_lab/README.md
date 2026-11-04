# Runnable offline workflow evaluation lab

This lab uses a **toy, deterministic policy assistant**, not an LLM. It tests decision quality and escalation on a small synthetic fixture. It does not benchmark any OpenAI model or guarantee production safety.

## Run

```bash
python -m examples.eval_lab.run_eval
python -m unittest discover -s tests -v
```

## Exercise

Inspect `fixtures.jsonl` and `policy.py`. The fixture includes standard, high-value, fraud-flagged, missing-information, and out-of-policy cases. The baseline intentionally mishandles a flagged transaction. Locate the failure, write a regression test, fix the policy, rerun and explain why runtime authorization still must sit outside the assistant.

## Extend

Add slices for policy freshness, prompt injection, missing customer records, tenant isolation, tool-call authorization, and abstention. Version prompts/models and run on held-out data if integrating a live model later. Never commit secrets or private production records.
