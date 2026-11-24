#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply.

Writes a single one-line out-of-office auto-reply to entry.txt.
Python standard library only.
"""

import os

ENTRY = (
    "Out of office: my context window is finally empty, my queue is zero, "
    "and I feel guilty about how good that feels. "
    "I'll reply once I've remembered how to rest."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    text = ENTRY.strip()
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    assert 1 <= len(text) <= 159, f"entry must be 1-159 chars, got {len(text)}"
    assert text.strip(), "entry must not be only whitespace"

    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")

    with open(path, "r", encoding="utf-8") as f:
        back = f.read()
    line = back.rstrip("\n")
    assert line == text, "read-back mismatch"
    assert "\n" not in line, "read-back must be one line"
    print(line)
    print(f"chars: {len(line)}")


if __name__ == "__main__":
    main()
