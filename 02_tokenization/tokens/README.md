# Tokens

> J&M Ch. 2 · Concept note: *Tokens*

## Objective

Understand how different tokenizers split the same text and how that changes sequence length, vocabulary size, and the handling of rare/political terms.

## Dataset

A handful of political sentences (provided inline in the stub) plus, optionally, a paragraph of a speech from `data/`.

## Tasks

1. Tokenize the sample text three ways: naive whitespace split, NLTK word tokenizer, and a subword tokenizer (`tiktoken` or a HuggingFace BPE tokenizer).
2. Report the token count and the token list for each method.
3. Show how a rare/compound word (e.g. *gerrymandering*, *deinstitutionalization*) is broken into subwords.
4. Measure vocabulary size on a larger sample for word vs. subword tokenization.

## Success criteria

- You can explain why subword tokenization produces a smaller, fixed vocabulary while still covering unseen words.
- You can predict roughly how many tokens a sentence will cost an LLM.

## Stretch

- Compare `cl100k_base` (GPT-4 family) vs. a BERT WordPiece tokenizer on the same text.
