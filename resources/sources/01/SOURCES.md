# Sources — chapter 01 (A01 Broken Access Control — Capital One, 2019)

All fetched 2026-09-01. PDFs are kept locally but gitignored; the `.txt` files alongside are
the excerpts the chapter relies on. "Section used" is where the chapter's claims come from.

## Primary — court and regulator

| File | Document | What it is | URL | Section used |
|---|---|---|---|---|
| `complaint.txt` (+ `complaint-ocr-raw.txt`, `complaint.pdf`) | *United States v. Paige A. Thompson*, No. MJ19-0344, W.D. Wash., Complaint for violation of 18 U.S.C. § 1030(a)(2), Doc. 1, filed 2019-07-29, sworn 2019-07-27 | **Criminal complaint** — FBI SA Joel Martini's affidavit. Allegations, not findings. Scanned PDF, OCR'd with tesseract and hand-cleaned. | https://www.justice.gov/usao-wdwa/press-release/file/1188626/download | Count 1 (p. 1); ¶¶2, 8–15, 18, 20, 25–27 (pp. 2, 5–12) |
| `occ-consent-order.txt` (+ `occ-consent-order.pdf`) | OCC Consent Order #2020-036, *In the Matter of Capital One, N.A. and Capital One Bank (USA), N.A.*, AA-EC-20-51, signed 2020-08-05 | **Consent order** (civil money penalty). "The Bank neither admits nor denies." | https://www.occ.gov/static/enforcement-actions/ea2020-036.pdf | Art. II ¶¶1–5 (pp. 2–3); Art. III ¶1 (p. 3) |
| `occ-news-release.txt` | OCC News Release 2020-101, 2020-08-06 | Regulator press release announcing the order | https://www.occ.gov/news-issuances/news-releases/2020/nr-occ-2020-101.html | whole |
| `fed-release.txt` | Federal Reserve Board press release, 2020-08-06 | Regulator press release on the companion cease-and-desist against the holding company | https://www.federalreserve.gov/newsevents/pressreleases/enforcement20200806a.htm | whole (the C&D order itself not fetched) |
| `ca9-opinion.txt` (+ `ca9-opinion.pdf`) | *United States v. Thompson*, No. 22-30179 (9th Cir. 2025-03-17) | **Appellate opinion** (published). Recites the trial record; vacates the sentence. | https://cdn.ca9.uscourts.gov/datastore/opinions/2025/03/17/22-30179.pdf | Summary pp. 2–3; I.A–C pp. 5–11; pp. 13–14; dissent pp. 28–29 |
| `doj-arrest.txt` | USAO W.D. Wash. press release, 2019-07-29 | Government press release (arrest on complaint). "Only allegations." | https://www.justice.gov/usao-wdwa/pr/seattle-tech-worker-arrested-data-theft-involving-large-financial-services-company | whole |
| `doj-indict.txt` | USAO W.D. Wash. press release, 2019-08-28 | Government press release (indictment). "Only allegations." | https://www.justice.gov/usao-wdwa/pr/former-seattle-tech-worker-indicted-federal-charges-wire-fraud-and-computer-data-theft | whole |
| `doj-verdict.txt` | USAO W.D. Wash. press release, June 2022 | Government press release (jury verdict) | https://www.justice.gov/usao-wdwa/pr/former-seattle-tech-worker-convicted-wire-fraud-and-computer-intrusions | whole |
| `doj-sentence.txt` | USAO W.D. Wash. press release, 2022-10-04 | Government press release (sentencing) | https://www.justice.gov/usao-wdwa/pr/former-hacker-sentenced-stealing-computer-power-mine-cryptocurrency-and-stealing | whole |

justice.gov serves a bot-check redirect to non-browser clients; all four releases and the
complaint were fetched with curl by following that redirect. WebFetch alone returned 403.

## Primary — vendor and company

| File | Document | What it is | URL | Section used |
|---|---|---|---|---|
| `aws-imdsv2.txt` | AWS Security Blog, Colm MacCárthaigh, 2019-11-19, "Add defense in depth against open firewalls, reverse proxies, and SSRF vulnerabilities with enhancements to the EC2 Instance Metadata Service" | **Vendor announcement** of IMDSv2 — the defense record | https://aws.amazon.com/blogs/security/defense-in-depth-open-firewalls-reverse-proxies-ssrf-vulnerabilities-ec2-instance-metadata-service/ | whole article body |
| `capitalone-facts2019.txt` | Capital One, "Information on the Capital One cyber incident" | **Company statement** (updated through 2022) | https://www.capitalone.com/digital/facts2019/ | excerpted sentences |

## Secondary — retellings (folk story only; never the source for a ledger verdict)

| File | Document | URL |
|---|---|---|
| `krebs-2019-07.txt` | Krebs, "Capital One Data Theft Impacts 106M People", 2019-07-30 | https://krebsonsecurity.com/2019/07/capital-one-data-theft-impacts-106m-people/ |
| `krebs-2019-08.txt` | Krebs, "What We Can Learn from the Capital One Hack", 2019-08-02 | https://krebsonsecurity.com/2019/08/what-we-can-learn-from-the-capital-one-hack/ |
| `wikipedia-capital-one.txt` | Wikipedia, "Capital One" § July 2019 data breach (CC BY-SA) | https://en.wikipedia.org/wiki/Capital_One |
| `cyberscoop-2025.txt` | CyberScoop, "Court reimposes original sentence for Capital One hacker", 2025-11-05 | https://cyberscoop.com/court-reimposes-original-sentence-for-capital-one-hacker/ |

## Not fetched / not available

- The **indictment** and **superseding indictment** (2:19-cr-00159-RSL) — not fetched; the
  DOJ indictment release and the Ninth Circuit opinion are used instead. Claims that rest on
  indictment wording rest on the release.
- The **trial transcript and exhibits** — not public online. This is the document that would
  settle *how* the firewall was made to fetch the credentials (the SSRF step); the complaint
  does not say. Ledger row 1 is OPEN for this reason.
- The **Federal Reserve cease-and-desist order** text — only the press release fetched.
- The **district court's November 2025 resentencing order** — only CyberScoop's report
  fetched; the claim is marked `open`.
- The **OWASP** spine is in `resources/owasp/` (fetched 2026-09-01 by the coordinating
  session); A01 and the Introduction are quoted.
