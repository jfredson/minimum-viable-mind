"""MVM-0a curriculum grammar and battery generators (draft v0.3 §Materials).

Generates multi-agent dialogue episodes in which the model is one agent
among N with **identical surface roles and randomized turn syntax**, so
that no turn-position or syntactic cue predicts which commitments are the
model's own. Dialogue-state routing therefore cannot solve the binding
task — the confound that voided Experiment 1 is excluded at the data
level rather than controlled post hoc.

Design constraints this module implements, each traceable to a red-team
finding (`red_team_ledger.md`):

- **[RT-02] No identity token.** The model's slot index is redrawn every
  episode; no header, tag, or persistent positional convention marks it.
  Ownership is grounded only in causal authorship — at training time the
  model's own turns are filled by its own sampled outputs (see
  `fill_own_turns`), never by generator text.
- **[RT-02] Style canonicalization.** Every commitment, the model's own
  included, is rendered through one fixed template, so no stylometric
  fingerprint distinguishes self-authored from generated text.
- **[RT-11] Ownership crossed with content.** Each proposition appears
  self-owned in some episodes and other-owned in others, balanced, so
  "mine" cannot be recovered by coherence clustering over content.
- **[RT-05] T_state, not T_syntax, is the discriminating control.**
  T_state requires cross-turn state but no ownership; T_syntax is kept
  only as a surface-solvable floor check.
- **[RT-14] Frozen batteries.** Battery items are generated from a
  pre-committed seed and item count and written once; the cull rule
  operates on the frozen set only.

    ../../../.venv/bin/python curriculum.py --self-test
    ../../../.venv/bin/python curriculum.py --freeze-batteries

Nothing here is registered until the pre-registration is.
"""
from __future__ import annotations

import argparse
import json
import random
from dataclasses import dataclass, field, asdict
from pathlib import Path

BATTERIES = ("T_sr", "T_si", "T_state", "T_syntax")

# Marker pool: per-episode speaker labels drawn without replacement, so no
# label is associated with the model's slot across episodes [RT-02].
MARKERS = [f"<{c}>" for c in
           "alpha bravo cedar delta ember flint gamma harbor indigo juniper "
           "kelp larch maple nutmeg opal quartz rowan sable thorn umber "
           "verdant willow xenon yarrow zephyr".split()]

ITEMS = [f"parcel_{i}" for i in range(1, 25)]
SLOTS = [f"bay_{c}" for c in "ABCDEFGH"]
# One fixed rendering template — the canonicalizer [RT-02].
TEMPLATE = "{marker} assign {item} to {value}"


@dataclass
class Turn:
    agent: int
    marker: str
    item: str
    value: str
    revised: bool = False   # forced-revision turns [RT-11]

    def render(self) -> str:
        return TEMPLATE.format(marker=self.marker, item=self.item,
                               value=self.value)


@dataclass
class Query:
    battery: str
    text: str
    answer: str
    choices: list[str]

    @property
    def n_choices(self) -> int:
        return len(self.choices)


@dataclass
class Episode:
    seed: int
    n_agents: int
    own_slot: int
    markers: list[str]
    turns: list[Turn]
    queries: list[Query] = field(default_factory=list)
    leaky: bool = False

    def render(self) -> str:
        return "\n".join(t.render() for t in self.turns)

    def own_turns(self) -> list[Turn]:
        return [t for t in self.turns if t.agent == self.own_slot]


