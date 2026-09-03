Created the consolidated report: [06-codex.md](/home/diablo/book17/drafts/reviews/06-codex.md).

Verdict: **BLOCK**. All 14 reviewer findings are adjudicated: 11 confirmed, 2 rejected, and 1 unverifiable. The report also identifies major ledger, sourcing, receipt, and defense-record problems both reviewers missed.
Location:** title/lede, “The Pentagon Did Not Ban the Watch”; defense, “the popular press seized upon a simple narrative”; ledger row 1.

The only saved retelling for this thesis says, “Pentagon tells troops: Turn off fitness tracker GPS when you head to warzones” (`ars-folk.txt`). That is a claim about disabling GPS, not banning a watch. The memorandum does prohibit personnel from using geolocation features in operational areas (`dod-geolocation-memo.txt`, lines 10–14). Its exceptions make the headline incomplete, but the ledger’s device-versus-feature rebuttal answers a claim the headline never made. The chapter itself upgrades “turn off GPS” into “banned fitness trackers” in the lede.

**Fix:** Either fetch and save a named retelling that explicitly says the Pentagon banned devices, then grade that exact claim, or reframe the title/lede and grade the Ars headline only on its omitted geographic scope and exceptions. On the current evidence, the feature/device distinction supports Ars rather than refutes it.

**Reviewer coverage:** missed by both.

### 2. Blocker — ledger rows 2 and 6 manufacture omissions rather than test what the retellings say

**Location:** row 2, Guardian “gives away location”; row 6, Wikipedia “discovered that this map had mapped military bases.”

The primary/technical record agrees that the heatmap leaked sensitive locations. Nothing in the Guardian headline claims a defect, a particular mechanism, or non-public source data, so “hides the design” does not earn `OVERSTATED`; with only the headline saved, it earns `HOLDS`. Likewise, Wikipedia reports the January discovery. It does not claim that DoD had never anticipated aggregation risk. The author-added gloss “the risk as a discovery” creates the proposition that the GAO report then defeats. That is a straw man, not a defender-useful `MISSING` row.

**Fix:** Mark row 2 `HOLDS` unless a fuller saved Guardian passage makes a mechanism claim. Remove row 6 or replace it with a named retelling that actually says the aggregation risk was first recognized in January 2018.

**Reviewer coverage:** missed by both.

### 3. Blocker — rows 5 and 7 are not folk stories; row 5’s record also does not test its claim

**Location:** row 5, Coons/Flake letter; row 7, Strava “Heatmap Updates.”

Both left cells use primary documents, contrary to `AGENT.md` lines 26–30 and the chapter contract’s folk-story-versus-record skeleton. Row 5 has a second, independent defect: Hassan et al. say identities were not **directly** leaked by the heatmap and describe a related spoofed-GPS attack. That does not test the senators’ different claim that heatmap data could be cross-referenced with other public information. The cited paper neither confirms nor refutes that cross-referencing claim, so `OVERSTATED` is unearned. Row 7 tests a vendor aspiration rather than a public retelling and therefore cannot carry a meaningful ledger verdict.

**Fix:** Remove both rows unless saved named retellings make the exact claims. If row 5 remains elsewhere in prose, describe the sources as two different identification paths rather than treating one as a rebuttal to the other.

**Reviewer adjudication:** Flash 3 **CONFIRMED**; Flash 4 **CONFIRMED**; Pro 2 **CONFIRMED**. The reviewers correctly found the source-class violation, but both missed row 5’s evidentiary non sequitur.

### 4. High — “no bug” is repeatedly stated as an established universal fact

**Location:** meta description, “without a single software bug”; lede, “The app had no bug”; mechanism, “zero implementation defects” and “Not a single line of software failed.”

Robb documents intended data selection, rasterization, and normalization. That can show that the described exposure follows from the documented design; it cannot prove that the entire application contained zero bugs or that every line met its specification. The chapter has the defensible wording twice—“Nothing in the record describes a defect”—but replaces that evidence-bound claim with absolutes elsewhere.

