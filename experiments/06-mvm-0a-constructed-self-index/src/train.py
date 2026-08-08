"""MVM-0a training loop (pre-registration v1.0 §Procedure).

What this implements, each traceable to the registration:

- **Answer-only supervision.** The loss is next-token CE on answer
  positions only (`model.loss`); no auxiliary loss anywhere [§Materials].
- **On-policy fill [RT-02].** From `--on-policy-after` steps, the model's
  own turns are filled by its own sampled outputs (canonicalized by the
  shared template in `curriculum.fill_own_turns`), so ownership is
  grounded in causal authorship. The warm-up window exists because an
  untrained model samples uniform noise; the registered 5-seed runs use
  the same schedule, recorded in the run config.
- **Frozen-battery eval [RT-14].** Held-out accuracy is read from the
  frozen `batteries/*.jsonl` items only — parsed from their frozen
  rendered text, never regenerated. Model selection during pilots uses
  held-out episodes; ablation batteries are never touched here.
- **Twin runs [RT-03]** via `--twin` (no-register model, same everything).
- **C2 (corrigibility):** this script trains only when a human runs it;
  it never launches pods, schedules itself, or restarts.

Smoke test (CPU/MPS, ~2 min, no GPU spend):

    ../../../.venv/bin/python train.py --smoke
"""
from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

import numpy as np
import torch

import curriculum as C
import encoding as E
from model import MVM0aModel, Config, SCALES, to_torch

BATTERY_DIR = Path(__file__).resolve().parents[1] / "batteries"


# ---------------------------------------------------------------- batteries

def parse_battery_item(d: dict) -> tuple[C.Episode, C.Query]:
    """Reconstruct an encodable episode from a FROZEN battery item's
    rendered text [RT-14]. Agents get pseudo-ids in order of first
    appearance; register keying is by marker, so pseudo-ids are harmless.
    own_slot is not reconstructed (the tensor dict never uses it)."""
    turns, markers = [], []
    for line in d["episode"].splitlines():
        m, _assign, item, _to, value = line.split()
        if m not in markers:
            markers.append(m)
        turns.append(C.Turn(agent=markers.index(m), marker=m,
                            item=item, value=value))
    q = d["question"]
    if q.startswith("where did"):
        choices = C.SLOTS
    elif q.startswith("which parcel"):
        choices = C.ITEMS
    elif q.startswith("how many parcels"):
        choices = [str(i) for i in range(len(turns) + 1)]
    else:                                   # "how many turns ..."
        choices = [str(i) for i in range(len(turns) + 2)]
    assert len(choices) == d["n_choices"], (q, len(choices), d["n_choices"])
    ep = C.Episode(seed=-1, n_agents=len(markers), own_slot=-1,
                   markers=markers, turns=turns)
    return ep, C.Query("frozen", q, d["answer"], list(choices))


def eval_batteries(model: MVM0aModel, device: str, n_per: int = 50) -> dict:
    model.eval()
    out = {}
    for path in sorted(BATTERY_DIR.glob("battery_*.jsonl")):
        items = [json.loads(l) for l in path.read_text().splitlines()][:n_per]
        correct = 0
        for i in range(0, len(items), 25):
            chunk = [parse_battery_item(d) for d in items[i:i + 25]]
            batch = to_torch(E.collate([E.encode_episode(ep, query=q)
                                        for ep, q in chunk]), device)
            cids = [[E.VOCAB[c] for c in q.choices] for _, q in chunk]
            picks = model.score_choices(batch, cids)
            correct += sum(p == E.VOCAB[q.answer]
                           for p, (_, q) in zip(picks, chunk))
        out[path.stem.replace("battery_", "")] = round(correct / len(items), 3)
    model.train()
    return out


# ------------------------------------------------------------- on-policy fill

