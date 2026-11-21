// Typed view of site/src/data/tracker.json, written by scripts/export_tracker.py from the
// tracker records in data/tracker/ (2026-11-21). Every tracker page reads from here and
// nowhere else, so the pages can never disagree with the scores (tracker pattern rule 1.5).
//
// Two habits the site check (scripts/check_site.py) relies on:
// - every number or date a tracker page shows goes through the N component, which writes
//   the raw value into a data-n attribute; the check refuses any other digit on the page and
//   any data-n value the data files do not carry;
// - every sentence quoted from a record goes through the R component (data-rec), whose text
//   the check finds in the data files word for word.
import raw from '../data/tracker.json';

export type State = 'untested' | 'supported' | 'contradicted' | 'mixed' | 'scores nothing';

export interface Source { id: string; citation: string; url: string | null; published?: string; published_long?: string }
export interface StudyRow {
  study: string; name: string; url: string | null; group: string; first_appeared: string; first_appeared_long: string;
  outcome: 'for' | 'against' | 'mixed' | null; settled_by: string; counted: boolean; why: string;
  weight: number; multiplier: number;
  protections: { registered: boolean; outside_camp: boolean; rival_agreed: boolean; replicated: boolean };
  readings: { who: string; verdict: string; reason: string; date: string }[];
  judgement: string;
}
export interface Prediction {
  id: string; theory: string; theory_name: string; core_claim: string; statement: string; stated_by: 'proponent' | 'site'; half_reason: string | null; null_excused_by: Source | null;
  first_stated: { source: Source | null; date: string | null; date_long: string | null; passage: string | null; location: string | null };
  test_for: string; test_against: string;
  separates_from: { theory: string; name: string; how: string; source: Source | null }[];
  could_fail: boolean; separates: boolean; testability_settled: string;
  state: State; studies: StudyRow[]; counted_count: number; verify_open: string[];
}
export interface Claim { id: string; plain: string; quote: string; location: string; level: number; half_reasons: string[]; predictions: string[]; sharp: number }
export interface Move {
  kind: 'claim' | 'probe' | 'probe-short'; claim?: string; claim_plain?: string; prediction?: string; statement?: string;
  from?: number | null; to?: number; for?: number; against?: number; weight?: number; passes_bar?: boolean;
  starts_score?: boolean; groups?: number; groups_needed?: number;
}
export interface Theory {
  id: string; name: string; plain: string; proponents: string[]; own: boolean;
  claims_from: Source | null; fixed_on: string; fixed_on_long: string; first_scored: string | null; first_scored_long: string | null;
  testability: number; support: number | null; left_to_test: number | null;
  past_bar: boolean; group: string; leans_against: boolean;
  claims_count: number; claims_sharp: number; claims_lacking: string[]; claims_needed_more: number;
  rests_on: { outcomes: number; studies: number; groups: number; group_names: string[]; total_weight: number };
  left_counts: { untested: number; total: number; placeholders: number; distinguishing: number };
  rank: number | null; ranked_count: number;
  tied: { with: string; with_name: string; study: string; study_name: string }[];
  claims: Claim[]; predictions: string[]; move: Move[];
  explained_afterwards: { prediction: string; study: string; name: string }[];
  verify_open: string[];
}
export interface OpenQuestion { id: string; title: string; plain: string; bears_on: string[] }
export interface Tracker {
  rules: Record<string, number>; probe_weight: number;
  listed: { id: string; name: string; scored: boolean }[]; listed_count: number; scored_count: number;
  groups: {
    ranked: { theory: string; rank: number }[]; testable: string[]; not_sharp: string[]; not_scored: string[];
    close_pairs: { a: string; b: string; study: string; study_name: string }[];
  };
  theories: Record<string, Theory>; predictions: Record<string, Prediction>;
  studies: Record<string, { id: string; name: string; group: string; opened: boolean; url: string | null; found_through_contrast: boolean }>;
  studies_count: number; contrast_count: number; judgement_count: number; judgement_status: Record<string, number>;
  verify_open: { id: string; statement: string; records: string[] }[]; verify_open_count: number;
  headline: {
    share_tested: number | null; tested: number; distinguishing: number; theories_scored: number; theories_listed: number;
    worked_out_on: string; worked_out_on_long: string; last_reading: string | null; last_reading_long?: string | null; waiting_studies?: number;
  };
  last_judgement: string; last_judgement_long: string;
  open_questions: OpenQuestion[];
  waiting: { waiting_studies: number; by_theory: Record<string, number>; last_reading: string | null; last_reading_long: string | null } | null;
  hand_check: { checked: number; random: number; own: number; read_again: number; theories: number; date: string | null } | null;
  refs: Record<string, { label: string; url: string | null }>;
  links: { people: Record<string, string>; theories: Record<string, string>; groups: Record<string, string>; person_pages: string[] };
  support_example: { theory: string; name: string; weighted_sum: number; total_weight: number; ratio: number; half_ratio: number; half_ratio_abs: number; support_exact: number; support: number } | null;
}

