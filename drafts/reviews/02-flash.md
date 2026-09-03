### 1. Release Timeline Conflation: 8 November 2017 Stated as GA / Shipping Date

* **Location:** 
  * Lede: `"And The Next Web, on the day 3.6 shipped: MongoDB 'will no longer come with an unsafe configuration out of the box'."`
  * Section *The defense*: `"General availability came on 8 November 2017. The London press release: 'The most popular installer for MongoDB already limits network access by binding to localhost by default...'"`
  * Section *The defense*: `"Seven months passed between merge and GA, and the September wave fell inside them."`
  * Section *The ledger* (Row 5): `"GA 8 Nov 2017."`
* **Problem:** 8 November 2017 was the date MongoDB announced version 3.6 at the MongoDB Europe conference in London and issued its press release ([`mongodb-newsroom-2017-11-08.txt`](file:///home/diablo/book17/resources/sources/02/mongodb-newsroom-2017-11-08.txt#L1-L15)), not the date 3.6 shipped or reached General Availability (GA). The cited source ([`tnw-2017-11-08.txt`](file:///home/diablo/book17/resources/sources/02/tnw-2017-11-08.txt#L10)) explicitly reports: *"Release candidates of the latest version of MongoDB have already been floated. The final release is expected at some point in December."* MongoDB 3.6.0 became generally available in early December 2017 (with 3.6.1 following on 26 December 2017, as recorded in [`release-notes-3.6-and-2.6-bind.txt`](file:///home/diablo/book17/resources/sources/02/release-notes-3.6-and-2.6-bind.txt#L108)). Describing 8 November 2017 as "General availability" and "the day 3.6 shipped" overstates the press release.
* **Fix:** Change "on the day 3.6 shipped" to "on the day 3.6 was announced", change "General availability came on 8 November 2017" to "The product was announced in London on 8 November 2017, with General Availability following in December", and adjust the elapsed time between the April 2017 commit/merge and December 2017 GA accordingly.

---

### 2. Ledger Verdict Asymmetry: Row 2 Graded `WRONG` vs Row 3 Graded `OVERSTATED`

* **Location:** 
  * Section *The ledger* (Row 2): Folk claim: `MongoDB "will no longer come with an unsafe configuration out of the box" as of 3.6 (TNW, 8 Nov 2017); "Because of MongoDB's default security configuration, which allows any user full access to the database" (Wikipedia § Security); "up until recently, the software's default configuration is insecure" (Register, 9 Jan 2017).` Verdict: `WRONG`.
  * Section *The ledger* (Row 3): Folk claim: `"If installed on a server with the default settings, for example, MongoDB allows anyone to browse the databases, download them, or even write over them and delete them." (Krebs, 10 Jan 2017...)` Verdict: `OVERSTATED`.
* **Problem:** Row 2 grades the folk claim that MongoDB was insecure out of the box until 3.6 as `WRONG`, arguing that official RPM and DEB packages had bound to localhost since 2.6.0 (April 2014). However, as the chapter itself establishes, the standalone binary (`mongod`), tarball distributions, and unmanaged cloud images continued to default to `0.0.0.0` until commit [`60636b4`](file:///home/diablo/book17/resources/sources/02/commit-60636b4.txt#L98-L99) in 3.6, and authentication was not (and is not) enabled out of the box. In Row 3, Krebs's virtually identical claim about default settings is graded `OVERSTATED` with the rationale: *"True of the tarball, the pre-2.6 packages and images built from them; not of an RPM/DEB install after April 2014. The authentication default was never changed."* Under CONTEXT §4, a claim that is true in outline (for raw binaries, tarballs, and cloud images) but wrong regarding the package timeline is `OVERSTATED`, not `WRONG`. Marking Row 2 as `WRONG` relies on defining "MongoDB" solely as "official RPM/DEB packages".
* **Fix:** Change the verdict of Ledger Row 2 from `WRONG` to `OVERSTATED`, aligning its rationale with Row 3 (or narrow Row 2's folk claim explicitly to the assertion that *all* MongoDB installations/packages were open until 3.6).

---

### 3. Tracking Sheet Characterization: "one row per actor, 109 rows in all"

* **Location:** 
  * Section *The break*: `"The document behind every January figure is a Google sheet. Its first tab has one row per actor, 109 rows in all, with the name of the replaced database..."`
  * Checks register ([`checks/claims/02.tsv`](file:///home/diablo/book17/checks/claims/02.tsv#L17)): `02-sheet`: `"The Gevers/Merrigan 'MongoDB ransacking' Google sheet, first tab: 109 rows, one per actor..."`
* **Problem:** The primary sheet excerpt ([`gevers-merrigan-sheet-excerpt.txt`](file:///home/diablo/book17/resources/sources/02/gevers-merrigan-sheet-excerpt.txt#L5-L74)) contains 109 total spreadsheet rows, but it is not "one row per actor". Actors with multiple ransom campaigns, bitcoin wallets, or replaced database names span multiple consecutive rows (e.g., `Harak1r1` spans rows 8–21; `Kraken0` spans rows 23–30; `cru3lty` spans rows 63–64). There are far fewer than 109 distinct threat actors tracked in the sheet.
* **Fix:** Rephrase to: `"Its first tab has 109 rows in all across dozens of tracked actors, recording each campaign signature with the name of the replaced database..."` and update the claim text in `checks/claims/02.tsv`.

---

### 4. Database Terminology: "single table named WARNING"

* **Location:** 
  * Lede: `"...found, where its data had been, a single table named WARNING with a ransom note in it."`
  * Section *The break*: `"...instead of its collections, one table named WARNING."`
* **Problem:** MongoDB is a document database organized into databases, collections, and BSON documents; it does not have "tables". While Bleeping Computer's original report ([`bleeping-2017-01-03.txt`](file:///home/diablo/book17/resources/sources/02/bleeping-2017-01-03.txt#L12-L20)) loosely used the words "collection of tables" and "tablename WARNING" when quoting Gevers, presenting "a single table named WARNING" in the lede without qualification uses incorrect NoSQL terminology.
* **Fix:** In the lede, adjust the phrasing to reflect MongoDB terminology or quote the source: `"...found, where its data had been, a single collection named WARNING (reported at the time as a table) with a ransom note in it."`

---

### 5. Technical Nuance: "no password on the admin account" vs. Disabled Access Control

* **Location:** 
  * Lede: `"...opened one more MongoDB server that had no password..."`
  * Section *The break*: `"...without a password on the admin account..."`
  * Section *The ledger* (Row 1): `"...without a password on the administrator account..."`
* **Problem:** In default MongoDB deployments of that era, access control was disabled entirely (`--auth` not specified), meaning clients connected without any credentials and commands were unauthenticated. There was no initialized "admin account with an empty password". While "no password on the admin account" accurately quotes the contemporaneous retellings ([`bleeping-2017-01-03.txt`](file:///home/diablo/book17/resources/sources/02/bleeping-2017-01-03.txt#L11), [`ottenheimer-2017-09-08.txt`](file:///home/diablo/book17/resources/sources/02/ottenheimer-2017-09-08.txt#L13)), the prose before line 52 adopts this phrasing as fact before explaining that authentication itself was the disabled switch.
* **Fix:** Clarify in the text where the phrase first appears that "no password on the admin account" was the public shorthand for authentication being disabled entirely.
