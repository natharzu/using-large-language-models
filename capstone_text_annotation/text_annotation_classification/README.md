# LLMs for Text Annotation & Classification

> Capstone · Concept note: *LLMs for Text Annotation & Classification*

## Objective

Use an LLM as an annotator for a political-science labeling task, then evaluate its reliability against human gold labels and compare it to a classical (Ch. 5) baseline.

## Dataset

A few hundred texts with a human-labeled gold subset (stance, topic, frame, sentiment, etc.) in `data/`.

## Tasks

1. Define a clear codebook (label definitions + examples) — this is the prompt's backbone.
2. Prompt an LLM to label the dataset (zero-shot and few-shot; reuse Ch. 12 skills).
3. Compute agreement with human labels: accuracy, macro-F1, and Cohen's/Krippendorff's kappa.
4. Train a TF-IDF + logistic regression baseline (Ch. 5) and compare cost vs. quality.
5. Error analysis: where does the LLM systematically disagree with humans?
6. Write a short report with a recommendation: when is LLM annotation trustworthy here?

## Success criteria

- An evaluation table: LLM (zero-shot / few-shot) vs. baseline vs. human agreement.
- Inter-annotator agreement reported with a proper kappa statistic.
- A written recommendation grounded in the numbers.

## Stretch

- Add a human-in-the-loop step: only auto-accept LLM labels above a confidence threshold; route the rest to manual review, and report the savings.
