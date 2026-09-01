# Chapter 10 — sources (A10:2025 Mishandling of Exceptional Conditions: Apple goto fail 2014; CrowdStrike Channel File 291, 2024)

All fetched 2026-09-01. PDFs are gitignored; plain-text excerpts sit beside this file.
"What it is" follows AGENT.md: a complaint alleges, a post-mortem admits, a commit shows.

## Primary — Apple, CVE-2014-1266

| File | Document | URL | What it is | Used |
|---|---|---|---|---|
| `apple-sslKeyExchange-55471.txt` | `libsecurity_ssl/lib/sslKeyExchange.c`, Apple open-source release Security-55471 (vulnerable) and Security-55471.14 (fixed, OS X 10.9.2) | https://raw.githubusercontent.com/apple-oss-distributions/Security/Security-55471/libsecurity_ssl/lib/sslKeyExchange.c and `.../Security-55471.14/...` | Apple's published source (Apple's own GitHub mirror of opensource.apple.com; the opensource.apple.com path 404s as of the fetch date) | function `SSLVerifySignedServerKeyExchange`, lines 575–652; unified diff between the two releases (one deleted line, 631) |
| `apple-security-notes.txt` | "About the security content of" iOS 6.1.6 (HT6146), iOS 7.0.6 (HT6147), OS X 10.9.2 (HT6150) | https://support.apple.com/en-us/HT6146 , HT6147 , HT6150 | Vendor security advisory | the Data Security entry (Impact / Description / CVE-ID), identical on all three |
| `cve-2014-1266.txt` | CVE-2014-1266 record | https://cveawg.mitre.org/api/cve/CVE-2014-1266 | CVE Program record (NVD page is JS-rendered; the JSON API was used) | description; datePublished 2014-02-22 |
| `imperialviolet-2014-02-22.txt` | Adam Langley, "Apple's SSL/TLS bug", 22 Feb 2014 | https://www.imperialviolet.org/2014/02/22/applebug.html | Personal blog post by the Chromium TLS engineer; first public analysis; the retelling everyone else copies | the code quotation, the mechanism paragraphs, the platform scope, the `-Wall` observation, the test-case and code-review paragraphs, the port-1266 test site |

## Primary — CrowdStrike, 19 July 2024

| File | Document | URL | What it is | Used |
|---|---|---|---|---|
| `crowdstrike-pir-2024-07-24.txt` | "Falcon Content Update Preliminary Post Incident Report" (Preliminary Post Incident Review), 24 July 2024 (updated 25 July) | https://www.crowdstrike.com/en-us/blog/falcon-content-update-preliminary-post-incident-report/ | Vendor post-mortem (admitted) | "What Happened?" through the prevention list: the 04:09–05:27 UTC window, sensor 7.11+, Sensor vs Rapid Response Content, the IPC Template Type timeline, the Content Validator bug, the out-of-bounds read |
| `crowdstrike-rca-2024-08-06.txt` | "External Technical Root Cause Analysis — Channel File 291", 6 Aug 2024, 12 pp. | https://www.crowdstrike.com/wp-content/uploads/2024/08/Channel-File-291-Incident-Root-Cause-Analysis-08.06.2024.pdf | Vendor root-cause analysis (admitted) | p.1 (~99% sensors online by 29 July); p.2 (21 fields defined, 20 supplied; wildcard; the 19 July non-wildcard instance; "confluence"); pp.3–6 (six findings and mitigations, dates); p.7 (kernel driver, early boot); p.9 (bugcheck text "This cannot be protected by try-except."); pp.10–12 (index 0x14, NULL check, invalid pointer) |
| `crowdstrike-kurtz-2024-07-19.txt` | George Kurtz, statement of 19 July 2024 (and 6 Aug 2024) on the Remediation and Guidance Hub | https://www.crowdstrike.com/en-us/blog/statement-on-falcon-content-update-for-windows-hosts/ | Vendor statement | "This was not a cyberattack"; "There is no impact to any protection if the Falcon sensor is installed" |
| `microsoft-weston-2024-07-20.txt` | David Weston, "Helping our customers through the CrowdStrike outage", 20 July 2024 | https://blogs.microsoft.com/blog/2024/07/20/helping-our-customers-through-the-crowdstrike-outage/ (Wayback copy; live page returns 403 to non-browser clients) | Vendor statement; the only published estimate of the host count | "We currently estimate that CrowdStrike's update affected 8.5 million Windows devices, or less than one percent of all Windows machines."; "this was not a Microsoft incident" |
| `microsoft-weston-2024-07-27.txt` | David Weston, "Windows Security best practices for integrating and managing security tools", 27 July 2024 | https://www.microsoft.com/en-us/security/blog/2024/07/27/windows-security-best-practices-for-integrating-and-managing-security-tools/ (Wayback copy; live page 403) | Vendor technical analysis (crash dumps) and design rationale | the NULL check before the read; "Why do security solutions leverage kernel drivers?"; "Kernel drivers provide the above properties at the cost of resilience."; "cannot fail and restart like a normal user application" |
| `delta-v-crowdstrike-complaint-2024-10-25.txt` | *Delta Air Lines, Inc. v. CrowdStrike, Inc.*, Complaint, Fulton County Superior Court, 24CV013621, filed 25 Oct 2024 | https://cdn.arstechnica.net/wp-content/uploads/2024/10/Delta-v-CrowdStrike-Complaint-10-25-24.pdf | **Complaint — allegations, not findings.** Used only for the "alleged" side of costs and for one folk claim (¶3) | caption and counts; ¶1–3; ¶48 (approx. 7,000 cancellations over five days; "at least $500 million"); prayer for relief |

## Secondary — retellings (folk story only; never a ledger record)

`retellings.txt` holds: the Wikipedia lede of "2024 CrowdStrike-related IT outages" and the "goto fail bug" section of "Unreachable code" (CC BY-SA); the sentences quoted from Dan Goodin, Ars Technica, 22 Feb 2014 ("a single line of misplaced code"); the sentences quoted from David A. Wheeler's essay "The Apple goto fail vulnerability: lessons learned" (2014, rev. 2021) — used as a retelling and for the gcc `-Wunreachable-code` observation, which he states as his own verified test; and two sentences from The Register, 21 May 2025, on the 16 May 2025 order in *Delta v. CrowdStrike* (press; the order itself was not fetched — the dependent claim is marked as press-sourced in the claims file).

## Not obtained

- Apple never published an account of how the duplicate line entered `sslKeyExchange.c`; the version history between iOS 5.1.1 and iOS 6 is not public. Ledger row 4 is OPEN for that reason.
- The 16 May 2025 order in *Delta v. CrowdStrike* (Fulton County) was not fetched; only The Register's report of it. Claim `10-delta-ruling` is checked against the press report and says so.
- The two independent third-party reviews CrowdStrike says it commissioned (RCA p.6): no published findings were found on the fetch date.