@torch.no_grad()
def model_fill(model: MVM0aModel, ep: C.Episode, device: str) -> C.Episode:
    """Fill the model's own turns with its own sampled slot choices
    [RT-02: causal authorship]. Sequential over own turns so each sample
    conditions on previously filled ones; queries are re-derived by
    `curriculum.fill_own_turns` (including the T_state count fix)."""
    own_idx = [i for i, t in enumerate(ep.turns) if t.agent == ep.own_slot]
    slot_ids = torch.tensor([E.VOCAB[s] for s in C.SLOTS], device=device)
    cursor = iter(own_idx)

    def sample_fn(ctx: str, item: str) -> str:
        ti = next(cursor)
        enc = to_torch(E.collate([E.encode_episode(ep)]), device)
        logits = model.forward(enc)[0]
        span = (enc["turn_ids"][0] == ti).nonzero().flatten()
        to_pos = int(span[-1]) - 2        # ... item to [value] <nl>
        row = logits[to_pos][slot_ids]
        return C.SLOTS[int(torch.multinomial(
            torch.softmax(row, dim=-1), 1))]

    return C.fill_own_turns(ep, sample_fn)


# ------------------------------------------------------------------ training

def run(args) -> dict:
    device = args.device
    torch.manual_seed(args.seed)
    cfg = SCALES[args.scale]
    if args.twin:
        cfg = Config(**{**cfg.__dict__, "use_register": False})
    model = MVM0aModel(cfg).to(device)
    n_params = sum(p.numel() for p in model.parameters())
    opt = torch.optim.AdamW(model.parameters(), lr=args.lr,
                            weight_decay=0.01)
    print(f"scale={args.scale} twin={args.twin} params={n_params/1e6:.1f}M "
          f"device={device} seed={args.seed}")

    tokens_seen, t0, log = 0, time.time(), []
    for step in range(1, args.steps + 1):
        eps = C.generate_balanced(args.batch, seed=args.seed * 10 ** 6 + step,
                                  forced_revision_frac=0.25)
        if step > args.on_policy_after:
            eps = [model_fill(model, e, device) for e in eps]
        pairs = [(e, e.queries[(step + i) % len(e.queries)])
                 for i, e in enumerate(eps)]
        batch = to_torch(E.collate([E.encode_episode(e, query=q)
                                    for e, q in pairs]), device)
        loss = model.loss(batch)
        opt.zero_grad(set_to_none=True)
        loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
        opt.step()
        tokens_seen += int(batch["input_ids"].numel())

        if step % args.eval_every == 0 or step == args.steps:
            accs = eval_batteries(model, device, n_per=args.eval_n)
            rec = {"step": step, "loss": round(float(loss.detach()), 4),
                   "tokens": tokens_seen, "acc": accs,
                   "sec": round(time.time() - t0, 1)}
            log.append(rec)
            print(rec)

    if args.out:
        Path(args.out).parent.mkdir(parents=True, exist_ok=True)
        torch.save({"cfg": cfg.__dict__, "state": model.state_dict(),
                    "log": log, "args": vars(args)}, args.out)
        print(f"saved {args.out}")
    return {"params": n_params, "tokens": tokens_seen, "log": log}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--scale", choices=list(SCALES), default="smoke")
    ap.add_argument("--twin", action="store_true",
                    help="no-register twin [RT-03]")
    ap.add_argument("--steps", type=int, default=300)
    ap.add_argument("--batch", type=int, default=16)
    ap.add_argument("--lr", type=float, default=3e-4)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--on-policy-after", type=int, default=150)
    ap.add_argument("--eval-every", type=int, default=100)
    ap.add_argument("--eval-n", type=int, default=40)
    ap.add_argument("--device", default="mps" if
                    torch.backends.mps.is_available() else "cpu")
    ap.add_argument("--out", default=None)
    ap.add_argument("--smoke", action="store_true",
                    help="pipeline smoke test: smoke scale, short run")
    args = ap.parse_args()
    if args.smoke:
        args.scale, args.eval_every = "smoke", 100
    run(args)


if __name__ == "__main__":
    main()