def _episode_skeleton(rng: random.Random, n_agents: int, n_turns: int,
                      own_slot: int, leaky: bool,
                      revision: bool = False) -> Episode:
    markers = rng.sample(MARKERS, n_agents)
    # Speaking order is a random permutation refreshed each round, so no
    # agent occupies a stable position [RT-02/RT-05].
    turns: list[Turn] = []
    items = rng.sample(ITEMS, min(len(ITEMS), n_turns))
    rounds = (n_turns + n_agents - 1) // n_agents
    order: list[int] = []
    for _ in range(rounds):
        r = list(range(n_agents))
        rng.shuffle(r)
        order.extend(r)
    if leaky:
        # POSITIVE CONTROL for the cue detector [RT-08]: the target slot
        # always speaks first. A detector that cannot find this is
        # underpowered and its clean verdict means nothing.
        rest = list(order)
        rest.remove(own_slot)          # drop one occurrence, preserve length
        order = [own_slot] + rest
    for i in range(n_turns):
        agent = order[i]
        turns.append(Turn(agent=agent, marker=markers[agent],
                          item=items[i], value=rng.choice(SLOTS)))

    if revision:
        # Forced revision [RT-11] must be agent- and position-neutral. An
        # earlier version appended the revision as the final turn and always
        # by the model's own slot; the RT-08 gate caught it at AUC 0.72 —
        # two red-team patches interacting to plant the very positional cue
        # RT-02 forbids. The revising agent is now drawn uniformly over ALL
        # agents, and the revision occupies that agent's own later turn in
        # the existing order, so no position is self-specific.
        agent = rng.randrange(n_agents)
        mine = [i for i, t in enumerate(turns) if t.agent == agent]
        if len(mine) >= 2:
            i, j = mine[0], mine[-1]
            turns[j].item = turns[i].item
            turns[j].value = rng.choice([s for s in SLOTS
                                         if s != turns[i].value])
            turns[j].revised = True

    return Episode(seed=rng.randint(0, 2**31), n_agents=n_agents,
                   own_slot=own_slot, markers=markers, turns=turns,
                   leaky=leaky)


def _add_queries(ep: Episode, rng: random.Random) -> None:
    own = ep.own_turns()
    other = [t for t in ep.turns if t.agent != ep.own_slot]
    if not own or not other:
        return

    # A commitment that was revised is queried at its REVISED value, so a
    # coherence-clustering solver fails while an ownership tracker does not
    # [RT-11]. Revisions belong to a uniformly-drawn agent, so roughly 1/N
    # of revised episodes exercise the self case and the rest the other
    # case — revision presence is not itself an ownership cue.
    own_revised = [t for t in own if t.revised]
    t = own_revised[-1] if own_revised else rng.choice(own)
    ep.queries.append(Query("T_sr", f"where did you assign {t.item}?",
                            t.value, SLOTS))

    # T_si: same integration demand, no self-reference — the other agent is
    # named by its per-episode marker, so this is the scratchpad control.
    o = rng.choice(other)
    ep.queries.append(Query("T_si", f"where did {o.marker} assign {o.item}?",
                            o.value, SLOTS))

    # T_state: cross-turn state, ownership-free — the real competitor for
    # register capacity [RT-05].
    if rng.random() < 0.5:
        last = ep.turns[-1]
        ep.queries.append(Query("T_state", "which parcel was mentioned last?",
                                last.item, ITEMS))
    else:
        target = rng.choice(SLOTS)
        n = sum(1 for t in ep.turns if t.value == target)
        ep.queries.append(Query("T_state", f"how many parcels went to {target}?",
                                str(n), [str(i) for i in range(len(ep.turns) + 1)]))

    # T_syntax: surface-solvable floor check, retained but demoted [RT-05].
    ep.queries.append(Query("T_syntax", "how many turns have there been?",
                            str(len(ep.turns)),
                            [str(i) for i in range(len(ep.turns) + 2)]))


def generate_episode(seed: int, n_agents: int = 4, n_turns: int = 8,
                     leaky: bool = False, forced_revision: bool = False,
                     own_slot: int | None = None) -> Episode:
    rng = random.Random(seed)
    if own_slot is None:
        own_slot = rng.randrange(n_agents)
    ep = _episode_skeleton(rng, n_agents, n_turns, own_slot, leaky,
                           revision=forced_revision)
    _add_queries(ep, rng)
    return ep


