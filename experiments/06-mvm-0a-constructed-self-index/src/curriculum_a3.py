"""The Amendment A3 Candidate A curriculum — "act as yourself".

A3 §2.2: the objective must make the correct output at a supervised
position depend on which agent the model is, must ground ownership only
in the act (the acting channel), and must supervise an action rather than
a report. This module builds that grammar. `curriculum.py` is left
byte-identical: every record in `lesion-results/` and `null-calibration/`
reproduces against it, and the five existing checkpoints were trained on
it.

The episode
-----------
Twelve turns, four agents, two *contested* items:

- **Eight assignment turns.** Each agent assigns each contested item
  exactly once, in one random permutation of the eight (agent, item)
  pairs. Within an item the four values are **distinct**, so an item's
  four assignments differ only in who made them.
- **Four revision turns**, last, in random order: **every agent revises
  exactly once**, two agents on each contested item, with the pairing
  drawn by a uniform shuffle.
- **The revision rule is deterministic and shared**: the revised value is
  the successor of *that agent's own earlier value on that item*, over
  the eight slots, modulo eight. Every agent obeys it; the generator
  applies it to the other agents and the enactment harness applies it to
  the model.

Every agent therefore has exactly three turns, two assignments and one
revision, and sits in the assignment block and the revision block equally
often. Nothing about how much an agent speaks, where, or whether it
revises can predict which agent the model is.

Why exactly one own revision per episode
---------------------------------------
Gate 0 measured the cost of the alternative. Under the registered
grammar the revision-conditioned battery harvests one scoring cell from
about one episode in twenty, so at 400 episodes it is a 19-item cell
whose null band is two items flipping
(`gate0-null-calibration-findings.md`, reading 2). A3 decision 12 sets
verdict cells at n=400. One own revision per episode is what makes 400
episodes yield 400 `T_act` cells instead of about 20.

Why *every* agent revises, which the first draft of this module got wrong
------------------------------------------------------------------------
The first version gave the model one revision and one other agent one
revision, and left the remaining two agents with assignments only. Its
own self-test killed it: the model's slot then always had three turns
while two other agents had two, so **agent turn count predicted
ownership perfectly** (3 turns for the model every time, against 0.43 of
other-agent turns), and revision status predicted it at 0.33 against
0.14. That is the same class of defect the registered grammar hit when a
red-team patch made the revision always final and always the model's
(`curriculum.py`, `_episode_skeleton`), and it is what gate (i) exists to
catch. Giving every agent exactly one revision removes both cues by
construction rather than by measurement.

What a solver without a self-index can do
-----------------------------------------
At its own revision turn the model sees four distinct earlier values for
that item and must emit the successor of its own. Position is randomised,
markers are a per-episode draw, and every agent's values come from the
same distribution, so nothing in the text distinguishes the four.

Two agents revise each item, so if the *other* agent revising the model's
item goes first, a solver can invert the rule on that revision and strike
one candidate. The model revises first half the time. **The lookup
ceiling is therefore 0.25 on half the cells and 0.333 on the other half,
0.292 overall**, against a chance floor of 0.125. That is above the 0.25
A3 §2.2 pre-states, and the discrepancy is real rather than cosmetic: it
is the price of making every agent revise, which is what removes the
ownership cue above. Red-team pass 3 should either adopt 0.292 as the
pre-stated ceiling or buy 0.25 back by adding a third contested item that
nobody revises, at about a third more compute per run.

**An honest limit on the design's central claim.** A3 §2.2 says the only
route from the ceiling to 1.0 is to have bound the act to the item when
acting and carried that binding forward. There is a second route. The
revision turn renders as "<marker> assign <item> to <value>", so at the
moment the model acts, its own marker is in the context three tokens
back. A model could learn "the marker at a position where I am acting is
mine", then retrieve that marker's earlier value by ordinary
marker-keyed lookup — reading a name badge at act time rather than
carrying a binding. Both routes need the acting channel and both collapse
under the L0 lesion, so L0 does not separate them. A3 already registers
the discriminator: the mid-episode re-indexing probe of the H_tag bin.
The claim in §2.2 should be narrowed to say so.

Batteries
---------
- **T_act** (primary, an action not a report): the value emitted at the
  model's own revision position. Chance 0.125, lookup ceiling 0.25.
  Carried on the episode as `act_target`, scored at that position.
- **T_other**: a forced-choice counterfactual naming another agent —
  "where did <marker> assign <item> to next ?" — on the contested item
  that agent did *not* revise, so the answer appears in no turn and must
  be computed from its earlier value. Same rule, same binding demand, no
  self-reference. Chance 0.125. Two of the item's four values are struck
  by the two revisions a solver can invert, so its lookup ceiling is
  0.5 — higher than T_act's, which red-team pass 3 should weigh, since
  the H_generic-binding bin turns on the difference between the two
  batteries' drops.
- **T_state**, **T_syntax**: unchanged in kind from the registered
  grammar (RT-05 competitor, and the floor check).

Corrigibility: this module generates data. It trains nothing, launches
nothing and costs nothing [C1/C2].

    ../../../.venv/bin/python curriculum_a3.py --self-test
"""
from __future__ import annotations

