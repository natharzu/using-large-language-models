"""Attention — Sandbox
J&M Speech and Language Processing, Chapter 9.

Objective:
    Implement scaled dot-product attention and visualize real attention weights.

Fill in each TODO, then run:
    python attention_sandbox.py
"""

import numpy as np


def softmax(x: np.ndarray, axis: int = -1) -> np.ndarray:
    # TODO: numerically stable softmax
    raise NotImplementedError


def attention(Q: np.ndarray, K: np.ndarray, V: np.ndarray):
    # TODO: return (output, weights) where
    #       weights = softmax(Q @ K.T / sqrt(d_k)); output = weights @ V
    raise NotImplementedError


def main() -> None:
    # TODO: test attention() on small random Q, K, V; assert each weight row sums to 1
    # TODO (stretch): load a HuggingFace model with output_attentions=True
    #                 and plot one head's attention as a heatmap
    ...


if __name__ == "__main__":
    main()
