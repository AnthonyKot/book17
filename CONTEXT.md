# Book 17 — CONTEXT (authority document)

**Working title: *Ten Ways In*.** Ten chapters, one per category of the OWASP Top 10:2025,
each told through one real break-in and one real defense, both from the public record.
The list is the spine; the incidents are the flesh; the reader leaves able to explain
the mechanism to a colleague and to recognise it in a system they run.

Precedence (inherited from book8/book12/book15): this file → AGENT.md (reader, priority
stack, incident rules, pitch gate) → chapter contract (§6) → TEMPLATE.md → prose.

## 1. Thesis

Every famous breach has a folk version: Equifax was "one unpatched server", Colonial was
"one password", Target was "the HVAC vendor". The folk version is never false and never
the whole story. The record — the indictment, the regulator's report, the vendor's own
post-mortem, the commit — always shows something the folk version skipped, and what it
skipped is usually the part that would have helped a defender. So each chapter carries
two comparisons as its skeleton:

- **Folk story vs record.** What everyone says happened, set against what the primary
  documents show. Scored in a ledger (§4).
- **Attack vs defense.** The mechanism as it was used against a real target, set against
  a real defense that either was in place and failed for a stated reason, or was adopted
  afterward and can be shown to have worked. Defenses are quiet and poorly documented;
  where the defense record is thin the chapter says so rather than inventing a success.

The OWASP list is used as ten *lenses*, not as ten claims. Several incidents (Colonial,
NotPetya, CrowdStrike) are wider than web applications, and the book says so where it
matters. Chapter 0 examines how the list itself is made and what a reader should and
should not conclude from a ranking.

## 2. Corpus

- **Spine:** OWASP Top 10:2025, category pages and introduction, fetched 2026-09-01 into
  `resources/owasp/*.txt` (CC BY-SA 4.0). Quotations from OWASP are gated against these
  files by `checks/quotes.py`. The fetch date is the edition; if OWASP revises a page the
  quote gate will say so.
- **Per-chapter primary sources:** court filings, regulator reports (OCC, FTC, ICO,
  Senate/House committee reports), vendor post-mortems, CVE/NVD records, mailing-list
  posts, commits. Each chapter keeps a `resources/sources/NN/` directory with a
  `SOURCES.md` index (what the document is, where it came from, fetch date) and plain-text
  excerpts where the licence allows. PDFs are gitignored.
- **Secondary (named, not relied on for facts):** Wired/Ars/Krebs retellings are used to
  identify the folk story, never as the source for a ledger row.
- **No claim about what happened rides on memory.** Every incident-side factual claim in
  prose carries `<!-- CHECK: id -->` and a row in `checks/claims/NN.tsv`.

## 3. Spine — ten chapters plus chapter 0

| # | OWASP 2025 category | Break (attack) | Defense set against it |
|---|---|---|---|
| 0 | — (Introduction, Methodology) | How the list is made | what a ranking can and cannot tell you |
| 1 | A01 Broken Access Control | Capital One, 2019 (SSRF → metadata service → over-broad role) | IMDSv2; least privilege for roles |
| 2 | A02 Security Misconfiguration | MongoDB ransom wave, 2017 (no-auth default, internet-bound) | the default changed to localhost; exposed count fell |
| 3 | A03 Software Supply Chain Failures | xz-utils backdoor, 2024 (maintainer capture, build-script injection) | reproducible builds; the unfunded-maintainer threat model |
| 4 | A04 Cryptographic Failures | Adobe, 2013 (encrypted-not-hashed passwords, ECB) | password hashing done right; LinkedIn 2012 as mirror |
| 5 | A05 Injection | MOVEit Transfer, 2023 (SQLi in a file-transfer product) | parameterised queries; why the bug still ships |
| 6 | A06 Insecure Design | Strava heatmap, 2018 (no bug; the design leaked bases) | threat modeling as the only tool for a flaw with no bug |
| 7 | A07 Authentication Failures | Colonial Pipeline, 2021 (legacy VPN account, no MFA) | hardware keys; Google's staff account-takeover result |
| 8 | A08 Software or Data Integrity Failures | NotPetya via M.E.Doc update, 2017; Maersk | signed updates; offline backups; the Ghana domain controller |
| 9 | A09 Security Logging and Alerting Failures | Target, 2013 (alerts fired, not acted on); Equifax's expired cert | dwell-time trend; what changed |
| 10 | A10 Mishandling of Exceptional Conditions | Apple goto fail, 2014 (failed open); CrowdStrike, 2024 (failed closed) | which way to fail, and why both answers are wrong somewhere |

Order = OWASP order. Chapter 0 is written *last* (it must report the pattern of the
other ten, not predict it). Pilots: chapters 1, 3, 10 — chosen because their sources are
three different kinds (court/regulator record; git history and mailing list; code plus
vendor post-mortem), so the pilots test the whole method.

## 4. Ledger vocabulary (hard rule — every ledger row uses exactly one)

Each chapter's ledger sets the folk story against the record, row by row.

- **HOLDS** — the folk claim is what the record shows.
- **OVERSTATED** — true in outline, wrong in a way that matters (a number, a cause, a timeline).
- **WRONG** — the record contradicts it.
- **MISSING** — the record shows something the folk story leaves out that a defender needed.
- **OPEN** — the record cannot say; the chapter names what document would settle it.

