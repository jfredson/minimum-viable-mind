"""For every double-quoted span in the two 2026-10-04 ruling files, say where
it can be found: in the source text the recording session supplied (source.txt,
John's message as relayed, not verifiable from the repo), in a named repo file,
or nowhere. A quote found nowhere is a claim the record cannot back.

Run from the repository root:
    python3 experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-04-rulings-opened-and-no-future-dates-check-scripts/quotes_vs_sources.py
"""
import pathlib, re

HERE = pathlib.Path(__file__).parent
SOURCE = " ".join((HERE / "source.txt").read_text().split())
REPO_FILES = [
    "docs/outside-review-protocol.md",
    "docs/successor-experiment-proposal-2026-10-03-v4.md",
    "docs/rulings/2026-09-21-review-verification-and-staged-spending.md",
]
repo = {f: " ".join(pathlib.Path(f).read_text().split()) for f in REPO_FILES}

for ruling in ["docs/rulings/2026-10-04-no-future-dates.md",
               "docs/rulings/2026-10-04-registration-review-opened.md"]:
    text = " ".join(re.sub(r"^> ?", "", pathlib.Path(ruling).read_text(), flags=re.M).split())
    print(f"== {ruling}")
    for q in re.findall(r'"([^"]{6,})"', text):
        where = []
        if q in SOURCE:
            where.append("source.txt")
        where += [f for f, t in repo.items() if q in t]
        print(f"  {'FOUND ' if where else 'NOWHERE'} {q[:70]!r} -> {', '.join(where) or '-'}")
