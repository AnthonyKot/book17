I have reviewed the chapter HTML, the claims file, and the sources against the provided checklist. Here are the findings, ranked by severity.

### 1. Record Accuracy (Severity: High)
* **Location:** "On 21 February 2014 Apple shipped iOS 7.0.6, iOS 6.1.6 and, four days later in the same batch of notes, OS X 10.9.2. `<!-- CHECK: 10-apple-ship-date -->`"
* **Problem:** The phrase "four days later" overstates and contradicts the cited sources. The `10-apple-ship-date` row in the claims TSV explicitly states that "Apple shipped the fix on 21 Feb 2014 in iOS 7.0.6, iOS 6.1.6 and OS X 10.9.2". None of the sources cited for that claim (Adam Langley's post, the CVE record, Wheeler's excerpt) mention a four-day delay for the OS X release. The prose is relying on un-receipted memory for a specific timeline detail. 
* **Fix:** Either remove "four days later" so the prose accurately reflects the sources in the claims file, or add the actual source that proves the February 25th release date for OS X 10.9.2 to `SOURCES.md` and the TSV. 

### 2. Fairness to Named People (Severity: High)
* **Location:** "...the review says so with some pride: 'Customers have complete control over the deployment of the sensor'."
* **Location:** "...the CEO's first statement shows how much that version is feared: 'There is no impact to any protection if the Falcon sensor is installed'."
* **Location:** "Finding 5 concedes that the instance was validated but never run in the interpreter..."
* **Problem:** The chapter attributes emotion (pride, fear) and reluctance ("concedes") to CrowdStrike and its CEO. The underlying documents (a Post Incident Review and a public statement) are dry and factual; they do not state that the company felt pride or fear. This directly violates the rule: *No speculation about motive, competence or character beyond what a document states.*
* **Fix:** Remove the editorializations. Change "with some pride" to "plainly" or "states". Change "shows how much that version is feared" to "shows the priority" or "notes". Change "concedes" to "reports" or "finds".

### 3. Ledger Fairness (Severity: Medium)
* **Location:** Ledger Row 7 (Delta complaint) — "Folk story (source): 'If CrowdStrike had tested the Faulty Update on even one computer before deployment, the computer would have crashed'. (Delta complaint ¶3, an allegation.)" 
* **Location:** Ledger Row 8 — "Delta estimates that it suffered over $500 million in out-of-pocket losses" (complaint ¶2).
* **Problem:** A legal complaint is a primary document making an allegation, not a "folk story". The skeleton of the ledger is explicitly designed to test "What everyone says happened" against "what the primary documents show", using named retellings (Wired, Wikipedia, etc.) for the left column. Pitting one primary document (a lawsuit) against another (an RCA) breaks the ledger's core premise and functions as a straw man for the folk story.
* **Fix:** If the "never tested on a single machine" claim became a widespread folk myth, cite a press retelling or Wikipedia as the source for the left column, using the complaint only as context. Alternatively, remove these rows if they represent a specific legal dispute rather than a broadly held public misconception.

### 4. Readability (Severity: Low)
* **Location:** "The twelve automated tests that passed the Template Type all used a wildcard in the field that mattered; `<!-- CHECK: 10-cs-12-tests -->` Finding 5 concedes that the instance was validated but never run in the interpreter, and adds that step. `<!-- CHECK: 10-cs-instance-testing -->`"
* **Problem:** The sentence feels dense and requires re-reading to parse what "and adds that step" means (it means adding the step of running the instance in the interpreter). 
* **Fix:** Split into two sentences and clarify the addition. Example: "The twelve automated tests that passed the Template Type all used a wildcard in the field that mattered. Finding 5 reports that the instance was validated but never run in the interpreter, and adds that requirement to the test suite."
