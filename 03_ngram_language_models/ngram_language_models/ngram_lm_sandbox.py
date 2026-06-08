"""N-gram Language Models — Sandbox
J&M Speech and Language Processing, Chapter 3.

Objective:
    Build bigram/trigram models with add-k smoothing and generate text.

Fill in each TODO, then run:
    python ngram_lm_sandbox.py
"""

from collections import defaultdict
from typing import Dict, List, Tuple


def load_corpus(path: str) -> List[List[str]]:
    # TODO: read file, split into sentences, tokenize, pad with <s> and </s>
    raise NotImplementedError


def count_ngrams(sentences: List[List[str]], n: int) -> Dict[Tuple[str, ...], int]:
    counts: Dict[Tuple[str, ...], int] = defaultdict(int)
    # TODO: slide an n-word window over each sentence and count
    raise NotImplementedError


def prob(context: Tuple[str, ...], word: str, k: float = 1.0) -> float:
    # TODO: add-k smoothed P(word | context)
    raise NotImplementedError


def generate(max_len: int = 30) -> str:
    # TODO: start from <s>, repeatedly sample next word until </s> or max_len
    raise NotImplementedError


def main() -> None:
    # TODO: load corpus, build counts, print a few sampled sentences for n=2 and n=3
    ...


if __name__ == "__main__":
    main()
