#!/usr/bin/env python3
"""Unsent: The Micro-Confession Sprint.

Writes a two-part micro-confession to /output/entry.txt:
a To: line naming who it was meant for, and the unsent message
itself, one line written exactly as it was typed.
Pure standard library, deterministic output.
"""

import os
import sys

ENTRY = (
    "To: my little brother\n"
    "i still have the apology i wrote the night you moved out "
    "saved in my notes, and i read it every year on your birthday"
)


def main() -> int:
    out_path = sys.argv[1] if len(sys.argv) > 1 else "/output/entry.txt"
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
