"""The training entry point for all four arms, on the rented machine or the
laptop.

FROZEN CODE, NOT YET REGISTERED. Frozen 2026-10-04 under
`docs/successor-code-freeze-method-2026-10-04.md`. Version 4 of the proposal
(section 5) lists "a training entry point on the rented machine for arms T, C
and M" as owed code; this is it, and it trains arm F the same way so that the
four arms differ only in their architecture.

The recipe
----------
The rehearsal's optimiser and schedule, unchanged (`training.train_arm` in
`experiments/rehearsal-successor-measure/src/`): AdamW at 0.002 with weight
decay 0.01, a one-cycle schedule with the first tenth warming up, gradients
clipped at 1.0. At full size it runs to a token budget, by default the closed
design's 585,544,960 tokens, on training episodes generated fresh at every
step, never matching an evaluation set and never carrying a fresh or relaxed
pairing (`grammar.TrainingStream`; the second since 2026-10-06). Every
number is an argument and is written into the checkpoint and the log. **The
defaults are the freeze session's call and the registration text must fix
them** (the method note, sections 3 and 6).

The files it writes, the run-file conventions the laptop watchdog and the
machine's shutdown watcher already expect (`train_a3.py` in experiment 06):

- `OUT.pt`: the checkpoint, replaced whole at every evaluation;
- `OUT.jsonl`: one line per evaluation, accuracy on the trajectory set
  (watched only; never a registered figure);
- `OUT.DONE`: written once, after the last checkpoint, with the step and token
  count; then "TRAINING COMPLETE" on its own line.

With `--no-self-terminate` (what the launcher passes when the machine's own
watcher is armed) the trainer never deletes its machine. Without it, it asks
to, and refuses unless the checkpoint is on the network volume and exists:
the guard `train_a3.self_terminate` carries, copied.

Corrigibility: trains on the machine it runs on; creates nothing, rents
nothing. The machine it runs on was created by a launcher under John's go
[C2].

    python train_successor.py --self-test
    python train_successor.py --arm M --size 10M --seed 0 --device cuda --out /workspace/mvm-out/x/succ_m_10m_seed0.pt
"""
from __future__ import annotations

import argparse
import json
import math
import os
import queue
import shutil
import tempfile
import threading
import time
from pathlib import Path

import numpy as np
import torch

import grammar as G
import models as M

REGISTERED_TOKEN_BUDGET = 585_544_960      # the closed design's, "the same token budget"


def steps_for(max_tokens: int, batch: int) -> int:
    return math.ceil(max_tokens / (batch * G.SEQ_LEN))


@torch.no_grad()
def accuracy(m, b: dict, chunk: int = 512) -> dict:
    m.eval()
    n = b["tokens"].shape[0]
    hits = np.zeros(2, dtype=np.int64)
    for s in range(0, n, chunk):
        sl = {k: v[s:min(s + chunk, n)] for k, v in b.items()}
        logits = m(sl)
        for c in (G.OWN, G.OTHER):
            hits[c] += int((logits[:, c].argmax(-1) == sl["targets"][:, c]).sum())
    m.train()
    return dict(own=float(hits[G.OWN] / n), other=float(hits[G.OTHER] / n), n=n)


class Prefetch:
    """Generates the next steps' batches on a background thread. The batch for
    a step depends only on the run seed and the step, so prefetching changes
    nothing about which episodes are seen."""

    def __init__(self, stream: G.TrainingStream, first: int, last: int, rows: int, depth: int = 8):
        self.q: queue.Queue = queue.Queue(maxsize=depth)
        self.err = None

        def work():
            try:
                for s in range(first, last + 1):
                    self.q.put((s, stream.batch_for_step(s, rows)))
            except BaseException as e:          # noqa: BLE001
                self.err = e
                self.q.put((None, None))

        self.t = threading.Thread(target=work, daemon=True)
        self.t.start()

    def get(self, step: int) -> dict:
        s, b = self.q.get()
        if s is None:
            raise RuntimeError(f"the data thread failed: {self.err!r}")
        assert s == step, (s, step)
        return b


