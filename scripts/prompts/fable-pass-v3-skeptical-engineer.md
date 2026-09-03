# Fable pass v3 — the skeptical engineer (chapter {{NN}} of *Ten Ways In*, repo ~/book17)

Your reader is a senior engineer reading on a lunch break, who has seen a dozen breach
write-ups and expects to learn nothing. Every paragraph must give them either something
they can use on Monday or an argument they would want to contest. Nothing else survives.

Read first: `CONTEXT.md` (all; §1 thesis, §4 ledger vocabulary, §5 voice and sourcing
standard, §6 row {{N}} contract), `AGENT.md`, `TEMPLATE.md`, then the chapter
`chapters/{{NN}}-*.html`, `drafts/{{NN}}.ledger.md`, `checks/claims/{{NN}}.tsv`,
`resources/sources/{{NN}}/SOURCES.md`, and the excerpts behind any sentence you touch.
The chapter has been drafted, panel-reviewed and revised; all checks pass. Edit it in place.

## Lenses, in order
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
