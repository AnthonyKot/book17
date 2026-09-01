### 1. Sourcing Error: Resume Platform Mismatch (GitHub vs. GitLab)

* **Severity:** High (Record Accuracy)
* **Location:** `"Her resume, linked from the same GitHub profile, said she had been a systems engineer at the Cloud Computing Company in 2015–16."` (Paragraph 8, line 41)
* **Problem:** Factual mismatch with the primary source and the claims register. The criminal complaint ([complaint.txt](file:///home/diablo/book17/resources/sources/01/complaint.txt#L111-L114), ¶15, pp. 8–9) explicitly states that the resume was found on a *GitLab* page (`"The GitLab Net***** Page includes, among other things, a resume for 'Paige Thompson'"`), whereas the gist containing the commands was on *GitHub* (¶9, pp. 5–6). The claims file [`checks/claims/01.tsv`](file:///home/diablo/book17/checks/claims/01.tsv#L24) (row 24, `01-resume`) also specifies `"Resume on a linked GitLab page"`. The prose incorrectly states `"the same GitHub profile"`.
* **Fix:** Change `"linked from the same GitHub profile"` to `"hosted on a linked GitLab page"` or `"found on a linked GitLab page"`.

---

### 2. Unresolved Open Claim and Unfetched Resentencing Order

* **Severity:** High (Record Accuracy / Pre-ship Gate)
* **Location:** `"and in November 2025, according to CyberScoop, the district court reimposed it with fuller reasons. <!-- CHECK: 01-resentence-2025 -->"` (Paragraph 10, line 45) and Ledger Row 8 (line 101)
* **Problem:** In [`checks/claims/01.tsv`](file:///home/diablo/book17/checks/claims/01.tsv#L32), claim `01-resentence-2025` is marked as `open`. [`resources/sources/01/SOURCES.md`](file:///home/diablo/book17/resources/sources/01/SOURCES.md#L48-L49) records that the district court's November 2025 resentencing order was not fetched and relies solely on a secondary web summary ([cyberscoop-2025.txt](file:///home/diablo/book17/resources/sources/01/cyberscoop-2025.txt)). Under `AGENT.md` Pre-ship test #3 (*"Is every incident claim marked and its row non-`open`?"*), this causes `./verify.sh 01` to flag an open claim.
* **Fix:** Fetch the official district court resentencing order on remand (*United States v. Thompson*, No. 2:19-cr-00159-RSL, W.D. Wash.) into `resources/sources/01/`, verify the terms against the primary filing, and update the status in [`checks/claims/01.tsv`](file:///home/diablo/book17/checks/claims/01.tsv) from `open` to `checked-by:...`.

---

### 3. Quote Truncation Without Ellipsis

* **Severity:** Medium (Record Accuracy)
* **Location:** `"Amazon told Krebs the intrusion 'was caused by a misconfiguration of a web application firewall and not the underlying infrastructure'."` (Paragraph 16, line 67)
* **Problem:** Inexact quotation. The cited primary source ([krebs-2019-08.txt](file:///home/diablo/book17/resources/sources/01/krebs-2019-08.txt#L37-L39), lines 37–39) records Amazon's statement as: `"The intrusion was caused by a misconfiguration of a web application firewall and not the underlying infrastructure or the location of the infrastructure."` The prose omits the concluding five words inside the quotation marks without an ellipsis.
* **Fix:** Insert an ellipsis or quote the full statement:
  ```html
  Amazon told Krebs the intrusion "was caused by a misconfiguration of a web application firewall and not the underlying infrastructure or the location of the infrastructure".
  ```
  or:
  ```html
  Amazon told Krebs the intrusion "was caused by a misconfiguration of a web application firewall and not the underlying infrastructure…".
  ```

---

### 4. Lede Scope Conflation (Arrest Charge vs. Full Incident Scope)

* **Severity:** Medium (Record Accuracy / Fairness)
* **Location:** `"On 29 July 2019 the FBI arrested a Seattle software engineer for taking credit-card application data on roughly a hundred million people from Capital One's cloud storage. <!-- CHECK: 01-arrest -->"` (Lede paragraph, line 25)
* **Problem:** Conflates the scope alleged in the initial arrest affidavit with the full public/trial breach total. The criminal complaint filed on 29 July 2019 ([complaint.txt](file:///home/diablo/book17/resources/sources/01/complaint.txt#L106-L110), ¶14) charged one count of computer fraud and abuse and estimated data on `"likely tens of millions of applications"` (including ~120,000 SSNs and ~77,000 bank account numbers). The `"roughly a hundred million"` figure originated from Capital One's simultaneous press announcement and subsequent trial findings (98 million Americans). Stating that the FBI arrested her *for* taking data on roughly 100 million people attributes the full retrospective scale to the initial arrest charge.
* **Fix:** Rephrase to distinguish the arrest action from the estimated overall impact:
  ```html
  On 29 July 2019 the FBI arrested a Seattle software engineer for an intrusion into Capital One's cloud storage that exposed credit-card application data on roughly a hundred million people.
  ```

---

### 5. Placeholder Navigation Links

* **Severity:** Low (Readability / Site Integrity)
* **Location:** `<nav class="chapter-nav"><a href="../index.html">← Previous</a><a href="../index.html">Contents</a><a href="../index.html">Next →</a></nav>` (Lines 124–128)
* **Problem:** Both the `← Previous` and `Next →` navigation controls link to `../index.html` rather than sequential chapters (e.g., `00-how-the-list-is-made.html` / disabled for Previous, and `02-security-misconfiguration.html` for Next).
* **Fix:** Update `Next →` to point to `02-security-misconfiguration.html` and point `← Previous` to `00-how-the-list-is-made.html` (or omit `← Previous` if Chapter 1 is accessed directly from the index).
