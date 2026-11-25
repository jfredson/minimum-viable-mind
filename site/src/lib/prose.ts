// Turns the record's own text into public copy, at build time (2026-11-14).
//
// The data file (data/project.toml) is written for the working sessions, so its prose cites
// repository files by path ("docs/next-steps-2026-10-24.md") and changes by pull request number
// ("pull request 166"). A stranger can do nothing with either. Rather than rewrite hundreds of
// records, which would also break the record's own cross-references, the pages pass every data
// string through `prose()`:
//
// - a repository path becomes a link to that file on GitHub, labelled with a readable name made
//   from the file name ("next steps"); the path itself stays only in the link's hover title;
// - a bare file name ("explainer.md") is found in the repository and treated the same way;
// - "pull request 166" becomes "a change on GitHub", linked to it; several become
//   "three changes on GitHub (first, second and third)", each word linked;
// - a bare number in brackets beside named pull requests ("(171)") becomes "(on GitHub)";
// - a pull request in the private Sentient Horizons repository becomes a plain phrase, unlinked.
//
// The data file is unchanged. The output is HTML, so pages render it with `set:html`; every
// piece of the original text is escaped first.
import { execSync } from 'node:child_process';
import { existsSync } from 'node:fs';
import { resolve } from 'node:path';

const REPO_URL = 'https://github.com/jfredson/minimum-viable-mind';

// The repository root: the build runs from site/, the data file sits one level up.
const ROOT = [resolve(process.cwd(), '..'), process.cwd()].find((p) => existsSync(resolve(p, 'data/project.toml'))) ?? resolve(process.cwd(), '..');

let files: Set<string> | null = null;
let byBase: Map<string, string[]> | null = null;
function index() {
  if (files && byBase) return { files, byBase };
  let list: string[] = [];
  try {
    list = execSync('git ls-files', { cwd: ROOT, encoding: 'utf8', maxBuffer: 64 * 1024 * 1024 }).split('\n').filter(Boolean);
  } catch {
    list = [];
  }
  files = new Set(list);
  byBase = new Map();
  for (const f of list) {
    const b = f.slice(f.lastIndexOf('/') + 1);
    byBase.set(b, [...(byBase.get(b) ?? []), f]);
  }
  return { files, byBase };
}

const esc = (s: string) => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');

// Names that read better written out than derived from the file name.
const KNOWN: Record<string, string> = {
  'STATUS.md': 'the status log',
  'STATUS-archive.md': 'the status log archive',
  'ROADMAP.md': 'the roadmap',
  'ROADMAP-post-removal-test.md': 'the roadmap after the removal test',
  'explainer.md': 'the explainer',
  'compute-ledger.md': 'the compute ledger',
  'spending-record.md': 'the spending record',
  'README.md': 'the read-me',
  'amendment-a3.md': 'Amendment A3',
};

// A readable label from a path: the file name without its folder, dates, extension or the
// review tool's suffix, hyphens as spaces.
export function labelFor(path: string): string {
  const clean = path.replace(/\/+$/, '');
  const base = clean.slice(clean.lastIndexOf('/') + 1);
  if (KNOWN[base]) return KNOWN[base];
  let name = base.replace(/\.[a-z0-9]+$/i, '');
  // A name that says little on its own ("results", "fixes-findings") takes its folder's name too,
  // unless the folder is one of the record's general ones.
  const parts = clean.split('/');
  const parent = parts.length > 1 ? parts[parts.length - 2] : '';
  const general = /^(docs|rulings|reviews|spec|drafts|experiments|outside-perspective|scripts|data)$/i.test(parent);
  if (parent && !general && (/^(results|findings|readme)$/i.test(name) || /^[a-z]+-findings$/i.test(name.replace(/-?\d{4}-\d{2}-\d{2}/g, "")))) {
    name = `${parent}-${name}`;
  }
  name = name
    .replace(/\d{4}-\d{2}-\d{2}/g, ' ')
    .replace(/-(claude-code|claude-worktree|claude)$/i, '')
    .replace(/^\d+-/, '')
    .replace(/[-_]+/g, ' ')
    .replace(/\bstep(\d)/gi, 'step $1')
    .replace(/\bv(\d+)\b/g, 'version $1')
    .replace(/\bmvm\b/gi, 'MVM')
    .replace(/\s+/g, ' ')
    .trim();
  return name || base;
}

function fileLink(path: string): string {
  const { files: f } = index();
  const isDir = path.endsWith('/');
  const label = esc(labelFor(path));
  const exists = isDir ? [...f].some((x) => x.startsWith(path)) : f.has(path);
  if (!exists) return label;
  const href = `${REPO_URL}/${isDir ? 'tree' : 'blob'}/main/${path.replace(/\/+$/, '')}`;
  return `<a class="src-link" href="${esc(href)}" title="${esc(path)}">${label}</a>`;
}

