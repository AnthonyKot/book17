# BLOCK — revise before shipping

The chapter has one source distortion, a misleading replication explanation, two unearned ledger verdicts, and unresolved verification/navigation failures.

Full consolidated report: [drafts/reviews/08-codex.md](/home/diablo/book17/drafts/reviews/08-codex.md)

All ten reviewer findings were adjudicated; three additional substantive findings were added. `./verify.sh 08` currently fails.
FIRMED**.

**Location:** “Cisco says M.E.Doc let its responders inspect engineers' accounts, logs and code.” (break section; claim `08-cisco-access`)

**Problem:** Cisco says M.E.Doc arranged “access to engineers and administrators who walked the team through the system” and provided access to logs and code (`cisco-medoc.txt`, line 10). It does not say Cisco inspected engineers' user accounts. The next source sentence separately says an unknown actor had stolen one administrator's credentials. The prose conflates access to people with inspection of accounts. The claim-register row compounds the problem by summarizing only the credential/root/NGINX findings, leaving the unsupported first sentence invisible to the receipt.

**Fix:** Write “Cisco says M.E.Doc gave its responders access to engineers and administrators, logs and code,” or “let its responders interview engineers and administrators and inspect logs and code.” Update the TSV summary so the whole marked paragraph is represented.

### 2. HIGH — The chapter wrongly makes domain-controller synchronization the mechanism of the common failure

**Reviewer adjudication:** **MISSED BY BOTH REVIEWERS.**

**Locations:** “That same synchronization keeps them inside one failure domain” (break section); “today's trusted machines faithfully synchronize today's destructive state” (closing exercise); related lede claim that synchronized machines “had preserved availability, not recovery.”

**Problem:** Ashton attributes NotPetya's movement into Maersk's servers and domain controllers to pass-the-hash and weakly controlled privileged access (`gavin-ashton.txt`, lines 9–11). Microsoft lists credential/session reuse, file shares, legitimate execution features and SMB vulnerabilities (`microsoft-petya.txt`, lines 10–14). Neither source says Active Directory replication spread NotPetya or replicated destructive state. Microsoft's recovery guide does warn in general that dangerous *directory data* can replicate back during forest recovery, but that is not evidence for the incident mechanism. The current prose blends two distinct properties: replication makes a controller a current availability peer rather than a historical restore point; shared reachability and administrative trust let this malware destroy all of those peers.

**Fix:** Separate the mechanisms explicitly. Say that live controllers continuously held current directory state, so they were not time-separated recovery copies, while NotPetya reached the controller fleet through lateral movement and privileged-access paths. Reserve the “replicating dangerous state” scenario for Microsoft's generic forest-recovery guidance and do not present it as what happened at Maersk.

### 3. HIGH — Ledger row 1 manufactures disagreement by omitting Wired's own caveat

**Reviewer adjudication:** **MISSED BY BOTH REVIEWERS.**

**Location:** “Wired calls the mutually synchronizing domain controllers a ‘decentralized backup strategy.’” → `OVERSTATED` (ledger row 1).

**Problem:** The saved Wired passage does not merely call the controllers backups. It says any controller could “in theory” function as a backup for the others and immediately says the strategy did not cover every controller being wiped simultaneously (`wired-notpetya.txt`, line 6). The record cell then uses Ashton's account to supply essentially the same simultaneous-loss limitation. Selectively dropping Wired's caveat makes the retelling look more naive than it is, so `OVERSTATED` is not earned against the actual folk claim.

**Fix:** Quote or closely paraphrase Wired's complete claim and grade it `HOLDS`, while explaining that “backup” is loose terminology; or locate a named retelling that really presents synchronized replicas as adequate disaster recovery. Do not use the chapter's preferred definition to make Wired say it missed a limitation that Wired expressly states.

### 4. HIGH — Ledger row 4 has no named folk source and its proposed reviewer repair is unsupported

**Reviewer adjudication:** Flash #1 — **CONFIRMED**. Pro #2 — **CONFIRMED**.

**Location:** “The update-server shorthand makes 27 June sound like one poisoned download.” → `MISSING` (ledger row 4).

**Problem:** `CONTEXT.md` §4 requires every left cell to be a specific claim quoted or closely paraphrased from a named retelling. This sentence is the author's interpretation, with no named source. The staged record on the right is useful, but it cannot earn a verdict against an invented folk claim.

Flash's proposed Wikipedia rewrite is not supported by the saved excerpt: Wikipedia says only that M.E.Doc's update mechanism was believed to have been compromised (`wikipedia-petya.txt`, line 6). It does not claim a one-time download or mention 27 June. That repair would preserve the straw man under an attribution.

**Fix:** Find and save a retelling that actually collapses the incident into one 27 June download, then quote or closely paraphrase it; otherwise remove the row and keep the staged sequence in the prose.

### 5. HIGH — Four claim-register rows remain unaudited under the book's explicit pre-ship rule

**Reviewer adjudication:** Flash #3 — **CONFIRMED**, with a correction to the reviewer's tooling explanation.

**Location:** `08-ghana-open`, `08-signing-open`, `08-ledger-ghana`, and `08-ledger-signing` in `checks/claims/08.tsv`.

