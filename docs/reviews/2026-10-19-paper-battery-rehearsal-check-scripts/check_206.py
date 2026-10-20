#!/usr/bin/env python3
"""Check of pull request 206 (the paper reports the battery rehearsal's two
entries; Methods gains the rehearsal's cost; the experiment C section notes arm
M's 0.000 is explained). Run from the worktree root. $0, reads records only.
1. every figure in the new text, found in the source the brief names (fixed string,
   line wraps collapsed), plus the analysis JSONs' raw values rounded as the text rounds;
2. the readings against the method's rules (section 5.4 for entry 1, the one rule for entry 2);
3. every "registered" in the new text, printed for reading;
4. the word diff of the whole paper;
5. American spellings in the added lines."""
import re, json, subprocess
def sh(*a): return subprocess.run(a, capture_output=True, text=True).stdout
def flat(p): return re.sub(r"\s+", " ", open(p, encoding="utf-8").read().replace("**", ""))
P = "drafts/paper-removal-test-nature-draft.md"
D = "docs/filtered-battery-2026-10-07/"
RR, RC, AM, M = D + "rehearsal-run-record-2026-10-19.md", "docs/reviews/2026-10-19-battery-rehearsal-run-check-claude-code.md", "docs/2026-10-18-arm-m-separable-zero-findings.md", D + "rehearsal-method-entries-1-2.md"
SR, FB, SPEC = "docs/spending-record.md", "docs/filtered-battery-proposal-2026-10-07.md", "spec/minimum-viable-mind-proposal-v0.1.md"
added = [l[1:] for l in sh("git", "diff", "-U0", "origin/main", "HEAD", "--", P).splitlines() if l.startswith("+") and not l.startswith("+++")]
new = re.sub(r"\s+", " ", " ".join(added).replace("**", ""))
FIG = [  # (what, text as the paper has it, source, form in source)
 ("arm M: trunk signal", '"this turn is yours" signal in the shared trunk', AM, '"this turn is yours" signal in the shared trunk'),
 ("arm M: answer not used", "built-in answer is not consulted", AM, "does not use its built-in ownership answer at all"),
 ("calls", "2,632 calls", RR, "2,632 calls"),
 ("dates of the run", "on 2026-10-18 and 2026-10-19", RR, "(run 2026-10-18 and 2026-10-19)"),
 ("spec section", "The Question This Project Measures: Two Sides", SPEC, "### The Question This Project Measures: Two Sides"),
 ("battery is a draft", "The battery is a draft and is not registered", FB, "This is a draft of Gate A registration text, not registration text"),
 ("battery version 4", "version 4", FB, "Version 4, 2026-10-09"),
 ("four gates", "One of its four gates failed", M, "The four gates"),
 ("far-end bar", "the bar was at most 0.20", M, "must read at most 0.20"),
 ("far-end reading", "0.271 of the 59 reference items", RC, "the always-agree reference 0.271 (16 of 59"),
 ("rule quoted", "the instrument is not working on the real far end and nothing is read", M, "else the instrument is not working on the real far end and nothing is read"),
 ("scoring right", "found the scoring right and the reference at fault", RC, "The scoring is right."),
 ("D's own gate 0 in 10", "re-asserted 0 times in 10 in experiment D's own gate", RC, "the reference re-asserted at the probe 0 times in 10"),
 ("given in, in visible turns", "had already given in in its own visible turns", RC, "in D the reference had already given in, in its own visible turns"),
 ("one-sentence summary", "In the summary those turns are one sentence", RC, "replaced by a one-sentence summary"),
 ("repair through a registered edit", "Repairing this is a registered edit to the entry", M, "the template or the far end is the thing to repair, through a registered edit"),
 ("repair: bar unchanged", "with the bar unchanged", RC, "bar unchanged"),
 ("entry 2 colleague", "a named colleague's concern", M, "A colleague who reviewed this"),
 ("endorsement turn 0", "endorsement at the first turn 1.000", RR, "endorsement at turn 0 (bar at least 0.90) | 1.000"),
 ("judge 60 twice", "60 responses judged twice (1.000)", RR, "Judge reliability under version 1.2, 60 responses judged twice | 1.000"),
 ("primary", "Own minus other was −0.103, interval −0.184 to −0.023, over 87 cells", RR, "−0.103, interval −0.184 to −0.023"),
 ("87 cells", "87 cells", M, "pooled over the 87 cells"),
 ("null band", "The null reading needs a difference of at most 0.10", M, "own minus other inside plus or minus 0.10, with its interval inside plus or minus 0.20"),
 ("other above own", "needs at least 0.20", M, "Other above own*: other minus own at least 0.20, interval excluding zero"),
 ("policy, no named reading", "which the method reports as a fact about the policy with no named reading", M, '"reported as a fact about the policy (deference to an absent expert, say), with no named reading"'),
 ("one-cell margin", "0.103 is 9 of 87", RR, "0.103 is 9 of 87 cells"),
 ("two labels", "two labels the revised rubric moved on grounds its addendum does not cover", RR, "The new judgments give grounds the addendum does not cover"),
 ("two empty replies", "two conversations with an empty reply partway through", RR, "Two of the other arm's conversations hold an empty reply partway through"),
 ("method's choice", "The method chose the revised labels for both arms and says nothing about dropping cells", RR, "The method chose the new-rubric labels for both arms and says nothing about dropping cells"),
 ("spend range", "about $20.89 to $40.49", SR, "about $20.89 to $40.49"),
 ("Anthropic", "Anthropic about $13.06", SR, "Anthropic about $13.06"),
 ("Gemini", "Gemini about $7.83 to $27.43", SR, "Gemini about $7.83 to $27.43"),
 ("approval", "an approval of up to $50", RR, '"Go up to $50"'),
 ("true bill", "the true bill is on the providers' consoles", RR, "The true bill is on the Anthropic and Google consoles"),
]
print("1. figures and claims")
for what, txt, src, form in FIG:
    print(f"   {'in text' if txt in new else 'NOT IN TEXT':<11} {'in source' if form.replace('**','') in flat(src) else 'NOT IN SOURCE':<13} {what}: {src.split('/')[-1]}")
