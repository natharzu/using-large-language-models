"""RNNs & LSTMs — starter.

Compare a vanilla RNN and an LSTM on a long-range copy task.
Fill in the TODOs. Run with: python rnn_sandbox.py
"""
from __future__ import annotations

import torch
import torch.nn as nn


def make_copy_task(
    n_samples: int, seq_len: int, gap: int, vocab_size: int = 8
) -> tuple[torch.Tensor, torch.Tensor]:
    """Return (inputs, targets) where the target is a token seen `gap` steps earlier."""
    # TODO: generate sequences where the label depends on a far-back token.
    raise NotImplementedError


class RecurrentClassifier(nn.Module):
    def __init__(self, vocab_size: int, hidden: int, cell: str = "rnn") -> None:
        super().__init__()
        # TODO: build an embedding + (nn.RNN or nn.LSTM) + linear head.
        raise NotImplementedError

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # TODO: run the recurrence and return logits from the final step.
        raise NotImplementedError


def train(model: nn.Module, data: tuple[torch.Tensor, torch.Tensor]) -> float:
    """Train the model and return final accuracy. Log gradient norms each step."""
    # TODO: standard training loop; record grad norms for the writeup.
    raise NotImplementedError


def main() -> None:
    data = make_copy_task(n_samples=2000, seq_len=30, gap=20)
    for cell in ("rnn", "lstm"):
        model = RecurrentClassifier(vocab_size=8, hidden=64, cell=cell)
        print(cell, "accuracy:", train(model, data))


if __name__ == "__main__":
    main()
