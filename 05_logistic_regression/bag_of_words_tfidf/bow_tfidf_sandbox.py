"""Bag of Words & TF-IDF — starter.

Build a document-term matrix and TF-IDF weighting from scratch.
Fill in the TODOs. Run with: python bow_tfidf_sandbox.py
"""
from __future__ import annotations

import math
from collections import Counter


def tokenize(text: str) -> list[str]:
    """Lowercase and split into tokens."""
    # TODO: return a list of tokens (start simple, refine later).
    raise NotImplementedError


def build_vocab(docs: list[str]) -> dict[str, int]:
    """Map each token to a stable column index."""
    # TODO: build the vocabulary from the tokenized corpus.
    raise NotImplementedError


def count_matrix(docs: list[str], vocab: dict[str, int]) -> list[list[int]]:
    """Return a document-term count matrix."""
    # TODO: fill rows with per-document token counts.
    raise NotImplementedError


def tfidf(matrix: list[list[int]]) -> list[list[float]]:
    """Apply tf * log(N / df) weighting to a count matrix."""
    # TODO: compute document frequency per term, then weight each cell.
    raise NotImplementedError


def main() -> None:
    docs = [
        "the senate voted to pass the bill",
        "the house rejected the amendment",
    ]
    vocab = build_vocab(docs)
    counts = count_matrix(docs, vocab)
    print("vocab size:", len(vocab))
    print("tfidf:", tfidf(counts))


if __name__ == "__main__":
    main()
