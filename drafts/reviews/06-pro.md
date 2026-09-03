**1. Record accuracy: Mismatched claim receipt** (Severity: High)
- **Location:** `DoD concurred with the recommendation. Thirteen months later came the memorandum, which, as saved for this chapter, does not name Strava or the heatmap. <!-- CHECK: 06-gao-dod-concurrence -->`
- **Problem:** The `<!-- CHECK: 06-gao-dod-concurrence -->` tag is placed at the end of the sentence about the DoD memorandum not naming Strava. However, the `06-gao-dod-concurrence` claim in the TSV strictly validates that DoD concurred with the GAO recommendation. The text about the memorandum not naming Strava is left functionally unreceipted, while the tag vouches for a claim it doesn't cover. 
- **Fix:** Move the `<!-- CHECK: 06-gao-dod-concurrence -->` tag to immediately follow "DoD concurred with the recommendation." Add a new check tag (e.g., `<!-- CHECK: 06-dod-memo-no-strava-mention -->`) for the memorandum sentence and register it in the TSV.

**2. Ledger fairness: Primary sources used as the "Folk story"** (Severity: High)
- **Location:** Ledger Row 5 (`Folk story: "the data posted can be easily cross-referenced... (Senators Coons and Flake to Strava, 14 Feb 2018)"`) and Ledger Row 7 (`Folk story: "we are eager to introduce new ways we are protecting that data..." (Strava, "Heatmap Updates", 2018)`).
- **Problem:** `CONTEXT.md` explicitly mandates that the left column of the ledger must be a folk story identified from "named retellings (cite them — Wired, Krebs, the Wikipedia lede) so the ledger's left column is real, not a straw man." Both a senatorial letter and Strava's own corporate blog post are primary documents, not folk retellings. Pitting a primary source against another primary source breaks the chapter's required "Folk story vs record" skeleton.
- **Fix:** Replace the folk claims in Rows 5 and 7 with quotes from secondary press/retellings (e.g., tech news headlines), or remove these rows if no folk retelling fits.

**3. Ledger fairness: Incorrect verdict on opt-in vs opt-out** (Severity: High)
- **Location:** Ledger Row 3: `"Strava did nothing wrong; they displayed anonymized tracks for opted-in users..." (Baumer et al.)` ... Verdict: `OVERSTATED`.
- **Problem:** The textbook claims users were "opted-in". However, James Quarles' letter explicitly states that Strava respected "the ability to opt out of heatmaps altogether". The difference between opt-in (default off) and opt-out (default on) is massive for privacy. The textbook is factually incorrect, not just overstating. According to the ledger vocabulary in `CONTEXT.md` ("WRONG — the record contradicts it"), this deserves the WRONG verdict.
- **Fix:** Change the verdict for this row to `WRONG`.

**4. Mechanism accuracy: Omission of algorithm modification** (Severity: Medium)
- **Location:** `"Under this algorithm, the normalized value of any given pixel represented the exact percentage of pixels with a lower heat value, guaranteeing a perfectly uniform distribution of colors across the display map."`
- **Problem:** The chapter claims the algorithm guaranteed a "perfectly uniform distribution". However, Drew Robb's post explicitly notes: "We use this technique with a slight modification to prevent quantization artifacts in areas of very low raw heat." Since the military bases leak occurred exactly in areas of "very low raw heat," ignoring Strava's specific mathematical modification for those exact areas oversimplifies the mechanism and misrepresents their documented design.
- **Fix:** Acknowledge the modification. For example: "...guaranteeing a highly uniform distribution of colors, though Robb noted a slight modification was applied specifically for areas of very low heat."

**5. Record accuracy: Unreceipted numbers** (Severity: Medium)
- **Location:** `"The total recorded distance spanned 16 billion kilometers, capturing more than 100,000 years of human physical exertion."`
- **Problem:** This sentence contains exact numbers but has no `<!-- CHECK: id -->` tag. The nearest tag (`06-robb-heatmap-scale`) precedes it, and its TSV row does not include these numbers. This violates the priority stack rule: "Every incident-side fact receipted... No numbers from memory."
- **Fix:** Add a check tag after this sentence, and add a corresponding row in `checks/claims/06.tsv` validating the 16 billion km and 100,000 years from the Robb source.

**6. Pre-ship test violation: Open claim** (Severity: Medium)
- **Location:** `"On 3 August 2018 the Deputy Secretary of Defense issued a two-page memorandum... <!-- CHECK: 06-dod-memo-date -->"`
- **Problem:** The claim `06-dod-memo-date` is marked as `open` in the TSV file. `AGENT.md` Pre-ship test 3 strictly requires: "Is every incident claim marked and its row non-`open`?" Shipping with an `open` claim violates the drafting rules.
- **Fix:** Change the status in the TSV from `open` to a checked status (e.g., `checked-by:human:2026-09-03`), as the date is corroborated by the fetch notes in `SOURCES.md`.

**7. Readability: Grammatical error** (Severity: Low)
- **Location:** `"Instead of a blanket ban, the directive lets Combatant Commanders or their designees to authorize non-government geolocation capabilities..."`
- **Problem:** "lets... to authorize" is a grammatical error.
- **Fix:** Change "lets" to "allows", or remove the word "to" before "authorize".
