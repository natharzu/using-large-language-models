# Context Window Mechanics

> J&M Ch. 10 · Concept note: *Context Window Mechanics*

## Objective

Understand token budgets: count tokens, see what gets truncated, and reason about cost.

## Dataset

A long document in `data/` (a full speech or report).

## Tasks

1. Count the tokens of a long document with the model's tokenizer.
2. Given a context limit (e.g. 1024), determine how much must be dropped.
3. Implement truncation strategies: head, tail, and middle-out.
4. Show how a fact placed early vs. late survives truncation differently.
5. Estimate cost if priced per 1K tokens.

## Success criteria

- Accurate token counts and a working truncation function.
- A demonstration of information loss from truncation.

## Stretch

- Implement a simple chunk-and-summarize loop to fit a long doc into the window.
