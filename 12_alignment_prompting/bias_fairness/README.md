# Bias & Fairness in LLMs

> J&M Ch. 12 · Concept note: *Bias & Fairness in LLMs*

## Objective

Measure social bias in word embeddings or an LLM, and quantify it with a simple, reproducible metric.

## Dataset

Curated word lists (target groups + attribute words), and optionally template sentences.

## Tasks

1. Pick target sets (e.g. group A vs. group B terms) and attribute sets (e.g. career vs. family).
2. Implement a WEAT-style association score using cosine similarity of embeddings.
3. Report the effect size and a permutation-test p-value.
4. (LLM variant) Use template prompts and compare model probabilities/completions across groups.
5. Write up findings and limitations honestly.

## Success criteria

- A numeric bias score with a significance estimate.
- A careful written discussion of what the metric does and does not show.

## Stretch

- Compare bias before vs. after a simple debiasing projection.
