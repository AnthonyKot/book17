#!/usr/bin/env bash
# Book 17 — standing verification. ./verify.sh [NN] [--strict]
#
#   checks/quotes.py     every OWASP quotation is in the fetched spine      GATING
#   checks/claims.py     every incident claim marker has a row, and back   GATING (open rows: advisory)
#   internal links       entirely inside this repo                          GATING
#   count sync           contents page vs chapters on disk                  GATING
#   checks/structure.py  TEMPLATE beats, word bounds, wall paragraphs       ADVISORY (--strict gates)
#
# What a green run proves: every OWASP line quoted is OWASP's; every incident claim has a
# named source. It does NOT prove the source says what we say it says — that is the
# panel's job and the reader's, not this script's.
set -u
cd "$(dirname "$0")"
fail=0; FILTER=""; STRICT=""
for a in "$@"; do case "$a" in --strict) STRICT=--strict;; *) FILTER="$a";; esac; done
echo "== OWASP quotations vs spine (gating) =="; python3 checks/quotes.py $FILTER || fail=1
echo "== incident claim markers vs register (gating) =="; python3 checks/claims.py $FILTER || fail=1
echo "== count sync =="
files=$(ls chapters/[0-9]*.html 2>/dev/null | wc -l | tr -d ' ')
links=$(grep -oE 'href="chapters/[0-9][^"]*\.html"' index.html 2>/dev/null | sort -u | wc -l | tr -d ' ')
echo "  $files chapter files on disk; $links linked from index.html"
[ "$files" = "$links" ] || { echo "  FAIL"; fail=1; }
echo "== internal links (gating) =="
python3 - <<'PY' || fail=1
import glob, os, re, sys
bad = 0
for f in glob.glob('**/*.html', recursive=True):
    if os.path.basename(f).startswith('_'): continue
    for m in re.findall(r'(?:href|src)="([^"#?:]+)"', open(f, encoding='utf-8').read()):
        if m.startswith(('http', '//', 'mailto')): continue
        if not os.path.exists(os.path.normpath(os.path.join(os.path.dirname(f), m))):
            print("  BROKEN  %s -> %s" % (f, m)); bad += 1
print("  %d broken link(s)" % bad); sys.exit(1 if bad else 0)
PY
echo "== structure (advisory) =="; python3 checks/structure.py $FILTER $STRICT || fail=1
[ $fail = 0 ] && echo "PASS" || { echo "FAIL"; exit 1; }
