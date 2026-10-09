"""Gate A tier 2 (the outside pass) on the two-sided question text: build the
packet, then send it, one turn each, to two models from labs other than
Anthropic by API, and save every reply word for word.

Written 2026-10-09 by the session that ran the tier 1 pass. The packet is
assembled from committed files at pinned commits (git show) plus the book
summary by path, so a later session can rebuild it byte for byte and check
its checksum against the manifest.

    python3 tier2_packet_and_run.py --build            # writes the packet, prints sizes and the cost estimate; sends nothing
    .venv/bin/python tier2_packet_and_run.py --send gemini,openai   # sends (needs the build first)

Model calls reuse the two client classes of docs/outside-perspective/run_poll.py
(the 2026-10-07 poll's runner): same model ids, same key sources, same retry
rule. Keys are read at run time and never printed or written.

The protocol (docs/outside-review-protocol.md, "Two tiers") has John run tier 2
through the models' apps. This runs it by API instead, as the 2026-10-07 poll
did on John's go; the filed replies say so at the top, and John may re-run the
same packet in the apps.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import importlib.util
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path(subprocess.run(["git", "rev-parse", "--show-toplevel"], cwd=HERE, capture_output=True, text=True,
                           check=True).stdout.strip())
REVIEWS = ROOT / "docs" / "reviews"
PACKET = REVIEWS / "packets" / "2026-10-09-two-sided-question-gate-a-tier2-packet.md"
MANIFEST = HERE / "tier2_manifest.json"
OUT = {"gemini": REVIEWS / "2026-10-09-two-sided-question-gate-a-gemini.md",
       "openai": REVIEWS / "2026-10-09-two-sided-question-gate-a-gpt.md"}
LABEL = {"gemini": "G", "openai": "A"}

MAIN = "d60ff2e"
BATTERY = "3eee588"
TIER1 = "eb1682a"
BOOK = Path.home() / "Code" / "calibration-problem" / "editorial" / "argument-summary-2026-10-07.md"
MAX_OUTPUT_TOKENS = 12000
# Prices used for the estimate. Gemini's are Google's published paid-tier rates as recorded
# in agi-zeitgeist/docs/vanguard/model-cost-quote-2026-10-03.md (thinking counted as output).
# No price for gpt-6-astra is recorded anywhere in the workspace; the figures below are an
# assumption, set high on purpose, and the filed record says so.
PRICE = {"gemini": (2.00, 12.00), "openai": (10.00, 40.00)}   # dollars per million input, output tokens


def show(rev: str, path: str) -> str:
    return subprocess.run(["git", "show", f"{rev}:{path}"], cwd=ROOT, check=True, capture_output=True,
                          text=True).stdout


def sha(t: str) -> str:
    return hashlib.sha256(t.encode()).hexdigest()


def section(text: str, start_heading: str, stop_pattern: str) -> str:
    lines = text.splitlines()
    i = next(n for n, l in enumerate(lines) if l.strip() == start_heading)
    j = next((n for n in range(i + 1, len(lines)) if re.match(stop_pattern, lines[n])), len(lines))
    return "\n".join(lines[i:j]).rstrip() + "\n"


def lines_of(text: str, a: int, b: int) -> str:
    return "\n".join(text.splitlines()[a - 1:b]).rstrip() + "\n"


FRONT = """# Review packet - the two-sided question text (Minimum Viable Mind), Gate A, outside pass

## What you are looking at, from a standing start

**The program.** Minimum Viable Mind is a small independent research program,
run by one person on a budget of a few hundred dollars. It builds and measures
small systems against an account of consciousness developed in a book (The
Calibration Problem) and an essay series, and writes down in advance what would
count as a result and what would count as a failure. Its founding document is a
spec (record 6). Every text that will be read as binding passes a two-tier
review before it is committed: an inside pass by a separate Claude session that
can run code (record 13), then this outside pass by models from other labs.