def run(args) -> dict:
    device = torch.device(args.device)
    if not G.check_even_split(args.batch):
        raise SystemExit(f"refusing to train: --batch {args.batch} is odd, which cuts a matched "
                         f"pair (the even-split rule, RT-58)")
    torch.manual_seed(args.seed)
    model = M.build(args.arm, args.size).to(device)
    n_params = M.n_params(model)
    steps = args.steps or steps_for(args.max_tokens, args.batch)
    opt = torch.optim.AdamW(model.parameters(), lr=args.lr, weight_decay=args.weight_decay)
    sched = torch.optim.lr_scheduler.OneCycleLR(opt, max_lr=args.lr, total_steps=steps,
                                                pct_start=args.warmup_frac)
    recipe = dict(arm=args.arm, size=args.size, seed=args.seed, batch=args.batch, lr=args.lr,
                  weight_decay=args.weight_decay, warmup_frac=args.warmup_frac,
                  max_tokens=args.max_tokens, steps=steps, clip=1.0,
                  tokens_per_step=args.batch * G.SEQ_LEN, parameters=n_params,
                  data="fresh per step, evaluation sets excluded, fresh and relaxed pairings excluded")
    print(f"recipe {json.dumps(recipe)}", flush=True)

    traj = M.to_torch(G.batch(G.episodes_from_pairs(G.eval_pairs("trajectory"))), device)
    stream = G.TrainingStream(args.seed)
    start, tokens, log = 0, 0, []
    if args.resume:
        ck = torch.load(args.resume, map_location=device, weights_only=False)
        assert ck["cfg"] == M.config_dict(model), "resume: the configuration does not match"
        assert ck["recipe"] == recipe, "resume: the recipe does not match"
        model.load_state_dict(ck["state"])
        opt.load_state_dict(ck["opt"])
        sched.load_state_dict(ck["sched"])
        start, tokens, log = ck["step"], ck["tokens_seen"], ck["log"]
        print(f"resumed from {args.resume} at step {start}", flush=True)

    out = Path(args.out) if args.out else None
    if out:
        out.parent.mkdir(parents=True, exist_ok=True)

    def save(step):
        if not out:
            return
        tmp = out.with_suffix(".pt.tmp")
        torch.save({"cfg": M.config_dict(model), "state": model.state_dict(), "opt": opt.state_dict(),
                    "sched": sched.state_dict(), "step": step, "tokens_seen": tokens, "log": log,
                    "recipe": recipe, "stream_skipped": stream.skipped}, tmp)
        os.replace(tmp, out)

    model.train()
    pre = Prefetch(stream, start + 1, steps, args.batch)
    t0 = time.time() - (log[-1]["sec"] if log else 0)
    for step in range(start + 1, steps + 1):
        b = M.to_torch(pre.get(step), device)
        loss = model.loss(b)
        opt.zero_grad(set_to_none=True)
        loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
        opt.step()
        sched.step()
        tokens += args.batch * G.SEQ_LEN
        if step % args.eval_every == 0 or step == steps:
            acc = accuracy(model, traj)
            rec = dict(step=step, loss=round(float(loss.detach()), 4), tokens=tokens,
                       lr=sched.get_last_lr()[0], traj_own=acc["own"], traj_other=acc["other"],
                       skipped=stream.skipped, sec=round(time.time() - t0, 1),
                       sec_per_step=round((time.time() - t0) / step, 5))
            log.append(rec)
            print(json.dumps(rec), flush=True)
            if out:
                with open(out.with_suffix(".jsonl"), "a") as f:
                    f.write(json.dumps(rec) + "\n")
            save(step)
    if out:
        out.with_suffix(".DONE").write_text(json.dumps(dict(step=steps, tokens=tokens)) + "\n")
        print(f"saved {out}", flush=True)
        print("TRAINING COMPLETE", flush=True)
        if not args.no_self_terminate:
            self_terminate(str(out))
    return dict(params=n_params, tokens=tokens, log=log, model=model, recipe=recipe)


def self_terminate(out_path: str | None = None) -> None:
    """Ask the machine to delete itself, best-effort, and only if the
    checkpoint is on the network volume and exists. Copied from
    `experiments/06-mvm-0a-constructed-self-index/src/train_a3.self_terminate`,
    whose docstring records why each guard is there."""
    import subprocess
    if out_path:
        real = os.path.realpath(out_path)
        if not real.startswith("/workspace/"):
            print(f"self-terminate: REFUSING: output {real} is not on the network volume, so "
                  f"deleting this machine would destroy the checkpoint. Leaving the reap to "
                  f"the watchdog.", flush=True)
            return
        if not os.path.exists(out_path):
            print(f"self-terminate: REFUSING: no checkpoint at {out_path}", flush=True)
            return
    pod = os.environ.get("RUNPOD_POD_ID", "")
    if not pod:
        try:
            pod = Path("/root/mvm/pod_id").read_text().strip()
        except Exception:
            pod = ""
    if not pod:
        print("self-terminate: no pod id; leaving the reap to the watchdog", flush=True)
        return
    for cmd in (["runpodctl", "remove", "pod", pod], ["runpodctl", "pod", "delete", pod]):
        try:
            r = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        except Exception as e:                       # noqa: BLE001
            print(f"self-terminate: {' '.join(cmd)} raised {e}", flush=True)
            continue
        print(f"self-terminate: {' '.join(cmd)} -> rc={r.returncode} "
              f"{(r.stdout + r.stderr).strip()[:200]}", flush=True)
        if r.returncode == 0:
            return
    print("self-terminate: no route worked; the watchdog will reap this machine", flush=True)


