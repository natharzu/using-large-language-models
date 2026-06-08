"""Bias & Fairness in LLMs — Sandbox
J&M Speech and Language Processing, Chapter 12.

Objective:
    Quantify embedding/LLM social bias with a WEAT-style association score.

Fill in each TODO, then run:
    python bias_fairness_sandbox.py
"""

from typing import List
import numpy as np

TARGET_A: List[str] = []   # TODO: fill target group A terms
TARGET_B: List[str] = []   # TODO: fill target group B terms
ATTR_X: List[str] = []     # TODO: fill attribute set X
ATTR_Y: List[str] = []     # TODO: fill attribute set Y


def association(word_vec, attr_x_vecs, attr_y_vecs) -> float:
    # TODO: mean cosine(word, X) - mean cosine(word, Y)
    raise NotImplementedError


def weat_effect_size(a_vecs, b_vecs, x_vecs, y_vecs) -> float:
    # TODO: standardized mean difference of associations between A and B
    raise NotImplementedError


def main() -> None:
    # TODO: load embeddings, compute WEAT effect size + permutation p-value
    # TODO: write a short, honest interpretation
    ...


if __name__ == "__main__":
    main()
