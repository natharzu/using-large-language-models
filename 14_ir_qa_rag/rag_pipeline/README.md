# RAG Pipeline

> J&M Ch. 14 · Concept note: *RAG Pipeline*

## Objective

Assemble a minimal Retrieval-Augmented Generation pipeline: retrieve relevant context, then condition an LLM's answer on it.

## Dataset

Reuse the corpus from the IR exercise plus a set of questions answerable from it.

## Tasks

1. Chunk documents and build a retriever (reuse the dense retriever).
2. For a question, retrieve top-k chunks.
3. Build a prompt that injects the retrieved context + question.
4. Generate an answer with a local pipeline or API client.
5. Show the answer **with citations** to the retrieved chunks.

## Success criteria

- An end-to-end `ask(question) -> answer + sources` function.
- Answers visibly grounded in the retrieved passages.

## Stretch

- Add a no-answer fallback when retrieval scores are low.
