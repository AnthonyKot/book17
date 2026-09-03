**BLOCK — the chapter misstates OWASP’s ranking arithmetic and converts several deliberately OPEN cross-chapter claims into facts.**

# Consolidated review: Chapter 00

## Ranked findings

### 1. Blocker — the central explanation of OWASP’s ranking is materially wrong

**Origin:** Missed by both reviewers.

**Location:** “The measure is the share of applications with at least one finding”; “Prevalence is half the ranking. The other half is severity”; “Here is the arithmetic” ([chapter lines 25, 35, 44](/home/diablo/book17/chapters/00-how-the-list-is-made.html:25)).

**Problem:** Incidence is calculated per CWE, not as the union of applications with any finding in the category. The displayed 3.73%, 3.00%, and 3.80% figures are average CWE incidence rates. For example, OWASP’s A02 page says 100% of tested applications had some misconfiguration while reporting a 3.00% average incidence rate ([A02 snapshot](/home/diablo/book17/resources/owasp/A02_2025-Security_Misconfiguration.txt:5)).

More importantly, the actual risk-score formula uses five terms: maximum incidence, maximum testing coverage, average exploit score, average impact score, and total occurrences. It is not “half prevalence, half severity,” and the comparison of A04’s average incidence with A01’s does not explain their ranks. The authoritative methodology page containing that formula is absent from the source pack. [OWASP’s ranking methodology](https://owasp.org/Top10/2025/0x02_2025-What_are_Application_Security_Risks/)

**Fix:** Save and index the `0x02` methodology page; define incidence and coverage per CWE; reproduce the five-term formula; distinguish the eight data-selected categories from the two survey promotions. Rewrite claims `00-what-it-is`, `00-prevalence`, and `00-three-prevalences`.

### 2. Blocker — Capital One’s OPEN SSRF reconstruction becomes fact

**Origin:** Missed by both reviewers.

**Location:** “Capital One is access control, but the route was a request forgery” ([line 50](/home/diablo/book17/chapters/00-how-the-list-is-made.html:50)); claim `00-boundaries-in-chapters` likewise says “route was SSRF” ([claims line 10](/home/diablo/book17/checks/claims/00.tsv:10)).

**Problem:** Chapter 1 explicitly says the SSRF-to-metadata route is a reconstruction that no court document confirms, and grades it OPEN ([Chapter 1 ledger](/home/diablo/book17/chapters/01-broken-access-control.html:95)). Chapter 00’s own ledger also grades it OPEN. The prose nevertheless states it as fact.

**Fix:** Say “the widely repeated reconstruction routes through SSRF, but the primary record confirms only a firewall misconfiguration,” and correct the claims row.

### 3. Blocker — the chapter reintroduces the unsupported Target alert-to-evaluation link

**Origin:** Missed by both reviewers; also makes Flash finding 2 more serious than reported.

**Location:** “Target’s own account has intruder activity detected, logged, surfaced and evaluated; the retelling stops … at ‘ignored’” and “An alert that was evaluated and then went nowhere” ([lines 63 and 93](/home/diablo/book17/chapters/00-how-the-list-is-made.html:63)).

**Problem:** Chapter 9 carefully says Target only *then believed* that some unspecified activity was evaluated and does not connect that activity to the reported FireEye alerts ([Chapter 9 line 25](/home/diablo/book17/chapters/09-evaluated-not-ignored.html:25)). Nothing establishes that a particular alert was evaluated and “went nowhere.” This is the exact linkage that Chapter 9’s prior review required removing.

**Fix:** Keep the two records separate: reported FireEye alerts on one side, unspecified evaluated activity on the other. Say the disposition of the particular alerts remains OPEN.

### 4. High — the MISSING-row synthesis and reader exercise misclassify their evidence

**Reviewer findings:** Flash 1 — **CONFIRMED**; Flash 2 — **CONFIRMED**, but its suggested Target replacement remains unsupported.

**Location:** “The MISSING rows … five times in ten” and “read only the MISSING rows” ([lines 63 and 93](/home/diablo/book17/chapters/00-how-the-list-is-made.html:63)).

**Problem:** Only the Adobe backup and xz tarball examples are actually MISSING rows.

- Maersk’s synchronized controllers are HOLDS, and Chapter 8 has no MISSING row ([Chapter 8 ledger](/home/diablo/book17/chapters/08-the-backup-that-was-not-a-backup.html:106)).
- MongoDB’s package-versus-binary default is OVERSTATED; its MISSING row concerns the gap between change and release ([Chapter 2 ledger](/home/diablo/book17/chapters/02-mongodb-ransom.html:105)).
- Colonial’s believed-disabled account is WRONG, and Chapter 7 has no MISSING row ([Chapter 7 ledger](/home/diablo/book17/chapters/07-colonial-pipeline.html:78)).
- The Target “evaluated and went nowhere” example is not established.

The claims register repeats the same false classification ([claim `00-missing-rhyme`](/home/diablo/book17/checks/claims/00.tsv:20)).

**Fix:** Rebuild the pattern strictly from actual MISSING rows, such as Adobe’s backup, xz’s tarball, MOVEit’s wider patch sequence, CrowdStrike’s pinnable sensor versus unpinnable content, and Capital One’s wider control findings. Do not retain the Target wording.

### 5. High — the population and scanner claims exceed the data record

**Origin:** Missed by both reviewers.

**Location:** “with the contributor’s tools, for the contributor’s customers”; “A weakness that no scanner finds is absent”; the three named non-web systems “were not in the population”; and “the list ranks weaknesses in code and configuration that tools can find” ([lines 29, 46, and 94](/home/diablo/book17/chapters/00-how-the-list-is-made.html:29)).

**Problem:** The source says the organizations donated data. It does not establish that every application was their customer, was tested using their own tools, or was tested by the donor itself. It also discusses manual testing, so scanner blindness does not entail absence. The corpus does not expose individual applications, making “was not in the population” unverifiable. Finally, the tool-findable description contradicts the two survey-selected categories and categories such as Insecure Design.

**Fix:** Describe only what is known: contributors supplied testing data, results were largely constrained by automatable testing, and the composition and application definition limit generalization. Replace categorical absence claims with scope warnings.

### 6. High — the xz HOLDS verdict validates what its evidence expressly cannot establish

**Reviewer finding:** Pro 3 — **CONFIRMED**.

**Location:** “an attacker who would ‘spend two years politely and enthusiastically volunteering’ … HOLDS” ([line 80](/home/diablo/book17/chapters/00-how-the-list-is-made.html:80)).

**Problem:** Git proves a two-year chronology of contributions followed by the payload. It does not prove that the account operator began as an attacker, maintained one malicious intention throughout, or was “polite and enthusiastic.” Chapter 3 itself says the evidence “says nothing about intent” ([Chapter 3 ledger](/home/diablo/book17/chapters/03-xz.html:76)).

**Fix:** Split the row: chronology can HOLDS; identity, intent, and a two-year cultivation operation remain OPEN. Regrade Chapter 3 first, then update Chapter 00 and recompute the tally.

### 7. High — the NotPetya row turns an indictment allegation into a finding

**Reviewer findings:** Flash 3 — **CONFIRMED**; Pro 2 — **CONFIRMED**.

**Location:** “DOJ indictment ¶33 … Designed to destroy, labeled as extortion” ([line 85](/home/diablo/book17/chapters/00-how-the-list-is-made.html:85)).

**Problem:** Chapter 8 correctly says “as an allegation” ([Chapter 8 line 110](/home/diablo/book17/chapters/08-the-backup-that-was-not-a-backup.html:110)); Chapter 00 drops that qualification. ESET establishes that recovery was impossible, but not the alleged conspirators’ purpose.

**Fix:** Restore “as an allegation,” or source the destructive characterization separately to Cisco’s incident-response description of a destructive payload disguised as ransomware.

### 8. High — the ledger bypasses the mandatory claims gate

**Origin:** Missed by both reviewers.

**Location:** All ten ledger rows ([lines 78–87](/home/diablo/book17/chapters/00-how-the-list-is-made.html:78)).

**Problem:** The rows contain incident facts, dates, quotations, and legal characterizations but have no `CHECK` markers or individual claims-register entries. `verify.sh 00` passes only because these claims are invisible to the marker/register comparison. A generic statement that the rows came from other chapters does not satisfy AGENT.md’s per-claim receipt rule.

**Fix:** Add `00-ledger-01` through `00-ledger-10` markers and claims rows referencing the corresponding chapter ledger and underlying documents.

### 9. High — Chapter 0’s own folk story is unsourced and absent from its ledger

**Origin:** Missed by both reviewers.

**Location:** “the most quoted document”; “quoted as a list of the ten most common vulnerabilities”; “The folk story … is a league table” ([lines 25 and 39](/home/diablo/book17/chapters/00-how-the-list-is-made.html:25)).

**Problem:** No named retelling supports these claims, and the ledger contains only one imported row per incident chapter. That violates the project rule that the folk story come from a named retelling rather than the author’s impression.

**Fix:** Cite one or more specific descriptions that call the list “most common” or treat rank as priority, then add a Chapter 0-specific ledger row testing that claim against the methodology.

### 10. Medium — the OPEN-row pattern falsely calls four different unknowns “the first step”

**Origin:** Missed by both reviewers.

**Location:** “What the record could not settle was, repeatedly, the first step” ([line 65](/home/diablo/book17/chapters/00-how-the-list-is-made.html:65)); claim `00-open-rhyme` ([claims line 23](/home/diablo/book17/checks/claims/00.tsv:23)).

**Problem:** Capital One’s SSRF route and Colonial’s credential origin concern ingress. Apple’s duplicated line concerns defect provenance, while Target’s evaluator decision occurs after detection. “They describe how an attacker began only when a trial forced it” is also an unsupported generalization.

**Fix:** Describe these as causal gaps at different stages, or restrict the “first step” pattern to the two ingress examples.

### 11. Medium — “almost every” defense has no outcome is not supported by the cited sample

**Origin:** Missed by both reviewers.

**Location:** “In almost every chapter the defense’s record is a design and a rationale with no published outcome” ([line 67](/home/diablo/book17/chapters/00-how-the-list-is-made.html:67)).

**Problem:** Claim `00-defense-thin` cites only four selected chapters, while others contain outcome evidence: MongoDB’s exposed-data trend, Google’s quantitative account-protection study, Debian’s sampled reproducibility result, and Maersk’s measured continuity during recovery. Those results have limitations, but they are published outcomes.

**Fix:** Replace “almost every” with a counted, chapter-by-chapter distinction between adoption, measured technical result, causal evidence, and unmeasured outcome.

### 12. Medium — the manual-testing tendency is converted into an absolute rule

**Reviewer finding:** Pro 1 — **CONFIRMED**.

**Location:** “manual testers list a weakness once” ([line 31](/home/diablo/book17/chapters/00-how-the-list-is-made.html:31)).

**Problem:** OWASP says manual testers “tend to” list a vulnerability once ([source line 63](/home/diablo/book17/resources/owasp/0x00_2025-Introduction.txt:63)).

**Fix:** Restore “tend to.”

### 13. Low — the claims register gives the wrong contributor count

**Reviewer finding:** Flash 4 — **CONFIRMED**.

**Location:** Claim `00-what-it-is` says “thirteen named contributors” ([claims line 31](/home/diablo/book17/checks/claims/00.tsv:31)).

**Problem:** The prose, contributor-specific claim, and source list all show twelve named organizations plus anonymous donors.

**Fix:** Change thirteen to twelve.

### 14. Low — malformed punctuation in the final ledger row

**Origin:** Missed by both reviewers.

**Location:** “one deleted `goto fail;.`” ([line 87](/home/diablo/book17/chapters/00-how-the-list-is-made.html:87)).

**Fix:** Remove the extra period or format the code phrase cleanly.
