# Chapter 05 — author's craft pass (Fable, 2026-09-03)

Read as a reader after the panel-revised codex draft (`05-applied.md`). Baseline: `./verify.sh 05` PASS, structure ok, 2,302 words. Edited lens by lens; one WIP commit per lens. Zero new facts; anything a better sentence needed but the excerpts do not hold is marked `<!-- pending fact-check -->` in the chapter and listed at the end.

## Lens 1 — Argument

**Restated in one sentence, as I found it:** MOVEit's SQL injection was not a missing escape but an escape repeated per use with one use missed, reached by a route through session state; parameterization changes that promise, and the four further SQL-injection CVEs Progress patched in five weeks show that repairing one function and removing a class are different jobs.

Found: the lede promised the first half (one function, escaped one use and not the other) but not the second half, which is where the ending goes (review found two more rounds; "repairing one observed path and eliminating a defect class are different jobs"). The break section carried an authorial aside ("The chapter need not reproduce the requests or payload…") that talks about the chapter instead of the record. The defense section's last two paragraphs made the same point twice (sharp center / soft edges; how vs institutional why) and repeated the Order 22 caveat a third time.

Changed:
- Lede: now ends "One function explains the break and the defense. The patches after it explain why fixing a function and removing a class are different jobs." Trimmed to 120 words (the cap).
- Cut the aside from the Mandiant paragraph.
- "Then one patch became three advisories" → "Then the one patch became a sequence" (the paragraph lists 9 June, 15 June and a July service pack; "three" was counting two ways).
- Merged the defense section's last two paragraphs into one (the Order 22 caveat now appears in the break section and the reading list only).

Every section still lands on its TEMPLATE beat; nothing restates across sections except the defense's one-paragraph recap of the diff, which the beat needs.

## Lens 2 — Mechanism in the reader's hands

Found: the pre-patch pseudocode showed one `LIKE` slot and an ellipsis, so the reader could not see the "four contexts from one field" that the closing section asks them to count; the post-patch block used `escaped` without defining it; the sentence "The route through session state reached the use that was not [escaped]" said more than Rapid7's excerpt does (Rapid7 says naive attempts failed because the application escaped the arguments, and that the path it found ran through session state to `UserGetUsersWithEmailAddress()`; it does not say which slot the payload landed in). The mechanism section was also under its TEMPLATE range (469 words against 500–700).

Changed:
- Pre-patch pseudocode now shows the whole `SELECT … WHERE` shape from Rapid7's diff: the raw `Email='{2}'` equality and the three escaped `{1}` pattern slots, with the intro saying what is dropped (two optional clauses, the decompiler's late-binding scaffolding). Post-patch block defines `escaped`; its intro says what it drops (column list, `InstID`/`Deleted` conditions, ordering).
- Added a one-sentence whiteboard: one address, four slots in one string, an escaper in front of the pattern slots and nothing in front of the equality.
- Weakened the session-route sentence to what the excerpt supports; TSV row `05-rapid7-naive-failed` reworded to match.
- Added OWASP's own "vulnerable when" line (gated, verbatim): "Dynamic queries or non-parameterized calls without context-aware escaping…" — *context-aware* is the chapter's whole point about per-use escaping, and OWASP's phrase carries it better than mine did.
- Trimmed the "polite internal name" flourish to a plain sentence.

Mechanism section now 540 words. Chapter 2,362.

## Lens 3 — The ledger and the record

