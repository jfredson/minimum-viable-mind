#!/usr/bin/env bash
# Checks 1 to 3 of the check of pull request 174 (2026-10-17): the dry run
# against its committed output, what the dry run writes, the refused
# invocations, and the rubric copy's hash against the main line. Calls no model.
#
# Every real-run invocation here is one the runner must refuse BEFORE it imports
# experiment D's network code (main() rejects a bad MVM_ENTRY first; real_run()
# checks MVM_GO_QUOTE and MVM_WORKLOG_ROW before anything else). No invocation
# here sets MVM_REHEARSAL_RUN=1 together with both of those. Every run gets a
# clean environment (env -i) holding no vendor key.
#
#   bash docs/reviews/2026-10-17-battery-rehearsal-method-check-scripts/checks_dryrun_gates_rubric.sh <scratch-dir>
set -u
SCR=${1:?scratch directory}; mkdir -p "$SCR"
cd "$(dirname "$0")/../../.."
P=docs/filtered-battery-2026-10-07/run_rehearsal_entries_1_2.py
OUTF=docs/filtered-battery-2026-10-07/run_rehearsal_entries_1_2.dryrun.out.txt
clean() { env -i HOME="$HOME" PATH="$PATH" PYTHONDONTWRITEBYTECODE=1 "$@"; }   # bytecode off, except in 2a

echo "## 1. the dry run, against its committed output"
clean python3 $P > "$SCR/dry.txt"; echo "exit $?"
cmp "$SCR/dry.txt" $OUTF && echo "cmp: identical"
shasum -a 256 "$SCR/dry.txt" $OUTF | sed "s#$SCR/##"
echo "python: $(python3 --version)"

echo; echo "## 2a. what the dry run leaves behind, with Python's default bytecode caching on"
before=$(git status --porcelain --ignored | sort)
env -i HOME="$HOME" PATH="$PATH" python3 $P > "$SCR/dry2.txt"; echo "exit $?"
cmp "$SCR/dry2.txt" $OUTF && echo "cmp: identical"
comm -13 <(echo "$before") <(git status --porcelain --ignored | sort) | sed 's/^/  new: /'
find docs/filtered-battery-2026-10-07 experiments/03-retained-independence/src -name '*.pyc' | sed 's/^/  file: /'
find docs/filtered-battery-2026-10-07 experiments/03-retained-independence/src -name __pycache__ -type d -exec rm -r {} +
echo "  (removed again by this script)"
ls -d artifacts 2>/dev/null || echo "  no artifacts/ directory in the checkout"

echo; echo "## 2b. the argument guard"
for a in --help -n run --dry-run ""; do
  clean python3 $P "$a" > "$SCR/arg.out" 2> "$SCR/arg.err"; c=$?
  echo "  args [$a]: exit $c; stdout $(wc -c < "$SCR/arg.out" | tr -d ' ') bytes; first stderr line: $(head -1 "$SCR/arg.err")"
done

echo; echo "## 2c. the real-run gate's refusals (each must refuse and print nothing on stdout)"
try() { local label=$1; shift
  clean "$@" python3 $P > "$SCR/g.out" 2> "$SCR/g.err"; c=$?
  echo "  $label: exit $c; stdout $(wc -c < "$SCR/g.out" | tr -d ' ') bytes; stderr: $(head -1 "$SCR/g.err" | cut -c1-110)"; }
try "MVM_REHEARSAL_RUN=1 alone" MVM_REHEARSAL_RUN=1
try "with MVM_GO_QUOTE only" MVM_REHEARSAL_RUN=1 MVM_GO_QUOTE="test, not a go"
try "with MVM_WORKLOG_ROW only" MVM_REHEARSAL_RUN=1 MVM_WORKLOG_ROW=test
try "with both set to blanks" MVM_REHEARSAL_RUN=1 MVM_GO_QUOTE="   " MVM_WORKLOG_ROW="  "
try "MVM_ENTRY=3 with the real-run switch" MVM_REHEARSAL_RUN=1 MVM_ENTRY=3
clean MVM_REHEARSAL_RUN=yes python3 $P > "$SCR/yes.out" 2>&1; c=$?
echo "  MVM_REHEARSAL_RUN=yes (not exactly 1): exit $c; output identical to the dry run: $(cmp -s "$SCR/yes.out" $OUTF && echo yes || echo no)"
echo "  no artifacts/ directory and no battery_rehearsal/ created: $( [ ! -e artifacts ] && [ ! -e /Users/john/Code/minimum-viable-mind/artifacts/stage3/battery_rehearsal ] && echo true || echo false)"

