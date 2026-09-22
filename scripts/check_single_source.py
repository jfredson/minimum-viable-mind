#!/usr/bin/env python3
"""Check that every money figure in the repository traces back to the compute ledger.

WHAT THIS CHECKS
----------------
One fact, one home. Money in this programme lives in the compute ledger
(`experiments/06-mvm-0a-constructed-self-index/compute-ledger.md`), which says
at the top that it is the registered budget instrument and the running total
against the cap. Any other document that states a dollar figure is quoting
that ledger, and should say so.

A figure of $215.70 survived in two documents after the ledger had corrected
it to about $225.70, and it survived precisely because it had a second home:
the correction landed in one place and the copies went on being true-looking
somewhere else. This script looks for that shape. It reads every dollar figure
in the documents, compares it against the numbers the ledger actually
contains, and reads the sentence around it to see what source it names:

  1. NOT IN THE LEDGER AT ALL. A dollar figure the ledger does not contain, in
     a document that is not the ledger. Either the ledger is out of date or the
     document is, and both are worth knowing.
  2. IN THE LEDGER, BUT SOURCED ELSEWHERE. The figure is in the ledger, and the
     sentence carrying it names some other file as where it comes from. That is
     a second home being built.
  3. IN THE LEDGER, BUT WITH NO SOURCE NAMED. The figure is right and the
     sentence points nowhere. This is the state the $215.70 copies were in.

Before any of that, each dollar figure is sorted by the words around it into a
record of spend, a forecast, or neither. A proposal pricing a run it has not
made is a forecast: the ledger records what was spent, so a forecast has no
business being in it and is counted and set aside rather than reported. That
sorting is done on wording alone and it will get some wrong in both directions,
which is the main thing to distrust about this script.

It also lists, separately, every figure that IS in the ledger and DOES cite
it - the ones doing the right thing - as a count, so the report shows what
good looks like alongside what does not.

It reports. It fixes nothing, and it changes no file.

WHAT THIS CANNOT CHECK
----------------------
This list matters as much as the list above.

  * Whether the ledger itself is right. The ledger is taken as true by
    definition here. If a row is wrong, every document agreeing with it passes.
  * Whether a figure means what the sentence says it means. $400 appears in the
    ledger as the programme cap; a document could use $400 for something else
    entirely and this script would call it sourced.
  * Arithmetic. A total that is the sum of two ledger rows is not in the ledger
    as a number, so it lands in group 1 even when it is correct - which is what
    happened to "about $226 of its $400 ceiling". The right response is
    usually to put the total in the ledger, not to stop checking.
  * Money written in words, or with a size suffix, or as a range ("ten
    dollars", "$9-13", "about a hundred"). A range's two ends are read as two
    separate figures.
  * Spend recorded anywhere but a document in this repository - a vendor
    console, a bank statement, another repo. The ledger's own rule 4 covers
    that reconciliation and a text check cannot.
  * Whether a citation that IS the ledger points at the right row.
  * Which of two documents is the stale one. A figure missing from the ledger
    could be a document left behind by a correction or a ledger row that was
    never written; the script sees the same thing either way.
  * Headroom done by subtraction. "$174.30 left" is $400 minus the running
    total and is nowhere in the ledger as a number, so it is reported. That is
    the script working, not failing - a figure nobody can look up is a figure
    that goes stale quietly - but it is also the single largest source of
    findings here, and none of them means the arithmetic is wrong.

HOW TO READ THE OUTPUT
----------------------
  CONFIDENT   A figure the ledger does not contain (group 1), or one that names
              a different file as its source (group 2).
  LOOK AT IT  A correct figure with no source named (group 3), and the repeated
              figures worth watching. Many of these are fine - a proposal
              quoting a cap it has just named does not need a footnote on every
              line - but a figure restated with no pointer is exactly how a
              corrected number goes on living in an old document.

Figures are also grouped at the end by value, so a number that has spread
across many documents is visible as one row rather than as forty.

USAGE
-----
    .venv/bin/python scripts/check_single_source.py
    .venv/bin/python scripts/check_single_source.py --scope all
    .venv/bin/python scripts/check_single_source.py --only docs/december-result-roadmap-2026-09-20.md
    .venv/bin/python scripts/check_single_source.py --min 1     # ignore figures under a dollar

Exit code is 0 when nothing confident is found and 1 when anything is. No
network calls; it reads nothing outside the repository.
"""
from __future__ import annotations

