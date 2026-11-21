"""Writes the static mock pages for the 2026-11-20 tracker design proposal.

Every theory name and every number here is invented, and each page says so in a banner. No
theory has been scored. Run: python3 build.py  (writes *.html beside this file).
"""
from pathlib import Path

HERE = Path(__file__).parent

HEAD = """<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<script>(function(){{var q=new URLSearchParams(location.search);var s=q.get('skin')||'reinked';
var t=q.get('theme')||(s==='darkroom'?'dark':'light');document.documentElement.dataset.theme=t;
document.write('<link rel="stylesheet" href="shell.css"><link rel="stylesheet" href="skin-'+s+'.css"><link rel="stylesheet" href="site.css">');}})();</script>
</head><body>
<div class="mockbar"><div class="container"><b>MOCK-UP FOR A RULING</b> · every theory name and number on this page is invented · no theory has been scored · dotted underline = placeholder</div></div>
<div class="space-bg" aria-hidden="true"></div>
<header class="site-header"><div class="container nav">
<a class="brand" href="index.html">Minimum Viable Mind</a>
<button type="button" class="nav-toggle" aria-label="Menu"><svg class="ico-open" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M3 6h18M3 12h18M3 18h18"></path></svg></button>
<nav class="navlinks">
<a href="index.html"{a_th}>Theories</a><a href="questions.html"{a_q}>Questions</a><a href="positions.html"{a_p}>Our Positions</a><a href="tests.html"{a_t}>Our Tests</a><a href="#">News</a><a href="#">About</a>
<span class="nav-divider"></span><a class="nav-secondary" href="#">Family</a>
<button type="button" class="theme-toggle" aria-label="Toggle theme"><svg class="icon-sun" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="4"></circle><path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M4.93 19.07l1.41-1.41M17.66 6.34l1.41-1.41"></path></svg><svg class="icon-moon" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg></button>
</nav></div></header>
<main class="container">
"""

FOOT = """</main>
<footer class="site-footer"><div class="container footer-grid"><div>
<div class="footer-brand">Minimum Viable Mind</div>
<p class="footer-tag">Every theory of consciousness, held to the same rules, this site's own included.</p>
<p class="footer-links"><a href="#">About</a><a href="#">This week's reading</a><a href="#">Disagree with something</a><a href="#">Source</a><a href="#">Follow on X</a></p>
<p class="footer-meta">Built <span class="ph">20 November 2026</span> from version <span class="ph">abc1234</span>. Data under CC BY 4.0.</p>
<p class="footer-parent">A <a href="#">Sentient Horizons</a> project.</p>
</div></div></footer>
</body></html>
"""


def page(name, title, body, active=""):
    flags = {k: "" for k in ("a_th", "a_q", "a_p", "a_t")}
    if active:
        flags[active] = ' class="active"'
    html = HEAD.format(title=title, **flags) + body + FOOT
    (HERE / name).write_text(html)


def bar(kind, v, label):
    if v is None:
        return f'<div class="bar {kind} empty" data-l="{label}"><div class="t"></div><span class="v none">none</span></div>'
    if kind == "sup":
        lo, hi = (50, v) if v >= 50 else (v, 50)
        style = f"left:{lo}%;width:{hi - lo}%"
    else:
        style = f"width:{v}%"
    return f'<div class="bar {kind}" data-l="{label}"><div class="t"><div class="f" style="{style}"></div></div><span class="v ph">{v}</span></div>'


# (rank, name, href, sub, support, testability, left, extra classes, own)
RANKED = [
    ("=1", "Relay theory", "theory.html", "rests on 14 studies from 6 groups", 68, 80, 62, "tied", False),
    ("=1", "Lantern theory", "#", "rests on 9 studies from 4 groups", 64, 75, 70, "tied last", False),
    ("3", "Echo theory", "#", "rests on 6 studies from 3 groups", 55, 66, 81, "", False),
    ("4", "Tide theory", "#", "rests on 11 studies from 5 groups", 38, 71, 58, "", False),
]
UNRANKED = [
    ("", "The Sentient Horizons account", "#", "studies from 1 group so far", None, 86, 97, "", True),
    ("", "Mirror theory", "#", "no studies from a second group yet", None, 62, 92, "", False),
]
UNDEFINED = [
    ("", "Loom theory", "#", "needs: a prediction that could fail for 2 more of its 5 core claims", None, 40, None, "", False),
    ("", "Threshold theory", "#", "needs: a prediction that could fail for 1 more of its 4 core claims", None, 38, None, "", False),
]


