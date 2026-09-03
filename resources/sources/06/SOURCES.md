# Chapter 06 sources

Fetch date for every item below: **2026-09-03**. Pitch letters are provisional until
`drafts/06.pitches.md` is written. “Full” describes what was fetched for inspection; the
adjacent `.txt` files retain only the relevant passages, not a second complete copy.

## Primary and technical record

### OWASP Top 10:2025 — A06 Insecure Design

- URL: https://owasp.org/Top10/2025/A06_2025-Insecure_Design/
- What it is: OWASP category page (the book’s spine; CC BY-SA 4.0).
- Page or section used: “Description,” “Secure Design,” and “How to prevent.”
- Fetch extent: full, from the repository’s authoritative 2025 snapshot at
  `resources/owasp/A06_2025-Insecure_Design.txt` (the snapshot was originally captured
  2026-09-01 and was re-read in full on the fetch date above).
- Serves: A, B, C, D.
- Saved excerpt: `owasp-a06.txt`.

### Drew Robb / Strava Engineering — “Building the Global Heatmap”

- URL: https://medium.com/strava-engineering/the-global-heatmap-now-6x-hotter-23fc01d301de
- What it is: vendor engineering post describing the November 2017 heatmap’s design and
  implementation.
- Page or section used: opening; “Input Data and Filtering”; “Heat Rasterization”; “Heat
  Normalization.”
- Fetch extent: full page fetched through the text browser; direct `curl` returned HTTP
  403. The excerpt preserves the parts used.
- Serves: A, B, C, D.
- Saved excerpt: `strava-building-heatmap.txt`.

### James Quarles / Strava — “A Letter to the Strava Community”

- Original URL: https://blog.strava.com/press/a-letter-to-the-strava-community/
- Fetched archive URL: https://arquivo.pt/wayback/20200219080522id_/https://blog.strava.com/press/a-letter-to-the-strava-community/
- What it is: vendor incident response dated 2018-01-29.
- Page or section used: full letter, especially the description of privacy selections,
  the acknowledgement of sensitive-location awareness, and the four response actions.
- Fetch extent: full archived page fetched from Arquivo.pt and converted to plain text.
- Serves: A, C, D.
- Saved excerpt: `strava-letter.txt`.

### Strava — “Heatmap Updates”

- Original URL: https://blog.strava.com/press/heatmap-updates/
- Fetched archive URL: https://arquivo.pt/wayback/20180719020035id_/https://blog.strava.com/press/heatmap-updates/
- What it is: vendor follow-up / change announcement dated 2018-03-13.
- Page or section used: full post; monthly privacy refresh, low-activity threshold,
  street-detail login, opt-out, private-activity, and Privacy Zone statements.
- Fetch extent: full archived page fetched from Arquivo.pt and converted to plain text.
- Serves: A, B, C.
- Saved excerpt: `strava-heatmap-updates.txt`.

### Senators Chris Coons and Jeff Flake — letter to Strava CEO James Quarles

- URL: https://www.coons.senate.gov/news/press-releases/sens-coons-flake-press-strava-ceo-on-privacy-data-security-failures-after-fitness-tracking-app-reveals-sensitive-information-of-us-military-service-members
- What it is: government correspondence dated 2018-02-14, reproduced in full on a Senate
  office site; its characterizations are the senators’ statements and questions, not
  adjudicated findings.
- Page or section used: paragraphs describing the heatmap and cross-referencing; quotation
  from Strava’s response; list of Strava action items; questions 1–5.
- Fetch extent: full webpage.
- Serves: A, C.
- Saved excerpt: `coons-flake-letter.txt`.

### U.S. Government Accountability Office — GAO-17-668, *Internet of Things: Enhanced Assessments and Guidance Are Needed to Address Security Risks in DOD*

- URL: https://www.gao.gov/assets/gao-17-668.pdf
- Landing page: https://www.gao.gov/products/gao-17-668
- What it is: government report, published 2017-07-27.
- Page or section used: report pp. 13–18 (design, aggregation, and threat-analysis record),
  pp. 29–31 (conclusions, recommendations, and DOD concurrence).
