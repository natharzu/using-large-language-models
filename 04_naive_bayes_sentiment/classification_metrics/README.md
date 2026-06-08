# Classification Metrics (Precision / Recall / F1)

> Companion exercise for the **Classification Metrics** page in the LLM Dictionary.

## Objective
Understand precision, recall, and F1 from the ground up by building a confusion matrix by hand and seeing how a decision threshold trades the two against each other. This is the evaluation backbone for every classifier in the repo.

## Dataset
Reuse the labelled sentiment data from `../vader_vs_star_ratings/` (gold labels + predicted scores), or any binary-labelled political-text set with model scores.

## Tasks
1. From gold labels and predictions, compute TP, FP, FN, TN **without** using a library.
2. Implement `precision`, `recall`, and `f1` from those counts and verify against `sklearn.metrics`.
3. Sweep the decision threshold from 0 to 1 and plot the precision-recall curve.
4. Report macro- vs micro-averaged F1 on a class-imbalanced split and explain the difference.
5. Write two sentences on which metric you would optimise for a *content-moderation* task vs a *recall-all-relevant-documents* task, and why.

## Success criteria
- Your hand-rolled metrics match scikit-learn to within floating-point error.
- You can point to the threshold that maximises F1 on your data.
- You can explain, in plain language, a case where high accuracy hides a useless model (the base-rate trap).

## Stretch
- Add a confusion matrix for a 3-class problem and compute per-class precision/recall.
- Bootstrap a 95% confidence interval around F1.

## Reference
Jurafsky & Martin, *Speech and Language Processing* (3rd ed.), Ch. 4.
