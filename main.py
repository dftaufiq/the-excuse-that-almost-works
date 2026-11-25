"""Write the excuse line to /output/entry.txt for make.fun's
"The Excuse That Almost Works" bounty.

The entry is one fixed line, chosen by pairwise judging of eight variants
against the judge's brief (see variants.md in the build folder): a boring,
specific, believable home emergency with a 2-beat structure — the burst at
3am, then the reveal that the kitchen is ankle-deep and the flat can't be
left. No GTA mention, no illness, no dead grandmother, no flat tyre.
Deterministic: the same bytes on every run.
"""

import os

LINE = "Morning, sorry, boiler burst at 3am, plumber's here till noon and the kitchen's ankle-deep, can't leave the flat."

# The sealed gate (RULES.txt): /output/entry.txt must be UTF-8 text of
# 1-140 characters, not only whitespace, one line; the brief caps the line
# at 20 words. Refuse to write anything that breaks either limit.
WORDS = LINE.split()
if not 1 <= len(LINE) <= 140 or not LINE.strip() or "\n" in LINE:
    raise SystemExit("entry line violates the 1-140 char single-line gate")
if len(WORDS) > 20:
    raise SystemExit("entry line is over the 20-word cap")

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)
