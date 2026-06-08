# Transformers

> J&M Ch. 9 · Concept note: *Transformers in LLMs*

## Objective

Run a pretrained transformer end-to-end, inspect tokenization, hidden states, and the shape of each component.

## Dataset

A few political sentences (inline) plus optional text from `data/`.

## Tasks

1. Load a small pretrained model + tokenizer from HuggingFace (e.g. `distilbert-base-uncased`).
2. Run a forward pass and inspect the output hidden-state shapes `(batch, seq_len, hidden)`.
3. Count parameters and identify the embedding, attention, and feed-forward blocks.
4. Use the model for a downstream task via `pipeline` (sentiment or fill-mask).
5. Compare CLS-pooled vs. mean-pooled sentence representations.

## Success criteria

- You can name each tensor's dimensions and what they represent.
- A working `pipeline` prediction on your own text.

## Stretch

- Compare hidden states from layer 1 vs. the last layer for the same token.
