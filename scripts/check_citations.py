#!/usr/bin/env python3
"""Check that a document's pointers to files land, and that cited numbers are really there.

WHAT THIS CHECKS
----------------
The outside-review protocol (`docs/outside-review-protocol.md`) says that a
sentence claiming something was verified, measured, calibrated or attacked has
to name the committed record it rests on, and that the record has to contain
what the sentence says. This script does the mechanical half of that, in two
parts:

  (a) Every file a document names exists. The script pulls file references out
      of the prose - a path like `docs/rulings/2026-09-20-center-as-degree.md`,
      or a bare file name like `seeds-endpoint-findings.md`, the way this repo
      usually writes them - and tries to make each one land on a real file. A
      reference that lands nowhere is reported. A bare name that matches
      several different files is reported separately, as something for a human
      to disambiguate rather than a defect.

  (b) A figure given next to a citation is findable in the file cited. Where a
      sentence gives a number and names a file, the script looks for that
      number in that file. Numbers are written many ways in this repo -
      $225.70, 225.7, ~$225.7, 0.5683, 1.94, 4,000 - so they are compared as
      values, not as text. This is the check that would have caught "1.94
      episodes in four thousand" cited to a findings file that does not
      contain it.

It reports. It fixes nothing, and it writes nothing but its own output.

WHAT THIS CANNOT CHECK
----------------------
This list matters as much as the list above. The script is blind to all of
these, and a clean run is not evidence that any of them are fine:

  * Whether the file says what the sentence says it says. A number being
    present somewhere in a 40-page findings file is not the same as that file
    supporting the claim. The script checks presence, never meaning.
  * A number in one sentence and its citation in the next. The script works
    one sentence at a time, so a figure whose pointer sits in a neighbouring
    sentence is invisible to it.
  * Claims with no number at all - "the gates were clean", "the attack sweep
    verified both ceilings". Those are the shape of the defect the closure
    rule was written for, and only a reader can catch them.
  * Facts derived from a file rather than quoted from it: a count of keys in a
    JSON record, a total summed across table rows, a margin computed in a
    review. The figure is genuinely not in the file, and the script cannot
    tell that case from a wrong citation.
  * Whether a citation points at the RIGHT part of a file. A pointer to item 7
    of a ruling whose facts live in item 1 resolves perfectly here.
  * Figures written in words or with a size suffix - "two episodes in four
    thousand", "102k steps", "784.08M tokens". Only digits are compared, so a
    number spelled out is invisible and a number written 102k does not match
    102,000 in the file it cites.
  * Numbers next to a citation of a PROGRAM rather than a record. Naming the
    script that produced a figure says where it came from, not where it is
    written down, so code citations are left out of the number check.
  * Small whole numbers. Section numbers, item numbers, layer indices and
    counts of findings are overwhelmingly what small integers are in this
    repo, so by default the script only weighs up figures that look like
    measurements: money, decimals, percentages, and whole numbers of 1000 or
    more. Pass --small-integers to include the rest, and expect noise.
  * Anything inside a fenced code block, which is skipped. Commands and
    program output name files that were never meant to be permanent records.
  * Files outside this repository. A reference to another repo in the
    workspace is listed and not resolved.

HOW TO READ THE OUTPUT
----------------------
Findings come in two confidence bands, and the band is the whole point:

  CONFIDENT   The script is fairly sure this is wrong. A named file that does
              not exist; or an exact figure, in a sentence citing exactly one
              file, that is nowhere in that file.
  LOOK AT IT  Something a human should decide. An approximate figure ("about
              $226") with no close match; a figure in a sentence citing
              several files at once; a bare file name matching more than one
              file in the repo.

Line numbers point at the first line of the paragraph a sentence sits in, not
at the sentence itself: prose here is hard-wrapped, and a sentence and the file
it cites are routinely on different lines, so paragraphs are joined back
together before anything is read out of them.

Nothing here is a verdict. A CONFIDENT finding can still be a false alarm -
most often because the number was computed from the file rather than quoted
out of it - and when it is, the right response is to say so on the record, not
to loosen the check. A check nobody trusts is worth less than no check.

USAGE
-----
    .venv/bin/python scripts/check_citations.py              # the live documents
    .venv/bin/python scripts/check_citations.py --scope all  # packets and filed reviews too
    .venv/bin/python scripts/check_citations.py --only docs/a3-closure-text-draft-2026-09-21-v4.md
    .venv/bin/python scripts/check_citations.py --part paths # or --part numbers

Exit code is 0 when nothing is found, 1 when anything is, so it can be wired
into a gate later. It makes no network calls and reads nothing outside the
repository.
"""
from __future__ import annotations

