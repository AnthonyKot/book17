### 1. Unnamed Folk Retelling in Ledger Row 4 (Straw Man Risk)

* **Severity:** High (Ledger Fairness / Sourcing Rule)
* **Location:** `"The update-server shorthand makes 27 June sound like one poisoned download."` (Ledger Row 4, line 107)
* **Problem:** Violates `AGENT.md` (§ Incident rules: *"Identify the folk story from named retellings (cite them — Wired, Krebs, the Wikipedia lede) so the ledger's left column is real, not a straw man"*) and `CONTEXT.md` §4 (*"A row is one specific folk claim (quoted or closely paraphrased from a named retelling)"*). Unlike all other rows which explicitly name their retelling (e.g., Wired, BleepingComputer, BBC, Darknet Diaries), Row 4's left column cites no source. The saved source excerpt in [`wikipedia-petya.txt`](file:///home/diablo/book17/resources/sources/08/wikipedia-petya.txt#L6) contains Wikipedia's lede (*"It was believed that the software update mechanism of M.E.Doc… had been compromised to spread the malware"*), which represents this shorthand. Presenting the left column as an unsourced summary turns it into an author-constructed straw man.
* **Fix:** Attribute the shorthand to a specific named retelling in the left cell:
  ```html
  <tr><td>Wikipedia's summary reduces the infection vector to a compromised “software update mechanism of M.E.Doc” on 27 June.</td><td>DOJ indictment ¶¶34, 37–38, as allegations: earlier modified update files preceded temporary rerouting and final delivery. Cisco reports changed code and server configuration. <!-- CHECK: 08-ledger-stages --></td><td class="verdict v-missing">MISSING</td></tr>
  ```

---

### 2. Sourcing Distortion: Staff Access Conflated with Account Inspection

