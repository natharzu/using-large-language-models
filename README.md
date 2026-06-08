# Using Large Language Models in Political Science

Hands-on **sandbox exercises** for learning Large Language Models (LLMs), organized by the chapters of Jurafsky & Martin's *Speech and Language Processing* (3rd ed.). Each exercise pairs a short theory recap with a runnable coding task, oriented toward **political-science text** (speeches, parliamentary debates, reviews, news, social media).

This repo is the practice companion to the LLM concept notes in Notion: every concept page there has a matching exercise here.

## How this repo is organized

Folders are numbered to match the J&M chapters. Each chapter folder contains one subfolder per exercise, and each exercise has:

- `README.md` — the task spec (objective, dataset, tasks, success criteria, reference)
- `*_sandbox.py` — a starter script with `TODO`s to fill in

## Chapter map

| Folder | J&M Chapter | Exercises |
| --- | --- | --- |
| `02_tokenization/` | Ch. 2 | Tokens |
| `03_ngram_language_models/` | Ch. 3 | N-gram Language Models · Perplexity & LM Evaluation |
| `04_naive_bayes_sentiment/` | Ch. 4 | VADER vs. Star Ratings |
| `05_logistic_regression/` | Ch. 5 | Logistic Regression & Text Classification |
| `06_vector_semantics/` | Ch. 6 | Embeddings · How Embeddings Get Trained |
| `07_neural_networks/` | Ch. 7 | Neural Networks |
| `09_transformers/` | Ch. 9 | Transformers · Attention |
| `10_large_language_models/` | Ch. 10 | Pretraining vs. Fine-tuning · Decoding & Sampling · Context Window · Scaling Laws |
| `11_masked_language_models/` | Ch. 11 | Masked Language Models (BERT) |
| `12_alignment_prompting/` | Ch. 12 | Prompting & In-Context Learning · RLHF & Alignment · Bias & Fairness |
| `13_machine_translation/` | Ch. 13 | Machine Translation & BLEU |
| `14_ir_qa_rag/` | Ch. 14 | Information Retrieval · RAG Pipeline · Hallucination & Validation |
| `capstone_text_annotation/` | Capstone | LLMs for Text Annotation & Classification |

## Setup

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Datasets go in `data/` (git-ignored except its README).

## Suggested workflow

1. Read the concept note in Notion.
2. Open the exercise `README.md` here.
3. Fill in the `TODO`s in the `*_sandbox.py` stub.
4. Commit your solution next to the stub (e.g. `tokens_solution.py`).

## License

MIT — see [LICENSE](LICENSE).
