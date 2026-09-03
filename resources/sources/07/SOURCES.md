# Sources — chapter 07 (A07 Authentication Failures — Colonial Pipeline, 2021; hardware keys)

All fetched 2026-09-02 for the pitch stage (no chapter drafted yet). PDFs, where kept, are
local and gitignored; the `.txt` files alongside are the excerpts actually read. Several
government hosts (tsa.gov, cisa.gov, gao.gov, fbi.gov, hsgac.senate.gov, federalregister.gov)
returned 403/CAPTCHA to both curl and WebFetch; where noted, the text was obtained through
the `r.jina.ai` reader proxy, which fetches the same URL server-side and returns its text.
Those copies should be re-verified against the originals in a browser before a ledger row
rests on a page number. justice.gov serves an Akamai interstitial; followed with curl as in
chapter 01.

## Primary — Congress

| File | Document | What it is | URL | Fetched? | Used for |
|---|---|---|---|---|---|
| `senate-hearing-2021-06-08.txt` (+ `senate-hrg.pdf`) | *Threats to Critical Infrastructure: Examining the Colonial Pipeline Cyber Attack*, Senate HSGAC, 8 June 2021, S. Hrg. 117-429, CHRG-117shrg46569 | **Hearing transcript** (GPO). Sworn oral testimony and Q&A; Blount's prepared statement is appended | https://www.govinfo.gov/content/pkg/CHRG-117shrg46569/html/CHRG-117shrg46569.htm (PDF: `/pdf/CHRG-117shrg46569.pdf`) | Yes (curl) | Peters/Portman openings (the "news reports" framing, 75 BTC, 63.7 BTC); Blount: "legacy VPN profile that was not intended to be in use"; "did only have single-factor authentication. It was a complicated password"; "we use an RSA token"; "did not show up in any pen testing"; TSA review "would not have resulted in finding that legacy VPN"; "$200 million over the last five years in our IT systems" |
| `house-hearing-2021-06-09.txt` (+ `house-hrg.pdf`) | *Cyber Threats in the Pipeline: Using Lessons from the Colonial Ransomware Attack to Defend Critical Infrastructure*, House Homeland Security Committee, 9 June 2021, CHRG-117hhrg45085 | **Hearing transcript** (GPO) with the prepared statements of Blount and of Charles Carmakal (SVP/CTO, FireEye Mandiant) | https://www.govinfo.gov/content/pkg/CHRG-117hhrg45085/html/CHRG-117hhrg45085.htm (PDF: `/pdf/CHRG-117hhrg45085.pdf`) | Yes (curl) | Carmakal statement: earliest evidence 29 April 2021, "legacy VPN profile and an employee's username and password", "did not require a one-time passcode"; Mandiant engaged 7 May via Hunton Andrews Kurth; DarkSide RaaS/affiliates; Q&A: "wasn't believed to be active", "misconfiguration", "One person", password "stolen from another website", "we do not know exactly where it came from". This is the Mandiant account of the credential — the primary for what the press attributed to Carmakal |
| `blount-senate-testimony.txt` | Joseph Blount, written testimony to the Senate HSGAC, 8 June 2021 (Word→PDF, "MASTER Testimony (6.4 441pm)") | **Prepared witness statement** | https://www.hsgac.senate.gov/wp-content/uploads/imo/media/doc/Testimony-Blount-2021-06-08.pdf | Reader proxy at pitch stage; **confirmed at drafting** against the Wayback copy of the PDF and against the Appendix of the govinfo hearing PDF (direct) | Ransom note found "just before 5:00 AM EDT on Friday, May 7th"; Operations Supervisor "put in the stop work order"; restart "Wednesday evening, May 12"; the legacy-VPN sentence; remediation |

The House joint-subcommittee hearing of 15 June 2021 on the *federal* response
(CHRG-117hhrg45085 is the 9 June full-committee hearing; the 15 June one is
congress.gov event LC67088) was identified but not fetched — no Colonial witness.

## Primary — executive branch and regulator

