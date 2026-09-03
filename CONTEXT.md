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
| 2 | A02 Security Misconfiguration | MongoDB ransom wave, 2017 (no-auth default, internet-bound) | the default changed to localhost; exposed data fell, the host count is contested |
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
  wave as measured at the time; the three defaults (package config from 2.6, binary
  default from 3.6, the images and old versions that had neither); what fell afterward
  (Shodan's exposed-data series holds; the host-count series is unsourced — say so).
  The defense chapter with the best numbers in the book — use them, with their method.
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
- 2026-09-02 — Pilots 1, 3, 10 reviewed by the panel (Gemini flash + pro, consolidated
  adversarially by codex gpt-5.6-sol) and revised. Common pattern across all three first
  drafts: sources overstated in the direction of the folk story (identity and motive
  asserted for the xz account; the SSRF-to-metadata step in Capital One stated as fact
  when the primary record does not show it; CrowdStrike's fix described as "failing
  closed"). Corrections logged per chapter in drafts/reviews/NN-applied.md. The link
  checker now skips resources/ snapshots (raw HTML saved as evidence is not a page).
  Book published at anthonykot.github.io/book17 with these three chapters.
- 2026-09-02 — Chapter 2 pitch gate (standard mode): four pitches written from the record
  (drafts/02.pitches.md); the user chose A ("three defaults, not one"), with D's
  statement-versus-change sequence folded in as a ledger row. Correction to §3/§6: the
  record supports "exposed data fell" (Shodan 2015→2020), not "exposed count fell" — the
  only host-count series (ZDNet 2020, 60,000→48,000) is unsourced. The register now says
  so rather than promising a number the chapter cannot source.
- 2026-09-02 — Chapter 5 pitch gate (standard mode): four pitches (drafts/05.pitches.md);
  the user chose A ("one function, three patches"), anchored on Rapid7's patch diff and
  Progress's own filings; B's victim-count method and D's 27–31 May timeline fold in as
  ledger rows. Known gap at pick time: the three Progress Knowledge Base advisories could
  not be fetched as text by any non-browser route; the chapter quotes them only from a
  saved copy or marks those claims open.
- 2026-09-02 — Chapter 7 pitch gate (standard mode): four pitches (drafts/07.pitches.md);
  the user chose A ("not intended to be in use"), anchored on Carmakal's House statement
  and Blount's Senate testimony; B (ransom recovery), C (TSA directives) and D (Google's
  number read carefully) fold in as ledger rows and paragraphs. Known gap at pick time:
  several .gov documents were fetched through reader proxies and are flagged in
  SOURCES.md for re-verification; the original 2021 SD-02 is SSI, only the 2024 renewal
  is public.
- 2026-09-03 — Chapters 2, 5, 7 drafted, panel-revised and wired (receipts in drafts/reviews/NN-applied.md; ch. 5's ledger shrank from eight rows to five after unearned rows were cut). All three
  evening drafting agents died at the token limit; recovered state was committed as-is.
  Ch. 2 revised by a Claude agent against the panel (drafts/reviews/02-applied.md): the
  3.6 GA date now rests on the r3.6.0 tag and the announce post, the ledger is ten rows.
  Ch. 7's claims register and structure pass, and ch. 5's prose from the finished ledger,
  were done by codex gpt-5.6-sol (logs in drafts/codex/, gitignored). Working-method
  decision: mechanical steps (registers, trims, ledger-to-prose, applying a consolidated
  panel report) go to codex by default; Claude agents only for judgment-heavy revision.
  Reason: three parallel Claude agents drained ~6% of the session quota per minute.
- 2026-09-03 — Chapter 4 and 6 pitch gates (standard mode; pitches by codex). Ch. 4: the
  user chose A ("the backup that defeated the migration"), anchored on the Irish DPC case
  study and the Australian OAIC report; B and C fold in as mechanism and defense mirror.
  Ch. 6: the user chose D ("the Pentagon did not ban the watch"), anchored on the August
  2018 DoD memorandum; the §6 contract's heatmap-as-designed mechanism and Strava's
  response come from pitch A's Strava Engineering account; B and C fold in as ledger rows.
- 2026-09-03 — Standalone-post experiment: five rewrite briefs (`scripts/prompts/
  fable-pass-v1..v5`) applied one each to chapters 1, 2, 3, 7, 10 → `posts/NN-vK.md`,
  chapters untouched. The user picks the winning brief; it then runs on the rest. Ch. 5
  received the earlier in-place five-lens edit instead (`drafts/reviews/05-fable.md`).
- 2026-09-03 (evening) — Chapters 4 and 6 drafted and wired during an OpenAI outage
  (codex unreachable). Ch. 4 (Adobe, pitch A) was drafted by the coordinating session
  from the pitch-step excerpts plus two extended regulator excerpts fetched via WebFetch.
  Ch. 6 (Strava, pitch D) was drafted by agy gemini-3.8-flash-high from the chapter brief
  in six minutes and then reviewed by the coordinating session in place of the panel:
  invented scene detail (analyst's name and age, "bare sand", "barbed-wire fences",
  invented counts), an unsupported signer and two unsupported dates, wrong textbook
  authors, and two ledger rows with no named retelling were removed or re-sourced; row 5
  regraded OVERSTATED. Both chapters carry `NN-*-date`-style open claims where a date
  rests on SOURCES.md rather than a saved excerpt. Panel review ran the same evening once
  codex returned: both BLOCK (ch. 4: the OAIC report does name the entry route, a
  compromised public-facing web server; ch. 6: the title argued against a headline about
  GPS, not watches); codex applied both reports (`drafts/reviews/04-applied.md`,
  `06-applied.md`); the memo's letterhead and date line were captured, closing the open
  claim.
- 2026-09-03 — Chapter 8 pitch gate (standard mode; pitches by codex): the user chose A
  ("the backup that was not a backup"), anchored on the DOJ indictment, Cisco's incident
  response and Ashton's Maersk account; B, C, D fold in as mechanism and ledger rows.
- 2026-09-03 — Chapter 9 pitch gate (standard mode; pitches by codex): the user chose A
  ("evaluated, not ignored"), anchored on Mulligan's Senate statement and the Senate staff
  report's timeline; B (Equifax certificate) is the mirror, C (dwell time) the defense, D
  (the report's Businessweek dependence) a caveat and OPEN row.
- 2026-09-03 (night) — Chapters 8 and 9 (codex drafts from the user's pick A each) panel-
  revised: ch. 9's thesis "evaluated, not ignored" was found to link events the sources never
  connect; retitled "Between Alert and Action". Chapter 0 written by the coordinating session
  from the OWASP Introduction (the saved Methodology file is a 404; the Introduction carries the
  methodology) and the ten ledgers; its tally sentence is recomputed from the chapters' verdict
  cells before each publish. Book-level read-through begun: titles normalised to Title Case,
  the "You know the headline" opener kept only in ch. 10.
