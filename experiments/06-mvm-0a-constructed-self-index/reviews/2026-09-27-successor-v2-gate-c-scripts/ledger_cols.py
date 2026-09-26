# Print the date, cost columns and running total of every compute-ledger table row,
# trimmed, so the rows the proposal cites can be read against its figures.
import re, sys
path = sys.argv[1]
want = sys.argv[2:] or None
for n, line in enumerate(open(path), 1):
    if not line.startswith('| 20'):
        continue
    cells = [c.strip() for c in line.strip().strip('|').split('|')]
    date = cells[0]
    if want and not any(date.startswith(w) for w in want):
        continue
    tail = cells[-4:]
    short = lambda s: (s[:170] + ' …') if len(s) > 170 else s
    print(f'line {n}: {date} | {cells[1][:60]}')
    for label, c in zip(('rate/venue', 'hours', 'estimate', 'actual', 'after this run')[-len(tail):], tail):
        print(f'     {label}: {short(c)}')
