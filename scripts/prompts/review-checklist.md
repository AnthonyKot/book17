You are reviewing one chapter of a book that tells each category of the OWASP Top 10:2025
through one real break-in and one real defense, from the public record. Read CONTEXT.md
§1, §4–6 and AGENT.md in the repo first. Then read the chapter HTML you were given, its
claims file (checks/claims/NN.tsv) and its sources index (resources/sources/NN/SOURCES.md).

Report findings only — no praise, no summary. For each finding: location (quote a phrase),
the problem, and what would fix it. Rank by severity.

Check, in this order:
1. **Record accuracy.** For every <!-- CHECK --> claim, does the cited source actually say
   that? Open the source excerpts in resources/sources/NN/ (and the URL if you can). Name
   every claim you would challenge and why. A claim that overstates its source is the
   worst finding in this book.
2. **Fairness to named people.** Does the chapter attribute motive, competence or
   knowledge to anyone beyond what a document states? Does it say "charged" where it
   should say "convicted", or "found" where it should say "alleged"?
3. **Mechanism accuracy.** Is the technical explanation of the bug class right? Is the
   minimal example correct? Would a security engineer wince anywhere? Could a reader draw
   it on a whiteboard afterward?
4. **Ledger fairness.** Is each folk claim real (sourced to a named retelling) or a straw
   man? Is each verdict earned by the cited document? Is any MISSING row really the folk
   story being slightly short rather than missing something a defender needed?
5. **Defense record.** Does the defense section rest on a document, or on the author's
   sense that the defense would have worked? Where the record is thin, does the chapter
   say so?
6. **Capability leak.** Does anything here function as a recipe against a live system
   rather than an explanation of a historical one? Flag it.
7. **OWASP fit.** Does the chapter quote the category definition, and does it say where
   the incident does not fit the category cleanly?
8. **Reader.** Would a developer who thinks the OWASP list is compliance theatre come out
   of this chapter able to see the mechanism in their own code — or only entertained?
9. **Readability.** Wall paragraphs, sentences that need re-reading, and any place the
   drama outruns the record.
