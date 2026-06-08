# VADER vs. Star Ratings

> J&M Ch. 4 · Concept note: *VADER vs. Star Ratings*

## Objective

Measure how well a rule/lexicon-based sentiment scorer (VADER) agrees with the star ratings users actually gave, and learn where lexicons break down.

## Dataset

Amazon product reviews with `text` and `stars` (1–5). Put a CSV in `data/`.

## Tasks

1. Load reviews; map stars to sentiment labels (1–2 = negative, 3 = neutral, 4–5 = positive).
2. Score each review with VADER's compound score.
3. Map the compound score to a predicted label and compute accuracy, precision, recall, F1.
4. Build a confusion matrix; inspect the worst disagreements.
5. Explain failures: negation, sarcasm, domain words, mixed sentiment.

## Success criteria

- A working evaluation table comparing VADER predictions to star-derived labels.
- A short written analysis of 3–5 misclassified reviews.

## Stretch

- Train a Naive Bayes classifier on the same data and compare to VADER.
