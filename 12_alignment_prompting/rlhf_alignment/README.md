# RLHF & Alignment

> J&M Ch. 12 · Concept note: *RLHF & Alignment*

## Objective

Understand the core of RLHF by training a small **reward model** on human preference pairs and using it to rank candidate responses.

## Dataset

Preference pairs `(prompt, chosen, rejected)` — a tiny hand-built set is fine, or a public preference dataset.

## Tasks

1. Encode each response (embeddings or a small encoder).
2. Train a reward model with the Bradley-Terry / pairwise logistic loss so `reward(chosen) > reward(rejected)`.
3. Evaluate pairwise accuracy on held-out pairs.
4. Use the reward model to re-rank N sampled responses (best-of-N).
5. Discuss how this reward signal would drive the PPO policy step (conceptually).

## Success criteria

- Reward model assigns higher scores to preferred responses above chance.
- A working best-of-N re-ranking demo.

## Stretch

- Add a KL penalty term and explain its role in keeping the policy near the base model.
