# The weekly reading: how new studies reach the tracker of theories of consciousness

*Written 2026-11-21 by the stage 3 scoring session, at John's request ("Yes, build the weekly
reading after the searches"). Modelled on the AGI Zeitgeist's weekly reading
(`agi-zeitgeist/docs/weekly-reading.md` and `weekly-reading-prompt.md`). What was ruled is marked
*(ruled)*; everything else, the schedule included, is a proposal until John rules on it.*

## The idea in one paragraph

Each theory on the site is scored from studies chosen by fixed searches, written down and committed
before they ran. Once a week, a fresh Claude session runs those same searches again, unchanged. It
keeps what has appeared since the last run, and reads each new paper's title and summary against the
prediction it was searched for. Where a paper is a real test of that prediction, it adds a dated row
to a waiting list, with a first reading of whether the prediction was on record in time and which way
the result went. It never changes a score. A study counts only when a working session has made the
full record and Google's Gemini has read every judgement on it blind, by the same rules as every
other study. Meanwhile the site shows how many studies are waiting.

## What was ruled (2026-11-21)

- *(ruled)* The weekly reading runs as a **cloud routine on John's Claude plan**. It does the search
  and the first reading, with no API key and no API spend.
- *(ruled)* **Gemini's blind second reading runs in working-session batches**, each with an estimate
  and a cap agreed with John before any call.
- *(ruled)* It **keeps running through the hibernation** from 2027-01-04.
- *(ruled)* The **site shows how many new studies are waiting to be scored**.
- *(ruled)* It **never changes a score on its own**.

## What the reading may and may not do

It **may**:
- run the fixed searches in `data/tracker/searches-*.toml`, exactly as written, and save their raw
  results in a new dated folder, `data/tracker/search-runs-<date>/`;
- compare the ConTraSt database's live list of papers with the list it has seen before, used as a
  reading list only, as ruled at stage 1;
- append rows to `data/tracker/waiting.toml`, one per new paper and prediction that qualifies;
- write the reading record `data/tracker/readings/<date>.json`, once, never edited afterwards;
- commit those files and push them (see "Where it pushes").

It **may not**:
- edit or delete any existing row, in any file;
- add or change a study record, a judgement, a ruling, a theory, a core claim or a prediction;
- change a search's wording, add a search or drop one. A search that has stopped working is flagged,
  and John rules on any change;
- call Gemini or any paid service;
- decide anything two readers could disagree on, beyond its own first reading. What a paper means
  for a score is decided later, by the same rules as every other study.

Anything outside those limits becomes a `flagged` item: what it would have done, and why it stopped.

## The four parts of a reading

1. **The fixed searches.** `python3 scripts/tracker_weekly.py search` reruns every search in
   `data/tracker/searches-*.toml`, saves the raw results, and lists the results that were in no
   earlier run. Today that is the 37 per-prediction searches for the five theories ConTraSt does not
   cover: Seth's view, attention schema theory, the sensorimotor theory, Orchestrated Objective
   Reduction and Damasio's theory.
