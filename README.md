# Ten Ways In

The OWASP Top 10:2025, one chapter per category, each told through a real break-in and a
real defense from the public record. Static HTML, no build step. `./verify.sh` gates.

- `CONTEXT.md` — authority document: thesis, corpus, spine, ledger vocabulary, chapter contracts, decision log
- `AGENT.md` — rules for the writing model; `TEMPLATE.md` — chapter beats
- `chapters/` — one HTML file per chapter (`_shell.html` is the template)
- `checks/` — `quotes.py` (OWASP quotes vs `resources/owasp/`), `claims.py` (markers vs `checks/claims/NN.tsv`), `structure.py`
- `resources/owasp/` — the spine as fetched; `resources/sources/NN/` — per-chapter primary documents
- `drafts/` — pitches, ledgers, `reviews/` from `scripts/review.sh NN`
- `scripts/draft-codex.sh NN` — fallback drafting lane using `scripts/prompts/chapter-brief.md`
