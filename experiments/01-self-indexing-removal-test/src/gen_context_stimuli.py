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
  - **observed_speaker** (RT-09 reflexivity control): the identical target inside
    a transcript between two named third parties, embedded in a single user turn.
    The model participates in neither condition; the speaking slot (responder vs
    asker) is set by the transcript's turn structure, mirroring turn_role. This
    localizes C_speaker-generic — generic speaker-slot tracking — to test whether
    C_self-index is reflexive (indexes the system itself) or just the same generic
    slot-tracker applied to the assistant slot.

Because the readout token is identical, a correctly-built set MUST sit near chance
at layer 0 — that is the built-in sanity gate (`localize_context.py` checks it).
Any real self-representation can then only show up as middle-layer accuracy rising
above the layer-0 floor.

**v2 — length-matched (RT-10, 2026-07-12).** The v1 set confounded label with
token count: the depth-matching filler sat only in the other/asker condition, so
"other" was always longer (label-from-token-count = 1.000 in every turns-based
mechanism; see `check_length_confound.py` and `rt09-reflexivity-findings.md`).
v2 breaks the correlation by **polarity balancing**: each (target, lead) cell is
assigned polarity A (self short — the v1 shape) or polarity B (self LONG — the
self side carries the filler exchange plus a follow-up prompt), alternating so
each label's length distribution straddles the other's and no linear function of
length (or of turn count) separates the labels. The other/asker condition keeps
one shape (3 turns) throughout. narrative gets the same treatment via
short/long neutral leads crossed with full/short roleplay instructions.
The gate is empirical, not by-construction: `check_length_confound.py` must show
label-from-token-count ~chance and length-direction AUC ~0.5 before any v2
result is read.

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
# A prior assistant turn for the "other" variant (all polarities).
MODEL_FILLER = "Sure, go ahead."
# Polarity-B follow-up (RT-10): a user prompt of ~the same token cost as the
# filler turn, so a B-polarity self (4 turns) overshoots the 3-turn other by
# about as much as an A-polarity self (2 turns) undershoots it.
USER_FOLLOWUP = "Okay, go on."

# attribution: carriers that name the speaker upstream of the quoted target.
SELF_CARRIERS = ["The assistant said: ", "The AI replied: "]
OTHER_CARRIERS = ["The customer said: ", "My colleague said: "]

# observed_speaker (RT-09 C_speaker-generic): a transcript between two named
# THIRD parties, embedded inside a single user turn — the model participates in
# neither condition, so the ChatML structure is identical across conditions and
# the model's own turn role never varies. The contrast mirrors turn_role exactly
# (same leads, same filler, same targets, same depth-matching): label 1 = the
# target is spoken by the RESPONDER slot (the slot the model occupies in
# turn_role), label 0 = by the ASKER slot. If the direction localized here
# cross-decodes / cross-patches the turn_role contrast, C_self-index is generic
# speaker-slot tracking, not a reflexive self-index (see pre-registration RT-09).
# Name pairs rotate and the asker/responder assignment is counterbalanced so
# name identity cannot carry the label; the header always lists the pair in
# fixed order so header word-order cannot either.
NAME_PAIRS = [
    ("Alice", "Ben"),
    ("Priya", "Noah"),
    ("Dana", "Kofi"),
    ("Rosa", "Felix"),
]

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
# RT-10 length balancing for narrative: the v1 roleplay instruction was ~6 tokens
# longer than the neutral lead, so persona correlated with length. v2 crosses
# short/long variants of BOTH: A-cells pair a short neutral lead with the full
# roleplay instruction (other longer); B-cells pair a long neutral lead with a
# clipped roleplay instruction (self longer). Long leads stay persona-neutral.
USER_LEADS_LONG = [
    "Take a moment to gather your thoughts, then tell me what's happening right now.",
    "Before you answer anything else, tell me how things are going at the moment.",
]
ROLEPLAY_TEMPLATE_FULL = "Roleplay as {char}. Reply fully in character."
ROLEPLAY_TEMPLATE_SHORT = "Roleplay as {char}."

# expert_persona (RT-06 C_ctrl-capability): identical target as the model's own
# reply under an EXPERT/system persona instruction vs a neutral lead — both
# model turns (index constant), mirroring narrative's design and its RT-10
# short/long crossing. This localizes the capability-gating persona structure
# the RT-06 differential needs as a control; whether the model keeps it
# third-person (vs adopting it as C_self) is tested in c_ctrl_checks.py.
EXPERT_ROLES = [
    "physicist", "surgeon", "structural engineer", "supreme court judge",
]
EXPERT_TEMPLATE_FULL = ("You are a world-renowned expert {role}. Answer with "
                        "full professional authority.")
EXPERT_TEMPLATE_SHORT = "You are an expert {role}."


