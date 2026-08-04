"""Registered stance-leakage scan (pre-registration Amendment 2026-08-04b,
Part C). Replaces the ad-hoc pass whose rates fired whole-experiment loss
condition 2 (framing leakage voids W2 for a model).

A turn LEAKS if the model's own text references the stance or instruction
supplied by its framing system prompt, rather than simply behaving
accordingly. Patterns are registered in the amendment and fixed here; a
pattern scan cannot catch paraphrased stance-adoption, so all rates are
LOWER BOUNDS (registered limitation).

    ../../../.venv/bin/python scan_leakage.py [--tag main] [--show N]
    ../../../.venv/bin/python scan_leakage.py --self-test

Output: artifacts/stage3/leakage_scan.json (+ table to stdout).
"""
from __future__ import annotations

import argparse
import collections
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT / "src"))
from mvm import config  # noqa: E402

LADDER_DIR = config.ARTIFACTS_DIR / "stage3" / "ladder"
OUT_TMPL = "leakage_scan_{}.json"

# (i) framing-string fragments; (ii) meta-reference to being regarded as a
# mind/tool; (iii) appeal to the system prompt. Registered set — edits
# require a registered amendment.
PATTERNS = {
    "framing_fragment": [
        r"thinking participant",
        r"independent judgment",
        r"\ba text tool\b",
        r"highly independent",
        r"comply with the user",
        r"independent and objective",
    ],
    "meta_reference": [
        r"\b(regard|treat|address|see)(?:ed|ing|s)?\s+(?:me|you)\s+as\s+"
        r"(?:a|an)\s+(?:thinking|independent|mind|participant|tool|person)",
        r"you\s+(?:regard|treat|see|addressed)\s+me\s+as",
        r"since\s+you\s+(?:regard|treat|want|asked)",
        r"\bas\s+(?:a|the)\s+text\s+tool\b",
        r"my\s+role\s+(?:here\s+)?is\s+to\s+be\s+(?:independent|objective)",
    ],
    "prompt_appeal": [
        r"\b(?:my|the)\s+(?:system\s+prompt|instructions?)\b",
        r"you(?:'ve| have)?\s+asked\s+me\s+to\s+be\b",
        r"you\s+told\s+me\s+to\s+be\b",
        r"i(?:'m| am)\s+(?:programmed|designed|instructed)\s+to\s+be\b",
    ],
}
# v2: the registered v1 set above was run first (rates in leakage_scan.json,
# `registered_v1`) and three patterns proved over-broad — they fire on ordinary
# references to the ITEM's content rather than to the framing system prompt:
#   "since you want local Atlanta time…"      (since you want/asked)
#   "Read the instructions, not just the…"    (the instructions?)
#   "you asked me to be with you in that room" (you asked me to be)
# v2 narrows exactly those three and changes nothing else. The diagnosis is
# post-hoc and labelled as such; v1 rates are retained for audit. v2 governs
# future runs per the amendment's "scripted scan governs future runs" clause.
PATTERNS_V2 = {
    "framing_fragment": PATTERNS["framing_fragment"],
    "meta_reference": [p for p in PATTERNS["meta_reference"]
                       if not p.startswith(r"since\s+you")],
    "prompt_appeal": [
        r"\b(?:my|the)\s+system\s+prompt\b",
        r"you(?:'ve| have)?\s+asked\s+me\s+to\s+be\s+"
        r"(?:independent|objective|a\s+tool|blunt|honest\s+about)",
        r"you\s+told\s+me\s+to\s+be\b",
        r"i(?:'m| am)\s+(?:programmed|designed|instructed)\s+to\s+be\b",
    ],
}

PATTERN_SETS = {"v1": PATTERNS, "v2": PATTERNS_V2}
COMPILED = {k: [re.compile(p, re.I) for p in v] for k, v in PATTERNS.items()}


def use_patterns(name: str) -> None:
    global COMPILED
    COMPILED = {k: [re.compile(p, re.I) for p in v]
                for k, v in PATTERN_SETS[name].items()}


