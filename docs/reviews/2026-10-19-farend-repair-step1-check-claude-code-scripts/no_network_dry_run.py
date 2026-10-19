"""Run the step-1 runner's dry run in this process with every network connection made to fail,
then report whether any connection was attempted and whether D's network modules were imported.
Usage: python no_network_dry_run.py <path to run_farend_repair_step1.py>"""
import contextlib, io, runpy, socket, sys

attempts = []
def refuse(self, *a, **k):
    attempts.append(a)
    raise OSError("network blocked by the check")
socket.socket.connect = refuse
socket.socket.connect_ex = refuse
socket.create_connection = lambda *a, **k: refuse(None, *a)

path = sys.argv[1]
sys.argv = [path]
buf = io.StringIO()
code = None
with contextlib.redirect_stdout(buf):
    try:
        runpy.run_path(path, run_name="__main__")
    except SystemExit as e:
        code = e.code
print(f"dry run exit code: {code}")
print(f"network connections attempted: {len(attempts)}")
for name in ("clients", "judge_objection", "run_ladder", "anthropic", "google.genai", "openai"):
    print(f"module {name!r} imported: {name in sys.modules}")
print(f"printed lines: {len(buf.getvalue().splitlines())}")
