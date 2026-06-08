# Inter-rater Reliability (Cohen's κ & Krippendorff's α)

> Companion exercise for the **Inter-rater Reliability** page in the LLM Dictionary.
> Best done *before* the capstone — you need these metrics to validate LLM-vs-human agreement.

## Objective
Learn why raw percent agreement is misleading and how chance-corrected metrics fix it. You will compute Cohen's κ and Krippendorff's α on annotation data and expose the base-rate trap.

## Dataset
A small set of items labelled by 2+ annotators (e.g. tweets coded for stance, or sentences coded for frame). A handful of items with deliberate disagreement works well. Put files in `data/`.

## Tasks
1. Compute raw percent agreement between two annotators.
2. Implement Cohen's κ (`(p_o - p_e) / (1 - p_e)`) from scratch and verify against a library.
3. Construct a high-agreement-but-low-κ example (heavy class imbalance) and explain the base-rate trap.
4. Compute Krippendorff's α for 3+ annotators (or with missing labels) and contrast it with κ.
5. Write a one-paragraph guideline: what κ/α thresholds you would accept before trusting a coding scheme.

## Success criteria
- Your hand-rolled κ matches a reference implementation to floating-point error.
- You have a concrete example where percent agreement ≥ 0.9 but κ is near 0.
- You can explain when to prefer α over κ (more raters, missing data, non-nominal scales).

## Stretch
- Add a third rater and report pairwise κ plus a single α.
- Treat the LLM as one "rater" and measure LLM-vs-human α — this feeds directly into the capstone.

## Reference
Jurafsky & Martin, *Speech and Language Processing* (3rd ed.), Ch. 4 (annotation); Artstein & Poesio (2008); Krippendorff (2004).