export const tk = raw as unknown as Tracker;
export const theory = (id: string) => tk.theories[id];
export const pred = (id: string) => tk.predictions[id];
export const listedName = (id: string) => tk.listed.find((t) => t.id === id)?.name ?? id;

// Small whole numbers written as words, as the line above the title does ("ten of them").
const WORDS = ['no', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve'];
export const word = (n: number) => WORDS[n] ?? String(n);

export const STATE_LABEL: Record<State, string> = {
  'untested': 'untested', 'supported': 'supported', 'contradicted': 'contradicted', 'mixed': 'mixed', 'scores nothing': 'scores nothing',
};
export const STATE_CLASS: Record<State, string> = {
  'untested': 'untested', 'supported': 'ok', 'contradicted': 'no', 'mixed': 'mixed', 'scores nothing': 'off',
};
export const OUTCOME_LABEL: Record<string, string> = { 'for': 'for', 'against': 'against', 'mixed': 'mixed' };

// The ranking's three ruled groups, in order (kickoff section 4, ranking rule 1).
// Titles ruled by John on 2026-11-21 ("Take the new titles"). Each note carries the ruled test
// in the same words (the bar: more than half the main claims, each with a prediction that could
// fail and that a rival's own published work predicts differently; and studies from two separate
// groups), because a title alone would promise less than the rule asks. "{groups}" is replaced
// by the ruled count of groups, from the records.
export const BAR_TEST = "main claims come with a prediction that could fail and that no rival theory's own published work predicts too";
export const GROUPS = [
  { key: 'ranked', title: 'Ranked by the evidence', note: `more than half its ${BAR_TEST}, and it has counted studies from at least {groups} separate research groups; listed from the most support to the least` },
  { key: 'testable', title: 'Waiting for more studies', note: `more than half its ${BAR_TEST}, but it does not yet have counted studies from {groups} separate research groups` },
  { key: 'not_sharp', title: 'Not yet clear enough to test', note: `half or fewer of its ${BAR_TEST}` },
] as const;

// The export's group names, shown by their ruled titles wherever a page names a theory's group.
export const groupTitle = (g: string) =>
  g === 'ranked' ? GROUPS[0].title : g.startsWith('testable') ? GROUPS[1].title : GROUPS[2].title;

// Why a prediction scores half a point on how clearly its theory can be tested (John, 2026-11-21,
// "Add the half-score line"), in the words About uses for the rule.
export const HALF_REASON: Record<string, string> = {
  inferred: 'it is inferred here, not stated by the theory\'s proponents',
  null_excused: 'its supporters wrote in advance that a result showing nothing should not count against it',
  partly: 'it could fail only in part',
};

// Where a claim's dot sits: filled when a proponent states a prediction that could fail and
// separates the theory from a rival, half when only the site has inferred one, empty otherwise.
export const dotClass = (level: number) => (level >= 1 ? 'full' : level > 0 ? 'half' : '');
