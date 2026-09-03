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
