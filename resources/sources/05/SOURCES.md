# Sources — chapter 05 (A05 Injection — MOVEit Transfer, 2023)

All fetched 2026-09-02 by the pitch agent (pitches only; no chapter drafted). PDFs are kept locally
and gitignored; the `.txt` files alongside are verbatim excerpts of the passages actually read.
"Pitch" says which candidate angle in `drafts/05.pitches.md` rests on the document. No exploit
material is copied anywhere in this directory; the product is still in service.

## Primary — vendor (Progress Software)

| File | Document | What it is | URL | Fetched? | Pitch |
|---|---|---|---|---|---|
| — (see note) | Progress, "MOVEit Transfer Critical Vulnerability (May 2023) (CVE-2023-34362)", Knowledge Base article, 2023-05-31, updated through June 2023 | **Vendor advisory** — the anchor document the CVE, KEV and every analyst post cite | https://community.progress.com/s/article/MOVEit-Transfer-Critical-Vulnerability-31May2023 | **No.** Salesforce Experience-Cloud page: curl, WebFetch, the Wayback snapshot (2023-06-30) and the r.jina.ai renderer all return the JavaScript shell with no article text; archive.today (archive.ph/58ty7) rate-limited (HTTP 429). Its opening sentence survives verbatim in the CVE record (`cve-nvd-kev-records.txt`) and in Rapid7's quotation of it (`rapid7-2023-06-01.txt`); its timeline survives in Progress's own security page (next row). **A human should open it in a browser and save the text before drafting.** | A, D |
| — | Progress, "MOVEit Transfer Critical Vulnerability (CVE-2023-35036) June 9, 2023" | Vendor advisory, second SQLi | https://community.progress.com/s/article/MOVEit-Transfer-Critical-Vulnerability-CVE-2023-35036-June-9-2023 | **No** (same shell) | A, D |
| — | Progress, "MOVEit Transfer Critical Vulnerability (June 15, 2023)" (CVE-2023-35708) | Vendor advisory, third SQLi | https://community.progress.com/s/article/MOVEit-Transfer-Critical-Vulnerability-15June2023 | **No** (same shell) | A, D |
| `progress-security-page-2023-08-02-wayback.txt` (+ raw HTML in scratchpad only) | Progress, "MOVEit Transfer and MOVEit Cloud Vulnerability", www.progress.com/security/…, Wayback snapshot 2023-08-02 | **Vendor running update log**: 31 May ("all within 48 hours"), 9 June (third-party code review; "cybersecurity firm Huntress has helped us to uncover additional vulnerabilities"), 15–18 June (third CVE "publicly posted online"), 5 July (Service Pack programme, "fixes for three new CVEs") | http://web.archive.org/web/20230802220348/https://www.progress.com/security/moveit-transfer-and-moveit-cloud-vulnerability (live URL now 301s to trust.progress.com, a Conveyor trust portal with no timeline) | Yes | A, C, D |
| `progress-8k-2023-06-05.txt` | Progress Software Corp., Form 8-K, Item 8.01, filed 2023-06-05 | **SEC filing** — the vendor's first sworn account: support call evening of 28 May, zero-day found, customers contacted and MOVEit Cloud taken down 30 May, patch 31 May; MOVEit <4% of revenue | https://www.sec.gov/Archives/edgar/data/876167/000087616723000113/prgs-20230530.htm | Yes | A, C, D |
| `progress-10q-2023-10-10.txt` | Progress, Form 10-Q for quarter ended 2023-08-31, filed 2023-10-10 | **SEC filing** — no telemetry into on-prem installs; 23 customer letters; 58 class actions; SEC subpoena 2 Oct 2023; $1.0M cost net of $1.9M insurance; $15M cyber policy; "third-parties have been actively scrutinizing… leading to the discovery and our prompt patching of additional vulnerabilities" | https://www.sec.gov/Archives/edgar/data/876167/000087616723000190/prgs-20230831.htm | Yes | C, D |
| `progress-10k-2024-01-26.txt` | Progress, Form 10-K for FY ended 2023-11-30, filed 2024-01-26 | **SEC filing** — 31 customer letters; ~118 class actions; three formal government investigations (federal law enforcement, SEC, D.C. Attorney General); FY2023 MOVEit cost $1.5M net of $3.7M recoveries | https://www.sec.gov/Archives/edgar/data/876167/000087616724000031/prgs-20231130.htm | Yes | C |
| `progress-8k-2024-08-07.txt` | Progress, Form 8-K Ex. 99.1, press release, 2024-08-07 | **SEC filing** — SEC Division of Enforcement "does not intend to recommend an enforcement action" | https://www.sec.gov/Archives/edgar/data/876167/000087616724000138/pressrelease-sec.htm | Yes | C |
| `cve-nvd-kev-records.txt` | CVE-2023-34362 / -35036 / -35708 records (CVE.org JSON), NVD record for -34362 (CVSS 9.8, CWE-89, references), CISA KEV entry (added 2023-06-02, due 2023-06-23, "Known" ransomware use) | **CVE / NVD / KEV records** — the description text is the advisory's text (NVD tags the advisory "Vendor Advisory") | https://nvd.nist.gov/vuln/detail/CVE-2023-34362 (HTML page returned only the NVD shell; the 2.0 API was used); https://cveawg.mitre.org/api/cve/CVE-2023-34362; https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json | Yes (APIs) | A, D |

