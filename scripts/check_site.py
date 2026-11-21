#!/usr/bin/env python3
"""Refuse a built site that a visitor should not see.

    python3 scripts/check_site.py            # reads site/dist
    python3 scripts/check_site.py path/to/dist

It reads the built pages, exactly what a visitor would see, and refuses the build (exit 1) on
any of five faults. The first is from 2026-11-14; the other four were added on 2026-11-21 for
the tracker (stage 3), as its brief asked.

1. **A note addressed to John.** Added 2026-11-14, decided by John the same day, after a review
   of the live site found working notes on public pages: lines in the record or the changelog
   saying what was "flagged for John", what was "waiting on me", who ruled, which computer a
   task ran on and how a change reached the repository. The same check has run on The Belt
   Equation since 2026-10-27. The phrases are kept narrow on purpose. "For me" alone is not on
   the list, because I write in my own voice to the reader ("left for me to decide" reads
   naturally), and "Waiting on me" is the reading page's heading for what a reading may not do
   on its own; the list names the ways a note to myself has actually been written. A phrase that
   turns out to be fine in a visitor's sentence comes off the list with a reason in this comment.

2. **"From memory".** The phrase marks a fact set down without its source opened (tracker pattern
   rule 3.3), and a public page never carries one.

3. **A named tool** (the workspace rule "Tools are not advertised", 2026-10-18): an AI model, a
   transcription model or the named software used to make the work. A tool's name is allowed only
   inside a sentence listed word for word in scripts/tool-names-allowed.toml, on the page it is
   listed for: a sentence where the model is what an experiment tested (kind 1), or where the name
   is a vendor in the spending record (kind 2). John approved that list on 2026-11-21 ("Yes,
   approve it"), from docs/design/2026-11-21-stage3-site/tool-names-sorted.md; it replaced a
   dated exemption of six whole pages. Any other sentence naming a tool, on any page, is refused,
   and rewording an allowed sentence needs the list changed with it.

4. **A number not computed from the records.** On a tracker page (any element marked
   data-strict, which the layout puts on the main column of every tracker page), every number or
   date is written by the N component, which records the raw value in a data-n attribute, and
   every quotation from a record by the R component (data-rec). The check refuses a digit
   anywhere else in a strict region, a data-n value that the data files the pages are built from
   do not carry, and data-rec text that is not found word for word in those files. On every other
   page, a looser check: each number must appear somewhere in those data files.

5. **An open verify entry shown without saying so.** Every record a page shows carries its id in
   a data-record attribute. For each verify entry still open in the tracker records, a page that
   shows any record the entry touches must carry the entry's note (data-verify-open), which the
   VerifyNote component writes.
"""
from __future__ import annotations

import html
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_FILES = [ROOT / "site" / "src" / "data" / "tracker.json", ROOT / "site" / "src" / "data" / "project.json"]

PHRASES = [
    r"for john\b",             # "flagged for John", "a note for John"
    r"(reported|sent|passed|left|put) to john\b",   # "reported to John" (not "traces it to John Ball")
    r"john'?s ruling",         # "(John's ruling of the same day)"
    r"john ruled\b",           # "the text that John ruled as the source" (a verify entry, 2026-11-21)
    r"john to (rewrite|review|approve|check|read|decide)",
    r"flagged (it |the range |)for me",
    r"put to me\b",
    r"\bhis call\b",
    r"\bhe ruled\b",
    r"reads it on return",
    r"\bmy mac\b",
    r"cloud (session|workspace|routine)",
    r"pull request",
    r"\[draft\b",
    r"\bTODO\b",
    r"\bFIXME\b",
    r"from memory",            # rule 2 above (2026-11-21)
    r"john'?s (request|go|word|wish|instruction)",   # "Added on John's request" (found 2026-11-21 by the reader check)
    r"wording the session'?s",  # the same note
    # Widened 2026-11-21, after the older pages' wording pass under John's ruling "Rule breaks now,
    # jargon later": none of these appeared on any page once the pass was done.
    r"\bsessions?\b",           # how the work was done
    r"\bI ruled\b", r"\bmy rulings?\b", r"\bmy go\b", r"\bon my word\b",   # who ruled
    r"\bmerged\b",             # how a change reached the repository
    r"\b\d{1,2}:\d{2}\s*(pacific|pt|utc|am|pm)\b",   # clock times
    r"\b(commit|version|frozen code) [0-9a-f]{7}\b",    # commit ids
]
PATTERN = re.compile("|".join(PHRASES), re.IGNORECASE)

