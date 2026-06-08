"""RLHF & Alignment — Sandbox
J&M Speech and Language Processing, Chapter 12.

Objective:
    Train a reward model on preference pairs and use it for best-of-N re-ranking.

Fill in each TODO, then run:
    python rlhf_sandbox.py
"""

from typing import List, Tuple
import torch
import torch.nn as nn

# (prompt, chosen, rejected)
PREFERENCES: List[Tuple[str, str, str]] = []


class RewardModel(nn.Module):
    def __init__(self, input_dim: int):
        super().__init__()
        # TODO: a small head mapping a response embedding -> scalar reward

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        raise NotImplementedError


def pairwise_loss(chosen_reward, rejected_reward):
    # TODO: -log(sigmoid(chosen_reward - rejected_reward)) averaged
    raise NotImplementedError


def main() -> None:
    # TODO: embed responses, train RewardModel with pairwise_loss
    # TODO: report pairwise accuracy; demo best-of-N re-ranking
    ...


if __name__ == "__main__":
    main()
