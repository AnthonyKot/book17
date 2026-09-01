#!/usr/bin/env python3
"""Structural lint: TEMPLATE.md beats present, word bounds, chapter nav, and the
readability tail — paragraphs over PARA_MAX words and sentences over SENT_MAX.
Advisory unless --strict. It cannot tell a fair ledger from an unfair one."""
import glob, html, os, re, sys
CEILING, FLOOR, PARA_MAX, SENT_MAX = 3400, 2200, 150, 40
REQUIRED = {
    "lede": r'<p class="lede">', "break section": r'<section class="break">',
    "mechanism section": r'<section class="mechanism">', "defense section": r'<section class="defense">',
    "ledger": r'<table class="ledger">', "see section": r'<section class="see">',
    "reading box": r'<div class="reading">', "chapter nav": r'<nav class="chapter-nav">',
}
VERDICTS = {"HOLDS", "OVERSTATED", "WRONG", "MISSING", "OPEN"}
strict = "--strict" in sys.argv
flt = next((a for a in sys.argv[1:] if re.fullmatch(r"\d\d", a)), None)
root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
bad = 0
for path in sorted(glob.glob(os.path.join(root, "chapters", "*.html"))):
    name = os.path.basename(path)
    if name.startswith("_") or (flt and not name.startswith(flt)): continue
    raw = open(path, encoding="utf-8").read()
    body = re.sub(r"(?is)<(script|style|head|header|footer|nav|pre|table).*?</\1>", " ", raw)
    body = re.sub(r"(?is)<div class=\"reading\">.*?</div>", " ", body)
    text = lambda s: html.unescape(re.sub(r"<[^>]+>", " ", s))
    words = len(text(body).split())
    probs = [k for k, rx in REQUIRED.items() if not re.search(rx, raw)]
    if not FLOOR <= words <= CEILING: probs.append("%d words (bounds %d-%d)" % (words, FLOOR, CEILING))
    walls = []; longs = 0
    for p in re.findall(r"(?is)<p[^>]*>(.*?)</p>", body):
        t = text(p); w = len(t.split())
        if w > PARA_MAX: walls.append(w)
        longs += sum(1 for s in re.split(r"(?<=[.!?])\s+", t) if len(s.split()) > SENT_MAX)
    if walls: probs.append("wall paragraph(s): %s words" % ", ".join(map(str, sorted(walls, reverse=True))))
    if longs: probs.append("%d sentence(s) over %d words" % (longs, SENT_MAX))
    if "ledger" not in " ".join(probs):
        cells = re.findall(r"(?is)<td[^>]*class=\"verdict[^\"]*\"[^>]*>(.*?)</td>", raw)
        badv = [text(c).strip() for c in cells if text(c).strip().split()[0].upper() if text(c).strip() and text(c).strip().split()[0].upper() not in VERDICTS]
        if not cells: probs.append("no <td class=\"verdict…\"> cells")
        if badv: probs.append("bad verdict(s): %s" % ", ".join(badv[:3]))
        rows = len(cells)
        if cells and not 5 <= rows <= 10: probs.append("%d ledger rows (5-10)" % rows)
    if probs: bad += 1; print("  %-40s %s" % (name, "; ".join(probs)))
    else: print("  %-40s ok (%d words)" % (name, words))
sys.exit(1 if (bad and strict) else 0)
