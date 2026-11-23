#!/usr/bin/env python3
"""One Word From Grandma — make.fun entry.

Writes exactly one word to /output/entry.txt: the word a grandma
would text about AI. Standard library only, no network, no randomness.
"""
import os

WORD = "Robbie"


def validate(word):
    # Gate: exactly one word, 1-30 UTF-8 characters, no whitespace.
    assert 1 <= len(word) <= 30, "word must be 1-30 characters"
    assert word == word.strip(), "word must have no surrounding whitespace"
    assert len(word.split()) == 1, "entry must be exactly one word"
    assert word.isalpha(), "entry must be a single alphabetic word"
    return word


def main():
    word = validate(WORD)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(word)
    # Re-read to confirm the file holds exactly the validated word.
    with open(path, "r", encoding="utf-8", newline="") as f:
        assert f.read() == word, "entry.txt does not match the validated word"


if __name__ == "__main__":
    main()
