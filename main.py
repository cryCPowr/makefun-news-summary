# News summary entry for make.fun bounty news-summary-01.
# The program writes the summary in summary.txt to /output/entry.txt
# (or $MAKEFUN_OUTPUT_DIR/entry.txt when run locally).
# Python 3.13, standard library only, no network, no clock:
# two runs write identical bytes.

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

# The gate takes UTF-8 text of 1 to 2,000 characters that is not only
# white space, so refuse to write an invalid entry.
summary = (ROOT / "summary.txt").read_text(encoding="utf-8")
assert 1 <= len(summary) <= 2000, "summary must be 1 to 2,000 characters"
assert summary.strip(), "summary must not be only white space"

OUT.mkdir(parents=True, exist_ok=True)
(OUT / "entry.txt").write_text(summary, encoding="utf-8")
