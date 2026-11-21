# The weekly reading: the standalone instruction for the scheduled run

*Written 2026-11-21. A fresh Claude session with no memory of any earlier conversation follows this
file from top to bottom. The routine's own prompt says only to open the repository and follow this
file. Where this file and `docs/weekly-reading.md` disagree, this file wins for the run, and the
disagreement is flagged for John.*

## 0. Orient

- Get the date in John's time zone first: `TZ=America/Los_Angeles date +%F`. That is the reading's
  date. The window is the seven days ending on it. Write every date as year-month-day.
- The repository is a fresh clone of `https://github.com/jfredson/minimum-viable-mind`. Bring `main`
  up to date: `git fetch origin && git checkout -B main origin/main`. If the working tree has changes
  that are not yours, stop and say so in the report.
- Record `git rev-parse --short HEAD` as `commit_before`.
- Read `docs/weekly-reading.md`, the header comment of every `data/tracker/searches-*.toml` file
  (the screening rule is point 2 of its method), and `data/tracker/README.md`.
- If a reading record for today already exists, name this one `<date>-2`.

## 1. Run the fixed searches

    python3 scripts/tracker_weekly.py search --date <date>

This reruns every search exactly as written and saves the raw results to
`data/tracker/search-runs-<date>/`. Do not change, add or drop a search. If Europe PMC fails after
the script's own retries, stop the reading, flag it, and commit nothing but the reading record.

## 2. ConTraSt

    python3 scripts/tracker_weekly.py contrast --record

Note each new paper it lists, by DOI and title only. Use ConTraSt as a reading list: copy none of its
fields. A new paper marked as designed to test one of the four families is screened in step 3 against
that theory's predictions in `data/tracker/predictions.toml`. If none fits, the paper is `noted`, not
added.

## 3. Screen every new result

Open `data/tracker/readings/<date>.candidates.json`. For each new result, read its title and summary
against the prediction it was found for (its `test_for` and `test_against` in
`data/tracker/predictions.toml`) and apply the screening rule exactly. Apply point 2 of the method (what
qualifies), not point 3 (the five most recent, one per prediction): point 3 chose the first set only,
and every qualifying result now becomes a waiting row that joins the scored studies once scored,
with nothing dropping out (John, 2026-11-21, "Join, nothing drops"). Reviews, theory papers, models
with no new data, comments and protocols never qualify. For every result, write one line: qualifies,
or does not qualify, with the reason.

## 4. First reading of each qualifying paper

- Look for an open copy: Europe PMC full text
  (`https://www.ebi.ac.uk/europepmc/webservices/rest/<PMCID>/fullTextXML`), the publisher's open page,
  or bioRxiv, PsyArXiv or arXiv. Never get past a paywall or a robot check. If there is no open copy,
  set `opened = false`, give no reading, and say what would open it.
- If opened, give the first reading:
  - **commitment:** was the prediction fixed by the theory's proponents before they could have known
    this study's result? Use the prediction's `first_stated` date and ruling D: before the
    registration for a registered study, before the earliest public appearance for any other study,
    before the data first appeared for a reanalysis. If the study's authors include an author of a
    proponents' statement in `data/tracker/sources.toml`, use the own-lab rule: before their lab had
    the data, shown by a registration or methods dates, else "unclear".
  - **outcome**, only if the commitment is "before": for, against or mixed, by the prediction's own
    test wording.
  - Give two to four plain sentences of reason, and mark `unsure` honestly.

## 5. Append, record, check

- Append one `[[waiting]]` row per qualifying paper and prediction to `data/tracker/waiting.toml`, in
  the form `docs/weekly-reading.md` gives. Never edit an existing row.
- Write `data/tracker/readings/<date>.json`: the header and one item per search that returned new
  results, one for ConTraSt, and one per flag.
- Run `python3 scripts/tracker_weekly.py check`. If it fails, fix what you wrote; never touch an older
  row to make it pass.
- Run `python3 scripts/tracker_weekly.py count` and put the figure in the report.

## 6. Commit and push

One commit:

    git add data/tracker/search-runs-<date> data/tracker/readings data/tracker/waiting.toml data/tracker/contrast-seen.txt && git commit -m "<date>: weekly reading, N new results, M waiting rows added, F flagged" -m "<attribution lines this session was given>" && git push origin main

If the push is refused, push the same commit once to `claude/reading-<date>` and say so in the
report. If that is refused too, stop and put the reading record's contents in the report. Never
force-push, rebase or touch another branch.

## 7. The report

In plain words, for someone who has not seen the project:
- how many new results were found;
- how many papers now wait to be scored, with the total from step 5;
- each new waiting paper, with its title, the prediction it bears on, whether it was opened and the
  first reading;
- every flag;
- the commit, and the branch if it was not `main`.

## What this run never does

It never changes a score, a study, a judgement, a ruling, a theory, a claim, a prediction or a search.
It never calls Gemini or any paid service. It never edits a row already in the record.
