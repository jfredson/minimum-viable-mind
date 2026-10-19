#!/bin/sh
# Check of pull request 196 (John's spending ruling of 2026-10-18). From the worktree root:
#   sh docs/reviews/2026-10-18-spending-ruling-check-claude-code-scripts/check_196.sh
# $0. Reads only; the field-removed case runs on a copy in a temporary folder.
BASE=af59d73   # main with pull request 195 merged, which pull request 196 corrects
L=experiments/06-mvm-0a-constructed-self-index/compute-ledger.md

echo "== 1. the headline wording, field present (worktree) and removed (copy)"
python3 scripts/export_site.py --check; echo "exit $?"
T=$(mktemp -d); mkdir -p "$T/scripts" "$T/data"
cp scripts/export_site.py "$T/scripts/"; cp data/project.toml data/roadmap.toml data/headline.json "$T/data/"
sed -i '' '/^headline_words = /d' "$T/data/project.toml"
echo "headline_words lines left in the copy: $(grep -c '^headline_words' "$T/data/project.toml")"
python3 "$T/scripts/export_site.py" --check 2>&1; echo "exit $?"

echo; echo "== 2. the site check"
(cd site && npm run check >/dev/null 2>&1; echo "npm run check exit $?")

echo; echo "== 3. the \$450 line before pull request 195, after it, and now"
python3 - "$BASE" <<'P'
import subprocess, sys, tomllib
def line(rev):
    d = tomllib.loads(subprocess.run(["git", "show", f"{rev}:data/project.toml"], capture_output=True, text=True, check=True).stdout)
    return [x for x in d["spend"]["lines"] if x["cap"] == 450][0]
b, m, n = line(sys.argv[1] + "^1"), line(sys.argv[1]), line("HEAD")
for k in ("name", "cap", "spent"):
    print(f"{k}: before 195 {b[k]!r} | after 195 {m[k]!r} | now {n[k]!r}")
mark = "As written before 2026-10-18: "
print("marker appears once:", n["note"].count(mark) == 1)
print("text after the marker is the note before 195, character for character:", n["note"].split(mark, 1)[1] == b["note"], f"({len(b['note'])} characters)")
P

echo; echo "== 4. John's words in STATUS.md against the ruling file"
python3 - <<'P'
import re
def quote(path, lead):
    t = " ".join(open(path).read().split())
    i = t.index(lead)
    return re.search(r'"([^"]+)"', t[i:]).group(1)
r = quote("docs/rulings/2026-10-18-spending-ruling.md", "relayed to this session:")
s = quote("STATUS.md", "John's ruling, in his words:")
print("ruling file:", r); print("STATUS.md:  ", s); print("identical:", r == s)
P

echo; echo "== 5. the spending record's sources"
echo "-- the ledger's running total (last programme figure):"
grep -o 'after this run: programme about \*\*\$230.94 of \$450\*\*' $L
echo "-- the ledger on 2026-08-30 (its 2026-08-17 row; the next row is 2026-09-14):"
grep -o '~\$181.4 / \$400 (A2)' $L; grep -o '^| 2026-0[89]-[0-9]*' $L | sed -n '/08-17/,/09-14/p'
echo "-- John's figure of 2026-08-30, as amendment-a3.md quotes his binding rulings of that day:"
grep -o 'true spend to date is about \$281 to \$300' experiments/06-mvm-0a-constructed-self-index/amendment-a3.md | head -1
echo "-- the Gate A tier 2 cost:"
grep -o '\*\*about \$1.04 at most\*\*' docs/reviews/2026-10-09-two-sided-question-gate-a-INDEX.md
echo "-- the poll's method file exists:"; ls docs/outside-perspective/2026-10-07-poll-method.md
echo "-- the running total's arithmetic: 230.94 + (100 to 119) + (1.04 + 2.88 to 7.13)"
python3 -c "print(round(230.94+100+1.04+2.88,2), 'to', round(230.94+119+1.04+7.13,2))"

echo; echo "== 6. what the ledger gains"
git diff --numstat $BASE HEAD -- $L
git diff $BASE HEAD -- $L | grep '^[+-]' | grep -v '^+++\|^---' | cut -c1-80

echo; echo "== 7. (own check) the explainer's citation for the total across every vendor"
echo "-- STATUS entries dated 2026-10-12 in STATUS.md and STATUS-archive.md:"
grep -c '^## WHERE THINGS STAND 2026-10-12' STATUS.md STATUS-archive.md
echo "-- '\$335 to \$360' in explainer.md before pull request 195, after it, and now:"
for r in $BASE^1 $BASE HEAD; do printf '%s ' "$(git show $r:explainer.md | grep -c '335 to \$360')"; done; echo
echo "-- the citation 'entry of 2026-10-12' in explainer.md before pull request 195:"
git show $BASE^1:explainer.md | grep -c 'entry of 2026-10-12'
echo "-- '335' in the compute ledger:"; grep -c '335' $L
