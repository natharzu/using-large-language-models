# Hallucination & Validation

> J&M Ch. 14 · Concept note: *Hallucination & Validation*

## Objective

Detect when a generated answer is **not grounded** in the retrieved context and quantify how often it happens.

## Dataset

Question/answer pairs produced by your RAG pipeline, plus the contexts used.

## Tasks

1. Generate answers with and without relevant context.
2. Implement a grounding check: does each answer sentence have support in the context? (entailment model or embedding overlap).
3. Flag unsupported claims as potential hallucinations.
4. Compute a hallucination rate across a question set.
5. Test mitigations: tighter prompts, a 'say I don't know' instruction, lower temperature.

## Success criteria

- A grounding/verification function returning per-claim support.
- A measured hallucination rate before vs. after mitigation.

## Stretch

- Use an NLI model (entailment/contradiction/neutral) for the grounding check.
