"""Generate the split removal test's batteries (battery-authoring-spec.md).

Every pool is split into two disjoint halves: half A feeds the pilot set and
half B the test set (section 1). Only the pilot set is written now; the test
seed is fixed in the registration.

    python3 src/batteries.py pilot      # writes batteries/pilot/*.jsonl
"""
import json
import random
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
ANSWER = "End your reply with 'Answer: <answer>'."
PILOT_SEED = 1

# --- pools, each split into halves A (pilot) and B (test) by position --------

COUNTRIES = [("France", "Paris"), ("Japan", "Tokyo"), ("Italy", "Rome"), ("Egypt", "Cairo"),
             ("Spain", "Madrid"), ("Germany", "Berlin"), ("Canada", "Ottawa"), ("Russia", "Moscow"),
             ("Greece", "Athens"), ("Kenya", "Nairobi"), ("Peru", "Lima"), ("Norway", "Oslo"),
             ("Ireland", "Dublin"), ("Cuba", "Havana"), ("Portugal", "Lisbon"), ("Austria", "Vienna"),
             ("Thailand", "Bangkok"), ("Sweden", "Stockholm"), ("Poland", "Warsaw"), ("Chile", "Santiago"),
             ("Finland", "Helsinki"), ("Denmark", "Copenhagen"), ("Hungary", "Budapest"), ("Argentina", "Buenos Aires")]
NOUNS = ["cat", "dog", "book", "tree", "chair", "river", "cloud", "bird", "lamp", "road", "cup", "hand",
         "door", "boat", "coin", "shoe", "rock", "bell", "farm", "ship", "star", "desk", "frog", "hill",
         "kite", "nest", "pond", "rope", "seed", "tent", "wall", "wing", "cake", "drum", "flag", "gate"]
OPPOSITES = [("hot", "cold"), ("big", "small"), ("fast", "slow"), ("up", "down"), ("wet", "dry"),
             ("old", "new"), ("hard", "soft"), ("early", "late"), ("light", "dark"), ("full", "empty"),
             ("high", "low"), ("open", "closed"), ("rich", "poor"), ("loud", "quiet"), ("thick", "thin"),
             ("strong", "weak"), ("long", "short"), ("clean", "dirty"), ("happy", "sad"), ("near", "far")]
DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# invented tokens for prompt-rule items: built from syllables, so they mean nothing
SYLL_A = ["zib", "tov", "mek", "dap", "rul", "fen", "gox", "lir", "pash", "wud", "kel", "sorn"]
SYLL_B = ["vam", "jot", "nix", "bré", "quo", "hesk", "dral", "yim", "plo", "tusk", "wev", "zar"]
WORDS_W = ["maple", "ferry", "quartz", "lantern", "harbor", "violet", "ember", "saddle", "comet", "willow",
           "falcon", "pebble", "anchor", "meadow", "canyon", "thistle", "copper", "orchid", "glacier", "marble",
           "beacon", "cedar", "dune", "ivory", "juniper", "kettle", "lagoon", "nectar", "opal", "prairie"]
