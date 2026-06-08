"""Prompting & In-Context Learning — Sandbox
J&M Speech and Language Processing, Chapter 12.

Objective:
    Compare zero-shot, few-shot, and chain-of-thought prompting accuracy.

Fill in each TODO, then run:
    python prompting_sandbox.py
"""

from typing import List, Tuple


def build_prompt(query: str, examples: List[Tuple[str, str]] = None, cot: bool = False) -> str:
    # TODO: assemble a prompt; if examples given -> few-shot; if cot -> add reasoning cue
    raise NotImplementedError


def predict(prompt: str) -> str:
    # TODO: call a local pipeline('text-generation') or an API client; parse the label
    raise NotImplementedError


def evaluate(eval_set, **prompt_kwargs) -> float:
    # TODO: build prompt per item, predict, return accuracy
    raise NotImplementedError


def main() -> None:
    # TODO: evaluate zero-shot, few-shot (k=3), and chain-of-thought; print a table
    ...


if __name__ == "__main__":
    main()
