# Verdict: REVISE — material sourcing and MFA-mechanism errors remain, alongside several unearned ledger verdicts.

## Ranked findings

### 1. High — The chapter breaks its own primary-record boundary

**Location:** [chapter line 31](/home/diablo/book17/chapters/07-colonial-pipeline.html:31), “Everything below about the intrusion comes from what those two men said under oath”; [line 49](/home/diablo/book17/chapters/07-colonial-pipeline.html:49), “no evidence of phishing … and no earlier attacker activity.”

**Reviewer adjudication:** **CONFIRMED — Flash 1; CONFIRMED — Pro 1.**

The latter claim comes only from CNN relaying Carmakal’s Bloomberg interview, not from either congressional record. That violates both the chapter’s explicit promise and CONTEXT’s rule against relying on secondary retellings for facts.

The reviewers missed a related problem: the Senate transcript records Blount being sworn, but the House transcript records no oath for Carmakal or Blount. Therefore “both … under oath” is unsupported by the gathered record.

**Fix:** Describe them simply as public congressional testimony, and remove the phishing/prior-activity sentence or identify it explicitly as a press-interview claim outside the sworn record.

### 2. High — The MFA-fatigue explanation names the wrong protective property

**Location:** [line 65](/home/diablo/book17/chapters/07-colonial-pipeline.html:65), “only a factor that cannot be approved for the wrong origin does that.”

**Reviewer adjudication:** **CONFIRMED — Flash 2.**

Uber’s attacker generated genuine prompts through Uber’s legitimate authentication service; there was no wrong origin. Origin binding explains resistance to phishing sites. A security key also resists remote prompt bombing because it signs the challenge for the local client session and requires user presence there—the victim cannot approve the attacker’s separate session through an out-of-band push.

**Fix:** Separate the two protections: origin binding defeats relay phishing; local, challenge-bound user presence defeats the Uber-style remote approval flow.

### 3. High — The lede says the East Coast’s fuel supply stopped

**Location:** [line 25](/home/diablo/book17/chapters/07-colonial-pipeline.html:25), “the fuel supply of the American East Coast stopped for most of a week.”

**Missed by both reviewers.**

The record says Colonial’s pipeline operations stopped; the pipeline supplied nearly half the East Coast’s fuel. It does not say the region’s entire fuel supply stopped. The claim also has no matching claim marker.

**Fix:** Say that Colonial shut the pipeline supplying nearly half the East Coast’s fuel, and register the percentage if retained.

### 4. Medium — The defense section misapplies the paper’s 52% friction result

**Location:** [line 64](/home/diablo/book17/chapters/07-colonial-pipeline.html:64), “challenges caused 52% of legitimate users initially to fail a sign-in … A second factor is both barrier and friction.”

**Missed by both reviewers.**

Doerfler et al.’s 52% figure concerns risk-triggered login challenges collectively, across numerous device-, knowledge-, delegation-, and recovery-based mechanisms. It is not a security-key or general MFA failure rate. The paper separately reports 88.2% same-session success for 2FA and says 2FA exhibited similar friction to password-only authentication.

**Fix:** Either describe the 52% figure strictly as risk-aware login-challenge friction or replace it with the paper’s 2FA/security-key-specific usability measurements.

### 5. Medium — The ransom-recovery ledger verdict is unearned

**Location:** [line 81](/home/diablo/book17/chapters/07-colonial-pipeline.html:81), “the FBI has since recovered most of it” → `OVERSTATED`.

**Reviewer adjudication:** **CONFIRMED — Flash 3; CONFIRMED — Pro 2.**

Thompson attributed recovery to the FBI, not Colonial. DOJ’s seizure of 63.7 of approximately 75 bitcoins supports “most.” The record cell rebuts a claim Thompson never made.

Flash’s proposed dollar-value rewrite is **REJECTED**: “it” can naturally refer to the bitcoin ransom, and changing valuation does not disprove recovery of most of the paid units.

**Fix:** Change the verdict to `HOLDS`, or remove the row.

### 6. Medium — The prose attributes intention and universal knowledge beyond the testimony

**Locations:** [line 38](/home/diablo/book17/chapters/07-colonial-pipeline.html:38), “Not a VPN they had decided to leave weak”; [line 59](/home/diablo/book17/chapters/07-colonial-pipeline.html:59), “a path nobody knew was live.”

**Missed by both reviewers.**

Blount said Colonial “could not see” the profile and that it did not appear in penetration testing; Carmakal said it was not believed enabled. Neither establishes what every employee knew or proves that no conscious decision had ever been made about it.

**Fix:** Retain the record’s epistemic limits: “a profile Colonial said it could not see and believed disabled.”

### 7. Medium — The Hassan ledger row enlarges her claim to manufacture an overstatement

**Location:** [line 79](/home/diablo/book17/chapters/07-colonial-pipeline.html:79), “Colonial ‘did not have two-step authentication in place’” → `OVERSTATED`.

**Missed by both reviewers.**

Hassan made the remark while summarizing the legacy-VPN discussion. The ledger treats it as a company-wide claim, then rebuts it with Colonial’s normal RSA-token practice. That broader reading is not clearly earned by the quoted context.

**Fix:** Include enough surrounding context to prove Hassan meant company-wide authentication, or mark/remove the row rather than using it as an `OVERSTATED` claim.

### 8. Medium — “Inactive account” is assigned the wrong ledger vocabulary

**Location:** [line 77](/home/diablo/book17/chapters/07-colonial-pipeline.html:77), “an inactive … account” → `MISSING`.

**Missed by both reviewers.**

The record shows the profile accepted a login. That contradicts “inactive”; it is not merely an omitted defensive detail. Under the book’s fixed vocabulary, `WRONG` is the cleaner verdict.

**Fix:** Change the verdict to `WRONG`, while retaining the useful distinction between believed-disabled and observably disabled.

### 9. Low — The Wikipedia/OT verdict is stronger than the quoted wording permits

**Location:** [line 76](/home/diablo/book17/chapters/07-colonial-pipeline.html:76), “computerized equipment managing the pipeline” → `WRONG`.

**Missed by both reviewers.**

CISA contradicts direct OT impact, but Wikipedia’s phrase does not explicitly say OT; it could encompass affected business IT. The wording is misleading, but the cited record does not unequivocally contradict it.

**Fix:** Use `OVERSTATED`, or select a folk claim that explicitly says the ransomware infected operational controls.

### 10. Low — One claim marker is attached to an unrelated sentence

**Location:** [line 25](/home/diablo/book17/chapters/07-colonial-pipeline.html:25), `07-carmakal-one-person`.

**Reviewer adjudication:** **CONFIRMED — Flash 4.**

That register entry concerns legitimate password access and reuse on another website; the lede sentence concerns the profile accepting a login. The other two markers already support the lede.

**Fix:** Remove this marker or replace it with `07-carmakal-misconfiguration`.

## Rejected reviewer findings

- **REJECTED — Flash 5:** “in the Senate, the chairman” is adequately disambiguated from the later House reference by the sentence itself. Naming Peters would be a harmless polish, not a reportable ambiguity.
- **REJECTED — Flash 6:** “one offered review” is accurate and understandable in context. Adding the unexplained acronym `VADR` would not clarify why it was questionnaire-based; moreover, the gathered excerpt supplies the acronym but not its expanded name.
