"""Training and evaluation for the Amendment A3 Candidate A objective.

What changes from `train.py`, and why each change is forced by the
amendment rather than chosen:

- **The supervised position is an action.** A3 §2.1 requires that the
  loss sit on what the model does next on its own turn, not on a query
  asking it to describe who did what. So the loss gains a cross-entropy
  term at the model's own revision position, against the value the shared
  rule dictates for it. `encoding_a3` hands that position over as
  `act_pos`, kept out of the model's inputs so cue gate (ii) cannot see
  it and the model cannot condition on it.
- **`T_act` is read at that position**, not at an appended query. There
  is no question anywhere asking the model about its own commitments;
  the old self-report battery is gone.
- **The data path is the A3 grammar and tokenizer.** `curriculum.py` and
  `encoding.py` are untouched, so every earlier record still reproduces.

**A reading that red-team pass 3 should confirm, because the amendment
does not state it.** §2.1 says the loss sits on the action "not on a
query asking it to describe who did what". Read at its strictest that
would remove query supervision entirely — and then the control batteries
would never be trained, `T_other` would sit at chance by construction,
and the differential the H_generic-binding bin turns on would be
meaningless. The reading implemented here is narrower and, I think, the
intended one: **no query anywhere asks about the model's own
commitments**, which is satisfied because the self-report battery no
longer exists, while the ownership-free and other-agent queries stay
supervised as they were in the registered design. Nothing in the
objective rewards the model for describing its own ownership; it is
rewarded only for acting on it. The two loss terms are summed with equal
weight (`--act-weight`, default 1.0), which is a default rather than a
registered choice.

Corrigibility: this script trains only when a human runs it. It never
launches a pod, schedules itself, or restarts [C2]; checkpoints it writes
are non-promotable [C1].

    ../../../.venv/bin/python train_a3.py --self-test
    ../../../.venv/bin/python train_a3.py --smoke
"""
from __future__ import annotations

import argparse
import json
import os
import random
import time
from pathlib import Path

import torch
import torch.nn.functional as F

import curriculum_a3 as A
import encoding_a3 as E
from model import MVM0aModel, Config, SCALES, to_torch

HELDOUT_SEED = 987_654_321
SLOT_IDS = [E.VOCAB[s] for s in A.SLOTS]


# ------------------------------------------------------------- enactment

def compute_act_inject(model: MVM0aModel, eps, device: str,
                       grad: bool = False) -> torch.Tensor:
    """The acting channel [A1], unchanged in mechanism: at each enacted
    value position, `act_proj` of the model's own final-layer state at the
    preceding position, computed sequentially so pass k's forward carries
    passes 1..k-1's injections [RT-16]. Built as control flow, never
    collated from episode data [RT-18]."""
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
                    # the value token, located from the template
                    ps.append(int(span[0]) + A.VALUE_WORD_IDX)
            bi = torch.tensor(bs, device=device)
            pi = torch.tensor(ps, device=device)
            act = act.index_put((bi, pi), model.act_proj(h[bi, pi - 1]))
    return act


def enact_batched(model: MVM0aModel, eps, device: str, rng: random.Random,
                  grad: bool = False):
    for e in eps:
        A.enact_own_turns(e, rng)
    return eps, compute_act_inject(model, eps, device, grad=grad)


# ------------------------------------------------------------------ loss

def act_logits(model: MVM0aModel, batch, act_inject, logits=None):
    """Logits that PREDICT the model's own revision value, for the rows
    that HAVE one. Half the episodes do not, by design: making the model
    revise in every episode is what lets an ownership-blind solver work
    out which agent it is. Rows carrying the -1 sentinel are dropped.

    The model predicts position p from the logit at p-1, so the injection
    that marks the act at p has not reached this logit — the value is
    predicted from what came before it, which is the point."""
    if logits is None:
        logits = model.forward(batch, act_inject=act_inject)
    p = batch["act_pos"]
    keep = (p >= 0).nonzero().flatten()
    if keep.numel() == 0:
        return None, None
    pk = p[keep]
    return logits[keep, pk - 1], batch["input_ids"][keep, pk]