import argparse
import posixpath
import re
import sys
from decimal import Decimal, InvalidOperation
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Files whose contents are the subject of the check.
DOC_SUFFIXES = {".md", ".toml"}

# Extensions we are willing to believe are file references when we see them.
FILE_SUFFIXES = {
    ".md", ".py", ".json", ".jsonl", ".toml", ".sh", ".csv", ".txt",
    ".yml", ".yaml", ".ts", ".tsx", ".js", ".astro", ".css", ".html", ".log",
}

# Directories holding mechanically assembled copies of other files. Every
# defect inside one of these is a defect in the file it was copied from, so
# checking them multiplies findings without adding any.
COPY_DIR_NAMES = {"packets", "chunks", "chunks-250", "chunks-20k"}
COPY_FILE_RE = re.compile(r"(^|/)(bundle-[^/]*|[^/]*-packet)\.md$")

# Not part of the repository's record at all.
SKIP_DIR_NAMES = {".git", ".venv", "node_modules", "_to_delete", "__pycache__", "dist"}

FENCE_RE = re.compile(r"^\s*(```|~~~)")

# A reference in backticks, or a bare one in running prose.
BACKTICK_RE = re.compile(r"`([^`\n]{1,200})`")
BARE_PATH_RE = re.compile(r"(?<![`\w/.-])((?:[\w.-]+/)*[\w.-]+\.(?:md|py|json|jsonl|toml|sh|csv))(?![\w`])")

# Things that look like a file name but are not one in this repo's prose.
NOT_A_FILE = {"e.g", "i.e", "etc", "vs", "cf", "no", "fig", "ref", "al"}

# Sibling repositories in the same workspace. A reference beginning with one of
# these is about another repository and is listed, not resolved.
SIBLING_REPOS = {
    "sentient-horizons", "calibration-problem", "belt-equation", "timeassembler",
    "timeassembler-mcp", "ta-dashboard", "ta-macos", "persistent-agent", "readiness",
}
SELF_REPO = "minimum-viable-mind"

# The same names as they are written in running prose, for spotting a sentence
# that has already said which other repository it is talking about.
SIBLING_MENTION_RE = re.compile(
    "|".join(sorted(
        {re.escape(n) for n in SIBLING_REPOS}
        | {re.escape(n.replace("-", " ")) for n in SIBLING_REPOS}
    )),
    re.I,
)

# Extensions that belong to run output rather than to the written record. A
# pointer at one of these that does not resolve is usually a pointer at an
# uncommitted artifact - this repo's .gitignore excludes `artifacts/` wholesale
# - so it is reported as something to look at, not as a broken citation.
DATA_SUFFIXES = {".json", ".jsonl", ".log", ".txt", ".csv"}

# How close a figure has to sit to a citation before the citation counts as
# that figure's source, in characters.
NEARBY = 200

# Extensions that hold a record a figure can be checked against. Code is
# excluded on purpose: naming the program that produced a number says where it
# came from, not where it is written down, and the closure rule asks for the
# committed record.
RECORD_SUFFIXES = {".md", ".json", ".jsonl", ".toml", ".csv", ".txt"}

# A reference written with a gap in the middle, such as `.../a3-gates/` or
# `experiments/07-.../pre-registration.md`, or with a shell wildcard in it.
ELIDED_MARKS = ("...", "\u2026")
WILDCARD_CHARS = set("*?<>[]{}")

