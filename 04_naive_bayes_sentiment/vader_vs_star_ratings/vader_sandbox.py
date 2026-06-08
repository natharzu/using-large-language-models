"""VADER vs. Star Ratings — Sandbox
J&M Speech and Language Processing, Chapter 4.

Objective:
    Compare VADER lexicon sentiment against ground-truth star ratings.

Setup:
    import nltk; nltk.download('vader_lexicon')

Fill in each TODO, then run:
    python vader_sandbox.py
"""

import pandas as pd


def stars_to_label(stars: int) -> str:
    # TODO: 1-2 -> 'negative', 3 -> 'neutral', 4-5 -> 'positive'
    raise NotImplementedError


def vader_label(text: str) -> str:
    # TODO: use SentimentIntensityAnalyzer().polarity_scores(text)['compound']
    #       thresholds: >= 0.05 positive, <= -0.05 negative, else neutral
    raise NotImplementedError


def main() -> None:
    # TODO: load data/reviews.csv into a DataFrame
    # TODO: add 'true_label' and 'pred_label' columns
    # TODO: print classification_report and confusion_matrix (sklearn)
    # TODO: print the 5 reviews with the largest disagreement and comment on why
    ...


if __name__ == "__main__":
    main()
