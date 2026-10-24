# The spending record: every dollar spent, every vendor, with the go it was spent under

*Started 2026-10-18 on John's ruling of that day
(`docs/rulings/2026-10-18-spending-ruling.md`): every new spend needs its own
go, and every dollar actually spent is tracked here, all vendors together.
This is a record, not a budget. The detailed sources stay where they are:
the compute ledger for rented machines
(`experiments/06-mvm-0a-constructed-self-index/compute-ledger.md`), and the
TimeAssembler worklog's before and after rows for API runs. A figure here
cites its source.*

*Status of this file: started, not yet complete. The rows before 2026-10-18
are what the record holds today; compiling every earlier API call with its
source is the roadmap step "Compile the exact spend across every vendor".
Until it is done, the total below is a range.*

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

## Running total

| | Figure | Source |
|---|---|---|
| Rented machines, 2026-08-07 to the stop of experiment C | $230.94 | the compute ledger's running total |
| Spend before the ledger opened, and API calls to 2026-08-30 | about $100 to $119 | John's figure of about $281 to $300 of true spend across every vendor, in his binding rulings of 2026-08-30 quoted at the top of `experiments/06-mvm-0a-constructed-self-index/amendment-a3.md`; the ledger then read about $181 (its 2026-08-17 row, "~$181.4 / $400 (A2)") |
| API calls logged since 2026-08-30 | at least about $4 to $8 | the rows below |
| **Total spent, every vendor** | **roughly $335 to $360** | still being compiled |

## Spends since 2026-10-18, each with its go

| Date | What | Vendor | The go | Estimate and ceiling | Spent | Source |
|---|---|---|---|---|---|---|
| 2026-10-18 | Measurement rehearsal of battery entries 1 and 2, first start | Anthropic and Google, by API | "Go up to $50" (John, relayed by the fifth master session) | $18.26 to $37.86; ceilings $27 for entry 1 and $23 for entry 2 | about $2.88 to $7.13 by the runner's estimate; true bill on the vendors' consoles | worklog rows 4110fb03 (before) and 255fff69 (after) |
| 2026-10-19 | The same rehearsal, second start, both entries to the end | Anthropic credits (key ending 3AAA) and Google, by API | the same go and ceilings | as above | the second start alone: about $18.01 to $33.36 by the runner's estimate (the whole run, both starts, is about $20.89 to $40.49: Anthropic about $13.06, Gemini about $7.83 to $27.43); Google refused no payment against a $20.00 prepaid balance; true bill on the vendors' consoles | `docs/filtered-battery-2026-10-07/rehearsal-run-record-2026-10-19.md`; the worklog row after |
| 2026-10-19 | Entry 1's far-end gate, repair step 1 (a diagnosis; 383 calls) | Anthropic credits (key ending 3AAA) and Google, by API | "Agreed" (John, to option (c), relayed by the sixth master session) | about $0.48 to $2.00; ceiling $5 | about $1.12 by the runner's estimate | `docs/filtered-battery-2026-10-07/farend-repair-step1-result-2026-10-19.md`; worklog row e45c580e (before) |
| 2026-10-24 | The split removal test's two free fixes, the rest of the run (two swap bounds and six removal checks), moved off the Mac because it was running hot | RunPod, one RTX 4090, community cloud | "Go on RunPod for the rest of the Minimum Viable Mind run, up to $2. I'll put my Hugging Face token on the pod." (John, relayed by the fourth weekend master session) | about $0.70; ceiling $2.00, enforced by deleting the machine from the laptop 2 hours after creation | to be filled after the run, from RunPod's billing rows (balance before: $66.38) | `experiments/09-split-removal-test/rehearsal/fixes-findings-2026-10-24.md`; the worklog rows before and after |

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

## Earlier API spends known so far (to be completed)

| Date | What | Vendor | The go | Spent | Source |
|---|---|---|---|---|---|
| 2026-10-09 | Gate A tier 2 on the two-sided question text | Google and OpenAI, by API | the protocol's tier 2 step, run by API | about $1.04 at most | `docs/reviews/2026-10-09-two-sided-question-gate-a-INDEX.md`, "What it cost" |
| 2026-10-07 | The outside-perspective poll | several vendors, by API | John's go for the poll | not yet compiled | `docs/outside-perspective/2026-10-07-poll-method.md` |