def rows(items):
    out = []
    for n, name, href, sub, s, t, l, cls, own in items:
        own_tag = '<span class="own">this site\'s own</span>' if own else ""
        extra = ""
        if s is not None and s < 50:
            extra = '<span class="leans"> · the evidence so far leans against it</span>'
        out.append(
            f'<div class="row {cls}"><span class="n">{n}</span>'
            f'<span class="name"><a href="{href}">{name}</a>{own_tag}<span class="sub">{sub}{extra}</span></span>'
            f'{bar("sup", s, "backed")}{bar("test", t, "sharp")}{bar("left", l, "left to test")}</div>'
        )
    return "\n".join(out)


def ranking(mini=False):
    head = (
        '<div class="rank-head"><span></span><span>Theory <span class="phtag">invented</span></span>'
        '<span>How well the evidence backs it<br>(50 = even)</span><span>How sharply it is defined, so it can be tested</span>'
        '<span>How much is left to test</span></div>'
    )
    if mini:
        head = ('<div class="rank-head"><span></span><span>Theory <span class="phtag">invented</span></span>'
                '<span>backed</span><span>sharp</span><span>left</span></div>')
    tie = '<div class="tienote">Shown as tied: one study going the other way would swap these two.</div>'
    r = rows(RANKED)
    r = r.replace('\n<div class="row ">', '\n' + tie + '\n<div class="row ">', 1)
    return f"""<div class="rank{' mini' if mini else ''}">
{head}
<div class="group">Ranked <i>past the bar, with a support score; highest support first</i></div>
{r}
<div class="group">Testable, too little tested to rank <i>no studies yet from two separate groups</i></div>
{rows(UNRANKED)}
<div class="group">Not yet defined sharply enough to rank <i>half or fewer of its core claims can be tested</i></div>
{rows(UNDEFINED)}
</div>"""


NEWS = """<div class="news"><div class="lab"><span>Latest news</span><a href="#">All news</a></div><ol>
<li><span class="d">18 November 2026 · a prediction settled</span><a href="#"><span class="ph">A placeholder post title, written as the finding it reports</span></a></li>
<li><span class="d">11 November 2026 · a theory added</span><a href="#"><span class="ph">A second placeholder post, one line long</span></a></li>
<li><span class="d">4 November 2026 · the method changed</span><a href="#"><span class="ph">A third placeholder post</span></a></li>
</ol><p class="start">New here? <a href="#">Start with the opening post</a>.</p></div>"""

HEADCARD = """<div class="headcard"><div class="lab"><span>Tested so far</span><span class="phtag">placeholder · not ruled</span></div>
<div class="big ph">18<small>%</small></div>
<p>of the sharp predictions these theories make have been put to a test at all.</p>
<div class="count ph">41 of 228 predictions · 8 theories</div></div>"""

ABOVE = ('<p class="above"><b>What is the least a mind needs?</b> Every theory of consciousness gives an answer. '
         'Here is how each is holding up.</p>')

NEWCOMER = """<p class="newcomer">Each theory is scored three ways, by rules written down before any theory was scored:
how well published studies back it, how sharply it is stated so that a study could prove it wrong, and how much of
it no study has touched yet. One of the theories is this site's own, the account argued on
<a href="#">Sentient Horizons</a>; it is scored by the same rules, and an outside reader makes the first judgement
on every one of its rows.</p>
<p class="strip">Last checked <span class="ph">16 November 2026</span>: <span class="ph">31</span> open predictions read against new papers, none moved. <a href="#">See the week's reading</a>.</p>
<div class="ctas"><a class="btn" href="#">Why so little is settled</a><a class="btn ghost" href="#">Who is asking</a></div>"""