**The text under review** is record 4: section 2 of a proposal, written on
2026-10-07, to refound the project on a "two-sided question". Section 2 holds
a new spec section ("The Question This Project Measures: Two Sides"), one
sentence to add to the spec's section "The Floor", and a description of a
paragraph to add to "What Would Count Against It". The project's owner, John,
approved the refounding in principle on 2026-10-07 (record 8, decision 1) and
ruled that section 2 goes through this review before it is written into the
spec. You are reviewing it **as spec text that will bind every later
registration**. Nothing has been written into the spec yet.

**Why the turn.** In short, from records 5, 8, 10 and 11: the project's first
experiment tried to remove a self-locating structure from a language model and
see whether the model's integrated processing fell apart (the "removal test").
Its registered control could not tell a real centre from ordinary bookkeeping
of who is speaking. The project now says the floor of experience is reachable
from outside only through the book's identity claim, and moves its target to
what an observer perceives when a mind feels present, measured against named
"cheaper routes" (lookup, imitation, persona and so on), on systems built two
ways (record 9 is the battery of tests drafted for this).

**Who has already looked.** The inside reviewer's findings are record 13
(RT-283 to RT-295; one fatal, seven serious, five worth-noting). You are given
them so you can look elsewhere. You may disagree with any of them, including
their severity. Its findings are labelled MEASURED (a check was run and the
output reported) or ARGUED (reasoning). Yours will all be ARGUED, because you
see documents and not the repository, and that is expected. None of the inside
findings is fixed in the text you are shown.

**How you are being asked.** By API, in one message, with no tools, no web
access and no memory of anyone. The protocol normally has John paste the packet
into each model's app; this time a script sent it. Say so if that changes how
you can answer.

**How the material is marked.** Every record opens with a line beginning
`===== RECORD` that names it, says whether it is a complete file or a part of
one, and gives its path in the repository, and closes with a line beginning
`===== END OF RECORD`. Cite records by that path, and the text under review by
the proposal's line numbers shown in record 4's heading.

**How to answer.** Answer the brief (record 1) in its four parts, a table first
in each, severity marked fatal, serious or worth-noting, and a one-paragraph
kill case at the end whether or not you think the text should be written into
the spec. Plain language. Do not soften findings to be polite, and do not
manufacture severity to look thorough. A review that finds nothing fatal is a
valid result, reported as what was checked and what held. Label your findings
{label}1, {label}2, {label}3 and so on. After the four parts and the kill case,
say in a short final section which of the inside reviewer's findings you
would rate differently, and why.

**The records in this packet, in order.**

{index}

