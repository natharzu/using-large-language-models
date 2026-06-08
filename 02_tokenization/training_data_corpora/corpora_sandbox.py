"""Training Data & Corpora — starter.

Profile a political-text corpus: size, vocabulary, duplication, and balance.
Fill in the TODOs. Run with: python corpora_sandbox.py
"""
from __future__ import annotations

from collections import Counter
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[2] / "data"


def load_corpus(data_dir: Path = DATA_DIR) -> list[str]:
    """Return a list of raw document strings from data/."""
    # TODO: read your corpus files (txt/csv/jsonl) into a list of documents.
    raise NotImplementedError


def basic_stats(docs: list[str]) -> dict[str, float]:
    """Return n_docs, n_tokens, n_types, and type/token ratio."""
    # TODO: tokenize (a simple .split() is fine to start) and aggregate counts.
    raise NotImplementedError


def token_frequencies(docs: list[str]) -> Counter:
    """Return a Counter of token -> frequency across the corpus."""
    # TODO: build and return the frequency distribution.
    raise NotImplementedError


def duplication_rate(docs: list[str], threshold: float = 0.8) -> float:
    """Estimate the fraction of documents that are near-duplicates.

    Start with exact-hash duplicates, then add shingled Jaccard / MinHash.
    """
    # TODO: implement exact + near-duplicate detection.
    raise NotImplementedError


def main() -> None:
    docs = load_corpus()
    print("stats:", basic_stats(docs))
    print("top tokens:", token_frequencies(docs).most_common(20))
    print("duplication rate:", duplication_rate(docs))


if __name__ == "__main__":
    main()
