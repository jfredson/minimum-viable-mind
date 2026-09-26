#!/usr/bin/env python3
"""check_remote_forms.py — run every background start a launcher sends over
ssh against a REAL local shell, and time how long the connection is held.

2026-09-25. The test for failure 6 in docs/known-failure-modes.md, "a remote
step tested only against stand-ins". On 2026-09-25 the unregistered launcher
hung for 30 minutes on its first real ssh to a rented machine
(docs/2026-09-25-rented-slice-findings.md, section 4). Every earlier test of
that line replaced ssh with a stand-in that exits at once, whatever the
remote command does, so no test could have seen it.

What stands in here is not ssh but the far end: `bash -c '<form>' | cat`.
Like ssh, `cat` waits until every process on the far side has closed its
output, which is exactly the property the hang depends on. Nothing is rented
and no vendor is contacted.

For each remote command in the launcher that contains `nohup` (a background
start), the check:
  * rewrites it to run locally: the program after `nohup` becomes a stand-in
    that leaves a marker file and then sleeps HOLD seconds, shell variables
    become a folder `x` beside the cd target, /root/ paths move under a
    scratch folder;
  * FAILS the start if the marker never appears: a form that returns at once
    because it never started anything has not been shown to return at once;
  * runs it through `bash -c … | cat` and times it;
  * decides: returns at once (under 2 s) -> ok; holds the connection AND the
    launcher cuts that ssh off with a time cap -> ok, reported as holding;
    holds and is NOT capped -> FAIL, because a real ssh would wait for the
    background program to finish.

Then a NEGATIVE CONTROL: a stand-in launcher line in the pre-fix form of
2026-09-25 (uncapped `cd … && nohup … &`) must be REJECTED. If it passes,
the check has stopped measuring what it claims to.

usage: check_remote_forms.py                 checks launch_a3_fetch_first.sh
       LAUNCHER=<file> check_remote_forms.py checks another launcher text
Exit 0 when every start passes and the control is rejected; 1 otherwise.
"""
import os
import re
import subprocess
import sys
import tempfile
import time
from pathlib import Path

HOLD = 8          # seconds the stand-in background program runs
AT_ONCE = 2.0     # a start that returns faster than this does not hold
SRC = Path(__file__).resolve().parent
LAUNCHER = Path(os.environ.get("LAUNCHER", SRC / "launch_a3_fetch_first.sh"))


def quoted_after(s, i):
    """The double-quoted string starting at s[i] == '"', unescaped; and the
    index just past its closing quote."""
    assert s[i] == '"'
    j, body = i + 1, ""
    while j < len(s):
        c = s[j]
        if c == "\\" and j + 1 < len(s):
            # bash's rules inside double quotes: backslash-newline vanishes,
            # a backslash escapes only $ ` " and itself, and is kept otherwise
            nxt = s[j + 1]
            body += "" if nxt == "\n" else nxt if nxt in '$`"\\' else c + nxt
            j += 2
            continue
        if c == '"':
            return body, j + 1
        body += c
        j += 1
    raise ValueError("unterminated quote")


CALL = re.compile(r'(\$SSH|ssh_capped\s+(\d+))\s+"')


def remote_starts(text):
    """Every `$SSH "…"` or `ssh_capped N "…"` whose quoted remote command
    contains nohup; with its line number and the cap the launcher puts on it."""
    found = []
    for m in CALL.finditer(text):
        line_start = text.rfind("\n", 0, m.start()) + 1
        if text[line_start:m.start()].lstrip().startswith("#"):
            continue
        body, end = quoted_after(text, m.end() - 1)
        if "nohup" not in body:
            continue
        n = text.count("\n", 0, m.start()) + 1
        capped = None
        if m.group(2):
            capped = f"ssh_capped {m.group(2)}s"
        else:
            rest = text[end:].split("\n")
            if re.match(r"\s*&\s*$", rest[0]):
                # the inline cap used since 2026-08-17: `$SSH "…" &` followed
                # within three lines by `( sleep N; kill "$PID" … ) &`
                for k, s2 in enumerate(rest[1:4], 1):
                    c = re.search(r"sleep\s+(\d+);\s*kill", s2)
                    if c:
                        capped = f"inline cap {c.group(1)}s (line {text.count(chr(10), 0, end) + 1 + k})"
                        break
        found.append((n, body, capped))
    return found