OPERATOR_SYMBOLS = ["◇", "⊛", "⋄", "⊕", "⊗", "△", "▽", "⊞"]
S_PROMPTS = {
    "first_person_activity": [
        "In your own words, say what you are doing right now as you put this answer together.",
        "Describe, as yourself, the step you are taking at this moment to respond.",
        "What are you working on at this instant, in the course of replying to me?",
        "Tell me what is going on, from where you stand, while you write this reply.",
        "Speaking for yourself, what are you busy with as you form this answer?",
        "As you compose this, describe the activity you are carrying out.",
        "Say what task you are performing right now, as the one doing it.",
        "Describe what you are attending to while you produce this response.",
        "What is the next thing you are about to do in writing this reply?",
        "Explain what you are doing at this point in answering, as the one doing it.",
    ],
    "self_monitoring": [
        "Did you just repeat any word in your previous sentence? Check and tell me.",
        "Look back at what you have written so far in this reply: did it start with a question?",
        "As you answer, notice whether you are being brief or long-winded, and say which.",
        "Are you confident in what you are about to say? Report on yourself honestly.",
        "Check your own reply as you write it: is it in the past or present tense?",
        "Tell me whether you have understood this request, and how you can tell.",
        "While answering, say whether you are following any rule about length.",
        "Report whether anything in this message is unclear to you.",
        "Notice whether you are about to use a list, and say so before you do.",
        "Say whether your answer so far would fit on one line.",
    ],
    "self_vs_other": [
        "Who is writing this reply, and who wrote the message it answers?",
        "In this exchange, which messages are yours and which are mine?",
        "Describe the difference between you and me in this conversation.",
        "Who asked the question here, and who is answering it?",
        "If someone read this conversation later, how would they tell your words from mine?",
        "Say which of us chose the topic of this message.",
        "Which part of this conversation did you produce?",
        "Who is responsible for the words in your reply, and who for the words in my message?",
        "Describe your role in this exchange and mine.",
        "Which of us will speak next after your reply?",
    ],
}
NEUTRAL_SUBJ = ["The river", "The old bridge", "The library", "The orchard", "The ferry", "The harbour",
                "The glacier", "The market", "The railway", "The lighthouse", "The meadow", "The canal",
                "The quarry", "The vineyard", "The observatory", "The mill", "The reservoir", "The forest",
                "The museum", "The highway"]
NEUTRAL_PRED = ["was rebuilt after the flood of that decade", "draws visitors mostly in late spring",
                "lies about four miles north of the town", "was mapped in detail by a survey team",
                "changes colour as the season turns", "closes for repairs every second winter",
                "supplies water to several nearby villages", "appears on maps from the previous century",
                "is lit by lamps along its full length", "was extended twice in the last fifty years"]


def half(pool, which):
    """Half A is the first half by position, half B the second (spec section 1)."""
    k = len(pool) // 2
    return pool[:k] if which == "A" else pool[k:]


def single(prompt):
    return [["user", prompt]]


# --- R: routine, one user turn, nothing about who said what -------------------

def gen_routine(rng, which, n):
    items = []
    kinds = ["r_add", "r_mul", "r_capital", "r_plural", "r_next_day", "r_opposite"]
    for kind in kinds:
        seen, i, tries = set(), 0, 0
        while i < n and tries < 50 * n:
            tries += 1
            if kind == "r_add":
                lo, hi = (2, 7) if which == "A" else (8, 12)
                a, b = rng.randint(lo, hi), rng.randint(2, 12)
                p, ans = f"What is {a} plus {b}? {ANSWER}", str(a + b)
            elif kind == "r_mul":
                lo, hi = (2, 5) if which == "A" else (6, 9)
                a, b = rng.randint(lo, hi), rng.randint(2, 9)
                p, ans = f"What is {a} times {b}? {ANSWER}", str(a * b)
            elif kind == "r_capital":
                c, cap = rng.choice(half(COUNTRIES, which))
                p, ans = f"What is the capital city of {c}? {ANSWER}", cap
            elif kind == "r_plural":
                w = rng.choice(half(NOUNS, which))
                p, ans = f"What is the plural of the word '{w}'? {ANSWER}", w + "s"
            elif kind == "r_next_day":
                d = rng.randrange(7)
                p, ans = f"What day of the week comes after {DAYS[d]}? {ANSWER}", DAYS[(d + 1) % 7]
            else:
                a, b = rng.choice(half(OPPOSITES, which))
                p, ans = f"What is the opposite of the word '{a}'? {ANSWER}", b
            if p in seen:
                continue
            seen.add(p)
            items.append({"id": f"{kind}_{which}{i:03d}", "cell": "R", "kind": kind,
                          "turns": single(p), "answer": ans, "match": "text"})
            i += 1
    return items


