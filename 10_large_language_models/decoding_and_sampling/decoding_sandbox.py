"""Decoding & Sampling — Sandbox
J&M Speech and Language Processing, Chapter 10.

Objective:
    Compare greedy / beam / temperature / top-k / top-p decoding.

Fill in each TODO, then run:
    python decoding_sandbox.py
"""

from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL_NAME = "distilgpt2"
PROMPT = "The new policy on voting rights will"


def generate(model, tokenizer, prompt: str, **gen_kwargs) -> str:
    # TODO: encode prompt, call model.generate(**gen_kwargs), decode
    raise NotImplementedError


def main() -> None:
    # TODO: load model + tokenizer
    # TODO: generate with: greedy; num_beams=4; do_sample temperature in {0.2,0.7,1.2};
    #       top_k=50; top_p=0.9 — print each result
    ...


if __name__ == "__main__":
    main()