| File | Document | What it is | URL | Fetched? | Used for |
|---|---|---|---|---|---|
| `doj-seizure-2021-06-07.txt` | DOJ OPA press release, "Department of Justice Seizes $2.3 Million in Cryptocurrency Paid to the Ransomware Extortionists Darkside", 7 June 2021 | **Government press release**; the seizure is "as alleged in the supporting affidavit" | https://www.justice.gov/opa/pr/department-justice-seizes-23-million-cryptocurrency-paid-ransomware-extortionists-darkside (now redirects to `/archives/opa/pr/...`) | Yes (curl, following the bm-verify interstitial) | 63.7 BTC "currently valued at approximately $2.3 million"; "approximately 75 bitcoins"; ransom paid 8 May; warrant by Magistrate Judge Laurel Beeler, N.D. Cal.; "the FBI has the 'private key'" |
| `cisa-aa21-131a.txt` | CISA/FBI Joint Advisory AA21-131A, "DarkSide Ransomware: Best Practices for Preventing Business Disruption from Ransomware Attacks", 11 May 2021, rev. 8 July 2021 | **Government advisory** | https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-131a | Yes — WebFetch (summary) and reader proxy (full text); cisa.gov 403 to curl | "gaining initial access through phishing and exploiting remotely accessible accounts and systems and Virtual Desktop Infrastructure"; "proactively disconnected certain OT systems"; first mitigation "Require multi-factor authentication for remote access to OT and IT networks"; RaaS definition |
| `fbi-statement-2021-05-10.txt` | FBI Statement on Compromise of Colonial Pipeline Networks, 10 May 2021 | **Government statement** (two sentences) | https://www.fbi.gov/news/press-releases/fbi-statement-on-compromise-of-colonial-pipeline-networks | Reader proxy at pitch stage; **confirmed at drafting** against the Wayback snapshot of 11 May 2021 (fbi.gov still 403) | Attribution to DarkSide |
| `tsa-press-2021-05-27.txt` (proxy returned navigation only; body not captured; **not used** — the Federal Register notice is used for SD-01) | TSA press release, "DHS Announces New Cybersecurity Requirements for Critical Pipeline Owners and Operators", 27 May 2021 | **Regulator press release** for SD Pipeline-2021-01 | https://www.tsa.gov/news/press/releases/2021/05/27/dhs-announces-new-cybersecurity-requirements-critical-pipeline | Text via reader proxy (tsa.gov 403; the URL ending `-owners` 404s) | Report incidents to CISA; Cybersecurity Coordinator 24/7; review and report gaps within 30 days; Mayorkas quote |
| `fedreg-2021-20738.txt` | 86 FR 52953, "Ratification of Security Directive", 24 Sept 2021 (TSOB ratification of SD Pipeline-2021-02) | **Federal Register notice**; §I.A and §I.B describe both 2021 directives as issued | https://www.federalregister.gov/documents/2021/09/24/2021-20738/ratification-of-security-directive | Reader proxy at pitch stage; **confirmed at drafting** against the Wayback copy (federalregister.gov returned 500 direct) | SD-01 issued 26 May 2021, effective 28 May: report within 12 hours, coordinator, self-assessment; SD-02 issued 19 July 2021, effective 26 July: mitigation measures, contingency plan, annual third-party architecture review. The original SD-02 text was not published (SSI) |
| `tsa-sd-pipeline-2021-02e.txt` (+ `tsa-sd02e.pdf`) | TSA Security Directive Pipeline-2021-02E, effective 27 July 2024 (renewal of SD-02; "continues to require performance-based regulatory cybersecurity measures first issued by TSA on July 26, 2021") | **Security directive**, current public text of the SD-02 series | https://www.tsa.gov/sites/default/files/tsa-security-directive-pipeline-2021-02e-and-memo-508c.pdf (tsa.gov 403; identical PDF fetched from https://www.mangancyber.com/wp-content/uploads/2024/08/tsa-security-directive-pipeline-2021-02e-and-memo-508c.pdf) | Mirror PDF at pitch stage; **confirmed at drafting** against the Wayback copy of the tsa.gov PDF (byte-identical III.C text; tsa.gov still 403) | §III.C.1–5: password-reset schedule; "Multi-factor authentication, or other logical and physical security controls that supplement password authentication to provide risk mitigation commensurate to multi-factor authentication"; least privilege; shared-account rules. Use with care: this is the 2024 wording; the July 2021 wording is not public |
| `tsa-sd-pipeline-2021-01e.txt` (not quoted in the chapter; not re-verified) | TSA Security Directive Pipeline-2021-01E, effective 3 May 2025 (renewal of SD-01) | **Security directive**, current public text of the SD-01 series | https://www.tsa.gov/sites/default/files/tsa-security-directive-pipeline-2021-01e-and-memo-508c.pdf | Text via reader proxy (tsa.gov 403) | The three continuing requirements (reporting, coordinator, assessment) |
| `gao-21-105263.txt` | GAO-21-105263, "Critical Infrastructure Protection: TSA Is Taking Steps to Address Some Pipeline Security Program Weaknesses", testimony, 27 July 2021 | **GAO testimony** (summarises GAO-19-48 and the 2021 directives) | https://www.gao.gov/assets/gao-21-105263.pdf (product page: https://www.gao.gov/products/gao-21-105263) | Reader proxy at pitch stage; **confirmed at drafting** against the Wayback copy of the PDF (gao.gov still 403) | Voluntary guidelines before May 2021; what SD-01 and SD-02 require; the open 2018 recommendations |

