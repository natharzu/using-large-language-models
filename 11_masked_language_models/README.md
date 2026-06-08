# Chapter 11 — Masked Language Models

> J&M *Speech and Language Processing*, Ch. 11 (Masked Language Models / Bidirectional Encoders).

Encoder-only transformers (BERT-style) are pretrained by predicting **masked** tokens using context from *both* directions. They excel at understanding and classification rather than open-ended generation.

## Exercises

- [`masked_language_models/`](masked_language_models/) — Probe a fill-mask model and fine-tune a BERT encoder for classification.
