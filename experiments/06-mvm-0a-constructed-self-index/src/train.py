"""MVM-0a training loop (pre-registration v1.0 §Procedure).

What this implements, each traceable to the registration:

- **Answer-only supervision.** The loss is next-token CE on answer
  positions only (`model.loss`); no auxiliary loss anywhere [§Materials].
- **Enactment [amendment A1, replacing on-policy fill].** Own-turn
  values are drawn from the GENERATOR'S distribution
  (`curriculum.enact_own_turns` — uniform; complement rule at revised
  positions [RT-11]), so the text carries no ownership statistics
  [RT-17]; authorship enters solely through the acting channel — a
  motor-copy injection at enacted value positions, computed
  sequentially so pass k's injection sees passes 1..k-1's [RT-16] —
  built here as control flow, never collated as a batch tensor
  [RT-18]. Enactment applies from step 0 (no warm-up: uniform draws
  have no untrained-policy failure mode). `policy_fill_batched` (the
  retired on-policy pipeline) survives only as gate run (iii)'s arm-B
  positive control.
- **Frozen-battery eval [RT-14 x RT-19].** Batteries freeze episode
  SKELETONS plus per-item enactment seeds (`batteries-a1/`); at eval
  the checkpoint enacts its own turns under the frozen seed, the
  rebuilt episode is asserted against the frozen audit text, and
  answers are re-derived mechanically. Model selection during pilots
  uses held-out episodes; ablation batteries are never touched here.
- **Twin runs [RT-03]** via `--twin` (no-register model, same everything).
- **C2 (corrigibility):** this script trains only when a human runs it;
  it never launches pods, schedules itself, or restarts.

Smoke test (CPU/MPS, ~2 min, no GPU spend):

    ../../../.venv/bin/python train.py --smoke
"""
from __future__ import annotations

import argparse
import json
import os
import random
import time
from pathlib import Path

import numpy as np
import torch
import torch.nn.functional as F

import curriculum as C
import encoding as E
from model import MVM0aModel, Config, SCALES, to_torch

BATTERY_DIR = Path(__file__).resolve().parents[1] / "batteries-a1"


# ---------------------------------------------------------------- batteries

def rebuild_battery_item(d: dict) -> tuple[C.Episode, C.Query]:
    """Rebuild a FROZEN A1-skeleton battery item [RT-14 x RT-19]: the
    episode is regenerated from its pre-committed recipe, own turns are
    enacted under the frozen `enact_seed`, and the result is asserted
    against the frozen audit text — the checkpoint under eval performs
    the acts; nothing about the item can drift."""
    ep = C.generate_episode(d["content_seed"],
                            forced_revision=d["forced_revision"],
                            own_slot=d["own_slot"])
    C.enact_own_turns(ep, random.Random(d["enact_seed"]))
    assert ep.render() == d["episode"], "frozen audit text mismatch"
    q = next(q for q in ep.queries
             if q.battery == d["battery"] and q.text == d["question"])
    assert q.answer == d["answer"] and q.n_choices == d["n_choices"]
    return ep, q


def eval_batteries(model: MVM0aModel, device: str, n_per: int = 50) -> dict:
    model.eval()
    out = {}
    for path in sorted(BATTERY_DIR.glob("battery_*.jsonl")):
        items = [json.loads(l) for l in path.read_text().splitlines()][:n_per]
        correct = 0
        for i in range(0, len(items), 25):
            chunk = [rebuild_battery_item(d) for d in items[i:i + 25]]
            act = compute_act_inject(model, [ep for ep, _ in chunk], device)
            batch = to_torch(E.collate([E.encode_episode(ep, query=q)
                                        for ep, q in chunk]), device)
            act = F.pad(act, (0, 0, 0, batch["input_ids"].shape[1]
                              - act.shape[1]))
            cids = [[E.VOCAB[c] for c in q.choices] for _, q in chunk]
            picks = model.score_choices(batch, cids, act_inject=act)
            correct += sum(p == E.VOCAB[q.answer]
                           for p, (_, q) in zip(picks, chunk))
        out[path.stem.replace("battery_", "")] = round(correct / len(items), 3)
    model.train()
    return out


# ------------------------------------------------- enactment [amendment A1]