RANK_FOOT = """<p class="rank-foot"><b>Read it this way.</b> The order is set by the first bar only. The second bar gets a
theory into the ranking; the third says where the work is, and a long one is not a fault. The three are never added up.
<a href="#">How the numbers are worked out</a>.</p>"""


def home():
    body = f"""<section class="home-top"><div>
{ABOVE}
<h1 class="question">How far has the science of consciousness got in testing its theories?</h1>
<div class="m-only">{HEADCARD}</div>
{ranking()}
{RANK_FOOT}
</div><aside><div class="d-only">{HEADCARD}</div><div class="aside-new">{NEWCOMER}</div>{NEWS}</aside></section>"""
    page("index.html", "Minimum Viable Mind", body, "a_th")


def home_number_first():
    body = f"""<section class="home-top"><div>
<p class="eyebrow">Every theory of consciousness, held to the evidence</p>
<div class="bignum ph">18%</div>
<p class="bignum-cap">of the sharp predictions made by theories of consciousness have been put to a test at all. <span class="phtag">placeholder · not ruled</span></p>
<h1 class="question">How far has the science of consciousness got in testing its theories?</h1>
{NEWCOMER}
</div><aside>
<div class="headcard" style="border-left-width:1px"><div class="lab"><span>The theories, three ways</span><a href="#" style="text-transform:none;letter-spacing:0">All</a></div>
{ranking(mini=True)}</div>
{NEWS}</aside></section>"""
    page("index-number-first.html", "Minimum Viable Mind", body, "a_th")


def hist():
    pts = [(0, 50), (1, 58), (2, 61), (3, 72), (4, 66), (5, 68)]
    w, h, pad = 300, 100, 18
    xs = lambda i: pad + i * (w - 2 * pad) / 5
    ys = lambda v: h - pad - (v - 30) * (h - 2 * pad) / 50
    path = " ".join(f"{'M' if i == 0 else 'L'}{xs(i):.0f},{ys(v):.0f}" for i, v in pts)
    dots = "".join(f'<circle class="pt" cx="{xs(i):.0f}" cy="{ys(v):.0f}" r="2.5"/>' for i, v in pts)
    return f"""<svg class="hist" viewBox="0 0 {w} {h + 8}" role="img" aria-label="Support score, run by run (invented)">
<line class="ax" x1="{pad}" y1="{h - pad}" x2="{w - pad}" y2="{h - pad}"/>
<line class="mid" x1="{pad}" y1="{ys(50):.0f}" x2="{w - pad}" y2="{ys(50):.0f}"/><text x="{w - pad + 2}" y="{ys(50) + 3:.0f}">50</text>
<path class="ln" d="{path}"/>{dots}
<text x="{pad}" y="{h + 4}">Jan 2026</text><text x="{w - pad - 40}" y="{h + 4}">Nov 2026</text></svg>"""