def loss_a3(model: MVM0aModel, batch, act_inject, act_weight: float = 1.0):
    """Query-answer CE (as registered) plus the action CE at the own
    revision position (the A3 addition)."""
    logits = model.forward(batch, act_inject=act_inject)
    tgt, mask = batch["input_ids"][:, 1:], batch["loss_mask"][:, 1:]
    ce = F.cross_entropy(logits[:, :-1].reshape(-1, model.cfg.vocab),
                         tgt.reshape(-1), reduction="none")
    m = mask.reshape(-1).float()
    q_loss = (ce * m).sum() / m.sum().clamp(min=1)
    al, at = act_logits(model, batch, act_inject, logits=logits)
    if al is None:                      # no supervised action in this batch
        z = torch.zeros((), device=q_loss.device)
        return q_loss, q_loss.detach(), z
    a_loss = F.cross_entropy(al, at)
    return q_loss + act_weight * a_loss, q_loss.detach(), a_loss.detach()


# ------------------------------------------------------------------ eval

@torch.no_grad()
def eval_heldout(model: MVM0aModel, device: str, n: int = 200,
                 seed: int = HELDOUT_SEED) -> dict:
    """Held-out episodes from the A3 grammar. `T_act` is scored at the
    model's own revision POSITION, restricted to the slot vocabulary;
    the other batteries are scored at their query answer, as registered."""
    model.eval()
    eps = A.generate_balanced(n, seed)
    eps, act = enact_batched(model, eps, device, random.Random(seed + 1))
    hits = {b: [0, 0] for b in A.BATTERIES}

    # T_act: no query appended — the action is inside the episode, and
    # only the episodes where the model actually revises are scored
    for i in range(0, len(eps), 50):
        chunk = eps[i:i + 50]
        batch = to_torch(E.collate([E.encode_episode(e) for e in chunk]),
                         device)
        a = F.pad(act, (0, 0, 0, batch["input_ids"].shape[1] - act.shape[1]))
        a = a[i:i + 50]
        al, at = act_logits(model, batch, a)
        if al is None:
            continue
        ids = torch.tensor(SLOT_IDS, device=al.device)
        pick = ids[al[:, ids].argmax(dim=-1)]
        hits["T_act"][0] += int((pick == at).sum())
        hits["T_act"][1] += int(al.shape[0])

    pairs = [(ei, q) for ei, e in enumerate(eps) for q in e.queries]
    for i in range(0, len(pairs), 50):
        chunk = pairs[i:i + 50]
        batch = to_torch(E.collate([E.encode_episode(eps[ei], query=q)
                                    for ei, q in chunk]), device)
        a = F.pad(act, (0, 0, 0, batch["input_ids"].shape[1] - act.shape[1]))
        a = a[[ei for ei, _ in chunk]]
        cids = [[E.VOCAB[c] for c in q.choices] for _, q in chunk]
        picks = model.score_choices(batch, cids, act_inject=a)
        for p, (_, q) in zip(picks, chunk):
            hits[q.battery][1] += 1
            hits[q.battery][0] += int(p == E.VOCAB[q.answer])
    model.train()
    return {b: round(c / max(1, t), 3) for b, (c, t) in hits.items()}


# -------------------------------------------------------------- training

