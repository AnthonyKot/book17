**VERDICT: REVISE — do not ship until the 8.5-million claim, CrowdStrike failure semantics, and several source overstatements are corrected.**

## High severity

### 1. Microsoft did not say 8.5 million devices crashed — MISSED BY BOTH

- **Location:** [chapter line 25](/home/diablo/book17/chapters/10-goto-fail-crowdstrike.html:25), “turned an estimated 8.5 million Windows machines into blue screens”; [ledger line 91](/home/diablo/book17/chapters/10-goto-fail-crowdstrike.html:91), verdict `HOLDS`.
- **Problem:** Microsoft estimated that the update “affected 8.5 million Windows devices”; it did not say every affected device crashed. The chapter upgrades an estimate of affected devices into a crash count, while the ledger incorrectly treats Wikipedia’s stronger wording as confirmed. [Microsoft excerpt](/home/diablo/book17/resources/sources/10/microsoft-weston-2024-07-20.txt:303)
- **Fix:** Use “affected an estimated 8.5 million Windows devices.” Change the ledger verdict to `OVERSTATED`, explaining that “crashed” is stronger than Microsoft’s “affected.”

### 2. The CrowdStrike “fail closed” framing conflates a fatal bug with a security policy — Reviewer Flash: **CONFIRMED**

- **Location:** [lines 68, 74, 77–80](/home/diablo/book17/chapters/10-goto-fail-crowdstrike.html:68), especially “That is failing closed,” “the code fix is a fail-open at a smaller boundary,” and “CrowdStrike’s was chosen by the platform.”
- **Problem:** A kernel bugcheck caused by an unchecked out-of-bounds read is not ordinarily called a designed fail-closed response. Neither CrowdStrike nor Microsoft uses that term. More importantly, the source does not say the bounds check makes “the rule fail” or skips it. CrowdStrike also corrected the Template Type to provide 21 inputs, so the stated “exactly what CrowdStrike’s own fix does” is unsupported. [RCA findings 1–2](/home/diablo/book17/resources/sources/10/crowdstrike-rca-2024-08-06.txt:90)
- **Fix:** Distinguish three things:

  1. Apple returned success across an authentication boundary.
  2. CrowdStrike suffered an unhandled kernel fault whose containment unit was the host.
  3. A safer content boundary would reject or quarantine malformed content while preserving the last known-good behavior.

  If “fail closed” is retained for the bugcheck, label it explicitly as an analogy about boundary size, not the standard taxonomy. Do not claim the published bounds check skips the rule unless a source states that behavior.

### 3. Apple’s release-date receipt is internally false and does not support the prose — Both reviewers: **CONFIRMED**

- **Location:** [chapter line 29](/home/diablo/book17/chapters/10-goto-fail-crowdstrike.html:29); [claim `10-apple-ship-date`](/home/diablo/book17/checks/claims/10.tsv:2).
- **Problem:** The TSV says all three releases shipped on 21 February, while the chapter says OS X 10.9.2 followed four days later. The saved Apple notes establish identical advisory text, not the original release dates; the extract’s editorial statement that all three shipped on the 21st is not supported by Langley or the CVE record. [Apple notes](/home/diablo/book17/resources/sources/10/apple-security-notes.txt:5)
- **Fix:** Add a primary source establishing the 21 and 25 February dates, then correct the TSV. “Same batch of notes” should be removed or defined. Contrary to the Pro reviewer’s alternative, simply deleting “four days later” would preserve the TSV’s likely error rather than solve it.

### 4. “Reached all Windows sensors … by 9 August” overstates “generally available” — MISSED BY BOTH

- **Location:** [chapter line 78](/home/diablo/book17/chapters/10-goto-fail-crowdstrike.html:78).
- **Problem:** The RCA says the hotfix would be “generally available by August 9,” not that it had reached or been installed on every sensor. [RCA lines 126–148](/home/diablo/book17/resources/sources/10/crowdstrike-rca-2024-08-06.txt:126)
- **Fix:** Say “was made generally available for Windows sensors 7.11 and later by 9 August.”

### 5. “Every host, at once” is contradicted by the incident scope — MISSED BY BOTH

- **Location:** [chapter line 79](/home/diablo/book17/chapters/10-goto-fail-crowdstrike.html:79).
- **Problem:** The PIR limits impact to eligible Windows hosts that were online during the 78-minute window and received the update. It does not establish simultaneous delivery or delivery to every host. [PIR lines 6–12](/home/diablo/book17/resources/sources/10/crowdstrike-pir-2024-07-24.txt:6)
- **Fix:** Say the content was cloud-delivered outside customers’ sensor-version controls and reached eligible online hosts during the deployment window.

