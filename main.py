"""One-Line Office Jokes entry for make.fun.

Writes a single-line office joke to /output/entry.txt
(MAKEFUN_OUTPUT_DIR overrides the output directory).
Pure Python standard library, no network, deterministic.
"""

import os
from pathlib import Path

LINE = "The printer jammed on page 1 of 1, so I now own a very expensive paperweight that judges me."

OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 199, f"line must be 1-199 chars, got {len(text)}"
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "entry.txt").write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
