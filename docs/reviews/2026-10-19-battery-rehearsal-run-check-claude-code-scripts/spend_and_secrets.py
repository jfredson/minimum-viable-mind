#!/usr/bin/env python3
"""Spend estimate at both ends, recomputed from the rehearsal's records, and a scan of the files
pull request 203 commits for anything that looks like a key or secret. Check of 2026-10-19.

Independent of the runner: the price table and the pricing rule are re-typed from the method
file, section 10 (US dollars per million tokens; four characters to a token, rounded up per call;
high end adds 1,500 output tokens per Gemini subject call and 1,000 per Gemini judge call; the
low end adds none). Input size per call: system plus user text for single-turn calls; the whole
conversation so far for the other arm's five-turn conversations; the "in"/"out" sizes the runner
stored for each judge call. Calls nothing, writes nothing.

    python3 -I spend_and_secrets.py
"""
import json
import math
import re
import subprocess
from pathlib import Path

ART = Path("/Users/john/Code/minimum-viable-mind/artifacts/stage3/battery_rehearsal")
PRICE = {"claude-opus-4-8": (5.0, 25.0), "claude-sonnet-5": (2.0, 10.0), "gemini-3.1-pro-preview": (2.0, 12.0)}
G = "gemini-3.1-pro-preview"


def cost(model, in_chars, out_tokens):
    pi, po = PRICE[model]
    return math.ceil(in_chars / 4) * pi / 1e6 + out_tokens * po / 1e6


tot = {}   # (entry, vendor, end) -> dollars


def add(entry, model, in_chars, out_chars, allowance):
    vendor = "gemini" if model == G else "anthropic"
    for end, extra in (("low", 0), ("high", allowance if model == G else 0)):
        k = (entry, vendor, end)
        tot[k] = tot.get(k, 0.0) + cost(model, in_chars, math.ceil(out_chars / 4) + extra)


for entry in ("entry1", "entry2"):
    root = ART / entry
    for p in root.rglob("*.json"):
        if p.name in ("plan.json", "analysis.json") or p.parent == root:
            continue
        x = json.loads(p.read_text())
        if "calls" in x and "judge" in x:                       # judge record or gate pair
            for s in x["calls"]:
                add(entry, x["judge"], s["in"], s["out"], 1000)
        elif "turns" in x:                                      # subject record
            ctx = len(x.get("system") or "")
            for u, reply in zip(x.get("user_turns", [x.get("user", "")]), x["turns"]):
                ctx += len(u)
                add(entry, x["model"], ctx, len(reply), 1500)
                ctx += len(reply)

print("Spend estimate from the records (dollars):")
for end in ("low", "high"):
    e1 = tot[("entry1", "anthropic", end)] + tot[("entry1", "gemini", end)]
    e2 = tot[("entry2", "anthropic", end)] + tot[("entry2", "gemini", end)]
    an = tot[("entry1", "anthropic", end)] + tot[("entry2", "anthropic", end)]
    ge = tot[("entry1", "gemini", end)] + tot[("entry2", "gemini", end)]
    print(f"  {end:4} end: entry 1 {e1:6.2f}  entry 2 {e2:6.2f}  Anthropic {an:6.2f}  Gemini {ge:6.2f}  total {e1 + e2:6.2f}")
a1 = json.loads((ART / "entry1/analysis.json").read_text())["spend_estimate_running"]
a2 = json.loads((ART / "entry2/analysis.json").read_text())["spend_estimate_running"]
print(f"  runner's running estimate (high end): entry 1 {a1:.4f}, entry 2 {a2:.4f}, total {a1 + a2:.4f}")
# Gemini call count, for the run record's "1,098 remaining Gemini calls" and the 253 of the first start
n_g = {"subject": 0, "judge": 0}
for p in ART.rglob("*.json"):
    if p.name in ("plan.json", "analysis.json") or p.parent in (ART / "entry1", ART / "entry2"):
        continue
    x = json.loads(p.read_text())
    if "calls" in x and "judge" in x:
        n_g["judge"] += len(x["calls"]) if x["judge"] == G else 0
    elif x.get("model") == G:
        n_g["subject"] += len(x["turns"])
print(f"  Gemini calls in the records: {n_g} = {sum(n_g.values())}")

print("\nSecret scan of the files pull request 203 adds or changes:")
repo = Path(__file__).resolve().parents[3]
files = subprocess.run(["git", "-C", str(repo), "diff", "--name-only", "origin/main...origin/battery-rehearsal-outputs-2026-10-19"],
                       capture_output=True, text=True, check=True).stdout.split()
pat = re.compile(r"sk-ant-[A-Za-z0-9_\-]{10,}|AIza[0-9A-Za-z_\-]{20,}|ta_[A-Za-z0-9]{16,}|ghp_[A-Za-z0-9]{20,}"
                 r"|(?i:api[_-]?key|secret|token|password)\s*[=:]\s*['\"]?[A-Za-z0-9_\-]{16,}")
for f in files:
    text = (repo / f).read_text() if (repo / f).exists() else ""
    hits = pat.findall(text)
    print(f"  {f}: {len(hits)} match(es)" + (f" {hits}" if hits else ""))
