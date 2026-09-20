// Typed view of site/src/data/project.json, written by scripts/export_site.py
// from data/project.toml. Every page reads from here and nowhere else.
import raw from '../data/project.json';

export type GoalStatus = 'delivered' | 'in-progress' | 'not-started';
export type StageStatus = 'delivered' | 'in-progress' | 'folded' | 'waiting' | 'descoped' | 'conditional' | 'not-started';
export type QuestionStatus = 'open' | 'answered' | 'answered-in-part' | 'parked' | 'waiting';
export type IdeaStatus = 'on-the-table' | 'authorised' | 'deferred' | 'rejected' | 'done';
export type FindingKind = 'registered' | 'diagnostic' | 'ruled' | 'process';
export type StepStatus = 'authorised' | 'in-progress' | 'pending' | 'done' | 'blocked';
export type TimelineKind = 'result' | 'null' | 'ruling' | 'process' | 'spend' | 'build';

export interface Project {
  name: string; short: string; updated_on: string; question: string; one_line: string;
  where_we_are: string; where_we_are_going: string; hibernation_by: string; wrap_up_start: string;
  pipeline_resumes: string; book_text_lock?: string; repo: string; sources: string[];
}
export interface Wager { title: string; claim: string; status_note: string; why_no_verdict: string; source: string }
export interface Goal { id: string; title: string; status: GoalStatus; summary: string; evidence: string }
export interface Stage {
  id: string; name: string; status: StageStatus; progress: number; one_line: string;
  delivered: string[]; remaining: string[]; adjudicates: string;
}
export interface Question {
  id: string; title: string; status: QuestionStatus; current_answer: string; answered_by: string; loses_if: string;
}
export interface Idea { id: string; title: string; status: IdeaStatus; cost: string; teaches: string; gate: string; stage: string }
export interface Finding {
  id: string; date: string; title: string; what: string; so_what: string; source: string; stage: string; kind: FindingKind;
}
export interface NextStep {
  id: string; title: string; when: string; owner: string; cost: string; decision: boolean; teaches: string; status: StepStatus;
}
export interface SpendLine { name: string; cap: number; spent: number; note: string; fraction: number; remaining: number }
export interface Spend {
  as_of: string; account_balance: number; account_note: string; idle_billing_lost?: number; idle_billing_note?: string; lines: SpendLine[];
}
export interface TimelineRow { date: string; kind: TimelineKind; title: string; summary: string }
export interface Derived {
  exported_on: string; commit: string | null; days_to_hibernation: number; days_to_wrap_up: number;
  stage_progress_mean: number;
  counts: {
    stages: Record<string, number>; questions: Record<string, number>; ideas: Record<string, number>;
    findings: number; findings_by_kind: Record<string, number>; timeline: number; decisions_pending: number;
  };
  decisions_pending: string[];
}
export interface Data {
  project: Project; wager: Wager; goals: Goal[]; stages: Stage[]; questions: Question[]; ideas: Idea[];
  findings: Finding[]; next_steps: NextStep[]; spend: Spend; timeline: TimelineRow[]; derived: Derived;
}

export const data = raw as unknown as Data;
export const project = data.project;
export const derived = data.derived;

// Human labels for every status code, so the site never shows a raw code.
export const LABEL: Record<string, string> = {
  'delivered': 'Delivered', 'in-progress': 'In progress', 'not-started': 'Not started',
  'folded': 'Folded into MVM-0', 'waiting': 'Waiting', 'descoped': 'Descoped', 'conditional': 'Conditional',
  'open': 'Open', 'answered': 'Answered', 'answered-in-part': 'Answered in part', 'parked': 'Parked',
  'on-the-table': 'On the table', 'authorised': 'Authorised', 'deferred': 'Deferred', 'rejected': 'Rejected', 'done': 'Done',
  'registered': 'Registered result', 'diagnostic': 'Diagnostic', 'ruled': 'Ruled for the record', 'process': 'Process',
  'pending': 'Pending', 'blocked': 'Blocked',
  'result': 'Result', 'null': 'Null', 'ruling': 'Ruling', 'spend': 'Spend', 'build': 'Build',
};
export const label = (s: string) => LABEL[s] ?? s;

// Tone classes: a small fixed set, each also carrying its text label, so state
// is never color alone.
export const TONE: Record<string, string> = {
  'delivered': 'ok', 'answered': 'ok', 'done': 'ok', 'result': 'ok',
  'in-progress': 'live', 'authorised': 'live', 'on-the-table': 'live', 'open': 'live', 'answered-in-part': 'live', 'ruling': 'live', 'ruled': 'live',
  'waiting': 'dim', 'parked': 'dim', 'deferred': 'dim', 'pending': 'dim', 'folded': 'dim', 'descoped': 'dim', 'conditional': 'dim', 'not-started': 'dim', 'process': 'dim', 'build': 'dim', 'diagnostic': 'dim',
  'rejected': 'no', 'blocked': 'no', 'null': 'no', 'spend': 'no',
  'registered': 'ok',
};
export const tone = (s: string) => TONE[s] ?? 'dim';

export const stageById = (id: string) => data.stages.find((s) => s.id === id);

export function fmtDate(iso: string): string {
  const [y, m, d] = iso.split('-').map(Number);
  const dt = new Date(Date.UTC(y, m - 1, d));
  return dt.toLocaleDateString('en-US', { year: 'numeric', month: 'short', day: 'numeric', timeZone: 'UTC' });
}
export const usd = (n: number) => `$${n.toFixed(n % 1 === 0 ? 0 : 2)}`;
