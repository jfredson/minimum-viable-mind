# Failure 2 part one (route sentence) and failure 4 part one (both sweeps), on the proposal.
import re, sys
path = sys.argv[1]
text = open(path).read().splitlines()
route = r'route to the states|route by|carried by the token|forced by the loss|is the input token'
hits = [(i + 1, l.strip()) for i, l in enumerate(text) if re.search(route, l, re.I)]
print(f'failure 2, part one: {len(hits)} route sentence line(s)')
for i, l in hits:
    print(f'   {i}: {l}')
words = (r'verif|measur|calibrat|attack|reproduc|confirm|\brun|\bran\b|check|'
         r'shows|showed|found|observed|recorded|returns|returned|yield|result')
nums = r'[0-9]+\.[0-9]{2,}|[0-9]{1,3},[0-9]{3}'
w = [i for i, l in enumerate(text) if re.search(words, l, re.I)]
n = [i for i, l in enumerate(text) if re.search(nums, l)]
print(f'failure 4, part one: word sweep {len(w)} lines; number sweep {len(n)} lines; '
      f'either {len(set(w) | set(n))} lines of {len(text)}')
print(f'lines carrying the word MEASURED: {sum("MEASURED" in l for l in text)}; '
      f'ARGUED: {sum("ARGUED" in l for l in text)}')
