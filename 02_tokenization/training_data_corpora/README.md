# Training Data & Corpora

> Companion exercise for the **Training Data & Corpora** page in the LLM Dictionary.

## Objective
Build intuition for what a corpus actually *contains* before you model it. You will profile a political-text corpus, quantify duplication and class balance, and document provenance — the unglamorous work that determines whether downstream results mean anything.

## Dataset
Any medium corpus of political text (e.g. congressional floor statements, party manifestos, or a sample of news articles). Drop raw files in `data/` (git-ignored). A few thousand documents is plenty.

## Tasks
1. Load the corpus and compute basic descriptive statistics: number of documents, tokens, types, and the type/token ratio.
2. Plot the token-frequency distribution (log-log) and confirm it is roughly Zipfian.
3. Detect near-duplicate documents (exact hash + a shingled Jaccard or MinHash pass) and report the duplication rate.
4. Profile metadata balance (e.g. party, chamber, year) and flag any axis that is severely skewed.
5. Write a short `DATASHEET.md`: source, license, collection date, known biases, and preprocessing applied.

## Success criteria
- You can state the corpus size, vocabulary size, and duplication rate with numbers.
- You have identified at least one sampling bias that would affect a classifier trained on this data.
- A `DATASHEET.md` exists and is honest about limitations.

## Stretch
- Deduplicate with MinHash + LSH and measure how vocabulary and class balance shift afterwards.
- Compare two collection windows (e.g. pre/post an election) and quantify vocabulary drift.

## Reference
Jurafsky & Martin, *Speech and Language Processing* (3rd ed.), Ch. 2; Gebru et al., "Datasheets for Datasets" (2021).
