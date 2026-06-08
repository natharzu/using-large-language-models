# Using Large Language Models in Political Science

Hands-on **sandbox exercises** for learning Large Language Models (LLMs), organized by the chapters of [Jurafsky & Martin's *Speech and Language Processing* (3rd ed.)](https://web.stanford.edu/~jurafsky/slp3/) — the draft is free and openly published online. Each exercise pairs a short theory recap with a runnable coding task, oriented toward **political-science text** (speeches, parliamentary debates, reviews, news, social media).

This repo is the practice companion to the LLM concept notes in Notion: every concept page there has a matching exercise here.

## How this repo is organized

Folders are numbered to match the J&M chapters ([3rd ed., latest draft](https://web.stanford.edu/~jurafsky/slp3/)). Each chapter folder contains one subfolder per exercise, and each exercise has:

- `README.md` — the task spec (objective, dataset, tasks, success criteria, reference)
- `*_sandbox.py` — a starter script with `TODO`s to fill in

## Chapter map

| Folder | J&M Chapter | Exercises |
| --- | --- | --- |
| `02_tokenization/` | Ch. 2 | Tokens · Training Data & Corpora |
| `03_ngram_language_models/` | Ch. 3 | N-gram Language Models · Perplexity & LM Evaluation |
| `04_naive_bayes_sentiment/` | Ch. 4 | VADER vs. Star Ratings · Classification Metrics |
| `05_logistic_regression/` | Ch. 5 | Logistic Regression & Text Classification · Bag of Words & TF-IDF |
| `06_vector_semantics/` | Ch. 6 | Embeddings · How Embeddings Get Trained |
| `07_neural_networks/` | Ch. 7 | Neural Networks |
| `08_rnns_lstms/` | Ch. 8 | RNNs & LSTMs |
| `09_transformers/` | Ch. 9 | Transformers · Attention |
| `10_large_language_models/` | Ch. 10 | Pretraining vs. Fine-tuning · Decoding & Sampling · Context Window · Scaling Laws |
| `11_masked_language_models/` | Ch. 11 | Masked Language Models (BERT) |
| `12_alignment_prompting/` | Ch. 12 | Prompting & In-Context Learning · RLHF & Alignment · Bias & Fairness · Agents & Tool Use |
| `13_machine_translation/` | Ch. 13 | Machine Translation & BLEU |
| `14_ir_qa_rag/` | Ch. 14 | Information Retrieval · RAG Pipeline · Hallucination & Validation |
| `capstone_text_annotation/` | Capstone | LLMs for Text Annotation & Classification · Inter-rater Reliability |

> **Note on numbering:** this repo follows the latest J&M 3rd-ed draft, where Ch. 8 = RNNs & LSTMs and Ch. 9 = Transformers. Some Notion course reading pages still use an older numbering (e.g. Transformers as Ch. 8); those should be reconciled to match this map. See issue #1.

## Setup

Requires **Python 3.11** (see `.python-version`). Dependencies are pinned in `requirements.txt` for reproducibility.

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Datasets go in `data/` (git-ignored except its README). A tiny runnable sample lives in `data/sample/` so the early exercises work out-of-the-box before you supply real data.

## Suggested workflow

1. Read the concept note in Notion.
2. Open the exercise `README.md` here.
3. Fill in the `TODO`s in the `*_sandbox.py` stub.
4. Commit your solution next to the stub (e.g. `tokens_solution.py`).

## Reference

- Daniel Jurafsky & James H. Martin, *Speech and Language Processing* (3rd ed. draft) — free online: https://web.stanford.edu/~jurafsky/slp3/

## License

MIT — see [LICENSE](LICENSE).
