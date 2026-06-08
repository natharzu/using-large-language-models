# Machine Translation & BLEU

> J&M Ch. 13 · Concept note: *Machine Translation*

## Objective

Use a pretrained encoder–decoder model to translate text, evaluate quality with BLEU, and see how beam search affects output.

## Dataset

A small set of source sentences with **reference** translations (a dozen political phrases is enough). Put pairs in `data/`.

## Tasks

1. Load a pretrained MT model + tokenizer (e.g. `Helsinki-NLP/opus-mt-en-fr` / MarianMT).
2. Translate the source sentences.
3. Compute corpus BLEU against the references (`sacrebleu`).
4. Vary `num_beams` (1, 4, 8) and observe BLEU + fluency.
5. Error analysis: where does it fail (named entities, idioms, negation)?

## Success criteria

- Translations with a reported BLEU score.
- A short analysis linking beam size to quality.

## Stretch

- Compare two language directions, or two different MT models, on the same inputs.
