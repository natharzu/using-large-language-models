# Masked Language Models

> J&M Ch. 11 · Concept note: *Masked Language Models*

## Objective

Understand the masked-language-modeling objective behind BERT-style encoders: probe a fill-mask model, then fine-tune the encoder for a political-text classification task.

## Dataset

Sentences with a `[MASK]` token for probing, plus the labeled dataset from Chapter 5 for fine-tuning.

## Tasks

1. Load a fill-mask pipeline (e.g. `bert-base-uncased`).
2. Mask a salient word in several political sentences and inspect the top predictions + probabilities.
3. Show how bidirectional context changes the prediction vs. a left-to-right model.
4. Fine-tune `AutoModelForSequenceClassification` (BERT) on the Ch. 5 labels.
5. Compare accuracy/F1 to the logistic regression (Ch. 5) and MLP (Ch. 7) baselines.

## Success criteria

- Sensible fill-mask predictions with probabilities.
- A fine-tuned classifier with a metrics comparison vs. earlier baselines.

## Stretch

- Compare `[CLS]` pooling vs. mean pooling for the classification head.
