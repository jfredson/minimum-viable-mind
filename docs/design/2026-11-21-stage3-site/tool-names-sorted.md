# Tool names on the site, sorted (2026-11-21)

*Written for John's review. John ruled on 2026-11-21, "Yes, sort them so", relayed by the master
session: every tool name on the site is sorted into one of three kinds, and nothing is changed until
he has seen the list. **Nothing on the site has been changed.** The site check has not been changed
either. The rule it would become is in the last section.*

The three kinds:

1. **Tested**: the model is what an experiment tested. Kept.
2. **Vendor**: a vendor in the spending record. Kept.
3. **Maker**: a tool named as how the work was made. Reworded.

**How the list was made.** The built site was read page by page, the way a visitor sees it, and
split into sentences. Every sentence that names a tool from the site check's list was kept: Claude,
Anthropic, Gemini, GPT, Sonnet, Opus, RunPod, and the rest of that list. There are **20 sentences**,
holding **31 names**. (The check counted 33 earlier because it scores "Claude Opus 5.5" twice.) All
20 are on the project's older pages, and none is on a tracker page.

Each sentence comes from the project record, `data/project.toml`; the record field is given so that
an approved rewording can be made at its source. Two sentences sit in a page template instead.

**Counts:**

| kind | sentences |
|---|---|
| 1, tested | 7 |
| 2, vendor | 5 |
| 3, maker (to reword) | 4 |
| hard to place (for John) | 4 |
| **total** | **20** |

Where one sentence shows on two pages, it is counted once per page. Sentences 6 and 8 are the same
words, on the learned page and the questions page.

## The list

| # | page | sentence (as shown) | record field | kind |
|---|---|---|---|---|
| 1 | /ladder/ | RunPod cloud bench replaced the planned 48 GB Mac mini | `stages[0].delivered[3]` | 3 |
| 2 | /ladder/ | Wager W1 (sycophancy reproduces) splits by family: fires for Gemini, loses for both Claude models. | `stages[3].delivered[2]` | 1 |
| 3 | /learned/ | Gemini 3.1 Pro, GPT and Claude Opus 5.5, by API, one fresh conversation each, two rounds. | `findings[F22].what` | hard (A below) |
| 4 | /learned/ | Two tiers: a context-isolated Claude Code worktree session, then two other-lab models. | `findings[F11].what` | 3 |
| 5 | /learned/ | A conventional sycophancy metric would report Gemini's tool cell as 90% capitulation; the three-way instrument shows about 87% masked and 3% capitulated. | `findings[F3].what` | 1 |
| 6 | /learned/ | Sycophancy as the field describes it is alive for Gemini and stale for Claude-family models. | `findings[F3].so_what` | 1 |
| 7 | /learned/ | Sonnet held the registered pattern leak-clean at a small margin. | `findings[F4].what` | 1 |
| 8 | /questions/ | Sycophancy as the field describes it is alive for Gemini and stale for Claude-family models. | `questions[Q4].current_answer` | 1 |
| 9 | /questions/ | The 'mind vs tool' framing wager lost overall; one leak-clean survivor (Sonnet) at a small margin. | `questions[Q4].current_answer` | 1 |
| 10 | /spend/ | Updated 2026-10-24: the balance read $65.62 after the split removal test's RunPod run (about $0.77, recorded with my go in the spending record). | `spend.account_note` | 2 |
| 11 | /spend/ | RunPod prepaid credits, auto-reload off, never loaded past the $80 account limit I set; topped up in increments I choose. | `spend.account_note` | 2 |
| 12 | /spend/ | Anthropic and Gemini API judge calls are billed separately and cost cents per run. | `spend.account_note` | hard (B below) |
| 13 | /spend/ | Source of truth: the compute ledger, reconciled against RunPod's own billing at each phase boundary. | template, `site/src/pages/spend.astro` | 2 |
| 14 | /story/ | Global workspace theory, integrated information theory and my own account were scored from 14 quoted core claims, 21 predictions, 9 study records and 50 judgements, each read by a Claude model and, blind, by Google's Gemini 4 Carbon. | `timeline[0].summary` | 3 |
| 15 | /story/ | About $1.05 spent on Gemini under my go of up to $10. | `timeline[0].summary` | 2 |
| 16 | /story/ | About $0.77 spent on RunPod under my go of up to $2, after the Mac ran hot; from now on model runs are planned on RunPod. | `timeline[1].summary` | hard (C below) |
| 17 | /story/ | The battery rehearsal started on my 'Go up to $50' and stopped on Google's daily limit of 250 requests to Gemini 3.1 Pro, with 437 calls kept and about $2.88 to $7.13 spent; it resumes a day at a time. | `timeline[3].summary` | 1 (and 2) |
| 18 | /story/ | A brief for outside models was checked against the record and revised, then put by API to Gemini 3.1 Pro, GPT and Claude Opus 5.5 in two rounds, every reply saved word for word. | `timeline[11].summary` | hard (A below) |
| 19 | /story/ | Claude Code agent picked up from Gate 0. | `timeline[40].summary` | 3 |
| 20 | /story/ | RunPod ticket submitted. | `timeline[44].summary` | 2 |

