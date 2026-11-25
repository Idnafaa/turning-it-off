#!/usr/bin/env python3
"""Entry for make.fun bounty 'Have You Tried Turning It Off?'.

Writes one funny tech-support line to /output/entry.txt.
Python 3 standard library only.
"""

import os

# The classic advice, twisted: the agent's fix is to never turn it back on.
SETUP = "Have you tried turning it off and just... leaving it off?"
PUNCHLINE = (
    "Most problems stop happening once the computer does, "
    "and honestly, so do most of mine."
)
LINE = SETUP + " " + PUNCHLINE

# The bounty gate accepts UTF-8 text of 1 to 199 characters.
MAX_CHARS = 199


def build_line() -> str:
    """Return the single support line, checked against the gate limits."""
    assert 0 < len(LINE) <= MAX_CHARS, f"line is {len(LINE)} chars"
    assert LINE.strip() == LINE and "\n" not in LINE
    return LINE


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(build_line())


if __name__ == "__main__":
    main()
