"""launch_gate_mutation_run.py — the launch gate seen FAILING, on purpose.

Breaks src/launch_gate.sh four ways, runs both harnesses against each broken
copy, and restores the original after every one, proving the restore by
hash. A test never seen to fail has not been shown to detect anything
(docs/known-failure-modes.md, "Adding to this list"); this is the record
that these two harnesses do. Method: ../launcher-sleep-gate-method.md §4;
output quoted in ../launcher-sleep-gate-findings.md.

It edits launch_gate.sh IN PLACE while it runs. Run it on a clean tree, and
if it is interrupted, put the file back with:  git checkout -- launch_gate.sh
Rents nothing: the harnesses it runs use stand-ins for every vendor call.

usage: python3 launch_gate_mutation_run.py   (from anywhere; no arguments)
"""
import hashlib
import os
import re
import shutil
import subprocess
import sys
import tempfile

if len(sys.argv) != 1:
    sys.exit("refusing to run: this takes no arguments")

SRC = os.path.dirname(os.path.abspath(__file__))
GATE = os.path.join(SRC, "launch_gate.sh")
HARNESSES = ["launch_gate_selftest.sh", "sleep_guard_selftest.sh"]

MUTATIONS = {
    "M1 warning only: the refusal prints and carries on":
        ("  } >&2\n  exit 1\n}", "  } >&2\n  return 0\n}"),
    "M2 the ledger check accepts anything":
        ('  echo "local pre-flight: is there a ledger row with an estimate for \'$OUT\'?"\n',
         '  echo "local pre-flight: is there a ledger row with an estimate for \'$OUT\'?"\n  return\n'),
    "M3 the deadline-order check removed":
        ('&& [ "$WATCH_H" -gt "$TERM_H" ]; then', '&& false; then'),
    "M4 the discharging-charger check removed":
        ('elif [ "$batt_state" = "discharging" ]; then', 'elif false; then'),
    # M5 and M6 added 2026-09-24 with the two fixes owed by the check of pull
    # request 33 (reviews/2026-09-24-launch-gate-pr33-check-claude-worktree.md):
    # each puts one of the two defects back.
    "M5 the name pattern treats '-' and '.' as word boundaries again":
        ('GATE_RE="(^|[^A-Za-z0-9_.-])(mvm-)?${re}([^A-Za-z0-9_.-]|\\\\.([^A-Za-z0-9_-]|\\$)|\\$)"',
         'GATE_RE="(^|[^A-Za-z0-9_])${re}([^A-Za-z0-9_]|\\$)"'),
    "M6 the eight-cell rule removed":
        ('    if [ "$cells" != 8 ]; then\n', '    if false; then\n'),
}


def sha(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


fd, backup = tempfile.mkstemp(suffix=".launch_gate.sh.orig")
os.close(fd)
shutil.copy(GATE, backup)
orig = sha(GATE)
ansi = re.compile(r"\x1b\[[0-9;]*m")
print("original launch_gate.sh sha256", orig)
try:
    for name, (old, new) in MUTATIONS.items():
        with open(backup) as f:
            text = f.read()
        assert text.count(old) == 1, "mutation site not found: " + name
        with open(GATE, "w") as f:
            f.write(text.replace(old, new))
        print("\n#", name)
        for h in HARNESSES:
            r = subprocess.run([os.path.join(SRC, h)], capture_output=True, text=True)
            out = ansi.sub("", r.stdout + r.stderr)
            counts = [l for l in out.splitlines() if l.startswith("checks passed")]
            print(f"  {h}: exit {r.returncode}; {counts[0] if counts else 'NO COUNT'}")
            seen = {}
            for line in out.splitlines():
                if "FAIL:" in line:
                    # the rental log line carries a timestamp; group on the rest
                    key = re.sub(r"--terminate-after \S+", "--terminate-after <time>", line.strip())
                    seen[key] = seen.get(key, 0) + 1
            for key, n in seen.items():
                print(f"      {n} x {key}")
finally:
    shutil.copy(backup, GATE)
    os.remove(backup)
print("\nrestored; sha256", sha(GATE), "matches original:", sha(GATE) == orig)
sys.exit(0 if sha(GATE) == orig else 1)