**Problem:** `AGENT.md` pre-ship test 3 requires every incident claim row to be non-`open`. The chapter may legitimately give a ledger claim an `OPEN` verdict, but the register status records whether the chapter's bounded statement about the evidence has been audited. Chapter 1 demonstrates the intended distinction: its ledger can remain `OPEN` while its corresponding TSV claim is checked. Here the negative-source audit is documented in `SOURCES.md`, yet the four duplicate register entries are still marked `open`.

The reviewer is wrong only if read as saying these rows make the claims checker itself fail: `checks/claims.py` labels open rows advisory and exits successfully. `./verify.sh 08` is nevertheless red for a separate count-sync failure.

**Fix:** After confirming the bounded statements against the saved corpus, mark all four register rows `checked-by:...`; keep the two ledger verdicts `OPEN`. Consider one claim ID per repeated uncertainty rather than registering the same source-gap twice.

### 6. MEDIUM — The nine-day `OVERSTATED` verdict is not established by the ten-day source

**Reviewer adjudication:** Flash #6 — **CONFIRMED**. Pro #3 — **CONFIRMED**.

**Location:** “Darknet Diaries says Maersk had a functioning network after about nine days.” → `OVERSTATED` (ledger row 7).

**Problem:** “About nine days” is compatible with Maersk's “just 10 days.” Nor does the record establish that “functioning network” and “network was rebuilt” are competing measurements. They could be different milestones, as the prose itself acknowledges. The source therefore does not show the folk claim to be wrong in a way that matters, which is the definition of `OVERSTATED`.

Flash's suggested repair — “Darknet Diaries equates an initial milestone to full recovery” — is also unsupported: the podcast excerpt does not call its milestone “full recovery,” and the record does not establish which milestone came first.

**Fix:** Regrade to `HOLDS` with the scope difference noted, or cut the row. Do not turn an unresolved semantic difference into an adverse verdict.

### 7. MEDIUM — Navigation and contents are stale more broadly than the reviewer reported

**Reviewer adjudication:** Flash #4 — **CONFIRMED**, but incomplete.

**Location:** Chapter 8 links “Next” to chapter 10.

**Problem:** Chapter 8 skips the existing chapter 9, as Flash reports. The surrounding sequence is also stale: chapter 7 skips chapters 8 and 9, chapter 10 points back to chapter 7, and `index.html` lists only eight of the ten chapter files while leaving chapters 8 and 9 under “Pitches awaiting a pick.” This is why `./verify.sh 08` reports `10 chapter files on disk; 8 linked from index.html` and exits `FAIL`.

**Fix:** Run the repository's navigation rewriter, verify the 7→8→9→10 chain in both directions, move chapters 8 and 9 into the main contents list, remove/update their pitch-status entries, and rerun `./verify.sh 08`.

### 8. MEDIUM — The lede's receipt does not cover its synchronization/availability claim

**Reviewer adjudication:** **MISSED BY BOTH REVIEWERS.**

**Location:** “a worldwide set of synchronized machines had preserved availability, not recovery” under claim `08-lede-controller`.

**Problem:** The TSV row and cited Ashton excerpt support the first restored controller running on a Surface Pro 4 and a globally distributed controller loss. They do not state that the controllers synchronized, or that they had preserved availability. Synchronization appears in Wired, while “availability, not recovery” is the author's architectural conclusion. One marker currently makes the participant source appear to support all of it.

**Fix:** Split the receipt: keep Ashton's Surface/global-loss facts under the existing claim, attribute synchronization to Wired, and present the availability/recovery distinction explicitly as analysis. Coordinate this with finding 2 so the lede does not imply replication caused the wipeout.

### 9. LOW — The Maersk PDF is cited under a subsection title as though that were the publication

**Reviewer adjudication:** Flash #5 — **CONFIRMED**.

**Location:** the line-53 reference, reading list, and the `08-ten-days-cost` / `08-ledger-days` claim citations.

**Problem:** “What we learned from the NotPetya Virus cyber-attack” is a boxed section on page 4 of *A View from the Other Side of a Crisis*, not the document title. The link is correct and the factual claim is supported, so this is bibliographic clarity rather than record falsity.

**Fix:** Cite *A View from the Other Side of a Crisis*, p. 4, followed by the section title in quotation marks.

### 10. REJECTED — A diagram is not required for the whiteboard test

**Reviewer adjudication:** Flash #7 — **REJECTED**.

**Location:** “Draw these four boxes clearly on a whiteboard...” (mechanism section).

**Why rejected:** The checklist asks whether a reader can draw the mechanism, not whether the chapter embeds a diagram. The prose gives the four nodes, their order, and the two questions to ask at each boundary; it is sufficiently operational. The suggested ASCII art is not a neutral fix: drawing a “Digital Signature” as a direct artifact-to-client arrow can obscure that a signature is produced by a signing authority, accompanies or is associated with the artifact, and is verified by the client. A diagram could improve presentation, but its absence is not a review finding.

## Verification snapshot

- OWASP quote gate: 2 quotations, both found.
- Claim-marker gate: 31 markers / 31 rows, no mismatches; 4 advisory `open` statuses.
- Structure: passes at exactly 2,200 words.
- Internal links: no broken target paths, though the sequential targets are wrong.
- Overall `./verify.sh 08`: **FAIL**, because 10 chapter files exist but only 8 are linked from `index.html`.

No fairness-to-named-people or capability-leak issue was found beyond the Cisco access distortion above. The chapter does explicitly state the thin defense record and the imperfect OWASP/web-application fit.
