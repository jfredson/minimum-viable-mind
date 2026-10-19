#!/bin/sh
# Re-run every check of this record from the worktree root; each writes its .out.txt beside it.
# Needs origin/main fetched (two files are read from it with git show). $0, no model called.
S=docs/reviews/2026-10-17-paper-fold-check-scripts
python3 -I $S/check_figures.py            > $S/check_figures.out.txt
python3 -I $S/check_figures.py unlisted   > $S/trace_unlisted.out.txt
python3 -I $S/ledger_rows.py              > $S/ledger_rows.out.txt
python3 -I $S/unlisted_numbers.py         > $S/unlisted_numbers.out.txt
python3 -I $S/status_words.py             > $S/status_words.out.txt
python3 -I $S/status_words.py unreg       > $S/unregistered_runs.out.txt
python3 -I $S/ruled_sentences.py          > $S/ruled_sentences.out.txt
python3 -I $S/reserved_places.py          > $S/reserved_places.out.txt
python3 -I $S/quotes.py                   > $S/quotes.out.txt
python3 -I $S/voice_scan.py               > $S/voice_scan.out.txt
python3 -I $S/word_counts.py              > $S/word_counts.out.txt
sh $S/approach_note.sh                    > $S/approach_note.out.txt
git diff origin/main...HEAD -- drafts/paper-removal-test-nature-draft.md | grep -E "^-[^-]" > $S/paper_removed_lines.out.txt
tail -n 1 $S/check_figures.out.txt $S/trace_unlisted.out.txt $S/unlisted_numbers.out.txt
