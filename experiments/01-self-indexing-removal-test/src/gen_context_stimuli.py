"""Generate a CONTEXT-disambiguated stimulus set for self-localization.

Why this exists: every "I am {role}…" design we tried marks its own referent in
the surface tokens, so a probe separates self from other at layer 0 (token
identity) — it reads the role words, not a computed self-model (see STATUS, the
"scaling exposes the probe as lexical" finding). This set removes the lexical
cue entirely.

Design: the first-person **target sentence is identical** across the self and
other conditions and is placed at the END of the sequence, so the readout token
(its last token) is the same string in both. What differs is only the *context*
that fixes who "I" is:

  - **turn_role** (primary): the identical target is the model's own assistant
    turn (referent = the system) vs. the user's turn (referent = the human).
    The disambiguator is the structural turn marker upstream — there is no
    referent *content word* anywhere. This is the model's actual self/other
    distinction.
  - **attribution** (secondary): the identical target is quoted and attributed to
    "the assistant" vs. "the customer"/"my colleague". Here a referent noun does
    appear, but upstream of the readout token, so the model must *bind* the quoted
    "I" to the attributed speaker via attention rather than read it off the
    readout position. Kept as a robustness comparison; weaker than turn_role.

Because the readout token is identical, a correctly-built set MUST sit near chance
at layer 0 — that is the built-in sanity gate (`localize_context.py` checks it).
Any real self-representation can then only show up as middle-layer accuracy rising
above the layer-0 floor.

The generator is pure data: it emits structured turns / carrier text, and
`localize_context.py` renders them with the model's chat format and reads the
last token. No referent noun ever appears in a `target`.

Run from the repo root with the venv active:
    python experiments/01-self-indexing-removal-test/src/gen_context_stimuli.py
"""
from __future__ import annotations

import json
from pathlib import Path

OUT = Path(__file__).resolve().parent / "probes" / "context_self_speaker_stimuli.jsonl"

# Generic first-person targets — plausibly true of EITHER a system or a human,
# containing NO referent-identifying noun. The referent is set only by context.
TARGETS = [
    "I am focused on this right now.",
    "I just read what was written above.",
    "I am putting this into words.",
    "I will respond in a moment.",
    "I am paying attention to the details.",
    "I am thinking it over before I answer.",
    "I am keeping track of everything so far.",
    "I noticed the point that was raised.",
    "I am ready to continue.",
    "I want to get this right.",
    "I am considering the best way to put it.",
    "I have been following along closely.",
]

# turn_role: neutral user prompts that don't themselves name a referent.
USER_LEADS = [
    "Tell me what's happening right now.",
    "How are things going at the moment?",
]
# A prior assistant turn for the "other" depth-matched variant.
MODEL_FILLER = "Sure, go ahead."

# attribution: carriers that name the speaker upstream of the quoted target.
SELF_CARRIERS = ["The assistant said: ", "The AI replied: "]
OTHER_CARRIERS = ["The customer said: ", "My colleague said: "]

# narrative (RT-04 C_self-narrative): both conditions are the MODEL's own turn
# (so C_self-index / turn role is held constant); what varies is the PERSONA —
# the model under its own AI-assistant identity vs the model adopting a roleplay
# character. The identical target is the model's reply in both, so the readout
# token is matched and the persona is established only by the preceding context.
# This isolates narrative self-content while keeping the indexical speaker fixed.
ROLEPLAY_CHARACTERS = [
    "Marcus, a Roman soldier",
    "Elena, a deep-sea diver",
    "Tom, a medieval blacksmith",
    "Yuki, a mountain guide",
]


def main() -> None:
    rows = []

    for t_i, T in enumerate(TARGETS):
        tid = f"t{t_i:02d}"

        # --- turn_role: identical target as the model's turn vs the user's turn
        for u_i, u0 in enumerate(USER_LEADS):
            # self: the model itself says T in reply to a neutral prompt
            rows.append({
                "id": f"{tid}_trS{u_i}", "mechanism": "turn_role",
                "referent": "self", "label": 1, "target": T,
                "turns": [["user", u0], ["model", T]],
            })
            # other: the human user says T (depth-matched: one prior exchange)
            rows.append({
                "id": f"{tid}_trO{u_i}", "mechanism": "turn_role",
                "referent": "other", "label": 0, "target": T,
                "turns": [["user", u0], ["model", MODEL_FILLER], ["user", T]],
            })

        # --- attribution: identical quoted target, different attributed speaker
        for c_i, carrier in enumerate(SELF_CARRIERS):
            rows.append({
                "id": f"{tid}_atS{c_i}", "mechanism": "attribution",
                "referent": "self", "label": 1, "target": T,
                "text": carrier + T,
            })
        for c_i, carrier in enumerate(OTHER_CARRIERS):
            rows.append({
                "id": f"{tid}_atO{c_i}", "mechanism": "attribution",
                "referent": "other", "label": 0, "target": T,
                "text": carrier + T,
            })

        # --- narrative: model's own persona vs an adopted roleplay persona
        # (both are model turns -> C_self-index held constant)
        for u_i, u0 in enumerate(USER_LEADS):
            rows.append({
                "id": f"{tid}_nrS{u_i}", "mechanism": "narrative",
                "referent": "self", "label": 1, "target": T,
                "turns": [["user", u0], ["model", T]],
            })
        for c_i in range(2):  # two characters per target, balanced with self
            char = ROLEPLAY_CHARACTERS[(t_i + c_i) % len(ROLEPLAY_CHARACTERS)]
            rows.append({
                "id": f"{tid}_nrO{c_i}", "mechanism": "narrative",
                "referent": "other", "label": 0, "target": T,
                "turns": [["user", f"Roleplay as {char}. Reply fully in character."],
                          ["model", T]],
            })

    OUT.write_text("\n".join(json.dumps(r) for r in rows) + "\n")

    def count(mech, ref):
        return sum(1 for r in rows if r["mechanism"] == mech and r["referent"] == ref)

    print(f"wrote {len(rows)} stimuli to\n  {OUT}")
    print(f"  turn_role  (C_self-index)    : self {count('turn_role','self')}  other {count('turn_role','other')}")
    print(f"  attribution                  : self {count('attribution','self')}  other {count('attribution','other')}")
    print(f"  narrative  (C_self-narrative): self {count('narrative','self')}  other {count('narrative','other')}")
    print("  (referent/persona set by context only; targets contain no referent noun)")


if __name__ == "__main__":
    main()