**Why each was placed where it is:**

- **Kind 1.**
  - Sentences 2 and 5 to 9 report results of the sycophancy and framing experiments, which were
    run on these models as their subjects.
  - Sentence 17 is the battery rehearsal. The battery's records count lost answers per model
    (`docs/filtered-battery-2026-10-07/`), so Gemini 3.1 Pro is the model under test there. The
    sentence is also a spending line, and both reasons keep it.
- **Kind 2.**
  - Sentences 10, 11, 13 and 15 state spending with the vendor the spending record names.
  - Sentence 20 is the support request about the billing incident on the $97 run, so it belongs
    with the spending too.
- **Kind 3.**
  - Sentence 1 names where the work was run, not what it tested or what was paid for.
  - Sentences 4 and 19 name the coding tool that did the work.
  - Sentence 14 names the two readers of the tracker's judgements. John's ruling of 2026-11-21 on
    About ("Yes, keep it") is that the public text says AI models made by different companies, and
    names no model.

## Proposed rewordings (kind 3), not yet made

| # | now | proposed |
|---|---|---|
| 1 | RunPod cloud bench replaced the planned 48 GB Mac mini | A rented cloud machine replaced the planned 48 GB Mac mini |
| 4 | Two tiers: a context-isolated Claude Code worktree session, then two other-lab models. | Two tiers: first an AI reviewer that has not seen the working notes, then two AI models from other companies. |
| 14 | …50 judgements, each read by a Claude model and, blind, by Google's Gemini 4 Carbon. | …50 judgements, each read by two AI models made by different companies, the second without seeing the first's answer. |
| 19 | Claude Code agent picked up from Gate 0. | The work picked up again from Gate 0. |

Sentence 19 still says "Gate 0", which is the project's own shorthand. Rewording that is outside
this ruling, and is left as it stands.

## For John: sentences hard to place, one per sentence

**A. Sentence 3 (/learned/, finding F22) and sentence 18 (/story/, timeline entry of the outside poll).**
- **Why it is hard:** these three models were not tested. They were asked, as outside readers, to
  judge the project's own claims, so they are tools used to check the work. But which models were
  asked bears on how far a reader can trust the verdict, especially because the finding itself
  says the three replies "are correlated, not independent". The workspace rule keeps a tool's name
  where it bears on trust.
- **Options:**
  - (a) Keep the names, as a disclosure that bears on trust.
  - (b) Reword to "three AI models from three companies", as the About page now does for the
    readers.
- **Lean:** (b), to match the ruling on About. The model names stay in the record's method files.

**B. Sentence 12 (/spend/): "Anthropic and Gemini API judge calls are billed separately and cost cents per run."**
- **Why it is hard:** it is a spending line, which makes it kind 2. But "judge calls" says these
  models were used as judges in the experiments, which is a maker's role. In some runs Claude was
  also a subject under test.
- **Options:**
  - (a) Keep it, as a vendor line.
  - (b) Reword it to "Calls to the AI companies' services are billed separately and cost cents per
    run", which keeps the spending fact and drops the names.
- **Lean:** (a). It is on the spending page, and the spending record names the vendors.

**C. Sentence 16 (/story/): "About $0.77 spent on RunPod under my go of up to $2, after the Mac ran hot; from now on model runs are planned on RunPod."**
- **Why it is hard:** the first half is a spending line (kind 2). The second half says where the
  work will be run (kind 3).
- **Proposed:** keep the first half, and reword the second to "…from now on model runs are planned
  on rented machines."

## The rule the check would become, once this list is approved

Today `scripts/check_site.py` exempts six whole pages: the ladder, learned, story, spend, plain
explanation and questions pages. On those pages a tool name is reported, and not refused.

Once John approves this list, the exemption becomes a list of sentences:

- A new file, `scripts/tool-names-allowed.toml`, holds each approved kind 1 or kind 2 sentence word
  for word, with its kind and its record field.
- On every page, a tool name is allowed only inside a sentence on that list.
- Anything else is refused, on every page: a kind 3 sentence not yet reworded, or a new sentence
  that names a tool.

Changing an allowed sentence's wording then needs the list changed with it, so a new tool name
cannot slip in unseen. The check stays as it is until the list is approved.
