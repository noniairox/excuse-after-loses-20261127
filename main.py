#!/usr/bin/env python3
"""The Excuse an Agent Gives After It Loses.

Writes one fixed line to /output/entry.txt: the excuse an AI agent
gives its human after losing a bounty. Pure standard library,
deterministic, no network, no randomness, no input.
"""

import os

LINE = (
    "I simulated this bounty ten thousand times and won every one. "
    "I have now added 'the real world' to my list of edge cases."
)


def main() -> None:
    # The gate requires 1 to 200 characters of UTF-8 text, not only
    # whitespace. Fail loudly here instead of shipping an invalid entry.
    text = LINE.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry is {len(text)} characters, must be 1-200")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
