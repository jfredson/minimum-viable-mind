#!/bin/sh
# Re-check of 2026-10-18: the same checks as run_all.sh plus recheck.py, written into recheck-2026-10-18/ so the first check outputs stay as filed.
# Needs origin/main fetched (two files are read from it with git show). $0, no model called.
S=docs/reviews/2026-10-17-paper-fold-check-scripts; O=$S/recheck-2026-10-18; mkdir -p $O
python3 -I $S/check_figures.py            > $O/check_figures.out.txt
python3 -I $S/check_figures.py unlisted   > $O/trace_unlisted.out.txt
python3 -I $S/ledger_rows.py              > $O/ledger_rows.out.txt
python3 -I $S/unlisted_numbers.py         > $O/unlisted_numbers.out.txt
python3 -I $S/status_words.py             > $O/status_words.out.txt
python3 -I $S/status_words.py unreg       > $O/unregistered_runs.out.txt
python3 -I $S/ruled_sentences.py          > $O/ruled_sentences.out.txt
python3 -I $S/reserved_places.py          > $O/reserved_places.out.txt
python3 -I $S/quotes.py                   > $O/quotes.out.txt
python3 -I $S/voice_scan.py               > $O/voice_scan.out.txt
python3 -I $S/word_counts.py              > $O/word_counts.out.txt
sh $S/approach_note.sh                    > $O/approach_note.out.txt
git diff origin/main...HEAD -- drafts/paper-removal-test-nature-draft.md | grep -E "^-[^-]" > $O/paper_removed_lines.out.txt
tail -n 1 $O/check_figures.out.txt $O/trace_unlisted.out.txt $O/unlisted_numbers.out.txt
python3 -I $S/recheck.py > $O/recheck.out.txt
