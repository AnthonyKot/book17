# Fable pass — author's review-and-edit of chapter {{NN}} of *Ten Ways In* (repo ~/book17)

The chapter `chapters/{{NN}}-*.html` has been drafted, panel-reviewed and revised; all checks
pass. This is the pass a human author does last: read it as a reader, then write the post
it should have been, **without adding a single fact**.

Read first: `CONTEXT.md` §1 (thesis), §4 (ledger vocabulary) and §5 (voice and sourcing
standard) — skip the rest — then the chapter `chapters/{{NN}}-*.html` in full,
`drafts/{{NN}}.ledger.md`, `resources/sources/{{NN}}/SOURCES.md`, and the excerpts behind any
fact you use. The chapter is a finished, panel-checked draft: every fact in it has a source.
That is your raw material, not your constraint.
## What to do, in order
1. **Argument.** One argument a reader can restate in a sentence. The lede promises what
   the ending delivers. Each section earns its place or is cut.
2. **Mechanism in the reader's hands.** After the mechanism section a developer can draw
   the bug on a whiteboard. Code and pseudocode are honest about what they abridge. Cut
   what explains without showing.
3. **Ledger and record.** Every verdict is earned by the record cell beside it; every folk
   claim is a real quoted retelling; one claim per row. Weaken any sentence the saved
   excerpt does not support. Fair to the named: only what a document says a person did;
   allegations stay allegations.
4. **Prose.** Plain, argued, no drama beyond the record. Cut hedges said twice, counting
   openers, throat-clearing, any sentence a reader would skip. Vary paragraph rhythm.
   Paragraphs under 150 words, sentences under 40. No new headers.
5. **Reader's exit.** The closing "what you can now see" is something a reader can do in a
   system they run this week, not a moral.

## What you write
Write a **new standalone post** from the chapter, using the chapter as your draft: keep what
is good, rewrite what is not, reorder freely, cut freely. Output: `posts/{{NN}}-v1.md`,
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
Write the post section by section into `posts/{{NN}}-v1.md`, saving after each section;
after each save, `git add posts/{{NN}}-v1.md` and `git commit -m "WIP ch.{{N}} post v1: <section>"`.
No push.

## Finish
End the file with a short **Editor's note** (≤120 words): the brief variant, what you kept
from the chapter, what you changed most, and any `[fact-check: …]` left inline. Final report
≤150 words: the post's one-sentence argument, word count, fact-checks left, last commit hash.
