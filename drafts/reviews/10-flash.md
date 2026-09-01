### 1. Record Accuracy

* **Location:** `checks/claims/10.tsv:2` (Claim `10-apple-ship-date`) and Chapter 10, line 29 (`"On 21 February 2014 Apple shipped iOS 7.0.6, iOS 6.1.6 and, four days later in the same batch of notes, OS X 10.9.2."`)
  * **Severity:** High
  * **Problem:** In `checks/claims/10.tsv`, claim `10-apple-ship-date` asserts: *"Apple shipped the fix on 21 Feb 2014 in iOS 7.0.6, iOS 6.1.6 and OS X 10.9.2"*. This is factually inaccurate. OS X 10.9.2 (and Security Advisory HT6150) was released on 25 February 2014, four days after iOS 7.0.6 and 6.1.6 (HT6147 and HT6146). While the chapter prose recognizes the four-day gap, describing it as *"in the same batch of notes"* is imprecise and contradictory since HT6150 was an independent release published four days later.
  * **Fix:** In `checks/claims/10.tsv`, update the claim text to distinguish the release dates (iOS 7.0.6/6.1.6 on 21 Feb 2014; OS X 10.9.2 on 25 Feb 2014). In `chapters/10-goto-fail-crowdstrike.html` (line 29), replace `"and, four days later in the same batch of notes, OS X 10.9.2"` with `"followed four days later by OS X 10.9.2 (HT6150) carrying identical advisory text"`.

---

### 2. Fairness to Named People

* **Location:** Chapter 10, line 79 (`"and the review says so with some pride: 'Customers have complete control over the deployment of the sensor'"` — `<!-- CHECK: 10-cs-sensor-control -->`)
  * **Severity:** Medium
  * **Problem:** Attributing *"some pride"* to a vendor post-incident review violates CONTEXT.md §5 and AGENT.md §Priority stack #2 ("No speculation about motive, competence or character beyond what a document states"). The PIR (`crowdstrike-pir-2024-07-24.txt`) simply describes product configuration capabilities without expressing emotional sentiment.
  * **Fix:** Remove the editorializing phrase *"with some pride"*. Rephrase to: `Before the incident customers chose the sensor version, N, N-1 or N-2; the review notes: "Customers have complete control over the deployment of the sensor".`

* **Location:** Chapter 10, line 77 (`"and the CEO's first statement shows how much that version is feared: 'There is no impact to any protection if the Falcon sensor is installed'"` — `<!-- CHECK: 10-cs-no-protection-impact -->`)
  * **Severity:** Medium
  * **Problem:** Attributing *"how much that version is feared"* speculates on internal psychological motivations of George Kurtz / CrowdStrike rather than reporting the record. The statement was a factual customer assurance regarding active sensor operation during the incident.
  * **Fix:** Remove the attribution of fear. Rephrase to: `For a security sensor, failing closed is the defensible default; the fail-open alternative—a sensor that silently ceases monitoring—is what the vendor sought to assure customers against in its initial statement: "There is no impact to any protection if the Falcon sensor is installed".`

---

### 3. Mechanism Accuracy

* **Location:** Chapter 10, line 67 (`"The interpreter asks for index 20 of a 20-element array and gets whatever lies past the end"`)
  * **Severity:** Low
  * **Problem:** In C 0-based indexing, an array of 20 elements has valid indices 0 through 19, so index 20 is the 21st slot (which corresponds to field 21). While mathematically and technically exact, juxtaposing "21 fields", "20 input values", and "index 20" without explicitly stating the 0-indexed offset can momentarily confuse readers trying to map field numbers to array indices on a whiteboard.
  * **Fix:** Clarify the 0-based indexing mapping in-line: `The interpreter asks for the 21st field at index 20 of a 20-element array (valid indices 0 to 19) and gets whatever lies past the end...`

---

### 4. Ledger Fairness

