# Book 17 — chapter template (beats; structure.py enforces the section classes)

Kicker: `Chapter N · A0N:2025 <Category name>` (chapter 0: `Chapter 0 · How the list is made`)
H1: chapter title. **Lede** (`p.lede`): the moment the reader already knows from the
headlines, and the one detail from the record they don't. ≤120 words.

1. **The break** (`section.break`) — the incident from the record, in order, ~800–1,000
   words. Quote the documents. Every factual claim → `<!-- CHECK: id -->`. Name the folk
   story explicitly, with its source, somewhere in this section.
2. **The mechanism** (`section.mechanism`) — what the OWASP category means, in the
   reader's hands: the bug class, the minimal example (historical public code where it
   exists), why it is easy to write and hard to see. ~500–700 words. Quote OWASP's
   definition verbatim (gated).
3. **The defense** (`section.defense`) — the real defense set against this attack: what
   was in place and why it failed, or what was adopted afterward and what the record says
   it achieved. ~500–700 words. Say plainly where the defense record is thin.
4. **The ledger** (`table.ledger`) — 5–10 rows: `Folk story (source) | Record (document,
   page/section) | verdict` using CONTEXT §4 vocabulary exactly.
5. **What you can now see** (`section.see`) — ≤250 words. One thing the reader could
   look for in a system they run tomorrow. Not a checklist; one thing.
6. **Reading** (`div.reading`) — the OWASP page, the 2–4 primary documents, and the
   retelling that carries the folk story.
Nav (`nav.chapter-nav`): prev / contents / next.

Chapter shell: copy `chapters/_shell.html` — same header/footer/static paths as book15.
