#!/bin/bash
# check_launcher_argument_guard.sh — the test for RT-198, the silent-argument
# failure.
#
# WHAT IT IS FOR. On 2026-09-21 a rented machine was created by a command whose
# stated purpose was to create nothing: the staged plan's step 0 ran a launcher
# with `--help`, the launcher had no argument handling at all, the flag was
# silently ignored, and the script carried on into a real launch at its
# defaults. This script is the test that catches that property.
#
# Method and reasoning: ../argument-guard-method.md. Ruled by John 2026-09-22.
#
# IT CREATES NOTHING AND SPENDS NOTHING. It never runs any launcher in a way
# that could reach a vendor command: the guarded launchers are run with an
# argument, which makes them refuse before they reach anything, and with
# DRYRUN=1, which the launchers' own guard stops before creation. The
# REGISTERED launcher is never run at all, with or without arguments, because
# running it with an argument is precisely the thing this test exists to
# forbid. It is checked by reading its text.
#
# Usage:  ./check_launcher_argument_guard.sh      (takes no arguments)
# Exit:   0 all checks pass; 1 a check failed.

set -uo pipefail

if [ "$#" -ne 0 ]; then
  echo "refusing to run: $(basename "$0") takes no command-line arguments." >&2
  echo "  got $# argument(s): $*" >&2
  exit 2
fi

SRC_DIR="$(cd "$(dirname "$0")" && pwd)"
fail=0
ok()  { echo "  [ ok ] $*"; }
bad() { echo "  [FAIL] $*"; fail=1; }

# The three UNREGISTERED launchers, which carry the guard as of 2026-09-22.
UNREGISTERED="launch_a3_fetch_first.sh launch_ctl_pilot.sh launch_pilot_a1.sh"

# The REGISTERED launcher. Amendment A3's "what is registered" section names
# it. It is NEVER run by this script.
REGISTERED="launch_a3.sh"

echo "RT-198 — launchers must refuse arguments rather than launch"
echo
echo "unregistered launchers: an argument is refused"
for f in $UNREGISTERED; do
  p="$SRC_DIR/$f"
  if [ ! -f "$p" ]; then bad "$f is missing"; continue; fi

  # The refusal itself. Any argument at all; this one is deliberately junk so
  # that nothing could interpret it as meaningful.
  out=$("$p" --definitely-not-a-real-flag 2>&1); st=$?
  if [ "$st" -eq 2 ]; then ok "$f refuses an argument (exit 2)"
  else bad "$f exited $st on an argument, wanted 2"; fi
  case "$out" in
    *"takes no command-line arguments"*) ok "$f says why it refused" ;;
    *) bad "$f refused without saying why: $out" ;;
  esac
  case "$out" in
    *"DRYRUN=1"*) ok "$f names DRYRUN=1 as the way to preview" ;;
    *) bad "$f does not tell the operator how to dry-run" ;;
  esac

  # STRUCTURAL: the guard must sit before anything that can reach the vendor.
  # This is checked by reading rather than by running, so that the check has no
  # network dependency and cannot itself create anything.
  gline=$(grep -n 'RT-198' "$p" | head -1 | cut -d: -f1)
  rline=$(grep -n '^[^#]*runpodctl' "$p" | head -1 | cut -d: -f1)
  if [ -n "$gline" ] && [ -n "$rline" ] && [ "$gline" -lt "$rline" ]; then
    ok "$f guard (line $gline) precedes any vendor command (line $rline)"
  else
    bad "$f guard does not demonstrably precede its first vendor command"
  fi
done

echo
echo "unregistered launchers: the guard did not break the real path"
for f in $UNREGISTERED; do
  p="$SRC_DIR/$f"
  [ -f "$p" ] || continue
  out=$(DRYRUN=1 "$p" 2>&1); st=$?
  if [ "$st" -eq 0 ]; then ok "$f dry run still exits 0"
  else bad "$f dry run exited $st"; fi
  case "$out" in
    *"nothing created"*) ok "$f dry run still creates nothing" ;;
    *) bad "$f dry run no longer reports creating nothing" ;;
  esac
done

echo
echo "registered launcher: read, never run"
p="$SRC_DIR/$REGISTERED"
if [ ! -f "$p" ]; then
  bad "$REGISTERED is missing"
elif grep -q 'RT-198' "$p"; then
  # The Gate A amendment has landed. From here the registered launcher is held
  # to the same standard as the others, and the standing prohibition below is
  # spent. Whoever lands that amendment should also run the refusal checks
  # above against this file.
  ok "$REGISTERED carries the guard — the Gate A amendment has landed"
  echo "  NOTE: move $REGISTERED into UNREGISTERED above so its refusal is exercised."
else
  ok "$REGISTERED does NOT carry the guard, which is expected before Gate A"
  cat <<'PROHIBITION'

  ***********************************************************************
  STANDING PROHIBITION, in force until the Gate A amendment clears:
  launch_a3.sh is REGISTERED TEXT and still has NO argument handling.
  An argument passed to it is SILENTLY IGNORED and it proceeds to a REAL
  LAUNCH at its defaults -- about ten hours and about ten dollars,
  writing into the registered seed-0 directory on the network volume.

      NO SESSION INVOKES A REGISTERED LAUNCHER WITH ANY ARGUMENT.

  To preview it without creating anything:  DRYRUN=1 ./launch_a3.sh
  Ruled by John 2026-09-22. Method: ../argument-guard-method.md [RT-198]
  ***********************************************************************

PROHIBITION
fi

echo
echo "negative control: the check must FAIL on an unguarded launcher"
# A test that can only pass proves nothing. This reproduces the shape the
# launchers had before 2026-09-22 -- a script that ignores its arguments and
# carries on -- and requires the checks above to REJECT it. The stand-in
# contains no vendor command, so it creates nothing even when it "proceeds".
# If this control ever reports the unguarded stand-in passing, the harness has
# stopped measuring what it claims to.
NEG_DIR=$(mktemp -d)
trap 'rm -rf "$NEG_DIR"' EXIT
cat > "$NEG_DIR/unguarded_launcher.sh" <<'STANDIN'
#!/bin/bash
set -uo pipefail
# No argument handling at all -- exactly the pre-2026-09-22 shape.
echo "creating SECURE pod (this stand-in creates nothing)"
STANDIN
chmod +x "$NEG_DIR/unguarded_launcher.sh"

neg_out=$("$NEG_DIR/unguarded_launcher.sh" --definitely-not-a-real-flag 2>&1); neg_st=$?
neg_caught=0
[ "$neg_st" -eq 2 ] || neg_caught=1
case "$neg_out" in *"takes no command-line arguments"*) ;; *) neg_caught=1 ;; esac
grep -q 'RT-198' "$NEG_DIR/unguarded_launcher.sh" || neg_caught=1

if [ "$neg_caught" -eq 1 ]; then
  ok "an unguarded launcher is REJECTED (exit $neg_st, no refusal, no guard)"
  ok "so these checks detect the property rather than always passing"
else
  bad "an unguarded launcher PASSED these checks -- the harness is broken"
fi

echo
if [ "$fail" -eq 0 ]; then
  echo "all checks pass. nothing was created and nothing was spent."
  exit 0
fi
echo "CHECKS FAILED."
exit 1