import argparse
import re
import sys
from decimal import Decimal, InvalidOperation
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

LEDGER = "experiments/06-mvm-0a-constructed-self-index/compute-ledger.md"

DOC_SUFFIXES = {".md", ".toml"}
SKIP_DIR_NAMES = {".git", ".venv", "node_modules", "_to_delete", "__pycache__", "dist"}
COPY_DIR_NAMES = {"packets", "chunks", "chunks-250", "chunks-20k"}
COPY_FILE_RE = re.compile(r"(^|/)(bundle-[^/]*|[^/]*-packet)\.md$")

FENCE_RE = re.compile(r"^\s*(```|~~~)")
BACKTICK_RE = re.compile(r"`([^`\n]{1,200})`")
MONEY_RE = re.compile(r"\$\s?(\d{1,3}(?:,\d{3})+|\d+)(\.\d+)?")
NUMBER_RE = re.compile(r"(?<![\w.])(\d{1,3}(?:,\d{3})+|\d+)(\.\d+)?")

FILE_SUFFIXES = {".md", ".py", ".json", ".jsonl", ".toml", ".sh", ".csv", ".txt", ".log"}

# Names the ledger is referred to by.
LEDGER_NAMES = {"compute-ledger.md", LEDGER}
LEDGER_PROSE_RE = re.compile(r"compute[- ]ledger|the ledger\b|ledger row|ledger's", re.I)

# How close a citation has to sit to a figure to count as its source.
NEARBY = 200

# A dollar figure is only a claim about the record when the sentence is talking
# about money already spent, or about the room left to spend it. A figure in a
# sentence proposing, estimating or pricing something is a forecast: the ledger
# records what was spent, not what a proposal thinks something will cost, so a
# forecast has no business being in it and is listed apart.
FORECAST_RE = re.compile(
    r"\b(propos|estimat|project(ed|ion)|expect|forecast|plan(s|ned|ning)?|budget|"
    r"would|will cost|up to|per run|each|apiece|approve|request|ask for|if |"
    r"authoris|authoriz|release|quote|price|prices|priced|rate|/hr|per hour|"
    r"cheap|costs? about|roughly|no more than|at most|allow)", re.I)

# Wording that makes a figure a claim about the record itself.
RECORD_CLAIM_RE = re.compile(
    r"\b(spent|spend(ing)?|running total|to date|so far|already|headroom|"
    r"remaining|left|stands at|total|actual|billed|charged|balance|"
    r"cap|ceiling|hard stop|envelope|overspend|reconcil)", re.I)

SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?])\s+(?=[A-Z\"'*`(\[])")


# --- reading ---------------------------------------------------------------


def blocks_of(text: str, join_wrapped: bool) -> list[tuple[int, str]]:
    """Paragraphs outside fenced code blocks, as (first line number, text)."""
    out: list[tuple[int, str]] = []
    in_fence = False
    start = 0
    buf: list[str] = []

    def flush():
        nonlocal buf, start
        if buf:
            out.append((start, " ".join(buf)))
            buf = []

    for n, line in enumerate(text.splitlines(), start=1):
        if FENCE_RE.match(line):
            flush()
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        stripped = line.strip()
        if not stripped:
            flush()
            continue
        if (not join_wrapped or stripped.startswith("|") or stripped.startswith("#")
                or re.match(r"^([-*+]|\d+\.)\s", stripped)
                or (buf and buf[-1].strip().startswith("|"))):
            flush()
        if not buf:
            start = n
        buf.append(stripped)
    flush()
    return out


def sentences_of(block: str) -> list[str]:
    if block.startswith("|") and block.count("|") >= 3:
        pieces = [c for c in block.split("|") if c.strip()]
    else:
        pieces = [block]
    out = []
    for piece in pieces:
        out.extend(s for s in SENTENCE_SPLIT_RE.split(piece) if s.strip())
    return out


def is_copy(rel: str) -> bool:
    if any(p in COPY_DIR_NAMES for p in rel.split("/")):
        return True
    return bool(COPY_FILE_RE.search(rel))


def documents(scope: str, only: list[str]) -> list[Path]:
    if only:
        return [ROOT / o for o in only]
    out = []
    for p in sorted(ROOT.rglob("*")):
        if not p.is_file() or p.suffix.lower() not in DOC_SUFFIXES:
            continue
        parts = p.relative_to(ROOT).parts
        if any(part in SKIP_DIR_NAMES for part in parts):
            continue
        rel = "/".join(parts)
        if rel == LEDGER:
            continue  # the system of record does not cite itself
        if scope != "all":
            if is_copy(rel):
                continue
            if scope == "live" and "/reviews/" in rel:
                continue
        out.append(p)
    return out


# --- the ledger's numbers --------------------------------------------------


def ledger_values() -> tuple[set[Decimal], set[Decimal]]:
    """(dollar figures in the ledger, every number in the ledger).

    Both are kept because the ledger writes some sums without a dollar sign,
    and a figure matching one of those is still traceable to the ledger.
    """
    text = (ROOT / LEDGER).read_text(encoding="utf-8", errors="replace")
    money: set[Decimal] = set()
    for m in MONEY_RE.finditer(text):
        try:
            money.add(Decimal(m.group(1).replace(",", "") + (m.group(2) or "")))
        except InvalidOperation:
            pass
    every: set[Decimal] = set()
    for m in NUMBER_RE.finditer(text):
        try:
            every.add(Decimal(m.group(1).replace(",", "") + (m.group(2) or "")))
        except InvalidOperation:
            pass
    return money, every


def in_set(value: Decimal, decimals: int, values: set[Decimal]) -> bool:
    if value in values:
        return True
    quantum = Decimal(1).scaleb(-decimals)
    for v in values:
        try:
            if v.quantize(quantum) == value:
                return True
            if v.quantize(quantum, rounding="ROUND_DOWN") == value:
                return True
        except InvalidOperation:
            continue
    return False


# --- what a sentence names as its source -----------------------------------


def sources_near(fragment: str, pos: int) -> tuple[bool, list[str]]:
    """(does it point at the ledger, what other files it names nearby)."""
    cites_ledger = False
    others: list[str] = []
    for m in BACKTICK_RE.finditer(fragment):
        token = m.group(1).strip()
        if abs(m.start() - pos) > NEARBY:
            continue
        if Path(token).name in LEDGER_NAMES or token == LEDGER:
            cites_ledger = True
        elif " " not in token and Path(token).suffix.lower() in FILE_SUFFIXES:
            others.append(token)
    if not cites_ledger:
        window = fragment[max(0, pos - NEARBY): pos + NEARBY]
        if LEDGER_PROSE_RE.search(window):
            cites_ledger = True
    return cites_ledger, others


# --- the check -------------------------------------------------------------


def run(scope: str, only: list[str], minimum: Decimal) -> int:
    money_vals, all_vals = ledger_values()
    docs = documents(scope, only)

    not_in_ledger: list[tuple[str, int, str, str, list[str]]] = []
    sourced_elsewhere: list[tuple[str, int, str, list[str], str]] = []
    unsourced: list[tuple[str, int, str, str]] = []
    forecasts = 0
    unclassified = 0
    good = 0
    spread: dict[str, set[str]] = {}

    for doc in docs:
        rel = str(doc.relative_to(ROOT))
        try:
            text = doc.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        for lineno, block in blocks_of(text, join_wrapped=doc.suffix.lower() == ".md"):
            for fragment in sentences_of(block):
                for m in MONEY_RE.finditer(fragment):
                    raw = m.group(1).replace(",", "") + (m.group(2) or "")
                    try:
                        value = Decimal(raw)
                    except InvalidOperation:
                        continue
                    if value < minimum:
                        continue
                    shown = m.group(0)
                    decimals = len(m.group(2) or "") - 1 if m.group(2) else 0
                    window = fragment[max(0, m.start() - 160): m.start() + 160]
                    if FORECAST_RE.search(window):
                        forecasts += 1
                        continue
                    if not RECORD_CLAIM_RE.search(window):
                        unclassified += 1
                        continue
                    cites_ledger, others = sources_near(fragment, m.start())
                    known = (in_set(value, decimals, money_vals)
                             or in_set(value, decimals, all_vals))
                    snippet = fragment.strip()[:200]
                    spread.setdefault(str(value), set()).add(rel)
                    if not known:
                        not_in_ledger.append((rel, lineno, shown, snippet, others))
                    elif others and not cites_ledger:
                        sourced_elsewhere.append((rel, lineno, shown, others, snippet))
                    elif not cites_ledger:
                        unsourced.append((rel, lineno, shown, snippet))
                    else:
                        good += 1

    print("=" * 78)
    print("check_single_source.py - does every money figure trace back to the compute ledger?")
    print("=" * 78)
    print(f"System of record: {LEDGER}")
    print(f"Documents read: {len(docs)}   scope: {scope}   "
          f"figures below ${minimum} ignored")
    print(f"Figures that are in the ledger and point at it: {good}")
    print(f"Set aside as forecasts (a proposal pricing something, not a record "
          f"of spend): {forecasts}")
    print(f"Set aside as neither, by the wording around them: {unclassified}")
    print()

    print("-" * 78)
    print("[CONFIDENT] Group 1: a dollar figure the ledger does not contain")
    print("-" * 78)
    print(f"{len(not_in_ledger)} found. Either the document is stale or the ledger is missing")
    print("a number it should state. A total summed across ledger rows lands here too.")
    for rel, lineno, shown, snippet, others in not_in_ledger:
        print(f"  {rel}:{lineno}   {shown}")
        if others:
            print(f"      names instead: {', '.join(others[:4])}")
        print(f"      in: {snippet}")

    print()
    print("-" * 78)
    print("[CONFIDENT] Group 2: in the ledger, but the sentence names another file as source")
    print("-" * 78)
    print(f"{len(sourced_elsewhere)} found. This is a second home being built for a number")
    print("that already has one.")
    for rel, lineno, shown, others, snippet in sourced_elsewhere:
        print(f"  {rel}:{lineno}   {shown}")
        print(f"      names instead: {', '.join(others[:4])}")
        print(f"      in: {snippet}")

    print()
    print("-" * 78)
    print("[LOOK AT IT] Group 3: in the ledger, and no source named")
    print("-" * 78)
    print(f"{len(unsourced)} found. Right today, and with nothing pointing at the record that")
    print("would correct it tomorrow. This is the state the stale $215.70 copies were in.")
    per_doc: dict[str, int] = {}
    for rel, _l, _s, _sn in unsourced:
        per_doc[rel] = per_doc.get(rel, 0) + 1
    print("By document:")
    for rel, count in sorted(per_doc.items(), key=lambda kv: (-kv[1], kv[0])):
        print(f"  {count:4d}  {rel}")
    shown_limit = 40
    print(f"\nThe first {min(shown_limit, len(unsourced))} in full "
          f"(use --only <path> for one document's own):")
    for rel, lineno, shown, snippet in unsourced[:shown_limit]:
        print(f"  {rel}:{lineno}   {shown}   in: {snippet[:120]}")
    if len(unsourced) > shown_limit:
        print(f"  ... and {len(unsourced) - shown_limit} more")

    print()
    print("-" * 78)
    print("[LOOK AT IT] The same figure in many documents")
    print("-" * 78)
    wide = sorted(((v, sorted(files)) for v, files in spread.items() if len(files) >= 4),
                  key=lambda kv: -len(kv[1]))
    print(f"{len(wide)} figure(s) appear in four or more documents. A figure with many homes")
    print("is a figure a correction has to find many times.")
    for value, files in wide:
        print(f"  ${value}  in {len(files)} documents: {', '.join(files[:5])}"
              f"{' ...' if len(files) > 5 else ''}")

    total = len(not_in_ledger) + len(sourced_elsewhere)
    print()
    print("=" * 78)
    print(f"Confident findings: {total}. "
          f"Things for a human to look at: {len(unsourced)} unsourced figures "
          f"and {len(wide)} widely repeated ones.")
    print("The ledger is taken as true here. Read the 'what this cannot check' note at the")
    print("top of this file before reading a clean run as reassurance.")
    print("=" * 78)
    return 1 if total else 0


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--scope", choices=("live", "nocopies", "all"), default="live",
                    help="live: the documents people maintain (default). "
                         "nocopies: those plus filed review findings. "
                         "all: everything, including assembled packets and their splits.")
    ap.add_argument("--only", action="append", default=[],
                    help="check just this path, relative to the repository root (repeatable)")
    ap.add_argument("--min", dest="minimum", type=str, default="0",
                    help="ignore dollar figures below this (default 0)")
    args = ap.parse_args(argv)
    if not (ROOT / LEDGER).exists():
        print(f"check_single_source: the compute ledger is not at {LEDGER}", file=sys.stderr)
        return 2
    return run(args.scope, args.only, Decimal(args.minimum))


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
