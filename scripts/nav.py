#!/usr/bin/env python3
"""Rewrite every chapter's prev/next nav in READING order (ORDER below), not file order.
Ends of the sequence link to Contents. Idempotent; run after adding or reordering a chapter.
The reading order was set on 2026-09-03 from drafts/reviews/virality-order.md; chapter
numbers remain the OWASP category numbers."""
import glob, os, re
ORDER = ["00", "07", "08", "04", "10", "01", "09", "02", "03", "06", "05"]
root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
byno = {os.path.basename(f)[:2]: f for f in glob.glob(os.path.join(root, "chapters", "[0-9]*.html"))}
missing = [n for n in ORDER if n not in byno]; extra = [n for n in byno if n not in ORDER]
assert not missing and not extra, (missing, extra)
files = [byno[n] for n in ORDER]
for i, f in enumerate(files):
    prev = '<a href="%s">← Previous</a>' % os.path.basename(files[i-1]) if i > 0 else '<span></span>'
    nxt = '<a href="%s">Next →</a>' % os.path.basename(files[i+1]) if i+1 < len(files) else '<span></span>'
    nav = '<nav class="chapter-nav">\n  %s\n  <a href="../index.html">Contents</a>\n  %s\n</nav>' % (prev, nxt)
    s = open(f, encoding="utf-8").read()
    s2 = re.sub(r'<nav class="chapter-nav">.*?</nav>', nav, s, flags=re.S)
    if s2 != s: open(f, "w", encoding="utf-8").write(s2); print("  rewrote", os.path.basename(f))