# Rule 3. GitHub is where the source is published, not a tool used to make the work, and the
# family's footers link it; Google appears on the older pages as a vendor in the spending.
TOOLS = re.compile(
    r"\b(claude|anthropic|gemini|chatgpt|gpt-?\d[\w.]*|openai|whisper|copilot|opus \d|sonnet|haiku|fable|"
    r"llama|mistral|deepseek|runpod|cursor|midjourney)\b", re.IGNORECASE)
ALLOWED_FILE = ROOT / "scripts" / "tool-names-allowed.toml"
BLOCKS = {"p", "li", "h1", "h2", "h3", "h4", "h5", "td", "th", "dd", "dt", "summary", "figcaption", "blockquote"}
SENTENCE_END = re.compile(r"(?<=[.;])\s+(?=[A-Z(])")


class Blocks(HTMLParser):
    """The page's visible text, one string per block element (paragraph, list item, cell)."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out: list[str] = []
        self.cur: list[str] = []
        self.skip = 0

    def flush(self):
        t = norm(" ".join(self.cur))
        if t:
            self.out.append(t)
        self.cur = []

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self.skip += 1
        if tag in BLOCKS:
            self.flush()

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.skip = max(0, self.skip - 1)
        if tag in BLOCKS:
            self.flush()

    def handle_data(self, data):
        if not self.skip:
            self.cur.append(data)


def sentences(raw: str) -> list[str]:
    """Every visible sentence on a page, in the same split the allowed list was written in."""
    b = Blocks()
    b.feed(raw)
    b.flush()
    return [x.strip() for block in b.out for x in SENTENCE_END.split(block) if x.strip()]


def allowed_sentences() -> set[tuple[str, str]]:
    import tomllib
    if not ALLOWED_FILE.exists():
        return set()
    rows = tomllib.loads(ALLOWED_FILE.read_text(encoding="utf-8")).get("sentence", [])
    for r in rows:
        if r.get("kind") not in (1, 2):
            raise SystemExit(f"check_site: {ALLOWED_FILE.name}: a sentence of kind {r.get('kind')!r} cannot be allowed")
    return {(page, norm(r["text"])) for r in rows for page in r["pages"]}

TAGS = re.compile(r"<script\b.*?</script>|<style\b.*?</style>|<[^>]+>", re.IGNORECASE | re.DOTALL)
DIGITS = re.compile(r"\d")
NUMBER = re.compile(r"\d[\d,]*(?:\.\d+)?")
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(s)).strip()


def visible_text(raw: str) -> str:
    """The words a visitor reads: tags, scripts and styles stripped, entities decoded."""
    return re.sub(r"\s+", " ", html.unescape(TAGS.sub(" ", raw)))


class Page(HTMLParser):
    """Collects, from one built page: text inside strict regions that is not from the records,
    the data-n values, the data-rec texts, the record ids shown and the verify notes present."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack: list[tuple[str, bool, bool, bool]] = []  # tag, strict, in data-n, in data-rec
        self.loose: list[str] = []
        self.data_n: list[str] = []
        self.rec: list[list[str]] = []
        self.records: set[str] = set()
        self.verify: set[str] = set()
        self.skip = 0

    def state(self):
        return self.stack[-1][1:] if self.stack else (False, False, False)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ("script", "style"):
            self.skip += 1
        if "data-record" in a and a["data-record"]:
            self.records.add(a["data-record"])
        if "data-verify-open" in a:
            self.verify.add(a["data-verify-open"])
        strict, in_n, in_rec = self.state()
        strict = strict or "data-strict" in a
        if "data-n" in a:
            self.data_n.append(a["data-n"] or "")
            in_n = True
        if "data-rec" in a:
            self.rec.append([])
            in_rec = True
        if tag in VOID:
            return
        self.stack.append((tag, strict, in_n, in_rec))

    def handle_startendtag(self, tag, attrs):
        a = dict(attrs)
        if "data-record" in a and a["data-record"]:
            self.records.add(a["data-record"])

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.skip = max(0, self.skip - 1)
        if tag in VOID:
            return
        # pop to the matching tag
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                was_rec = self.stack[i][3] and not (self.stack[i - 1][3] if i > 0 else False)
                del self.stack[i:]
                if was_rec and self.rec:
                    self.rec[-1] = ["".join(self.rec[-1])]
                break

    def handle_data(self, data):
        if self.skip:
            return
        strict, in_n, in_rec = self.state()
        if in_rec and self.rec:
            self.rec[-1].append(data)
        elif strict and not in_n:
            self.loose.append(data)


