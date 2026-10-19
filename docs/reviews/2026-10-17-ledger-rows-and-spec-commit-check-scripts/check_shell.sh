#!/bin/bash
# Plain-shell versions of checks 1, 5 and 6 (pull request 173), so a reader can
# re-run them without the Python script. Reads committed git objects only.
# Run from anywhere inside the repository:  bash check_shell.sh > check_shell.out.txt
cd "$(git rev-parse --show-toplevel)" || exit 1
S=spec/minimum-viable-mind-proposal-v0.1.md
V=docs/rulings/2026-10-12-two-sided-question-section-2-v3.md
L=experiments/06-mvm-0a-constructed-self-index/red_team_ledger.md
run() { echo "\$ $1"; bash -c "$1"; echo; }
run "git show 1a9752e:$S | shasum -a 256"
run "git diff -U0 a99e8e9 1a9752e -- $S | grep -E '^@@'"
run "git diff -U0 a99e8e9 1a9752e -- $S | grep -c '^-[^-]'"
run "git diff -U0 a99e8e9 1a9752e -- $S | grep '^+' | grep -vc '^+++'; echo '(every added line, blank ones included)'"
run "git diff --stat a99e8e9 origin/main -- $S $V $L | tail -1; echo '(nothing above: none of the three files changed on the main line since the branch point)'"
run "diff <(git show bfd1d5d:$V | sed -n 75,293p) <(git show 1a9752e:$S | sed -n 20,238p) && echo IDENTICAL"
run "diff <(git show bfd1d5d:$V) <(git show 1a9752e:$V | sed 3,25d) && echo IDENTICAL"
run "git show a99e8e9:$L | grep -cE 'RT-(28[3-9]|29[0-9]|30[0-4])\b'"
run "git show 1a9752e:$L | grep -oE '^\| RT-(28[3-9]|29[0-9]|30[0-4])\b' | sort | uniq -c | awk '{print \$1}' | sort | uniq -c; echo '(read: N numbers each with exactly M rows, as \"N M\")'"
run "git show 1a9752e:$S | grep -n -o 'each interval above zero'"
run "git show 1a9752e:experiments/01-self-indexing-removal-test/removal_ci.json | python3 -c 'import json,sys; c=json.load(sys.stdin)[\"cells\"][\"idxres_mean_k16\"]; [print(k, c[k]) for k in (\"T_self_irrelevant\",\"T_self_relevant\",\"T_syntax\")]'"
run "git show 1a9752e:$S | grep -n -o -E 'no better than in the frontier|no more presence in the constructed systems than'"
