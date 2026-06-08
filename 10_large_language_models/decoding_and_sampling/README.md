# Decoding & Sampling

> J&M Ch. 10 · Concept note: *Decoding & Sampling*

## Objective

See how decoding strategy changes generated text: greedy, beam search, temperature, top-k, and top-p (nucleus).

## Dataset

A few prompts (inline).

## Tasks

1. Load a small generative model (e.g. `gpt2` or `distilgpt2`).
2. Generate from the same prompt with greedy, beam, and sampling settings.
3. Sweep temperature (0.2, 0.7, 1.2) and observe diversity vs. coherence.
4. Compare top-k vs. top-p for the same temperature.
5. Write up which setting you'd choose for (a) factual summaries, (b) creative drafts.

## Success criteria

- A table of outputs across strategies for one prompt.
- A short rationale linking each setting to its behavior.

## Stretch

- Plot the next-token probability distribution before/after temperature scaling.