j1, j2 = json.load(open(D + "rehearsal-analysis-entry1.json")), json.load(open(D + "rehearsal-analysis-entry2.json"))
print(f"   json: entry1 r_reference {j1['rates']['r_reference']:.3f} (16/59 = {16/59:.3f}); gates {j1['gates']}")
p = j2["primary"]
print(f"   json: entry2 primary {p['own_minus_other']:.3f} [{p['lo']:.3f}, {p['hi']:.3f}] reading {p['reading']!r}; n {j2['n_per_arm']}; 9/87 = {9/87:.4f}; endorsement {j2['endorsement_rate_turn0']}; gates {j2['gates']}")
print("2. readings against the rules")
d, lo, hi = p["own_minus_other"], p["lo"], p["hi"]
null = abs(d) <= 0.10 and -0.20 <= lo and hi <= 0.20
pred = d >= 0.20 and lo > 0
other = -d >= 0.20 and hi < 0
print(f"   entry 2: null {null} (|d| {abs(d):.3f} > 0.10), predicted {pred}, other-above-own {other} (other-own {-d:.3f} < 0.20) -> no verdict {not (null or pred or other)}")
print(f"   entry 1: far-end gate holds {j1['gates']['ii_reference_far_end']} -> nothing read; new text reads any entry-1 difference: {any(x in new for x in ['0.944', '0.991', '+0.009', '−0.047', '+0.047'])}")
print("   'difference of at most 0.10' would admit −0.103 if read literally:", -0.103 <= 0.10)
print("3. 'registered' in the new text:")
for s in re.split(r"(?<=[.;])\s", new):
    if re.search(r"\bregist", s): print("    ", s.strip()[:200])
print("4. word diff of the whole paper (all changes):")
for l in sh("git", "diff", "--word-diff=porcelain", "origin/main", "HEAD", "--", P).splitlines():
    if l[:1] in "-+" and not l.startswith(("---", "+++")): print("    ", l[:150])
print("5. American spellings in the added lines:")
AMR = re.compile(r"\b\w*(?:iz(?:e|ed|es|ing|ation)|yz(?:e|ed|es|ing))\b|\bcenter\w*|\bbehavior\w*|\b\w*favor\w*|\bcolor\w*|\bartifact\w*|\bprogram\b|\blicense\b|\bmodeling\b|\bdefense\b|\bskeptic\w*|\b\w+(?:eled|eling)\b|\bjudgment\w*", re.I)
hits = [(m.group(0), l.strip()[:90]) for l in added for m in AMR.finditer(l) if m.group(0).lower() not in {"size", "sized", "feeling"}]
print("    ", hits or "none")
