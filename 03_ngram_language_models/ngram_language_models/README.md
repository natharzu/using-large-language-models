# N-gram Language Models

> J&M Ch. 3 · Concept note: *N-gram Language Models*

## Objective

Build a bigram and trigram language model from a text corpus, apply smoothing, and generate new text.

## Dataset

A corpus of political speeches or any plain-text file in `data/` (a few thousand sentences is plenty).

## Tasks

1. Tokenize the corpus and pad each sentence with `<s>` / `</s>`.
2. Count unigram, bigram, and trigram frequencies.
3. Estimate next-word probabilities with **add-k (Laplace) smoothing**.
4. Generate text by sampling from the model.
5. Compare bigram vs. trigram fluency.

## Success criteria

- Probabilities for a given context sum to 1.
- Generated trigram text is visibly more fluent than bigram text.

## Stretch

- Implement simple backoff from trigram → bigram → unigram.
