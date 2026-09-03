# Sources — chapter 08 (A08 Software or Data Integrity Failures — NotPetya; Maersk)

Fetched 2026-09-03 for the pitch stage; no chapter has been drafted. “Full” means the
whole HTML page or PDF was fetched and inspected, not that the excerpt file reproduces
the whole work. The indictment records allegations, not findings. NotPetya and Maersk's
enterprise network are outside the web-application scope from which the OWASP Top 10 is
drawn; A08 is being used as a lens on trust in an update mechanism.

The thinnest part of the chapter contract is the famous Ghana recovery. Wired reports it
from interviews with unnamed Maersk staff, but the Maersk publications fetched here do not
name Ghana. Gavin Ashton's first-person account confirms a forest-wide domain-controller
loss and restoration of the first controller, but not the location or blackout. The chapter
must preserve that source boundary.

## Spine and attack record

| File | Document / URL | What it is | Page or section used; fetch extent | Pitches |
|---|---|---|---|---|
| `owasp-a08.txt` | OWASP, “A08:2025 Software or Data Integrity Failures” — https://owasp.org/Top10/2025/A08_2025-Software_or_Data_Integrity_Failures/ | **OWASP category page** (CC BY-SA 4.0); repository snapshot is `resources/owasp/A08_2025-Software_or_Data_Integrity_Failures.txt` | Description; How to prevent; Scenario #2. **Full** local snapshot | A, B, C, D |
| `doj-indictment.txt` | *United States v. Andrienko et al.*, No. 2:20-cr-00316-DWA (W.D. Pa.), indictment filed 15 Oct. 2020, unsealed 19 Oct. 2020 — https://www.justice.gov/archives/opa/press-release/file/1328521/dl?inline= | **Indictment**; allegations, not adjudicated facts | ¶¶33–38, PDF pp.16–19: ransomware ruse; M.E.Doc update server; three modified update files; June 27 delivery. **Full** 50-page PDF fetched by curl | A, B, D |
| `cisco-medoc.txt` | Cisco Talos, “The MeDoc Connection,” 5 July 2017 — https://blog.talosintelligence.com/the-medoc-connection/ | **Vendor incident-response report / post-mortem** based on Cisco's access to M.E.Doc engineers, logs and code | Summary; Details; ZvitPublishedObjects.dll Backdoor Analysis; What Now? **Full** HTML fetched | A, B, D |
| `eset-telebots.txt` | Anton Cherepanov, ESET Research, “TeleBots are back: Supply-chain attacks against Ukraine,” 30 June 2017 — https://www.welivesecurity.com/2017/06/30/telebots-back-supply-chain-attacks-against-ukraine/ | **Vendor research report** | Diskcoder.C outbreak; Initial infection vector; Conclusions. **Full** HTML fetched | B, D |
| `microsoft-petya.txt` | Microsoft Defender Security Research Team, “New ransomware, old techniques: Petya adds worm capabilities,” 27 June 2017 — https://www.microsoft.com/en-us/security/blog/2017/06/27/new-ransomware-old-techniques-petya-adds-worm-capabilities/ | **Vendor research report** based on Microsoft telemetry | Delivery and installation; lateral movement. **Full** HTML fetched | B, D |
| `ukraine-cyberpolice.txt` | Cyber Police of Ukraine, “The Petya virus (Diskcoder.C) was used as a cover for the largest cyberattack in Ukraine's history,” 5 July 2017 — https://cyberpolice.gov.ua/news/prykryttyam-najmasshtabnishoyi-kiberataky-v-istoriyi-ukrayiny-stav-virus-diskcoderc-881/ | **Regulator / law-enforcement report** in Ukrainian; excerpt includes a clearly labelled working translation | Findings announced after the investigation began: M.E.Doc update, source-code access, backdoor, destructive cover. **Full** HTML fetched | B, D |

## Maersk and the defense record

| File | Document / URL | What it is | Page or section used; fetch extent | Pitches |
|---|---|---|---|---|
| `maersk-q2-2017.txt` | A.P. Moller–Maersk, *Key Statements Q2 2017*, 16 Aug. 2017 — https://investor.maersk.com/static-files/0ed2b2c8-518c-48ce-b009-c7b06308ad71 | **Company report / investor presentation** | PDF p.4 (slide printed “Interim report Q2 2017 — Page 5”), Cyber-Attack: entry through Ukrainian tax-filing software; manual workarounds; vessel control; then-estimated cost. **Full** 33-page PDF fetched by curl | A, C |
| `maersk-annual-2017.txt` | A.P. Moller–Maersk, *Annual Report 2017* — https://investor.maersk.com/system/files-encrypted/nasdaq_kms/assets/2018/04/25/13-00-21/A.P._Moller_-_Maersk_Annual_Report_2017.pdf | **Company annual report** | Printed pp.29 and 54 (PDF pp.28 and 53): approximately USD 250–300m; what that range covers; recovery and continuity initiatives. **Full** 151-page PDF fetched by curl | A, C, D |
| `maersk-ten-days.txt` | Maersk, *A View from the Other Side of a Crisis: The Maersk China case to mitigate the world's largest supply chain disruptor – COVID-19* — https://www.maersk.com/~/media_sc9/maersk/stay-ahead/maersk---a-view-from-the-other-side-of-a-crisis---final.pdf | **Company white paper** with a boxed NotPetya retrospective | PDF p.4, “What we learned from the NotPetya Virus cyber-attack”: network rebuilt in ten days while cargo kept moving. **Full** 11-page PDF fetched through the browser reader; direct curl timed out | A, C |
| `gavin-ashton.txt` | Gavin Ashton, “Maersk, me & NotPetya,” 21 June 2020 — https://gvnshtn.com/p/maersk-me-and-notpetya | **First-person post** by Maersk's former Identity and Access Management service owner; not an official Maersk post-mortem | notPetya; A bitter pill; Finding our feet: fleet-wide domain-controller loss, recovery planning gap, first restored DC, and controls added afterward. **Full** HTML fetched | A, C |
| `microsoft-ad-recovery.txt` | Microsoft Learn, “Active Directory Forest Recovery — Determine how to recover the forest,” updated 10 July 2023 — https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-determine-how-to-recover | **Vendor recovery documentation** | Opening; Determine which backups to use; Determine which domain controllers to restore; Recover the forest in isolation. **Full** HTML fetched | A, C |
| `ncsc-ransomware-backups.txt` | UK National Cyber Security Centre, “Mitigating malware and ransomware attacks,” version 3.0, published 13 Feb. 2020, reviewed 9 Sept. 2021 — https://www.ncsc.gov.uk/guidance/mitigating-malware-and-ransomware-attacks | **Government guidance** | What are malware and ransomware?; Action 1; Action 4: offline, separate and tested backups; planning for unusable onsite and cloud backup servers. **Full** HTML fetched | A, C, D |

