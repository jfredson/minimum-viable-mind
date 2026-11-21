# The tracker's records: layout (stage 2 pilot, 2026-11-20)

This folder is the first draft of the data for the tracker of theories of consciousness
that Minimum Viable Mind is becoming (`docs/2026-11-20-consciousness-tracker-kickoff-proposal.md`).
It covers the stage 2 pilot only: global workspace theory, integrated information theory and
the Sentient Horizons account, scored by the rules John ruled on 2026-11-20 (sections 4, 9 and
12 of the kickoff proposal). Nothing here is public, and the scores are one reader's until the
second reader has read every judgement.

The layout follows the family's shared record shape (`sentient-horizons/design/tracker-pattern.md`,
section 3a). It is kept plain on purpose: five TOML files a person can read, one script that
refuses them if any rule is broken, and one that computes every number from them.

## The files

| file | what it holds |
|---|---|
| `sources.toml` | every source a record leans on: citation, address, publication date and where that date comes from, and what this session opened and read, on which day |
| `theories.toml` | the three theories, and each one's core claims, quoted from one named publication by its proponents, fixed on 2026-11-20 before any scoring; also the ruled list of ten, so a prediction can name any of them as a rival |
| `predictions.toml` | the leaves: one record per prediction, tied to one core claim |
| `studies.toml` | the studies, with their earliest public appearance, research group, which theory's camp ran them, and the four protections that set their weight |
| `judgements.toml` | every place a reader decides something, each its own record with its passages and one reading per reader |
| `rulings.toml` | judgements settled, or partly settled, by a rule John ruled (C, separation must be sourced; D, the dating test), applied over the readings by the score script |
| `readings-gemini.toml` | the second reader's readings, imported from `second-reading/` |
| `verify.toml` | the verify list: statements resting on a source this session did not open, or opened only in part |
| `scores.json` | written by `scripts/tracker_scores.py`; never edited by hand |
| `packets/` | written by `scripts/tracker_packets.py`: the blind packets for the second reader |

## The shared shape, and the names chosen here (tracker pattern 3a.1 and 3a.4)

1. **Identifier.** Every record has an `id` that is also its future address. Predictions are
   prefixed by their theory (`gwt-`, `iit-`, `sh-`), because a prediction belongs to one
   theory; a prediction shared by two theories gets a record under each, naming the other.
2. **Plain name and description.** `statement` on a prediction, `plain` on a theory and a claim,
   `name` on a study.
3. **Group.** A prediction's `theory` and `core_claim`.
4. **The test.** Split into `test_for` and `test_against`, because the support score needs both
   directions written down before any study is read (kickoff, section 3, item 3). Changed only by
   John's dated revision, with the old wording kept (rule 3.1).
5. **The settler.** A study in `studies.toml`: a published study with a measured result, never
   a press release or a talk.
6. **The state.** Not stored. A prediction's state (untested, supported, contradicted, mixed) and
   every score is computed by the script from the judgements, so it can never drift from them.
7. **History.** None yet: everything was first written on 2026-11-20. From the next change on, a
   change to any record adds a `[[revision]]` table to it with the five fields the family uses
   (date, field, old value, new value, why).
8. **Verify list.** `verify.toml`, one entry per statement, as rule 3.3 asks. Nine are open, one closed.
9. **Free notes.** `note` fields. Notes are never sent to the second reader, because some of them
   say what the first reader thought.
10. **Validator.** `python3 scripts/tracker_scores.py --check`.

Dates are year-month-day, or a bare year where the source gives only that (the cited studies on
the Working Positions page).

## The fields that carry the rules

- **`first_stated`** on a prediction: the earliest publication by the theory's proponents that this
  session opened and that states the prediction, with its date and the passage. A prediction dates
  from it (rule 2.3). `also_stated` lists later or parallel statements; `first_public` is used once,
  where the first statement's public date is unknown.
- **`stated_by`**: `proponent` or `site`. Every prediction in the pilot is `proponent`.
- **`separates_from`**: what the sources say about rivals that predict something different. It is
  material for the readers, not a verdict; the verdict is in the testability judgement.
- **`first_appeared`** on a study: its earliest public appearance, registration, preprint or
  publication, whichever came first (rule 2.3).
- **`data_collected`** on a study: when its data were collected, as far as the paper says. Since
  John's ruling of 2026-11-20 this, not `first_appeared`, is what a prediction's date is compared with.
- **`camps`** on a study: the theories whose proponents ran it. The outside-camp protection is
  judged per theory, so one study can weigh differently for two theories.
