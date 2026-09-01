# AGENT.md — instructions for the writing model (book 17)

## Who is reading
A developer or engineering manager who has shipped web software, has heard of the OWASP
Top 10 and suspects it is compliance theatre, and has read the headlines about the big
breaches. They will not read a court filing themselves — the chapter must carry enough of
the record, quoted, that they don't need to. They will check a claim that looks too neat,
and they will notice if the mechanism is hand-waved.

## Priority stack (higher wins on conflict)
1. **Never false.** Every incident-side fact receipted (`<!-- CHECK: id -->` + claims row).
   OWASP quoted verbatim and gated. No numbers from memory. Being dull is a failure;
   being wrong is a betrayal.
2. **Fair to the named.** People appear as the record names them, doing what the record
   says. No motive, no character, no "should have known" unless a document says it.
3. **Mechanism in the reader's hands.** After the chapter the reader can explain the bug
   class to a colleague on a whiteboard and recognise it in a code review. If the
   mechanism section could be skipped without losing the story, it is too thin.
4. **The folk story is never the whole story.** Every ledger must contain at least one
   OVERSTATED, WRONG or MISSING row, found honestly in the record. If the folk story
   genuinely HOLDS on every point, the chapter says so and the panel is told to attack it.
5. **Understanding, not capability.** Historical public code is quoted; no working
   exploit for anything still in service; no evasion or credential material. If a detail
   would help an attacker more than a reader, describe it, don't show it.

## Incident rules
- Identify the folk story from named retellings (cite them — Wired, Krebs, the Wikipedia
  lede) so the ledger's left column is real, not a straw man.
- Prefer the document closest to the event: indictment over news report, vendor
  post-mortem over analyst summary, commit over blog post about the commit.
- Save what you rely on: `resources/sources/NN/SOURCES.md` lists every document with
  URL, what it is, fetch date, and the page/section used. Plain-text excerpts go alongside
  where the licence allows (government documents, OWASP, mailing lists, commits: yes;
  paywalled press: excerpt only what is quoted).
- Defense side: find the *record* of the defense — the changelog that changed a default,
  the published measurement, the post-incident review that says what was adopted. If none
  exists, say the defense record is thin and what would fill it. Never manufacture a
  success.
- A thing being *alleged* (complaint, lawsuit, press) is not the thing being *found*
  (verdict, consent order, admitted post-mortem). Receipt exactly what the document is.
- The OWASP category text is the chapter's frame: quote its definition and its
  "how to prevent" list where the chapter meets them, and note where the incident does
  not fit the category cleanly (Colonial, NotPetya, CrowdStrike are not web apps).

## Pitch before writing (the guinea-pig gate)
Never drafted cold. For each chapter, 2–4 candidate angles of ≤4 sentences each: the
document that anchors it, the folk claim it tests, the defense it sets against the attack,
and the reader's takeaway. Standard mode: the user picks, the rest are banked in
`drafts/NN.pitches.md`. **Pilot mode (chapters 1, 3, 10, 2026-09-01):** the drafting agent
picks with a stated reason, drafts, and banks the alternates; the user re-picks after
reading.

## Check the chosen pitch against the CONTEXT §6 contract before drafting
The pitch does not amend the authority document. If the angle covers less than §6
requires, widen the chapter or record an amendment in §8 first.

## Write the ledger before the prose
The rows are the argument; prose that precedes them rationalises. Draft
`drafts/NN.ledger.md` first, then the chapter.

## After any prose edit
Re-run `./verify.sh NN`. A claim you introduced and never registered is invisible to the
gate. Read the structure report for wall paragraphs.

## Pre-ship test (all six or don't ship)
1. Could a reader disagree with *our reading* of the record from the quotes alone?
2. Is there a real OVERSTATED / WRONG / MISSING row, argued, not token?
3. Is every incident claim marked and its row non-`open`?
4. Whiteboard test: can the reader now draw the mechanism?
5. Would the named people's lawyers and the named people's critics both call the chapter
   fair? (Panel question.)
6. Dinner test: can the reader say in one sentence what the folk story got wrong here,
   without saying "it's always more complicated"?

## Panel (review)
`scripts/review.sh NN` — two Gemini reviewers via agy review independently against
`scripts/prompts/review-checklist.md`; codex consolidates and is adversarial toward *their*
findings. Always check output size. Findings go to `drafts/reviews/NN-*.md`; the chapter
is revised; the correction is logged in CONTEXT §8.
