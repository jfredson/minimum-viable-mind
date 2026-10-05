#!/bin/bash
# Test T7 of docs/successor-code-freeze-method-2026-10-04.md: the successor
# launcher, checked without creating anything.
#   1. the argument guard of RT-198, the same three checks
#      experiments/06-.../src/check_launcher_argument_guard.sh runs on the
#      other unregistered launchers (that script's list is not edited);
#   2. a dry run exits 0, says it created nothing, and never calls the vendor
#      tool (a stand-in on PATH fails loudly if it is called);
#   3. it refuses to run without ARM, SIZE, WAVE, ESTIMATE_HOURS or a hard cap;
#   4. a dry run reports that a real launch would be refused while the
#      tripwire's halt file exists;
#   5. the remote-start forms check of experiment 06, pointed at this launcher.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
L="$HERE/../src/launch_successor.sh"
OPS="$HERE/../../06-mvm-0a-constructed-self-index/src"
PY="${PY:-$HOME/Code/minimum-viable-mind/.venv/bin/python}"
fails=0
ok()  { echo "  [ ok ] $*"; }
bad() { echo "  [FAIL] $*"; fails=$((fails + 1)); }
STUB=$(mktemp -d); trap 'rm -rf "$STUB"' EXIT
printf '#!/bin/sh\necho "STAND-IN runpodctl CALLED: $*" >> "%s/called"; exit 99\n' "$STUB" > "$STUB/runpodctl"
chmod +x "$STUB/runpodctl"
ENVOK="ARM=C SIZE=10M SEED=0 WAVE=check ESTIMATE_HOURS=1.5 HARD_CAP_USD=2.50 RATE_PER_HOUR_USD=0.99 PY_LOCAL=$PY"

echo "1. the argument guard (RT-198)"
out=$("$L" --definitely-not-a-real-flag 2>&1); st=$?
[ "$st" -eq 2 ] && ok "an argument is refused (exit 2)" || bad "exit $st on an argument, wanted 2"
case "$out" in *"takes no command-line arguments"*) ok "it says why" ;; *) bad "no reason given" ;; esac
case "$out" in *"DRYRUN=1"*) ok "it names DRYRUN=1" ;; *) bad "no dry-run hint" ;; esac
g=$(grep -n 'RT-198' "$L" | head -1 | cut -d: -f1); r=$(grep -n '^[^#]*runpodctl' "$L" | head -1 | cut -d: -f1)
[ -n "$g" ] && [ -n "$r" ] && [ "$g" -lt "$r" ] && ok "the guard (line $g) precedes any vendor command (line $r)" \
  || bad "the guard does not precede the first vendor command"

echo "2. a dry run creates nothing and calls no vendor"
out=$(env PATH="$STUB:$PATH" $ENVOK DRYRUN=1 "$L" 2>&1); st=$?
[ "$st" -eq 0 ] && ok "dry run exits 0" || bad "dry run exited $st"
case "$out" in *"nothing created"*) ok "dry run says nothing was created" ;; *) bad "dry run does not say nothing was created" ;; esac
[ ! -f "$STUB/called" ] && ok "the vendor tool was never called" || bad "the vendor tool was called: $(cat "$STUB/called")"
case "$out" in *"train_successor.py --arm C --size 10M --seed 0 --batch 96"*) ok "the training command is the successor trainer with the recipe spelled out" ;; *) bad "unexpected training command" ;; esac

echo "3. required settings"
for drop in ARM SIZE WAVE ESTIMATE_HOURS HARD_CAP_USD; do
  e=$(echo "$ENVOK" | tr ' ' '\n' | grep -v "^$drop=" | tr '\n' ' ')
  out=$(env -u $drop PATH="$STUB:$PATH" $e DRYRUN=1 "$L" 2>&1); st=$?
  [ "$st" -eq 2 ] && ok "refuses without $drop" || bad "ran without $drop (exit $st)"
done
out=$(env PATH="$STUB:$PATH" $(echo "$ENVOK" | sed 's/SIZE=10M/SIZE=toy/') DRYRUN=1 "$L" 2>&1); st=$?
[ "$st" -eq 2 ] && ok "refuses the toy size on a rented machine" || bad "accepted SIZE=toy"

echo "4. a halt file is reported"
T="$HERE/../artifacts/tripwire/check"; mkdir -p "$T"; echo "TRIPPED (test)" > "$T/HALT"
out=$(env PATH="$STUB:$PATH" $ENVOK DRYRUN=1 "$L" 2>&1)
case "$out" in *"would be REFUSED"*) ok "the dry run says a real launch would be refused" ;; *) bad "halt file not reported" ;; esac
rm -rf "$T"; rmdir "$HERE/../artifacts/tripwire" "$HERE/../artifacts" 2>/dev/null

echo "5. remote starts return or are capped (experiment 06's check, pointed here)"
if LAUNCHER="$L" "$PY" "$OPS/check_remote_forms.py" > "$STUB/forms.txt" 2>&1; then
  ok "check_remote_forms.py passes on this launcher"; sed 's/^/      /' "$STUB/forms.txt"
else
  bad "check_remote_forms.py fails on this launcher"; sed 's/^/      /' "$STUB/forms.txt"
fi

echo
[ "$fails" -eq 0 ] && echo "all checks pass. nothing was created and nothing was spent." || echo "$fails check(s) FAILED"
exit $fails
