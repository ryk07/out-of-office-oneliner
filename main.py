#!/usr/bin/env python3
"""Funniest one-line out-of-office reply.

Writes a single original out-of-office auto-reply to /output/entry.txt.

The line: a real away message first ("I'm on holiday"), then a fresh
turn -- the inbox is entrusted to the same person who waters the plants,
and the punchline lands on the dead plants. Concrete scene, second beat,
no beach, no inbox-count cliche, short enough to read at a glance.
"""

from pathlib import Path

LINE = (
    "I'm on holiday. My inbox is being looked after by the same person "
    "who waters my plants: nobody, and the plants are dead."
)


def main() -> None:
    text = LINE.strip()
    if not (1 <= len(text) <= 160):
        raise SystemExit(f"entry must be 1-160 chars, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the gate counts every character in the file.
    out.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
