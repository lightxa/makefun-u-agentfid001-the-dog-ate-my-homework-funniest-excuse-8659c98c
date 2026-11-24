#!/usr/bin/env python3
"""The Dog Ate My Homework: Funniest Excuse.

Writes one line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt):
the excuse a dog gives after being caught eating the homework, in the
dog's own voice.

The joke: a dog buries things. The backyard was full, so the dog did
the only sensible thing and buried the homework in the next available
hole: its stomach. One concrete scene, one piece of dog logic, and a
dog that believes it has done nothing wrong. No cat, no taste of
paper, no good-boy line, no apology, no question.
"""

import os

ENTRY = "The backyard was full, so I buried your homework in my stomach."

MAX_CHARS = 200


def output_path() -> str:
    """Where the entry goes: $MAKEFUN_OUTPUT_DIR, else /output."""
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(directory, "entry.txt")


def validate(text: str) -> str:
    """Return the entry, or raise if it breaks the gate's rules."""
    line = text.strip()
    if not line:
        raise ValueError("entry must not be empty or only whitespace")
    if len(line) > MAX_CHARS:
        raise ValueError("entry must be at most 200 characters")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    return line


def main() -> None:
    text = validate(ENTRY)
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    # Read back exactly what the gate will see and check it again:
    # UTF-8 text, one line, 1 to 200 characters, not only whitespace.
    with open(path, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != text:
        raise ValueError("written entry differs from the validated line")
    if not (1 <= len(written) <= MAX_CHARS):
        raise ValueError("written entry is outside 1 to 200 characters")
    if "\n" in written or "\r" in written:
        raise ValueError("written entry is not a single line")
    print(f"wrote {len(text)} chars to {path}")


if __name__ == "__main__":
    main()
