# Sample data

A tiny, synthetic sample so the early exercises (VADER, classification metrics,
bag-of-words) run out-of-the-box. **Not** real Amazon data and **not** for
reporting results — replace with a real corpus in `data/` for actual work.

## `reviews_sample.csv`

12 product reviews with columns:

- `text` — the review body
- `stars` — the star rating (1–5), used as the ground-truth sentiment signal

The sample deliberately includes the hard cases discussed in the VADER note:
sarcasm, factual complaints with no negative-lexicon words, and "I wanted to
love it" 1-star reviews.
