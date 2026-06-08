"""Information Retrieval: Sparse & Dense — Sandbox
J&M Speech and Language Processing, Chapter 14.

Objective:
    Compare BM25 (sparse) and embedding-based (dense) retrieval.

Fill in each TODO, then run:
    python ir_sandbox.py
"""

from typing import List

CORPUS: List[str] = []   # TODO: load passages from data/
QUERIES: List[str] = ["What did the bill say about voting access?"]


def bm25_search(corpus: List[str], query: str, k: int = 5):
    # TODO: tokenize corpus, build rank_bm25.BM25Okapi, return top-k passages
    raise NotImplementedError


def dense_search(corpus: List[str], query: str, k: int = 5):
    # TODO: embed corpus + query with sentence-transformers, rank by cosine (or FAISS)
    raise NotImplementedError


def main() -> None:
    # TODO: for each query, print BM25 vs dense top-k and compare
    ...


if __name__ == "__main__":
    main()
