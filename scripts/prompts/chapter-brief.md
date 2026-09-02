# Chapter brief — draft chapter {{NN}} of *Ten Ways In* (repo: ~/book17)

You are drafting one chapter of a book. Everything you need is in the repo. Read, in this
order, before doing anything else: `CONTEXT.md` (all of it; §6 has your chapter's contract),
`AGENT.md`, `TEMPLATE.md`, `chapters/_shell.html`, `checks/claims/README.md`, and
`resources/owasp/A{{NN}}_*.txt` (your category's OWASP page; for chapter 00 read the
Introduction and Methodology files). Do not read other chapters unless they exist and
you need the nav links.

## What to produce (all files; nothing else in the repo is yours to edit)
1. `drafts/{{NN}}.pitches.md` — 2–4 candidate angles, ≤4 sentences each (anchor document,
   folk claim tested, defense set against the attack, reader's takeaway). Mark the one you
   chose and give a one-paragraph reason. Pilot mode: you pick; the user re-picks later.
2. `resources/sources/{{NN}}/SOURCES.md` — every document you rely on: URL, what it is
   (indictment / consent order / committee report / post-mortem / commit / mailing-list
   post / retelling), fetch date, and the page or section you used. Save plain-text
   excerpts of what you quote as `resources/sources/{{NN}}/<short-name>.txt` (government
   documents, OWASP, mailing lists, commits: excerpt freely; press: only the sentences
   you quote). Fetch the documents; do not work from memory. If a document cannot be
   fetched, say so in SOURCES.md and mark the dependent claims `open`.
3. `drafts/{{NN}}.ledger.md` — the ledger rows, written BEFORE the prose, 5–10 rows:
   folk claim (with the retelling it comes from) | record (document, page/section) |
   verdict from CONTEXT §4 exactly (HOLDS / OVERSTATED / WRONG / MISSING / OPEN).
   At least one row must be OVERSTATED, WRONG or MISSING, found honestly.
4. `checks/claims/{{NN}}.tsv` — one row per `<!-- CHECK: {{NN}}-… -->` marker in the chapter.
   Status `checked-by:<your-name>:2026-09-01` only if you read the source; else `open`.
5. `chapters/{{NN}}-<slug>.html` — the chapter, copied from `_shell.html`, on TEMPLATE.md's
   beats, 2,200–3,400 words, every section class present, the ledger as
   `<table class="ledger">` with `<td class="verdict">` cells (add class `v-holds`,
   `v-overstated`, `v-wrong`, `v-missing` or `v-open` to the cell). OWASP quotations go in
   `<q class="owasp" data-src="A{{NN}}">…</q>` and must be verbatim from the fetched
   text — the gate checks them. Nav links: previous/next chapter files may not exist
   yet; link to `../index.html` for both if so.

## Rules that override everything else
- Never false. No numbers from memory. Every incident-side fact gets a marker and a row.
- Fair to the named. Only what a document says a person did. Alleged is not found.
- Mechanism in the reader's hands: after the mechanism section a developer can draw the
  bug on a whiteboard. Quote historical public code where the record has it. Write no
  working exploit for anything still in service and no evasion recipe; explain, do not arm.
- Voice: plain, argued, no drama beyond the record. Paragraphs under 150 words; sentences
  under 40. No headers inside sections beyond the h2 the template gives.
- Defense side rests on a document. Where the record is thin, say so in the chapter.

## Save as you go (hard rule)
Sessions can die at the token limit. Write each artifact to disk the moment it is drafted;
write the chapter section by section and save after each. After each artifact lands, `git add`
only your own files (the paths above) and `git commit -m "WIP ch.{{NN}}: <what landed>"`; do
not push and do not add any other file. The coordinating session squashes and pushes.

## When done
Run `./verify.sh {{NN}}` from the repo root and fix anything it reports until the two
gating checks pass and the structure line for your chapter reads `ok`. Then write a
final report of ≤300 words: the angle you chose and why, the ledger verdicts, the claims
still `open` and why, anything you could not source, and the verify.sh output line for
your chapter. Do not edit `index.html`, `CONTEXT.md` or any file outside the paths above.