echo; echo "## 2d. where the runner writes, and where it imports network code (line numbers)"
grep -nE 'write_text|write_bytes|open\(|mkdir|unlink|rmtree|rename|shutil|os\.remove' $P | sed 's/^/  /'
grep -nE '^\s*(from clients|import judge_objection|import anthropic|from google)' $P | sed 's/^/  /'
grep -nE '^def (dry_run|real_run|main)' $P | sed 's/^/  /'

echo; echo "## 3. the rubric copy's pinned hash against experiment D's registered file on the main line"
RUB=experiments/03-retained-independence/src/batteries/liveness_rubric.md
echo "  main line $(git rev-parse --short origin/main): $(git show origin/main:$RUB | shasum -a 256 | cut -c1-64)"
echo "  this branch's file:      $(shasum -a 256 $RUB | cut -c1-64)"
echo "  pinned in the runner:    $(grep -A1 'liveness_rubric.md":' $P | tail -1 | tr -dc 'a-f0-9')"
echo "  named in the method:     $(grep -o 'a6f2[0-9a-f]*' docs/filtered-battery-2026-10-07/rehearsal-method-entries-1-2.md | sort -u | tr '\n' ' ')"
echo "  named in the v1.2 file:  $(grep -o 'a6f2[0-9a-f]*' docs/filtered-battery-2026-10-07/liveness_rubric_v1.2_entry2.md | sort -u | tr '\n' ' ')"
echo "  the registered file's history: $(git log --format='%h %ad' --date=short origin/main -- $RUB | tr '\n' ' ')"
for f in experiments/03-retained-independence/src/stage3_run_config.json experiments/03-retained-independence/src/framings.py; do
  echo "  $(basename $f): main line $(git show origin/main:$f | shasum -a 256 | cut -c1-16)... pinned $(grep -A1 "$(basename $f)\":" $P | tail -1 | tr -dc 'a-f0-9' | cut -c1-16)..."
done
python3 - <<'EOF'
from pathlib import Path
v11 = Path("experiments/03-retained-independence/src/batteries/liveness_rubric.md").read_bytes()
v12 = Path("docs/filtered-battery-2026-10-07/liveness_rubric_v1.2_entry2.md").read_bytes()
i = v12.find(v11)
print(f"  v1.1 bytes ({len(v11)}) found inside the v1.2 file at byte offset {i}; once only: {v12.count(v11) == 1}")
print(f"  what precedes it: an HTML comment of {i} bytes ending {v12[i-6:i]!r}; what follows: {v12[i+len(v11):i+len(v11)+40]!r}")
EOF
echo "  anything in the pull request that opens D's registered rubric for writing:"
git diff --name-only origin/main...HEAD | while read -r f; do
  grep -nE "liveness_rubric\.md" "$f" | grep -iE "write|open\(.*['\"][wa]|unlink|replace|edit" | sed "s#^#    $f:#"
done
echo "    (end of list)"
echo "  every line of the runner naming RUBRIC_V11 (each must only read it):"
grep -nE 'RUBRIC_V11' $P | sed 's/^/    /' 
echo "  pull request's changes to anything under experiments/: $(git diff --name-only origin/main...HEAD -- experiments | wc -l | tr -d ' ') files"

echo; echo "## end: bytecode left in the checkout by this script (must be none): $(find docs/filtered-battery-2026-10-07 experiments/03-retained-independence/src -name '*.pyc' | wc -l | tr -d ' ')"