## Primary — regulators and courts

| File | Document | What it is | URL | Fetched? | Pitch |
|---|---|---|---|---|---|
| `cisa-fbi-aa23-158a.txt` | CISA/FBI joint CSA AA23-158A, "#StopRansomware: CL0P Ransomware Gang Exploits CVE-2023-34362 MOVEit Vulnerability", 2023-06-07, updated 2023-06-16 | **Regulator advisory** — "Beginning on May 27, 2023"; LEMURLOOT / human2.aspx; "Health Check Service" admin account; names only CVE-2023-34362; no victim count | https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-158a | **Partly.** cisa.gov returns 403 to curl (HTML and PDF); WebFetch returned quoted sentences, saved with a caveat. Re-fetch in a browser before quoting in a ledger row. | A, D |
| `cisa-fbi-secure-by-design-sqli-2024-03.txt` (+ `.pdf`) | CISA/FBI, "Secure by Design Alert: Eliminating SQL Injection Vulnerabilities in Software", TLP:CLEAR, March 2024 | **Regulator alert, full text** — issued "in response to a recent well-publicized… campaign that exploited SQLi defects in a managed file transfer application… impacting thousands of organizations"; MySQL prepared statements 2004; "'unforgivable' vulnerability since at least 2007"; "A simple code review would reveal the prevalence"; input sanitisation "brittle" | https://www.cisa.gov/sites/default/files/2024-03/SbD%20Alert%20-%20Eliminating%20SQL%20Injection%20Vulnerabilities%20in%20Software_508c.pdf (landing page: https://www.cisa.gov/resources-tools/resources/secure-design-alert-eliminating-sql-injection-vulnerabilities-software) | Yes (PDF via WebFetch; text by pdftotext) | A, D |
| `jpml-transfer-order-2023-10-04.txt` (+ `.pdf`) | JPML, *In re: MOVEit Customer Data Security Breach Litigation*, MDL No. 3083, Transfer Order, Doc. 312, 2023-10-04 | **Court order** — 91 related actions in 22 districts; "estimated to have compromised the PII of over 55 million people"; centralised in D. Mass. before Judge Burroughs; lists which defendants (PBI, Genworth, Maximus, TIAA…) supported or opposed | https://www.jpml.uscourts.gov/sites/jpml/files/MDL-3083-Transfer_Order-9-23.pdf | Yes | B, C |
| `mdl-order-22-2025-07-31.txt` (+ `.pdf`) | D. Mass., No. 1:23-md-03083-ADB, MDL Order No. 22 (Progress motion to dismiss, Rule 12(b)(6)), ECF 1516, 2025-07-31 | **Court order** — recites the *allegations* (three vulnerabilities: SQLi, BinaryFormatter deserialisation, unencrypted keys; Cl0p named >2,600 entities / >93M records as of Jan 2024); holds "the allegation of a persistent SQL injection vulnerability… clears that hurdle at the pleading stage"; Ch. 93A count survives. Allegations, not findings. | https://www.cohenmilstein.com/wp-content/uploads/2024/05/Order-22-MOVEit-MTD-Progress-Software-July-31-2025.pdf (law-firm mirror of the ECF document) | Yes | C |
| `mdl-order-19-2024-12-12.txt` (+ `.pdf`) | MDL Order No. 19 (Article III standing), ECF 1304, 2024-12-12 | Court order — opening only excerpted | https://www.mad.uscourts.gov/caseinfo/pdf/mdl/3083/Order%2019.pdf | Yes | C |
| `mdl-order-27-2025.txt` (+ `.pdf`) | MDL Order No. 27 (Progress's motion for partial reconsideration of Order 22 — DENIED) | Court order — opening only excerpted | https://www.mad.uscourts.gov/caseinfo/pdf/mdl/3083/Order%2027.pdf | Yes | C |

## Primary — affected companies (SEC filings; two of ~30 found by EDGAR full-text search for "MOVEit")

| File | Document | What it is | URL | Fetched? | Pitch |
|---|---|---|---|---|---|
| `maximus-8k-2023-07-26.txt` | Maximus, Inc., Form 8-K Item 8.01, 2023-07-26 | Direct MOVEit customer: "at least 8 to 11 million individuals"; ~$15M expense | https://www.sec.gov/Archives/edgar/data/1032220/000103222023000061/mms-20230726.htm | Yes | B |
| `genworth-8k-2023-06-22.txt` | Genworth Financial, Form 8-K Item 8.01, 2023-06-22 | Indirect victim via vendor PBI: "approximately 2.5-2.7 million policyholders"; "the Company does not itself use the MOVEit file transfer system" | https://www.sec.gov/Archives/edgar/data/1276520/000119312523172549/d463993d8k.htm | Yes | B |

EDGAR full-text search (`efts.sec.gov/LATEST/search-index?q="MOVEit"&forms=8-K,10-Q,10-K`, 2023-06-01 → 2024-12-31) returned 151 hits; the list is in the scratchpad, not saved here.

## Technical write-ups (vendor-adjacent; used for mechanism, not for verdicts)

| File | Document | What it is | URL | Fetched? | Pitch |
|---|---|---|---|---|---|
| `mandiant-2023-06-02.txt` | Mandiant, "Zero-Day Vulnerability in MOVEit Transfer Exploited for Data Theft", 2023-06-02, upd. 06-09 | IR vendor: earliest exploitation 27 May; "data theft… within minutes"; "seemingly opportunistic"; UNC4857 → FIN11; LEMURLOOT description | https://cloud.google.com/blog/topics/threat-intelligence/zero-day-moveit-data-theft | Yes | A, D |
| `huntress-2023-06-01.txt` | Huntress, "MOVEit Transfer Critical Vulnerability Rapid Response", 2023-06-01, upd. through 06-12 | MDR vendor: "less than ten organizations" in its base vs "over 2,500 servers" on Shodan; chain recreated 5 June; its code review produced CVE-2023-35036 | https://www.huntress.com/blog/moveit-transfer-critical-vulnerability-rapid-response | Yes | A, D |
| `rapid7-2023-06-01.txt` | Rapid7, "Observed Exploitation of MOVEit Transfer Vulnerability CVE-2023-34362", 2023-06-01, upd. through 08-10 | Quotes the Progress advisory; ~2,500 exposed instances as of 31 May; IoCs from 27 May; "opportunistic rather than highly targeted"; July update: three more CVEs (36934/36932/36933) | https://www.rapid7.com/blog/post/2023/06/01/rapid7-observed-exploitation-of-critical-moveit-transfer-vulnerability/ | Yes | A, D |
| `rapid7-analysis-cve-2023-34362.txt` | Rapid7 / AttackerKB, "CVE-2023-34362 — Rapid7 Analysis" | **Patch diff** — the closest thing to a commit: `UserGetUsersWithEmailAddress()` rebuilt from string concatenation to `SQLBasicBuilder` with bound parameters; `SetAllSessionVarsFromHeaders()` removed; "naive injection attempts fail — in every case the application correctly escapes the arguments"; SQLi alone suffices for data theft, deserialisation needed for RCE. **Excerpt omits every payload.** | https://attackerkb.com/topics/mXmV0YpC3W/cve-2023-34362/rapid7-analysis → https://www.rapid7.com/blog/post/ra-cve-2023-34362-analysis/ | Yes | A (anchor), D |
| `rapid7-timeline-2023-06-14.txt` | Rapid7, "CVE-2023-34362: MOVEit Vulnerability Timeline of Events", 2023-06-14 | Day-by-day timeline 27 May – 15 June | https://www.rapid7.com/blog/post/2023/06/14/etr-cve-2023-34362-moveit-vulnerability-timeline-of-events/ | Yes | A, D |

## Victim tallies (secondary compilations; each states its own method — quote the method with the number)

| File | Document | What it is | URL | Fetched? | Pitch |
|---|---|---|---|---|---|
| `emsisoft-tally.txt` | Emsisoft, "Unpacking the MOVEit Breach: Statistics and Analysis", 2023-07-18, tally "current as of June 28th, 2024" | 2,773 organisations / 95,788,491 individuals; 78.9% US; education 39.1%; "$165 per record" → $15.8bn; admits overlap it "cannot account for"; upstream/downstream note | https://www.emsisoft.com/en/blog/44123/unpacking-the-moveit-breach-statistics-and-analysis/ | Yes | B |
| `konbriefing-tally.txt` | KonBriefing Research, "MOVEit hack victim list", last updated 2023-12-20 | 2,611 organisations / 85.1–89.9m; method note: "strictly speaking, the sum is not the total number of people affected, but the total number of people records affected" | https://konbriefing.com/en-topics/cyber-attacks-moveit-victim-list.html (the plural "…victims-list.html" in the brief returns HTTP 300) | Yes | B |

## Secondary — retellings (folk story only; never the source for a verdict)

| File | Document | Carries | URL | Fetched? |
|---|---|---|---|---|
| `techcrunch-2023-08-25.txt` | TechCrunch, Carly Page, "MOVEit, the biggest hack of the year, by the numbers", 2023-08-25 | "more than 1,000 known victims… 60 million"; "zero-day… allowed… Clop… to raid MOVEit Transfer servers" | https://techcrunch.com/2023/08/25/moveit-mass-hack-by-the-numbers/ | Yes |
| `techtarget-2023-09-26.txt` | TechTarget, "Clop MoveIt Transfer attacks affect over 2,000 organizations", 2023-09-26 | "2,095 organizations and 62,054,613 individuals"; Callow: "1,690 of the 2,098… compromised via third parties" | https://www.techtarget.com/searchsecurity/news/366553304/Clop-MoveIt-Transfer-attacks-affect-over-2000-organizations | Yes |
| `wikipedia-2023-moveit-data-breach.txt` | Wikipedia, "2023 MOVEit data breach" (lede) | "over 2,700 organizations… approximately 93.3 million individuals"; "zero-day… via SQL injection" | https://en.wikipedia.org/wiki/2023_MOVEit_data_breach | Yes |

## Reference — the category and the weakness

| File | Document | URL | Fetched? |
|---|---|---|---|
| `../../owasp/A05_*.txt` | OWASP Top 10:2025 A05 Injection (fetched 2026-09-01 by the coordinating session; quote-gated) | — | (already in repo) |
| `cwe-89.txt` | MITRE CWE-89 — description, mitigations ("Process SQL queries using prepared statements, parameterized queries, or stored procedures"), likelihood High | https://cwe.mitre.org/data/definitions/89.html | Yes |
| `owasp-sqli-prevention-cheat-sheet.txt` | OWASP SQL Injection Prevention Cheat Sheet — "the database will always distinguish between code and data, regardless of what user input is supplied" | https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html | Yes |

## Not fetched / not available

- The **three Progress Knowledge Base advisories** (above): text not retrievable by any non-browser route tried. Highest-priority manual fetch before drafting.
- **AA23-158A raw text** — 403 to curl; only WebFetch-mediated quotes on disk.
- **HHS HC3 sector alert** (hhs.gov/…/moveit-transfer-software-sector-alert.pdf) — 403.
- The **Bellwether Consolidated Class Action Amended Complaint** (ECF 1332) — not fetched; its allegations are known only as recited in Order 22.
- **Progress's 10-Q of 2023-07-07** and later 10-Qs (2024-04, 2024-07, 2024-10) — fetched to scratchpad but not excerpted; the Oct-2023 10-Q and the 10-K carry the same paragraphs with updated counts. Useful if a pitch needs the count series (58 → ~118 class actions).
- **Cl0p leak-site post of 2023-06-06** — known only through Mandiant, Emsisoft and Rapid7's descriptions; no primary copy.
- **A Wired or Krebs retelling** — searches turned up none dedicated to MOVEit; TechCrunch, TechTarget and Wikipedia carry the folk numbers instead.
- **ZDI advisory for CVE-2023-36934** (July 2023, a fourth critical SQLi) — found by search, not fetched; relevant to pitch D's "how many were there" question.
