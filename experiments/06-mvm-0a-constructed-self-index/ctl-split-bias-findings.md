# The fixed batch-split bias check — no bias in episode order, and the reason is structural

*2026-09-20. Step 4 housekeeping, ruled by John 2026-09-20 (STATUS.md,
"Before the closure text is drafted", item 5). Unregistered and labelled
so. Local, $0, no training, no registered text touched. Method and
decision rule committed before output at `e54748f`; run with
`src/ctl_split_check.py --split`. Record:
`a3-gates/ctl_split_bias_check.json`.*

## Verdict

**No bias in episode order.** One pre-stated property does differ between
the halves; it is a badly chosen property rather than a bias, and the
section below says so with the arithmetic rather than waving it away.

| quantity | value |
|---|---|
| steps replayed | 55,116 — every step the pilot trained |
| rows checked | 7,054,848 (3,527,424 each side) |
| structural checks passing | 4 of 4, on every batch |
| content pairs cut by the split boundary | 0 |
| largest Cramér's V on any episode property | 0.0009 against a pre-stated bar of 0.01 |
| largest Cohen's d on any episode property | 0.000 against a pre-stated bar of 0.02 |

## What was in doubt

Under the pilot's change, the control battery's rows are the **first half
of every batch**. That is a fixed positional split, and nobody had checked
whether position in a batch says anything about the episode sitting there.

If it did, the consequence would be serious in a specific way. The control
battery would have been trained on a systematically different slice of the
distribution from the one the other batteries saw, and the pilot's
headline number — the battery sitting at 0.3125, on the shoulder of a
solver that cannot read the name the question supplies — would be a fact
about that slice rather than about the battery. The review filed this as
serious and carried it open for exactly that reason.

## The structural answer, which is the real one

The statistics below are confirmation. The finding is structural, and it
is the interesting part.

**The generator does not emit independent episodes.** It emits them in
**matched content pairs**: one content seed, the owning agent rotated,
appended back to back. Rows 0 and 1 are the same episode content with a
different agent being the model; so are rows 2 and 3, and so on. This is
deliberate — it is the crossing of ownership against content the
programme adopted so that each proposition appears self-owned and
other-owned equally often. It is also precisely why batch position is not
random, and so why the question was worth asking.

**The split boundary falls between pairs, never through one.** The
control half is `round(128 × 0.5) = 64` rows, and 64 is **even**. Pairs
occupy rows (0,1), (2,3), … (62,63) and then (64,65) onward, so every
pair lies wholly inside one half. Checked on all 55,116 batches: **zero
straddles**.

That is the hinge, and it is worth being plain about how narrow it is. An
odd control-row count would cut the last pair at the boundary, handing
the control half one member and the other half its partner — and those
two members differ precisely in which agent is the model. The crossing
would then be broken at the boundary in every batch of the run. The split
is safe here because of an arithmetic coincidence between the batch size,
the control fraction and the pairing, not because anyone chose it to be.

**Any future run that changes the batch size or the control fraction has
to re-check this.** `round(batch × ctl_frac)` must be even. That is the
one sentence of this note worth carrying forward.

Two further structural checks, both holding on every batch: the control
half is always full at 64 rows (no episode falls through for want of a
control query — the grammar gives every episode exactly one), and every
control row carries a control-battery query while no other row does.

## The properties, compared between the halves

Eight of them are properties of the **episode**, which is what the
question is about. The ninth, at the bottom of the table, measures the
whole encoded row and is the one that fired; it has its own section
below.

Each is compared between the control half and the rest, and read against
the bars fixed before the run.

Two plain words about the measures, because they are new vocabulary here.
Both answer "how big is the difference", not "is it real" — and they are
on a scale where 0 means the two halves look identical and 1 means
knowing which half a row is in tells you the property outright. **Cramér's
V** is that measure for a property with named categories, like which of
the four agents the model is. **Cohen's d** is the same idea for a
property that is a number, like how many turns an episode has, and reads
as "how far apart the two averages are, counted in typical spreads". A
d of 1 means the averages differ by a full typical spread, which is a
large difference; the bar below is 0.02.

The reason the bars are on size rather than on the usual
is-it-real test: at three and a half million rows a side, a
significance test calls almost anything significant, including
differences far too small to matter. The adjusted probabilities are
reported anyway, and none of them is anywhere near its bar either.

| property | Cramér's V or Cohen's d | p | material? |
|---|---|---|---|
| which agent the model is | V = 0.00071 | 0.32 | no |
| whether the model revises at all | V = 0.00020 | 0.60 | no |
| the control question's answer (eight bays) | V = 0.00090 | 0.57 | no |
| which contested parcel the control question asks about | V = 0.00022 | 0.55 | no |
| which other agent the control question names | V = 0.00014 | 0.93 | no |
| whether that named agent revised anything | V = 0.00033 | 0.38 | no |
| which of the two state questions the episode carries | V = 0.00043 | 0.25 | no |
| number of turns | d = 0.000 | 1.00 | no |
| **length of the encoded row in tokens** | **d = 4.08** | **0.00** | **yes — see below** |

The turn count is identical: exactly 10.0 on both sides, with no
variation anywhere in the run. The counts behind the categorical rows are
as flat as they look — the model is each of the four agents about 881,000
times in each half, and the control answer lands on each of the eight
bays about 441,000 times in each half.