- Fetch extent: full 46-page PDF fetched and text-extracted by the browser.
- Serves: A, C, D.
- Saved excerpt: `gao-17-668.txt`.

### U.S. Department of Defense — “Use of Geolocation-Capable Devices, Applications, and Services”

- URL: https://media.defense.gov/2018/Aug/06/2001951064/-1/-1/1/GEOLOCATION-DEVICES-APPLICATIONS-SERVICES.PDF
- What it is: two-page policy memorandum from the Deputy Secretary of Defense, dated
  2018-08-03.
- Page or section used: pp. 1–2, in full.
- Fetch extent: full PDF fetched and text-extracted through the browser; direct `curl`
  returned HTTP 403.
- Serves: A, C, D.
- Saved excerpt: `dod-geolocation-memo.txt`.

### Hassan et al. — “Fitness Trackers: Fit for Health but Unfit for Security and Privacy”

- URL: https://www.usenix.org/system/files/conference/usenixsecurity18/sec18-hassan_0.pdf
- What it is: peer-reviewed paper, 27th USENIX Security Symposium (2018).
- Page or section used: proceedings pp. 507–510, especially §§7.1, 7.3, and 9 (“Ethics
  and Disclosure”).
- Fetch extent: full 17-page PDF fetched and text-extracted.
- Serves: B, C.
- Saved excerpt: `hassan-fitness-trackers.txt`.

## Retellings used only to identify folk claims

Only the sentence or title that may be quoted in a pitch is retained from each retelling.

### *The Guardian* — “Fitness tracking app Strava gives away location of secret US army bases”

- URL: https://www.theguardian.com/world/2018/jan/28/fitness-tracking-app-gives-away-location-of-secret-us-army-bases
- What it is: press retelling dated 2018-01-28.
- Page or section used: headline only.
- Fetch extent: page fetched partly; only the headline used and retained.
- Serves: A.
- Saved excerpt: `guardian-folk.txt`.

### Wikipedia — “Strava,” privacy concerns / military breaches

- URL: https://en.wikipedia.org/wiki/Strava#Military_breaches
- What it is: encyclopedia retelling.
- Page or section used: one sentence in “Military breaches.”
- Fetch extent: section fetched partly; only the sentence used and retained.
- Serves: B.
- Saved excerpt: `wikipedia-folk.txt`.

### Baumer et al. — *Data Science in Context*

- URL: https://datascienceincontext.com/wp-content/uploads/2022/07/Data-Science-in-Context-V.995-Web-Beta.pdf
- What it is: popular/educational retelling in an authors’ manuscript for Cambridge
  University Press (2022).
- Page or section used: printed p. 134 (PDF p. 135), §10.1.4, one sentence on Strava.
- Fetch extent: full 294-page PDF fetched; only the sentence used is retained.
- Serves: C.
- Saved excerpt: `data-science-context-folk.txt`.

### *Ars Technica* — “Pentagon tells troops: Turn off fitness tracker GPS when you head to warzones”

- URL: https://arstechnica.com/information-technology/2018/08/pentagon-tells-troops-turn-off-the-fitness-trackers-when-you-head-to-warzones/
- What it is: press retelling dated 2018-08-07.
- Page or section used: headline only.
- Fetch extent: page fetched partly; only the headline used and retained.
- Serves: D.
- Saved excerpt: `ars-folk.txt`.

## Not fetched / not available

- Both live `blog.strava.com/press/` URLs above now redirect to the generic
  `stories.strava.com` homepage. Direct live-page fetches were tried with `curl`; the
  substantive pages were recovered in full from Arquivo.pt instead.
- Internet Archive CDX/replay was tried for both retired Strava posts and returned its
  “Temporarily Offline” page. Arquivo.pt supplied complete captures.
- Direct `curl` fetches of the Medium engineering post and the Defense Department PDF
  returned HTTP 403. Both documents were fetched in full through the text browser; no
  factual claim depends on the blocked route.
- ZDNet’s 2018 article at
  `https://www.zdnet.com/article/pentagon-bans-military-from-using-devices-with-gps/`
  was considered as a folk retelling, but its site blocked the text browser with
  `robots.txt`; it was not used, and the fetchable Ars Technica headline supplies D’s
  folk claim instead.
