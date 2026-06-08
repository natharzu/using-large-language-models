"""Perplexity & LM Evaluation — Sandbox
J&M Speech and Language Processing, Chapter 3.

Objective:
    Compute perplexity of an n-gram model on held-out text.

Fill in each TODO, then run:
    python perplexity_sandbox.py
"""

import math
from typing import List


def train_test_split(sentences: List[List[str]], frac: float = 0.8):
    # TODO: return (train, test)
    raise NotImplementedError


def log_prob_of_corpus(sentences: List[List[str]], n: int, k: float = 1.0) -> float:
    # TODO: sum log2 P(word | context) over every token in `sentences`
    raise NotImplementedError


def perplexity(log2_prob: float, num_tokens: int) -> float:
    # TODO: H = -log2_prob / num_tokens ; return 2 ** H
    raise NotImplementedError


def main() -> None:
    # TODO: train on train split, evaluate perplexity on test split for n=2 and n=3
    # TODO: sweep k in {0.1, 0.5, 1.0} and report perplexity
    ...


if __name__ == "__main__":
    main()
