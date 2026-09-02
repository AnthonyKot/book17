#!/usr/bin/env python3
"""Rewrite every chapter's prev/next nav from the chapters on disk, in file order.
Ends of the sequence link to Contents. Idempotent; run after adding a chapter."""
import glob, os, re
root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
files = sorted(f for f in glob.glob(os.path.join(root, "chapters", "[0-9]*.html")))
for i, f in enumerate(files):
    prev = '<a href="%s">← Previous</a>' % os.path.basename(files[i-1]) if i > 0 else '<span></span>'
    nxt = '<a href="%s">Next →</a>' % os.path.basename(files[i+1]) if i+1 < len(files) else '<span></span>'
    nav = '<nav class="chapter-nav">\n  %s\n  <a href="../index.html">Contents</a>\n  %s\n</nav>' % (prev, nxt)
    s = open(f, encoding="utf-8").read()
    s2 = re.sub(r'<nav class="chapter-nav">.*?</nav>', nav, s, flags=re.S)
    if s2 != s: open(f, "w", encoding="utf-8").write(s2); print("  rewrote", os.path.basename(f))
