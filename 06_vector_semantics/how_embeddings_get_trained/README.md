# How Embeddings Get Trained

> J&M Ch. 6 · Concept note: *How Embeddings Get Trained*

## Objective

Understand the skip-gram-with-negative-sampling objective by training small embeddings from scratch on your own corpus.

## Dataset

Any tokenized text corpus in `data/` (the speeches corpus works well).

## Tasks

1. Build a vocabulary and (center, context) training pairs within a window.
2. Implement the skip-gram forward pass: dot product + sigmoid.
3. Train with negative sampling using gradient descent (NumPy or PyTorch).
4. Track the loss curve.
5. Inspect nearest neighbors of a few words and compare to the pretrained version.

## Success criteria

- Loss decreases over epochs.
- Learned neighbors are at least weakly sensible given the corpus size.

## Stretch

- Compare your trained vectors to `gensim.models.Word2Vec` on the same corpus.
