"""Classification Metrics — starter.

Build precision / recall / F1 from a confusion matrix, then sweep a threshold.
Fill in the TODOs. Run with: python metrics_sandbox.py
"""
from __future__ import annotations


def confusion_counts(
    y_true: list[int], y_pred: list[int]
) -> tuple[int, int, int, int]:
    """Return (tp, fp, fn, tn) for binary labels in {0, 1}."""
    # TODO: count the four cells without using a library.
    raise NotImplementedError


def precision(tp: int, fp: int) -> float:
    # TODO: tp / (tp + fp), guarding against division by zero.
    raise NotImplementedError


def recall(tp: int, fn: int) -> float:
    # TODO: tp / (tp + fn), guarding against division by zero.
    raise NotImplementedError


def f1(precision_value: float, recall_value: float) -> float:
    # TODO: harmonic mean of precision and recall.
    raise NotImplementedError


def sweep_threshold(
    y_true: list[int], scores: list[float]
) -> list[tuple[float, float, float]]:
    """Return (threshold, precision, recall) triples across thresholds 0..1."""
    # TODO: binarise scores at each threshold and compute P/R.
    raise NotImplementedError


def main() -> None:
    y_true = [1, 1, 0, 0, 1, 0]
    y_pred = [1, 0, 0, 1, 1, 0]
    tp, fp, fn, tn = confusion_counts(y_true, y_pred)
    p, r = precision(tp, fp), recall(tp, fn)
    print(f"P={p:.3f} R={r:.3f} F1={f1(p, r):.3f}")


if __name__ == "__main__":
    main()