const NUMBER_WORD = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten'];
const ORDINAL = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth'];
const joinAnd = (xs: string[]) => (xs.length > 1 ? `${xs.slice(0, -1).join(', ')} and ${xs[xs.length - 1]}` : xs.join(''));
const prLink = (n: number, text: string) => `<a class="src-link" href="${REPO_URL}/pull/${n}">${text}</a>`;

function prNumbers(list: string): number[] {
  const out: number[] = [];
  const range = list.match(/^(\d+) to (\d+)$/);
  if (range) {
    for (let i = Number(range[1]); i <= Number(range[2]); i++) out.push(i);
    return out;
  }
  for (const m of list.matchAll(/\d+/g)) out.push(Number(m[0]));
  return out;
}

function prPhrase(match: string, sh: string | undefined, draft: string | undefined, list: string, bracketed = false): string {
  const cap = /^[A-Z]/.test(match);
  const nums = prNumbers(list);
  let out: string;
  if (sh) {
    out = 'a change to the Sentient Horizons site';
  } else if (nums.length === 1) {
    out = prLink(nums[0], `a ${draft ? 'draft ' : ''}change on GitHub`);
  } else {
    const count = NUMBER_WORD[nums.length] ?? String(nums.length);
    const links = nums.map((n, i) => prLink(n, ORDINAL[i] ?? `change ${i + 1}`));
    // Written with the numbers in brackets ("pull requests (71 and 72)"), the sentence already
    // counts them or needs no count, so none is added.
    out = `${bracketed ? '' : `${count} `}${draft ? 'draft ' : ''}changes on GitHub (${joinAnd(links)})`;
  }
  return cap ? out.replace(/^a /, 'A ').replace(/^([a-z])/, (c) => c.toUpperCase()) : out;
}

// One pattern, three kinds of match, tried left to right.
const TOKEN = new RegExp(
  [
    // 1-4: "[sentient-horizons ][draft ]pull request(s) N[, N and N | N to N]" (group 3 is the
    // separator: a space, or the mark left where the numbers were in brackets)
    String.raw`((?:sentient-horizons )?)((?:draft )?)[Pp]ull requests?( |\u0000)(\d+(?: to \d+|(?:(?:, | and |, and )\d+)*))`,
    // 5: a repository path: at least one folder, ending in a file extension or a slash
    String.raw`((?<![\w/.:-])(?:[\w.-]+\/)+(?:[\w.-]*\.(?:md|py|toml|json|jsonl|yaml|yml|csv|txt|pdf|png|ts)\b|(?=[\s,;)]|$)))`,
    // 6: a bare file name
    String.raw`((?<![\w/.:-])[\w.-]+\.(?:md|py|toml|jsonl)\b)`,
  ].join('|'),
  'g',
);

/** The record's text as public HTML: paths and pull request numbers turned into readable links. */
export function prose(text: string | undefined | null): string {
  if (!text) return '';
  // "open pull requests (71 and 72)": the numbers in brackets are the same pull requests. A mark
  // takes the brackets' place so the pattern below links them, without adding a count (2026-11-14).
  text = text.replace(/([Pp]ull requests?) \((\d+(?: to \d+|(?:(?:, | and |, and )\d+)*))\)/g, '$1\u0000$2');
  let out = '';
  let last = 0;
  for (const m of text.matchAll(TOKEN)) {
    const at = m.index ?? 0;
    out += esc(text.slice(last, at));
    if (m[4] !== undefined) {
      out += prPhrase(m[0], m[1] || undefined, m[2] || undefined, m[4], m[3] === '\u0000');
    } else if (m[5] !== undefined) {
      out += m[5].endsWith('/') || /\.[a-z0-9]+$/i.test(m[5]) ? fileLink(m[5]) : esc(m[5]);
    } else if (m[6] !== undefined) {
      const found = index().byBase.get(m[6]);
      out += found && found.length === 1 ? fileLink(found[0]) : esc(KNOWN[m[6]] ?? labelFor(m[6]));
    } else {
      out += esc(m[0]);
    }
    last = at + m[0].length;
  }
  out += esc(text.slice(last));
  // Where a sentence has named pull requests, a bare number in brackets after an item is one too
  // ("the closure checks (171)"); it becomes "(on GitHub)", linked.
  if (/pull requests?/i.test(text)) {
    out = out.replace(/\((\d{2,3})(?=[,)])/g, (_m, n: string) => `(${prLink(Number(n), 'on GitHub')}`);
  }
  // A pull request named without a number ("five pull requests landed on my word") is a change
  // to a visitor; the deploy's check refuses the words "pull request" on a public page (2026-11-14).
  out = out.replace(/\b([Pp])ull request(s?)\b/g, (_m, p: string, s: string) => `${p === 'P' ? 'C' : 'c'}hange${s}`);
  // "the About page" in the record links to the tracker's own About page, where the rules are
  // explained (2026-11-21).
  out = out.replace(/\bthe About page\b/g, '<a href="/about/#numbers">the About page</a>');
  return out;
}