* **Location:** Chapter 10, line 94 (Ledger Row 8: `"Delta estimates that it suffered over $500 million in out-of-pocket losses" (complaint ¶2; ¶48 quotes the 8-K, "at least $500 million")`)
  * **Severity:** Low
  * **Problem:** The folk column is worded as `"Delta estimates that it suffered over $500 million..."`. The cited documents (Delta complaint ¶2, SEC Form 8-K) prove that Delta *did* make that estimate, which slightly mismatches the `OPEN` verdict. The unadjudicated claim being tested is that the outage caused $500M in damages, not whether Delta estimated it.
  * **Fix:** Reframe the folk column to state the substantive claim being tested: `"The CrowdStrike outage cost Delta over $500 million in out-of-pocket losses (complaint ¶2; SEC Form 8-K, 8 Aug 2024)."` This makes the `OPEN` verdict earned against the record (which is an unresolved complaint without an adjudicated loss amount).

---

### 5. Readability & Tone

* **Location:** Chapter 10, line 54 (`"By that evening the company's chief executive had said the sentence every incident now needs: 'This was not a cyberattack'."`)
  * **Severity:** Low
  * **Problem:** The phrase *"the sentence every incident now needs"* is cynical commentary that departs from the plain, detached series voice required by CONTEXT.md §5.
  * **Fix:** Simplify to neutral phrasing: `By that evening the company's chief executive stated: "This was not a cyberattack".`
However, CrowdStrike's own published post-mortem documents (RCA Finding 5, p. 5 and PIR p. 3) explicitly admit that the Template Instances deployed on July 19 were validated only by the Content Validator and were *not* run in the Content Interpreter or tested on live endpoints prior to production rollout. While the legal cause of action remains open in court, the factual premise of whether the update was executed on an endpoint prior to rollout is admitted by the vendor's own record.
* **What Would Fix It:** Update the right column in Row 7 to state explicitly that CrowdStrike's RCA (Finding 5, p. 5) admits that Template Instances were validated against definitions but never executed in the Content Interpreter prior to deployment, making the lack of dynamic execution testing an admitted fact rather than merely an unverified complaint allegation.

---

### Finding 6 (Mechanism Accuracy / Diff Precision): Line numbering ambiguity in diff citation

* **Location:** `chapters/10-goto-fail-crowdstrike.html`, line 53:
  > `Between Security-55471 and Security-55471.14, the release for OS X 10.9.2, the entire change to this file is one deleted line: line 631, <code>goto fail;</code>. <!-- CHECK: 10-diff-one-line -->`
* **The Problem:** In `apple-sslKeyExchange-55471.txt`, lines 630 and 631 were identical (`goto fail;`). In the unified diff between `Security-55471` and `Security-55471.14` (`apple-sslKeyExchange-55471.txt` lines 92–99), diff hunk deletion removes the first identical line (line 630) and retains line 631. Asserting that specifically "line 631" was deleted is technically ambiguous depending on diff algorithm alignment.
* **What Would Fix It:** Rephrase for technical precision:
  `Between Security-55471 and Security-55471.14, the release for OS X 10.9.2, the entire change to this file is the deletion of one line: the duplicate <code>goto fail;</code> at line 630. <!-- CHECK: 10-diff-one-line -->` (or simply `the duplicate <code>goto fail;</code>`).

---

### Finding 7 (Mechanism Accuracy): Conceptual framing of OS Bugcheck as "Failing Closed"

* **Location:** `chapters/10-goto-fail-crowdstrike.html`, line 68:
  > `The machine stops, and because the driver loads at boot, it stops again on restart. That is failing closed, done by the operating system on the sensor's behalf.`
* **The Problem:** In software security and fault-tolerance taxonomy, an unhandled out-of-bounds memory read causing a kernel panic / blue screen (CWE-248 Uncaught Exception / CWE-125) is an unhandled fatal fault and catastrophic denial of service. Equating an operating system bugcheck directly to "failing closed" risks conflating an unhandled fatal crash with a designed security posture (e.g., rejecting an unauthenticated session). Although the chapter later explains in lines 78 and 80 that "fail closed at the machine was the wrong size", introducing the crash as "failing closed" in line 68 can cause a systems engineer to wince at the terminology.
* **What Would Fix It:** Clarify in line 68 that kernel panic is the operating system enforcing containment at the hardware/OS level (halting the entire system to prevent memory corruption) rather than an intentional application-level fail-closed defense.
