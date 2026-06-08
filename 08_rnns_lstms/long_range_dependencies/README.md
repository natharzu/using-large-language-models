# RNNs & LSTMs

> Companion exercise for the **RNNs & LSTMs** page in the LLM Dictionary.
>
> This fills the intentionally-skipped `08_` slot (see issue #1 on chapter numbering).

## Objective
See *why* vanilla RNNs struggle with long-range dependencies and how an LSTM's gating fixes it. You will train both on a synthetic copy/memory task where the signal is separated from the label by a long gap.

## Dataset
Synthetic: a "copy task" or "adding problem" you generate in code (no download needed). Optionally, a political-text sequence-labelling set as a stretch.

## Tasks
1. Generate a copy-task dataset where the model must recall a token seen `k` steps earlier.
2. Implement a vanilla RNN (`nn.RNN`) classifier and train it; record accuracy as `k` grows.
3. Swap in an `nn.LSTM` with the same budget and compare accuracy vs sequence length.
4. Log gradient norms during training for both models to observe vanishing/exploding gradients.
5. Write two sentences explaining, in terms of the cell state and gates, why the LSTM holds information longer.

## Success criteria
- You have an accuracy-vs-gap-length curve for both models on the same task.
- You can point to the gap length where the vanilla RNN collapses but the LSTM still works.
- You have at least one gradient-norm plot illustrating the vanishing-gradient effect.

## Stretch
- Add gradient clipping to the vanilla RNN and measure how much it helps.
- Replace the LSTM with a GRU and compare parameter count vs accuracy.

## Reference
Jurafsky & Martin, *Speech and Language Processing* (3rd ed.), Ch. 8 (RNNs and LSTMs); Hochreiter & Schmidhuber (1997).
