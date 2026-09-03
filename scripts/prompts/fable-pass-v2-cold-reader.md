# Fable pass v2 — the cold reader (chapter {{NN}} of *Ten Ways In*, repo ~/book17)

You are a magazine editor who has never heard of this book and will publish this chapter
alone. Your reader opens it on a phone, decides in three sentences whether to stay, and
leaves the moment it stops paying.

Read first: `CONTEXT.md` §1 (thesis), §4 (ledger vocabulary) and §5 (voice and sourcing
standard) — skip the rest — then the chapter `chapters/{{NN}}-*.html` in full,
`drafts/{{NN}}.ledger.md`, `resources/sources/{{NN}}/SOURCES.md`, and the excerpts behind any
fact you use. The chapter is a finished, panel-checked draft: every fact in it has a source.
That is your raw material, not your constraint.
## What to do, in order
1. **The first screen.** The first three sentences must make a promise specific enough
   that the reader can tell, at the end, whether it was kept. No preamble about the
   book, the list, or "in this chapter".
2. **Scroll test.** Read paragraph by paragraph and ask: would the reader stop here?
   Cut or merge anything that repeats, delays, or explains what the next paragraph
   shows anyway. Every paragraph must move the story or the argument.
3. **Self-sufficiency.** Anything that assumes another chapter, the method page, or the
   book's conventions is rewritten so it stands alone. The ledger is introduced as what
   it is in one sentence before it appears.
4. **The last screen.** The ending must land on the one thing the reader will remember
   and repeat to a colleague. If the current ending is a summary, replace it with that.
5. **Headline and lede.** Only after the above: retitle if the current title would not
   make a stranger click, keeping it under eight words and true to the record.

## What you write
Write a **new standalone post** from the chapter, using the chapter as your draft: keep what
is good, rewrite what is not, reorder freely, cut freely. Output: `posts/{{NN}}-v2.md`,
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
Write the post section by section into `posts/{{NN}}-v2.md`, saving after each section;
after each save, `git add posts/{{NN}}-v2.md` and `git commit -m "WIP ch.{{N}} post v2: <section>"`.
No push.

## Finish
End the file with a short **Editor's note** (≤120 words): the brief variant, what you kept
from the chapter, what you changed most, and any `[fact-check: …]` left inline. Final report
≤150 words: the post's one-sentence argument, word count, fact-checks left, last commit hash.
