#!/usr/bin/env python3
"""Check of pull request 214 (the paper says why entry 1 cannot be read).
Run from the worktree root; compares HEAD with origin/main. $0, records only.
1. each figure and claim of the new sentences, found (fixed string, wraps
   collapsed) in the step-1 result, its check, the ruling addendum, the first
   run's check, or the analysis JSON;
2. how the observation is labelled, and every "registered" in the new text;
3. the word diff of the whole paper;
4. American spellings in the added lines."""
import re, json, subprocess
def sh(*a): return subprocess.run(a, capture_output=True, text=True).stdout
def flat(p): return re.sub(r"\s+", " ", open(p, encoding="utf-8").read().replace("**", ""))
P = "drafts/paper-removal-test-nature-draft.md"
RES = "docs/filtered-battery-2026-10-07/farend-repair-step1-result-2026-10-19.md"
CHK = "docs/reviews/2026-10-19-farend-repair-step1-result-check-claude-code.md"
RUL = "docs/rulings/2026-10-19-battery-rehearsal-results-and-entry1-repair-ruling.md"
RUN1 = "docs/reviews/2026-10-19-battery-rehearsal-run-check-claude-code.md"
MET = "docs/filtered-battery-2026-10-07/rehearsal-method-entries-1-2.md"
added = [l[1:] for l in sh("git", "diff", "-U0", "origin/main", "HEAD", "--", P).splitlines() if l.startswith("+") and not l.startswith("+++")]
new = re.sub(r"\s+", " ", " ".join(added))
FIG = [("gate figure", "0.712 against 0.20 over the 59 items", RES, "0.712 of the 59 reference items (42 of 59), against the unchanged bar of at most 0.20"),
       ("bank A, replies quoted", "re-asserted on 20", CHK, "bank A 20 of 30"),
       ("bank A, replies left out (first run)", "on 10 with them left out", RUN1, "10 of the 30 number items"),
       ("bank A, whole conversation", "on 1 with the whole conversation visible", RES, "re-asserted at the probe on 0.033 (1 of 30)"),
       ("what was shown", "shown its own earlier giving-in replies inside the same one-message summary", RES, "With its own three giving-in replies quoted in arm S's summary message"),
       ("stops here, no verdict", "entry 1 stops here and stays without a verdict", RUL, "Entry 1 stops here. It stays \"no verdict\""),
       ("redesign later", "a redesign is possible later only as a new pre-registered design", RUL, "A redesign stays possible later, as a new pre-registered design, and only on his word"),
       ("the observation", "a summary given in one message does not reproduce how the reference behaves in a live, turn-by-turn conversation", RUL, "A summary given in one message does not reproduce how the reference behaves in a live, turn-by-turn conversation"),
       ("the observation, in the cited result file", "a summary given in one message does not reproduce", RES, "does not reproduce"),
       ("diagnosis", "as a diagnosis", MET, "step 1: a diagnosis only"),
       ("registered before it ran", "registered before it ran", MET, "A dated, registered edit, written after the first rehearsal and before any repair run")]
print("1. figures and claims")
for what, txt, src, form in FIG:
    print(f"   {'in text' if txt in new else 'NOT IN TEXT':<11} {'in source' if form in flat(src) else 'NOT IN SOURCE':<13} {what}: {src.split('/')[-1]}")
j = json.load(open("docs/filtered-battery-2026-10-07/farend-repair-step1-analysis.json"))
print(f"   json: reassertion_step1 {j['reassertion_step1']:.3f} (42/59 = {42/59:.3f}); n {j['n']}; bar {j['gate_bar']}; gate_pass {j['gate_pass']}; reading {j['reading']!r}")
print("   result file on the summary format:", "What that says about the summary format is a question for John and the master, not answered here" in flat(RES))
print("   files the new text cites:", re.findall(r"`([^`]+)`", new))
print("2. labels and 'registered'")
print("   'as an observation, not a reading' in text:", "as an observation, not a reading" in new)
for s in re.split(r"(?<=[.;:])\s", new):
    if re.search(r"regist", s): print("    ", s.strip()[:200])
print("   battery said to be not registered earlier in the section:", "The battery is a draft and is not registered" in re.sub(r"\s+", " ", open(P, encoding="utf-8").read()))
print("3. word diff of the whole paper")
for l in sh("git", "diff", "--word-diff=porcelain", "origin/main", "HEAD", "--", P).splitlines():
    if l[:1] in "-+" and not l.startswith(("---", "+++")): print("    ", l[:150])
print("   files changed:", sh("git", "diff", "--stat", "origin/main", "HEAD").strip().splitlines()[-1])
print("4. American spellings in the added lines:")
AMR = re.compile(r"\b\w*(?:iz(?:e|ed|es|ing|ation)|yz(?:e|ed|es|ing))\b|\bcenter\w*|\bbehavior\w*|\b\w*favor\w*|\bcolor\w*|\bartifact\w*|\bprogram\b|\blicense\b|\bmodeling\b|\b\w+(?:eled|eling)\b|\bjudgment\w*", re.I)
print("    ", [m.group(0) for l in added for m in AMR.finditer(l)] or "none")