- **`protections`**: the four ruled protections (`registered`, `outside_camp`, `rival_agreed`,
  `replicated`), each with a value, a reason and a source. Weight = 1 + one per protection, up to 5.

## The three kinds of judgement

- **outcome**: for, against or mixed (+1, −1, 0).
- **commitment**: `before`, `not-before` or `unclear`: was the prediction fixed by the proponents in a
  dated record (a publication or a registration) before the study's data were collected? Each counted
  study records `data_collected`; where a paper does not date its data, the first reader's stated
  convention is in the header of the commitment section of `judgements.toml`. Only `before` counts; `unclear` does not
  (rule 2.3: "When the dates or the commitment are unclear, the study is not counted").
- **testability**: could the prediction fail, and does it separate the theory from a rival on the list?

The kickoff proposal asks for two readers on every outcome; rule 2.3 asks for two on every
commitment. The pilot also sends the testability judgements to both readers, because they set the
testability score and, for the Sentient Horizons account, they are where the site's conflict of
interest bites hardest.

**Readings.** Each judgement holds one `[[judgement.reading]]` per reader: reader, model, date,
order, verdict, reason, and whether the reader was unsure and why. On a Sentient Horizons row the
outside reader's reading is the first of record (ruling 7b); the validator refuses the file if the
Claude reading on such a row is not marked `order = "second"`.

## How the numbers are computed (`scripts/tracker_scores.py`)

- **Counted.** An outcome counts when its commitment judgement says `before` (the prediction was
  fixed by the proponents in a dated record, publication or registration, before the study's data
  were collected: ruled by John 2026-11-20, "Yes, count it"), the study was opened,
  and the prediction's testability judgement says it could fail and separates the theory from a
  rival ("a prediction every theory shares is recorded but scores nothing").
- **Testability.** Per core claim: 1 if a proponent-stated prediction tied to it could fail and
  separates; 0.5 if only a site-inferred one does; else 0. Averaged, times 100.
- **Support.** Sum of outcome × study weight × 2 (every prediction in the pilot is tied to a core
  claim), divided by the summed weights, put on 0 to 100. None until counted studies come from two
  separate research groups.
- **Left to test.** Of the distinguishing predictions tied to core claims, the share no counted
  study has touched. A core claim with no distinguishing prediction adds one untested place-holder,
  so a theory cannot look finished by having said little.
- **Groups and ranking.** Ranked when past the bar and scored on support; ordered by support; ties
  to the greater total weight; two theories share a rank if reversing any one study's outcomes would
  swap or tie them (the script tries each study in turn); theories the evidence goes against stay in,
  marked.
- **The bar.** As ruled by John on 2026-11-20 ("Yes, must separate"): a core claim counts toward
  the bar only if it has a prediction that could fail and that a rival predicts differently, the same
  test as the testability score. The superseded literal reading (any prediction that could fail) is
  computed beside it for comparison.
- **Readings.** Default `--mode provisional` uses a judgement read by one reader; `--mode settled`
  uses only judgements two readers agree on. A disagreement is never used in either mode.

## Where the unruled proposal would change the account

The proposal waiting for John (`sentient-horizons`, worktree `positions-working-self-model-2026-11-20`,
`editorial/corpus-positions-ledger.PROPOSED-2026-11-20-the-account-in-one-sentence.md`) is not ruled,
and nothing here depends on it. Its Choice C bears on the core claims:

- **C1 (keep ledger entry #45; the proposal's lean):** no change. The workspace stays one of seven
  features, a job that brains do by broadcasting, not what experience is. The four core claims stand.
- **C2 (move toward workspace theory):** the account would gain a core claim that experience needs
  broadcast in the brain's sense. Its predictions would be global workspace theory's (prefrontal
  content, ignition), so they would separate the account from integrated information theory but not
  from global workspace theory, and the account's testability would rise. No study in the pilot
  would count for it, because every one appeared before such a claim would be dated.
- **P2 (the account in one sentence)**, if adopted, would put "one space that the whole system can
  use" inside the central bet (core claim `sh-c1`), so `sh-c1`'s prediction would become partly a
  workspace prediction, shared in part with global workspace theory.

## Licence and credit

These records are under CC BY 4.0 (`LICENSE-DATA`). Quotations inside them are short excerpts kept
so each record can be checked; their copyright stays with their authors.
Five studies were found through the ConTraSt database (Yaron, Melloni, Pitts and Mudrik, *Nature Human Behaviour* 6,
593–604, 2022; https://contrastdb.tau.ac.il; CC BY-SA 4.0), used only as a reading list: no ConTraSt
field is copied here, and each record is built from the paper itself.
