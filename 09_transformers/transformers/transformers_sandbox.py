"""Transformers — Sandbox
J&M Speech and Language Processing, Chapter 9.

Objective:
    Run a pretrained transformer and inspect its components and outputs.

Fill in each TODO, then run:
    python transformers_sandbox.py
"""

from transformers import AutoModel, AutoTokenizer

MODEL_NAME = "distilbert-base-uncased"
TEXT = "The senator proposed a sweeping reform of campaign finance."


def main() -> None:
    # TODO: load tokenizer + model (AutoTokenizer / AutoModel)
    # TODO: tokenize TEXT, run forward pass with torch.no_grad()
    # TODO: print last_hidden_state.shape and total parameter count
    # TODO: compute a CLS-pooled and a mean-pooled sentence vector
    ...


if __name__ == "__main__":
    main()
