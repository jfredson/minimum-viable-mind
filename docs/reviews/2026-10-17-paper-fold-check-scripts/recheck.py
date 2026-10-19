#!/usr/bin/env python3
"""Re-check of 2026-10-18, after commit 9751f97 applied the eight conditions.
(a) For each condition, a command whose output would come out wrong if the
condition were not met as stated. (b) Every changed line of 9751f97, so a reader
can see that no line outside the conditions moved. Run from the worktree root."""
import re, subprocess
def sh(*a): return subprocess.run(a, capture_output=True, text=True).stdout
def flat(path): return re.sub(r"\s+", " ", open(path, encoding="utf-8").read())
E, P, N, L = "explainer.md", "drafts/paper-removal-test-nature-draft.md", "docs/outside-reader-approach-note-2026-10-17.md", "experiments/06-mvm-0a-constructed-self-index/compute-ledger.md"
e, p, n, ledger = flat(E), flat(P), flat(N), open(L, encoding="utf-8").read()
def show(k, ok, detail): print(f"condition {k}: {'MET' if ok else 'NOT MET'}  {detail}")
# 1 the interval sentence
ci = sh("python3", "-I", "-c", "import json;c=json.load(open('experiments/01-self-indexing-removal-test/removal_ci.json'))['cells']['idxres_mean_k16'];print({k:(v['lo'],v['hi']) for k,v in c.items()})").strip()
show(1, "each with its uncertainty interval above zero" not in e and "two of the three with their uncertainty intervals above zero; the self-relevant drop of 0.10 has an interval from 0.00 to 0.20, which reaches down to zero" in e, f"removal_ci.json lo/hi: {ci}")
# 2 the development runs' status
m = re.search(r"Four unregistered development runs.{0,330}?as a pipeline and throughput check", p)
show(2, bool(m) and "registered in advance" not in m.group(0) and "version 4 of the proposal (not registered)" in m.group(0), repr(m.group(0)[-170:]) if m else "sentence not found")
v4 = sh("git", "show", "HEAD:docs/successor-experiment-proposal-2026-10-03-v4.md")
print("   version 4 header says 'Nothing here is registered':", "Nothing here is registered" in re.sub(r"\s+", " ", v4[:2000]))
# 3 the four costs, read from the paper and found in the ledger
costs = re.search(r"\$1\.47 in all: \$([\d.]+), \$([\d.]+), \$([\d.]+) and \$([\d.]+) for arms M, T, C and F", p)
found = {c: ("| " + c + " |") in ledger for c in costs.groups()} if costs else {}
show(3, bool(costs) and all(found.values()) and abs(sum(map(float, costs.groups())) - 1.4655) < 1e-9, f"paper carries {costs.groups() if costs else None}; in the ledger's annotation table: {found}; sum {sum(map(float, costs.groups())) if costs else None:.4f}")
# 4 the closure quotation, exact against the closure block
src = re.sub(r"\s+", " ", sh("sed", "-n", "565,567p", "experiments/06-mvm-0a-constructed-self-index/amendment-a3.md").replace("**", "")).strip()
q = re.search(r'closed under its loss condition: "([^"]+)"', e)
show(4, bool(q) and q.group(1) in src, f"explainer quotes {q.group(1)[:60]!r}… ; inside closure line 565-567: {bool(q) and q.group(1) in src}")
# 5 the three labels
labels = {"ceiling measurement": "An unregistered measurement on 2026-09-17" in e,
          "fitted detector": "An unregistered fitted detector" in e,
          "C development runs": "The first development runs, which were not registered," in e}
show(5, all(labels.values()), str(labels))
# 6 the approach note
show(6, "to be validated on hand-set reference systems" in n and ", validated on hand-set" not in n, f"'to be validated on': {n.count('to be validated on')}")
# 7 the two headers
hp, hn = p[:1500], n[:1500]
show(7, "passed the Voice" not in hp and "passed the Voice" not in hn and hp.count("by the session that wrote them") == 1 and hn.count("by the session that wrote them") == 1 and "2026-10-17-paper-fold-check-claude-code.md" in hp and "2026-10-17-paper-fold-check-claude-code.md" in hn, "paper header and note header: 'passed' gone, self-pass and the check named")
# 8 the stale citation
c8 = {f: flat(f).count("pull request 172") for f in (E, P, N)}
body = sh("gh", "pr", "view", "175", "--json", "body", "-q", ".body")
show(8, not any(c8.values()), f"'pull request 172' in the three texts: {c8}")
print("   pull request 175's body (not editable by a commit): 'pull request 172'", body.count("pull request 172"), "; '$0.34'", body.count("$0.34"))
# (c) the explainer's lines are whole paragraphs, so list the changes word by word
print("\nword-level changes of 9751f97 (- removed, + added), all three files:")
for l in sh("git", "show", "--format=", "--word-diff=porcelain", "9751f97").splitlines():
    if (l.startswith("-") or l.startswith("+")) and not l.startswith(("---", "+++")):
        print("  ", l[:150])
# (b) every line the commit changed
print("\nlines changed by 9751f97 (old line number -> text):")
for l in sh("git", "show", "-U0", "--format=", "9751f97").splitlines():
    if l.startswith(("@@", "+++", "---")) or l.startswith(("+", "-")):
        print("  ", l[:150])
