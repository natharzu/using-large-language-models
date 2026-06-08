"""Pretraining vs. Fine-tuning — Sandbox
J&M Speech and Language Processing, Chapter 10.

Objective:
    Compare a base pretrained model to a fine-tuned / LoRA-tuned version.

Fill in each TODO, then run:
    python pretraining_finetuning_sandbox.py
"""

from transformers import AutoModelForSequenceClassification, AutoTokenizer

MODEL_NAME = "distilbert-base-uncased"


def evaluate(model, tokenizer, texts, labels) -> float:
    # TODO: run model, return accuracy (or F1)
    raise NotImplementedError


def finetune(model, tokenizer, train_texts, train_labels):
    # TODO: full fine-tune OR attach a LoRA adapter with peft; train a few epochs
    # TODO: print number of trainable parameters
    raise NotImplementedError


def main() -> None:
    # TODO: load model + tokenizer; evaluate base; finetune; evaluate again; compare
    ...


if __name__ == "__main__":
    main()
