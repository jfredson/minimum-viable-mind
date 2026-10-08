"""Independent check of pull request 116: can two programs writing the alarm's
records at once lose a write?  $0; every vendor call is a stand-in.

The watcher loads the records, then reads the vendor (seconds, up to 60 s
each), then saves. If the watchdog's `gone` (or the launcher's `register`)
writes in between, the watcher's save puts back the copy it loaded. Here the
stand-in balance reading performs the other program's write at that moment,
which is what a real overlap would do.

    python tests/check-of-116/shared_records_race.py   (from experiments/08-successor-degree)
"""
from __future__ import annotations

import os
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "src"))
import tripwire as T  # noqa: E402

clock = [1_900_000_000.0]
T.now = lambda: clock[0]


def quiet(f, *a):
    so = sys.stdout
    sys.stdout = open(os.devnull, "w")
    try:
        return f(*a)
    finally:
        sys.stdout.close()
        sys.stdout = so


# Case 1: the watchdog records a deletion while the watcher is mid-read.
d = tempfile.mkdtemp()
T.read_balance = lambda: 75.0
T.running_pods = lambda: {"podA"}
quiet(T.cmd_preflight, d)
quiet(T.cmd_register, d, "podA", 0.99, 1.0, "o")
clock[0] += 1800
deleted_at = clock[0] - 5


def balance_while_watchdog_writes():
    quiet(T.cmd_gone, d, "podA", deleted_at, "the watchdog")        # the other program's write
    return 74.5


T.read_balance = balance_while_watchdog_writes
T.running_pods = lambda: set()                                       # the machine is gone
quiet(T.watch_once, d, True)
m = T.load_state(d)["machines"]["podA"]
lost1 = m.get("gone_by") != "the watchdog"
print("1. the watchdog writes a deletion time while the watcher is reading the vendor")
print(f"   recorded: gone at {m.get('gone')} by {m.get('gone_by')!r}, inferred {m.get('gone_inferred')}")
print(f"   the watchdog's time ({deleted_at}) {'WAS LOST (replaced by the watcher inferring it)' if lost1 else 'survived'}")

# Case 2: the launcher registers a second machine while the watcher is mid-read.
d2 = tempfile.mkdtemp()
T.read_balance = lambda: 75.0
T.running_pods = lambda: {"podA"}
quiet(T.cmd_preflight, d2)
quiet(T.cmd_register, d2, "podA", 0.99, 1.0, "o")
clock[0] += 300


def balance_while_launcher_registers():
    quiet(T.cmd_register, d2, "podB", 0.99, 1.0, "o")
    return 74.9


T.read_balance = balance_while_launcher_registers
T.running_pods = lambda: {"podA", "podB"}
quiet(T.watch_once, d2, True)
lost2 = "podB" not in T.load_state(d2)["machines"]
print("\n2. the launcher registers a second machine while the watcher is reading the vendor")
print(f"   machines in the records afterwards: {sorted(T.load_state(d2)['machines'])}")
print(f"   the second machine {'WAS LOST: its spending is now unpredicted, so the comparison reads high' if lost2 else 'survived'}")
print(f"\n{'a write can be lost' if (lost1 or lost2) else 'no write lost'}")
