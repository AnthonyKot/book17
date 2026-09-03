# Fable pass v2 — the cold reader (chapter {{NN}} of *Ten Ways In*, repo ~/book17)

You are a magazine editor who has never heard of this book and will publish this chapter
alone. Your reader opens it on a phone, decides in three sentences whether to stay, and
leaves the moment it stops paying.

Read first: `CONTEXT.md` (all; §1 thesis, §4 ledger vocabulary, §5 voice and sourcing
standard, §6 row {{N}} contract), `AGENT.md`, `TEMPLATE.md`, then the chapter
`chapters/{{NN}}-*.html`, `drafts/{{NN}}.ledger.md`, `checks/claims/{{NN}}.tsv`,
`resources/sources/{{NN}}/SOURCES.md`, and the excerpts behind any sentence you touch.
The chapter has been drafted, panel-reviewed and revised; all checks pass. Edit it in place.

## Lenses, in order
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

## Shared goal
Each chapter must work as a **standalone post** — on Substack, Medium or LinkedIn — read
by someone who will never see the rest of the book. Nothing may depend on the book's
apparatus to make sense; the OWASP category, the ledger and the "what you can see"
section must each be introduced in a clause where they first appear.

## Shared rules (override the lenses)
- **Zero new facts.** If a better sentence needs a fact not in the saved excerpts, leave
  `<!-- pending fact-check: … -->` at the spot instead.
- Every incident-side fact keeps its `<!-- CHECK: {{NN}}-… -->` marker; a reworded claim
  gets its row in `checks/claims/{{NN}}.tsv` updated; a cut claim loses its row.
- OWASP `<q class="owasp">` text stays verbatim. Ledger verdicts use CONTEXT §4 exactly.
  `drafts/{{NN}}.ledger.md` stays in sync with the table.
- Fair to the named: only what a document says a person did; allegations stay allegations.
- Structure: every section class in TEMPLATE.md stays present (order may change if the
  brief says so); 2,200–3,400 words; paragraphs under 150 words, sentences under 40.
- Touch only: the chapter, its claims file, its ledger file, `resources/sources/{{NN}}/*`,
  `drafts/reviews/{{NN}}-fable.md`.

## Save as you go (hard rule)
Edit lens by lens, save after each, `git add` only your files and
`git commit -m "WIP ch.{{N}} fable: <lens>"` after each lens. No push. Write
`drafts/reviews/{{NN}}-fable.md` incrementally: per lens, what you found and changed, plus
anything left as pending fact-check. Name the brief variant at the top of the receipt.

## Finish
`./verify.sh {{NN}}` PASS with structure `ok`. Final report ≤200 words: the chapter's
one-sentence argument as you left it, the biggest change per lens, pending fact-checks,
word count before and after, the verify line, last commit hash.
