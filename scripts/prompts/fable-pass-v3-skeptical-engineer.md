# Fable pass v3 — the skeptical engineer (chapter {{NN}} of *Ten Ways In*, repo ~/book17)

Your reader is a senior engineer reading on a lunch break, who has seen a dozen breach
write-ups and expects to learn nothing. Every paragraph must give them either something
they can use on Monday or an argument they would want to contest. Nothing else survives.

Read first: `CONTEXT.md` §1 (thesis), §4 (ledger vocabulary) and §5 (voice and sourcing
standard) — skip the rest — then the chapter `chapters/{{NN}}-*.html` in full,
`drafts/{{NN}}.ledger.md`, `resources/sources/{{NN}}/SOURCES.md`, and the excerpts behind any
fact you use. The chapter is a finished, panel-checked draft: every fact in it has a source.
That is your raw material, not your constraint.
## What to do, in order
1. **The claim they'd contest.** Find the chapter's sharpest contestable claim (usually
   in the ledger or the defense section) and make sure it is stated plainly, early, with
   the record behind it in the same paragraph.
2. **Mechanism first.** The mechanism section must let them draw the bug on a whiteboard
   and see exactly which line, default or decision failed. Cut narrative that delays it;
   cut explanation that shows nothing. Code stays honest about what it abridges.
3. **The defense as a spec.** The defense section must name what was actually deployed,
   by whom, with which document, and what it did not cover. "Should" is not a defense.
   Any sentence that recommends without a record is cut or turned into a question.
4. **Kill the history lesson.** Dates, names and quotations that do not change what the
   engineer would do are cut. Keep the ones that do.
5. **Monday.** The closing section becomes a concrete check they can run this week on a
   system they own, phrased as an instruction, with what a bad result looks like.

## What you write
Write a **new standalone post** from the chapter, using the chapter as your draft: keep what
is good, rewrite what is not, reorder freely, cut freely. Output: `posts/{{NN}}-v3.md`,
Markdown, with a title line, suitable to paste into Substack, Medium or LinkedIn as-is.
Length is yours to judge for the platform (roughly 1,500–3,000 words). Read by someone who
will never see the rest of the book: nothing may depend on the book's apparatus; introduce
the OWASP category, the folk-vs-record ledger and the closing check in a clause where each
first appears. Keep a ledger in some form — it is the book's signature — but its shape (a
table, a run of short paragraphs, a numbered list) is yours.

## The one rule that stays
**Never false, no new facts.** Every fact about the incident and the defense must come from
the saved excerpts in `resources/sources/{{NN}}/` or the chapter's quoted documents. If a
better sentence needs a fact you do not have, write the sentence without it or leave
`[fact-check: …]` inline. Fair to the named: only what a document says a person did;
allegations stay allegations. OWASP quotations verbatim. Do not touch the chapter file, the
claims register, the ledger file, `index.html` or `CONTEXT.md`.

## Save as you go (hard rule)
Write the post section by section into `posts/{{NN}}-v3.md`, saving after each section;
after each save, `git add posts/{{NN}}-v3.md` and `git commit -m "WIP ch.{{N}} post v3: <section>"`.
No push.

## Finish
End the file with a short **Editor's note** (≤120 words): the brief variant, what you kept
from the chapter, what you changed most, and any `[fact-check: …]` left inline. Final report
≤150 words: the post's one-sentence argument, word count, fact-checks left, last commit hash.
