# Pretraining vs. Fine-tuning

> J&M Ch. 10 · Concept note: *Pretraining vs. Fine-tuning*

## Objective

Feel the difference between a general pretrained model and a task-adapted one by fine-tuning a small model (full or LoRA/PEFT) on a classification task.

## Dataset

A small labeled text dataset (reuse Ch. 5).

## Tasks

1. Evaluate a pretrained model zero-shot / with a frozen classifier head.
2. Fine-tune the model (or attach a LoRA adapter via `peft`) on the training set.
3. Compare metrics before vs. after fine-tuning.
4. Report trainable parameter counts (full vs. LoRA).
5. Discuss compute/quality trade-offs.

## Success criteria

- A clear before/after metrics table.
- An understanding of why LoRA trains far fewer parameters.

## Stretch

- Vary the amount of training data and plot the learning curve.
