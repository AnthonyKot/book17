**BLOCK — the chapter contains one false record claim and several source overstatements that must be corrected before shipping.**

# Consolidated review: Chapter 04

## Ranked findings

### 1. Critical — The record does identify part of the attackers’ route

**Origin:** Missed by both reviewers  
**Location:** [“How the attackers got in is not in any of the three reports”](/home/diablo/book17/chapters/04-adobe.html:31)

The full Australian report says the attacker compromised a public-facing web server and used it to access other Adobe servers. It does not identify how that web server was compromised, but the chapter’s categorical claim that none of the reports describes how the attackers got in is false. The source index says the full Background section was consulted, making the omission especially problematic. [OAIC report, Background](https://www.oaic.gov.au/privacy/privacy-assessments-and-decisions/privacy-decisions/Investigation-inquiry-reports/adobe-systems-software-ireland-ltd-own-motion-investigation-report)

**Fix:** Say that OAIC identifies the public-facing web server as the entry point but does not identify the vulnerability or technique used to compromise it. Add the sentence to the saved excerpt and register the claim.

### 2. High — The chapter turns retained old data into unsupported “running old code”

**Origin:** Missed by both reviewers  
**Locations:** [“older code is still running” and “Here … it was”](/home/diablo/book17/chapters/04-adobe.html:56), [“the reversible store online”](/home/diablo/book17/chapters/04-adobe.html:79), [“the correct system ran beside a reversible one”](/home/diablo/book17/chapters/04-adobe.html:114)

The reports establish that a backup database remained on a backup system/server designated for decommissioning. They do not establish that the old authentication code remained active or served logins. The chapter’s strongest lesson is data-remanence after migration; reframing it as old code still running exceeds the record.

**Fix:** Replace “older code running” with “older data or redundant systems remaining reachable.” Describe the old system as retained, not as an active authentication path.

### 3. High — The claimed defense outcome exceeds the remediation evidence

**Origin:** Missed by both reviewers  
**Location:** [“The measurable defense is that the reversible store no longer exists”](/home/diablo/book17/chapters/04-adobe.html:87)

The regulators report that the affected server was decommissioned. They do not say every copy of the reversible database was found and destroyed. The same paragraph correctly admits that no regulator checked whether another copy existed, then contradicts that caveat by declaring the store nonexistent.

**Fix:** Make the measurable result only that the affected server was decommissioned and hints abolished. Keep the existence of other copies expressly open.

### 4. High — Adobe’s replacement is equated with OWASP’s current password-hashing prescription

**Origin:** Missed by both reviewers  
**Location:** [“Adobe’s new system did this: SHA-256, salted, iterated more than a thousand times”](/home/diablo/book17/chapters/04-adobe.html:72)

OWASP calls for a strong adaptive password-hashing function and names Argon2, yescrypt, scrypt, and PBKDF2-HMAC-SHA-512. The Adobe record establishes SHA-256, salt, and more than 1,000 iterations, but does not establish the construction or that it meets the current OWASP standard. “Did this” overclaims equivalence.

**Fix:** Say the new system had the relevant structural properties—salt and repeated work—while noting that the record is insufficient to assess it against today’s recommended schemes.

### 5. High — Adobe’s characterization is presented as Canada’s finding

**Origin:** Flash #1 — **CONFIRMED**  
**Locations:** [“The Canadian report calls it…”](/home/diablo/book17/chapters/04-adobe.html:31), [ledger row 4](/home/diablo/book17/chapters/04-adobe.html:103)

Paragraph 10 says, “Adobe described” the intrusion that way. The chapter converts a party’s representation into the regulator’s voice. The Irish report independently uses “sophisticated and sustained,” so that source could support a regulator-attributed version.

**Fix:** Write “Adobe described it to the Canadian Commissioner as…” or quote the Irish finding instead. Correct the ledger attribution too.

### 6. Medium — April 2010 is attached to parameters whose start date is not established

**Origin:** Flash #2 — **CONFIRMED**  
**Locations:** [lede](/home/diablo/book17/chapters/04-adobe.html:25), [defense opening](/home/diablo/book17/chapters/04-adobe.html:79)

The record dates introduction of the replacement system to April 2010. Separately, Adobe stated that “for more than a year” its authentication system had used salted, iterated SHA-256. The sources do not date the stated work factor—or unambiguously every hashing parameter—to April 2010.

**Fix:** Separate the facts: the replacement system was introduced in April 2010; by the later period described by Adobe it used salted SHA-256 with more than 1,000 iterations.

### 7. Medium — “Every report” is not supported

**Origin:** Missed by both reviewers  
**Location:** [“every report says the copy came from the backup of the old one”](/home/diablo/book17/chapters/04-adobe.html:79)

The Irish and Australian reports identify the backup system. The Canadian report describes the accessed information and remediation but does not identify the copied database as a backup.

**Fix:** Replace “every report” with “the Irish and Australian reports.” Also phrase “no report says the hashed store was taken” as an absence in the available record, not proof that the new system repelled the attack.

### 8. Medium — Australian counts are generalized to the worldwide database

**Origin:** Missed by both reviewers  
**Location:** [“For most of the people in it, the password it held … still opened their account”](/home/diablo/book17/chapters/04-adobe.html:35)

The cited figures establish the ratio between current and obsolete password data for Australian users. They do not establish the same distribution across the global database.

**Fix:** Say “For most of the Australian users counted in the report…” or obtain a worldwide breakdown.

### 9. Medium — Two ledger rows do not use genuine folk-story sources

**Origin:** Pro #1 — **CONFIRMED, with narrowed scope**  
**Locations:** [ledger rows 5–8](/home/diablo/book17/chapters/04-adobe.html:104)

Rows 5 and 8 put vendor incident statements from Adobe and LinkedIn in the “Folk story” column, contrary to the hard requirement that the left side come from a named retelling. Row 6 is defensible: Stajano et al.’s later “motivating story” is itself a named retelling, even though the source index groups it with the technical record.

**Fix:** Replace rows 5 and 8 with corresponding claims from secondary retellings, or remove them. Row 6 can remain if the source index explicitly identifies its incident passage as a retelling.

### 10. Medium — Two LinkedIn ledger conclusions are not established by the cited excerpts

**Origin:** Missed by both reviewers  
**Locations:** [ledger rows 7–8](/home/diablo/book17/chapters/04-adobe.html:106)

Row 7 declares that the reported 300,000 passwords “were guessed.” The sources establish unsalted SHA-1 and ease of cracking, but not what happened to that particular 300,000.

Row 8 says 6.5 million “was what had been posted, not what had been taken.” LinkedIn’s cited statement explicitly calls it the theft of approximately 6.5 million; Harsha et al. gives a much larger stolen count but does not explain what the 6.5 million represented.

**Fix:** Limit row 7 to the categorical distinction that hashes are cracked or guessed, not decrypted. For row 8, describe the sources as conflicting or add a source that explicitly identifies 6.5 million as the initially published subset.

### 11. Medium — Absence of reported decryption becomes a claim that none occurred

**Origin:** Missed by both reviewers  
**Location:** [“on the record, none happened”](/home/diablo/book17/chapters/04-adobe.html:68)

The available reports do not say that the password-encryption key was recovered. That is not affirmative evidence that no password decryption occurred. Elsewhere the chapter uses the properly limited formulation, “No report says the encryption key was recovered.”

**Fix:** Use that limited formulation consistently: “The documented crossword attack did not require the key, and the reports do not say it was recovered.”

### 12. Low — Users do not “share a row”

**Origin:** Pro #2 — **CONFIRMED**  
**Location:** [“share a row of ciphertext”](/home/diablo/book17/chapters/04-adobe.html:68)

Each user has a separate database row; equal passwords produce equal ciphertext values.

**Fix:** Change this to “have identical ciphertext values in their respective rows.”

## Rejected reviewer findings

- **Flash #3 — REJECTED.** Ellipses are not normally required merely because a quotation stops before the source sentence ends. Both omitted clauses occur at the end, are grammatically separable, and their removal does not change the meaning.

- **Flash #4 — REJECTED.** The `%20` is unusual but is present in LinkedIn’s own indexed URL and currently resolves to the official notice. Removing it is not a verified correction. [LinkedIn notice](https://www.linkedin.com/help/linkedin/answer/a1338522/notice-of-data-brea%20ch-may-2016?lang=en)

- **Flash #5 — REJECTED.** The chapter already explains that ECB operates independently on fixed-size blocks. Shared-prefix leakage is technically relevant in a deeper treatment, but its omission does not make the documented equal-password mechanism wrong, and the supplied sources do not establish Adobe’s encoding and padding details needed for the reviewer’s proposed length-deduction claim.

**UNVERIFIABLE reviewer findings:** None.
