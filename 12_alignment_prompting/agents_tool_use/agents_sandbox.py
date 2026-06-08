"""Agents & Tool Use — starter.

A minimal ReAct-style observe-think-act loop with two tools.
Fill in the TODOs. Run with: python agents_sandbox.py

Note: wire `call_model` to whatever LLM you use (local transformers or an API).
See issue #4 about declaring an LLM client in requirements.txt.
"""
from __future__ import annotations

from typing import Callable


def search(query: str) -> str:
    """Pretend to look something up. Replace with a real lookup."""
    # TODO: implement or stub a retrieval over your facts.
    raise NotImplementedError


def calculator(expression: str) -> str:
    """Safely evaluate a simple arithmetic expression."""
    # TODO: implement a guarded evaluator.
    raise NotImplementedError


TOOLS: dict[str, Callable[[str], str]] = {"search": search, "calculator": calculator}


def call_model(prompt: str) -> str:
    """Return the model's next message (may contain a tool call)."""
    # TODO: connect to your LLM of choice.
    raise NotImplementedError


def parse_action(message: str) -> tuple[str, str] | None:
    """Return (tool_name, tool_input) if the message requests a tool, else None."""
    # TODO: parse the model's chosen action.
    raise NotImplementedError


def run_agent(question: str, max_steps: int = 6) -> str:
    """Observe-think-act loop with a hard step budget."""
    # TODO: loop: call_model -> parse_action -> run tool -> append observation.
    raise NotImplementedError


def main() -> None:
    print(run_agent("How many seats does the governing party currently hold?"))


if __name__ == "__main__":
    main()