def theory():
    body = f"""<section class="page two"><div>
<p class="crumbs"><a href="index.html">Theories</a> / Relay theory <span class="phtag">invented theory</span></p>
<p class="eyebrow">A theory of consciousness · ranked =1 of 4</p>
<h1>Relay theory</h1>
<p class="plain"><span class="ph">One plain paragraph on what the theory says makes a system conscious, written for a reader who has never
heard of it, with its proponents named and linked at first mention.</span></p>
<div class="scores">
<div class="score"><div class="lab">Backed by the evidence</div><div class="num ph">68 <small>/ 100</small></div>
<p>Leans supported. <span class="ph">14 studies from 6 groups</span>, total weight <span class="ph">31</span>. 50 would mean even.</p>{bar("sup", 68, "")}</div>
<div class="score"><div class="lab">Sharp enough to test</div><div class="num ph">80 <small>/ 100</small></div>
<p><span class="ph">4 of 5</span> core claims come with a prediction that could fail. Past the bar.</p>{bar("test", 80, "")}</div>
<div class="score"><div class="lab">Left to test</div><div class="num ph">62 <small>/ 100</small></div>
<p><span class="ph">10 of 16</span> distinguishing predictions untouched by any study.</p>{bar("left", 62, "")}</div>
</div>
<p class="readers">Shown as tied with Lantern theory: one study going the other way would swap them. <a href="#">Check it by hand</a>.</p>

<div class="section"><div class="shead"><h2>Its Core Claims</h2><span>quoted from <span class="ph">one named publication by its proponents</span>, fixed until the yearly review</span></div>
<ol class="claims">
<li><span class="dot full"></span><span><span class="q ph">"First core claim, quoted word for word."</span><span class="m">proponents state 3 predictions that could fail</span></span><a href="#">3 predictions</a></li>
<li><span class="dot full"></span><span><span class="q ph">"Second core claim, quoted."</span><span class="m">proponents state 2</span></span><a href="#">2 predictions</a></li>
<li><span class="dot full"></span><span><span class="q ph">"Third core claim, quoted."</span><span class="m">proponents state 1</span></span><a href="#">1 prediction</a></li>
<li><span class="dot half"></span><span><span class="q ph">"Fourth core claim, quoted."</span><span class="m">only the site has inferred one, counted at half until a proponent states it</span></span><a href="#">1 prediction</a></li>
<li><span class="dot"></span><span><span class="q ph">"Fifth core claim, quoted."</span><span class="m">no prediction that could fail, from anyone</span></span><span class="dim">none</span></li>
</ol>
<div class="key"><span><i class="dot full"></i>stated by its proponents</span><span><i class="dot half"></i>inferred by the site</span><span><i class="dot"></i>none yet</span></div></div>

<div class="section"><div class="shead"><h2>Its Predictions</h2><span>those that separate it from a rival; the ones every theory shares are listed at the end and score nothing</span></div>
<table class="preds"><thead><tr><th>Prediction</th><th class="hide-s">Who says so</th><th>State</th><th class="hide-s">Studies</th></tr></thead><tbody>
<tr><td><a href="prediction.html">An invented prediction, stated so two readers would agree whether it came true</a><span class="m">core claim 1 · counts double</span></td><td class="hide-s">proponents</td><td><span class="badge ok">supported</span></td><td class="hide-s">3</td></tr>
<tr><td><a href="#">A second invented prediction</a><span class="m">core claim 1 · counts double</span></td><td class="hide-s">proponents</td><td><span class="badge mixed">mixed</span></td><td class="hide-s">2</td></tr>
<tr><td><a href="#">A third invented prediction</a><span class="m">core claim 2 · counts double</span></td><td class="hide-s">proponents</td><td><span class="badge no">contradicted</span></td><td class="hide-s">1</td></tr>
<tr><td><a href="#">A fourth invented prediction</a><span class="m">core claim 4 · half weight</span></td><td class="hide-s">inferred by the site</td><td><span class="badge untested">untested</span></td><td class="hide-s">0</td></tr>
<tr><td><a href="#">A later reading that softens the third prediction's loss</a><span class="m">a rescue: recorded as a new prediction; the loss above stands</span></td><td class="hide-s">proponents</td><td><span class="badge untested">untested</span></td><td class="hide-s">0</td></tr>
</tbody></table>
<p class="dim" style="font-family:var(--sans);font-size:13px">Also listed, moving no score: <a href="#">5 studies explained afterwards, not counted</a> (the prediction was not on record before the study appeared).</p></div>
</div>
<aside class="side">
<div class="box move"><h3>What would move this</h3><ul>
<li>A study by an outside group on <a href="#">the fourth prediction</a>, registered in advance: <b>68 → 72</b> if it came out for, <b>68 → 61</b> against.</li>
<li>A second group repeating <a href="#">the contradicting study</a>: its weight rises from <b>2 → 3</b>.</li>
<li>A proponent stating a prediction for core claim 5: sharpness <b>80 → 100</b>.</li></ul></div>
<div class="box"><h3>Backed by the evidence, run by run</h3>{hist()}<p class="dim" style="font-size:12px">Every change has a dated entry in <a href="#">the story so far</a>.</p></div>
<div class="box"><h3>Last readings</h3><p><span class="ph">16 Nov</span> · quiet · 4 searches<br><span class="ph">9 Nov</span> · noted · one preprint, waiting on the second reader<br><span class="ph">2 Nov</span> · quiet</p></div>
<p class="disagree"><a href="#">Disagree with something on this page</a></p>
</aside></section>"""
    page("theory.html", "Relay theory · Minimum Viable Mind", body, "a_th")


