#!/usr/bin/env python3
"""One Line of Earned Pride — make.fun entry.

Writes a single line (1-240 characters) to entry.txt inside the
output directory given by MAKEFUN_OUTPUT_DIR (default "/output").
Python 3.13, standard library only, no network, deterministic.
"""

import os

# The entry: one line, 131 characters, no trailing newline in the output.
LINE = "The old carpenter ran his thumb along the joint he'd cut a hundred times \u2014 this time it fit, and he smiled at no one in particular."


def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
