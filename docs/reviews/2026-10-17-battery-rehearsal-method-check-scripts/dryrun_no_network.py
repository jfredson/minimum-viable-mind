#!/usr/bin/env python3
"""Run the rehearsal runner's dry run with the network blocked and every import
recorded, for the check of pull request 174 (2026-10-17).

Before the runner starts, this harness (1) makes every socket connection raise,
so a call that reached a vendor would crash the dry run instead of going out,
and (2) records every module imported. It then runs the committed runner, with
no arguments, as the main program, writes its output to the file named by
argument 1, and prints which network or experiment-D call modules were
imported. The runner is not changed. Calls no model.

    python3 docs/reviews/2026-10-17-battery-rehearsal-method-check-scripts/dryrun_no_network.py <out-file>
"""
import builtins
import io
import os
import runpy
import socket
import sys
from contextlib import redirect_stdout
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
OUT = Path(sys.argv[1]).resolve()
RUNNER = REPO / "docs/filtered-battery-2026-10-07/run_rehearsal_entries_1_2.py"
attempts = []


def refuse(*a, **k):
    attempts.append(repr(a)[:80])
    raise OSError("network blocked by the check harness")


socket.socket.connect = refuse
socket.socket.connect_ex = refuse
socket.create_connection = refuse
socket.getaddrinfo = refuse

imported = set()
_real_import = builtins.__import__


def recording_import(name, *a, **k):
    imported.add(name.split(".")[0])
    return _real_import(name, *a, **k)


builtins.__import__ = recording_import
for k in [k for k in os.environ if k.startswith("MVM_") or k.endswith("_API_KEY")]:
    del os.environ[k]
before = set(sys.modules)
sys.argv = [str(RUNNER.relative_to(REPO))]
os.chdir(REPO)
buf = io.StringIO()
code = 0
with redirect_stdout(buf):
    try:
        runpy.run_path(str(RUNNER), run_name="__main__")
    except SystemExit as e:
        code = e.code
watch = {"anthropic", "google", "openai", "httpx", "requests", "urllib3", "clients", "judge_objection",
         "run_ladder", "judge_ladder", "mvm", "concurrent"}
new_modules = {m.split(".")[0] for m in set(sys.modules) - before}
print(f"runner exit status: {code}")
print(f"socket connection attempts: {len(attempts)}")
print(f"network or experiment-D call modules imported: {sorted((imported | new_modules) & watch) or 'none'}")
print(f"experiment D modules imported: {sorted((imported | new_modules) & {'items', 'framings', 'clients', 'judge_objection', 'run_ladder'})}")
# Self-test, so the two detectors are seen to fire: a blocked connection and a recorded import.
try:
    socket.create_connection(("api.anthropic.com", 443))
except OSError:
    pass
import xml.dom  # noqa: E402,F401  (any module the runner did not import)
print(f"self-test: a connection attempt after the run is caught: {len(attempts) == 1}; "
      f"an import after the run is recorded: {'xml' in imported}")
OUT.write_text(buf.getvalue())
print(f"dry-run output written to {OUT.name}: {len(buf.getvalue().encode())} bytes")