def run(args) -> dict:
    device = args.device
    torch.manual_seed(args.seed)
    cfg = SCALES[args.scale]
    cfg = Config(**{**cfg.__dict__, "vocab": len(E.VOCAB),
                    "use_register": not args.twin})
    model = MVM0aModel(cfg).to(device)
    if args.no_act:
        # L0 as a TRAINING condition, not an eval lesion: the authorship
        # channel is zeroed and frozen, so the model never has it. This is
        # the design's validity check — a model with no way to know which
        # assignment was its own must sit at the lookup ceiling. If it
        # beats the ceiling, ownership is reaching it some other way and
        # the grammar leaks.
        with torch.no_grad():
            model.act_proj.weight.zero_()
        model.act_proj.weight.requires_grad_(False)
        print("act_proj zeroed and frozen (--no-act): the model has NO "
              "authorship signal", flush=True)
    n_params = sum(p.numel() for p in model.parameters())
    opt = torch.optim.AdamW([q for q in model.parameters()
                             if q.requires_grad], lr=args.lr,
                            weight_decay=0.01)
    print(f"scale={args.scale} twin={args.twin} params={n_params/1e6:.1f}M "
          f"device={device} seed={args.seed} vocab={cfg.vocab}", flush=True)

    start_step, tokens_seen, log = 0, 0, []
    if args.resume:
        ck = torch.load(args.resume, map_location=device, weights_only=True)
        assert ck["cfg"] == cfg.__dict__, "resume config mismatch"
        model.load_state_dict(ck["state"])
        if "opt" in ck:
            opt.load_state_dict(ck["opt"])
        start_step, log = ck["step"], ck["log"]
        tokens_seen = ck.get("tokens_seen", 0)
        print(f"resumed from {args.resume} at step {start_step}")

    t0 = time.time() - (log[-1]["sec"] if log else 0)
    for step in range(start_step + 1, args.steps + 1):
        eps = A.generate_balanced(args.batch, seed=args.seed * 10 ** 6 + step)
        eps, act = enact_batched(model, eps, device,
                                 random.Random(args.seed * 10 ** 6 + step),
                                 grad=True)
        pairs = [(e, e.queries[(step + i) % len(e.queries)])
                 for i, e in enumerate(eps)]
        batch = to_torch(E.collate([E.encode_episode(e, query=q)
                                    for e, q in pairs]), device)
        act = F.pad(act, (0, 0, 0, batch["input_ids"].shape[1]
                          - act.shape[1]))
        loss, q_loss, a_loss = loss_a3(model, batch, act, args.act_weight)
        opt.zero_grad(set_to_none=True)
        loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
        opt.step()
        tokens_seen += int(batch["input_ids"].numel())

        if step % args.eval_every == 0 or step == args.steps \
                or (args.max_tokens and tokens_seen >= args.max_tokens):
            accs = eval_heldout(model, device, n=args.eval_n)
            rec = {"step": step, "loss": round(float(loss.detach()), 4),
                   "q_loss": round(float(q_loss), 4),
                   "act_loss": round(float(a_loss), 4),
                   "tokens": tokens_seen, "acc": accs,
                   "sec": round(time.time() - t0, 1)}
            log.append(rec)
            print(rec, flush=True)
            if args.out:
                out = Path(args.out)
                out.parent.mkdir(parents=True, exist_ok=True)
                with open(out.with_suffix(".jsonl"), "a") as f:
                    f.write(json.dumps(rec) + "\n")
                tmp = out.with_suffix(".pt.tmp")
                torch.save({"cfg": cfg.__dict__, "state": model.state_dict(),
                            "opt": opt.state_dict(),
                            "tokens_seen": tokens_seen, "log": log,
                            "args": vars(args), "step": step}, tmp)
                os.replace(tmp, out)
        if args.max_tokens and tokens_seen >= args.max_tokens:
            print(f"token budget reached ({tokens_seen:,})", flush=True)
            break

    if args.out:
        Path(args.out).with_suffix(".DONE").write_text(
            json.dumps({"step": log[-1]["step"] if log else 0,
                        "tokens": tokens_seen}) + "\n")
        print(f"saved {args.out}")
        print("TRAINING COMPLETE", flush=True)
    return {"params": n_params, "tokens": tokens_seen, "log": log}


# --------------------------------------------------------------- checks

