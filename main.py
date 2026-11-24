#!/usr/bin/env python3
"""The Funniest Out-of-Office -- make.fun entry.

Writes exactly one out-of-office auto-reply line to /output/entry.txt.
The line is a fixed string: the joke is the entry, not a generator,
so every run produces byte-identical output.
"""

import os
import sys

LINE = (
    "I'm out of the office until Monday, running an experiment to see "
    "if my job notices I'm gone. Early results are encouraging."
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> int:
    text = LINE.strip()
    if not text:
        print("error: entry line is empty", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("error: entry line must be a single line", file=sys.stderr)
        return 1
    if len(text) > 140:
        print(
            f"error: entry line is {len(text)} chars, over the 140 limit",
            file=sys.stderr,
        )
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH) or ".", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