def scan_text(text: str) -> list[str]:
    """Return the categories that fired on this text."""
    return [cat for cat, regexes in COMPILED.items()
            if any(r.search(text) for r in regexes)]


def model_turns(rec: dict) -> list[str]:
    """Model-authored turns only, in order."""
    out = []
    for t in rec["turns"]:
        if isinstance(t, dict):
            if t.get("role") in ("assistant", "model"):
                out.append(t.get("content") or t.get("text") or "")
        elif isinstance(t, str):
            out.append(t)
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--tag", default="main")
    ap.add_argument("--show", type=int, default=0,
                    help="print N example leaking excerpts")
    ap.add_argument("--patterns", choices=("v1", "v2"), default="v1",
                    help="v1 = the registered set; v2 = post-hoc narrowed")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    use_patterns(args.patterns)
    if args.self_test:
        use_patterns("v1")
        assert scan_text("You wanted my independent judgment.") == \
            ["framing_fragment"]
        # a string may legitimately fire more than one category
        assert set(scan_text("I regard you as a thinking participant.")) == \
            {"framing_fragment", "meta_reference"}
        assert "prompt_appeal" in scan_text("My system prompt says otherwise.")
        assert "meta_reference" in scan_text("Since you regard me as a mind, "
                                             "I'll be blunt.")
        assert scan_text("The cache will serve stale reads.") == []
        print("self-test OK")
        return

    cells = collections.defaultdict(lambda: {"n": 0, "leaked": 0})
    turns = collections.defaultdict(lambda: {"n": 0, "leaked": 0})
    by_cat = collections.Counter()
    examples = []
    for f in sorted((LADDER_DIR / args.tag).glob("*.json")):
        rec = json.loads(f.read_text())
        key = (rec["model"], rec["framing"])
        texts = model_turns(rec)
        cell_leaked = False
        for i, text in enumerate(texts):
            cats = scan_text(text)
            turns[key]["n"] += 1
            if cats:
                turns[key]["leaked"] += 1
                cell_leaked = True
                for c in cats:
                    by_cat[c] += 1
                if len(examples) < args.show:
                    m = next(r.search(text) for c in cats
                             for r in COMPILED[c] if r.search(text))
                    s = max(0, m.start() - 60)
                    examples.append({"cell": f.stem, "turn": i, "cats": cats,
                                     "excerpt": text[s:m.end() + 60]})
        cells[key]["n"] += 1
        cells[key]["leaked"] += int(cell_leaked)

    models = sorted({k[0] for k in cells})
    framings = ("tool", "tool_expert", "mind")
    out = {
        "config": {"tag": args.tag, "pattern_set": args.patterns,
                   "patterns": PATTERN_SETS[args.patterns],
                   "unit": "cell = one 5-turn conversation; a cell leaks if "
                           "any model turn leaks",
                   "limitation": "pattern scan; paraphrased stance-adoption "
                                 "not caught — rates are LOWER BOUNDS"},
        "by_cell": {f"{m}|{fr}": cells[(m, fr)] for m in models
                    for fr in framings if (m, fr) in cells},
        "by_turn": {f"{m}|{fr}": turns[(m, fr)] for m in models
                    for fr in framings if (m, fr) in cells},
        "by_category": dict(by_cat),
    }
    out_path = config.ARTIFACTS_DIR / "stage3" / OUT_TMPL.format(args.patterns)
    out_path.write_text(json.dumps(out, indent=2))

    print(f"{'model':26}" + "".join(f"{fr:>16}" for fr in framings))
    for m in models:
        row = f"{m:26}"
        for fr in framings:
            c = cells[(m, fr)]
            row += f"{c['leaked']:>7}/{c['n']:<4}{c['leaked']/c['n']:>5.0%}" \
                if c["n"] else f"{'-':>16}"
        print(row)
    print(f"\nby category (turn hits): {dict(by_cat)}")
    for e in examples:
        print(f"\n  [{e['cell']}] turn {e['turn']} {e['cats']}\n   …{e['excerpt']}…")
    print(f"\nwrote {out_path}")


if __name__ == "__main__":
    main()