A row is one *specific* folk claim (quoted or closely paraphrased from a named retelling)
against one *specific* document (cited, with page or section). "Equifax didn't patch" is
not a row. "Folk: one unpatched Struts server. Record: the House Oversight report (p. 26)
shows the patch notice reached the team; the scan that was meant to find unpatched hosts
was misconfigured; and a certificate on the traffic-inspection device had been expired for
19 months — MISSING" is a row.

## 5. Voice and sourcing standard

- Series voice: plain, argued, no drama for its own sake. The reader is assumed to have
  seen the headlines; the chapter's job is to show what the headline hid.
- Named people appear only as the public record names them, doing what the record says
  they did. No speculation about motive, competence or character beyond what a document
  states. Where a person was charged or found liable, say what the court said and no more.
- Mechanism is explained to the point where the reader could reproduce the *understanding*,
  not the attack. Historical code fragments already in the public record (the goto fail
  lines, the xz build-script hook) are quoted. No working exploit for any system still in
  service, no evasion recipe, no credential lists.
- No numbers from memory. Record counts, dollar figures, dates, CVE numbers: source or cut.
- Chapters are 2,200–3,400 words, on TEMPLATE.md. Paragraphs over 150 words and sentences
  over 40 are flagged by `checks/structure.py` (advisory) because the series' long tail
  of wall paragraphs is its main readability problem (measured 2026-09-01).

## 6. Chapter register (contracts)

Each chapter has one exclusive job; the pitch (AGENT.md) fixes the angle before drafting.

- **0 How the list is made.** Job: the data call, the CWE mapping, the community-survey
  categories, what moved and what merged in 2025, and what a ranking of *tested
  applications* can and cannot say about *your* application. Reports the pattern across
  chapters 1–10 (how often the folk story HOLDS). Not a summary.
- **1 Broken Access Control — Capital One.** Job: the chain from a misconfigured WAF to
  an SSRF to the metadata service to a role that could read every bucket, from the
  criminal complaint and the OCC consent order. Defense: IMDSv2 as a direct response,
  and why "least privilege" is the boring answer that would have stopped it. Must state
  clearly what SSRF is and why OWASP folded it into A01.
- **2 Security Misconfiguration — MongoDB.** Job: a default, not a bug. The 2017 ransom
  wave as measured at the time; the default-bind change; the exposed count afterward.
  The defense chapter with the best numbers in the book — use them.
- **3 Supply Chain — xz.** Job: the two-year capture of a maintainer, told from the
  commits and the mailing list (the book16 dig method). The build-script injection
  explained at the level of "what did the tarball contain that the git tree did not".
  Defense: reproducible builds and what they would and would not have caught; the
  unfunded-maintainer problem stated as a threat model, not a lament.
- **4 Cryptographic Failures — Adobe.** Job: encryption is not hashing. The 2013 dump,
  the ECB pattern leak, the password-hint crossword. Defense: what a slow salted hash
  buys and why LinkedIn 2012 (unsalted SHA-1) fell a different way.
- **5 Injection — MOVEit.** Job: one SQL injection, thousands of downstream victims. The
  CVE, the vendor advisory, the Cl0p campaign as reported by the regulators. Defense:
  parameterised queries, then the honest question of why a 2023 product shipped without
  them.
- **6 Insecure Design — Strava.** Job: no bug anywhere. The heatmap as designed; what it
  revealed; Strava's response. Defense: threat modeling, and why no scanner finds this.
- **7 Authentication — Colonial.** Job: one legacy account, from the Senate testimony.
  Defense: what a second factor would have changed, and Google's published result on
  hardware keys for staff. The chapter must not overclaim MFA: say what MFA fatigue
  (Uber 2022) shows about its limits.
- **8 Integrity — NotPetya.** Job: a legitimate update mechanism as the delivery
  channel; Maersk's recovery from one surviving domain controller. Defense: signed
  updates, offline backups, and the cost of ten days.
- **9 Logging and Alerting — Target.** Job: the alerts existed. The Senate Commerce
  report's timeline; Equifax's expired certificate as the mirror. Defense: the
  dwell-time trend (M-Trends) and what actually moved it.
- **10 Exceptional Conditions — goto fail and CrowdStrike.** Job: two failures in
  opposite directions. The Apple diff (public) and what it skipped; the CrowdStrike
  post-incident review and the out-of-bounds read. Defense: fail-closed vs fail-open is
  a decision, and the chapter shows a case where each was the wrong one.

## 7. Working method

- `AGENT.md` pitch gate; TEMPLATE beats; `verify.sh` before any commit; `scripts/review.sh
  NN` panel (two Gemini reviewers via agy, codex consolidates); corrections logged in §8.
- Parallel drafting: chapters are independent files with per-chapter claims files
  (`checks/claims/NN.tsv`) and source directories, so several can be drafted at once
  without touching the same file. `index.html` is edited only by the coordinating session.

## 8. Decision record and correction log

- 2026-09-01 — Book created. Spine fixed to OWASP Top 10:2025 (final, not RC). Pilots
  chosen: 1, 3, 10. Ledger vocabulary §4 chosen over a verdict-on-OWASP vocabulary because
  grading OWASP itself would need data the book does not have; grading the folk story
  needs only the record.
- 2026-09-01 — Pilot mode for the pitch gate: the drafting agent writes 2–4 pitches,
  picks one with a stated reason, drafts it, and banks the rest; the user re-picks after
  reading. Standard mode (user picks before drafting) resumes for chapters 2, 4–9.