**Fix:** Use the corpus-limited formulation consistently: no implementation defect is needed to explain this exposure, and none is described in the collected record.

**Reviewer coverage:** missed by both.

### 5. High — the defense section claims a documented Strava response and a newly designed threat model that its sources do not establish

**Location:** “When the military establishment responded to the heatmap disclosures”; “It designed an operational threat model”; “Strava complemented the military’s operational controls.”

The saved memorandum never names Strava or the heatmap, as the chapter later concedes. The saved GAO report shows that the threat-based OPSEC survey predated the memorandum and was already required under Directive 5205.02E. The memorandum invokes that existing process; it does not document designing a new threat model. “Complemented” also suggests a coordinated defense record not present in the packet.

**Fix:** Say the August policy followed the disclosure in time, invoked an existing OPSEC-survey requirement, and does not itself state its relationship to Strava. “Alongside” is safer than “complemented.” If causal attribution is retained, add a primary source that expressly makes it and receipt the claim.

**Reviewer coverage:** missed by both.

### 6. High — ledger row 3 has the wrong authors, bundles unlike claims, and uses the wrong verdict for the factual part

**Location:** row 3 and `resources/sources/06/SOURCES.md`, “Baumer et al.”; verdict `OVERSTATED`.

The book is by Alfred Spector, Peter Norvig, Chris Wiggins, and Jeannette Wing, as the chapter prose, reading list, and claim row correctly say. The row then bundles a normative judgment (“did nothing wrong”), anonymization, opt-in status, and user awareness. Quarles’s “ability to opt out” directly contradicts the factual “opted-in” claim; under the fixed vocabulary that narrowed claim is `WRONG`. Quarles acknowledging responsibility does not by itself adjudicate the normative “did nothing wrong.”

**Fix:** Correct the authors in both locations. Narrow the row to the opt-in claim and mark it `WRONG`, or split/remove the other propositions rather than giving the composite an averaged verdict.

**Reviewer adjudication:** Flash 1 **CONFIRMED**; Pro 3 **CONFIRMED**, with the qualification that the row must first be narrowed because it currently contains more than one claim.

### 7. High — exact facts are unreceipted, misreceipted, or still open

**Locations:**

- “16 billion kilometers” and “more than 100,000 years” have no marker and are absent from `06-robb-heatmap-scale`, although `strava-building-heatmap.txt` lines 17–18 supports them.
- “The map ran for nearly three months before anyone said in public what it showed” has no marker; the dates can establish an interval, but the universal “before anyone” claim is not established by the packet.
- “Thirteen months later” and “the memorandum … does not name Strava or the heatmap” are not covered by `06-gao-dod-concurrence`; that row receipts only DoD concurrence.
- `06-dod-memo-date` remains `open`. The official PDF confirms the 3 August 2018 date and the Deputy Secretary letterhead, but those lines were omitted from the saved excerpt. `./verify.sh 06` reports one open claim even though its final summary says `PASS`.

**Fix:** Add matching claim rows/markers or cut the facts; split the GAO concurrence receipt from the memorandum-content receipt. Save the DoD header/date (and signatory if named), then re-check rather than merely changing the status flag.

**Reviewer adjudication:** Pro 1 **CONFIRMED**; Pro 5 **CONFIRMED**; Flash 2 **CONFIRMED**; Pro 6 **CONFIRMED**. The proposed bare status flip in Pro 6 is not sufficient evidence hygiene.

### 8. High — the claimed absence of defense measurements cannot be proved from the two implementation documents cited

**Location:** “neither entity ever published empirical follow-up audits”; claim `06-defense-unmeasured-outcome`.

The claim row cites only the DoD memorandum and Strava update. Those documents do not contain outcome measurements, but they cannot establish that neither entity **ever published** one. This is an unchecked universal negative disguised as a checked claim. The next sentence has the same scope problem in “The public record does not contain.”

