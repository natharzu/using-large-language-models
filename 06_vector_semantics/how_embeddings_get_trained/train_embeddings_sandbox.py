"""How Embeddings Get Trained — Sandbox
J&M Speech and Language Processing, Chapter 6.

Objective:
    Train skip-gram embeddings with negative sampling from scratch.

Fill in each TODO, then run:
    python train_embeddings_sandbox.py
"""

from typing import List, Tuple
import numpy as np


def build_vocab(tokens: List[str]):
    # TODO: return word2id, id2word, and unigram frequency table
    raise NotImplementedError


def make_pairs(token_ids: List[int], window: int = 2) -> List[Tuple[int, int]]:
    # TODO: return list of (center, context) id pairs
    raise NotImplementedError


def train(pairs, vocab_size: int, dim: int = 50, epochs: int = 5, lr: float = 0.05):
    # TODO: init center/context matrices; SGD with sigmoid + negative sampling
    # TODO: print loss per epoch; return the embedding matrix
    raise NotImplementedError


def main() -> None:
    # TODO: load corpus -> tokens -> vocab -> pairs -> train -> inspect neighbors
    ...


if __name__ == "__main__":
    main()
