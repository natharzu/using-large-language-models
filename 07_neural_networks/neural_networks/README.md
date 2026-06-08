# Neural Networks

> J&M Ch. 7 · Concept note: *Neural Networks*

## Objective

Build a feed-forward neural network text classifier in PyTorch and compare it to the Ch. 5 logistic regression baseline.

## Dataset

Reuse the labeled text dataset from Chapter 5.

## Tasks

1. Vectorize text (TF-IDF or averaged embeddings) into input tensors.
2. Define an MLP: `Linear -> ReLU -> Linear -> softmax`.
3. Train with cross-entropy loss and an Adam optimizer; track train/val loss.
4. Evaluate accuracy/F1 and compare to logistic regression.
5. Experiment with hidden size, dropout, and learning rate.

## Success criteria

- A training loop that converges with a decreasing loss curve.
- A fair comparison table vs. the logistic regression baseline.

## Stretch

- Swap TF-IDF inputs for averaged pretrained embeddings and compare.
