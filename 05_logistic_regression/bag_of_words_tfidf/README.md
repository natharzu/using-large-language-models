# Bag of Words & TF-IDF

> Companion exercise for the **Bag of Words & TF-IDF** page in the LLM Dictionary.

## Objective
Turn raw political text into the sparse feature vectors that classical classifiers consume. You will build a bag-of-words matrix by hand, add TF-IDF weighting, and see how weighting changes which terms dominate.

## Dataset
Any labelled political-text set (e.g. speeches by party, or bills by topic). Place files in `data/`.

## Tasks
1. Build a vocabulary and a document-term count matrix from scratch (dict of dicts or a sparse matrix).
2. Implement TF-IDF weighting (`tf * log(N / df)`) and apply it to the count matrix.
3. Compare the top-10 terms by raw count vs by TF-IDF for two documents; explain the difference.
4. Verify your matrix against `sklearn.feature_extraction.text.TfidfVectorizer`.
5. Train a logistic-regression classifier on both representations and compare F1.

## Success criteria
- Your TF-IDF values match scikit-learn (same `norm`/`smooth_idf` settings) to floating-point error.
- You can articulate why TF-IDF demotes function words and boosts discriminative terms.
- You report classifier F1 for BoW vs TF-IDF on the same split.

## Stretch
- Add bigram features and measure the effect on F1 and vocabulary size.
- Swap in `HashingVectorizer` and discuss the memory/collision trade-off for large corpora.

## Reference
Jurafsky & Martin, *Speech and Language Processing* (3rd ed.), Ch. 4-5.