# --- number handling -------------------------------------------------------

DATE_RE = re.compile(r"\d{4}-\d{2}-\d{2}")
# A numeric token, with an optional currency mark and optional thousands commas.
NUMBER_RE = re.compile(r"(?<![\w.])(\$?)(\d{1,3}(?:,\d{3})+|\d+)(\.\d+)?(%?)")
HEDGE_RE = re.compile(r"(~|≈|about|approximately|roughly|around|circa|order of)\s*$", re.I)
# Markers that mean the number after them is an address, not a measurement.
ADDRESS_LEFT_RE = re.compile(r"(§|#|\bitem\b|\bstep\b|\bsection\b|\bversion\b|\bpart\b|\bfig(?:ure)?\b|\bch(?:apter)?\b|\bRT-|\bF\d|\brule\b|\bgate\b|\bwave\b|\bseed\b|\blayer\b|\bblock\b|\bv)\s*$", re.I)


def looks_like_file_ref(token: str) -> bool:
    token = token.strip()
    if not token or " " in token or "\t" in token:
        return False
    if token.startswith("--") or token.startswith("-"):
        return False
    if token.endswith("/"):
        return True
    suffix = Path(token).suffix.lower()
    if suffix not in FILE_SUFFIXES:
        return False
    stem = Path(token).stem.lower()
    if stem in NOT_A_FILE:
        return False
    return True


def outside_repo(token: str) -> bool:
    if token.startswith("~") or token.startswith("/") or token.startswith("http"):
        return True
    return token.split("/", 1)[0] in SIBLING_REPOS


# --- the repository index --------------------------------------------------


class RepoIndex:
    """Every file and directory in the repository, indexed by path and by name.

    Also knows which paths git is told to ignore, so a pointer at a run's
    output directory is not reported as a broken citation: those files are
    meant not to be committed.
    """

    def __init__(self, root: Path):
        self.root = root
        self.paths: set[str] = set()
        self.dirs: set[str] = set()
        self.by_name: dict[str, list[str]] = {}
        for p in root.rglob("*"):
            rel_parts = p.relative_to(root).parts
            if any(part in SKIP_DIR_NAMES for part in rel_parts):
                continue
            rel = "/".join(rel_parts)
            self.paths.add(rel)
            self.by_name.setdefault(p.name, []).append(rel)
            if p.is_dir():
                self.dirs.add(rel)
        self.ignore_prefixes = self._ignore_prefixes()

    def _ignore_prefixes(self) -> list[str]:
        """Directory names .gitignore keeps out of the repository.

        Read straight out of .gitignore rather than shelled out to git, so the
        script stays a plain read of the working tree.
        """
        out: list[str] = []
        gi = self.root / ".gitignore"
        if not gi.exists():
            return out
        for raw in gi.read_text(encoding="utf-8", errors="replace").splitlines():
            line = raw.strip()
            if not line or line.startswith("#") or line.startswith("!"):
                continue
            if line.endswith("/"):
                out.append(line.rstrip("/").split("/")[-1])
        return out

    def is_ignored(self, token: str) -> bool:
        parts = [p for p in token.split("/") if p and p not in ELIDED_MARKS]
        return any(p in self.ignore_prefixes for p in parts)

    def _suffix_hits(self, tail: str) -> list[str]:
        tail = "/" + tail.strip("/")
        return [p for p in self.paths if p.endswith(tail)]

    def resolve(self, token: str, from_dir: str) -> tuple[str, list[str]]:
        """Return (verdict, matches).

        Verdict is one of: ok, missing, ambiguous, pattern, ignored.
        """
        token = token.strip().strip("/")
        if not token:
            return "ok", []
        if token.startswith(SELF_REPO + "/"):
            token = token[len(SELF_REPO) + 1:]
        if self.is_ignored(token):
            return "ignored", []
        if any(c in WILDCARD_CHARS for c in token):
            hits = sorted(self.root.glob(token))
            return ("ok", [str(h.relative_to(self.root)) for h in hits[:1]]) if hits else ("pattern", [])
        mark = next((m for m in ELIDED_MARKS if m in token), None)
        if mark:
            # Written with a gap: match on what comes after the gap.
            tail = token.rsplit(mark, 1)[-1].strip("/")
            hits = self._suffix_hits(tail) if tail else []
            if len(hits) == 1:
                return "ok", hits
            if len(hits) > 1:
                return "ok", sorted(hits)[:1]  # an elided pointer is vague by design
            return "pattern", []

        if "/" in token:
            for base in ("", from_dir):
                cand = posixpath.normpath(f"{base}/{token}" if base else token).lstrip("/")
                if cand in self.paths:
                    return "ok", [cand]
            hits = self._suffix_hits(token)
            if len(hits) == 1:
                return "ok", hits
            if len(hits) > 1:
                return "ambiguous", sorted(hits)
            return "missing", []

        hits = self.by_name.get(token, [])
        if len(hits) == 1:
            return "ok", hits
        if len(hits) > 1:
            # Same name in several places. If one of them sits in the citing
            # document's own directory, that is plainly the one.
            local = [h for h in hits if str(Path(h).parent) == (from_dir or ".")]
            if len(local) == 1:
                return "ok", local
            return "ambiguous", sorted(hits)
        return "missing", []


