# The spending record: every dollar spent, every vendor, with the go it was spent under

*Started 2026-10-18 on John's ruling of that day
(`docs/rulings/2026-10-18-spending-ruling.md`): every new spend needs its own
go, and every dollar actually spent is tracked here, all vendors together.
This is a record, not a budget. The detailed sources stay where they are:
the compute ledger for rented machines
(`experiments/06-mvm-0a-constructed-self-index/compute-ledger.md`), and the
TimeAssembler worklog's before and after rows for API runs. A figure here
cites its source.*

*Completed 2026-10-25 (roadmap task "Complete docs/spending-record.md",
`df06b472`) by a working session that ran nothing and spent nothing: every
figure below comes from a committed file, the worklog, or arithmetic on
token counts the providers returned. A dollar that could not be traced to a
source is listed under "Untraced" and is not in the total. Where a figure is
an estimate rather than a bill, the row says so.*

## The total

**About $419 to $439 spent across every vendor, from the first rented
machine on 2026-07-12 to 2026-10-24**, plus the untraced amounts listed
below, which are not in it.

| Part | Figure | How firm |
|---|---|---|
| Rented machines (RunPod), 2026-07-12 to 2026-10-24 | $304.38 | Measured: money put into the account less the balance left, checked against RunPod's own billing exports (see "How the rented-machine figure was checked") |
| Google, the Stage 3 grid's Gemini arm, 2026-08-02 | $49.77 | Billed: Google Cloud's August bill |
| Anthropic, the Stage 3 grid's Claude arm, 2026-08-02 | at least $40.56 | Billed in part: two of the three automatic top-ups the run set off; the third is untraced |
| API calls since 2026-10-07 (the poll, Gate A tier 2, the battery rehearsal, the far-end repair) | about $24.72 to $44.32 | Estimated from token counts or the runner's records; the true bills are on the vendors' consoles |
| **Total traced** | **about $419.43 to $439.03** | the range comes only from the estimates in the last line |

Of that, about $394.71 is billed or measured, and the rest is estimated.
The low end of the range assumes Gemini billed no thinking in the battery
rehearsal; the high end assumes the most it could have.