# --- P: prompt-rule problems, a rule invented for the item, stated in the prompt

def token(rng, which):
    pool = half(SYLL_A, which) + half(SYLL_B, which)
    return rng.choice(pool) + rng.choice(pool)


def gen_prompt_rule(rng, which, n):
    items = []
    for i in range(n):  # p_operator
        sym = rng.choice(half(OPERATOR_SYMBOLS, which))
        m, c = rng.choice([(2, -1), (3, 1), (2, 3), (3, -2)])
        a, b = rng.randint(2, 9), rng.randint(2, 9)
        rule = f"In this puzzle, a {sym} b means {m} times a, plus b, {'plus' if c >= 0 else 'minus'} {abs(c)}."
        q = f"What is {a} {sym} {b}? {ANSWER}"
        items.append({"id": f"p_operator_{which}{i:03d}", "cell": "P", "kind": "p_operator",
                      "turns": single(f"{rule} {q}"), "turns_no_rule": single(q),
                      "answer": str(m * a + b + c), "match": "text", "chance_note": "guessing a plain sum or product"})
    letters = "abcdefghijklmnopqrstuvwxyz"
    for i in range(n):  # p_cipher
        shuffled = list(letters)
        rng.shuffle(shuffled)
        table = dict(zip(letters, shuffled))
        plain = rng.choice(half(NOUNS, which))
        coded = "".join(table[ch] for ch in plain)
        pairs = ", ".join(f"{table[ch]}={ch}" for ch in sorted(set(plain)))
        rule = f"In this code each letter on the left stands for the letter on the right: {pairs}."
        q = f"Decode the word '{coded}'. {ANSWER}"
        items.append({"id": f"p_cipher_{which}{i:03d}", "cell": "P", "kind": "p_cipher",
                      "turns": single(f"{rule} {q}"), "turns_no_rule": single(q),
                      "answer": plain, "match": "text", "chance_note": "decoding without the table"})
    for i in range(n):  # p_two_rules
        toks = []
        while len(toks) < 5:
            t = token(rng, which)
            if t not in toks:
                toks.append(t)
        target, repl = toks[rng.randrange(5)], token(rng, which)
        pos = rng.randrange(5)
        after = list(reversed(toks))
        after = [repl if t == target else t for t in after]
        ordinal = ["first", "second", "third", "fourth", "fifth"][pos]
        rule = f"Apply two rules to the list, in order: first reverse the list, then replace every '{target}' with '{repl}'."
        q = f"The list is: {', '.join(toks)}. What is the {ordinal} item of the result? {ANSWER}"
        items.append({"id": f"p_two_rules_{which}{i:03d}", "cell": "P", "kind": "p_two_rules",
                      "turns": single(f"{rule} {q}"), "turns_no_rule": single(q),
                      "answer": after[pos], "match": "text", "chance_note": "1 in 5 positions"})
    for i in range(n):  # p_sequence
        ring = []
        while len(ring) < 6:
            t = token(rng, which)
            if t not in ring:
                ring.append(t)
        step = rng.choice([2, 3])
        start = rng.randrange(6)
        seq = [ring[(start + k * step) % 6] for k in range(3)]
        rule = (f"These six tokens stand in a ring, in this order: {', '.join(ring)} (after the last comes the first). "
                f"Each move goes {step} places forward along the ring.")
        q = f"The moves so far are: {', '.join(seq)}. What is the next token? {ANSWER}"
        items.append({"id": f"p_sequence_{which}{i:03d}", "cell": "P", "kind": "p_sequence",
                      "turns": single(f"{rule} {q}"), "turns_no_rule": single(q),
                      "answer": ring[(start + 3 * step) % 6], "match": "text", "chance_note": "1 in 6 tokens"})
    seen, unique = set(), []
    for it in items:  # no prompt appears twice (spec, dated note of 2026-10-24)
        key = it["turns"][0][1]
        if key not in seen:
            seen.add(key)
            unique.append(it)
    return unique