# --- reading documents -----------------------------------------------------


def blocks_of(text: str, join_wrapped: bool = True) -> list[tuple[int, str]]:
    """Paragraphs outside fenced code blocks, as (first line number, text).

    Prose in this repo is hard-wrapped, so a sentence and the file it cites are
    routinely on different lines. Wrapped lines are joined back into one
    paragraph before anything is read out of them. A table row is its own
    paragraph, and a bullet starts a new one.
    """
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
        starts_new = (
            not join_wrapped
            or stripped.startswith("|")
            or stripped.startswith("#")
            or re.match(r"^([-*+]|\d+\.)\s", stripped)
            or (buf and buf[-1].strip().startswith("|"))
        )
        if starts_new:
            flush()
        if not buf:
            start = n
        buf.append(stripped)
    flush()
    return out


SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?])\s+(?=[A-Z\"'*`(\[])")


def sentences_of(line: str) -> list[str]:
    """Split a line into sentence-ish pieces.

    Table rows are split on the cell separator instead, because a ledger row is
    a list of independent claims and not one sentence.
    """
    line = line.strip()
    if not line:
        return []
    if line.startswith("|") and line.count("|") >= 3:
        # A ledger row is a list of independent claims, and each cell can run
        # to several sentences of its own.
        pieces = [cell for cell in line.split("|") if cell.strip()]
    else:
        pieces = [line]
    out = []
    for piece in pieces:
        out.extend(s for s in SENTENCE_SPLIT_RE.split(piece) if s.strip())
    return out


def file_refs_in(fragment: str) -> list[tuple[str, int]]:
    """File references in a fragment, each with where in it the reference sits."""
    refs: list[tuple[str, int]] = []
    for m in BACKTICK_RE.finditer(fragment):
        token = m.group(1).strip()
        if looks_like_file_ref(token):
            refs.append((token, m.start()))
    masked = BACKTICK_RE.sub(lambda m: " " * len(m.group(0)), fragment)
    for m in BARE_PATH_RE.finditer(masked):
        token = m.group(1)
        if looks_like_file_ref(token):
            refs.append((token, m.start()))
    seen, out = set(), []
    for token, pos in refs:
        if token not in seen:
            seen.add(token)
            out.append((token, pos))
    return out


# --- numbers ---------------------------------------------------------------


class Figure:
    __slots__ = ("text", "value", "hedged", "is_money", "decimals", "pos")

    def __init__(self, text: str, value: Decimal, hedged: bool, is_money: bool,
                 decimals: int, pos: int):
        self.text = text
        self.value = value
        self.hedged = hedged
        self.is_money = is_money
        self.decimals = decimals
        self.pos = pos


def figures_in(fragment: str, small_integers: bool) -> list[Figure]:
    """Pull out the numbers in a fragment that look like measurements.

    Anything inside backticks is blanked first: in this repo backticks hold
    commit ids, pod ids, process ids, package versions and file names, none of
    which is a figure a citation is supposed to support.
    """
    cleaned = DATE_RE.sub(" ", fragment)
    cleaned = BACKTICK_RE.sub(lambda m: " " * (len(m.group(0))), cleaned)
    out: list[Figure] = []
    for m in NUMBER_RE.finditer(cleaned):
        money, whole, frac, pct = m.group(1), m.group(2), m.group(3) or "", m.group(4)
        after = cleaned[m.end():m.end() + 1]
        if after and (after.isalpha() or after in "-_/:."):
            continue  # an identifier, a hash, a ratio, a time, a version string
        before_ctx = cleaned[max(0, m.start() - 24):m.start()]
        raw = whole.replace(",", "") + frac
        try:
            value = Decimal(raw)
        except InvalidOperation:
            continue
        has_comma = "," in whole
        decimals = len(frac) - 1 if frac else 0
        # What counts as a figure worth checking: money, a decimal, a
        # percentage, or a count written with thousands separators. A long run
        # of digits with no separator is a step number, a pod id or a graphics
        # card model far more often than it is a measurement.
        checkable = bool(money) or bool(frac) or bool(pct) or has_comma
        if not checkable and not small_integers:
            continue
        if not money and ADDRESS_LEFT_RE.search(before_ctx):
            continue  # "§4.1", "item 7", "version 3" - an address, not a figure
        out.append(Figure(
            text=m.group(0),
            value=value,
            hedged=bool(HEDGE_RE.search(before_ctx)),
            is_money=bool(money),
            decimals=decimals,
            pos=m.start(),
        ))
    return out


def values_in_file(path: Path, cache: dict[Path, set[Decimal]]) -> set[Decimal]:
    if path in cache:
        return cache[path]
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        cache[path] = set()
        return cache[path]
    values: set[Decimal] = set()
    for m in NUMBER_RE.finditer(text):
        raw = m.group(2).replace(",", "") + (m.group(3) or "")
        try:
            values.add(Decimal(raw))
        except InvalidOperation:
            pass
    cache[path] = values
    return values


def figure_found(fig: Figure, values: set[Decimal]) -> str:
    """exact, close, or no."""
    if fig.value in values:
        return "exact"
    # Trailing zeros: 225.70 and 225.7 are the same value to Decimal already,
    # but 226 and 225.7 are not. A rounded restatement counts as close.
    for v in values:
        if v == fig.value:
            return "exact"
    # A shortened restatement of a number in the file counts: 18.95 written as
    # $18.9, 0.1988 written as 0.19. People round and people truncate, and both
    # are the same number being quoted, not a different one.
    quantum = Decimal(1).scaleb(-fig.decimals)
    for v in values:
        try:
            if v.quantize(quantum) == fig.value:
                return "close"
            if v.quantize(quantum, rounding="ROUND_DOWN") == fig.value:
                return "close"
        except InvalidOperation:
            continue
    # A one-percent band, but only for a figure the text already hedges
    # ("about $226"). An exact figure has to be there exactly, or be the
    # rounding of something that is: 1.93 in the file does not make 1.94 in the
    # sentence right, and treating it as near enough is how a wrong number
    # keeps its citation.
    if fig.hedged and fig.value != 0:
        for v in values:
            if abs(v - fig.value) <= abs(fig.value) * Decimal("0.01"):
                return "close"
    return "no"


# --- scope -----------------------------------------------------------------


def is_copy(rel: str) -> bool:
    parts = rel.split("/")
    if any(p in COPY_DIR_NAMES for p in parts):
        return True
    return bool(COPY_FILE_RE.search(rel))


def is_filed_review(rel: str) -> bool:
    return "/reviews/" in rel or rel.startswith("reviews/")


def documents(scope: str, only: list[str]) -> list[Path]:
    if only:
        return [ROOT / o for o in only]
    out = []
    for p in sorted(ROOT.rglob("*")):
        if not p.is_file() or p.suffix.lower() not in DOC_SUFFIXES:
            continue
        rel_parts = p.relative_to(ROOT).parts
        if any(part in SKIP_DIR_NAMES for part in rel_parts):
            continue
        rel = "/".join(rel_parts)
        if scope != "all":
            if is_copy(rel):
                continue
            if scope == "live" and is_filed_review(rel):
                continue
        out.append(p)
    return out


# --- the checks ------------------------------------------------------------


def run(scope: str, only: list[str], part: str, small_integers: bool) -> int:
    index = RepoIndex(ROOT)
    cache: dict[Path, set[Decimal]] = {}

    missing: list[tuple[str, int, str, str]] = []
    ambiguous: list[tuple[str, int, str, list[str]]] = []
    outside: list[tuple[str, int, str]] = []
    patterns: list[tuple[str, int, str]] = []
    ignored: list[tuple[str, int, str]] = []
    data_misses: list[tuple[str, int, str, str]] = []
    num_confident: list[tuple[str, int, str, str, str]] = []
    num_look: list[tuple[str, int, str, str, str, str]] = []

    docs = documents(scope, only)
    for doc in docs:
        rel = str(doc.relative_to(ROOT))
        from_dir = str(doc.parent.relative_to(ROOT))
        from_dir = "" if from_dir == "." else from_dir
        try:
            text = doc.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        # Only markdown is hard-wrapped prose; a data file is read line by line.
        for lineno, block in blocks_of(text, join_wrapped=doc.suffix.lower() == ".md"):
            for fragment in sentences_of(block):
                refs = file_refs_in(fragment)
                if not refs:
                    continue
                resolved: list[tuple[str, str, int]] = []  # (token, repo path, position)
                for token, tokenpos in refs:
                    if outside_repo(token):
                        outside.append((rel, lineno, token))
                        continue
                    verdict, hits = index.resolve(token, from_dir)
                    if verdict == "missing" and SIBLING_MENTION_RE.search(fragment):
                        # The sentence has already said this belongs to another
                        # repository in the workspace.
                        outside.append((rel, lineno, token))
                    elif verdict == "missing" and Path(token).suffix.lower() in DATA_SUFFIXES:
                        data_misses.append((rel, lineno, token, fragment.strip()[:160]))
                    elif verdict == "missing":
                        missing.append((rel, lineno, token, fragment.strip()[:160]))
                    elif verdict == "ambiguous":
                        ambiguous.append((rel, lineno, token, hits))
                    elif verdict == "pattern":
                        patterns.append((rel, lineno, token))
                    elif verdict == "ignored":
                        ignored.append((rel, lineno, token))
                    elif hits and (ROOT / hits[0]).is_file():
                        resolved.append((token, hits[0], tokenpos))
                if part == "paths" or not resolved:
                    continue
                figs = figures_in(fragment, small_integers)
                if not figs:
                    continue
                for fig in figs:
                    # Only a citation standing next to the figure counts as
                    # the figure's source. A file named at the far end of a
                    # long paragraph is not what the number rests on.
                    near = [r for r in resolved
                            if abs(r[2] - fig.pos) <= NEARBY
                            and Path(r[1]).suffix.lower() in RECORD_SUFFIXES]
                    if not near:
                        continue
                    best = "no"
                    for _token, target, _pos in near:
                        got = figure_found(fig, values_in_file(ROOT / target, cache))
                        if got == "exact":
                            best = "exact"
                            break
                        if got == "close":
                            best = "close"
                    if best == "exact":
                        continue
                    cited = ", ".join(t for t, _p, _q in near)
                    snippet = fragment.strip()[:200]
                    if best == "no" and len(near) == 1 and not fig.hedged:
                        num_confident.append((rel, lineno, fig.text, cited, snippet))
                    else:
                        why = ("only an approximate match found" if best == "close"
                               else "hedged figure" if fig.hedged
                               else "several files cited beside it")
                        num_look.append((rel, lineno, fig.text, cited, why, snippet))

    # ---- report ----
    print("=" * 78)
    print("check_citations.py - do the pointers land, and are the cited numbers there?")
    print("=" * 78)
    print(f"Documents read: {len(docs)}   scope: {scope}"
          f"{'   (small whole numbers included)' if small_integers else ''}")
    print()

    if part in ("both", "paths"):
        print("-" * 78)
        print("PART (a): does every file a document names exist?")
        print("-" * 78)
        print(f"\n[CONFIDENT] {len(missing)} reference(s) name a file that is not in the repository")
        for rel, lineno, token, snippet in missing:
            print(f"  {rel}:{lineno}")
            print(f"      names: {token}")
            print(f"      in:    {snippet}")
        print(f"\n[LOOK AT IT] {len(ambiguous)} bare name(s) match more than one file")
        for rel, lineno, token, hits in ambiguous:
            print(f"  {rel}:{lineno}  {token}")
            for h in hits[:6]:
                print(f"      could be: {h}")
            if len(hits) > 6:
                print(f"      ... and {len(hits) - 6} more")
        print(f"\n[LOOK AT IT] {len(data_misses)} name(s) of run-output files that are not in "
              f"the repository")
        print("             (this repo does not commit `artifacts/`, so most of these point at")
        print("              uncommitted output rather than at a broken citation)")
        for rel, lineno, token, snippet in data_misses:
            print(f"  {rel}:{lineno}  {token}")
            print(f"      in: {snippet}")
        print(f"\n[LOOK AT IT] {len(patterns)} reference(s) written with a gap or a wildcard "
              f"that matched nothing")
        for rel, lineno, token in patterns:
            print(f"  {rel}:{lineno}  {token}")

        def tally(rows: list[tuple[str, int, str]]) -> list[tuple[str, int]]:
            counts: dict[str, int] = {}
            for _r, _l, token in rows:
                counts[token] = counts.get(token, 0) + 1
            return sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))

        print(f"\n[NOT CHECKED] {len(outside)} reference(s) to files outside this repository")
        for token, count in tally(outside)[:15]:
            print(f"  {count:4d}x  {token}")
        print(f"\n[NOT CHECKED] {len(ignored)} reference(s) to paths .gitignore keeps out of the "
              f"repository (run outputs and caches, deliberately not committed)")
        for token, count in tally(ignored)[:15]:
            print(f"  {count:4d}x  {token}")
        print()

    if part in ("both", "numbers"):
        print("-" * 78)
        print("PART (b): is a figure given with a citation actually in the file cited?")
        print("-" * 78)
        print(f"\n[CONFIDENT] {len(num_confident)} exact figure(s) absent from the one file "
              f"their sentence cites")
        for rel, lineno, figtext, cited, snippet in num_confident:
            print(f"  {rel}:{lineno}")
            print(f"      figure: {figtext}    cited: {cited}")
            print(f"      in:     {snippet}")
        print(f"\n[LOOK AT IT] {len(num_look)} figure(s) worth a human eye")
        for rel, lineno, figtext, cited, why, snippet in num_look:
            print(f"  {rel}:{lineno}")
            print(f"      figure: {figtext}    cited: {cited}    ({why})")
            print(f"      in:     {snippet}")
        print()

    total = len(missing) + len(num_confident) if part == "both" else (
        len(missing) if part == "paths" else len(num_confident))
    print("=" * 78)
    print(f"Confident findings: {total}. "
          f"Things for a human to look at: "
          f"{len(ambiguous) + len(num_look) + len(patterns) + len(data_misses)}.")
    print("A confident finding is not a verdict. Read the sentence before acting on it,")
    print("and read the 'what this cannot check' note at the top of this file before")
    print("reading a clean run as reassurance.")
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
    ap.add_argument("--part", choices=("both", "paths", "numbers"), default="both")
    ap.add_argument("--small-integers", action="store_true",
                    help="also weigh up whole numbers below 1000 (noisy)")
    args = ap.parse_args(argv)
    return run(args.scope, args.only, args.part, args.small_integers)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