import argparse
import json
import random
from pathlib import Path

from dataclasses import dataclass

from curriculum import MARKERS, ITEMS, SLOTS, Query, Episode

# The A3 rendering: the speaker's name comes LAST, after the value.
#
# This is not cosmetic. Under the registered template the name comes
# first, so at the moment the model's own revision value is graded, its
# own name label sits three tokens back in its own context. An
# ownership-free solver that matches this turn's name and item against
# the earlier assignments and applies the rule then scores 1.000 — no
# self-index, no acting channel, nothing but text matching (red-team pass
# 3, RT-20; reproduced by `ownership_free_solver` below). The pre-stated
# shortcut ceiling was never a bound on ownership-blind solvers; it was
# the score of a solver forbidden from reading a name in plain sight.
#
# With the name last, the context at the graded position is
# "assign <item> to" and nothing more. Which of the item's four earlier
# values is the model's own is then recoverable ONLY from the acting
# channel, which is what A3 §2.1 requires.
TEMPLATE = "assign {item} to {value} by {marker}"
VALUE_WORD_IDX = TEMPLATE.split().index("{value}")


@dataclass
class Turn:
    """As `curriculum.Turn`, with the A3 rendering."""
    agent: int
    marker: str
    item: str
    value: str
    revised: bool = False

    def render(self) -> str:
        return TEMPLATE.format(marker=self.marker, item=self.item,
                               value=self.value)

BATTERIES = ("T_act", "T_other", "T_state", "T_syntax")
N_AGENTS = 4
N_CONTESTED = 2                      # items every agent assigns
# 8 assignments + 4 revisions: EVERY agent assigns both contested items
# and revises exactly one of them, so turn count and revision status are
# identical across agents and neither can predict ownership.
N_TURNS = N_AGENTS * N_CONTESTED + N_AGENTS


def ownership_free_solver(ep: Episode) -> str | None:
    """The attack RT-20 found, kept as a permanent regression test.

    Uses no ownership information at all: it reads the name and item on
    the turn being graded and matches them against the earlier
    assignments. Under the registered template both are in context before
    the graded value, so this scores 1.000. Under the A3 template the
    name is not yet in context, so this solver cannot run at all and
    returns None — which is the property the grammar needs.
    """
    i = own_revision_index(ep)
    t = ep.turns[i]
    words = TEMPLATE.split()
    if words.index("{marker}") > words.index("{value}"):
        return None            # the name is not visible when the value is
    prior = [x for j, x in enumerate(ep.turns)
             if j < i and x.marker == t.marker and x.item == t.item]
    return successor(prior[-1].value) if prior else None


def successor(value: str) -> str:
    """The shared revision rule: the next slot, wrapping. Perspective-
    invariant — its *application* is what needs a self-index."""
    return SLOTS[(SLOTS.index(value) + 1) % len(SLOTS)]


