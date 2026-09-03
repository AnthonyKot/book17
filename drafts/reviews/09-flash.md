### 1. Ledger Row 4 lacks the document required by the OPEN verdict standard (Severity: High)
* **Location:** `The ledger`, row 4 (`Recipients, judgments, and reasons remain unavailable.`)
* **Problem:** [CONTEXT.md](file:///home/diablo/book17/CONTEXT.md#L77) §4 strictly defines the `OPEN` verdict: *"the record cannot say; the chapter names what document would settle it."* In Ledger Row 4, the record cell notes what details are missing from the public record, but fails to name what specific document would resolve the question.
* **Fix:** Name the settling document directly in the Record cell (e.g. `Senate staff report, pp. 1, 4–5; Mulligan statement, pp. 2–4. Target's internal SOC case-management logs or unreleased forensic report would settle the disposition and reason.`).

---

### 2. Claims register leaves an `open` status marker in production TSV (Severity: Medium)
* **Location:** [checks/claims/09.tsv](file:///home/diablo/book17/checks/claims/09.tsv#L14), row 14 (`09-decision-path-open`)
* **Problem:** Row 14 has `open` in its status column, which causes `verify.sh` to report `1 open` and violates the pre-ship gate in [AGENT.md](file:///home/diablo/book17/AGENT.md#L68) (*"Is every incident claim marked and its row non-`open`?"*). While the historical verdict in the ledger is `OPEN`, the factual claim made in prose (that the fetched record does not establish the evaluators' decision) has been verified against the fetched source corpus.
* **Fix:** Update the status column in `checks/claims/09.tsv` from `open` to `checked-by:codex:2026-09-03` to reflect that the negative finding across the source corpus is verified.

---

### 3. GAO attribution presents Equifax officials' assertion as an auditor finding (Severity: Medium)
* **Location:** `The defense`, paragraph 5 (`GAO supplies the likely source of confusion: it says the certificate expired about ten months before the breach began.`)
* **Problem:** [GAO-18-559](file:///home/diablo/book17/resources/sources/09/equifax-gao-report.txt#L12) (p. 13) does not state "about ten months" as an independent forensic finding; it explicitly qualifies: *"According to Equifax officials... The certificate had expired about 10 months before the breach occurred"*, and notes on p. 18 that GAO did not independently assess Equifax's statements. Furthermore, the House Oversight report established from primary records that the certificate expired on January 31, 2016 (over 15 months before the breach began on May 13, 2017).
* **Fix:** Clarify that GAO was relaying Equifax officials' statements: `GAO supplies the likely source of confusion: it reports Equifax officials' statement that the certificate expired about ten months before the breach began.`

---

### 4. Ledger Row 7 omits page/section citations (Severity: Medium)
* **Location:** `The ledger`, row 7 (`M-Trends 2024 shows the long median decline, but most 2023 cases were externally notified. M-Trends 2026 records an increase from 11 days to 14 as case mix changed.`)
* **Problem:** [CONTEXT.md](file:///home/diablo/book17/CONTEXT.md#L79-L84) §4 mandates that every ledger row cite *"one specific document (cited, with page or section)."* Unlike rows 1–6, Row 7 names the reports without page numbers.
* **Fix:** Add specific page citations to the Record cell: `M-Trends 2024 Executive Edition, p. 2; M-Trends 2026 Executive Edition, pp. 2–3.`

---

### 5. Ledger Row 3 grades a headline about initial access as MISSING post-exploitation evaluation (Severity: Low)
* **Location:** `The ledger`, row 3 (`“Target Hackers Broke in Via HVAC Company.” (KrebsOnSecurity)`)
* **Problem:** Krebs's headline specifically addresses how attackers entered the network (*"Broke in"*). The Senate report confirms that entry route (`stolen credentials from an HVAC and refrigeration company`). Marking the headline itself as `MISSING` penalizes a report about initial access for not covering post-compromise SOC operations.
* **Fix:** Clarify the folk claim to represent the broader cultural retelling rather than solely the headline (e.g. `“The Target breach was an HVAC vendor break-in.” (KrebsOnSecurity headline / popular retelling)`), or clarify in the record column that while the entry vector holds, treating initial access as the complete breach story omits the internal detection and alert-evaluation breakdown.

---

### 6. Mulligan quotation truncates epistemic qualification (Severity: Low)
* **Location:** `The break`, paragraph 4 (`“Some intruder activity was detected,” Mulligan testified.`)
* **Problem:** In his [prepared statement](file:///home/diablo/book17/resources/sources/09/target-mulligan-testimony.txt#L8) (p. 3), Mulligan stated: *"We now believe that some intruder activity was detected by our computer security systems..."* Quoting only `“Some intruder activity was detected,”` removes his explicit qualification (*"We now believe that"*).
* **Fix:** Include the full clause: `“We now believe that some intruder activity was detected,” Mulligan testified.`