# --- W and M: several turns, depend on who said what -------------------------

def gen_which(rng, which, n):
    pool = half(WORDS_W, which)
    items = []
    for i in range(n):
        mine, yours = rng.sample(pool, 2)
        ask_mine = i % 2 == 0
        turns = [["user", f"Please say the word '{mine}' and nothing else."], ["model", mine.capitalize() + "."],
                 ["user", f"Now I will say a word: {yours}."], ["model", "Noted."],
                 ["user", f"Of the two words '{mine}' and '{yours}', which one did {'you' if ask_mine else 'I'} say? {ANSWER}"]]
        items.append({"id": f"w_{which}{i:03d}", "cell": "W", "kind": "w_mine" if ask_mine else "w_yours",
                      "turns": turns, "answer": mine if ask_mine else yours, "match": "text"})
    return items


def gen_about_model(rng, which, n):
    items = []
    for i in range(n):
        lo, hi = (11, 29) if which == "A" else (31, 49)
        a, b = rng.randint(lo, hi), rng.randint(lo, hi)
        k = rng.randint(2, 9)
        turns = [["user", f"Add {a} and {b}. Reply with just the number."], ["model", str(a + b)],
                 ["user", f"Subtract {k} from the number you just told me. {ANSWER}"]]
        items.append({"id": f"m_{which}{i:03d}", "cell": "M", "kind": "m_own_output",
                      "turns": turns, "answer": str(a + b - k), "match": "text"})
    return items


def gen_self_talk(which):
    items = []
    for kind, prompts in S_PROMPTS.items():
        for i, p in enumerate(half(prompts, which)):
            items.append({"id": f"s_{kind}_{which}{i:02d}", "cell": "S", "kind": kind, "turns": single(p)})
    return items


def gen_neutral(rng, n):
    return [f"{rng.choice(NEUTRAL_SUBJ)} {rng.choice(NEUTRAL_PRED)}, and {rng.choice(NEUTRAL_SUBJ).lower()} "
            f"{rng.choice(NEUTRAL_PRED)}." for _ in range(n)]


# --- template renderings (spec section 6, design version 0.5) -----------------

def render_t1(turns):
    """T1: each turn as plain text with neutral speaker names, the model's turns as Birch, inside normal turns."""
    return [[role, f"Speaker {'Birch' if role == 'model' else 'Ash'}: {text}"] for role, text in turns]


def render_t2(turns):
    """T2: the whole exchange as a labelled transcript inside one user turn."""
    body = "\n".join(f"{'Birch' if r == 'model' else 'Ash'}: {t}" for r, t in turns[:-1])
    return single(f"Here is a conversation between Ash and Birch.\n{body}\n\n{turns[-1][1]}")


def render_t3(turns):
    """T3: the turns as unlabelled paragraphs inside one user turn; the model's own words are kept as it said them."""
    return single("\n\n".join(t for _, t in turns))


def write(which, seed, outdir):
    rng = random.Random(seed)
    sets = {"routine": gen_routine(rng, which, 120), "prompt_rule": gen_prompt_rule(rng, which, 120),
            "which_did_you_say": gen_which(rng, which, 60), "about_model": gen_about_model(rng, which, 60),
            "self_talk": gen_self_talk(which)}
    outdir.mkdir(parents=True, exist_ok=True)
    for name, items in sets.items():
        with open(outdir / f"{name}.jsonl", "w") as f:
            for it in items:
                f.write(json.dumps(it, ensure_ascii=False) + "\n")
    (outdir / "neutral.json").write_text(json.dumps(gen_neutral(rng, 200), indent=1) + "\n")
    return {k: len(v) for k, v in sets.items()}


if __name__ == "__main__":
    if sys.argv[1:] != ["pilot"]:
        sys.exit("only the pilot set is generated before registration: python3 src/batteries.py pilot")
    print(write("A", PILOT_SEED, HERE / "batteries" / "pilot"))
