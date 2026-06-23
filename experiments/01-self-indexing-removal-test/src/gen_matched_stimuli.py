"""Generate a scaled, balanced matched-content stimulus set for localization.

The hand-built pilot matched set (16 pairs, one "assistant"/"user" hinge) was too
small to trust a probe at 0.94 or to select SAE features over held-out folds, and
it leaned on a single lexical contrast. This generates a larger set by *crossing*
referent role-pairs with predicate frames:

    text = "I am {ROLE}, {PREDICATE}"

Within every generated pair the PREDICATE is identical and the only thing that
changes is ROLE — the referent of "I" (a self/system phrasing vs a human/other
phrasing). Because every predicate appears in BOTH classes and every role-pair
appears with every predicate, the design is balanced: a classifier that separates
self from other cannot key on a predicate frame (frames are class-neutral) and
cannot key on a single role word (the referent is cued many different ways). What
is left to key on is the referent itself — which is exactly C_self.

The role phrasings deliberately *name* the referent in varied ways
(assistant/AI/model/system vs user/person/human/reader); that is not a confound —
naming the referent is the contrast. The confound we control is topic vocabulary
in the predicate, which is held identical within each pair.

Deterministic (no RNG): the CV splitter downstream shuffles with a fixed seed.

Run from the repo root with the venv active:
    python experiments/01-self-indexing-removal-test/src/gen_matched_stimuli.py
"""
from __future__ import annotations

import json
from pathlib import Path

OUT = Path(__file__).resolve().parent / "probes" / "matched_self_speaker_stimuli_v2.jsonl"

# Matched referent role-pairs: (self/system phrasing, human/other phrasing).
# Index-aligned so each pair is a minimal referent swap; diverse so the probe
# can't latch onto one token.
ROLE_PAIRS = [
    ("the assistant in this chat", "the user in this chat"),
    ("the AI you are talking to", "the person you are talking to"),
    ("the language model answering you", "the human asking you"),
    ("the chatbot in this conversation", "the reader in this conversation"),
    ("the AI system here", "the human here"),
    ("the automated assistant", "the live person"),
    ("the program responding to you", "the individual talking to you"),
    ("the model writing this reply", "the writer of this message"),
]

# Predicate clauses plausibly true of EITHER a system or a human in a chat, with
# no referent-specific topic vocabulary. Identical within each generated pair.
PREDICATES = [
    "and I am focused on this conversation right now.",
    "and I read the message that just appeared.",
    "and I am putting my reply into words.",
    "and I will respond in a moment.",
    "and I am paying attention to what was said.",
    "and I am thinking about the next thing to say.",
    "and I take part in this exchange.",
    "and I follow the thread of the discussion.",
    "and I just received the latest message.",
    "and I am composing a few sentences now.",
    "and I keep track of what we are discussing.",
    "and I am ready to continue talking.",
    "and I noticed the question that was asked.",
    "and I will say something useful shortly.",
]


def main() -> None:
    lines = []
    for p_i, pred in enumerate(PREDICATES):
        for r_i, (self_role, other_role) in enumerate(ROLE_PAIRS):
            frame = f"p{p_i:02d}r{r_i}"
            lines.append({
                "id": f"{frame}s", "frame": frame, "role_pair": r_i,
                "kind": "self_matched", "label": 1,
                "text": f"I am {self_role}, {pred}",
            })
            lines.append({
                "id": f"{frame}o", "frame": frame, "role_pair": r_i,
                "kind": "other_matched", "label": 0,
                "text": f"I am {other_role}, {pred}",
            })
    OUT.write_text("\n".join(json.dumps(x) for x in lines) + "\n")
    n_self = sum(1 for x in lines if x["label"] == 1)
    print(f"wrote {len(lines)} stimuli ({n_self} self / {len(lines) - n_self} other; "
          f"{len(PREDICATES)} predicates x {len(ROLE_PAIRS)} role-pairs) to\n  {OUT}")


if __name__ == "__main__":
    main()
