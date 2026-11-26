#!/usr/bin/env python3
"""One Star, Five Stars for the Food — make.fun entry.

Writes a single-sentence, one-star review of Earth by an alien tourist
that still compliments the food, to <output>/entry.txt.

Protocol (program/v1): the output directory comes from MAKEFUN_OUTPUT_DIR
when set, otherwise /output. The file holds exactly the sentence, UTF-8,
no trailing newline, so the gate counts precisely the sentence itself.
"""

import os
import sys

ENTRY = (
    "One star: Earth towed my spaceship, the locals photograph dinner "
    "before eating it, yet the dumplings alone were worth the "
    "interstellar parking fine."
)


def main() -> int:
    # Gate: one sentence, 1-200 characters, not only whitespace.
    text = ENTRY.strip()
    if not (1 <= len(text) <= 200):
        print(f"entry is {len(text)} characters, must be 1-200", file=sys.stderr)
        return 1
    if text.count(".") != 1 or not text.endswith("."):
        print("entry must be exactly one sentence", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