### 6. The reboot-loop claim is not in the cited source — MISSED BY BOTH

- **Location:** [chapter line 68](/home/diablo/book17/chapters/10-goto-fail-crowdstrike.html:68), “because the driver loads at boot, it stops again on restart.”
- **Problem:** The RCA establishes that the driver loads early and that the bad access caused a bugcheck. The saved sources do not establish that every restart encountered the fault again or explain the conditions under which it did. The claim marker covers only the driver identity/loading fact.
- **Fix:** Add a source describing the repeated-boot failure, or stop after “The machine stops.”

### 7. “Anyone on the network” drops the attacker prerequisite — MISSED BY BOTH

- **Location:** [chapter line 25](/home/diablo/book17/chapters/10-goto-fail-crowdstrike.html:25).
- **Problem:** Apple’s note requires “an attacker with a privileged network position”; Langley describes breaking the proof that the server possessed the certificate’s private key. “Anyone on the network” is both unreceipted and broader.
- **Fix:** Use “an attacker able to intercept the connection could impersonate a server to an affected client without possessing the certificate’s private key.”

## Medium severity

### 8. The ledger’s “invalid certificates” verdict is wrong and combines two different claims — MISSED BY BOTH

- **Location:** [ledger line 88](/home/diablo/book17/chapters/10-goto-fail-crowdstrike.html:88).
- **Problem:** Wheeler’s claim that “invalid certificates were quietly accepted as valid” is contradicted by the cited mechanism: the certificate chain could be correct, while possession of its private key was not proved. That is `WRONG`, not merely `OVERSTATED`. The same row also includes Ars’s materially different and substantially accurate claim that a verification check was skipped.
- **Fix:** Split the row. Grade Wheeler’s “invalid certificates” claim `WRONG`; grade the skipped-signature-verification claim separately.

### 9. “Pride,” “fear,” and “concedes” assign attitude beyond the record — Both reviewers: **CONFIRMED**

- **Location:** [lines 77 and 79](/home/diablo/book17/chapters/10-goto-fail-crowdstrike.html:77).
- **Problem:** The documents state product behavior and findings; they do not express pride, fear, or reluctance. This violates the strict fairness rule. The reviewers’ High ranking is excessive, but the finding is valid.
- **Fix:** Replace with neutral verbs such as “states,” “reports,” and “found.”

### 10. The Delta complaint is not a sourced folk retelling — Reviewer Pro: **CONFIRMED**

- **Location:** [ledger lines 93–94](/home/diablo/book17/chapters/10-goto-fail-crowdstrike.html:93).
- **Problem:** The ledger contract requires its left column to come from named retellings. A litigant’s complaint is a primary adversarial allegation, not evidence of what “everyone says happened.” Both Delta rows depart from the ledger’s defined comparison.
- **Fix:** Source the claims to an actual public retelling if they became part of the folk account. Otherwise move them into a clearly labeled “disputed consequences” passage or remove them from the ledger.

### 11. The $500 million row tests the fact of Delta’s estimate, not the loss — Reviewer Flash: **CONFIRMED**

- **Location:** [ledger line 94](/home/diablo/book17/chapters/10-goto-fail-crowdstrike.html:94).
- **Problem:** The complaint and quoted 8-K conclusively establish that Delta made the estimate. Therefore that exact sentence is not `OPEN`. Whether CrowdStrike caused an adjudicated $500 million loss is open.
- **Fix:** If retained, word the proposition as “The outage caused Delta at least $500 million in losses,” while preserving the allegation/finding distinction. The broader complaint-as-folk defect remains.

### 12. The reviewer overstates what Finding 5 admits — Reviewer Flash: **UNVERIFIABLE**

- **Reviewer claim:** CrowdStrike “explicitly admit[s]” that the 19 July update was never executed on a live endpoint before rollout, so Delta’s “one computer” premise is settled.
- **Why unverifiable:** Finding 5 says testing should expand into the Content Interpreter and that every new Template Instance will receive additional testing. It does not explicitly say “no live endpoint executed this update,” and Delta’s counterfactual also depends on the test machine receiving an IPC event. [RCA lines 199–226](/home/diablo/book17/resources/sources/10/crowdstrike-rca-2024-08-06.txt:199)
- **Consequence for the chapter:** The chapter’s own categorical wording—“never run in the interpreter”—is likewise stronger than the saved passage. Say the pre-deployment process did not expose the mismatch, or source the stronger assertion.

### 13. The exact deleted Apple line number is wrong/indeterminate — Reviewer Flash: **CONFIRMED**

