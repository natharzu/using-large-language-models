"""Inter-rater Reliability — starter.

Compute percent agreement and Cohen's kappa from scratch; expose the
base-rate trap. Fill in the TODOs. Run with: python irr_sandbox.py
"""
from __future__ import annotations


def percent_agreement(a: list[str], b: list[str]) -> float:
    """Fraction of items where two annotators agree."""
    # TODO: compare label-by-label.
    raise NotImplementedError


def cohens_kappa(a: list[str], b: list[str]) -> float:
    """Cohen's kappa: (p_o - p_e) / (1 - p_e)."""
    # TODO: compute observed agreement p_o and expected agreement p_e.
    raise NotImplementedError


def base_rate_trap_demo() -> None:
    """Build a high-agreement, near-zero-kappa example and print both."""
    # TODO: construct heavily imbalanced labels and show the gap.
    raise NotImplementedError


def main() -> None:
    a = ["pos", "pos", "neg", "pos", "neg"]
    b = ["pos", "neg", "neg", "pos", "neg"]
    print("percent agreement:", percent_agreement(a, b))
    print("cohen's kappa:", cohens_kappa(a, b))
    base_rate_trap_demo()


if __name__ == "__main__":
    main()