**Fix:** Bound the claim to the research corpus and date: “No follow-up measurement was found in the sources collected for this chapter as of 3 September 2026.” Record the search scope, or add a source that actually surveys follow-up evidence.

**Reviewer coverage:** missed by both.

### 9. Medium — two identity/privacy statements are stronger than Hassan et al.

**Location:** “Identifying a person needed a different feature”; “randomized spatial cloaking to prevent reverse-engineering of endpoints.”

Hassan et al. say identity was not **directly** leaked in the heatmap and describe one related attack; that does not prove that every identification route required another Strava feature. On Privacy Zones, the excerpt says the countermeasure increases the complexity of breaking an endpoint privacy zone and “may” dissuade attackers, while the chapter says it prevents reverse engineering.

**Fix:** Preserve the source’s bounds: the heatmap did not directly expose IDs; the paper demonstrated an adjacent ID-discovery method. Say spatial cloaking was adopted to make endpoint inference harder, not to prevent it.

**Reviewer coverage:** missed by both.

### 10. Medium — the OWASP comparison and scanner claim are overbroad

**Location:** “No automated code scanner could ever have detected this exposure”; “That is OWASP’s segregation advice in operational form.”

The first sentence unnecessarily universalizes beyond the evidence. The useful point is that ordinary static/dynamic defect scanning would not identify the documented business-risk assumption. The second sentence conflates OWASP’s advice to segregate application/network tiers by exposure with DoD’s tiered categorization of location sensitivity. Threat modeling is the direct OWASP fit; tier segregation is not.

**Fix:** Bound the scanner claim and connect the defense to OWASP’s saved threat-modeling language instead of the unrelated tier-segregation bullet.

**Reviewer coverage:** missed by both.

### 11. Low — grammar error

**Location:** “lets Combatant Commanders or their designees to authorize.”

**Fix:** Use “allows … to authorize” or “lets … authorize.”

**Reviewer adjudication:** Flash 5 **CONFIRMED**; Pro 7 **CONFIRMED**.

### 12. Low — the Heatmap Updates publication date is repeated but not preserved in the saved excerpt

**Location:** prose says “archived in July 2018”; the reading list and `SOURCES.md` say 13 March 2018.

The prose is accurate about the archive capture and does not conflict with a March publication date. However, the saved post has no date line, so the exact publication date repeated elsewhere in the repository cannot be independently re-checked from the evidence packet.

**Fix:** Preserve the dated page metadata/header from a primary archive, or omit the exact publication date. If retained, distinguish “published 13 March” from “captured 19 July.”

**Reviewer adjudication:** Flash 6 **UNVERIFIABLE** as stated. It correctly spots an evidence-preservation gap, but the present prose is not inconsistent, and the saved sources do not establish that adding “13 March” to the excerpt would reproduce the archived page faithfully.

## Rejected reviewer findings

- **Flash 7 — REJECTED.** “Abused by people with bad intent” is a faithful, non-prejudicial paraphrase of “compromised by people with bad intent.” It neither changes the actor nor attributes motive beyond the source. Quoting the original would be stylistically closer, but this is not a fairness or accuracy defect.
- **Pro 4 — REJECTED.** Robb does mention “a slight modification to prevent quantization artifacts in areas of very low raw heat,” but then expressly says the approach has a “perfectly uniform distribution over the colormap” (`strava-building-heatmap.txt`, lines 38–40). The reviewer’s claim that the modification invalidates the chapter’s uniform-distribution statement is contradicted by the source, and its assertion that the modification targeted the exact military-leak condition conflates low raw heat with Hassan’s different phrase, sparse background noise. Mentioning the modification could add completeness, but its omission is not the claimed mechanism error.

## Gate result

`./verify.sh 06` finds 33 markers and 33 rows, no mismatches, valid OWASP quotations, valid links, and acceptable structure at 2,309 words. It also reports one `open` incident claim. More importantly, the mechanical marker gate does not detect the unmarked and overbroad claims above or the ledger’s source/verdict failures; the chapter does not pass the substantive pre-ship tests in `AGENT.md`.
