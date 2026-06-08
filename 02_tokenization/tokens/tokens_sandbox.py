"""Tokens — Sandbox
J&M Speech and Language Processing, Chapter 2.

Objective:
    Compare whitespace, word-level, and subword (BPE) tokenization on
    political text, and observe the effect on sequence length and vocabulary.

Fill in each TODO, then run:
    python tokens_sandbox.py
"""

from typing import List

SAMPLES: List[str] = [
    "The committee debated the gerrymandering proposal for hours.",
    "Deinstitutionalization reshaped mid-century social policy.",
    "Voters demanded transparency and accountability.",
]


def whitespace_tokenize(text: str) -> List[str]:
    # TODO: split on whitespace
    raise NotImplementedError


def word_tokenize(text: str) -> List[str]:
    # TODO: use nltk.word_tokenize (remember nltk.download('punkt'))
    raise NotImplementedError


def subword_tokenize(text: str) -> List[str]:
    # TODO: use tiktoken (e.g. encoding 'cl100k_base') or a HuggingFace tokenizer
    #       and decode each token id back to its string piece for display.
    raise NotImplementedError


def main() -> None:
    for text in SAMPLES:
        print("=" * 60)
        print(text)
        # TODO: print token list + count for each method
        # TODO: highlight how a rare/compound word is split by the subword tokenizer
    # TODO: compute vocabulary size for word vs. subword tokenization on all SAMPLES


if __name__ == "__main__":
    main()
