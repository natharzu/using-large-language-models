# Prompting & In-Context Learning

> J&M Ch. 12 · Concept note: *Prompting & In-Context Learning*

## Objective

Measure how prompt design (zero-shot vs. few-shot vs. chain-of-thought) changes task accuracy.

## Dataset

A small labeled classification set (e.g. sentence sentiment or stance).

## Tasks

1. Pick a generative model (local `transformers` pipeline or an API client).
2. Write a zero-shot prompt; measure accuracy on a held-out set.
3. Add k in-context examples (few-shot); measure again.
4. Add a chain-of-thought instruction; measure again.
5. Track how prompt length (tokens) grows with k.

## Success criteria

- An accuracy table across prompting styles.
- A note on the accuracy-vs-token-cost trade-off.

## Stretch

- Test sensitivity to example ordering and wording.
