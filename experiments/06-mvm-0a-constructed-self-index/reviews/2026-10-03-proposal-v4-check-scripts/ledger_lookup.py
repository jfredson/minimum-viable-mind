"""Check of proposal version 4: is each dollar figure of its section 12 in the
ledger line (or the note) it names?

Run from the root of the checkout:
    .venv/bin/python experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-03-proposal-v4-check-scripts/ledger_lookup.py

Reads two committed files. Spends nothing.
"""
import re

LEDGER = 'experiments/06-mvm-0a-constructed-self-index/compute-ledger.md'
NOTE = 'experiments/rehearsal-successor-measure/out/rented-slice-2026-09-25-attempt-2/second-release-arithmetic.txt'
lines = open(LEDGER).read().split('\n')
line = lambda n: lines[n - 1]
bad = 0


def look(what, text, where, *needles):
    global bad
    for nd in needles:
        ok = nd in text
        bad += not ok
        print(f"{'FOUND  ' if ok else 'MISSING'} | {nd:<12} | {what} | {where}")


rows = [i + 1 for i, l in enumerate(lines) if re.match(r'\| 20\d\d-\d\d-\d\d', l)]
print('ledger lines that are dated table rows:', len(rows), '| the last five:', [(n, line(n)[2:12]) for n in rows[-5:]])
last_run_row = max(n for n in rows if n < 120)
print('the last row of the run table is line', last_run_row, 'dated', line(last_run_row)[2:12])
print()
look('spent across the programme', line(95), 'line 95', '228.15')
look('Amendment A3 against its $100 stop', line(95), 'line 95', '46.75')
look('rehearsal line left, of $10', line(95), 'line 95', '9.43')
look('second attempt cost', line(95), 'line 95', '0.0525')
look('vendor balance on 2026-09-26T01:54Z', line(95), 'line 95', '75.8645')
look('first attempt cost', line(94), 'line 94', '0.4974')
look('the 2026-09-21 slice row', line(93), 'line 93', '0.02')
look('2026-08-08 anomaly, billed and existed hours', line(93), 'line 93', '8.47', '2.42')
look('the same, in the note', line(423), 'line 423', '8.47', '2.42')
look('two-run pod-hours and rate', line(88), 'line 88', '20.28', '0.99')
look('10-million run trued up', line(393) + line(400), 'lines 393 and 400', '1.943')
head = '\n'.join(lines[:40])
look('ceiling raised to $450 on 2026-09-25', head, 'the top of the file', '450', '2026-09-25')
print()
note = open(NOTE).read()
look("the note's arithmetic", note, 'second-release-arithmetic.txt',
     '$10.48', '$10.84', '$10.04', '$84.06', '$129.90', '$161.90', '1.044', '1.080', '13.08', '13.52', '12.53', '1,792', '10,624')
print('\nnothing missing' if not bad else f'\n{bad} missing')
