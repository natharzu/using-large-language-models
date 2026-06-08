# Attention

> J&M Ch. 9 · Concept note: *Attention*

## Objective

Implement scaled dot-product attention from scratch, then visualize the attention weights of a real pretrained model.

## Dataset

Short sentences with clear dependencies (pronoun resolution, subject–verb).

## Tasks

1. Implement `attention(Q, K, V)` = `softmax(QK^T / sqrt(d_k)) V` in NumPy or PyTorch.
2. Verify shapes and that each attention row sums to 1.
3. Implement (or call) multi-head attention and explain the head split.
4. Extract real attention weights from a HuggingFace model (`output_attentions=True`).
5. Visualize a head's attention matrix as a heatmap (or with `bertviz`).

## Success criteria

- Your hand-written attention matches a reference implementation on random inputs.
- A heatmap showing a head attending to a sensible token (e.g. a pronoun to its antecedent).

## Stretch

- Compare attention patterns across layers/heads for the same sentence.
