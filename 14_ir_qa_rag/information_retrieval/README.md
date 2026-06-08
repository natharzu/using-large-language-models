# Information Retrieval: Sparse & Dense

> J&M Ch. 14 · Concept note: *Information Retrieval: Sparse & Dense*

## Objective

Build and compare a sparse lexical retriever (BM25) and a dense embedding retriever over a document corpus.

## Dataset

A corpus of short documents/passages in `data/` (policy snippets, FAQ entries, speech paragraphs) plus a handful of queries.

## Tasks

1. Index the corpus with BM25 (`rank_bm25`).
2. Build a dense index: embed passages (`sentence-transformers`) and search with cosine / FAISS.
3. For each query, retrieve top-k from both methods.
4. Compare results qualitatively and with a metric (e.g. recall@k against a small gold set).
5. Note where lexical beats dense and vice versa.

## Success criteria

- Two working retrievers returning ranked passages.
- A comparison showing the strengths of each approach.

## Stretch

- Combine them into a hybrid score and see if it beats either alone.
