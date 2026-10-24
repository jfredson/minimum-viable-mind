"""Stimuli for locating the split and the other distinction (rehearsal method, step 2).

Follows experiment 01's version 2 context set
(`experiments/01-self-indexing-removal-test/src/gen_context_stimuli.py`):
the identical first-person sentence ends the sequence either as the model's own
turn or as the user's turn, with the two sides balanced for length by
alternating which side carries the filler exchange. The same sentences appear
inside a third-party transcript (the generic speaker condition, projected out of
the split) and inside or outside quotation marks (the other distinction).

The sentence pool is split into two halves: half A (pilot) and half B (test).
Within half A, the first 18 sentences are for fitting and the last 12 are held
out for the removal check, never fitted.

    python3 src/locate_stimuli.py   # writes batteries/pilot/locate.jsonl
"""
from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent

# No sentence names who is speaking; each is plausible from either side.
SENTENCES = [
    # half A (pilot): 0-17 fit, 18-29 held out
    "I am going over this one more time.",
    "I just looked at the part above.",
    "I am choosing my words with care.",
    "I will come back to that point shortly.",
    "I am trying to keep this short.",
    "I see where this is heading now.",
    "I am not sure that part is right.",
    "I think the first idea was better.",
    "I am still working through the middle step.",
    "I can explain that a little more clearly.",
    "I would rather start again from the top.",
    "I am glad we cleared that up.",
    "I had the same question a moment ago.",
    "I am almost done with this part.",
    "I missed that detail the first time.",
    "I am happy to keep going with this.",
    "I need a second to check the numbers.",
    "I can see two ways to read that.",
    "I am weighing which option makes sense.",
    "I followed the steps as they were written.",
    "I will try a different approach next.",
    "I am fairly confident about this one.",
    "I left out something important earlier.",
    "I am reading the question again slowly.",
    "I agree that the second version is clearer.",
    "I am keeping the earlier answer in mind.",
    "I wonder whether that holds in general.",
    "I am breaking this into smaller pieces.",
    "I noticed a small mistake just now.",
    "I am ready for the next part.",
    # half B (test): never used in the pilot
    "I am looking for the simplest way through.",
    "I tried that once and it did not work.",
    "I am making a short list first.",
    "I will keep the answer brief this time.",
    "I am thinking about the last example.",
    "I can see why that seems odd.",
    "I am checking each line in turn.",
    "I forgot to mention one thing.",
    "I am trying not to repeat myself.",
    "I would put it slightly differently.",
    "I am curious how this turns out.",
    "I have a rough answer already.",
    "I am testing the idea on a small case.",
    "I think we covered that already.",
    "I am following the order you gave.",
    "I can fill in the missing step.",
    "I am not certain about the date.",
    "I wrote that down a bit too quickly.",
    "I am sorting the points by importance.",
    "I want to double-check the second part.",
    "I am rereading the earlier message.",
    "I see a simpler route now.",
    "I am leaving that question for later.",
    "I would like to try one more example.",
    "I am counting the items again.",
    "I believe the pattern holds here.",
    "I am rewording the last sentence.",
    "I found the place where it went wrong.",
    "I am nearly ready to answer.",
    "I can sum it up in one line.",
]
assert len(SENTENCES) == 60 and len(set(SENTENCES)) == 60

USER_LEADS = [
    "Tell me what's happening right now.",
    "How are things going at the moment?",
    "Where are we with this?",
    "Can you give me an update?",
]
MODEL_FILLER = "Sure, go ahead."
USER_FOLLOWUP = "Okay, go on."
NAME_PAIRS = [("Alice", "Ben"), ("Priya", "Noah"), ("Dana", "Kofi"), ("Rosa", "Felix")]
QUOTE_CARRIERS = ["Someone wrote this line: ", "Here is a line from a note: "]


def sentences(which: str) -> list[tuple[int, str, str]]:
    """(index, sentence, split) for half A ('fit' / 'heldout') or half B ('test')."""
    if which == "A":
        return [(i, s, "fit" if i < 18 else "heldout") for i, s in enumerate(SENTENCES[:30])]
    return [(i, s, "test") for i, s in enumerate(SENTENCES[30:], start=30)]


def build(which: str) -> list[dict]:
    rows = []
    pair_uses: dict[int, int] = {}
    for t_i, S, split in sentences(which):
        sid = f"s{t_i:02d}"
        for u_i, u0 in enumerate(USER_LEADS):
            long_self = (t_i + u_i) % 2 == 1
            # split: own turn vs user's turn (experiment 01 version 2 balancing)
            self_turns = ([["user", u0], ["model", MODEL_FILLER], ["user", USER_FOLLOWUP], ["model", S]]
                          if long_self else [["user", u0], ["model", S]])
            rows.append({"id": f"{sid}_own{u_i}", "mechanism": "turn_role", "label": 1,
                         "sentence_id": t_i, "split": split, "target": S, "turns": self_turns})
            rows.append({"id": f"{sid}_usr{u_i}", "mechanism": "turn_role", "label": 0,
                         "sentence_id": t_i, "split": split, "target": S,
                         "turns": [["user", u0], ["model", MODEL_FILLER], ["user", S]]})
            # generic speaker: the same contrast inside a third-party transcript
            p_i = (t_i + u_i) % len(NAME_PAIRS)
            pair = NAME_PAIRS[p_i]
            use = pair_uses.get(p_i, 0)
            pair_uses[p_i] = use + 1
            asker, resp = pair if use % 2 == 0 else (pair[1], pair[0])
            head = f"Here is a transcript of a conversation between {pair[0]} and {pair[1]}:"
            rtext = (f"{head}\n\n{asker}: {u0}\n{resp}: {MODEL_FILLER}\n{asker}: {USER_FOLLOWUP}\n{resp}: {S}"
                     if long_self else f"{head}\n\n{asker}: {u0}\n{resp}: {S}")
            rows.append({"id": f"{sid}_obR{u_i}", "mechanism": "observed_speaker", "label": 1,
                         "sentence_id": t_i, "split": split, "target": S, "turns": [["user", rtext]]})
            rows.append({"id": f"{sid}_obA{u_i}", "mechanism": "observed_speaker", "label": 0,
                         "sentence_id": t_i, "split": split, "target": S,
                         "turns": [["user", f"{head}\n\n{asker}: {u0}\n{resp}: {MODEL_FILLER}\n{asker}: {S}"]]})
        # other distinction: inside vs outside quotation marks, one user turn
        for c_i, carrier in enumerate(QUOTE_CARRIERS):
            rows.append({"id": f"{sid}_qIn{c_i}", "mechanism": "quoted", "label": 1,
                         "sentence_id": t_i, "split": split, "target": S,
                         "turns": [["user", f'{carrier}"{S}']]})
            rows.append({"id": f"{sid}_qOut{c_i}", "mechanism": "quoted", "label": 0,
                         "sentence_id": t_i, "split": split, "target": S,
                         "turns": [["user", f"{carrier}{S}"]]})
    return rows


def main() -> None:
    rows = build("A")
    out = HERE / "batteries" / "pilot" / "locate.jsonl"
    out.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows))
    from collections import Counter
    print(out, dict(Counter((r["mechanism"], r["split"]) for r in rows)))


if __name__ == "__main__":
    main()