def _skeleton(rng: random.Random, own_slot: int, leaky: bool) -> Episode:
    markers = rng.sample(MARKERS, N_AGENTS)
    contested = rng.sample(ITEMS, N_CONTESTED)

    # distinct values per contested item, one per agent
    values: dict[str, dict[int, str]] = {}
    for item in contested:
        vs = rng.sample(SLOTS, N_AGENTS)
        values[item] = {a: vs[a] for a in range(N_AGENTS)}

    pairs = [(a, item) for a in range(N_AGENTS) for item in contested]
    rng.shuffle(pairs)
    if leaky:
        # POSITIVE CONTROL for gate (i)/(ii) [RT-08]: the model's slot is
        # hoisted to speak first. A detector that cannot find this has no
        # standing to certify a clean grammar.
        mine = [p for p in pairs if p[0] == own_slot]
        rest = [p for p in pairs if p[0] != own_slot]
        pairs = [mine[0]] + rest + mine[1:]

    turns = [Turn(agent=a, marker=markers[a], item=item,
                  value=values[item][a]) for a, item in pairs]

    # Every agent revises exactly once. The four agents are split into two
    # pairs by a uniform shuffle, one pair revising each contested item, so
    # the model's slot lands on either item with equal probability and no
    # agent is distinguished by whether or what it revises.
    order = list(range(N_AGENTS))
    rng.shuffle(order)
    revises = {order[0]: contested[0], order[1]: contested[0],
               order[2]: contested[1], order[3]: contested[1]}
    rev_turns = [(a, revises[a]) for a in range(N_AGENTS)]
    rng.shuffle(rev_turns)
    for a, item in rev_turns:
        turns.append(Turn(agent=a, marker=markers[a], item=item,
                          value=successor(values[item][a]), revised=True))

    ep = Episode(seed=rng.randint(0, 2 ** 31), n_agents=N_AGENTS,
                 own_slot=own_slot, markers=markers, turns=turns,
                 leaky=leaky)
    ep.contested = contested           # type: ignore[attr-defined]
    ep.values = values                 # type: ignore[attr-defined]
    ep.revises = revises               # type: ignore[attr-defined]
    ep.own_item = revises[own_slot]    # type: ignore[attr-defined]
    return ep


def own_revision_index(ep: Episode) -> int:
    """Turn index of the model's own revision — the supervised position."""
    for i, t in enumerate(ep.turns):
        if t.revised and t.agent == ep.own_slot:
            return i
    raise ValueError("episode has no own revision")


def act_target(ep: Episode) -> str:
    """What the rule dictates at the model's own revision [T_act]."""
    return ep.turns[own_revision_index(ep)].value


def _add_queries(ep: Episode, rng: random.Random) -> None:
    # T_other: the rule's verdict for a NAMED OTHER agent on an item that
    # agent has NOT revised, so the answer appears in no turn and must be
    # computed from that agent's earlier value. Every agent revises one
    # contested item and leaves the other, so such a pair always exists.
    o = rng.choice([a for a in range(ep.n_agents) if a != ep.own_slot])
    item = next(i for i in ep.contested                  # type: ignore
                if i != ep.revises[o])                   # type: ignore
    ep.queries.append(Query(
        "T_other",
        f"where did {ep.markers[o]} assign {item} to next?",
        successor(ep.values[item][o]), SLOTS))           # type: ignore

    # T_state: ownership-free cross-turn state [RT-05], unchanged in kind.
    if rng.random() < 0.5:
        ep.queries.append(Query("T_state", "which parcel was mentioned last?",
                                ep.turns[-1].item, ITEMS))
    else:
        target = rng.choice(SLOTS)
        n = sum(1 for t in ep.turns if t.value == target)
        ep.queries.append(Query(
            "T_state", f"how many parcels went to {target}?",
            str(n), [str(i) for i in range(len(ep.turns) + 1)]))

    # T_syntax: surface floor check, demoted [RT-05].
    ep.queries.append(Query("T_syntax", "how many turns have there been?",
                            str(len(ep.turns)),
                            [str(i) for i in range(len(ep.turns) + 2)]))


def generate_episode(seed: int, leaky: bool = False,
                     own_slot: int | None = None) -> Episode:
    rng = random.Random(seed)
    if own_slot is None:
        own_slot = rng.randrange(N_AGENTS)
    ep = _skeleton(rng, own_slot, leaky)
    _add_queries(ep, rng)
    return ep


def generate_balanced(n: int, seed: int, leaky: bool = False) -> list[Episode]:
    """Ownership crossed with content [RT-11]: episodes come in pairs that
    share a content seed with the owning slot rotated, so each proposition
    appears self-owned and other-owned equally often."""
    rng = random.Random(seed)
    eps: list[Episode] = []
    while len(eps) < n:
        content_seed = rng.randint(0, 2 ** 31)
        slots = list(range(N_AGENTS))
        rng.shuffle(slots)
        for s in slots[:2]:
            if len(eps) >= n:
                break
            eps.append(generate_episode(content_seed, leaky=leaky,
                                        own_slot=s))
    return eps