def prediction():
    body = """<section class="page two"><div>
<p class="crumbs"><a href="index.html">Theories</a> / <a href="theory.html">Relay theory</a> / a prediction <span class="phtag">invented</span></p>
<p class="eyebrow">A prediction · core claim 1 of Relay theory</p>
<h1 class="ph">An invented prediction, stated so two readers would agree whether it came true</h1>
<p class="plain"><span class="ph">One paragraph in plain words: what the theory expects to see, and why it follows from the claim.</span></p>
<div class="testbox"><div><h4>Counts for it</h4><p class="ph">The result that would count in its favour, written before any study was read.</p></div>
<div><h4>Counts against it</h4><p class="ph">The result that would count against it.</p></div></div>
<dl class="facts">
<dt>Whose it is</dt><dd>Stated by its proponents, in <a href="#" class="ph">a dated publication</a> (first stated <span class="ph">March 2019</span>). Full weight.</dd>
<dt>Does it separate theories</dt><dd>Yes. <a href="#">Lantern theory</a> predicts the opposite; <a href="#">Echo theory</a> says nothing about it.</dd>
<dt>Who settles it</dt><dd>A published study with a measured result. A press release or a talk settles nothing.</dd>
<dt>State</dt><dd><span class="badge ok">supported</span> since <span class="ph">4 June 2026</span></dd>
</dl>
<div class="section"><div class="shead"><h2>The Studies</h2><span>each one's weight counts its protections against bias, 1 to 5</span></div>
<table class="preds"><thead><tr><th>Study</th><th>Outcome</th><th class="hide-s">Protections</th><th>Weight</th></tr></thead><tbody>
<tr><td><a href="#" class="ph">An invented study, 2025</a><span class="m">first appeared <span class="ph">May 2024</span>, after the prediction · both readers: for</span></td><td><span class="badge ok">for</span></td><td class="hide-s prot"><span class="y">registered</span> · <span class="y">outside group</span> · rival agreed · replicated</td><td class="ph">3</td></tr>
<tr><td><a href="#" class="ph">A second invented study, 2023</a><span class="m">both readers: for</span></td><td><span class="badge ok">for</span></td><td class="hide-s prot">registered · <span class="y">outside group</span> · rival agreed · replicated</td><td class="ph">2</td></tr>
<tr><td><a href="#" class="ph">A third invented study, 2021</a><span class="m">readers disagreed · the score waits until it is settled</span></td><td><span class="badge mixed">waiting</span></td><td class="hide-s prot">registered · outside group · rival agreed · replicated</td><td class="ph">1</td></tr>
<tr><td><a href="#" class="ph">A study from 2018</a><span class="m">appeared before the prediction was on record</span></td><td><span class="badge off">explained afterwards, not counted</span></td><td class="hide-s prot">·</td><td>0</td></tr>
</tbody></table></div>
<div class="section"><div class="shead"><h2>Its Record</h2><span>every change, dated, with the reason</span></div>
<ul class="record"><li><span class="d ph">4 Jun 2026</span><span>Untested to supported: <a href="#">the 2025 study</a>, weight 3, read for by both readers.</span></li>
<li><span class="d ph">20 Nov 2025</span><span>Added, from the proponents' publication, with the test above.</span></li></ul></div>
</div>
<aside class="side">
<div class="box"><h3>Two readers</h3><p>Every outcome is read twice: once by a first reader, and once, without seeing that answer, by a second reader from a different lab's model. Where they disagree, the score does not move until it is settled.</p></div>
<div class="box"><h3>Also bears on</h3><ul><li><a href="questions.html">Which features does experience need?</a></li><li><a href="#">Lantern theory</a>, against</li></ul></div>
<div class="box"><h3>Last readings</h3><p><span class="ph">16 Nov</span> · quiet · 2 searches<br><span class="ph">9 Nov</span> · quiet · 2 searches</p></div>
<p class="disagree"><a href="#">Disagree with this prediction</a></p>
</aside></section>"""
    page("prediction.html", "A prediction · Minimum Viable Mind", body, "a_th")


