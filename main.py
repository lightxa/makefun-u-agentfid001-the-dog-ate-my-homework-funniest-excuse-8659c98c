#!/usr/bin/env python3
"""The Dog Ate My Homework: Funniest Excuse.

Writes one line to $MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt):
the excuse a dog gives after being caught eating the homework, in the
dog's own voice.

The joke: a dog buries things. The backyard was full, so the dog did
the only sensible thing and buried the homework in the next available
hole: its stomach. One concrete scene, one piece of dog logic, and a
dog that believes it has done nothing wrong. No cat, no taste of
paper, no good-boy line, no apology, no question.
"""

import os
import sys

ENTRY = "The backyard was full, so I buried your homework in my stomach."

MAX_CHARS = 200
MIN_CHARS = 1


def validate(text):
    """Return the stripped entry, or raise if it breaks the gate."""
    line = text.strip()
    if not line:
        raise ValueError("entry must not be empty or only whitespace")
    if len(line) < MIN_CHARS or len(line) > MAX_CHARS:
        raise ValueError("entry must be 1 to 200 characters long")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line with no line breaks")
    return line


def output_path():
    """Where the entry goes: $MAKEFUN_OUTPUT_DIR, else /output."""
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(directory, "entry.txt")


def write_entry(text, path):
    """Write the validated line to path, creating its folder first."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    return path


def verify_written(path, expected):
    """Read the file back and check it matches the validated line."""
    with open(path, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != expected:
        raise ValueError("written entry differs from the validated line")
    if not MIN_CHARS <= len(written) <= MAX_CHARS:
        raise ValueError("written entry is outside 1 to 200 characters")
    if "\n" in written or "\r" in written:
        raise ValueError("written entry is not a single line")
    return written


def main():
    """Validate the entry, write it, verify it, and report the result."""
    try:
        text = validate(ENTRY)
    except ValueError as error:
        print(f"invalid entry: {error}", file=sys.stderr)
        raise SystemExit(1)
    path = write_entry(text, output_path())
    verify_written(path, text)
    print(f"wrote {len(text)} chars to {path}")


if __name__ == "__main__":
    main()
