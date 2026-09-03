### 1. Record Accuracy / Secondary Source Boundary (Severity: High)
* **Location:** `The mechanism`, paragraph 3 ("Carmakal said there was no evidence of phishing of the employee and no earlier attacker activity; the login used a username and a password. <!-- CHECK: 07-cnn-folk --> <!-- CHECK: 07-carmakal-first-login -->")
* **Problem:** In `The break` (paragraph 3), the text promises: *"Everything below about the intrusion comes from what those two men said under oath, and from the written statements attached to their testimony."* However, Carmakal never discussed the absence of employee phishing or prior attacker activity in his sworn House testimony or written statement. That quotation was given by Carmakal in an unsworn press interview with Bloomberg, cited here via CNN (`cnn-2021-06-04.txt`). The chapter relies on a secondary press retelling as factual evidence for the intrusion mechanism, breaking both its sworn-record boundary and CONTEXT §2 ("Secondary... never as the source for a ledger row / facts").
* **Fix:** Remove the claim asserting "no evidence of phishing" from the factual explanation of the mechanism, or explicitly qualify it as an unsworn statement given to Bloomberg/CNN rather than part of the sworn record.

---

### 2. Mechanism Accuracy: MFA Fatigue vs. Origin Binding (Severity: High)
* **Location:** `The defense`, paragraph 7 ("The defence that closes a leaked-password login does not close a worn-down approval; only a factor that cannot be approved for the wrong origin does that.")
* **Problem:** The text conflates origin binding (anti-phishing) with the defense against MFA fatigue / prompt bombing. In the Uber 2022 incident cited, the attacker attempted to log in directly to Uber's *legitimate* corporate portal using purchased credentials, triggering genuine push prompts to the contractor's phone. There was no "wrong origin" involved in the prompt. Security keys (WebAuthn/FIDO) prevent MFA prompt fatigue because the authentication handshake requires local physical interaction within the active client session (e.g. tapping the key in the browser/OS client), making it impossible for a remote attacker to trigger or complete an out-of-band approval from afar.
* **Fix:** Revise the sentence to explain that security keys stop prompt fatigue because authentication is bound to the local client session requiring physical presence, rather than attributing the mitigation to origin mismatch.

---

### 3. Ledger Fairness / Straw Man Argument in Row 7 (Severity: Medium)
* **Location:** `The ledger`, Row 7 (`"the FBI has since recovered most of it" (Chairman Thompson, House hearing opening)`)
* **Problem:** Chairman Thompson's opening statement was: *"We know Colonial Pipeline paid the ransom demand and the FBI has since recovered most of it."* Thompson explicitly credited the *FBI* with the recovery, not Colonial. In terms of cryptocurrency units, the DOJ/FBI seized 63.7 of approximately 75 bitcoins (~85%), which literally is "most of it." The record cell argues the claim is OVERSTATED because *"the release records a government seizure—not recovery by Colonial"*, attacking a claim Thompson did not make. If the OVERSTATED verdict is to be earned, the overstatement is financial: in dollar terms, the $2.3 million seized was only ~52% of the $4.4 million paid due to the price collapse of Bitcoin between May 8 and June 7.
* **Fix:** Reframe the record cell to evaluate the dollar valuation ($2.3M vs. $4.4M) rather than asserting that Thompson claimed Colonial recovered the funds.

---

### 4. Record Accuracy / Claim Marker Misplacement (Severity: Medium)
* **Location:** Lede, paragraph 1 ("The profile was believed not to be enabled; it did not show up in Colonial's penetration tests; and on 29 April 2021 it accepted a username and a password and let someone in. <!-- CHECK: 07-carmakal-one-person --> <!-- CHECK: 07-blount-pen-testing --> <!-- CHECK: 07-carmakal-first-login -->")
* **Problem:** `<!-- CHECK: 07-carmakal-one-person -->` is attached to this sentence, but the claim registered in `checks/claims/07.tsv` is *"Carmakal said one person had legitimate password access as far as Mandiant knew, and that the password had been stolen from another website although its exact source was unknown"*. The lede sentence contains neither the "one person" claim nor the "stolen from another website" fact. The claim marker is already correctly placed in paragraph 12 (line 40) and paragraph 15 (line 48).
* **Fix:** Remove `<!-- CHECK: 07-carmakal-one-person -->` from the lede sentence (or replace it with `07-carmakal-misconfiguration`, which covers the legacy profile believed inactive).

---

### 5. Readability / Ambiguous Congressional Attribution (Severity: Low)
* **Location:** `The break`, paragraph 6 ("DOJ puts the 8 May payment at "approximately 75 bitcoins"; in the Senate, the chairman put it at $4.4 million and Blount described choosing to pay. <!-- CHECK: 07-blount-ransom -->")
* **Problem:** Referring simply to "the chairman" in the Senate hearing is ambiguous and slightly disjointed, especially since Chairman Thompson of the House Homeland Security Committee is introduced by name later in the chapter.
* **Fix:** Specify "Senate committee chairman Peters" or "Chairman Peters" for clarity and consistency.

---

### 6. Technical Sourcing Precision / TSA Review Context (Severity: Low)
* **Location:** `The defense`, paragraph 8 ("Colonial had not yet taken up one offered review. Blount said it probably would not have found the legacy VPN because it was questionnaire-based. <!-- CHECK: 07-blount-tsa-review -->")
* **Problem:** The text refers vaguely to "one offered review." In the transcript (`senate-hearing-2021-06-08.txt` lines 209–211), Blount explicitly named the program: TSA's "VADR program" (Validated Architecture Design Review). Naming it clarifies why it was questionnaire-based rather than a technical penetration test.
* **Fix:** Name the program directly: "TSA's offered Validated Architecture Design Review (VADR)."
