# Embeddings

> J&M Ch. 6 · Concept note: *Embeddings*

## Objective

Load pretrained embeddings, measure similarity with cosine, and explore analogies and clustering on political vocabulary.

## Dataset

Pretrained vectors (GloVe via `gensim`, or `sentence-transformers` for sentence embeddings) plus a list of political terms.

## Tasks

1. Load pretrained word vectors.
2. Compute cosine similarity between word pairs (e.g. *senate/congress*, *liberal/conservative*).
3. Find nearest neighbors of several political terms.
4. Try the analogy `king - man + woman` and a political analogy.
5. Reduce a set of terms to 2D (PCA/t-SNE) and plot the clusters.

## Success criteria

- Neighbors and similarities are intuitively sensible.
- A 2D plot showing meaningful clusters.

## Stretch

- Embed full sentences with `sentence-transformers` and cluster speeches by topic.