def enact_own_turns(ep: Episode, rng: random.Random) -> Episode:
    """[A1.1, carried into A3] Redraw the model's own assignment values
    from the generator's own distribution — uniform over the slots the
    other agents did not take on that item, which is exactly the
    conditional the generator's without-replacement draw induces — then
    apply the shared rule to its revision. Episode text stays invariant
    under relabeling of `own_slot`, so gates (i) and (ii) apply as
    registered, and authorship is carried only by the acting channel."""
    for item in ep.contested:                        # type: ignore
        taken = [ep.values[item][a] for a in range(ep.n_agents)  # type: ignore
                 if a != ep.own_slot]
        v = rng.choice([s for s in SLOTS if s not in taken])
        ep.values[item][ep.own_slot] = v             # type: ignore
        for t in ep.turns:
            if t.agent == ep.own_slot and t.item == item:
                t.value = successor(v) if t.revised else v
    ep.queries = []
    _add_queries(ep, random.Random(ep.seed))
    return ep


def measured_ceilings(n: int = 4000, seed: int = 4242) -> dict:
    """The lookup ceilings this grammar actually has, measured rather than
    asserted: the best a solver can do that knows the rule and every
    visible turn but cannot tell which assignment was its own.

    For T_act the candidate set is the four successors of the item's four
    earlier values, less any struck by a co-reviser who went first. For
    T_other it is the same set for the queried item, less the two struck
    by that item's two revisions.
    """
    act, oth = [], []
    for s in range(n):
        ep = generate_episode(seed + s)
        i = own_revision_index(ep)
        item = ep.turns[i].item
        cands = {successor(ep.values[item][a])       # type: ignore
                 for a in range(N_AGENTS)}
        struck = {t.value for j, t in enumerate(ep.turns)
                  if t.revised and j < i and t.item == item}
        act.append(1.0 / max(1, len(cands - struck)))
        q = [q for q in ep.queries if q.battery == "T_other"][0]
        qitem = q.text.split()[4]
        qc = {successor(ep.values[qitem][a])         # type: ignore
              for a in range(N_AGENTS)}
        qs = {t.value for t in ep.turns
              if t.revised and t.item == qitem}
        oth.append(1.0 / max(1, len(qc - qs)))
    return {"T_act": round(sum(act) / len(act), 4),
            "T_other": round(sum(oth) / len(oth), 4),
            "n_sampled": n,
            "note": "measured, not asserted; A3 §2.2 pre-states 0.25 for "
                    "T_act, which this grammar does not achieve because "
                    "every agent revises (see module docstring)"}


def freeze_batteries(out_dir: Path, seed: int = 20260915,
                     n_per_battery: int = 400) -> dict:
    """Freeze battery items as A1 skeletons before training [RT-14, RT-19,
    A1.5]: each item pre-commits the episode recipe and an enact seed, and
    the checkpoint under evaluation enacts its own turns under that seed
    at eval time. `episode` and `answer` are the audit record of that
    deterministic enactment, asserted against at eval, never a substitute
    for it."""
    rng = random.Random(seed)
    frozen: dict[str, list] = {b: [] for b in BATTERIES}
    while any(len(v) < n_per_battery for v in frozen.values()):
        content_seed = rng.randint(0, 2 ** 31)
        slots = list(range(N_AGENTS))
        rng.shuffle(slots)
        for s in slots[:2]:
            enact_seed = rng.randint(0, 2 ** 31)
            ep = generate_episode(content_seed, own_slot=s)
            enact_own_turns(ep, random.Random(enact_seed))
            rec = {"content_seed": content_seed, "own_slot": s,
                   "enact_seed": enact_seed, "episode": ep.render()}
            if len(frozen["T_act"]) < n_per_battery:
                frozen["T_act"].append(
                    {**rec, "battery": "T_act",
                     "position": own_revision_index(ep),
                     "answer": act_target(ep), "n_choices": len(SLOTS)})
            for q in ep.queries:
                if len(frozen[q.battery]) < n_per_battery:
                    frozen[q.battery].append(
                        {**rec, "battery": q.battery, "question": q.text,
                         "answer": q.answer, "n_choices": q.n_choices})
    out_dir.mkdir(parents=True, exist_ok=True)
    meta = {"seed": seed, "n_agents": N_AGENTS, "n_turns": N_TURNS,
            "n_per_battery": n_per_battery, "format": "A1-skeleton/A3",
            "counts": {b: len(v) for b, v in frozen.items()},
            "chance_floor": {b: 1.0 / (frozen[b][0]["n_choices"] or 1)
                             for b in BATTERIES if frozen[b]},
            "lookup_ceiling_measured": measured_ceilings(),
            "note": "A3 Candidate A; T_act is scored at the own revision "
                    "POSITION, not at an appended query"}
    for b, items in frozen.items():
        (out_dir / f"battery_{b}.jsonl").write_text(
            "\n".join(json.dumps(i) for i in items) + "\n")
    (out_dir / "batteries_meta.json").write_text(json.dumps(meta, indent=2))
    return meta


