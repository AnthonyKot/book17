# Fable pass — author's review-and-edit of chapter {{NN}} of *Ten Ways In* (repo ~/book17)

The chapter `chapters/{{NN}}-*.html` has been drafted, panel-reviewed and revised; all checks
pass. This is the pass a human author does last: read it as a reader, then edit it in place
so it is the best chapter it can be **without adding a single fact**.

Read first: `CONTEXT.md` (all; §1 thesis, §4 ledger vocabulary, §5 voice and sourcing
standard, §6 row {{N}} contract), `AGENT.md`, `TEMPLATE.md`, one other finished chapter for
register, then the chapter, `drafts/{{NN}}.ledger.md`, `checks/claims/{{NN}}.tsv`,
`resources/sources/{{NN}}/SOURCES.md`, and the excerpts behind any sentence you touch.

## Five lenses, in this order
1. **Argument.** One argument a reader can restate in a sentence. The lede promises what
   the ending delivers. Each section earns its place on TEMPLATE.md's beats or is cut.
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

## Rules
- Zero new facts. If a better sentence needs a fact not in the excerpts, leave
  `<!-- pending fact-check: … -->` at the spot instead.
- Every incident-side fact keeps its `<!-- CHECK: {{NN}}-… -->` marker; reworded claims get
  their row in `checks/claims/{{NN}}.tsv` updated; cut claims lose their row.
- OWASP `<q class="owasp">` text stays verbatim. `drafts/{{NN}}.ledger.md` stays in sync
  with the table.
- Touch only: the chapter, its claims file, its ledger file, `resources/sources/{{NN}}/*`,
  `drafts/reviews/{{NN}}-fable.md`.

## Save as you go (hard rule)
Edit lens by lens, save after each, `git add` only your files and
`git commit -m "WIP ch.{{N}} fable: <lens>"` after each lens. No push. Write
`drafts/reviews/{{NN}}-fable.md` incrementally: per lens, what you found and what you
changed, plus anything left as pending fact-check.

## Finish
`./verify.sh {{NN}}` PASS with structure `ok`. Final report ≤200 words: the chapter's
one-sentence argument as you left it, the biggest change per lens, pending fact-checks,
word count before and after, the verify line, last commit hash.