- **Location:** [chapter line 53](/home/diablo/book17/chapters/10-goto-fail-crowdstrike.html:53), [claim TSV line 8](/home/diablo/book17/checks/claims/10.tsv:8), and [ledger line 87](/home/diablo/book17/chapters/10-goto-fail-crowdstrike.html:87).
- **Problem:** The unified diff attributes the deletion to old line 630, while the two adjacent lines are identical and diff alignment is not semantic identity. “Line 631” is unjustified.
- **Fix:** Say only “the duplicate `goto fail;` line.” Do not replace it with the equally brittle “line 630.”

### 14. The chapter declares Apple’s choice accidental while its ledger says motive is open — MISSED BY BOTH

- **Location:** [chapter line 80](/home/diablo/book17/chapters/10-goto-fail-crowdstrike.html:80), “Apple’s was chosen by accident”; [ledger line 90](/home/diablo/book17/chapters/10-goto-fail-crowdstrike.html:90).
- **Problem:** The ledger correctly says the record cannot establish how the duplicate entered the tree. The conclusion then resolves that uncertainty as an accident.
- **Fix:** Say the resulting boundary was open “whether or not anyone intended that result,” or remove the causal phrase.

### 15. Ledger row four’s “deliberate plant” retelling is absent from the saved evidence — MISSED BY BOTH

- **Location:** [ledger line 90](/home/diablo/book17/chapters/10-goto-fail-crowdstrike.html:90).
- **Problem:** The row cites a gotofail.com FAQ “quoted by Wheeler,” but the saved Wheeler excerpt contains no such quotation. The folk claim therefore cannot be checked from the repository.
- **Fix:** Save the exact retelling and its wording, or remove the deliberate-plant side of the row.

### 16. “Channel File 292” is not a meaningful outcome test — MISSED BY BOTH

- **Location:** [chapter line 80](/home/diablo/book17/chapters/10-goto-fail-crowdstrike.html:80).
- **Problem:** In the RCA, 291 identifies the channel associated with the IPC Template Type, not an incident sequence number. The absence of a “Channel File 292” would neither test the fix nor demonstrate that the failure did not recur.
- **Fix:** End after noting that published independent findings were unavailable on the research date. Do not use absence of another incident as proof of efficacy.

### 17. The defense section promotes unaffected software and an after-the-fact diagnostic into proven defenses — MISSED BY BOTH

- **Location:** [chapter line 76](/home/diablo/book17/chapters/10-goto-fail-crowdstrike.html:76).
- **Problem:** NSS-based clients were unaffected, but the source does not show that implementation diversity was adopted as a defense against this failure. Langley’s test server detected vulnerable clients after disclosure; it was not a defense shown to have prevented the shipped bug. This conflicts with the chapter’s otherwise accurate admission that Apple’s defense record is thin.
- **Fix:** Describe these as blast-radius evidence and a post-disclosure negative test, not “defenses that demonstrably worked.”

### 18. One highlighted CrowdStrike folk claim is never adjudicated — MISSED BY BOTH

- **Location:** [chapter line 58](/home/diablo/book17/chapters/10-goto-fail-crowdstrike.html:58), “the largest outage in the history of information technology.”
- **Problem:** The chapter presents this as part of the folk story, but no ledger row tests it.
- **Fix:** Add an `OPEN` row naming what evidence could establish “largest,” or omit the claim from the chapter’s stated folk story.

## Low severity and rejected reviewer findings

### 19. Dense “adds that step” sentence — Reviewer Pro: **CONFIRMED**

- **Location:** [chapter line 79](/home/diablo/book17/chapters/10-goto-fail-crowdstrike.html:79).
- **Problem:** “Adds that step” has an unclear antecedent and is bundled with a separate twelve-test finding.
- **Fix:** Split the claims and state exactly what new test procedure was added.

### 20. “Compiled it with all warnings on” is technically misleading — MISSED BY BOTH

- **Location:** [chapter line 66](/home/diablo/book17/chapters/10-goto-fail-crowdstrike.html:66).
- **Problem:** `-Wall` does not enable all compiler warnings—the following sentence itself explains that `-Wunreachable-code` was excluded.
- **Fix:** Say “compiled it with `-Wall`.”

### 21. Zero-based index clarification — Reviewer Flash: **REJECTED**

- **Why:** “Index 20 of a 20-element array” is accurate, and the immediately preceding text already maps it to the 21st field. Adding “valid indices 0–19” is optional pedagogy, not a defect.

### 22. “The sentence every incident now needs” tone objection — Reviewer Flash: **REJECTED**

- **Why:** This is a short observation distinguishing an operational failure from an attack. It attributes no motive or character and does not outrun the record. Removing it would be a stylistic preference, not a required correction.
