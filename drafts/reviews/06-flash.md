### 1. Record Accuracy / Ledger Fairness (Severity: High)
- **Location:** `(Baumer et al., <em>Data Science in Context</em>, Cambridge University Press, 2022, p. 134)` (in Ledger Row 3, line 90) and `### Baumer et al. — *Data Science in Context*` ([`SOURCES.md:L120`](file:///home/diablo/book17/resources/sources/06/SOURCES.md#L120)).
- **Problem:** The cited textbook *Data Science in Context* was written by Alfred Spector, Peter Norvig, Chris Wiggins, and Jeannette M. Wing. Benjamin Baumer is not an author of this work. While the main prose ([`06-strava.html:L35`](file:///home/diablo/book17/chapters/06-strava.html#L35)), claims register ([`06.tsv:L9`](file:///home/diablo/book17/checks/claims/06.tsv#L9)), and Reading list ([`06-strava.html:L112`](file:///home/diablo/book17/chapters/06-strava.html#L112)) correctly credit Spector, Norvig, Wiggins, and Wing, the ledger table entry (line 90) and `SOURCES.md` still attribute the book to "Baumer et al."
- **Fix:** Replace `Baumer et al.` with `Spector et al.` in Ledger Row 3 ([`06-strava.html:L90`](file:///home/diablo/book17/chapters/06-strava.html#L90)) and in [`SOURCES.md:L120`](file:///home/diablo/book17/resources/sources/06/SOURCES.md#L120).

---

### 2. Record Accuracy / Pre-Ship Gating (Severity: High)
- **Location:** `06-dod-memo-date` in [`checks/claims/06.tsv:L33`](file:///home/diablo/book17/checks/claims/06.tsv#L33) (and `<!-- CHECK: 06-dod-memo-date -->` in [`06-strava.html:L69`](file:///home/diablo/book17/chapters/06-strava.html#L69)).
- **Problem:** Claim `06-dod-memo-date` is marked with status `open` in `06.tsv`, which violates `AGENT.md` Pre-ship test 3 ("Is every incident claim marked and its row non-`open`?"). The claim remains `open` because the saved excerpt [`dod-geolocation-memo.txt`](file:///home/diablo/book17/resources/sources/06/dod-geolocation-memo.txt) omitted the memorandum's header and date line, even though the primary DoD memorandum PDF is dated August 3, 2018 and signed by Deputy Secretary Patrick M. Shanahan.
- **Fix:** Add the date line (`August 3, 2018`) and signatory block (`Patrick M. Shanahan, Deputy Secretary of Defense`) into [`resources/sources/06/dod-geolocation-memo.txt`](file:///home/diablo/book17/resources/sources/06/dod-geolocation-memo.txt), and update the status of `06-dod-memo-date` in [`checks/claims/06.tsv:L33`](file:///home/diablo/book17/checks/claims/06.tsv#L33) from `open` to `checked-by:...`.

---

### 3. Ledger Fairness (Severity: Medium)
- **Location:** `"the data posted can be easily cross-referenced with other publicly available information to identify individual users" (Senators Coons and Flake to Strava, 14 Feb 2018).` (Ledger Row 5, [`06-strava.html:L92`](file:///home/diablo/book17/chapters/06-strava.html#L92))
- **Problem:** The left column uses a primary congressional oversight letter rather than a secondary retelling from the public or press narrative. Under `AGENT.md` incident rules, the left column must be sourced from named retellings (e.g., press or popular accounts) so that primary government inquiries are not cast as folk straw men.
- **Fix:** Attribute the de-anonymization claim to a named secondary article that reported on the cross-referencing of heatmap data, and cite the Coons/Flake letter in the right column alongside Hassan et al.

---

### 4. Ledger Fairness (Severity: Medium)
- **Location:** `"we are eager to introduce new ways we are protecting that data and the athletes who provide it" (Strava, "Heatmap Updates", 2018).` (Ledger Row 7, [`06-strava.html:L94`](file:///home/diablo/book17/chapters/06-strava.html#L94))
- **Problem:** The left column quotes Strava's own corporate blog post rather than a named secondary retelling. While the row evaluates whether Strava's remediation achieved measurable outcomes (earning an `OPEN` verdict), using a vendor primary source in the folk column blurs the boundary between public retelling and primary documentation.
- **Fix:** Source the folk column to a named press account that reported Strava's updates as having resolved the security exposure, or rephrase the left column to reflect the media narrative being tested.

---

### 5. Readability / Grammar (Severity: Low)
- **Location:** `Instead of a blanket ban, the directive lets Combatant Commanders or their designees to authorize non-government geolocation capabilities...` ([`06-strava.html:L71`](file:///home/diablo/book17/chapters/06-strava.html#L71))
- **Problem:** Ungrammatical verb construction ("lets [x] to authorize").
- **Fix:** Change to `the directive allows Combatant Commanders or their designees to authorize` or `the directive lets Combatant Commanders or their designees authorize`.

---

### 6. Record Accuracy (Severity: Low)
- **Location:** `In a later post, "Heatmap Updates", archived in July 2018, the company announced changes...` ([`06-strava.html:L41`](file:///home/diablo/book17/chapters/06-strava.html#L41)) vs `Strava, "Heatmap Updates", 13 March 2018` ([`06-strava.html:L109`](file:///home/diablo/book17/chapters/06-strava.html#L109), [`SOURCES.md:L47`](file:///home/diablo/book17/resources/sources/06/SOURCES.md#L47), and [`06.tsv:L32`](file:///home/diablo/book17/checks/claims/06.tsv#L32)).
- **Problem:** The prose avoids naming the post date and refers only to the archive capture date ("archived in July 2018") because [`strava-heatmap-updates.txt`](file:///home/diablo/book17/resources/sources/06/strava-heatmap-updates.txt) omitted the date line. However, the Reading list, `SOURCES.md`, and claims file all specify the post date as 13 March 2018.
- **Fix:** Include the 13 March 2018 publication date in the header of [`strava-heatmap-updates.txt`](file:///home/diablo/book17/resources/sources/06/strava-heatmap-updates.txt) and harmonize the prose in line 41 to reference March 2018 directly.

---

### 7. Fairness to Named People / Precision (Severity: Low)
- **Location:** `He pledged to review motivating features to ensure they could not be abused by people with bad intent.` ([`06-strava.html:L37`](file:///home/diablo/book17/chapters/06-strava.html#L37))
- **Problem:** Quarles' letter states: *"reviewing features that were originally designed for athlete motivation and inspiration to ensure they cannot be compromised by people with bad intent."* Paraphrasing "compromised" as "abused" alters the nuance from architectural integrity/compromise to intentional user abuse.
- **Fix:** Change to `ensure they could not be compromised by people with bad intent` to match Quarles' exact terminology.