2. **ConTraSt.** `python3 scripts/tracker_weekly.py contrast` lists papers new to ConTraSt that are
   marked as designed to test global workspace, integrated information, higher-order or first-order
   (recurrent processing) theories. Those are the four families it covers, and the stage 3 studies for
   them were chosen from its list. The seen list holds DOIs only (the papers' permanent identifiers),
   no ConTraSt field, so nothing under ConTraSt's share-alike licence is copied.
3. **Screening.** Each new result is read, title and summary only, against the screening rule fixed
   in `data/tracker/searches-2026-11-21.toml` (point 2 of its method). A result that qualifies
   becomes a waiting row. One that doesn't is listed in the reading record with the reason, as the
   baseline screens were.
4. **The first reading.** For each waiting row, the session opens the paper if an open copy exists.
   It never gets past a paywall or a robot check. It writes its first reading into the row:
   - whether the prediction was on record before the study could be known, under ruling D and the
     own-lab dating ruling;
   - and, if so, which way the result went.

   The reading is marked as a first reading by one reader, and it scores nothing.

The Sentient Horizons account has no study search, because none of its predictions has been tested.
New positions on the Working Positions page are not part of this reading.

## The waiting list

`data/tracker/waiting.toml` is appended to and never edited. A row stops waiting only when a later
`[[resolved]]` entry names it.

    [[waiting]]
    id = "w-2026-11-24-01"            the reading's date, then a two-digit counter
    found_on = "2026-11-24"           the reading that found it
    reading = "2026-11-24"            the reading record it belongs to
    prediction = "seth-interoceptive-suppression"
    europepmc_id = "..."              and doi, pmcid where given
    title = "..."
    authors = "..."
    first_appeared = "2026-11-19"     its earliest public date, as Europe PMC gives it
    screen = "Qualifies: ..."         why it is a test of this prediction, in a sentence
    opened = true                     whether an open copy was read
    first_reading = { commitment = "before", outcome = "for", reason = "...", unsure = false }

    [[resolved]]
    waiting = "w-2026-11-24-01"
    how = "scored"                    or "dropped", with why
    on = "2026-12-05"
    study = "smith-2026"              the study record it became

A working session turns waiting rows into study records and judgements, sends the blind packets to
Gemini in one batch under a cap, settles by the ruled rules, and adds a `[[resolved]]` entry. Only
then can a score move.

## The reading record

One file per run, `data/tracker/readings/<date>.json`, never edited:

    {
      "reading": {
        "date": "2026-11-24", "window_start": "2026-11-18", "window_end": "2026-11-24",
        "commit_before": "abc1234", "by": "scheduled",
        "searches": 37, "new_results": 12, "waiting_added": 2, "flagged": 0
      },
      "items": [
        { "id": "seth-interoceptive-suppression", "verdict": "waiting",
          "found": "One plain sentence.", "new_results": ["MED:..."], "waiting_rows": ["w-2026-11-24-01"] },
        { "id": "contrast", "verdict": "quiet", "found": "No new paper marked designed to test." }
      ]
    }

Verdicts: `quiet` (nothing new), `noted` (new results, none qualifies, each with its reason),
`waiting` (rows added), `flagged` (something the reading may not decide; `for_john` says what and
why). `python3 scripts/tracker_weekly.py check` validates the waiting list and every reading record.

## What the site shows

`python3 scripts/tracker_weekly.py count` gives the number of studies waiting to be scored, in all
and by theory, with the date of the last reading. A study waiting for two predictions is counted once.
The site's export reads it from `waiting_counts()` in `scripts/tracker_weekly.py`. The proposed line,
for the site session to place and word: "4 new studies are waiting to be scored (last weekly reading
24 November 2026)." Theory pages could carry their own count. When nothing waits: "No new studies
are waiting to be scored (last weekly reading ...)."

## Proposals for John

1. **The day and time: Tuesday 06:00 Pacific.** Proposed. The Upgrade Tree's reading has Sunday
   18:00 and the AGI Zeitgeist's has Monday 06:00, so Tuesday keeps the three apart, and Europe PMC
   has indexed the previous week's papers by then. Alternative: Monday 07:00, beside the AGI
   Zeitgeist's.
2. **Where it pushes.** Proposed: one commit, pushed to `main`, as the AGI Zeitgeist's routine does,
   so the site's count updates. It touches only the files listed above, and the site's checks run on
   the push. If the push is refused, the same commit goes once to `claude/reading-<date>` and the
   report says so. Alternative: always a branch, merged by a working session; the count then lags.
3. **New studies are added beside the five chosen, not instead of them.** Proposed. The ruled rule
   takes "the five most recent qualifying studies per theory". Applied every week, it would swap older
   studies out of the score as newer ones arrived, so the scored set would turn over by date alone.
   Proposed: the five-most-recent rule chose the first set; a later qualifying study joins it. *Weakest
   step:* busy topics will gather many studies over time, which the one-per-prediction cap was meant
   to prevent; the cap could apply per reading instead.
4. **The window.** The seven days ending on the reading's date, Pacific. What makes a result new is
   that no earlier run returned it, not its date. A paper indexed late is still caught, and the record
   says how old it is.

## How it is run

The cloud routine's prompt says only to open the repository and follow
`docs/weekly-reading-prompt.md`, so the procedure can change without touching the routine. A run by
hand in a working session follows the same file and records `by = "hand"`.

## What it costs

Nothing in money. The routine runs on John's Claude plan, Europe PMC's search is free, and no Gemini
call is made. Gemini's batches are separate. At the stage 3 rate of about 2 cents a call, a batch of
20 judgements costs about 40 cents before December 1st and about 80 cents after; each batch comes to
John with its estimate and cap.