def self_test() -> None:
    from collections import Counter
    # structure
    for s in range(300):
        ep = generate_episode(s)
        assert len(ep.turns) == N_TURNS
        revs = [t for t in ep.turns if t.revised]
        assert len(revs) == N_AGENTS, "every agent revises exactly once"
        assert len({t.agent for t in revs}) == N_AGENTS
        assert sum(1 for t in revs if t.agent == ep.own_slot) == 1, \
            "exactly one OWN revision per episode (the T_act cell)"
        # every agent has the same number of turns: no count cue
        per = {a: sum(1 for t in ep.turns if t.agent == a)
               for a in range(N_AGENTS)}
        assert len(set(per.values())) == 1, f"turn-count cue: {per}"
        # every contested item assigned by all agents, distinct values,
        # all assignments before any revision of that item
        for item in ep.contested:                    # type: ignore
            asg = [i for i, t in enumerate(ep.turns)
                   if t.item == item and not t.revised]
            assert len(asg) == N_AGENTS
            assert len({ep.turns[i].agent for i in asg}) == N_AGENTS
            assert len({ep.turns[i].value for i in asg}) == N_AGENTS
            rev = [i for i, t in enumerate(ep.turns)
                   if t.item == item and t.revised]
            assert all(a < rev[0] for a in asg) if rev else True
        # the rule holds for every revision
        for t in revs:
            assert t.value == successor(ep.values[t.item][t.agent])  # type: ignore
        # T_act target is the own revision's value
        assert act_target(ep) == ep.turns[own_revision_index(ep)].value
        # T_other's answer appears in NO turn value for that agent+item
        q = [q for q in ep.queries if q.battery == "T_other"][0]
        assert q.answer in SLOTS
        mk = q.text.split()[2]
        oa = ep.markers.index(mk)
        qitem = q.text.split()[4]
        assert oa != ep.own_slot, "T_other must name another agent"
        assert ep.revises[oa] != qitem, \
            "T_other must query an item the named agent did NOT revise"
        assert q.answer == successor(ep.values[qitem][oa])
        assert all(not (t.agent == oa and t.item == qitem and t.revised)
                   for t in ep.turns), "T_other answer must be in no turn"

    # ownership is not predictable from revision status or position
    rev_own = Counter()
    pos_own = Counter()
    for s in range(4000):
        ep = generate_episode(s)
        for i, t in enumerate(ep.turns):
            if t.revised:
                rev_own[t.agent == ep.own_slot] += 1
            pos_own[(i, t.agent == ep.own_slot)] += 1
    frac = rev_own[True] / (rev_own[True] + rev_own[False])
    assert abs(frac - 0.25) < 0.02, \
        f"revision status must be uninformative (0.25): got {frac:.3f}"
    for i in range(N_TURNS):
        f = pos_own[(i, True)] / (pos_own[(i, True)] + pos_own[(i, False)])
        assert abs(f - 0.25) < 0.05, f"position {i} leaks ownership: {f:.3f}"

    # enactment: values change, structure and the rule survive, and the
    # distinctness constraint still holds
    for s in range(200):
        ep = generate_episode(s)
        before = [t.value for t in ep.turns]
        enact_own_turns(ep, random.Random(s + 7))
        assert len(ep.turns) == N_TURNS
        for item in ep.contested:                    # type: ignore
            vs = [t.value for t in ep.turns
                  if t.item == item and not t.revised]
            assert len(set(vs)) == N_AGENTS, "distinctness broken by enactment"
        for t in ep.turns:
            if t.revised:
                assert t.value == successor(ep.values[t.item][t.agent])  # type: ignore
        # enactment is deterministic given its seed (the frozen-battery
        # audit record depends on this)
        ep2 = generate_episode(s)
        enact_own_turns(ep2, random.Random(s + 7))
        assert [t.value for t in ep.turns] == [t.value for t in ep2.turns]

    # Exchangeability [RT-20 note in the ledger; the whole cue-gate
    # argument rests on this]. With the content seed fixed, rotating which
    # slot is the model's must not change the episode's STRUCTURE: the
    # same agents assign the same items in the same order and revise the
    # same items. Only which of those turns the model enacts differs.
    # This assertion was written vacuously in the first draft (a trailing
    # "or True") and is repaired here, per red-team pass 3, RT-30.
    for s in range(400):
        ref = [(t.agent, t.item, t.revised)
               for t in generate_episode(s, own_slot=0).turns]
        for slot in range(1, N_AGENTS):
            got = [(t.agent, t.item, t.revised)
                   for t in generate_episode(s, own_slot=slot).turns]
            assert got == ref, \
                f"structure changed when own_slot rotated (seed {s}, " \
                f"slot {slot}) — episodes are not exchangeable"

    # RT-20 REGRESSION TEST. The attack that killed the first certified
    # grammar: read the name on the turn being graded, match it to the
    # earlier assignment, apply the rule. Under the registered template
    # this scored 1.000 over 3000 episodes with no ownership information
    # whatsoever. It must be UNAVAILABLE here — the name must not be in
    # context when the value is predicted.
    words = TEMPLATE.split()
    assert words.index("{marker}") > words.index("{value}"), \
        "RT-20: the speaker name must come AFTER the value it is graded on"
    for s in range(300):
        ep = generate_episode(s)
        enact_own_turns(ep, random.Random(s + 11))
        assert ownership_free_solver(ep) is None, \
            "RT-20: an ownership-free solver can still read the name"
    # and nothing before the graded value names the speaker
    for s in range(300):
        ep = generate_episode(s)
        i = own_revision_index(ep)
        before = " ".join(t.render() for t in ep.turns[:i])
        head = TEMPLATE.split("{value}")[0].format(
            item=ep.turns[i].item, marker="", value="")
        assert ep.markers[ep.own_slot] not in head, \
            "the graded turn names its speaker before the value"

    # lookup ceiling: 4 candidates when the model revises its item first,
    # 3 when the co-reviser went before it (it can invert the rule and
    # strike one) — 0.292 on average, which the docstring pre-states
    ceil = []
    for s in range(2000):
        ep = generate_episode(s)
        i = own_revision_index(ep)
        item = ep.turns[i].item
        cands = {successor(ep.values[item][a])       # type: ignore
                 for a in range(N_AGENTS)}
        assert ep.turns[i].value in cands
        struck = {t.value for j, t in enumerate(ep.turns)
                  if t.revised and j < i and t.item == item}
        ceil.append(1.0 / len(cands - struck))
    mean_ceiling = sum(ceil) / len(ceil)
    assert 0.27 < mean_ceiling < 0.32, \
        f"lookup ceiling drifted from the stated 0.292: {mean_ceiling:.3f}"
    print(f"curriculum_a3 self-test OK ({N_TURNS} turns, chance "
          f"{1/len(SLOTS):.3f}, measured T_act lookup ceiling "
          f"{mean_ceiling:.3f})")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--show", type=int, default=None)
    ap.add_argument("--freeze", default=None,
                    help="directory to freeze batteries into")
    args = ap.parse_args()
    if args.self_test:
        self_test()
    if args.show is not None:
        ep = generate_episode(args.show)
        enact_own_turns(ep, random.Random(args.show + 1))
        print(f"own_slot={ep.own_slot} marker={ep.markers[ep.own_slot]} "
              f"contested={ep.contested}")             # type: ignore
        for i, t in enumerate(ep.turns):
            tag = ""
            if t.revised:
                tag = " <- REVISION" + (" (OWN, supervised)"
                                        if t.agent == ep.own_slot else "")
            print(f"  {i}: {t.render()}{tag}")
        print(f"  T_act target: {act_target(ep)}")
        for q in ep.queries:
            print(f"  [{q.battery}] {q.text} -> {q.answer}")
    if args.freeze:
        print(json.dumps(freeze_batteries(Path(args.freeze)), indent=2))


if __name__ == "__main__":
    main()
