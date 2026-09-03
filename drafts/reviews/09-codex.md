**BLOCK — the chapter’s central “evaluated, not ignored” contrast links events the sources never connect and drops Target’s “we now believe” qualification.**

Consolidated report: [drafts/reviews/09-codex.md](/home/diablo/book17/drafts/reviews/09-codex.md)

Reviewer adjudication: **6 confirmed, 2 rejected, 0 unverifiable**. The report also ranks findings both reviewers missed.
 settle it.** CONTEXT §4 requires that explicitly. “Recipients, judgments, and reasons remain unavailable” names missing facts, not the missing record. Name Target's SOC case-management records, its completed forensic report, or another specific internal incident record that would show the alert disposition and response.

2. **CONFIRMED — `09-decision-path-open` is incorrectly left `open` in the claims register.** The ledger verdict may be OPEN while the chapter's narrower, corpus-bounded claim—“the fetched record does not establish…”—is checked. Other chapters use that convention. The current status violates AGENT.md's pre-ship test even though `verify.sh` treats open rows as advisory and prints `PASS`.

3. **CONFIRMED, with a correction to the reviewer's rationale — GAO's ten-month statement needs attribution to Equifax officials.** The excerpt says “According to Equifax officials.” However, GAO's later disclaimer is specifically that it did not independently assess Equifax's *remediation efforts*; it is not a blanket disclaimer of every Equifax-supplied fact. The larger defect is that the House report's exact dates—31 January 2016 to a breach beginning 13 May 2017—imply about fifteen and a half months, not GAO's ten. The chapter must expose that source conflict rather than imply that different endpoints reconcile it.

4. **CONFIRMED — ledger row 7 omits the mandatory page/section locators.** Add `M-Trends 2024 Executive Edition, p. 2` (and/or infographic, p. 1) and `M-Trends 2026 Executive Edition, pp. 2–3`.

5. **REJECTED — the HVAC MISSING verdict is allowed by this book's governing method.** CONTEXT §1 explicitly identifies “Target was the HVAC vendor” as the folk version, while §4 defines MISSING as a true claim that omits something a defender needed. The later alert-to-judgment path qualifies. The row could state the implied folk version more clearly, but the reviewer has not shown that the verdict itself violates the ledger rules.

6. **CONFIRMED — the Mulligan quotation removes a material epistemic qualifier.** The source says, “We now believe that some intruder activity was detected…”. This is not confined to the quotation on line 35: the lede, mechanism, claims register, and ledger repeatedly turn Target's retrospective belief into an unqualified fact. All repetitions need correction.

### Pro report

1. **CONFIRMED — “with the source chain left visible” is false for the cited details.** The saved Senate excerpt explicitly attributes the FireEye alert/non-reaction account and generic label to Businessweek, but it gives no named source for the Symantec assertion, and “reportedly” is not a visible source chain for the destination-server assertion. Say only that these are parts of the staff report's reconstruction from outside material.

2. **REJECTED — the fact that Target was breached does not prove that its team “did not act.”** It proves that no action prevented the breach; it does not distinguish no action from late, partial, failed, or misdirected action, nor establish the “ample time” component. Mulligan's statement establishes evaluation of unspecified activity, while the non-reaction account remains secondhand in the fetched corpus. OPEN is the defensible verdict, provided the row names the record that would settle it.

No reviewer finding is UNVERIFIABLE from the supplied chapter and source corpus.

## Ranked consolidated findings

### 1. Blocker — the title and core argument join two events the sources never join

**Location:** title and lede, “Evaluated, not ignored”; “Some intruder activity … was … evaluated”; then “Do not label the question mark ‘ignored.’” (lines 24–25, 35–37, 51, 64, and ledger rows 1, 3, and 4).

**Problem:** Mulligan said Target *then believed* that **some intruder activity** had been detected, logged, surfaced, and evaluated. He did not identify that activity as the FireEye warnings in the Businessweek/Senate reconstruction. Both propositions can therefore be true: Target may have evaluated some intruder activity while failing to react to the particular FireEye alerts. “Evaluated” also does not by itself negate every ordinary meaning of “ignored”: an item can be reviewed and dismissed without effective follow-up. The chapter carefully admits that the decision path is unknown, but its title and repeated bridge claim resolve that uncertainty in Target's favor.

**Fix:** Preserve “We now believe” wherever this testimony is quoted or paraphrased; call the evaluated activity unspecified; do not equate it with the FireEye alerts; and retitle/reframe around the genuinely supported point—the record ends between an unspecified evaluation and effective action. Keep the FireEye non-reaction claim explicitly secondhand and OPEN.

### 2. High — the chapter calls a modal CBS claim “certainty”