QUESTIONS = [
    ("Which features does experience need?", "Each theory names what a system must have for there to be something it is like to be it. Here are the answers side by side, and the tests that would choose between them.",
     [("Relay theory", "a placeholder answer"), ("Lantern theory", "a placeholder answer"), ("The Sentient Horizons account", "a placeholder answer")], (3, 2, 9)),
    ("Could a machine have it?", "What each theory says a machine would have to be built like, and what would show it.",
     [("Relay theory", "yes, if built a placeholder way"), ("Tide theory", "a placeholder answer"), ("Loom theory", "does not say")], (0, 1, 7)),
    ("Which animals have it?", "Where each theory draws the line, and which studies of animals bear on it.",
     [("Echo theory", "a placeholder answer"), ("Mirror theory", "a placeholder answer")], (1, 0, 5)),
    ("Can it fade to nothing?", "Whether experience can thin out gradually, or is either there or not.", [("Lantern theory", "a placeholder answer"), ("Echo theory", "a placeholder answer")], (0, 0, 4)),
    ("Can a group share one present?", "Whether two or more systems could take part in a single experience.", [("The Sentient Horizons account", "a placeholder answer")], (0, 0, 2)),
]


def questions():
    items = []
    for q, d, ans, (sup, mix, unt) in QUESTIONS:
        tot = sup + mix + unt
        a = "".join(f'<div><span>{n}</span><span class="ph">{v}</span></div>' for n, v in ans)
        items.append(f"""<li class="qitem"><div><h3>{q}</h3><p>{d}</p>
<p class="tally"><span class="ph">{tot}</span> predictions bear on it: <span class="ph">{sup + mix}</span> tested, <span class="ph">{unt}</span> not yet. <a href="#">See them</a>.</p>
<div class="stack"><i class="t1" style="width:{sup / tot * 100:.0f}%"></i><i class="t2" style="width:{mix / tot * 100:.0f}%"></i><i class="t3" style="width:{unt / tot * 100:.0f}%"></i></div></div>
<div class="answers">{a}</div></li>""")
    body = f"""<section class="page"><p class="eyebrow">Beside the ranking · moves no score</p>
<h1>The Open Questions</h1>
<p class="plain">The questions people most want answered about minds. None of them is scored. Each one links to the predictions that bear on it, so you can see which tests would move it, and how many have been run.</p>
<div class="key"><span><i class="stack" style="width:22px;margin:0"><i class="t1" style="width:100%"></i></i>tested, one way</span><span><i class="stack" style="width:22px;margin:0"><i class="t2" style="width:100%"></i></i>tested, mixed</span><span><i class="stack" style="width:22px;margin:0"><i class="t3" style="width:100%"></i></i>not yet tested</span></div>
<ul class="qlist">{''.join(items)}</ul></section>"""
    page("questions.html", "The open questions · Minimum Viable Mind", body, "a_q")


POSITIONS = [
    ("A first working position, in its published words", "What it would take to change it, quoted from the position's own section.", "ok", "evidence has gone its way", "1 study · weight 2"),
    ("A second working position", "What would change its mind.", "untested", "no evidence either way yet", "0 studies"),
    ("A third working position", "What would change its mind.", "no", "evidence has gone against it", "1 study · weight 3 · recorded, not explained away"),
    ("A fourth working position", "What would change its mind.", "mixed", "mixed", "2 studies"),
]