def parser():
    ap = argparse.ArgumentParser()
    ap.add_argument("--arm", choices=M.ARMS)
    ap.add_argument("--size", choices=tuple(M.SIZES), default=M.REGISTERED_SIZE)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--batch", type=int, default=96)
    ap.add_argument("--lr", type=float, default=2e-3)
    ap.add_argument("--weight-decay", type=float, default=0.01)
    ap.add_argument("--warmup-frac", type=float, default=0.1)
    ap.add_argument("--max-tokens", type=int, default=REGISTERED_TOKEN_BUDGET)
    ap.add_argument("--steps", type=int, default=0, help="0: from the token budget")
    ap.add_argument("--eval-every", type=int, default=2000)
    ap.add_argument("--device", default="cpu")
    ap.add_argument("--out", default="")
    ap.add_argument("--resume", default="")
    ap.add_argument("--no-self-terminate", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    return ap


def self_test() -> None:
    fails = []

    def check(name, ok, detail=""):
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ""))
        if not ok:
            fails.append(name)

    print("train_successor.py self-test")
    check("the default token budget is 108,919 steps of 96 episodes",
          steps_for(REGISTERED_TOKEN_BUDGET, 96) == 108_919)
    tmp = tempfile.mkdtemp()
    try:
        for arm in M.ARMS:
            out = os.path.join(tmp, f"t_{arm}.pt")
            a = parser().parse_args(["--arm", arm, "--size", "toy", "--steps", "12", "--batch", "16",
                                     "--eval-every", "6", "--out", out, "--no-self-terminate"])
            r = run(a)
            ok = (os.path.exists(out) and os.path.exists(out.replace(".pt", ".DONE"))
                  and len(open(out.replace(".pt", ".jsonl")).read().splitlines()) == 2
                  and all(math.isfinite(x["loss"]) for x in r["log"]))
            check(f"arm {arm}: trains, writes the checkpoint, the log and the finished-marker", ok)
            ck = torch.load(out, weights_only=False)
            m2 = M.build_from_config(ck["cfg"])
            m2.load_state_dict(ck["state"], strict=True)
            check(f"arm {arm}: the checkpoint rebuilds the model it came from",
                  all(torch.equal(p, q) for p, q in zip(m2.state_dict().values(), r["model"].state_dict().values())))
        # resuming gives the run it would have been
        straight = os.path.join(tmp, "straight.pt")
        run(parser().parse_args(["--arm", "M", "--size", "toy", "--steps", "12", "--batch", "16",
                                 "--eval-every", "6", "--out", straight, "--no-self-terminate"]))
        # a run that is stopped after its step-6 checkpoint and resumed from it
        killed = os.path.join(tmp, "killed.pt")
        a_k = parser().parse_args(["--arm", "M", "--size", "toy", "--steps", "12", "--batch", "16",
                                   "--eval-every", "6", "--out", killed, "--no-self-terminate"])
        # keep the step-6 checkpoint as it was written, then resume from it
        snap = {}
        _orig = torch.save

        mid = os.path.join(tmp, "mid.pt")

        def capture_save(obj, path, *x, **k):
            r = _orig(obj, path, *x, **k)
            if isinstance(obj, dict) and obj.get("step") == 6:
                shutil.copyfile(path, mid)
                snap["ck"] = True
            return r
        torch.save = capture_save
        try:
            run(a_k)
        finally:
            torch.save = _orig
        assert snap.get("ck"), "no step-6 checkpoint was written"
        resumed = os.path.join(tmp, "resumed.pt")
        a_r = parser().parse_args(["--arm", "M", "--size", "toy", "--steps", "12", "--batch", "16",
                                   "--eval-every", "6", "--out", resumed, "--resume", mid,
                                   "--no-self-terminate"])
        run(a_r)
        s1 = torch.load(straight, weights_only=False)["state"]
        s2 = torch.load(resumed, weights_only=False)["state"]
        check("a run resumed from its step-6 checkpoint ends bit-identical to one never stopped",
              all(torch.equal(s1[k], s2[k]) for k in s1))
        # the even-split rule at the entry point
        try:
            run(parser().parse_args(["--arm", "F", "--size", "toy", "--steps", "2", "--batch", "15"]))
            check("an odd batch is refused before anything trains (RT-58)", False)
        except SystemExit:
            check("an odd batch is refused before anything trains (RT-58)", True)
        # the self-delete guard
        import io
        import contextlib
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            self_terminate(straight)
        check("the machine is never asked to delete itself when the checkpoint is off the "
              "network volume", "REFUSING" in buf.getvalue())
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    if fails:
        print(f"\n{len(fails)} failure(s)")
        raise SystemExit(1)
    print("\nall checks passed\ntrain_successor self-test OK")


if __name__ == "__main__":
    args = parser().parse_args()
    if args.self_test:
        self_test()
    else:
        if not args.arm:
            raise SystemExit("--arm is required")
        run(args)
