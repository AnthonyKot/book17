#!/usr/bin/env python3
"""OWASP quotation gate: every <q class="owasp" data-src="A01">…</q> in a chapter must appear
verbatim (whitespace/quote-normalised) in resources/owasp/<data-src>*.txt. Gating: the
spine is a fixed fetch, nothing upstream can drift without the fetch changing."""
import glob, html, os, re, sys, unicodedata
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.join(here, "..")
flt = next((a for a in sys.argv[1:] if re.fullmatch(r"\d\d", a)), None)
def norm(s):
    s = unicodedata.normalize("NFKC", html.unescape(s))
    s = re.sub(r"[‘’]", "'", s); s = re.sub(r"[“”]", '"', s)
    s = re.sub(r"[–—]", "-", s)
    return re.sub(r"\s+", " ", s).strip().lower()
corpus = {}
for f in glob.glob(os.path.join(root, "resources", "owasp", "*.txt")):
    corpus[os.path.basename(f).split("_")[0]] = norm(open(f, encoding="utf-8").read())
bad = n = 0
for path in sorted(glob.glob(os.path.join(root, "chapters", "*.html"))):
    b = os.path.basename(path)
    if b.startswith("_") or (flt and not b.startswith(flt)): continue
    for src, body in re.findall(r'<q class="owasp" data-src="([^"]+)">(.*?)</q>', open(path, encoding="utf-8").read(), re.S):
        n += 1; q = norm(re.sub(r"<[^>]+>", "", body))
        if src not in corpus: print("  NO CORPUS  %s  %s" % (src, b)); bad += 1
        elif q not in corpus[src]: print("  NOT FOUND  %s  %s: %s" % (src, b, q[:70])); bad += 1
print("  %d OWASP quotation(s), %d not found" % (n, bad))
sys.exit(1 if bad else 0)