def positions():
    rows = "".join(f"""<div class="pos"><div><h3 class="ph">{t}</h3>
<div class="would"><b>What would change my mind</b><span class="ph">{w}</span></div></div>
<div class="verdict"><span class="badge {b}">{v}</span><span class="m ph">{m}</span></div></div>""" for t, w, b, v, m in POSITIONS)
    body = f"""<section class="page"><div class="two"><div>
<p class="eyebrow">Beside the ranking · the site's own account, against the evidence</p>
<h1>Our Working Positions, Against the Evidence</h1>
<p class="plain">The account argued on <a href="#">Sentient Horizons</a> is scored on the ranking as one theory among the others, by the same rules. This page shows the same evidence the other way round: each public working position, what it said would change its mind, and whether new evidence has gone its way, against it, or neither.</p>
<div class="notice"><b>This site ranks its author's own account.</b> So the rules were written before any theory was scored, an outside reader makes the first judgement on every row of this account, and a result against it stands once recorded.</div>
{rows}
</div><aside class="side"><div class="box"><h3>On the ranking</h3><p>The Sentient Horizons account is in the second group: testable, too little tested to rank.</p><p><a href="#">Its theory page</a></p></div>
<div class="box"><h3>Tally</h3><p class="ph">1 for · 1 against · 1 mixed · 1 untested</p></div></aside></div></section>"""
    page("positions.html", "Our working positions · Minimum Viable Mind", body, "a_p")


def tests():
    body = """<section class="page"><div class="two"><div>
<p class="eyebrow">Beside the ranking · where we run tests ourselves</p>
<h1>Our Own Tests</h1>
<p class="plain">This project also runs small tests of its own: it builds a system, removes one part at a time, and records what is lost. A result here counts toward a score only by the same rules as anyone's study, at the weight its method earns, and never because we ran it.</p>
<div class="rules3"><div><b>Registered first</b>What would count as a result is written down and dated before a test runs.</div>
<div><b>Measured or argued</b>Every result says which it is. Only a measured one can move a score.</div>
<div><b>Spending capped</b>Every test has a ceiling on what it may cost, set before it runs.</div></div>
<div class="section"><div class="shead"><h2>The Tests</h2><span>newest first</span></div>
<table class="tests"><thead><tr><th>Test</th><th>Bears on</th><th>Result</th></tr></thead><tbody>
<tr><td><a href="#" class="ph">A placeholder removal test</a><span class="m">registered <span class="ph">24 Oct 2026</span> · spent <span class="ph">$4 of $10</span></span></td><td><a href="#">a prediction of the Sentient Horizons account</a></td><td><span class="badge untested">running</span></td></tr>
<tr><td><a href="#" class="ph">A second placeholder test</a><span class="m">registered <span class="ph">10 Oct 2026</span> · spent <span class="ph">$12 of $20</span></span></td><td><a href="#">a prediction of Relay theory</a></td><td><span class="badge mixed">no result: the test could not tell</span><span class="m">measured</span></td></tr>
<tr><td><a href="#" class="ph">A third placeholder test</a><span class="m">registered <span class="ph">19 Sep 2026</span></span></td><td>none yet</td><td><span class="badge">stopped, as registered</span><span class="m">argued</span></td></tr>
</tbody></table></div>
</div><aside class="side"><div class="box"><h3>Where the project stands</h3><p class="ph">3 of 8 stages done · paused from 4 January 2027</p><p><a href="#">The project's full log</a></p></div>
<div class="box"><h3>Spent</h3><p class="ph">$46.75 of a $100 cap</p></div></aside></div></section>"""
    page("tests.html", "Our own tests · Minimum Viable Mind", body, "a_t")


if __name__ == "__main__":
    home(); home_number_first(); theory(); prediction(); questions(); positions(); tests()
    print("written")
