### 1. Misattribution of Party Representation as Regulator Finding

* **Severity:** High (Record Accuracy / Fairness to Named Entities)
* **Location:** `"The Canadian report calls it 'a sophisticated, long-term intrusion of its computer systems'. <!-- CHECK: 04-opc-intrusion -->"` ([chapters/04-adobe.html:L31](file:///home/diablo/book17/chapters/04-adobe.html#L31)) and Ledger Row 4 ([chapters/04-adobe.html:L103](file:///home/diablo/book17/chapters/04-adobe.html#L103))
* **Problem:** Attributes Adobe's self-characterization to the Privacy Commissioner of Canada. The cited source ([`canada-opc-2014-015-extended.txt`](file:///home/diablo/book17/resources/sources/04/canada-opc-2014-015-extended.txt#L7), ¶10) states: `"Adobe described a sophisticated, long-term intrusion of its computer systems."` Stating that the Canadian report itself calls it that elevates an audited entity's submission into an official finding of fact by the regulator.
* **Fix:** Change the phrasing to reflect that Adobe provided this description, or cite the Irish DPC report ([`irish-dpc-2014-adobe.txt`](file:///home/diablo/book17/resources/sources/04/irish-dpc-2014-adobe.txt#L8)), which made its own finding in similar language:
  ```html
  Adobe described it to the Canadian Commissioner as "a sophisticated, long-term intrusion of its computer systems".
  ```
  or:
  ```html
  The Irish report calls it "a sophisticated and sustained intrusion of Adobe's computer systems".
  ```

---

### 2. Overstatement of System Launch Date vs. Iteration Work Factor Date

* **Severity:** Medium (Record Accuracy)
* **Location:** `"Adobe's authentication system had hashed and salted passwords since April 2010. <!-- CHECK: 04-new-system-2010 -->"` ([chapters/04-adobe.html:L25](file:///home/diablo/book17/chapters/04-adobe.html#L25)) and `"It was the new system: hashing, salting, a work factor, live since April 2010."` ([chapters/04-adobe.html:L79](file:///home/diablo/book17/chapters/04-adobe.html#L79))
* **Problem:** Conflates the April 2010 launch date of the new authentication system with the specific parameterization (iterated SHA-256 >1,000 times). The primary document ([`australia-oaic-adobe-extended.txt`](file:///home/diablo/book17/resources/sources/04/australia-oaic-adobe-extended.txt#L21-L22)) distinguishes two facts: (1) `"Adobe introduced a new system in April 2010 as a more secure means of authenticating users..."`, and (2) `"For more than a year, Adobe's authentication system has cryptographically hashed customer passwords using the SHA-256 algorithm, including salting the passwords and iterating the hash more than 1,000 times."` While Paragraph 12 of the chapter ([chapters/04-adobe.html:L45](file:///home/diablo/book17/chapters/04-adobe.html#L45)) reports this distinction accurately, the lede and defense sections collapse them into a single claim that the full work-factor scheme had been live since April 2010.
* **Fix:** Align the lede and defense text with the Irish DPC and OAIC source wording:
  ```html
  Adobe had introduced a replacement authentication system in April 2010 that hashed and salted passwords.
  ```
  and:
  ```html
  It was the new system: hashing, salting, a work factor, running in production long before the intrusion.
  ```

---

### 3. Quotation Truncations Without Ellipses

* **Severity:** Medium (Record Accuracy)
* **Location 1:** `"The Irish Data Protection Commissioner: 'Attackers identified and removed data from a backup server that stored the compromised data'. <!-- CHECK: 04-dpc-backup-server -->"` ([chapters/04-adobe.html:L33](file:///home/diablo/book17/chapters/04-adobe.html#L33))
* **Location 2:** `"LinkedIn's own statement of 12 June says it had 'completed a long-planned transition from a password database system that hashed passwords, i.e. provided one layer of encoding, to a system that both hashes and salts the passwords'. <!-- CHECK: 04-linkedin-transition -->"` ([chapters/04-adobe.html:L89](file:///home/diablo/book17/chapters/04-adobe.html#L89))
* **Problem:** In both instances, closing clauses inside the quoted sentence are omitted without an ellipsis:
  - The Irish DPC excerpt ([`irish-dpc-2014-adobe.txt`](file:///home/diablo/book17/resources/sources/04/irish-dpc-2014-adobe.txt#L9-L10)) reads: `"Attackers identified and removed data from a backup server that stored the compromised data described above."`
  - The LinkedIn statement excerpt ([`linkedin-statement-2012-06-12.txt`](file:///home/diablo/book17/resources/sources/04/linkedin-statement-2012-06-12.txt#L12-L14)) reads: `"...to a system that both hashes and salts the passwords, i.e. provides an extra layer of protection."`
* **Fix:** Add ellipses or include the complete clauses:
  ```html
  The Irish Data Protection Commissioner: "Attackers identified and removed data from a backup server that stored the compromised data described above".
  ```
  and:
  ```html
  LinkedIn's own statement of 12 June says it had "completed a long-planned transition from a password database system that hashed passwords, i.e. provided one layer of encoding, to a system that both hashes and salts the passwords…".
  ```

---

### 4. Malformed URL in Reading List and Source Index

* **Severity:** Low (Readability / Source Integrity)
* **Location:** `href="https://www.linkedin.com/help/linkedin/answer/a1338522/notice-of-data-brea%20ch-may-2016?lang=en"` ([chapters/04-adobe.html:L122](file:///home/diablo/book17/chapters/04-adobe.html#L122)) and [`resources/sources/04/SOURCES.md:L70`](file:///home/diablo/book17/resources/sources/04/SOURCES.md#L70)
* **Problem:** The URL contains an errant URL-encoded space (`%20`) within the word `breach` (`brea%20ch`).
* **Fix:** Update the URL to `https://www.linkedin.com/help/linkedin/answer/a1338522/notice-of-data-breach-may-2016?lang=en`.

---

### 5. Mechanism: Block-Level Equality Omission in ECB Explanation

* **Severity:** Low (Mechanism Accuracy)
* **Location:** `"Three people with the same password share a row of ciphertext. Whoever reads the table can group users by ciphertext without knowing the key, and then read every hint in a group."` ([chapters/04-adobe.html:L68](file:///home/diablo/book17/chapters/04-adobe.html#L68))
* **Problem:** While technically correct for identical full passwords, the explanation does not mention 3DES's 64-bit (8-byte) block boundary. In ECB mode, passwords sharing the same 8-byte prefix (e.g., `password1` and `password2`) also produce identical initial 8-byte ciphertext blocks (`2fca9b003de39278`), allowing prefix grouping and length deduction across differing passwords. 
* **Fix:** Add a brief clause clarifying that ECB mode leaks equality block-by-block (every 8 bytes for 3DES), exposing identical full passwords as well as shared 8-byte password prefixes.