## Primary — defense record (hardware keys, MFA limits)

| File | Document | What it is | URL | Fetched? | Used for |
|---|---|---|---|---|---|
| `krebs-2018-security-keys.txt` | Krebs on Security, "Google: Security Keys Neutralized Employee Phishing", 23 July 2018 | **Journalist's article carrying Google's statement**. No Google Security Blog post exists for this claim; every 2018 retelling (9to5Google, Slashdot, Gizmodo, Fortune) cites Krebs. Treat the numbers as a vendor statement to a reporter | https://krebsonsecurity.com/2018/07/google-security-keys-neutralized-employee-phishing/ | Yes (curl) | "85,000+ employees … since early 2017"; "We have had no reported or confirmed account takeovers since implementing security keys at Google" |
| `google-2019-account-hygiene.txt` | Google Security Blog, Kurt Thomas and Angelika Moscicki, "New research: How effective is basic account hygiene at preventing hijacking", 17 May 2019 | **Vendor blog post** summarising the WWW '19 paper | https://security.googleblog.com/2019/05/new-research-how-effective-is-basic.html | Yes (curl) | SMS 100/96/76%, on-device prompt 100/99/90% (bots/bulk phishing/targeted); "zero users that exclusively use security keys fell victim to targeted phishing during our investigation"; 38% of challenged users lacked their phone |
| `doerfler-2019-login-challenges.txt` (+ `doerfler2019.pdf`) | Doerfler, Thomas, Marincenko, Ranieri, Jiang, Moscicki, McCoy, "Evaluating Login Challenges as a Defense Against Account Takeover", WWW '19, doi 10.1145/3308558.3313481 | **Peer-reviewed paper** (Google + NYU + UCSD); the primary behind the blog post | https://damonmccoy.com/papers/loginchallenges.pdf (author copy; Google listing https://research.google/pubs/pub48119/) | Yes (curl) | Over 350,000 hijacking attempts; Table 3: Security Key 100% ± 25% (bots), 100% ± 28% (phishing), **no figure** for targeted attacks; "security keys offer the best immediate solution"; OTP apps "vulnerable to man-in-the-middle … something U2F security keys solve" |
| `lang-2016-security-keys.txt` (+ `fc16-lang.pdf`) | Lang, Czeskis, Balfanz, Schilder, Srinivas (Google), "Security Keys: Practical Cryptographic Second Factors for the Modern Web", FC 2016 | **Peer-reviewed paper**; the design and the internal-deployment record | https://fc16.ifca.ai/preproceedings/25_Lang.pdf | Yes (curl) | Abstract; OTPs "still vulnerable to … phishing"; deployed "within Google's internal sign-in system"; Chrome support "since version 41" |
| `webauthn-l3.txt` | W3C, "Web Authentication: An API for accessing Public Key Credentials – Level 3", W3C Recommendation | **Standard** | https://www.w3.org/TR/webauthn-3/ (editor's draft https://w3c.github.io/webauthn/ also fetched) | Yes (curl with curl's own UA; 403 to a browser UA and to WebFetch on `/webauthn-2/`) | Abstract ("strong, attested, scoped, public key-based credentials"); §1 "can only be accessed by origins belonging to that Relying Party. This scoping is enforced jointly by conforming User Agents and authenticators" |
| `uber-2022-security-update.txt` | Uber Newsroom, "Security update", 16 Sept 2022, updated 19 Sept | **Company post-incident statement** (required by CONTEXT §6 as the MFA-fatigue limit) | https://www.uber.com/newsroom/security-update/ | Yes (curl; 406 without an Accept header) | Contractor password "purchased … on the dark web"; "repeatedly tried to log in … Eventually, however, the contractor accepted one" |

## Secondary — retellings (folk story only; never the source for a ledger verdict)

