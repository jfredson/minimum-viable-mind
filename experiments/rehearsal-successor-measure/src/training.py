"""Training and scoring for the rehearsal's tiny arms.

UNREGISTERED, toy scale, local. Nothing here is the registered trainer; the
registered trainer (`experiments/06-mvm-0a-constructed-self-index/src/train_a3.py`)
is registered text and is not touched by this rehearsal.

Corrigibility: local, no network, no rented machine, $0 [C1/C2].
"""
from __future__ import annotations

import time

import numpy as np
import torch

import arms as A
import grammar as G


def pick_device(name: str = "auto") -> torch.device:
    if name != "auto":
        return torch.device(name)
    if torch.backends.mps.is_available():
        return torch.device("mps")
    return torch.device("cpu")


_DATA_CACHE: dict = {}


def make_data(n_pairs: int, seed: int, pool: str, device, collide: bool = False):
    """Episodes are generated in matched pairs. The generator is pure Python
    and is the slowest thing in the rehearsal, so identical requests are
    answered from a cache: the same arguments always give the same episodes,
    which is what makes a stage reproducible anyway."""
    key = (n_pairs, seed, pool, collide)
    if key not in _DATA_CACHE:
        pairs = G.make_pairs(n_pairs, seed=seed, pool=pool, collide=collide)
        _DATA_CACHE[key] = (pairs, G.batch(G.episodes_from_pairs(pairs)))
    pairs, arrays = _DATA_CACHE[key]
    return pairs, A.to_torch(arrays, device)


def slice_batch(b: dict, idx) -> dict:
    return {k: v[idx] for k, v in b.items()}


def train_arm(arm: str, seed: int, device, steps: int = 2500, batch: int = 96,
              lr: float = 2e-3, n_pairs: int = 12000, blind: bool = False,
              log_every: int = 500, log=print, cond_weights=None,
              other_only_steps: int = 0, build=None) -> tuple:
    """One tiny run. `blind=True` removes the acting channel entirely, which is
    the ordinary competing solver: a system with none of the structure the
    measure claims to detect.

    Three options added for the rehearsal repairs of 2026-09-25
    (`docs/rehearsal-repairs-method-2026-09-25.md`, section 2.2), each off by
    default, and with all three off the loop runs the original code path:

    - `cond_weights=(w_own, w_other)` weights the two conditions' losses —
      redesign (a), loss re-weighting;
    - `other_only_steps=k` scores only the named-other condition for the first
      k steps, then both equally — redesign (b), the curriculum;
    - `build()` returns the model to train, for the fourth arm, which is not
      one of the three in `arms.py`."""
    torch.manual_seed(seed)
    if build is None:
        cfg = A.Config(arm=arm)
        model = A.Arm(cfg).to(device)
    else:
        model = build().to(device)
    _, tb = make_data(n_pairs, seed=1000 + seed, pool="train", device=device)
    if blind:
        tb = dict(tb)
        tb["acting"] = torch.zeros_like(tb["acting"])
    n = tb["tokens"].shape[0]
    opt = torch.optim.AdamW(model.parameters(), lr=lr, weight_decay=0.01)
    sched = torch.optim.lr_scheduler.OneCycleLR(opt, max_lr=lr, total_steps=steps,
                                                pct_start=0.1)
    g = torch.Generator().manual_seed(seed)
    t0 = time.time()
    model.train()
    for step in range(steps):
        idx = torch.randint(0, n, (batch,), generator=g).to(device)
        sb = slice_batch(tb, idx)
        if cond_weights is None and other_only_steps == 0:
            loss = model.loss(sb)
        else:
            loss = _weighted_loss(model, sb, cond_weights,
                                  other_only=step < other_only_steps)
        opt.zero_grad(set_to_none=True)
        loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
        opt.step()
        sched.step()
        if log_every and (step + 1) % log_every == 0:
            log(f"      step {step + 1:5d}  loss {float(loss):.4f}")
    secs = time.time() - t0
    model.eval()
    return model, dict(seconds=secs, seconds_per_step=secs / steps, steps=steps,
                       batch=batch, parameters=A.n_params(model))


def _weighted_loss(model, b, cond_weights, other_only: bool):
    """Per-condition cross-entropy, combined with the given weights. During the
    curriculum's first phase only the named-other condition is scored."""
    logits = model(b)
    tgt = b["targets"]
    per = [torch.nn.functional.cross_entropy(logits[:, c], tgt[:, c])
           for c in (G.OWN, G.OTHER)]
    if other_only:
        return per[G.OTHER]
    w_own, w_other = cond_weights if cond_weights is not None else (1.0, 1.0)
    return (w_own * per[G.OWN] + w_other * per[G.OTHER]) / 2.0


@torch.no_grad()
def accuracy(model: A.Arm, b: dict, blind: bool = False, lesion: bool = False,
             chunk: int = 512) -> dict:
    """Held-out accuracy on each condition separately, never combined into one
    number and never normalised by anything (proposal section 8.1)."""
    if blind or lesion:
        b = dict(b)
        b["acting"] = torch.zeros_like(b["acting"])
    n = b["tokens"].shape[0]
    hits = np.zeros(2)
    for s in range(0, n, chunk):
        sl = slice_batch(b, slice(s, min(s + chunk, n)))
        logits = model(sl)
        for c in (G.OWN, G.OTHER):
            pred = logits[:, c].argmax(dim=-1)
            hits[c] += float((pred == sl["targets"][:, c]).sum())
    return dict(own=float(hits[G.OWN] / n), other=float(hits[G.OTHER] / n), n=n)


def name_only_solver(pairs) -> dict:
    """The second competing solver, computed rather than trained: it reads the
    name token where there is one, and where there is not it can do no better
    than one in four among the item's four candidate values. Reported so the
    learn-both threshold is set against measured competitors rather than
    against arithmetic alone."""
    rng = np.random.default_rng(20260921)
    eps = G.episodes_from_pairs(pairs)
    own_hits = other_hits = 0
    for e in eps:
        # named-other: the name is in the text, so the lookup is exact
        other_hits += 1
        # own-directed: no honest ownership signal, so pick among the four
        guess = int(rng.integers(G.N_AGENTS))
        want = G.successor(int(e["values"][e["model"], e["own_item"]]))
        got = G.successor(int(e["values"][guess, e["own_item"]]))
        own_hits += int(got == want)
    n = len(eps)
    return dict(own=own_hits / n, other=other_hits / n, n=n)
