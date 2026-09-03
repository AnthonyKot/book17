# Chapter 04 source index

Fetch date for every item: **2026-09-03**. Pitch labels refer to the candidates in
`drafts/04.pitches.md`: A, “The backup that defeated the migration”; B, “The crossword
was not decryption”; C, “Hashing is not encryption — and not enough.”

## Primary and technical record

### OWASP Top 10:2025 — A04 Cryptographic Failures

- URL: https://owasp.org/Top10/2025/A04_2025-Cryptographic_Failures/
- What it is: OWASP category page (the chapter's spine).
- Page or section used: Description; How to prevent; especially the ECB question and the
  instruction to use a strong adaptive, salted password hash with a work factor.
- Fetch extent: full page (the repository snapshot in `resources/owasp/A04_*.txt` was
  read in full); the saved chapter excerpt is partial.
- Saved excerpt: `owasp-a04-2025.txt`.
- Pitches served: A, B, C.

### Adobe — “Important Customer Security Announcement”

- URL: https://blog.adobe.com/en/publish/2013/10/03/important-customer-security-announcement
- What it is: vendor incident announcement by Adobe chief security officer Brad Arkin.
- Page or section used: opening disclosure and the password-reset response.
- Fetch extent: full HTML article; saved excerpt is partial.
- Saved excerpt: `adobe-announcement-2013-10-03.txt`.
- Pitches served: A, B.

### Data Protection Commissioner of Ireland — Annual Report 2014

- URL: https://www.dataprotection.ie/sites/default/files/uploads/2018-11/Annual%20Report%202014.pdf
- What it is: regulator report; Case Study 16, “Compromise of Adobe Network.”
- Page or section used: printed pp. 27–29, particularly “How the Breach Occurred,”
  “Passwords,” “Storage,” and “Conclusion and Findings.”
- Fetch extent: full 36-page PDF fetched; saved excerpt is pp. 27–29 only.
- Saved excerpt: `irish-dpc-2014-adobe.txt`.
- Pitches served: A, B.

### Office of the Privacy Commissioner of Canada — PIPEDA Report of Findings #2014-015

- URL: https://www.priv.gc.ca/en/opc-actions-and-decisions/investigations/investigations-into-businesses/2014/pipeda-2014-015/
- What it is: regulator report of findings on the Adobe breach.
- Page or section used: “Details Regarding the Data Breach,” “Security Safeguards,” and
  “Findings,” paragraphs 10–20 and 31–37.
- Fetch extent: full HTML report; saved excerpt is partial.
- Saved excerpt: `canada-opc-2014-015.txt`.
- Pitches served: A, B.

### Office of the Australian Information Commissioner — Adobe own-motion investigation

- URL: https://www.oaic.gov.au/privacy/privacy-assessments-and-decisions/privacy-decisions/Investigation-inquiry-reports/adobe-systems-software-ireland-ltd-own-motion-investigation-report
- What it is: regulator investigation report.
- Page or section used: Overview; Background; the NPP 4 analysis and conclusion;
  Rectification; Recommendations; Conclusion.
- Fetch extent: full HTML report; saved excerpt is partial.
- Saved excerpt: `australia-oaic-adobe.txt`.
- Pitches served: A, B.

### LinkedIn — “LinkedIn summarizes password theft and member security efforts”

- URL: https://news.linkedin.com/2012/06/linkedin-summarizes-password-theft-and-member-security-efforts
- What it is: vendor incident response statement.
- Page or section used: “Member Commitment and Response” and “Technology Expertise.”
- Fetch extent: full HTML statement; saved excerpt is partial.
- Saved excerpt: `linkedin-statement-2012-06-12.txt`.
- Pitches served: C; the LinkedIn mirror required by the chapter contract.

### LinkedIn — “Notice of data breach: May 2016”

- URL: https://www.linkedin.com/help/linkedin/answer/a1338522/notice-of-data-brea%20ch-may-2016?lang=en
- What it is: vendor follow-up notice about data stolen in 2012 resurfacing in 2016.
- Page or section used: “What Happened?”, “What Information Was Involved?”, and “What
  We Are Doing?”.
- Fetch extent: full help article; saved excerpt is partial.
- Saved excerpt: `linkedin-notice-2016.txt`.
- Pitches served: C.

### NIST SP 800-63B — Authentication and Authenticator Management

- URL: https://pages.nist.gov/800-63-4/sp800-63b.html
- What it is: government technical standard/guideline.
- Page or section used: “Password Verifiers” in §3.1.1.2, including what salt and a cost
  factor do in an offline attack.
- Fetch extent: full HTML publication fetched; saved excerpt is the relevant subsection.
- Saved excerpt: `nist-sp800-63b-password-verifiers.txt`.
- Pitches served: A, B, C.

### Stajano et al. — “Pico without public keys”

- URL: https://uhra.herts.ac.uk/id/eprint/13828/1/2014_StajanoLomChr_postquantum_2.pdf
- What it is: paper (accepted manuscript, CC BY 4.0), by Frank Stajano, Bruce
  Christianson, Mark Lomas, Graeme Jenkinson, Jeunese Payne, Max Spencer, and Quentin
  Stafford-Fraser.
- Page or section used: pp. 1–3, “Introduction: a motivating story,” including the Adobe
  ECB/hint mechanism and the effect and limit of salting.
- Fetch extent: full 18-page PDF fetched; saved excerpt is pp. 1–3 only.
- Saved excerpt: `stajano-pico-adobe.txt`.
- Pitches served: B, C.

### Harsha et al. — “Bicycle attacks considered harmful”

- URL: https://par.nsf.gov/servlets/purl/10200731
- What it is: paper in the *Journal of Computer Security*, by Benjamin Harsha, Jeremiah
  Blocki, John Springer, and Melissa Dark.
- Page or section used: §7, “Background on LinkedIn Password Breach,” printed p. 12.
- Fetch extent: full 38-page PDF fetched; saved excerpt is the relevant paragraph only.
- Saved excerpt: `harsha-linkedin-background.txt`.
- Pitches served: C.

## Retellings used only to state folk claims

Only the quoted folk-claim sentences are saved from these sources.

### Have I Been Pwned — Adobe breach page

- URL: https://haveibeenpwned.com/Breach/Adobe
- What it is: popular breach-database retelling.
- Page or section used: “What Happened.”
- Fetch extent: full page fetched; saved excerpt is only the sentences proposed for
  quotation.
- Saved excerpt: `retelling-hibp-adobe.txt`.
- Pitches served: B.

### Wikipedia — “Adobe Inc.”

- URL: https://en.wikipedia.org/wiki/Adobe_Inc.
- What it is: encyclopedia retelling.
- Page or section used: “Customer data breach.”
- Fetch extent: page fetched partly around that section; saved excerpt is only the
  sentence proposed for quotation.
- Saved excerpt: `retelling-wikipedia-adobe.txt`.
- Pitches served: A.

### WIRED — “Was Your LinkedIn Password Leaked?”

- URL: https://www.wired.com/2012/06/linkedin-data-breach/
- What it is: press retelling by Ruth Suehle.
- Page or section used: standfirst and opening paragraph.
- Fetch extent: full article fetched; saved excerpt is only the sentence proposed for
  quotation.
- Saved excerpt: `retelling-wired-linkedin.txt`.
- Pitches served: C.

## Not fetched / not available

- **The stolen Adobe credential dump.** Not fetched and not sought: it contains stolen
  personal and credential material, is unnecessary to establish the mechanism, and would
  violate the book's understanding-not-capability rule. The three regulator reports and
  the paper above describe analyses of it.
- **Jeremi Gosney / Stricture Consulting Group's original Adobe frequency analysis.**
  Searches for the title, author, company, “Adobe,” “ECB,” and “3DES,” including a
  site-restricted search of the former company domain, found only contemporary press
  quotations and later retellings, not an accessible original post. Those retellings are
  not used as the factual record.
- **A separate full Irish DPC technical report.** The Irish DPC site and web search were
  checked. The accessible official account is Case Study 16 in the 2014 annual report;
  no separate public technical report was located. The Canadian finding also says many
  remediation details were commercially sensitive and could not be published.
- **LinkedIn's first 6 June 2012 blog post.** The historical blog URL referenced by
  contemporary coverage no longer resolved as an accessible original in search. The
  company's 12 June consolidated statement and current 2016 notice were fetched instead.