## Retellings — folk claims only

These sources identify claims to test; they do not establish the incident-side ledger
verdicts. Press excerpts contain only the sentences proposed for quotation.

| File | Document / URL | What it is | Page or section used; fetch extent | Pitches |
|---|---|---|---|---|
| `wired-notpetya.txt` | Andy Greenberg, “The Untold Story of NotPetya, the Most Devastating Cyberattack in History,” *Wired*, 22 Aug. 2018; accessible syndication — https://www.issp.ca/wired-the-untold-story-of-notpetya | **Press retelling / oral history** | Maersk recovery: “decentralized backup strategy,” lone Ghana controller, blackout. **Full** syndication page fetched; saved excerpt is only the folk-claim sentences | A |
| `bleepingcomputer-medoc.txt` | Catalin Cimpanu, “Ukrainian Police Seize Servers From Where NotPetya Outbreak First Spread,” *BleepingComputer*, 4 July 2017, updated 5 July — https://www.bleepingcomputer.com/news/security/ukrainian-police-seize-servers-from-where-notpetya-outbreak-first-spread/ | **Press retelling** | “M.E.Doc update servers were responsible” and “didn't use HTTPS or cryptographically-signed binaries.” **Full** HTML fetched; saved excerpt is only the folk-claim sentences | B |
| `darknet-diaries-54.txt` | Jack Rhysider with Andy Greenberg, “NotPetya,” *Darknet Diaries* episode 54 transcript, 24 Dec. 2019 — https://darknetdiaries.com/transcript/54/ | **Popular explainer / interview transcript** | Transcript lines on the Ghana controller, a functioning network after “about nine days,” and “350 million dollars.” **Full** transcript fetched; saved excerpt is only the folk-claim sentences | C |
| `bbc-notpetya.txt` | “UK and US blame Russia for ‘malicious’ NotPetya cyber-attack,” *BBC News*, 15 Feb. 2018 — https://www.bbc.com/news/uk-politics-43062113 | **Press retelling** | Opening description: “NotPetya ransomware attack.” **Full** HTML fetched by curl after the feed URL returned 404; saved excerpt is only the folk-claim sentence | D |
| `wikipedia-petya.txt` | Wikipedia, “Petya (malware family)” — https://en.wikipedia.org/wiki/Petya_(malware_family) | **Retelling / encyclopedia article** (CC BY-SA) | 2017 cyberattack; Operation; Impact: update mechanism, reversible-encryption caveat, cost superlative. **Full** HTML fetched; saved excerpt is only the folk-claim sentences used | B, D |

## Not fetched / not available

- Maersk's September 2017 employee magazine article “When the screens went black” was
  located at https://www.maersk.com/~/media_sc9/maersk/corporate/press/publications/files/2017-september-maersk-post-full-issue.pdf . The Maersk CDN returned no bytes before two
  curl timeouts and the browser reader returned an internal error. Search indexing exposed
  only part of the article, so it is not quoted and has no excerpt file.
- The CISA *#StopRansomware Guide* page and PDF were tried at
  https://www.cisa.gov/stopransomware/ransomware-guide and
  https://www.cisa.gov/sites/default/files/2023-10/StopRansomware-Guide-508C-v3_1.pdf .
  Both returned 403 outside the search index. NCSC's fully fetched guidance supplies the
  offline-backup defense instead.
- No fetched Maersk document confirms that the surviving controller was in Ghana, that a
  blackout isolated it, or that its disk travelled through Nigeria. Those details remain
  attributable to Wired's interviews. Ashton confirms the domain-controller recovery but
  does not repeat the Ghana story.
- No primary document fetched here states whether M.E.Doc update binaries were or were not
  cryptographically signed. The absence of HTTPS and signed binaries is a
  BleepingComputer claim; until a M.E.Doc specification, binary, or forensic report settles
  it, the signing state is OPEN.
- M.E.Doc / Intellect Service's contemporary forum posts and denials linked by the press
  did not yield a usable first-party statement. The live notice at
  https://www.me-doc.com.ua/1111193340-budte-bditelny-virusnaya-ataka-na-korporativnyy-sektor,
  the Facebook post at https://www.facebook.com/medoc.ua/posts/1904044929883085, and the
  Cyber Police page's archived denial at
  https://web.archive.org/web/20170628185144/http%3A//www.me-doc.com.ua/1111193342 were
  each tried through the source page and returned cache misses.