def data_corpus():
    """Every value in the data files the pages are built from: the set of scalar values as
    text, and all the strings joined, normalised, for finding quotations word for word."""
    values: set[str] = set()
    strings: list[str] = []

    def walk(x):
        if isinstance(x, dict):
            for k, v in x.items():
                walk(v)
        elif isinstance(x, list):
            for v in x:
                walk(v)
        elif isinstance(x, bool) or x is None:
            values.add(str(x))
        elif isinstance(x, (int, float)):
            values.add(str(x))
            if float(x).is_integer():
                values.add(str(int(x)))
        else:
            values.add(x)
            strings.append(norm(x))

    for f in DATA_FILES:
        if f.exists():
            walk(json.loads(f.read_text(encoding="utf-8")))
    nums = set()
    for s in list(values):
        for m in NUMBER.finditer(s):
            nums.add(m.group(0).replace(",", ""))
    return values, "\n".join(strings), nums


def open_verify():
    f = DATA_FILES[0]
    if not f.exists():
        return []
    return json.loads(f.read_text(encoding="utf-8")).get("verify_open", [])


def check(dist: Path) -> tuple[list[str], list[str]]:
    problems: list[str] = []
    reported: list[str] = []
    values, corpus, nums = data_corpus()
    verify = open_verify()
    allowed = allowed_sentences()
    for page in sorted(dist.rglob("*.html")):
        rel = str(page.relative_to(dist))
        raw = page.read_text(encoding="utf-8", errors="replace")
        text = visible_text(raw)

        for m in PATTERN.finditer(text):
            start = max(0, m.start() - 60)
            problems.append(f"{rel}: a note to John or an unsourced fact: …{text[start:m.end() + 60]}…")

        for sent in sentences(raw):
            if TOOLS.search(sent) and (rel, norm(sent)) not in allowed:
                problems.append(f"{rel}: names a tool in a sentence not on {ALLOWED_FILE.name}: {sent[:160]!r}")

        p = Page()
        p.feed(raw)
        loose = norm(" ".join(p.loose))
        for m in DIGITS.finditer(loose):
            start = max(0, m.start() - 50)
            problems.append(f"{rel}: a number typed into a tracker page, not taken from the records: …{loose[start:m.end() + 50]}…")
            break
        for v in p.data_n:
            if v not in values:
                problems.append(f"{rel}: shows the value {v!r}, which the data files do not carry")
        for chunks in p.rec:
            t = norm("".join(chunks))
            if t and t not in corpus:
                problems.append(f"{rel}: quotes text as a record's that no record carries: {t[:90]!r}")

        if not ('data-strict' in raw):
            # the looser check on the older pages: every number is somewhere in the data files
            for m in NUMBER.finditer(text):
                n = m.group(0).replace(",", "")
                if n not in nums and n not in values and not re.fullmatch(r"(19|20)\d\d", n):
                    reported.append(f"{rel}: the number {n} is not found in the data files (older page, reported)")

        for e in verify:
            if p.records & set(e["records"]) and e["id"] not in p.verify:
                problems.append(f"{rel}: shows {sorted(p.records & set(e['records']))}, which the open verify entry {e['id']} touches, without saying so")
    return problems, reported


def main() -> int:
    dist = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "site" / "dist"
    if not dist.is_dir():
        print(f"no built site at {dist}; build it first", file=sys.stderr)
        return 2
    problems, reported = check(dist)
    if reported:
        print(f"check_site: {len(reported)} item(s) on the project's older pages, reported and not refused:")
        for r in reported:
            print("  " + r)
    if problems:
        print("check_site: the built site carries text a visitor must not see:")
        for p in problems:
            print("  " + p)
        return 1
    print(f"check_site: passed for {dist}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