**Location:** “Possibility became certainty as the story travelled” and ledger row 2 (lines 45 and 103).

**Problem:** CBS says the attack “could have been prevented.” `Could have` is modal language, not certainty. The Senate's “could have potentially blocked” is more hedged and narrower—it concerns the malware's effect—and Mulligan's “may have led to different outcomes” is weaker still, but the chapter's possibility-versus-certainty contrast is linguistically false. As written, the OVERSTATED verdict is not earned by the explanation in the record cell.

**Fix:** Argue the real escalation: CBS expands a possible change in outcome or possible blocking of the malware's effect into preventability of the attack as a whole. Replace “certainty” with a precise statement about scope and confidence, and make that distinction explicit in the ledger.

### 3. High — the Equifax timing paragraph conceals a contradiction between its sources

**Location:** “GAO supplies the likely source of confusion: it says the certificate expired about ten months before the breach began. Those are different intervals with different endpoints.” (line 83; ledger row 5).

**Problem:** GAO attributes the ten-month figure to Equifax officials. More importantly, the House report says both that the certificate expired on 31 January 2016 and that the intrusion began on 13 May 2017—about fifteen and a half months later. Thus GAO's ten months and the House report's exact dates use the same endpoint (breach onset) and conflict. Only the House report's nineteen-month figure uses discovery as the endpoint. The chapter's endpoint explanation makes the record look consistent when it is not, and “likely source of confusion” speculates about the origin of Wikipedia's nine-month sentence without a source trail.

**Fix:** Attribute GAO's number to Equifax officials, calculate and state the conflict with the House dates, separate the onset and discovery clocks, and leave the origin of Wikipedia's number unknown unless its citation chain is fetched.

### 4. Medium — the second Equifax MISSING row invents an exhaustive folk claim

**Location:** “The Equifax monitoring problem was ‘the certificate.’ (Wikipedia)” (line 107).

**Problem:** The saved Wikipedia excerpt says only, “The certificate had been expired for nine months.” It does not say that this was the whole monitoring problem, that only one certificate was expired, or that certificate inventory and ownership were otherwise sound. The ledger turns a singular reference to the breach-relevant certificate into a broader causal claim, then faults that constructed claim for incompleteness. That is not a close paraphrase of the named retelling.

**Fix:** Delete this ledger row or source a retelling that actually reduces the control failure to one certificate. Keep the 324/79 inventory evidence in prose as a broader lesson without assigning a verdict to wording Wikipedia did not use.

### 5. Medium — the OPEN row fails the ledger's settlement-document rule

**Location:** ledger row 4, “Recipients, judgments, and reasons remain unavailable” (line 105).

**Problem:** This does not say what document would settle the question, as CONTEXT §4 requires.

**Fix:** Name the needed Target SOC alert/case records, completed forensic report, or equivalent internal incident record showing receipt, disposition, rationale, and follow-up action.

### 6. Medium — the prose claims a visible source chain where none is shown

**Location:** “These details belong to the report's reconstruction, with the source chain left visible” (line 43).

**Problem:** The Senate excerpt provides no named source for the Symantec sentence and only says “reportedly” for the destination-server sentence. The claim overstates the report's sourcing transparency.

**Fix:** Describe them as claims in the staff report's outside-source reconstruction; do not say their source chain is visible.

### 7. Medium — the claims register has a pre-ship open status for a checkable corpus claim

**Location:** `checks/claims/09.tsv`, `09-decision-path-open`.

**Problem:** `verify.sh 09` reports 25 markers, 25 rows, and `1 open`. The negative claim is explicitly bounded to the fetched record and can be checked against that corpus, even though the underlying historical question and ledger verdict remain OPEN.

**Fix:** After naming the missing settling document, mark the claims row checked and keep the ledger verdict OPEN.

### 8. Medium — ledger row 7 lacks required page/section citations

**Location:** M-Trends ledger row (line 108).

**Problem:** CONTEXT §4 makes page or section citations mandatory for every ledger row; this row names reports only.

**Fix:** Cite the 2024 infographic p. 1 / Executive Edition p. 2 and the 2026 Executive Edition pp. 2–3.

### 9. Low — the public Reading list omits several documents the chapter asks the reader to trust

**Location:** Reading (lines 119–125).

**Problem:** The chapter relies materially on GAO-18-559, the FTC complaint and order, M-Trends 2026, and both Wikipedia retellings, but none appears in the Reading list. The invisible claims register is not a substitute for reader-facing provenance, especially where the prose discusses a source conflict.

**Fix:** Add links for the materially used GAO, FTC, M-Trends 2026, and folk-retelling sources, or trim claims whose sources will not be exposed to the reader.
