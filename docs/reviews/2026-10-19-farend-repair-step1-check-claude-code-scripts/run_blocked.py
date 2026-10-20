"""Run a script with every network connection made to fail; pass its arguments through.
Prints the exit code, any connection attempts, and whether D's network modules were imported.
Usage: python run_blocked.py <script> [args...]"""
import runpy, socket, sys
attempts = []
def refuse(self, *a, **k):
    attempts.append(a); raise OSError("network blocked by the check")
socket.socket.connect = refuse; socket.socket.connect_ex = refuse
socket.create_connection = lambda *a, **k: refuse(None, *a)
path = sys.argv[1]; sys.argv = sys.argv[1:]
code = 0
try:
    runpy.run_path(path, run_name="__main__")
except SystemExit as e:
    code = e.code
sys.stderr.flush()
print(f"  exit {code}; connections attempted {len(attempts)}; clients imported {'clients' in sys.modules}")
