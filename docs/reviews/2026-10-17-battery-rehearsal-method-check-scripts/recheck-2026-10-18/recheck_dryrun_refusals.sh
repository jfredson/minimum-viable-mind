#!/usr/bin/env bash
# Re-check of the fixed runner (commit 3b22925 on pull request 174's branch),
# 2026-10-18: the dry run against its new committed output, what the dry run and
# the refused invocations leave behind with Python's default bytecode caching ON,
# and the refusals that stop before any network import. Calls no model. Every run
# gets a clean environment holding no vendor key. The ceiling refusals, which sit
# after the go-quote check, are tried only in the stand-in copy
# (recheck_standin.sh), never here.
#
#   bash docs/reviews/2026-10-17-battery-rehearsal-method-check-scripts/recheck-2026-10-18/recheck_dryrun_refusals.sh <scratch-dir>
set -u
SCR=${1:?scratch directory}; mkdir -p "$SCR"
cd "$(dirname "$0")/../../../.."
P=docs/filtered-battery-2026-10-07/run_rehearsal_entries_1_2.py
OUTF=docs/filtered-battery-2026-10-07/run_rehearsal_entries_1_2.dryrun.out.txt
bare() { env -i HOME="$HOME" PATH="$PATH" "$@"; }   # bytecode caching left ON, Python's default
echo "runner at commit $(git log -1 --format=%h -- $P); committed output at commit $(git log -1 --format=%h -- $OUTF)"
before=$(git status --porcelain --ignored | sort)

echo "## 1. the dry run against its committed output (default bytecode caching on)"
bare python3 $P > "$SCR/dry.txt"; echo "exit $?"
cmp "$SCR/dry.txt" $OUTF && echo "cmp: identical"
shasum -a 256 "$SCR/dry.txt" $OUTF | sed "s#$SCR/##"
bare python3 $P > "$SCR/dry2.txt"; cmp -s "$SCR/dry.txt" "$SCR/dry2.txt" && echo "second run identical to the first"

echo; echo "## 2. the argument guard"
for a in --help -n run --dry-run ""; do
  bare python3 $P "$a" > "$SCR/arg.out" 2> "$SCR/arg.err"; c=$?
  echo "  args [$a]: exit $c; stdout $(wc -c < "$SCR/arg.out" | tr -d ' ') bytes; $(head -1 "$SCR/arg.err" | cut -c1-80)"
done

echo; echo "## 3. refusals before any network import"
try() { local label=$1; shift
  bare "$@" python3 $P > "$SCR/g.out" 2> "$SCR/g.err"; c=$?
  echo "  $label: exit $c; stdout $(wc -c < "$SCR/g.out" | tr -d ' ') bytes; stderr: $(head -1 "$SCR/g.err" | cut -c1-100)"; }
try "MVM_REHEARSAL_RUN=1 alone" MVM_REHEARSAL_RUN=1
try "with the ceilings but no go or row" MVM_REHEARSAL_RUN=1 MVM_CEILING_E1=21 MVM_CEILING_E2=17
try "with MVM_GO_QUOTE only" MVM_REHEARSAL_RUN=1 MVM_GO_QUOTE="test, not a go"
try "with both set to blanks" MVM_REHEARSAL_RUN=1 MVM_GO_QUOTE="  " MVM_WORKLOG_ROW=" "
try "MVM_ENTRY=3 with the switch" MVM_REHEARSAL_RUN=1 MVM_ENTRY=3
echo "  dry run with a bad ceiling value (MVM_CEILING_E1=abc):"
bare MVM_CEILING_E1=abc python3 $P > "$SCR/bad.out" 2>&1; echo "    exit $?; $(grep -m1 'refusing' "$SCR/bad.out")"
echo "  dry run with named ceilings 21.14 and 16.72 (the high end):"
bare MVM_CEILING_E1=21.14 MVM_CEILING_E2=16.72 python3 $P > "$SCR/named.out"; echo "    exit $?"
grep -E "ceilings for this preview|ceiling falls|not reached|NOTE" "$SCR/named.out" | sed 's/^/    /'

echo; echo "## 4. what all of the above left behind (must be nothing)"
comm -13 <(echo "$before") <(git status --porcelain --ignored | sort) | sed 's/^/  new: /'
echo "  .pyc files under the runner's folder and D's src: $(find docs/filtered-battery-2026-10-07 experiments/03-retained-independence/src -name '*.pyc' | wc -l | tr -d ' ')"
echo "  artifacts/ in the checkout: $( [ -e artifacts ] && echo yes || echo no); battery_rehearsal/ in the main checkout: $( [ -e /Users/john/Code/minimum-viable-mind/artifacts/stage3/battery_rehearsal ] && echo yes || echo no)"
echo "  where sys.dont_write_bytecode is set (line) and the first import of D's code (line): $(grep -n '^sys.dont_write_bytecode = True' $P | cut -d: -f1) and $(grep -n '^import items' $P | cut -d: -f1)"