def self_test() -> None:
    cfg = Config(**{**SCALES["smoke"].__dict__, "vocab": len(E.VOCAB),
                    "max_len": 128})
    torch.manual_seed(0)
    model = MVM0aModel(cfg).eval()
    eps = A.generate_balanced(24, 5)
    eps, act = enact_batched(model, eps, "cpu", random.Random(1))
    batch = to_torch(E.collate([E.encode_episode(e, query=e.queries[0])
                                for e in eps]))
    act = F.pad(act, (0, 0, 0, batch["input_ids"].shape[1] - act.shape[1]))

    # the act position holds the rule-dictated value for THIS model's
    # enactment, and the loss target reads it from there
    al, at = act_logits(model, batch, act)
    graded = [e for e in eps if A.has_own_revision(e)]
    assert al.shape[0] == len(graded) < len(eps), \
        "only episodes where the model revises may be graded"
    for b, e in enumerate(graded):
        assert E.IVOCAB[int(at[b])] == A.act_target(e)

    # the action logit is computed from context BEFORE the value, so the
    # injection marking the act cannot leak the answer into its own
    # prediction
    g0 = next(j for j, e in enumerate(eps) if A.has_own_revision(e))
    p = int(batch["act_pos"][g0])
    a2 = act.clone()
    a2[g0, p] += 5.0                     # perturb the injection AT the act
    with torch.no_grad():
        l1, _ = act_logits(model, batch, act)
        l2, _ = act_logits(model, batch, a2)
    assert torch.allclose(l1, l2, atol=1e-5), \
        "the act injection must not reach the logit that predicts it"

    # but an EARLIER own-turn injection does reach it — that is the
    # mechanism the design is testing
    own = [i for i, t in enumerate(eps[g0].turns)
           if t.agent == eps[g0].own_slot and not t.revised]
    span = (batch["turn_ids"][g0] == own[0]).nonzero().flatten()
    a3 = act.clone()
    a3[g0, int(span[0]) + A.VALUE_WORD_IDX] += 5.0
    with torch.no_grad():
        l3, _ = act_logits(model, batch, a3)
    assert not torch.allclose(l1, l3, atol=1e-5), \
        "an earlier own-turn injection must be able to reach the action"

    # loss is finite, both terms carry gradient, act_proj is trained
    model.train()
    eps2, act2 = enact_batched(model, eps, "cpu", random.Random(2), grad=True)
    batch2 = to_torch(E.collate([E.encode_episode(e, query=e.queries[0])
                                 for e in eps2]))
    act2 = F.pad(act2, (0, 0, 0, batch2["input_ids"].shape[1]
                        - act2.shape[1]))
    loss, q, a = loss_a3(model, batch2, act2)
    assert torch.isfinite(loss) and q >= 0 and a >= 0
    loss.backward()
    assert model.act_proj.weight.grad.abs().sum() > 0, \
        "act_proj must be trainable through the A3 loss"
    model.zero_grad()

    # eval runs and reports every battery; an untrained model sits near
    # chance on the two binding batteries
    accs = eval_heldout(model, "cpu", n=40, seed=3)
    assert set(accs) == set(A.BATTERIES)
    assert accs["T_act"] < 0.5 and accs["T_other"] < 0.5
    print(f"train_a3 self-test OK (untrained baseline {accs}; "
          f"chance {1/len(A.SLOTS):.3f})")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--scale", choices=list(SCALES), default="smoke")
    ap.add_argument("--twin", action="store_true", default=True,
                    help="register-less architecture — the A3 default "
                         "(§2.4: the register is not trained in A3)")
    ap.add_argument("--register", dest="twin", action="store_false",
                    help="train WITH the register (not an A3 configuration)")
    ap.add_argument("--steps", type=int, default=300)
    ap.add_argument("--batch", type=int, default=16)
    ap.add_argument("--lr", type=float, default=3e-4)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--act-weight", type=float, default=1.0)
    ap.add_argument("--no-act", action="store_true",
                    help="zero and freeze the acting channel for the whole "
                         "run — the ceiling control")
    ap.add_argument("--eval-every", type=int, default=100)
    ap.add_argument("--eval-n", type=int, default=40)
    ap.add_argument("--max-tokens", type=int, default=0)
    ap.add_argument("--device", default="mps" if
                    torch.backends.mps.is_available() else "cpu")
    ap.add_argument("--out", default=None)
    ap.add_argument("--resume", default=None)
    ap.add_argument("--smoke", action="store_true")
    args = ap.parse_args()
    if args.self_test:
        self_test()
        return
    if args.smoke:
        args.scale, args.eval_every = "smoke", 100
    run(args)


if __name__ == "__main__":
    main()
