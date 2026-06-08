"""Masked Language Models — Sandbox
J&M Speech and Language Processing, Chapter 11.

Objective:
    Probe a fill-mask (BERT) model and fine-tune the encoder for classification.

Fill in each TODO, then run:
    python masked_lm_sandbox.py
"""

from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline

MODEL_NAME = "bert-base-uncased"
MASKED = [
    "The senate voted to [MASK] the new bill.",
    "Voters expressed deep [MASK] about the election results.",
]


def probe_fill_mask() -> None:
    # TODO: build pipeline('fill-mask', model=MODEL_NAME)
    # TODO: for each sentence in MASKED, print top-5 predictions + scores
    raise NotImplementedError


def finetune_classifier(train_texts, train_labels, test_texts, test_labels):
    # TODO: load AutoModelForSequenceClassification, tokenize, train a few epochs
    # TODO: return accuracy / macro-F1 on the test set
    raise NotImplementedError


def main() -> None:
    probe_fill_mask()
    # TODO: load Ch.5 dataset, fine-tune, compare to logreg + MLP baselines
    ...


if __name__ == "__main__":
    main()