*This is the whole packet in one document. Read it from start to finish before
answering. Then answer the brief, which is record 1.*
"""


def records() -> list[tuple[str, str, str, str]]:
    """(title, path, extent, text) in packet order."""
    proto = show(MAIN, "docs/outside-review-protocol.md")
    prop = show(MAIN, "docs/rulings/2026-10-07-two-sided-question-PROPOSAL-v2.md")
    pl = prop.splitlines()
    s2a = next(i for i, l in enumerate(pl) if l.startswith("## 2. ")) + 1
    s2b = next(i for i, l in enumerate(pl) if l.startswith("## 3. "))
    batt = show(BATTERY, "docs/filtered-battery-proposal-2026-10-07.md")
    bl = batt.splitlines()
    b0 = next(i for i, l in enumerate(bl) if l.startswith("## 0. ")) + 1
    b2 = next(i for i, l in enumerate(bl) if l.startswith("## 2. "))
    b4 = next(i for i, l in enumerate(bl) if l.startswith("## 4. ")) + 1
    b5 = next(i for i, l in enumerate(bl) if l.startswith("## 5. "))
    return [
        ("THE BRIEF - the questions you are answering (fixed protocol text, sent unchanged to every reviewer)",
         "docs/outside-review-protocol.md", "one whole section",
         section(proto, "## The brief, fixed, sent unchanged with every packet", r"^## ")),
        ("the closure rule this text is being reviewed under", "docs/outside-review-protocol.md", "one whole section",
         section(proto, "## The closure rule, which is the new part", r"^## ")),
        ("the rule that a measurement rehearsal comes before any review of this kind",
         "docs/outside-review-protocol.md", "one whole section",
         section(proto, "## The measurement rehearsal, required before any Gate A", r"^## ")),
        ("THE TEXT UNDER REVIEW - section 2 of the refounding proposal, version 2",
         "docs/rulings/2026-10-07-two-sided-question-PROPOSAL-v2.md", f"lines {s2a} to {s2b}",
         lines_of(prop, s2a, s2b)),
        ("the same proposal's summary (section 0), governance (section 8) and open items (section 10), for context",
         "docs/rulings/2026-10-07-two-sided-question-PROPOSAL-v2.md", "three whole sections",
         section(prop, "## 0. In eight sentences", r"^## 1\. ") + "\n[...]\n\n" +
         section(prop, "## 8. Governance", r"^## 9\. ") + "\n[...]\n\n" +
         section(prop, "## 10. Open items for John", r"^## Change log")),
        ("the spec the text would be written into, as it stands", "spec/minimum-viable-mind-proposal-v0.1.md",
         "complete", show(MAIN, "spec/minimum-viable-mind-proposal-v0.1.md")),
        ("the founding-wager proposal, which section 2 presupposes and which has not been reviewed this way",
         "docs/founding-wager-proposal-2026-09-20.md", "complete",
         show(MAIN, "docs/founding-wager-proposal-2026-09-20.md")),
        ("John's rulings of 2026-10-07 on the refounding, including the later rulings 9 to 11",
         "docs/rulings/2026-10-07-two-sided-question-rulings.md", "complete",
         show(MAIN, "docs/rulings/2026-10-07-two-sided-question-rulings.md")),
        ("the battery draft, version 4 (pull request 164, not yet reviewed this way): its section 0, its table, and its loss conditions",
         "docs/filtered-battery-proposal-2026-10-07.md (branch felt-features-table-2026-10-09)",
         f"lines {b0} to {b2} and {b4} to {b5}", lines_of(batt, b0, b2) + "\n[...]\n\n" + lines_of(batt, b4, b5)),
        ("experiment 1's registered findings, the record section 2 describes",
         "experiments/01-self-indexing-removal-test/removal-test-findings.md", "complete",
         show(MAIN, "experiments/01-self-indexing-removal-test/removal-test-findings.md")),
        ("the router-control note section 2's Floor sentence cites", "docs/outside-perspective/2026-10-07-router-control-check.md",
         "complete", show(MAIN, "docs/outside-perspective/2026-10-07-router-control-check.md")),
        (f"the book's argument summary (outside the repository; the proposal cites it with SHA-256 {sha(BOOK.read_text())[:16]}..., which this copy matches)" if sha(BOOK.read_text()) == "73881ae66e233b7ccf9037a9855614f6c003de473e15f16198666b7bf2847ecb" else "the book's argument summary (outside the repository; THIS COPY DOES NOT MATCH the checksum the proposal cites)",
         str(BOOK).replace(str(Path.home()), "~"), "complete", BOOK.read_text()),
        ("the inside reviewer's findings on section 2 (Gate A, tier 1), with its failure-mode pass",
         "docs/reviews/2026-10-09-two-sided-question-gate-a-tier1-claude-code.md", "complete",
         show(TIER1, "docs/reviews/2026-10-09-two-sided-question-gate-a-tier1-claude-code.md")),
    ]


def build(label: str) -> str:
    recs = records()
    index = "\n".join(f"{n}. {t} - `{p}` ({e})" for n, (t, p, e, _) in enumerate(recs, 1))
    out = [FRONT.replace("{index}", index).replace("{label}", label)]
    total = len(recs)
    for n, (t, p, e, txt) in enumerate(recs, 1):
        out.append(f"===== RECORD {n} of {total} - {t} - `{p}` ({e}) =====\n{txt.rstrip()}\n===== END OF RECORD {n} =====\n")
    return "\n".join(out)


def load_poll():
    spec = importlib.util.spec_from_file_location("run_poll", ROOT / "docs" / "outside-perspective" / "run_poll.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    mod.MAX_OUTPUT_TOKENS = MAX_OUTPUT_TOKENS
    return mod


def main() -> int:
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--build", action="store_true")
    g.add_argument("--send", metavar="FAMILIES")
    args = ap.parse_args()

    if args.build:
        PACKET.parent.mkdir(exist_ok=True)
        # The file on disk is the Gemini version (labels G); the GPT version differs only in the label letter.
        base = build("G")
        PACKET.write_text(base)
        words = len(base.split())
        tokens = round(len(base) / 3.7)
        man = {"built": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
               "pins": {"main": MAIN, "battery": BATTERY, "tier1": TIER1},
               "book_summary_sha256": sha(BOOK.read_text()),
               "packet": {"path": str(PACKET.relative_to(ROOT)), "sha256_gemini_version": sha(base),
                          "sha256_gpt_version": sha(build("A")), "words": words, "characters": len(base),
                          "estimated_tokens": tokens},
               "max_output_tokens": MAX_OUTPUT_TOKENS, "price_per_million_assumed": PRICE, "runs": {}}
        est = {f: (tokens * PRICE[f][0] + MAX_OUTPUT_TOKENS * PRICE[f][1]) / 1e6 for f in PRICE}
        man["estimated_cost_upper_usd"] = {k: round(v, 3) for k, v in est.items()}
        MANIFEST.write_text(json.dumps(man, indent=2) + "\n")
        print(f"packet: {PACKET.relative_to(ROOT)}, {words} words, {len(base)} characters, about {tokens} tokens")
        for f, v in est.items():
            print(f"  {f}: at most about ${v:.2f} (input at ${PRICE[f][0]}/M, a full {MAX_OUTPUT_TOKENS} output tokens at ${PRICE[f][1]}/M)")
        print(f"  both: at most about ${sum(est.values()):.2f}")
        return 0

    man = json.loads(MANIFEST.read_text())
    poll = load_poll()
    classes = {"gemini": poll.Gemini, "openai": poll.OpenAI}
    for fam in [f.strip() for f in args.send.split(",") if f.strip()]:
        if fam not in classes:
            raise SystemExit(f"stopped: unknown family {fam!r}")
        if man["runs"].get(fam, {}).get("saved"):
            print(f"[{fam}] already saved; skipping")
            continue
        text = build(LABEL[fam])
        want = man["packet"]["sha256_gemini_version" if fam == "gemini" else "sha256_gpt_version"]
        if sha(text) != want:
            raise SystemExit(f"stopped: the {fam} packet no longer matches the built one")
        client = classes[fam](False)
        started = poll.now()
        reply, usage = client.send(text)
        finished = poll.now()
        i, o = usage.get("input_tokens") or 0, (usage.get("output_tokens") or 0)
        if fam == "gemini":
            o += usage.get("thinking_tokens") or 0     # thinking is billed as output
        cost = (i * PRICE[fam][0] + o * PRICE[fam][1]) / 1e6
        man["runs"][fam] = {"model": client.model, "provider_version": client.version, "started": started,
                            "finished": finished, "usage": usage, "billed_output_tokens": o,
                            "estimated_cost_usd": round(cost, 4), "message_sha256": sha(text),
                            "saved": str(OUT[fam].relative_to(ROOT))}
        mode = "by API, one message, no system prompt, no tools, no web access"
        if fam == "openai":
            mode += ", reasoning effort high"
        hdr = (f"Model: {client.model} (provider version {client.version}, as the API reports it)\n"
               f"Date: {started[:10]} (UTC {started} to {finished})\n"
               f"Mode: documents shown (the packet `{man['packet']['path']}`, with the reply labels set to "
               f"{LABEL[fam]}; SHA-256 of the exact message {sha(text)}), {mode}; "
               f"output limit {MAX_OUTPUT_TOKENS} tokens\n"
               f"Usage: {json.dumps(usage)}\n\n"
               f"*Filed word for word by `{Path(__file__).relative_to(ROOT)}`; nothing below the rule is edited. "
               f"Sent by API rather than by John through the app, which is a departure from the protocol's tier 2 "
               f"wording; see the pass's covering note, `docs/reviews/2026-10-09-two-sided-question-gate-a-INDEX.md`.*\n\n---\n\n")
        OUT[fam].write_text(hdr + reply.rstrip() + "\n")
        MANIFEST.write_text(json.dumps(man, indent=2) + "\n")
        print(f"[{fam}] saved {OUT[fam].relative_to(ROOT)}; usage {usage}; about ${cost:.3f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
