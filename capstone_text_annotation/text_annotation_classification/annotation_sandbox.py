"""LLMs for Text Annotation & Classification — Capstone Sandbox

Objective:
    Use an LLM to annotate a dataset, evaluate vs. human labels and a baseline.

Fill in each TODO, then run:
    python annotation_sandbox.py
"""

from typing import Dict, List

LABELS: List[str] = []   # TODO: define your label set
CODEBOOK: Dict[str, str] = {}   # TODO: label -> definition (used in the prompt)


def build_annotation_prompt(text: str, few_shot: bool = False) -> str:
    # TODO: assemble codebook + (optional) examples + the text to label
    raise NotImplementedError


def llm_annotate(text: str, few_shot: bool = False) -> str:
    # TODO: call the LLM, parse and return one of LABELS
    raise NotImplementedError


def baseline_classify(train_texts, train_labels, test_texts):
    # TODO: TF-IDF + LogisticRegression (reuse Chapter 5); return predictions
    raise NotImplementedError


def evaluate(gold: List[str], pred: List[str]) -> Dict[str, float]:
    # TODO: accuracy, macro-F1, Cohen's kappa
    raise NotImplementedError


def main() -> None:
    # TODO: load gold data
    # TODO: get LLM annotations (zero-shot + few-shot) and baseline predictions
    # TODO: print the comparison table + kappa; do a short error analysis
    ...


if __name__ == "__main__":
    main()