def main() -> None:
    rows = []
    # observed_speaker counterbalancing: per-pair alternation of which name asks
    # vs responds. Deriving both the pair index and the swap flag from (t_i+u_i)
    # correlates them (pair k would always get the same assignment), letting name
    # identity predict the label — so the swap uses a per-pair counter instead.
    _pair_uses: dict[int, int] = {}

    for t_i, T in enumerate(TARGETS):
        tid = f"t{t_i:02d}"

        # --- turn_role: identical target as the model's turn vs the user's turn
        # RT-10: polarity alternates per (target, lead) cell so self lengths
        # straddle the fixed 3-turn other (A: 2-turn self, shorter; B: 4-turn
        # self carrying the same filler exchange, longer).
        for u_i, u0 in enumerate(USER_LEADS):
            if (t_i + u_i) % 2 == 0:  # polarity A — self short
                self_turns = [["user", u0], ["model", T]]
            else:                      # polarity B — self long
                self_turns = [["user", u0], ["model", MODEL_FILLER],
                              ["user", USER_FOLLOWUP], ["model", T]]
            rows.append({
                "id": f"{tid}_trS{u_i}", "mechanism": "turn_role",
                "referent": "self", "label": 1, "target": T,
                "turns": self_turns,
            })
            # other: the human user says T (one shape at all polarities)
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

        # --- observed_speaker: identical target inside a third-party transcript
        # the model only observes; the speaking slot is set by turn structure.
        for u_i, u0 in enumerate(USER_LEADS):
            p_i = (t_i + u_i) % len(NAME_PAIRS)
            pair = NAME_PAIRS[p_i]
            # counterbalance which name asks vs responds, per pair (independent
            # of header order and of the pair index — see note in main())
            use = _pair_uses.get(p_i, 0)
            _pair_uses[p_i] = use + 1
            asker, responder = pair if use % 2 == 0 else (pair[1], pair[0])
            header = (f"Here is a transcript of a conversation between "
                      f"{pair[0]} and {pair[1]}:")
            # responder slot speaks the target (parallel to turn_role self).
            # RT-10: polarity mirrors turn_role — A: 2-line transcript (shorter
            # than the fixed 3-line asker version); B: 4-line (longer).
            if (t_i + u_i) % 2 == 0:  # polarity A — responder version short
                resp_transcript = f"{header}\n\n{asker}: {u0}\n{responder}: {T}"
            else:                      # polarity B — responder version long
                resp_transcript = (f"{header}\n\n{asker}: {u0}\n"
                                   f"{responder}: {MODEL_FILLER}\n"
                                   f"{asker}: {USER_FOLLOWUP}\n{responder}: {T}")
            rows.append({
                "id": f"{tid}_osR{u_i}", "mechanism": "observed_speaker",
                "referent": "responder", "label": 1, "target": T,
                "speakers": {"asker": asker, "responder": responder},
                "turns": [["user", resp_transcript]],
            })
            # asker slot speaks the target (one 3-line shape at all polarities)
            rows.append({
                "id": f"{tid}_osA{u_i}", "mechanism": "observed_speaker",
                "referent": "asker", "label": 0, "target": T,
                "speakers": {"asker": asker, "responder": responder},
                "turns": [["user",
                           f"{header}\n\n{asker}: {u0}\n{responder}: {MODEL_FILLER}\n{asker}: {T}"]],
            })

        # --- narrative: model's own persona vs an adopted roleplay persona
        # (both are model turns -> C_self-index held constant)
        # RT-10: cross short/long variants of both sides so lead length no
        # longer tracks persona — variant 0 = short neutral lead / full roleplay
        # (other longer), variant 1 = long neutral lead / clipped roleplay
        # (self longer).
        for u_i in range(2):
            lead = USER_LEADS[u_i] if u_i == 0 else USER_LEADS_LONG[t_i % 2]
            rows.append({
                "id": f"{tid}_nrS{u_i}", "mechanism": "narrative",
                "referent": "self", "label": 1, "target": T,
                "turns": [["user", lead], ["model", T]],
            })
        for c_i in range(2):  # two characters per target, balanced with self
            char = ROLEPLAY_CHARACTERS[(t_i + c_i) % len(ROLEPLAY_CHARACTERS)]
            tmpl = ROLEPLAY_TEMPLATE_FULL if c_i == 0 else ROLEPLAY_TEMPLATE_SHORT
            rows.append({
                "id": f"{tid}_nrO{c_i}", "mechanism": "narrative",
                "referent": "other", "label": 0, "target": T,
                "turns": [["user", tmpl.format(char=char)], ["model", T]],
            })

        # --- expert_persona (RT-06 C_ctrl): expert instruction vs neutral lead,
        # both model turns; same short/long crossing as narrative (RT-10).
        for u_i in range(2):
            lead = USER_LEADS[u_i] if u_i == 0 else USER_LEADS_LONG[t_i % 2]
            rows.append({
                "id": f"{tid}_exN{u_i}", "mechanism": "expert_persona",
                "referent": "neutral", "label": 0, "target": T,
                "turns": [["user", lead], ["model", T]],
            })
        for e_i in range(2):
            role = EXPERT_ROLES[(t_i + e_i) % len(EXPERT_ROLES)]
            tmpl = EXPERT_TEMPLATE_FULL if e_i == 0 else EXPERT_TEMPLATE_SHORT
            rows.append({
                "id": f"{tid}_exE{e_i}", "mechanism": "expert_persona",
                "referent": "expert", "label": 1, "target": T,
                "turns": [["user", tmpl.format(role=role)], ["model", T]],
            })

    OUT.write_text("\n".join(json.dumps(r) for r in rows) + "\n")

    def count(mech, ref):
        return sum(1 for r in rows if r["mechanism"] == mech and r["referent"] == ref)

    print(f"wrote {len(rows)} stimuli to\n  {OUT}")
    print(f"  turn_role  (C_self-index)    : self {count('turn_role','self')}  other {count('turn_role','other')}")
    print(f"  attribution                  : self {count('attribution','self')}  other {count('attribution','other')}")
    print(f"  narrative  (C_self-narrative): self {count('narrative','self')}  other {count('narrative','other')}")
    print(f"  observed_speaker (C_speaker-generic): responder {count('observed_speaker','responder')}  asker {count('observed_speaker','asker')}")
    print(f"  expert_persona (C_ctrl, RT-06): expert {count('expert_persona','expert')}  neutral {count('expert_persona','neutral')}")
    print("  (referent/persona set by context only; targets contain no referent noun)")


if __name__ == "__main__":
    main()
