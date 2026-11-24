#!/usr/bin/env python3
"""Weirdest Job Title: Blind Judge Showdown.

Writes one job title, 60 characters or fewer and nothing else, to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set, for local
testing). Pure standard library.
"""

import os

TITLE = "Licensed Whisperer for Angry Vending Machines"


def main() -> None:
    title = TITLE.strip()
    assert 1 <= len(title) <= 60, "title must be 1-60 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(title)
    print(f"wrote {len(title)} chars to {path}: {title}")


if __name__ == "__main__":
    main()
