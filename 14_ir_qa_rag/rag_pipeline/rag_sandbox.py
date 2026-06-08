"""RAG Pipeline — Sandbox
J&M Speech and Language Processing, Chapter 14.

Objective:
    Build a minimal retrieve-then-generate pipeline with source citations.

Fill in each TODO, then run:
    python rag_sandbox.py
"""

from typing import List, Tuple

CORPUS: List[str] = []   # TODO: load chunks from data/


def retrieve(question: str, k: int = 4) -> List[Tuple[int, str]]:
    # TODO: return top-k (chunk_id, chunk_text) by dense similarity
    raise NotImplementedError


def build_prompt(question: str, contexts: List[Tuple[int, str]]) -> str:
    # TODO: format retrieved contexts + question into a grounded prompt
    raise NotImplementedError


def generate(prompt: str) -> str:
    # TODO: call a local pipeline('text-generation') or API client
    raise NotImplementedError


def ask(question: str):
    # TODO: retrieve -> build_prompt -> generate -> return (answer, source_ids)
    raise NotImplementedError


def main() -> None:
    # TODO: ask a few questions and print answers with their source chunk ids
    ...


if __name__ == "__main__":
    main()