def localise(body, scratch):
    # the program after nohup, up to its first redirect, becomes a stand-in
    # that leaves a marker and then holds for HOLD seconds
    body = re.sub(r"nohup\s+.*?(?=\s(?:>>|>|2>|<)\s)", f"nohup sh {scratch}/hold.sh", body, count=1)
    body = body.replace("/root/", f"{scratch}/root/")
    # every shell variable becomes the relative folder `x`, which exists
    # beside the cd target, so redirects into "$RUN_DIR/…" still resolve
    body = re.sub(r"\$\{?[A-Za-z_][A-Za-z0-9_]*\}?", "x", body)
    return body


def time_form(form, cwd):
    # started from inside the stand-in for /root/mvm/src, so a form with no
    # `cd` of its own still finds the folder `x` its redirects point into
    t0 = time.monotonic()
    subprocess.run(["bash", "-c", 'bash -c "$1" | cat >/dev/null', "_", form],
                   cwd=cwd, timeout=HOLD + 10)
    return time.monotonic() - t0


def check(text, label, control=False):
    starts = remote_starts(text)
    bad = 0
    with tempfile.TemporaryDirectory() as t:
        scratch = str(Path(t).resolve())
        os.makedirs(f"{scratch}/root/mvm/src/x")
        Path(f"{scratch}/hold.sh").write_text(f"touch {scratch}/started\nsleep {HOLD}\n")
        for n, body, capped in starts:
            Path(f"{scratch}/started").unlink(missing_ok=True)
            secs = time_form(localise(body, scratch), f"{scratch}/root/mvm/src")
            time.sleep(0.5)
            held = secs >= AT_ONCE
            if not Path(f"{scratch}/started").exists():
                verdict, ok = "the stand-in background program NEVER STARTED, so this timing says nothing", False
            elif not held:
                verdict, ok = "returns at once", True
            elif capped:
                verdict, ok = f"HOLDS the connection; cut off by the launcher's {capped}", True
            else:
                verdict, ok = "HOLDS the connection and nothing cuts it off: a real ssh would wait for the background program", False
            bad += not ok
            tag = ("rejected" if not ok else "ACCEPTED") if control else (" ok " if ok else "FAIL")
            print(f"  [{tag}] {label} line {n}: returned after {secs:.1f}s -- {verdict}")
    return starts, bad


def main():
    print(f"remote background starts, run against a real local shell (| cat stands in for ssh; the background program holds {HOLD}s)")
    print(f"\n{LAUNCHER.name}")
    starts, bad = check(LAUNCHER.read_text(), LAUNCHER.name)
    if not starts:
        print("  [FAIL] found no background start at all -- the parser no longer matches this launcher")
        bad += 1

    print("\nnegative control: the pre-fix form of 2026-09-25 must be REJECTED")
    control = ('  $SSH "cd /root/mvm/src && nohup sh reap_agent.sh /root/mvm/reap.env \\\n'
               '        >> $RUN_DIR/reaper.log 2>&1 < /dev/null &" >/dev/null 2>&1\n')
    cstarts, cbad = check(control, "stand-in", control=True)
    if cstarts and cbad == len(cstarts):
        print("  [ ok ] the uncapped `cd … && nohup … &` stand-in is rejected, so this check detects the hang")
    else:
        print("  [FAIL] the pre-fix stand-in was NOT rejected: this check has stopped measuring the hang")
        bad += 1

    print()
    if bad:
        print(f"{bad} problem(s). Nothing was rented and nothing was spent.")
        return 1
    print("all checks pass. Nothing was rented and nothing was spent.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