* **Severity:** High (Record Accuracy)
* **Location:** `"Cisco says M.E.Doc let its responders inspect engineers' accounts, logs and code."` (Break section, paragraph 4, line 33)
* **Problem:** Factual distortion of the cited primary source. Cisco Talos ([`cisco-medoc.txt`](file:///home/diablo/book17/resources/sources/08/cisco-medoc.txt#L10), line 10) reports: `"M.E.Doc was exceptionally open in arranging access to engineers and administrators who walked the team through the system and provided access to log files and code."` The source describes access to personnel (interviews and system walkthroughs with engineers), not inspecting `"engineers' accounts"` (user accounts or credentials). In fact, the compromise involved a stolen administrator account, not engineers' accounts.
* **Fix:** Rephrase to match Cisco's statement:
  ```html
  Cisco says M.E.Doc was exceptionally open, granting responders access to its engineers and administrators, log files and code.
  ```

---

### 3. Unresolved Open Claim Statuses in TSV Register

* **Severity:** High (Pre-ship Verification Gate)
* **Location:** Claims `08-ghana-open`, `08-signing-open`, `08-ledger-ghana`, `08-ledger-signing` in [`checks/claims/08.tsv`](file:///home/diablo/book17/checks/claims/08.tsv#L13-L30) (lines 13, 17, 26, 29)
* **Problem:** In [`checks/claims/08.tsv`](file:///home/diablo/book17/checks/claims/08.tsv), four rows have their status set literally to `open`. While the ledger verdict in the chapter is legitimately `OPEN` (as defined in `CONTEXT.md` §4), `AGENT.md` Pre-ship test #3 (*"Is every incident claim marked and its row non-`open`?"*) requires that every claim row in the register be audited and signed off. Leaving `open` in column 5 causes `./verify.sh 08` to report 4 unresolved open claims.
* **Fix:** Once the open-record source audit in [`resources/sources/08/SOURCES.md`](file:///home/diablo/book17/resources/sources/08/SOURCES.md#L61-L68) is verified, update column 5 for these four rows from `open` to `checked-by:codex:2026-09-03` (or the reviewing auditor ID).

---

### 4. Sequential Navigation Skips Chapter 9

* **Severity:** Medium (Site Integrity / Navigation)
* **Location:** `<a href="10-goto-fail-crowdstrike.html">Next →</a>` (Chapter navigation, line 137)
* **Problem:** The navigation link points directly to Chapter 10 (`10-goto-fail-crowdstrike.html`), bypassing Chapter 9 (`09-evaluated-not-ignored.html`).
* **Fix:** Update line 137 to point to Chapter 9:
  ```html
  <a href="09-evaluated-not-ignored.html">Next →</a>
  ```

---

### 5. Incomplete Citation of Maersk White Paper

* **Severity:** Medium (Record Accuracy / Sourcing)
* **Location:** `“What we learned from the NotPetya Virus cyber-attack”` in prose (line 53), Reading list (line 128), and [`checks/claims/08.tsv`](file:///home/diablo/book17/checks/claims/08.tsv#L14) (line 14)
* **Problem:** The citation names only the title of the callout box on page 4 of the PDF rather than the actual published document. As recorded in [`resources/sources/08/SOURCES.md`](file:///home/diablo/book17/resources/sources/08/SOURCES.md#L32), the publication is *A View from the Other Side of a Crisis: The Maersk China case to mitigate the world's largest supply chain disruptor – COVID-19*. A reader opening the link will see the COVID-19 crisis title and may believe the link is incorrect.
* **Fix:** Cite the full white paper title along with the retrospective section:
  ```html
  Maersk, <a href="https://www.maersk.com/~/media_sc9/maersk/stay-ahead/maersk---a-view-from-the-other-side-of-a-crisis---final.pdf"><cite>A View from the Other Side of a Crisis</cite></a>, p. 4 (“What we learned from the NotPetya Virus cyber-attack”).
  ```

---

### 6. Over-Argued Verdict on Podcast Colloquialism in Ledger Row 7

* **Severity:** Low (Ledger Fairness)
* **Location:** `"Maersk's later retrospective says the network was rebuilt in ten days while cargo kept moving. “Functioning” and “rebuilt” are different thresholds."` (Ledger Row 7, line 110)
* **Problem:** The ledger grades Darknet Diaries' phrase `"after about nine days"` as `OVERSTATED` against Maersk's corporate white paper statement of rebuilding the network in `"just 10 days"`. `"About nine days"` is an approximate colloquial phrase in spoken audio that spans 8–10 days; treating the 1-day difference as a substantive evidentiary overstatement borders on pedantry. The genuine difference is the threshold (a functioning core network vs. full network rebuild).
* **Fix:** Clarify the record explanation in Row 7 so the verdict focuses cleanly on the threshold conflation rather than the day count:
  ```html
  <tr><td>Darknet Diaries says Maersk had a functioning network after about nine days.</td><td>Maersk's retrospective reports rebuilding the network in ten days while keeping cargo moving; Darknet Diaries equates an initial milestone to full recovery. <!-- CHECK: 08-ledger-days --></td><td class="verdict v-overstated">OVERSTATED</td></tr>
  ```

---

### 7. Missing Visual/Diagrammatic Anchor in Mechanism Section

* **Severity:** Low (Mechanism Usability / Whiteboard Test)
* **Location:** `"Draw these four boxes clearly on a whiteboard: source code, build artifact, update service, client."` (Mechanism section, paragraph 17, line 62)
* **Problem:** While the four-box model and its two governing verification questions are conceptually clear, the section relies entirely on prose. Unlike other chapters that provide concrete code/config fragments or explicit text schematics, the reader must infer the diagram structure purely from verbal instructions.
* **Fix:** Add a compact text schematic or ASCII diagram illustrating the four stages, the transport channel (TLS), and the artifact signing boundary:
  ```html
  <pre><code>[ Source Code ] ──> [ Build Artifact ] ──> [ Update Service ] ──(TLS)──> [ Client ]
                            │                                                ▲
                            └──────── (Digital Signature) ───────────────────┘</code></pre>
  ```
