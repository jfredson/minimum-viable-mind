"""For each reviewer sentence the ruling adopts, report whether version 5 carries it
word for word. 'exact' = byte-identical substring. 'normalised' = identical after
collapsing whitespace and mapping curly quotes/apostrophes to straight ones and
ignoring inserted parenthetical glosses is NOT done here; glosses are reported by
checking the pieces around them separately where the writer inserted one."""
import re, sys
v5 = open(sys.argv[1]).read()
def norm(s):
    s = s.replace('“', '"').replace('”', '"').replace('’', "'").replace('‘', "'")
    return re.sub(r'\s+', ' ', s).strip()
V = norm(v5)
adopted = {
 # item: (source, sentence)
 '7 A2 s1': 'The difference-of-averages sweep found no discovery-position clearance for either target: 135 tests read the registered marker-word target and 135 read the register index.',
 '7 A2 s2': 'Positive-control detections occurred where the answer was supplied by the input token (`powered-position-sweep-findings.md`).',
 '9 A4 s1': 'The successor proceeds through Gate A with both tiers as soon as its prerequisites are complete.',
 '9 A4 s2': 'The operative deadlines remain registration by 2026-10-18 and launch of the registered runs by 2026-11-01; missing either is recorded as a schedule failure (`docs/rulings/2026-09-20-december-result-roadmap.md`, including its 2026-09-21 annotation).',
 '11 A6 successor': 'A successor must demonstrate both its control ceiling and a usable comparison metric; measuring the ceiling alone does not resolve this defect.',
 '11 restriction (ruling words)': 'any control fully determined by the visible episode and not requiring ownership',
 '12 ruling phrase': 'excluded the exclusion confound in the form proposed, a four-way rank of the other agent that this probe could decode',
 '14 A10 s1 head': 'John ruled the 2026-09-16 blind arm',
 '14 A10 s1 tail': 'discharged, so it does not block this closure.',
 '14 A10 s2': 'That disposition does not establish successful recovery of an acquired ownership representation on the A3 design.',
 '14 A10 s3': 'The unmet sensitivity requirement carries into the successor’s rehearsal',
 '15 A11 s1 head': 'Patching is not scheduled for A3; the December-result ruling assigns its construction to the successor',
 '15 A11 s2 head': 'No further investigation of the other-agent revision-value position is authorised under the follow-up ruling',
 '15 A11 s3': 'The marker-word fitted read remains deferred, and whether it runs before the paper remains undecided.',
 '15 A11 s4': 'These limitations do not imply that the missing measurements have been satisfied.',
 '16 A12 headline': '**Outcome: not testable — the registered comparison was undefined for every possible model. Separately, removing the ownership-input channel reduced primary-battery accuracy on all three trained seeds.**',
 '17 A13 s1': '“Above zero” is the project’s classification under its 2026-09-20 definition of a load-bearing input, not a measured integration score.',
 '17 A13 s2': 'A3 does not establish that binding specifies its center in the same act, and it provides no licensed verdict about consciousness or experience.',
 '17 A13 public': 'Removing the ownership-input channel reduced primary-battery accuracy on three trained seeds. The matched comparison was unavailable; whether an acquired internal ownership structure exists was not established, and integration degree was not measured.',
 '18 A14 s1': 'The fitted register-index read had a heuristic reach of approximately one episode in eleven, calculated using its positive-control accuracy.',
 '18 A14 s2 head': 'This is not measured detection power at the discovery positions and does not establish the sensitivity of the unrun fitted marker-word read (`fitted-position-sweep-findings-CORRECTION-2026-09-20.md`',
 '19a A15': '“The validity-gate bin was not evaluated: its gates were unimplemented and unapplied.”',
 '19b ruling': 'had not been attacked before registration',
 '19c A15': '“The state drop was 0.0769 on seed 2, versus 0.0018 and 0.0002 on the other seeds; all were below the locked 0.1172 threshold.”',
 '19d A15': '“An accuracy margin of 0.000484, equivalent to 1.94 of 4,000 episodes.”',
 '19d as used': 'an accuracy margin of 0.000484, equivalent to 1.94 of 4,000 episodes',
 '19e A15': '“The second estimator produced one nominal crossing; its folds and permutation draws also differed, so the change cannot be attributed to scaling alone.”',
 '19f A15': '“Ownership-channel dependence was established; recovery of an acquired internal representation by this stack was not.”',
 '5 ruling': 'never applied to the input-channel lesion, the only lesion A3 ran, on any seed',
 '6 ruling': 'per-row gradient weight quadrupled',
 '2 Gemini G6 verbatim': 'Because causal patching was never run, probe-patching convergence could not be tested and no L1 subspace was ever localized; therefore, the registered uncarvable signature H_diffuse was never reachable',
 '2 ruling/proposal words': 'Because causal patching was never run, agreement between probe and patching could not be tested and no L1 subspace',
 '1 ruling: tests whether two instruments agree': 'tests whether two instruments agree',
 '1 ruling: never built': 'Causal patching was never built for this design (ruling of 2026-09-20, ledger RT-96), so the test was never run',
 '1 ruling: rests on 3.2': "rests instead on §3.2's convergence requirement",
 '1 ruling: closes under loss condition': "closes under the pre-registration's loss condition above, with no further A3 seeds",
 '1 ruling: John': "This reading of the registered kill list is John's, ruled on 2026-09-25",
 '1 ruling: K5 is not reached': 'K5 is not reached',
 '8 ruling: 46.2': 'about $46.2',
 '8 ruling: 227.6': 'about $227.6',
 '8 ruling: 450': 'raised from $400 to $450 on 2026-09-25',
 '8 ruling: page 6': '`docs/rulings/2026-09-26-weekend-1-queue.md`, page 6',
 'A6 main replacement NOT adopted (should be absent)': 'John applied the registered loss condition and ruled the outcome',
 'A8 full replacement NOT adopted (should be absent)': 'did not support the proposed explanation',
 'A7 replacement NOT adopted verbatim (ruling words used instead)': 'Localization was not established under',
 'v4 2026-10-11 (should be absent)': '2026-10-11',
 'v4 never converged (should be absent)': 'never converged',
 'v4 270 tests (should be absent)': '270 tests',
 'v4 $44.3 (should be absent)': '44.3',
 'v4 $225.7 (should be absent)': '225.7',
 'A15b invalidated (should be absent)': 'invalidated',
 'v4 quadrupled weight (should be absent)': 'at quadrupled weight',
}
print(f'{"item":60} exact  normalised')
for k, s in adopted.items():
    exact = s in v5
    nrm = norm(s) in V
    print(f'{k:60} {str(exact):6} {str(nrm)}')
