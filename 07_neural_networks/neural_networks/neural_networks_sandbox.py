"""Neural Networks — Sandbox
J&M Speech and Language Processing, Chapter 7.

Objective:
    Feed-forward (MLP) text classifier in PyTorch vs. logistic regression baseline.

Fill in each TODO, then run:
    python neural_networks_sandbox.py
"""

import torch
import torch.nn as nn


class MLP(nn.Module):
    def __init__(self, input_dim: int, hidden_dim: int, num_classes: int):
        super().__init__()
        # TODO: define Linear -> ReLU -> (Dropout) -> Linear

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # TODO: return logits
        raise NotImplementedError


def train(model, X_train, y_train, X_val, y_val, epochs: int = 20, lr: float = 1e-3):
    # TODO: CrossEntropyLoss + Adam; loop epochs; print train/val loss
    raise NotImplementedError


def main() -> None:
    # TODO: build tensors from the Ch.5 dataset
    # TODO: train MLP, evaluate, compare to logistic regression
    ...


if __name__ == "__main__":
    main()
