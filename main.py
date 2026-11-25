#!/usr/bin/env python3
"""The One-Liner Groan-Off — deterministic dad-joke entry writer."""

import os
import sys

ENTRY = "My suitcase refuses to travel \u2014 it says it's carrying too much emotional baggage."

OUTPUT_PATH = "/output/entry.txt"


def validate(text):
    """Validate the entry text. Returns the character count.

    Raises ValueError if the text is empty/whitespace-only, outside
    1-140 characters, contains a newline, or has leading/trailing
    whitespace.
    """
    if not text or not text.strip():
        raise ValueError("entry is empty or whitespace-only")
    if len(text) < 1 or len(text) > 140:
        raise ValueError("entry must be 1-140 characters, got %d" % len(text))
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text != text.strip():
        raise ValueError("entry has leading/trailing whitespace")
    return len(text)


def main():
    text = ENTRY
    text.encode("utf-8")  # UTF-8 check
    count = validate(text)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    print("%d characters written to %s" % (count, OUTPUT_PATH))
    return 0


if __name__ == "__main__":
    sys.exit(main())
