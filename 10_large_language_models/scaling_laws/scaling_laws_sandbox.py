"""Scaling Laws & Model Size — Sandbox
J&M Speech and Language Processing, Chapter 10.

Objective:
    Fit and interpret a power-law scaling curve of loss vs. model size.

Fill in each TODO, then run:
    python scaling_laws_sandbox.py
"""

import numpy as np


def power_law(N, a, b, c):
    return a * np.power(N, -b) + c


def main() -> None:
    # TODO: define arrays of model sizes (N) and observed losses (L)
    # TODO: fit power_law with scipy.optimize.curve_fit
    # TODO: plot data + fitted curve on log-log axes (matplotlib)
    # TODO: print fitted a, b, c and interpret them
    ...


if __name__ == "__main__":
    main()
