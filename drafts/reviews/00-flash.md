### Finding 1 (Severity: Blocker — Record Accuracy)

* **Location:** `<p>The MISSING rows are where the defender's lesson lived, and they rhyme. The thing the folk story left out was, five times in ten, a second copy or a second place. Adobe's replacement system was running; the old reversible store was kept as a backup. Maersk's controllers were synchronised peers; none was a time-separated copy. xz's trigger was never in git; it was in the release tarball. MongoDB's safe default lived in a package file; the binary said otherwise. Target's own account has intruder activity detected, logged, surfaced and evaluated; the retelling stops at the vendor's door and at "ignored". <!-- CHECK: 00-missing-rhyme --></p>` ([00-how-the-list-is-made.html#L63](file:///home/diablo/book17/chapters/00-how-the-list-is-made.html#L63))
* **Problem:** The prose claims that these five examples represent "The MISSING rows ... five times in ten". However:
  1. In Chapter 08 ([08-the-backup-that-was-not-a-backup.html](file:///home/diablo/book17/chapters/08-the-backup-that-was-not-a-backup.html)), the row concerning synchronised controllers (Row 1) is graded **HOLDS**, and Chapter 08 has zero MISSING rows in its ledger.
  2. In Chapter 02 ([02-mongodb-ransom.html](file:///home/diablo/book17/chapters/02-mongodb-ransom.html)), the row concerning the package configuration vs. binary default (Row 2) is graded **OVERSTATED**, not MISSING (Chapter 02's sole MISSING row is Row 5, which concerns the timing gap between specification/commit and announcement).
  Asserting that the Maersk and MongoDB examples were "MISSING rows" contradicts the ledgers in Chapters 08 and 02.
* **Fix:** Rephrase the paragraph to cite genuine MISSING rows from the book that demonstrate the "unreviewed twin / second place" or defender's lesson (for example, Chapter 10 Row 7: CrowdStrike's unpinnable Channel File configuration update vs. the dormant sensor code defect; Chapter 01 Row 6: systemic cloud governance/audit/alert dispositioning vs. the proximate WAF misconfiguration; or Chapter 05 Row 3: the four additional SQLi flaws requiring patches across the product vs. the single publicized CVE-2023-34362). Update [checks/claims/00.tsv](file:///home/diablo/book17/checks/claims/00.tsv#L20) for claim `00-missing-rhyme` accordingly.

---

### Finding 2 (Severity: High — Ledger Fairness & Reader Takeaway)

* **Location:** `<p>Take the list and find the category your own system's folk story lives in: the breach your team cites when it argues for a control. Then open that chapter's ledger and read only the MISSING rows. Each names a thing the famous story left out that a defender needed. A backup that still held the secret. A tarball that was not the tree. A default that lived in one install path. An account that was believed disabled. An alert that was evaluated and then went nowhere.</p>` ([00-how-the-list-is-made.html#L93](file:///home/diablo/book17/chapters/00-how-the-list-is-made.html#L93))
* **Problem:** The reader is directed to "read only the MISSING rows" and given five examples. Two of these examples do not correspond to MISSING rows in their respective chapters:
  1. "An account that was believed disabled" refers to Chapter 07 ([07-colonial-pipeline.html](file:///home/diablo/book17/chapters/07-colonial-pipeline.html)), which contains zero MISSING rows (the account status is graded WRONG in Row 3 and OVERSTATED in Row 1).
  2. "A default that lived in one install path" refers to Chapter 02 ([02-mongodb-ransom.html](file:///home/diablo/book17/chapters/02-mongodb-ransom.html)), where that claim is graded OVERSTATED in Row 2.
  A reader inspecting those chapters' ledgers for MISSING rows will not find these claims.
* **Fix:** Align the examples in Line 93 strictly with actual MISSING rows across the chapters (e.g., "A backup that still held the secret" [Ch. 4, Row 1], "A tarball that was not the tree" [Ch. 3, Row 5], "A configuration update that triggered a dormant sensor defect" [Ch. 10, Row 7], "An alert that was evaluated and then went nowhere" [Ch. 9, Row 3], "A patch for one function while four more injection flaws remained" [Ch. 5, Row 3]).

---

### Finding 3 (Severity: Medium — Fairness to Named People & Legal Precision)

* **Location:** `<tr><td>Ch. 8: the "NotPetya ransomware attack" (BBC).</td><td>DOJ indictment ¶33: "the purported ransomware purpose of NotPetya was a ruse"; ESET found recovery impossible. Designed to destroy, labelled as extortion.</td><td class="verdict v-wrong">WRONG</td></tr>` ([00-how-the-list-is-made.html#L85](file:///home/diablo/book17/chapters/00-how-the-list-is-made.html#L85))
* **Problem:** In Chapter 08 ([08-the-backup-that-was-not-a-backup.html#L75](file:///home/diablo/book17/chapters/08-the-backup-that-was-not-a-backup.html#L75)), the ledger row explicitly qualifies the DOJ indictment: `DOJ indictment ¶33, as an allegation: the ransomware purpose was a ruse, and files could not be recovered after payment.` In Chapter 00's ledger table, the qualifying phrase "as an allegation" was dropped. An unadjudicated indictment must be receipted as an allegation.
* **Fix:** Add `, as an allegation:` to the record cell in Chapter 00's ledger Row 8:
  ```html
  <td>DOJ indictment ¶33, as an allegation: "the purported ransomware purpose of NotPetya was a ruse"; ESET found recovery impossible. Designed to destroy, labelled as extortion.</td>
  ```

---

### Finding 4 (Severity: Low — Claims Register Discrepancy)

* **Location:** `checks/claims/00.tsv` line 31 ([checks/claims/00.tsv#L31](file:///home/diablo/book17/checks/claims/00.tsv#L31))
* **Problem:** The claim text in TSV row `00-what-it-is` states: `The 2025 list ranks ten categories across applications tested by thirteen named contributors...`. However, the prose in Chapter 00 ([00-how-the-list-is-made.html#L25](file:///home/diablo/book17/chapters/00-how-the-list-is-made.html#L25) and [L29](file:///home/diablo/book17/chapters/00-how-the-list-is-made.html#L29)), the TSV entry for `00-contributors` ([checks/claims/00.tsv#L11](file:///home/diablo/book17/checks/claims/00.tsv#L11)), and the primary source ([0x00_2025-Introduction.txt#L91-L115](file:///home/diablo/book17/resources/owasp/0x00_2025-Introduction.txt#L91-L115)) all state **twelve** named contributors (Accenture Prague, Bugcrowd, Contrast Security, CryptoNet Labs, Intuitor SoftTech Services, Orca Security, Probely, Semgrep, Sonar, usd AG, Veracode, Wallarm) plus anonymous donors.
* **Fix:** Change `thirteen named contributors` to `twelve named contributors` in [checks/claims/00.tsv](file:///home/diablo/book17/checks/claims/00.tsv#L31).
