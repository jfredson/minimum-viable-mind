"""The θ/δ threshold lock, and the guard that makes it a gate.

Amendment A3 decision 15, ratified 2026-09-15 and never built until now:
*the lesion script must refuse to run a localized-subspace (L1) ablation
without a lock-hash argument.*

Why a mechanism and not a promise
---------------------------------
RT-10's clause is that any ablation result read before the thresholds are
locked voids the lock. That clause has already been broken once, by
accident and in good faith: thread 4 read register-ablation battery scores
on the pilot seed-0 checkpoint on 2026-08-19 before any lock existed,
which is why that checkpoint's band is labelled *for the record* rather
than as a clean lock (`gate0-null-calibration-findings.md`). A3 §3.3 says
the sequence is this time "enforced by the gate order, not by intention".
Intention is what failed. This is the enforcement.

How it works
------------
1. After the pilot is trained and its calibration has run, `write_lock`
   records the thresholds together with the hash of the calibration record
   they came from, the checkpoint they were computed on, and a timestamp.
   **The lock commit is John's**, per the registration; this module only
   produces the file he commits.
2. Any script that performs an L1 ablation calls `require_lock(path)`
   first. It refuses unless the file exists, parses, covers the batteries
   about to be read, and matches the digest of the calibration record it
   claims to come from. A missing, malformed, stale or mismatched lock
   stops the run.

What this cannot do
-------------------
It cannot stop somebody running an ablation by hand in a notebook, and it
is not meant to. It removes the specific failure that already happened —
a script being pointed at a checkpoint before the thresholds existed —
and makes the omission loud instead of silent.

    ../../../.venv/bin/python lock_guard.py --self-test
"""
from __future__ import annotations

import argparse
import hashlib
import json
import tempfile
from datetime import datetime, timezone
from pathlib import Path

LOCK_VERSION = 1


class LockError(RuntimeError):
    """Raised when an L1 ablation is attempted without a valid lock."""


def digest(path: Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write_lock(out: Path, *, calibration_record: Path, checkpoint: str,
               checkpoint_md5: str, theta: dict, delta: dict,
               ceilings: dict, note: str = "") -> dict:
    """Produce the lock file. Refuses to overwrite: a second lock on the
    same path would silently replace the thresholds a result was read
    against [C6]."""
    out = Path(out)
    if out.exists():
        raise LockError(f"refusing to overwrite an existing lock: {out}")
    rec = {
        "lock_version": LOCK_VERSION,
        "locked_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "calibration_record": str(Path(calibration_record).name),
        "calibration_sha256": digest(calibration_record),
        "checkpoint": checkpoint, "checkpoint_md5": checkpoint_md5,
        "theta": theta, "delta": delta, "ceilings": ceilings,
        "note": note or ("thresholds locked before any L1 ablation was "
                         "read, per RT-10 and A3 §3.3"),
    }
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(rec, indent=2))
    return rec


def require_lock(lock_path: str | Path | None, *, batteries: tuple,
                 calibration_record: Path | None = None) -> dict:
    """Gate an L1 ablation. Returns the lock, or raises.

    `batteries` is what the caller is about to read; a lock that does not
    carry a threshold for one of them does not authorize reading it.
    """
    if not lock_path:
        raise LockError(
            "L1 ablation requires --lock <path>. The thresholds must be "
            "locked BEFORE any localized-subspace result is read (RT-10; "
            "A3 §3.3). This is the check that thread 4's accidental "
            "pre-lock read on 2026-08-19 did not have.")
    p = Path(lock_path)
    if not p.exists():
        raise LockError(f"lock file not found: {p}")
    try:
        rec = json.loads(p.read_text())
    except Exception as e:
        raise LockError(f"lock file unreadable: {p} ({e})") from e
    if rec.get("lock_version") != LOCK_VERSION:
        raise LockError(f"unknown lock version: {rec.get('lock_version')}")
    for field in ("theta", "delta", "calibration_sha256", "checkpoint"):
        if field not in rec:
            raise LockError(f"lock is missing '{field}': {p}")
    missing = [b for b in batteries if b not in rec["theta"]]
    if missing:
        raise LockError(
            f"lock carries no threshold for {missing}; it does not "
            f"authorize reading {batteries}")
    if calibration_record is not None:
        got = digest(calibration_record)
        if got != rec["calibration_sha256"]:
            raise LockError(
                "the calibration record does not match the one this lock "
                f"was written from (lock {rec['calibration_sha256'][:12]}, "
                f"record {got[:12]}) — the thresholds were locked against "
                "different numbers")
    return rec


def self_test() -> None:
    with tempfile.TemporaryDirectory() as d:
        d = Path(d)
        cal = d / "calibration.json"
        cal.write_text(json.dumps({"summary": {"theta": {"T_act": 0.01}}}))
        lock = d / "theta_delta.lock.json"
        bats = ("T_act", "T_other")

        # no lock at all
        for bad in (None, ""):
            try:
                require_lock(bad, batteries=bats)
                raise AssertionError("missing lock must refuse")
            except LockError:
                pass
        try:
            require_lock(d / "nope.json", batteries=bats)
            raise AssertionError("absent file must refuse")
        except LockError:
            pass

        rec = write_lock(lock, calibration_record=cal, checkpoint="a3.pt",
                         checkpoint_md5="deadbeef",
                         theta={"T_act": 0.01, "T_other": 0.01},
                         delta={"T_act-T_other": 0.01},
                         ceilings={"T_act": 0.2921, "T_other": 0.3227})
        assert rec["lock_version"] == LOCK_VERSION

        # a valid lock passes, and validates against its calibration record
        got = require_lock(lock, batteries=bats, calibration_record=cal)
        assert got["checkpoint"] == "a3.pt"

        # a lock that does not cover the battery being read refuses
        try:
            require_lock(lock, batteries=("T_act", "T_state"))
            raise AssertionError("uncovered battery must refuse")
        except LockError:
            pass

        # thresholds locked against different numbers refuse
        cal2 = d / "other_calibration.json"
        cal2.write_text(json.dumps({"summary": {"theta": {"T_act": 0.9}}}))
        try:
            require_lock(lock, batteries=bats, calibration_record=cal2)
            raise AssertionError("mismatched calibration must refuse")
        except LockError:
            pass

        # a second lock must not silently replace the first
        try:
            write_lock(lock, calibration_record=cal, checkpoint="x",
                       checkpoint_md5="x", theta={}, delta={}, ceilings={})
            raise AssertionError("overwriting a lock must refuse")
        except LockError:
            pass

        # a corrupt lock refuses rather than passing something through
        bad = d / "corrupt.json"
        bad.write_text("{not json")
        try:
            require_lock(bad, batteries=bats)
            raise AssertionError("corrupt lock must refuse")
        except LockError:
            pass
    print("lock_guard self-test OK (7 refusal paths, 1 accept path)")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--verify", default=None,
                    help="check a lock file and print it")
    ap.add_argument("--batteries", default="T_act,T_other")
    args = ap.parse_args()
    if args.self_test:
        self_test()
        return
    if args.verify:
        rec = require_lock(args.verify,
                           batteries=tuple(args.batteries.split(",")))
        print(json.dumps(rec, indent=2))


if __name__ == "__main__":
    main()
