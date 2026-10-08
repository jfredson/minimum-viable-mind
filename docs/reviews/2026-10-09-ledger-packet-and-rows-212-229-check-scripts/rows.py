import re,sys
f=sys.argv[1]
rows={}
for l in open(f):
    m=re.match(r"\| (RT-\d+)([^|]*)\|",l)
    if m:
        c=[x.strip() for x in l.split("|")]
        rows.setdefault(m.group(1),[]).append(c)
for k in sys.argv[2:]:
    if k=="OPEN":
        print("open:",[r for r,v in rows.items() for c in v if c[5].startswith("**Open")])
    elif k=="ALL":
        for r,v in rows.items():
            for c in v:
                w=re.match(r"\*\*([^*]+)\*\*",c[5]); print(r,"|",c[3],"|",w.group(1) if w else c[5][:40])
    else:
        for c in rows.get(k,[]): print(k,"|",c[3],"|",c[5][:90])
