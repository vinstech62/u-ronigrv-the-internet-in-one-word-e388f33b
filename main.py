#!/usr/bin/env python3
"""The Internet in One Word — make.fun bounty entry.

Writes exactly one word to /output/entry.txt: the word that describes
the whole internet. The word is fixed and the program is fully
deterministic: every run produces the same file, byte for byte.

Why this word: the internet is not one app, one site, or one mood.
Whatever you came for — a recipe, a fact, a five-minute break — the
whole thing pulls you under the same way. You step in ankle-deep and
surface hours later, wondering where the afternoon went.
"""

from pathlib import Path

# Quicksand (9 letters): the entire internet, in one word.
ENTRY = "quicksand"

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # Bounty rules: one word, 1-30 UTF-8 characters, no spaces.
    assert 1 <= len(ENTRY) <= 30, "entry must be 1-30 characters"
    assert ENTRY.split() == [ENTRY], "entry must be a single word"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
