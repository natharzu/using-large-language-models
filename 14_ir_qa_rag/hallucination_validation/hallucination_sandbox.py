"""Hallucination & Validation — Sandbox
J&M Speech and Language Processing, Chapter 14.

Objective:
    Detect ungrounded claims in generated answers and measure hallucination rate.

Fill in each TODO, then run:
    python hallucination_sandbox.py
"""

from typing import List


def split_claims(answer: str) -> List[str]:
    # TODO: split an answer into atomic claim sentences
    raise NotImplementedError


def is_supported(claim: str, context: str) -> bool:
    # TODO: embedding-overlap threshold OR an NLI entailment model
    raise NotImplementedError


def hallucination_rate(answers: List[str], contexts: List[str]) -> float:
    # TODO: fraction of claims across all answers that are unsupported
    raise NotImplementedError


def main() -> None:
    # TODO: run on RAG outputs; report rate; compare with/without mitigation
    ...


if __name__ == "__main__":
    main()
