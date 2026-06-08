# Logistic Regression & Text Classification

> J&M Ch. 5 · Concept note: *Logistic Regression & Text Classification*

## Objective

Build and evaluate a TF-IDF + logistic regression text classifier, and interpret the learned weights.

## Dataset

Any labeled text: review sentiment, news topic, or party of a speech. Put a CSV in `data/`.

## Tasks

1. Split into train/test.
2. Vectorize text with `TfidfVectorizer`.
3. Train `LogisticRegression`; report accuracy, precision, recall, F1.
4. Inspect the highest positive/negative weight features per class.
5. Try L1 vs. L2 regularization and vary C.

## Success criteria

- A reproducible train/eval pipeline.
- A list of the most informative tokens that makes intuitive sense.

## Stretch

- Add bigram features and compare; calibrate probabilities and plot a reliability curve.