One sanity check worth recording, because it shows the properties are
measuring what they claim: the "which other agent is named" property has
an empty column at offset zero in both halves. The control question never
names the model itself, which is how the grammar defines that question.
A property that cannot see a known structural fact is not measuring
anything, and this one sees it.

## The property that fired, and what it actually is

`n_tokens` differs, and by a lot: 83.0 tokens in the control half against
81.75 in the rest. Under the rule fixed before the run, that is a
material difference and it is reported as one.

It is not a bias in episode order. It is the intervention showing up in a
badly chosen instrument. `n_tokens` measures the whole encoded **row**,
which is the episode *plus the question attached to it* — and control
rows carry the control question **by design**. The property was supposed
to ask whether longer episodes land at the front of the batch. It asked
something else.

The decomposition is exact, and leaves nothing to interpretation:

| piece | control half | other half |
|---|---|---|
| the episode body, no question attached | 71.000 tokens, **zero variation** | 71.000 tokens, **zero variation** |
| the question | 12.000 (the control question) | 10.750 (state and syntax questions) |
| total | 83.000 | 81.750 |

71 + 12 = 83.000. 71 + 10.750 = 81.750, against a measured 81.7501. The
whole difference is the control question being a quarter of a token over
one token longer than the questions the other rows carry: the control
question is 12 tokens every time, the syntax question 11 every time, and
the state question 10.5 on average because it comes in two forms.

And the episode side gives the stronger result than any test could:
**every episode in the run encodes to exactly 71 tokens, with zero
variance, in both halves.** Batch position cannot correlate with a
quantity that never varies. The answer to "do longer episodes land at the
front" is that there are no longer episodes.

**How this was handled, stated plainly.** The decision rule was committed
before the sweep ran, so the property was not quietly dropped when it
turned out to be awkward. It stays in the check, its result stays
reported, and the verdict field names it. The corrected property — the
episode's own length, with no question attached — was **added after
seeing the first result** and is labelled as such in the code and here. It
is reported alongside the pre-stated one, never in its place. A reader who
distrusts the reasoning above has the query-length decomposition in the
record and can redo the arithmetic.

Adding a ninth property moved the adjusted probability bar from 0.05 ÷ 9
to 0.05 ÷ 10, which is recorded in the run record and changes nothing:
no episode property comes within a factor of forty of either bar. The
size bars, which are the operative rule, were not touched.

## Two corrections to this check, made before its result was trusted

Recorded because the check is the instrument, and an instrument's faults
belong with its output.

1. **A substring bug in one property.** Parcel names collide: `parcel_1`
   is a substring of `parcel_10`. The first version of the
   "which parcel does the control question ask about" property used a
   plain containment test, so a question about parcel 10 was scored as one
   about parcel 1 whenever both were contested. Found before the result
   was read, fixed with a space-padded match, and the sweep re-run from
   the start. It would not have manufactured a false bias — the
   misclassification does not depend on batch position — but it would have
   garbled one of the eight properties. The module's self-test now
   contains this exact case.
2. **The `n_tokens` confound**, above.

Each fault meant re-running the sweep from the start, which produced a
check worth having in its own right: **two independent full runs, 55,116
steps each, agree bit for bit** on every property they share — every
count, every statistic, every structural result. The replay is meant to
be deterministic, and this is the evidence that it is. A drift between
runs would have meant the reconstruction of the pilot's batches was not
faithful, which would have sunk the whole check quietly.

## What this does not establish

Eight episode properties are a finite list. They cannot prove the absence
of every conceivable difference between the halves, and this note does not
claim they do. What carries the weight is the structural result, which is
an exact statement about the code holding on every batch, not an average:
episodes come in pairs, the boundary is even, and no pair is ever cut.

It is also specific to the settings the pilot ran — seed 0, batch 128,
control fraction 0.5. Change either number and the evenness argument has
to be redone.

No result changes. The pilot's verdict (DID NOT LEARN) stands exactly as
ruled, with the scope it was ruled with. This removes a way that verdict
could have been an artefact, and finds that it was not.

## Ledger closure

**RT-58 — the control rows are the first half of every batch, a fixed
positional split never checked for bias. CLOSED 2026-09-20, NO BIAS IN
EPISODE ORDER.** Checked by replaying all 55,116 steps the pilot trained,
7,054,848 rows, not a sample. Structurally: episodes come in matched
content pairs, the control half is 64 rows and 64 is even, so no pair is
ever cut by the boundary (zero straddles in 55,116 batches) and the
ownership crossing survives inside each half; the control half is always
full and only control rows carry the control question. Statistically:
seven episode properties clean, largest Cramér's V 0.0009 against a
pre-stated bar of 0.01; turn count identical at 10.0. The one property
that fired, row length in tokens, decomposes exactly into a 71-token
episode body with **zero variance in both halves** plus a control question
1.25 tokens longer than the others — the intervention, not episode order;
reported rather than dropped, with the corrected episode-only property
added alongside and labelled as added after the fact. **Carried forward:
any future run must keep `round(batch × ctl_frac)` even, or the split cuts
content pairs.** Check: `src/ctl_split_check.py` (new, unregistered; the
trainer is registered text and was not touched). Record:
`a3-gates/ctl_split_bias_check.json`. Findings note:
`ctl-split-bias-findings.md`.
