"""Embeddings — Sandbox
J&M Speech and Language Processing, Chapter 6.

Objective:
    Explore pretrained embeddings: cosine similarity, neighbors, analogies, clustering.

Fill in each TODO, then run:
    python embeddings_sandbox.py
"""

from typing import List
import numpy as np

TERMS: List[str] = ["senate", "congress", "liberal", "conservative", "election", "policy"]


def load_vectors():
    # TODO: load pretrained vectors, e.g. gensim.downloader.load('glove-wiki-gigaword-100')
    raise NotImplementedError


def cosine(a: np.ndarray, b: np.ndarray) -> float:
    # TODO: return cosine similarity between vectors a and b
    raise NotImplementedError


def main() -> None:
    # TODO: load vectors
    # TODO: print cosine similarity for a few political word pairs
    # TODO: print nearest neighbors for each term in TERMS
    # TODO: run one analogy and one 2D projection plot (matplotlib)
    ...


if __name__ == "__main__":
    main()
