"""Context Window Mechanics — Sandbox
J&M Speech and Language Processing, Chapter 10.

Objective:
    Count tokens, apply truncation strategies, and reason about context limits.

Fill in each TODO, then run:
    python context_window_sandbox.py
"""

from transformers import AutoTokenizer

MODEL_NAME = "gpt2"
CONTEXT_LIMIT = 1024


def count_tokens(tokenizer, text: str) -> int:
    # TODO: return number of tokens
    raise NotImplementedError


def truncate(tokenizer, text: str, limit: int, strategy: str = "tail") -> str:
    # TODO: implement 'head', 'tail', and 'middle' truncation to <= limit tokens
    raise NotImplementedError


def main() -> None:
    # TODO: load a long document from data/, count tokens
    # TODO: truncate with each strategy and show what survives
    # TODO: estimate token cost at an example price per 1K tokens
    ...


if __name__ == "__main__":
    main()
