# Chapter 09 source ledger

Fetch date for every entry: **2026-09-03**.

The pitch labels below refer to `drafts/09.pitches.md`: A is the Target alert-to-response
timeline; B is the Equifax inspection-certificate mirror; C is the M-Trends dwell-time
measurement; D tests how much of the Target story the Senate report itself establishes.

## Primary and first-party documents

### OWASP — A09:2025 Security Logging & Alerting Failures

- URL: https://owasp.org/Top10/2025/A09_2025-Security_Logging_and_Alerting_Failures/
- What it is: OWASP category page.
- Page or section used: Description; How to Prevent.
- Fetch extent: full; repository snapshot `resources/owasp/A09_2025-Security_Logging_and_Alerting_Failures.txt` was fetched 2026-09-01 and read in full on the date above.
- Pitches served: A, B, C, D.

### U.S. Senate Commerce Committee — *A “Kill Chain” Analysis of the 2013 Target Data Breach*

- URL: https://www.commerce.senate.gov/wp-content/uploads/media/doc/2014%200325%20Target%20Kill%20Chain%20Analysis.pdf
- What it is: government report (majority staff report for Chairman Rockefeller, 26 March 2014).
- Page or section used: Executive Summary pp. 1–2; “A. The Target Data Breach” pp. 2–6; “Analysis of the Target Data Breach Using the Kill Chain” pp. 8–13.
- Fetch extent: full, 18 pages, through the browser document reader; direct `curl` returned HTTP 403. The report is also reproduced in full in the GovInfo hearing record below.
- Pitches served: A, D.

### U.S. Senate Commerce Committee / GovInfo — hearing record, *Protecting Personal Consumer Information from Cyber Attacks and Data Breaches*

- URL: https://www.govinfo.gov/content/pkg/CHRG-113shrg92594/pdf/CHRG-113shrg92594.pdf
- What it is: government hearing record, S. Hrg. 113-576; it includes the Senate majority staff Target report.
- Page or section used: printed pp. 3–17, the included “Kill Chain” report.
- Fetch extent: full, 115 pages.
- Pitches served: A, D.

### John J. Mulligan / Target — written testimony to Senate Commerce Committee

- URL: https://www.commerce.senate.gov/services/files/C2103BD3-8C40-42C3-973B-BD08C7DE45EF
- What it is: company officer’s written congressional testimony (26 March 2014).
- Page or section used: pp. 1–4, especially the discovery timeline and pre-breach controls.
- Fetch extent: full through the browser document reader; direct `curl` returned HTTP 403.
- Pitches served: A, D.

### Target — “Updates on Target’s security and technology enhancements”

- URL: https://corporate.target.com/news-features/article/2014/04/updates-on-target-s-security-and-technology-enhanc
- What it is: vendor/company post-incident update (29 April 2014).
- Page or section used: “Enhancing monitoring and logging”; application whitelisting; segmentation; vendor access; accounts.
- Fetch extent: full HTML page.
- Pitches served: A, D.

### U.S. House Committee on Oversight and Government Reform — *The Equifax Data Breach*

- URL: https://oversight.house.gov/wp-content/uploads/2018/12/Equifax-Report.pdf
- What it is: government report (majority staff report, December 2018).
- Page or section used: Executive Summary pp. 1–5; “Anatomy of the Equifax Data Breach” pp. 26–53, especially “Expired SSL Certificates,” pp. 48–49.
- Fetch extent: full, 96 pages.
- Pitches served: B.

### U.S. Government Accountability Office — GAO-18-559, *Data Protection: Actions Taken by Equifax and Federal Agencies in Response to the 2017 Breach*

- URL: https://www.gao.gov/assets/gao-18-559.pdf
- What it is: government regulator/auditor report (August 2018).
- Page or section used: pp. 13–20, attack, discovery, contributing factors, and Equifax-reported remediation.
- Fetch extent: full, 40 pages.
- Pitches served: B.

### Federal Trade Commission — complaint, *FTC v. Equifax Inc.*

- URL: https://www.ftc.gov/system/files/documents/cases/172_3203_equifax_complaint_7-22-19.pdf
- What it is: government complaint (allegations, not findings), filed 22 July 2019.
- Page or section used: paragraphs 13–24, pp. 5–9.
- Fetch extent: full, 24 pages.
- Pitches served: B.

### Federal Trade Commission — stipulated order, *FTC v. Equifax Inc.*