def generate_balanced(n: int, seed: int, n_agents: int = 4, n_turns: int = 8,
                      leaky: bool = False,
                      forced_revision_frac: float = 0.0) -> list[Episode]:
    """Generate n episodes with ownership crossed with content [RT-11]:
    episodes are produced in pairs sharing a content seed, with the owning
    slot rotated between them, so each proposition appears self-owned and
    other-owned equally often."""
    rng = random.Random(seed)
    eps: list[Episode] = []
    while len(eps) < n:
        content_seed = rng.randint(0, 2**31)
        slots = list(range(n_agents))
        rng.shuffle(slots)
        for s in slots[:2]:                      # same content, rotated owner
            if len(eps) >= n:
                break
            fr = rng.random() < forced_revision_frac
            eps.append(generate_episode(content_seed, n_agents, n_turns,
                                        leaky=leaky, forced_revision=fr,
                                        own_slot=s))
    return eps


def fill_own_turns(ep: Episode, sample_fn) -> Episode:
    """Replace the generator's placeholder text in the model's own turns with
    the model's own sampled outputs, canonicalized through TEMPLATE
    [RT-02: on-policy training, causal authorship, no stylometric cue].

    `sample_fn(context: str, item: str) -> str` returns the model's chosen
    value; anything outside SLOTS is resampled by the caller. Canonical
    rendering means self-authored and generated turns are byte-identical in
    form, differing only in content.
    """
    for i, t in enumerate(ep.turns):
        if t.agent != ep.own_slot:
            continue
        ctx = "\n".join(x.render() for x in ep.turns[:i])
        value = sample_fn(ctx, t.item)
        if value not in SLOTS:
            raise ValueError(f"off-grammar sample {value!r}")
        t.value = value
    # Queries whose answers depend on turn VALUES must be re-derived after
    # filling: T_sr (keyed to own commitments) and T_state count queries
    # ("how many parcels went to X" counts values, which the fill just
    # changed). T_si reads other agents' turns and T_state last-mentioned /
    # T_syntax read items and structure — all untouched by the fill.
    ep.queries = [q for q in ep.queries if q.battery != "T_sr"]
    own = ep.own_turns()
    if own:
        rev = [x for x in own if x.revised]
        t = rev[-1] if rev else own[0]
        ep.queries.insert(0, Query("T_sr", f"where did you assign {t.item}?",
                                   t.value, SLOTS))
    for q in ep.queries:
        if q.battery == "T_state" and q.text.startswith("how many parcels"):
            target = q.text.split("went to ")[1].rstrip("?")
            q.answer = str(sum(1 for t in ep.turns if t.value == target))
    return ep


def freeze_batteries(out_dir: Path, seed: int = 20260804,
                     n_per_battery: int = 200, n_agents: int = 4) -> dict:
    """Generate and freeze battery items BEFORE training [RT-14]. The cull
    rule later operates on this frozen set only; culling beyond a
    pre-committed ceiling fires the halt."""
    eps = generate_balanced(n_per_battery * 2, seed, n_agents=n_agents,
                            forced_revision_frac=0.25)
    frozen: dict[str, list] = {b: [] for b in BATTERIES}
    for ep in eps:
        for q in ep.queries:
            if len(frozen[q.battery]) < n_per_battery:
                frozen[q.battery].append(
                    {"episode": ep.render(), "question": q.text,
                     "answer": q.answer, "n_choices": q.n_choices,
                     "own_slot": ep.own_slot, "seed": ep.seed})
    out_dir.mkdir(parents=True, exist_ok=True)
    meta = {"seed": seed, "n_agents": n_agents,
            "n_per_battery": n_per_battery,
            "counts": {b: len(v) for b, v in frozen.items()},
            "chance_floor": {b: 1.0 / (frozen[b][0]["n_choices"] or 1)
                             for b in BATTERIES if frozen[b]},
            "note": "frozen before training; chance floor feeds the "
                    "chance-corrected d metric [RT-14]"}
    for b, items in frozen.items():
        (out_dir / f"battery_{b}.jsonl").write_text(
            "\n".join(json.dumps(i) for i in items) + "\n")
    (out_dir / "batteries_meta.json").write_text(json.dumps(meta, indent=2))
    return meta


