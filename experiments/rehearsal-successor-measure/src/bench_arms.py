"""Seconds per step for the three architectures, at a stated shape, on
whatever machine it is run on.

UNREGISTERED. This is the measurement rehearsal item R-7 of
`docs/successor-experiment-proposal-2026-09-21.md`: seconds per step and
projected wall-clock and money for each of the three architectures at the
registered size, so that the second release of money rests on a measurement
rather than on a per-step premium inferred from a different experiment.

**What this file can and cannot answer.** Run on the laptop it gives the
*ratios* between the three architectures, which is the part of the estimate
that is about the architectures. It cannot give the absolute seconds per step
on rented hardware, and no arithmetic on a laptop figure can: that is the
whole reason John's ruling of 2026-09-21 asks for the figure to be measured
rather than inferred. The same file run on a rented machine gives the absolute
number, which is why the staged slice runs it there.

Nothing here rents anything or contacts any vendor. It times a model on the
machine it is already on.

    ../../../.venv/bin/python bench_arms.py --device auto --steps 20
    python bench_arms.py --device cuda --steps 50 --out /workspace/mvm-out/slice_handshake/bench_arms.json
"""
from __future__ import annotations

import argparse
import json
import os
import platform
import time

import torch

import arms as A
import grammar as G
import training as T

# The registered configuration's shape: the 30-million rung of the scale
# ladder in `experiments/06-mvm-0a-constructed-self-index/src/model.py`.
REGISTERED_SHAPE = dict(d_model=448, n_layers=12, n_heads=8)


def bench(arm: str, device, shape: dict, batch: int, steps: int,
          warmup: int = 5) -> dict:
    cfg = A.Config(arm=arm, **shape)
    model = A.Arm(cfg).to(device)
    opt = torch.optim.AdamW(model.parameters(), lr=1e-4)
    _, tb = T.make_data(max(batch, 8), seed=5, pool="train", device=device)
    b = T.slice_batch(tb, torch.arange(batch, device=device))

    def one():
        loss = model.loss(b)
        opt.zero_grad(set_to_none=True)
        loss.backward()
        opt.step()

    for _ in range(warmup):
        one()
    sync(device)
    per = []
    for _ in range(steps):
        t0 = time.time()
        one()
        sync(device)
        per.append(time.time() - t0)
    per.sort()
    return dict(arm=arm, seconds_per_step=sum(per) / len(per),
                median_seconds_per_step=per[len(per) // 2],
                fastest=per[0], slowest=per[-1], steps=steps, batch=batch,
                parameters=A.n_params(model), sequence_length=G.SEQ_LEN, **shape)


def sync(device):
    if device.type == "cuda":
        torch.cuda.synchronize()
    elif device.type == "mps":
        torch.mps.synchronize()


def machine() -> dict:
    d = dict(platform=platform.platform(), processor=platform.processor(),
             torch=torch.__version__)
    if torch.cuda.is_available():
        d["accelerator"] = torch.cuda.get_device_name(0)
    return d


def write(path: str, out: dict) -> None:
    """Replace the output file whole, so a copy taken at any moment finds
    either the previous version or this one, never half of one."""
    tmp = path + ".tmp"
    with open(tmp, "w") as f:
        json.dump(out, f, indent=2, sort_keys=True)
    os.replace(tmp, path)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--device", default="auto")
    ap.add_argument("--steps", type=int, default=20)
    ap.add_argument("--batch", type=int, default=32)
    ap.add_argument("--out", default="")
    a = ap.parse_args()
    device = T.pick_device(a.device)
    # "complete" stays false until every architecture is timed. The file is
    # rewritten after EACH one, so a run cut short (out of memory on one arm,
    # the machine deleted, the step's time cap) still leaves the figures it
    # got, and says it is short rather than looking finished.
    out = dict(machine=machine(), device=str(device), shape=REGISTERED_SHAPE,
               arms={}, complete=False)
    for arm in A.ARMS:
        r = bench(arm, device, REGISTERED_SHAPE, a.batch, a.steps)
        out["arms"][arm] = r
        print(f"arm {arm}: {r['seconds_per_step'] * 1000:.1f} ms/step "
              f"(median {r['median_seconds_per_step'] * 1000:.1f}), "
              f"{r['parameters']:,} parameters", flush=True)
        if a.out:
            write(a.out, out)
            print(f"wrote {a.out} ({len(out['arms'])} of {len(A.ARMS)} "
                  f"architectures)", flush=True)
    base = out["arms"]["F"]["seconds_per_step"]
    out["ratio_to_arm_F"] = {k: v["seconds_per_step"] / base
                             for k, v in out["arms"].items()}
    out["complete"] = True
    print("ratios to the freely trained arm: "
          + ", ".join(f"{k} {v:.3f}" for k, v in out["ratio_to_arm_F"].items()))
    if a.out:
        write(a.out, out)
        print(f"wrote {a.out}")


if __name__ == "__main__":
    main()
