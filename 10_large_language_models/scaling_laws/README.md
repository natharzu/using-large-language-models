# Scaling Laws & Model Size

> J&M Ch. 10 · Concept note: *Scaling Laws & Model Size*

## Objective

Build intuition for power-law scaling: as compute/parameters/data grow, loss falls predictably.

## Dataset

Either (a) published (params, loss) points you collect, or (b) your own runs: train a tiny model at a few sizes and record loss.

## Tasks

1. Collect or generate (model_size, loss) pairs.
2. Plot loss vs. size on log-log axes.
3. Fit a power law `L = a * N**(-b) + c` (e.g. `scipy.optimize.curve_fit`).
4. Interpret the exponent and the irreducible-loss term.
5. Extrapolate (carefully!) and discuss why extrapolation is risky.

## Success criteria

- A log-log plot with a fitted curve.
- A written interpretation of the fitted parameters.

## Stretch

- Add a compute-optimal (Chinchilla-style) discussion of data vs. parameters.
