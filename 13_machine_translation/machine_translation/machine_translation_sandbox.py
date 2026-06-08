"""Machine Translation & BLEU — Sandbox
J&M Speech and Language Processing, Chapter 13.

Objective:
    Translate with a pretrained seq2seq model and evaluate with BLEU.

Setup:
    pip install sacrebleu sentencepiece

Fill in each TODO, then run:
    python machine_translation_sandbox.py
"""

from typing import List
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

MODEL_NAME = "Helsinki-NLP/opus-mt-en-fr"
SOURCES: List[str] = ["The parliament passed the new law."]
REFERENCES: List[str] = ["Le parlement a adopté la nouvelle loi."]


def translate(model, tokenizer, texts: List[str], num_beams: int = 4) -> List[str]:
    # TODO: tokenize, model.generate(num_beams=...), batch_decode
    raise NotImplementedError


def corpus_bleu(hypotheses: List[str], references: List[str]) -> float:
    # TODO: use sacrebleu.corpus_bleu(hypotheses, [references]).score
    raise NotImplementedError


def main() -> None:
    # TODO: load model + tokenizer
    # TODO: translate SOURCES, print translations
    # TODO: compute BLEU vs REFERENCES; sweep num_beams in {1,4,8}
    ...


if __name__ == "__main__":
    main()