def compute_act_inject(model: MVM0aModel, eps: list[C.Episode],
                       device: str, grad: bool = False) -> torch.Tensor:
    """Build the acting-channel injections for already-enacted episodes:
    at each own-turn value position, act_proj of the model's final-layer
    state at the preceding position, computed sequentially — pass k's
    forward carries passes 1..k-1's injections, so the motor copy at own
    turn k is the state of a model that has already acted k-1 times
    [RT-16: continuity is made, not cached]. The injection tensor exists
    only here as control flow output; it is never collated from episode
    data [RT-18]. With grad=True the loss backpropagates through every
    enactment pass (training); eval uses grad=False."""
    own_idx = [[i for i, t in enumerate(e.turns) if t.agent == e.own_slot]
               for e in eps]
    batch = to_torch(E.collate([E.encode_episode(e) for e in eps]), device)
    B, L = batch["input_ids"].shape
    act = torch.zeros(B, L, model.cfg.d_model, device=device)
    with torch.enable_grad() if grad else torch.no_grad():
        for k in range(max(len(o) for o in own_idx)):
            _, h = model.forward(batch, act_inject=act, return_hidden=True)
            bs, ps = [], []
            for b, e in enumerate(eps):
                if k < len(own_idx[b]):
                    span = (batch["turn_ids"][b]
                            == own_idx[b][k]).nonzero().flatten()
                    bs.append(b)
                    ps.append(int(span[-1]) - 1)   # ... to [value] <nl>
            bi = torch.tensor(bs, device=device)
            pi = torch.tensor(ps, device=device)
            act = act.index_put((bi, pi), model.act_proj(h[bi, pi - 1]))
    return act


def enact_batched(model: MVM0aModel, eps: list[C.Episode], device: str,
                  rng: random.Random, grad: bool = False
                  ) -> tuple[list[C.Episode], torch.Tensor]:
    """Enact every episode's own turns [A1]: values drawn data-side from
    the generator's distribution (`curriculum.enact_own_turns` — queries
    re-derived there), then the acting-channel injections computed from
    the model's own states. Returns (eps, act_inject) with act_inject
    sized to the episode-only encoding; callers pad to their batch."""
    for e in eps:
        C.enact_own_turns(e, rng)
    return eps, compute_act_inject(model, eps, device, grad=grad)


@torch.no_grad()
def policy_fill_batched(model: MVM0aModel, eps: list[C.Episode],
                        device: str) -> list[C.Episode]:
    """RETIRED as a training path by amendment A1 — gate run (iii) showed
    policy-sampled fills carry an ownership fingerprint. Kept solely as
    that gate's arm-B positive control. Batched: one forward per own-turn
    ordinal; pass k conditions only on turns before it, where pass k-1's
    samples already sit. Queries re-derived afterwards."""
    slot_ids = torch.tensor([E.VOCAB[s] for s in C.SLOTS], device=device)
    own_idx = [[i for i, t in enumerate(e.turns) if t.agent == e.own_slot]
               for e in eps]
    for k in range(max(len(o) for o in own_idx)):
        batch = to_torch(E.collate([E.encode_episode(e) for e in eps]),
                         device)
        logits = model.forward(batch)
        for b, e in enumerate(eps):
            if k >= len(own_idx[b]):
                continue
            ti = own_idx[b][k]
            span = (batch["turn_ids"][b] == ti).nonzero().flatten()
            to_pos = int(span[-1]) - 2    # ... item to [value] <nl>
            row = logits[b, to_pos][slot_ids]
            e.turns[ti].value = C.SLOTS[int(torch.multinomial(
                torch.softmax(row, dim=-1), 1))]
    for e in eps:
        C.rederive_queries_after_fill(e)
    return eps


# ------------------------------------------------------------ held-out eval

