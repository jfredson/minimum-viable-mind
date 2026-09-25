// Typed view of site/src/data/roadmap.json, written by scripts/export_site.py
// from data/roadmap.toml. The /roadmap/ page reads from here and nowhere else.
// Status labels and tones live with the rest in ./project.ts (label, tone).
import raw from '../data/roadmap.json';

export type WeekendStatus = 'planned' | 'active' | 'done' | 'partial' | 'blackout' | 'slack';
export type RoadmapGoalStatus = 'planned' | 'done' | 'carried' | 'dropped' | 'not_needed';
export type GoalOwner = 'john' | 'agents' | 'both';
export type MilestoneKind = 'kill_date' | 'wrap_up' | 'hibernation';
export type ExtensionStatus = 'proposed' | 'authorised' | 'running' | 'done' | 'deferred' | 'declined';

export interface RoadmapHead {
  title: string; written_on: string; updated_on: string; source: string; one_line: string; question: string;
  wrap_up_start: string; hibernation_by: string; weekday_rule: string; replan_rule: string;
}
export interface Milestone { id: string; date: string; title: string; kind: MilestoneKind; note?: string }
export interface RoadmapGoal { id: string; text: string; owner: GoalOwner; status: RoadmapGoalStatus; note?: string }
export interface Weekend {
  id: string; number: number; start: string; end: string; days: number; status: WeekendStatus;
  title: string; outcome: string; beside: string; john_hours: string; john_items: string[]; goals: RoadmapGoal[];
}
export interface Extension { id: string; title: string; when: string; cost: string; teaches: string; status: ExtensionStatus }
export interface RoadmapDerived {
  exported_on: string; commit: string | null;
  goals_done: number; goals_counting: number; goals_total: number; goal_counts: Record<string, number>;
  weekends_done: number; weekends_working: number; weekend_counts: Record<string, number>;
  active_weekend: string | null;
  milestones: { id: string; days_to: number }[];
  // Positions on the timeline axis, as percentages of its width.
  axis: {
    start: string; end: string; today: number | null;
    weekends: { id: string; left: number; width: number }[];
    milestones: { id: string; at: number }[];
  };
}
export interface Roadmap {
  roadmap: RoadmapHead; milestones: Milestone[]; weekends: Weekend[]; extensions: Extension[]; derived: RoadmapDerived;
}

export const rm = raw as unknown as Roadmap;

export const OWNER: Record<GoalOwner, string> = { john: 'John', agents: 'Agents', both: 'John and agents' };

// A milestone's short name for the timeline axis: the part of its title before
// the colon ("Kill date 1"), or its kind for titles without one.
const KIND_SHORT: Record<MilestoneKind, string> = { kill_date: 'Kill date', wrap_up: 'Wrap-up', hibernation: 'Hibernation' };
export const milestoneShort = (m: Milestone) => (m.title.includes(':') ? m.title.split(':')[0] : KIND_SHORT[m.kind]);

export const daysTo = (id: string) => rm.derived.milestones.find((m) => m.id === id)?.days_to ?? 0;

// "Sep 26–27, 2026", or "Oct 31 – Nov 1, 2026" across a month boundary.
export function fmtRange(start: string, end: string): string {
  const d = (iso: string) => { const [y, m, dd] = iso.split('-').map(Number); return new Date(Date.UTC(y, m - 1, dd)); };
  const a = d(start), b = d(end);
  const mon = (x: Date) => x.toLocaleDateString('en-US', { month: 'short', timeZone: 'UTC' });
  const yr = b.getUTCFullYear();
  if (start === end) return `${mon(a)} ${a.getUTCDate()}, ${yr}`;
  if (a.getUTCMonth() === b.getUTCMonth()) return `${mon(a)} ${a.getUTCDate()}–${b.getUTCDate()}, ${yr}`;
  return `${mon(a)} ${a.getUTCDate()} – ${mon(b)} ${b.getUTCDate()}, ${yr}`;
}