| File | Document | URL | Fetched? | Carries |
|---|---|---|---|---|
| `wikipedia-colonial.txt` | Wikipedia, "Colonial Pipeline ransomware attack" (CC BY-SA) | https://en.wikipedia.org/wiki/Colonial_Pipeline_ransomware_attack | Yes | "compromised password for an inactive VPN account, which did not have multi-factor authentication"; "started from a breached employee personal password"; "recovered 63.7 of the bitcoins (about 84%)" |
| `cnn-2021-06-04.txt` | CNN, Fung and Sands, "Ransomware attackers used compromised password to access Colonial Pipeline network, company confirms", 4 June 2021 | https://edition.cnn.com/2021/06/04/politics/colonial-pipeline-ransomware-attack-password/index.html | Yes (quoted sentences only) | "using a compromised password"; "batch of leaked passwords found on the dark web, according to Bloomberg's interview with Carmakal"; "We don't see any evidence of phishing" |
| `bloomberg-2021-06-04.txt` | Bloomberg, Turton and Mehrotra, "Hackers Breached Colonial Pipeline Using Compromised Password", 4 June 2021 — the origin of the "one password" headline and of the Carmakal interview | https://www.bloomberg.com/news/articles/2021-06-04/hackers-breached-colonial-pipeline-using-compromised-password | **Partial** (2026-09-03): bloomberg.com 403 direct; the Wayback Machine 2021 snapshot returned the headline, byline, timestamp and the opening two paragraphs ("a single compromised password"; entry 29 April "through a virtual private network account"; "no longer in use at the time of the attack but could still be used"). The rest is paywalled in the snapshot, so the "batch of leaked passwords found on the dark web" sentence and the "no evidence of phishing" quotation remain cited through CNN |
| — | Krebs on Security, "A Closer Look at the DarkSide Ransomware Gang", 11 May 2021 | https://krebsonsecurity.com/2021/05/a-closer-look-at-the-darkside-ransomware-gang/ | Still 502 direct at drafting (2026-09-02); fetched from the Wayback Machine (web.archive.org/web/2024id_/…). Excerpt of the three sentences used: `krebs-2021-darkside.txt`. Retelling only |
| — | OWASP A07:2025 page | `resources/owasp/A07_*.txt` (fetched 2026-09-01 by the coordinating session) | Yes | "Has missing or ineffective multi-factor authentication"; prevention #1 "implement and enforce use of multi-factor authentication" |

## Not fetched / not available

- **The seizure-warrant affidavit** (N.D. Cal., June 2021) that the DOJ release cites — not
  linked from the release; not fetched. Pitch B's "how the FBI had the key" row would be OPEN.
- **TSA press release of 20 July 2021** (SD-02) — the page loads through the proxy but its
  body did not render; the Federal Register notice §I.B is used for what SD-02 required.
- **Original 2021 texts of SD Pipeline-2021-01 and -02** — SD-02 was Sensitive Security
  Information when issued; only the renewals (01E, 02E) are public. Any quotation of the
  MFA requirement is of the 2024 wording and must say so.
- **Mandiant's own written account** beyond Carmakal's House statement (no Mandiant blog
  post on Colonial exists that I could find); the Bloomberg interview is the only other
  first-person source and is paywalled.
- **A Google primary post for the 2018 "no account takeovers" statement** — none exists;
  it lives only in Krebs. The 2019 paper and blog are the published measurement.
- **Senate hearing video** — not needed; the GPO transcript is the record.

## Re-verification at drafting (2026-09-02)

Every .gov document obtained through the reader proxy at the pitch stage was tried once
more directly (curl with a browser UA, and WebFetch) and once through the Wayback Machine:

| Document | Direct | Wayback | Result |
|---|---|---|---|
| Blount written testimony (hsgac.senate.gov PDF) | 403 | 200, PDF | Confirmed; also printed in the govinfo Senate hearing PDF Appendix (direct fetch) |
| FBI statement 10 May 2021 | 403 (Cloudflare) | 200 (snapshot 2021-05-11) | Confirmed, identical two sentences |
| 86 FR 52953 (federalregister.gov) | 500 | 200 | Confirmed |
| GAO-21-105263 PDF | 403 | 200, PDF | Confirmed |
| TSA SD Pipeline-2021-02E PDF (tsa.gov) | 403 | 200, PDF | Confirmed; identical to the mirror copy. 2024 wording; the 2021 SD-02 is SSI |
| Krebs, "A Closer Look at the DarkSide Ransomware Gang" | 502 | 200 | Fetched; retelling only |

No claim in `checks/claims/07.tsv` rests on an unconfirmed proxy copy.

## Claims-register stage (2026-09-03)

- Bloomberg: one direct attempt (403 robot wall) and one Wayback fetch (200, opening only — see
  `bloomberg-2021-06-04.txt`). The headline and the "no longer in use ... but could still be used"
  sentence are now on disk; the dark-web sentence is still cited through CNN and the chapter says so.
- `senate-hearing-2021-06-08.txt` extended with three passages from the govinfo PDF (Peters/Blount
  on the $4.4 million, Hawley/Blount on the TSA review Colonial had scheduled for late July 2021,
  Ossoff/Blount on sharing the Mandiant review). The chapter's wording on the TSA review was
  corrected against them: the review was one Colonial had not yet taken up, not a pre-attack review.