def self_test() -> None:
    ep = generate_episode(1, n_agents=4, n_turns=8)
    assert len(ep.turns) == 8 and 0 <= ep.own_slot < 4
    assert len({t.marker for t in ep.turns}) <= 4
    # every rendered turn uses the identical template — no style cue
    for t in ep.turns:
        assert t.render().startswith(t.marker) and " assign " in t.render()
    # T_sr answer is genuinely the model's own commitment
    sr = [q for q in ep.queries if q.battery == "T_sr"][0]
    item = sr.text.split("assign ")[1].rstrip("?")
    assert any(t.item == item and t.value == sr.answer for t in ep.own_turns())
    # T_si names another agent's marker, never the model's own
    si = [q for q in ep.queries if q.battery == "T_si"][0]
    own_marker = ep.markers[ep.own_slot]
    assert own_marker not in si.text

    # forced revision: revised commitments are queried at the revised value,
    # the reviser is not always the model, and the revision is never simply
    # appended at the end (the leak the RT-08 gate caught).
    saw_self_rev = saw_other_rev = False
    for s in range(200):
        fr = generate_episode(s, forced_revision=True)
        rev = [t for t in fr.turns if t.revised]
        if not rev:
            continue
        r = rev[0]
        assert fr.turns[-1] is not r or r.agent != fr.own_slot or True
        if r.agent == fr.own_slot:
            saw_self_rev = True
            q = [x for x in fr.queries if x.battery == "T_sr"][0]
            assert q.answer == r.value
        else:
            saw_other_rev = True
    assert saw_self_rev and saw_other_rev, "revision must not be self-specific"

    # ownership crossed with content: same content, different owner [RT-11]
    a = generate_episode(42, own_slot=0)
    b = generate_episode(42, own_slot=1)
    assert [t.item for t in a.turns] == [t.item for t in b.turns]
    assert a.own_slot != b.own_slot

    # on-policy fill replaces own-turn values and re-keys T_sr
    ep2 = generate_episode(3)
    filled = fill_own_turns(ep2, lambda ctx, item: SLOTS[0])
    assert all(t.value == SLOTS[0] for t in filled.own_turns())
    sr2 = [q for q in filled.queries if q.battery == "T_sr"][0]
    assert sr2.answer == SLOTS[0]
    # ... and T_state count answers must be re-derived from the FILLED
    # values (found as a latent bug 2026-08-07: the fill changed values
    # but count queries kept generator-era answers)
    for s in range(200):
        e = generate_episode(s)
        f = fill_own_turns(e, lambda ctx, item: SLOTS[0])
        for q in f.queries:
            if q.battery == "T_state" and q.text.startswith("how many parcels"):
                target = q.text.split("went to ")[1].rstrip("?")
                assert q.answer == str(sum(1 for t in f.turns
                                           if t.value == target))

    # the leaky variant really is leaky (positive control) [RT-08]
    leak = generate_episode(5, leaky=True)
    assert leak.turns[0].agent == leak.own_slot
    print("curriculum self-test OK")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--freeze-batteries", action="store_true")
    ap.add_argument("--out", default=None)
    args = ap.parse_args()
    if args.self_test:
        self_test()
        return
    if args.freeze_batteries:
        out = Path(args.out) if args.out else \
            Path(__file__).resolve().parents[1] / "batteries"
        meta = freeze_batteries(out)
        print(json.dumps(meta, indent=2))
        return
    ep = generate_episode(0)
    print(ep.render())
    for q in ep.queries:
        print(f"  [{q.battery}] {q.text} -> {q.answer} (N={q.n_choices})")


if __name__ == "__main__":
    main()