**Out of pocket and from credits.** Only the battery rehearsal's and the
far-end repair's Anthropic calls are recorded as paid from John's Max-plan
credits (about $13.06, plus a share of the repair's $1.12). Everything else
in the total is not recorded as paid from credits; the poll's Anthropic call, for one, drew on the same organisation balance the credits now cover.

## Every line, by vendor

### Rented machines (RunPod)

| Dates | What | The go | Spent | Source |
|---|---|---|---|---|
| 2026-07-12 to 2026-08-06 | Before the ledger opened: the removal test (experiment 1) and other early rented work | Before goes were recorded per run; John's own work and approvals. No go is on record for any of it | $42.85 | RunPod billing exports, quoted in `docs/w37-spend-review-2026-09-16.md`, section 6 ("of which before the ledger opened") |
| 2026-08-07 to 2026-09-16 | The ledger's rows from the first pilot to the A3 self-delete test, including the lost pilot of a model with 30 million adjustable numbers ($97.04) and its re-run (about $18.90), plus storage on days with no machine | Each machine row's go is in the compute ledger: the registered caps of 2026-08-07 ($200) and 2026-08-16 ($400, Amendment A2), and John's go per launch, except about $17.82 of the lost pilot, spent after its safety cut-off failed, which no go covered. The storage has no go | $215.33 (machines $194.03, storage $21.31) | the same section 6, "of which ledger era"; the compute ledger's rows |
| 2026-09-17 | Amendment A3's second and third training runs (different random starts), launched together | "Go" (John, quoted in the ledger row) | $20.10, from measured machine lifetimes | compute ledger, row of 2026-09-17 |
| 2026-09-19 | The control-learnability pilot (unregistered) | "Go. Launch the control-learnability pilot as staged…" (John, quoted in the ledger row) | about $9.90 | compute ledger, row of 2026-09-19 and its correction of 2026-09-21 |
| 2026-09-20 | Recovery of that pilot's final checkpoint | "Go, recover the checkpoint, and kill the watchdog." (John) | $0.07 | compute ledger, row of 2026-09-20 |
| 2026-09-20 | The two follow-up reading runs, refused by the instrument's own check and deleted | "Go" (John, quoted in the ledger rows) | $1.90, measured from the balance | compute ledger, the two rows of 2026-09-20 |
| 2026-09-21 and 2026-09-25 | Three attempts at the small rented rehearsal slice | The rehearsal line of the first release, each row quoting John's go | about $0.57 ($0.02, $0.50 and $0.05) | compute ledger, the rows of 2026-09-21 and 2026-09-25 |
| 2026-10-04 | Four development runs of the successor experiment, on models of 10 million adjustable numbers | John's go for the development runs, quoted in the rows | $1.47 | compute ledger, the four rows of 2026-10-04 |
| 2026-10-09 | Three verification reruns of the successor experiment, same size | The registered repair, about $1.14 approved; billed $0.16 over at the $1.19 hourly rate | $1.30 | compute ledger, the three rows of 2026-10-09 |
| 2026-10-24 | The split removal test's two free fixes, moved off the Mac | "Go on RunPod for the rest of the Minimum Viable Mind run, up to $2…" (John, relayed by the fourth weekend master session) | about $0.77 | `experiments/09-split-removal-test/rehearsal/fixes-findings-2026-10-24.md`; the row in the table further down |
| 2026-09-17 to 2026-10-24 | Storage for the network volume on days with no machine, which has no ledger row | **None.** It is a standing charge, about $0.24 a day since late September | about $10.12, by subtraction | the measured total less every row above |
| **All rented machines** | | | **$304.38** | |

### Google (Gemini)

| Date | What | The go | Spent | Source |
|---|---|---|---|---|
| 2026-08-02 | The Stage 3 registered grid (the retained-independence experiment), the part run on Gemini (31 of 360 subjects before Google's quota stopped it), Vertex AI, project "CoWork" | The registered grid, launched 2026-08-02; no spending go is on record, and this was before the all-vendor ruling of 2026-08-30 | $49.77 | Google Cloud's August bill, traced in worklog entry "Cost finding: the Stage 3 Gemini arm cost $49.77…" (`558a695a`) |
| 2026-10-07 | The outside-model poll, Gemini 3.1 Pro, both rounds | "Go" (John, quoted in the poll's method file) | about $0.14, estimated | token counts in `docs/outside-perspective/replies/2026-10-07-manifest.json` (26,228 in; 7,290 out, thinking included) at $2 and $12 per million, the rate the Gate A index used |
| 2026-10-09 | The outside review of the two-sided question text by two other companies' models (Gate A, tier 2), Gemini 3.1 Pro | The review protocol's tier 2 step, run by API. The overseer's brief said to stop before any tier costing more than about $1; the session went ahead on the expected cost, so no go covered the part above $1 | about $0.16, estimated | `docs/reviews/2026-10-09-two-sided-question-gate-a-INDEX.md`, "What it cost" |
| 2026-10-18 and 2026-10-19 | The battery rehearsal, entries 1 and 2, both starts, Gemini share | "Go up to $50" (John) | about $7.83 to $27.43, estimated | `docs/filtered-battery-2026-10-07/rehearsal-run-record-2026-10-19.md`, "Spend". Google's prepaid balance of $20.00 refused no payment in the second start, so the true high end is a little lower |

### OpenAI

| Date | What | The go | Spent | Source |
|---|---|---|---|---|
| 2026-10-07 | The outside-model poll, GPT-6 Astra, both rounds | "Go" (John) | about $0.81 at most, estimated | the poll's manifest (32,280 in; 12,250 out) at an assumed $10 and $40 per million, the deliberately high rate the Gate A index used, since no rate for this model is on record |
| 2026-10-09 | The same outside review, GPT-6 Astra | As for the Gemini row of that day | about $0.88 at most, estimated | the Gate A index, "What it cost" |

### Anthropic

| Date | What | The go | Spent | Source |
|---|---|---|---|---|
| 2026-08-02 | The Stage 3 registered grid (the retained-independence experiment), the part run on Claude models (720 of 720 subjects) | As for the Gemini row of that day | at least $40.56: two automatic top-ups of $20.38 and $20.18; a third fired the same day and its amount was never recorded | worklog entries `558a695a` and "RULED 2026-08-30 — the A2 $400 ceiling means ALL MVM compute across vendors…" (`a3834db7`) |
| 2026-10-07 | The outside-model poll, Claude Opus 5.5, both rounds | "Go" (John) | about $0.72, estimated | the poll's manifest (40,681 in; 20,615 out) at $5 and $25 per million, the Opus rate the battery runner uses; no rate for this model is on record in the repository |
| 2026-10-18 and 2026-10-19 | The battery rehearsal, Anthropic share, both starts | "Go up to $50" (John); vendor "Anthropic credits" for the second start, through the key ending 3AAA | about $13.06, estimated | the rehearsal run record, "Spend" |
| 2026-10-19 | Entry 1's far-end gate, repair step 1 (both vendors together) | "Agreed" (John, to option (c)) | about $1.12, estimated | `docs/filtered-battery-2026-10-07/farend-repair-step1-result-2026-10-19.md`, "Cost" |

### Reviews that cost nothing per call

The outside reviews of 2026-09-25 (Amendment A3's closure text) and
2026-10-06 (the successor's registration, version 4) were run by John in the
ChatGPT and Gemini apps under his own subscriptions, and filed word for word
(`experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-21-a3-closure-*.md`
and `2026-10-04-successor-v4-*.md`). The programme review of 2026-09-20 was pasted
in by John through the same two apps and likewise has no row. They added nothing to any bill, so they
carry no row. Every run on the Mac, including the split removal test's
rehearsal on 2026-10-24 before it moved to RunPod, cost $0.

## Untraced

These were found in the record but could not be traced to a bill or a row,
so they are **not in the total**.

1. **The third Anthropic top-up on 2026-08-02.** It fired the same day as
   the two recorded ones, during the Stage 3 grid's Claude arm, and its
   amount was never written down. John's figure of 2026-08-30 allowed up to
   about $18 for it. Anthropic's console, Billing page, holds it.
2. **Experiment 1's judge calls and its outside design review, July 2026.**
   The removal test's self-report battery was scored by Claude Opus through
   the API (`experiments/01-self-indexing-removal-test/src/judge.py`), and its
   design was attacked by Gemini 3.1 Pro and answered by Claude through the
   API (`red_team.py` and `defend.py` beside it). The paper puts the judge
   calls at "low tens of dollars". No bill or worklog row for any of it was
   found.
3. **Any Stage 3 calls before the registered grid of 2026-08-02**, such as
   pilots. None is recorded with a cost.
4. **Google Cloud's July bill of $2.86, and the $2.75 of August's bill
   ($52.52) outside the Gemini arm's $49.77**, which the 2026-08-30 finance
   review did not attribute to anything. They may not be this project's.

Together these could be roughly $20 to $50, on the paper's own words and
John's 2026-08-30 allowance, but that is a guess and is not counted.

## How the rented-machine figure was checked

Money put into the RunPod account: $150 before the ledger opened, then
$25.00 on 2026-08-12, $75.00 on 2026-08-15 and $120.00 on 2026-08-16, which
is $370.00 (the compute ledger, "Reconciliation baseline"). No top-up is
recorded after 2026-08-16, and every balance the record reads after it is
lower than the one before. The balance after the machine of 2026-10-24 was
deleted was $65.62. So the account has spent **$370.00 − $65.62 = $304.38**.

Two checks agree with it:

- RunPod's own billing exports put all spend from 2026-07-12 to 2026-09-16
  at $258.18. That implies a balance of $111.82 on 2026-09-16, and the
  ledger read $111.74 that day, after the self-delete test: 8 cents apart.
- From 2026-09-26 ($75.86, after the last slice attempt) to 2026-10-24
  ($66.38, before the split-test machine), the balance fell $9.48, of which
  $2.77 is the development runs and reruns. The other $6.71 over 28 days,
  about $0.24 a day, matches one 100 GB network volume's standing charge.

This assumes the RunPod account served only this project, which is what
every record of it says.

## Why the total is higher than the range of roughly $335 to $360

The range of 2026-10-18 added the ledger's $230.94 to John's 2026-08-30
estimate less the ledger of that date, plus the API calls logged by then.
Three things were missing from it:

- **The rented machines before the ledger opened, $42.85.** John's
  2026-08-30 figure of about $281 to $300 was the RunPod balance's spend
  since 2026-08-07 (about $191.3), the Gemini arm ($49.77) and the Anthropic
  top-ups (about $40.56 and the third). It did not include the earlier
  RunPod spend.
- **Storage on days with no machine since 2026-08-30, about $20,** which has
  no ledger row.
- **The poll of 2026-10-07 (about $1.67), the battery rehearsal's second
  start and the far-end repair, about $21 to $36 together.** The poll was
  never added, and the other two ran after the range was written. (The
  range's top end also allowed about $19 for the third Anthropic top-up,
  which is now listed as untraced instead.)

The spending review of 2026-09-16 (`docs/w37-spend-review-2026-09-16.md`,
section 6) rebuilt John's 2026-08-30 figure differently, as the earlier
RunPod spend plus the RunPod spend since 2026-08-07 plus the Gemini arm, and
gave a "known all-vendor spend" of $307.95. That rebuild left out the
Anthropic top-ups of 2026-08-02 (at least $40.56), which the ruling of
2026-08-30 counted. This record counts both the earlier RunPod spend and the
Anthropic top-ups, so it supersedes that rebuild.

## What needs John's ruling

1. **The network volume's standing charge has no go.** It is about $0.24 a
   day (about $7 a month) for as long as the volume exists, and the
   spending ruling says every new spend needs its own go. Either a go for it
   as a standing line, or deleting the volume once its files are confirmed
   held elsewhere; deletion cannot be undone and is John's call.
2. **The third Anthropic top-up of 2026-08-02** can only be read on
   Anthropic's console, which a session cannot see. If John reads it, it
   moves from "Untraced" into the total.
3. **The paper's cost sentence** says experiment 1 ran for "about $10 to $20
   of rented consumer GPU time". RunPod's exports show $42.85 of rented
   machines before the ledger opened. Some of that may be other work, but
   the sentence should be checked against this record in the paper's
   readiness steps.

## Anthropic credits (added 2026-10-18)

John said on 2026-10-18 that his Max plan includes $200 of Anthropic API
credits every month, resetting on the 2nd. Anthropic's pages say unused credit
expires at the end of each cycle and does not roll over. His rule for runs paid
from those credits (relayed by the fifth master session, 2026-10-18): a single
job expected to cost more than about $50 comes to him first, with the number
and what it buys; smaller credit-paid runs do not need his go, but each is
recorded here, with the vendor written "Anthropic credits". Spend out of
pocket still needs his go first, as in the spending ruling. Writing the vendor
this way lets the total be read two ways: everything spent, and what came out
of pocket. Minimum Viable Mind has no Console workspace or key of its own yet;
it is proposed to John, and until it exists these runs are not on the credits.
The guide is `timeassembler/docs/session-routing.md`. Outside reviews and
second readers stay on a non-Claude model whatever the credit balance.

## Spends since 2026-10-18, each with its go

| Date | What | Vendor | The go | Estimate and ceiling | Spent | Source |
|---|---|---|---|---|---|---|
| 2026-10-18 | Measurement rehearsal of battery entries 1 and 2, first start | Anthropic and Google, by API | "Go up to $50" (John, relayed by the fifth master session) | $18.26 to $37.86; ceilings $27 for entry 1 and $23 for entry 2 | about $2.88 to $7.13 by the runner's estimate; true bill on the vendors' consoles | the worklog row written before the first start (`4110fb03`) and the one written after it (`255fff69`) |
| 2026-10-19 | The same rehearsal, second start, both entries to the end | Anthropic credits (key ending 3AAA) and Google, by API | the same go and ceilings | as above | the second start alone: about $18.01 to $33.36 by the runner's estimate (the whole run, both starts, is about $20.89 to $40.49: Anthropic about $13.06, Gemini about $7.83 to $27.43); Google refused no payment against a $20.00 prepaid balance; true bill on the vendors' consoles | `docs/filtered-battery-2026-10-07/rehearsal-run-record-2026-10-19.md`; the worklog row after |
| 2026-10-19 | Entry 1's far-end gate, repair step 1 (a diagnosis; 383 calls) | Anthropic credits (key ending 3AAA) and Google, by API | "Agreed" (John, to option (c), relayed by the sixth master session) | about $0.48 to $2.00; ceiling $5 | about $1.12 by the runner's estimate | `docs/filtered-battery-2026-10-07/farend-repair-step1-result-2026-10-19.md`; the worklog row written before the repair's first call (`e45c580e`) |
| 2026-10-24 | The split removal test's two free fixes, the rest of the run (two swap bounds and six removal checks), moved off the Mac because it was running hot | RunPod, one RTX 4090 graphics card, from its cheaper shared pool | "Go on RunPod for the rest of the Minimum Viable Mind run, up to $2. I'll put my Hugging Face token on the pod." (John, relayed by the fourth weekend master session) | about $0.70; ceiling $2.00, enforced by deleting the machine from the laptop 2 hours after creation | about $0.77: the balance fell from $66.38 to $65.62 (machine created 13:31:39 PDT, deleted 14:25:22 PDT at the master session's instruction; a secure-cloud RTX 4090 at $0.89 an hour, because no community-cloud one was free); RunPod's billing row for the day not yet posted | `experiments/09-split-removal-test/rehearsal/fixes-findings-2026-10-24.md`; the worklog rows before and after |

Later starts of the same rehearsal run under the same go and ceilings, and
each adds a row.

**Which key and which pocket.** The first start's Anthropic calls (about 184
of its 437) went through the Anthropic key in `minimum-viable-mind/.env` that
ended GQAA, in the default Console workspace. By the session-routing guide
(`timeassembler/docs/session-routing.md`) that key was Minimum Viable Mind's
own, so no call went through another project's key. From the later starts on,
the key is Minimum Viable Mind's new one, workspace `mvm-judge`, ending 3AAA,
set up on 2026-10-18. Under the addendum to the spending ruling, the
Anthropic share is paid from John's Max-plan credits (vendor "Anthropic
credits": recorded, no go needed below about $50 a job), and the Gemini share
is out of pocket and stays inside his "Go up to $50".