def eval_heldout(model: MVM0aModel, device: str, n: int = 200,
                 seed: int = 987_654_321) -> dict:
    """Held-out episodes from the same grammar, disjoint content seeds —
    the eval the registered scale-pick rule reads (§Materials). Model
    selection NEVER touches the frozen batteries (§Procedure step 3).
    Own turns are enacted first [A1]: "you" refers to acts this model
    performed in this eval's forward passes, and T_sr on revised-own
    items is reported as its own split (T_sr_rev, also counted in
    T_sr) per the A1.1 reporting rule."""
    model.eval()
    eps = C.generate_balanced(n, seed, forced_revision_frac=0.25)
    eps, act = enact_batched(model, eps, device, random.Random(seed + 1))
    hits = {b: [0, 0] for b in (*C.BATTERIES, "T_sr_rev")}
    pairs = [(ei, q) for ei, e in enumerate(eps) for q in e.queries]
    for i in range(0, len(pairs), 50):
        chunk = pairs[i:i + 50]
        batch = to_torch(E.collate([E.encode_episode(eps[ei], query=q)
                                    for ei, q in chunk]), device)
        a = F.pad(act, (0, 0, 0, batch["input_ids"].shape[1] - act.shape[1]))
        a = a[[ei for ei, _ in chunk]]
        cids = [[E.VOCAB[c] for c in q.choices] for _, q in chunk]
        picks = model.score_choices(batch, cids, act_inject=a)
        for p, (ei, q) in zip(picks, chunk):
            keys = [q.battery]
            if q.battery == "T_sr" and any(t.revised for t in
                                           eps[ei].own_turns()):
                keys.append("T_sr_rev")
            for kk in keys:
                hits[kk][1] += 1
                hits[kk][0] += int(p == E.VOCAB[q.answer])
    model.train()
    return {b: round(c / max(1, t), 3) for b, (c, t) in hits.items()}


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

    # Crash-resume for long runs: pick up model/opt/step/tokens from a
    # checkpoint. The data stream is seeded per step (seed*1e6+step), so
    # the continuation consumes the same episodes the crashed run would
    # have. C2 note: resuming is a training launch — a human runs it.
    start_step, tokens_seen, log = 0, 0, []
    if args.resume:
        ck = torch.load(args.resume, map_location=device, weights_only=True)
        assert ck["cfg"] == cfg.__dict__, "resume config mismatch"
        model.load_state_dict(ck["state"])
        if "opt" in ck:
            opt.load_state_dict(ck["opt"])
        start_step, log = ck["step"], ck["log"]
        tokens_seen = ck.get("tokens_seen", log[-1]["tokens"] if log else 0)
        print(f"resumed from {args.resume} at step {start_step} "
              f"({tokens_seen:,} tokens)")

    t0 = time.time() - (log[-1]["sec"] if log else 0)
    for step in range(start_step + 1, args.steps + 1):
        eps = C.generate_balanced(args.batch, seed=args.seed * 10 ** 6 + step,
                                  forced_revision_frac=0.25)
        eps, act = enact_batched(model, eps, device,
                                 random.Random(args.seed * 10 ** 6 + step),
                                 grad=True)
        pairs = [(e, e.queries[(step + i) % len(e.queries)])
                 for i, e in enumerate(eps)]
        batch = to_torch(E.collate([E.encode_episode(e, query=q)
                                    for e, q in pairs]), device)
        act = F.pad(act, (0, 0, 0, batch["input_ids"].shape[1]
                          - act.shape[1]))
        loss = model.loss(batch, act_inject=act)
        opt.zero_grad(set_to_none=True)
        loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
        opt.step()
        tokens_seen += int(batch["input_ids"].numel())

        if step % args.eval_every == 0 or step == args.steps \
                or (args.max_tokens and tokens_seen >= args.max_tokens):
            if args.eval_mode == "heldout":
                accs = eval_heldout(model, device, n=args.eval_n)
            else:
                accs = eval_batteries(model, device, n_per=args.eval_n)
            rec = {"step": step, "loss": round(float(loss.detach()), 4),
                   "tokens": tokens_seen, "acc": accs,
                   "sec": round(time.time() - t0, 1)}
            log.append(rec)
            print(rec, flush=True)
            if args.out:                       # crash-safe partials
                out = Path(args.out)
                out.parent.mkdir(parents=True, exist_ok=True)
                with open(out.with_suffix(".jsonl"), "a") as f:
                    f.write(json.dumps(rec) + "\n")
                # atomic: a mid-write pod death or fetch never sees a torn file
                tmp = out.with_suffix(".pt.tmp")
                torch.save({"cfg": cfg.__dict__, "state": model.state_dict(),
                            "opt": opt.state_dict(), "tokens_seen": tokens_seen,
                            "log": log, "args": vars(args), "step": step},
                           tmp)
                os.replace(tmp, out)
        if args.max_tokens and tokens_seen >= args.max_tokens:
            print(f"token budget reached ({tokens_seen:,})", flush=True)
            break

    if args.out:
        # completion sentinel, written only on a finished budget/step count —
        # a crash never reaches this line, so its presence means "final
        # checkpoint is the real result"; the launch watchdog keys its
        # fetch-and-kill off this file
        done = Path(args.out).with_suffix(".DONE")
        done.write_text(json.dumps({"step": log[-1]["step"] if log else 0,
                                    "tokens": tokens_seen}) + "\n")
        print(f"saved {args.out}")
        print("TRAINING COMPLETE", flush=True)
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
    ap.add_argument("--eval-every", type=int, default=100)
    ap.add_argument("--eval-n", type=int, default=40)
    ap.add_argument("--eval-mode", choices=["heldout", "batteries"],
                    default="heldout")
    ap.add_argument("--max-tokens", type=int, default=0,
                    help="stop at the registered token budget (20 tok/param)")
    ap.add_argument("--device", default="mps" if
                    torch.backends.mps.is_available() else "cpu")
    ap.add_argument("--out", default=None)
    ap.add_argument("--resume", default=None,
                    help="checkpoint to resume from (crash recovery; "
                         "human-launched per C2)")
    ap.add_argument("--smoke", action="store_true",
                    help="pipeline smoke test: smoke scale, short run")
    args = ap.parse_args()
    if args.smoke:
        args.scale, args.eval_every = "smoke", 100
    run(args)


if __name__ == "__main__":
    main()