- URL: https://www.ftc.gov/system/files/documents/cases/172_3203_equifax_order_signed_7-23-19.pdf
- What it is: stipulated consent order / permanent injunction, entered 23 July 2019.
- Page or section used: Section II, Mandated Information Security Program, pp. 14–20.
- Fetch extent: full, 74 pages.
- Pitches served: B.

### Mandiant — *M-Trends 2024* infographic

- URL: https://services.google.com/fh/files/misc/mtrends_2024_infographic.pdf
- What it is: vendor incident-response measurement / report infographic.
- Page or section used: “When Are Attackers Found?” and “How Are Attackers Found?”
- Fetch extent: full, one page.
- Pitches served: C; contextual defense record for A and B.

### Mandiant — *M-Trends 2024 Special Report: Executive Edition*

- URL: https://services.google.com/fh/files/misc/m-trends-2024-executive-edition.pdf
- What it is: vendor incident-response report.
- Page or section used: “By the Numbers—The Data of M-Trends,” p. 2.
- Fetch extent: full, six pages.
- Pitches served: C; contextual defense record for A and B.

### Mandiant — *M-Trends 2026 Report: Executive Edition*

- URL: https://services.google.com/fh/files/misc/m-trends-2026-executive-edition-en.pdf
- What it is: vendor incident-response report.
- Page or section used: Foreword pp. 2–3; “By the Numbers” pp. 3–4; “Multi-Year Intrusions Highlighting Extreme Persistence” pp. 7–8.
- Fetch extent: full, 12 pages.
- Pitches served: C.

## Retellings used only to establish folk claims

Only the sentences actually eligible for quotation will be saved from these sources.

### KrebsOnSecurity — “Target Hackers Broke in Via HVAC Company”

- URL: https://krebsonsecurity.com/2014/02/target-hackers-broke-in-via-hvac-company/
- What it is: press retelling (5 February 2014).
- Page or section used: headline and first two paragraphs.
- Fetch extent: partly; the quoted folk claim only.
- Pitches served: A.

### CBS News — “Did Target ignore data breach warnings?”

- URL: https://www.cbsnews.com/news/target-ignored-systems-hacking-warnings-report-says/
- What it is: press retelling of Bloomberg Businessweek’s reporting (13 March 2014).
- Page or section used: headline and passages quoting Businessweek editor Josh Tyrangiel.
- Fetch extent: partly through the browser document reader; direct `curl` returned HTTP 406.
- Pitches served: A, D.

### Wikipedia — “History of Target Corporation,” 2013 security breach subsection

- URL: https://en.wikipedia.org/wiki/History_of_Target_Corporation
- What it is: crowd-edited popular retelling.
- Page or section used: “2013 security breach.”
- Fetch extent: partly; the quoted folk claim only.
- Pitches served: D.

### Wikipedia — “2017 Equifax data breach,” Discovery subsection

- URL: https://en.wikipedia.org/wiki/2017_Equifax_data_breach
- What it is: crowd-edited popular retelling.
- Page or section used: “Discovery.”
- Fetch extent: partly; the quoted folk claim only.
- Pitches served: B.

### The Register — “Mandiant: Orgs are detecting cybercriminals faster than ever”

- URL: https://www.theregister.com/2024/04/23/mandiant_orgs_are_sniffing_out_cybercrims_faster_than_ever/
- What it is: press retelling (23 April 2024).
- Page or section used: headline, standfirst, and opening paragraphs.
- Fetch extent: partly; the quoted folk claim only.
- Pitches served: C.

## Not fetched / not available

- Bloomberg Businessweek, “Missed Alarms and 40 Million Stolen Credit Card Numbers: How Target Blew It” (13 March 2014), formerly at `http://www.businessweek.com/articles/2014-03-13/target-missed-alarms-in-epic-hack-of-credit-card-data`: a browser search did not return the article, and `curl -L` with a browser user agent redirected to the Bloomberg Businessweek landing page with HTTP 403. The Senate report cites it for the FireEye details, and CBS quotes its editor; no Bloomberg wording will be quoted unless a fetchable copy is later obtained.
- The standalone Senate-hosted Target report and Mulligan testimony rejected direct `curl` requests with HTTP 403. Both were readable through the browser document reader; the report is independently available inside the fully fetched GovInfo hearing PDF.
- CBS and Time pages rejected direct `curl` requests with HTTP 406. CBS was fetched partly through the browser document reader. The Time retelling was not selected and will not be quoted.
