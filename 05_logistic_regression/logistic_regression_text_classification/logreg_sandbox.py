"""Logistic Regression & Text Classification — Sandbox
J&M Speech and Language Processing, Chapter 5.

Objective:
    TF-IDF + logistic regression text classifier, with weight interpretation.

Fill in each TODO, then run:
    python logreg_sandbox.py
"""

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report


def load_data(path: str):
    # TODO: return texts (List[str]) and labels (List[str])
    raise NotImplementedError


def top_features(vectorizer: TfidfVectorizer, model: LogisticRegression, k: int = 15):
    # TODO: map model.coef_ back to feature names; print top +/- tokens per class
    raise NotImplementedError


def main() -> None:
    # TODO: load -> split -> TfidfVectorizer.fit_transform -> LogisticRegression.fit
    # TODO: print classification_report on the test set
    # TODO: call top_features to interpret the model
    ...


if __name__ == "__main__":
    main()
