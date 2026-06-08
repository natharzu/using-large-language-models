# Agents & Tool Use

> Companion exercise for the **Agents & Tool Use** page in the LLM Dictionary.

## Objective
Build a minimal tool-using loop: an LLM that decides when to call an external tool, reads the result, and continues. You will implement the ReAct-style observe-think-act cycle and see where it breaks.

## Dataset
No dataset required. You provide a small set of questions about political facts (e.g. "How many seats does party X hold?") that require a lookup the model cannot answer reliably from memory.

## Tasks
1. Define two tools as plain Python functions (e.g. `search(query)` and `calculator(expr)`) with typed signatures and docstrings.
2. Implement an agent loop: prompt the model, parse a tool call, execute it, feed the observation back, repeat until a final answer.
3. Add a step budget and a stop condition so the loop cannot run forever.
4. Log the full trace (thought → action → observation) for three questions.
5. Document one failure mode you observed (wrong tool, hallucinated arguments, infinite loop) and how you mitigated it.

## Success criteria
- The agent answers at least one question it cannot answer without the tool.
- The loop terminates safely on every input (no runaway calls).
- You have a written trace and a documented failure mode + mitigation.

## Stretch
- Add a third tool and a router prompt; measure how often the right tool is selected.
- Replace string parsing with structured/JSON tool-calling and compare reliability.

## Reference
Jurafsky & Martin, *Speech and Language Processing* (3rd ed.), Ch. 12; Yao et al., "ReAct" (2023); Schick et al., "Toolformer" (2023).