Read every marked sentence against its excerpt. Findings and changes:
- **Spokesperson quote compressed.** The chapter had "a sophisticated, multi-stage zero-day attack"; TechTarget's quote is "a sophisticated, multi-stage attack to exploit this zero-day vulnerability". Now quoted as the excerpt has it, with the "fixed the issue" phrase set up as the one folk claim that comes from Progress itself (which is why a vendor statement sits in the folk column of row 5). TSV rows `05-spokesperson-techtarget` and `-provenance` reworded.
- **KB capture overstated.** "catches the advisory while the patch was still being made" — the 1 June 00:22 UTC capture still says "while our team produces a patch" but already lists fixed versions. Now says only what the capture says. "leave only SFTP and FTP/S operating normally" was an instruction the article did not give; it noted those protocols would keep working. TSV rows `05-kb-first-state`, `05-kb-revision-cve`, `05-kev-entry` tightened to the excerpts' wording (the KEV "Known" mark is on the entry; the date is the add date).
- **1,690 of 2,098 attributed to "Emsisoft".** The excerpt attributes the sentence to "Callow" and never states his affiliation (the tally itself is Emsisoft's). Now "TechTarget reported…", with a `pending fact-check` comment. TSV row `05-third-party-share` says so.
- **Row 1 record cell** did not itself earn "steal customer data"; added Mandiant's 27 May web-shells-then-data-theft evidence (source added to the TSV row).
- **Row 4 folk cell** lacked its source tag; now "(TechCrunch)".
- **Row 5 record cell** now quotes Rapid7 exactly ("several parts of an exploit chain that were not fully mitigated by the first patch") rather than paraphrasing, since the OVERSTATED verdict rests on that sentence. Fairness to Progress: its position (the June flaws were distinct) stays in the cell.
- Verdicts unchanged: HOLDS 2, OVERSTATED 1, MISSING 1, OPEN 1. `drafts/05.ledger.md` synced (rows 1, 4, 5).
- Checked and left alone: the 8-K timeline, Mandiant attribution wording, Emsisoft/KonBriefing method sentences, the five-CVE count (34362, 35036, 35708, 36934, 36932 across 31 May–6 July), the 10-K counts, the SEC letter, Order 22's status as allegations, all Rapid7 diff claims, the CISA Secure by Design paraphrases.

## Lens 4 — Prose

Found: after lens 1's cut, "That boundary sat on an internet-facing file-transfer service" had lost its antecedent; TechTarget says "instances", the chapter said "servers"; a few phrases were padded ("not merely", "permits reviewers to answer differently", "the large people number"); every break paragraph ran 70–120 words with no short one; two "public record does not…" hedges in different sections said the same thing in the same words.

Changed: antecedent fixed ("The vulnerable page sat on…"); "instances"; the five-CVEs-in-five-weeks sentences split out as a two-sentence paragraph; "recorded here as exploited" → "recorded as exploited in the sources saved for this chapter"; the closing-section sentence now reads "It is an interface that lets the answer differ at each occurrence"; the defense hedge reworded so the two do not echo. No headers added; no paragraph over 150 words; no sentence over 40 (the checker does not split on a period inside closing quotes, so two quotes now end British-style, as chapter 2's do).

Section sizes after the pass: break 827, mechanism 567, defense 650, see 222 — all inside TEMPLATE's ranges. Chapter 2,397 words.

## Lens 5 — The reader's exit

Found: the closing section was already a procedure rather than a moral — start at the final database call, mark every occurrence of one value as raw, escaped or bound, follow it one step further back than its variable name, and treat an API that makes the bound shape awkward as part of the finding. It passes the "can do it this week" test as written.

Changed: only the opening — it now sets the time frame ("This week, open one function…") and names the obvious candidate ("a lookup by email address"), so the reader's first move maps directly onto `UserGetUsersWithEmailAddress()`. 233 words (cap 250).

## Pending fact-checks

1. Break section, third-party share: TechTarget attributes "1,690 of the 2,098 known victim organizations were compromised via third parties" to "Callow" and the saved excerpt never gives his affiliation; the tally in the same article is Emsisoft's. The sentence now credits TechTarget. To close: confirm Callow's affiliation from the full article and restore "Emsisoft's analyst" if it holds.

## Result

- Argument as left: MOVEit's SQL injection was not a missing escape but an escape repeated per use with one use missed, reached through session state; bound parameters change that promise, and the four further SQL-injection CVEs Progress patched in five weeks show that fixing a function and removing a class are different jobs.
- Word count 2,302 → 2,408. Lede 120. Ledger 5 rows, verdicts unchanged.
- `./verify.sh 05`: 3 OWASP quotations, 0 not found; 51 markers, 51 rows, 0 mismatches, 0 open; 0 broken links; structure ok; PASS.
