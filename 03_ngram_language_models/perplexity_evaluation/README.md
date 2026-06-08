# Perplexity & LM Evaluation

> J&M Ch. 3 · Concept note: *Perplexity & LM Evaluation*

## Objective

Measure how well a language model predicts held-out text using **perplexity**, and connect it to cross-entropy.

## Dataset

Split your Ch. 3 corpus into train/test (e.g. 80/20).

## Tasks

1. Train an n-gram model on the training split (reuse the previous exercise).
2. Compute the log-probability of the test split.
3. Convert to per-word cross-entropy and then perplexity: `PP = 2 ** H`.
4. Compare perplexity for bigram vs. trigram and for different smoothing values of k.
5. (Optional) Compute perplexity of a pretrained model (e.g. GPT-2) on the same text and compare orders of magnitude.

## Success criteria

- Lower perplexity corresponds to the model you'd judge more fluent.
- You can explain why perplexity is the exponentiated average negative log-likelihood.

## Stretch

- Plot perplexity as a function of k.
