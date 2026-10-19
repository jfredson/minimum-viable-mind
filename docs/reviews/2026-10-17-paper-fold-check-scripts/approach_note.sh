#!/bin/sh
# Check 6. Does the approach note name a reader, and does anything say it was sent?
# Every name and organisation on the shortlist (docs/outside-reader-shortlist-2026-09-19.md, "Candidates"),
# grepped in the note, case-insensitive. Then words that would mean it went out, and a salutation line.
N=docs/outside-reader-approach-note-2026-10-17.md
for name in Shai Riechers Simplex Shiller Butlin Nanda DeepMind Berg Reciprocal Long Sebo Chis-Ciure Sussex Seth Ren "Center for AI Safety" Eleos Anthropic; do
  c=$(grep -c -i -w -- "$name" "$N"); echo "$name: $c"; [ "$c" -gt 0 ] && grep -n -i -w -- "$name" "$N" | cut -c1-200
done
echo "--- sending words"; grep -n -i -E "\b(sent|send|emailed|posted|replied|delivered)\b" "$N" | cut -c1-200
echo "--- salutation lines"; grep -n -E "^(Dear|Hi|Hello) " "$N" || echo "none"
