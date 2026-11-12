# News summary entry for make.fun bounty news-summary-01.
# The summary is the summary.txt beside this file; the program copies it
# to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt for local runs).
# Standard library only, no network, no clock: two runs write identical bytes.

import os
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

# The gate takes UTF-8 text of 1 to 2,000 characters that is not only
# white space, so check the summary against those three rules and fail
# loudly rather than writing an invalid entry.
text = (HERE / "summary.txt").read_text(encoding="utf-8")
assert 1 <= len(text) <= 2000, "summary must be 1 to 2,000 characters"
assert any(not ch.isspace() for ch in text), "summary must not be only white space"

OUT_DIR.mkdir(parents=True, exist_ok=True)
(OUT_DIR / "entry.txt").write_text(text, encoding="utf-8")
