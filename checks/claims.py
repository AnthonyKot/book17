#!/usr/bin/env python3
"""Every <!-- CHECK: id --> in a chapter has a row in checks/claims/*.tsv and vice versa;
rows still 'open' are reported (advisory). Per-chapter files so chapters can be drafted
in parallel. Row: chapter<TAB>id<TAB>claim<TAB>source<TAB>status. Optional filter: NN."""
import glob, os, re, sys
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.join(here, "..")
flt = next((a for a in sys.argv[1:] if re.fullmatch(r"\d\d", a)), None)
rows = {}
for tsv in sorted(glob.glob(os.path.join(here, "claims", "*.tsv"))):
    if flt and not os.path.basename(tsv).startswith(flt): continue
    for line in open(tsv, encoding="utf-8"):
        if not line.strip() or line.startswith("#"): continue
        f = line.rstrip("\n").split("\t")
        if len(f) < 5: print("  MALFORMED  %s: %s" % (os.path.basename(tsv), line[:60])); continue
        if f[1] in rows: print("  DUPLICATE  %s" % f[1])
        rows[f[1]] = f
markers = {}
for path in sorted(glob.glob(os.path.join(root, "chapters", "*.html"))):
    b = os.path.basename(path)
    if b.startswith("_") or (flt and not b.startswith(flt)): continue
    for m in re.findall(r"<!--\s*CHECK:\s*([A-Za-z0-9_.-]+)", open(path, encoding="utf-8").read()):
        markers.setdefault(m, []).append(b)
bad = 0
for m in sorted(set(markers) - set(rows)): print("  NO ROW     %s  (%s)" % (m, ", ".join(markers[m]))); bad += 1
for r in sorted(set(rows) - set(markers)): print("  NO MARKER  %s" % r); bad += 1
opens = [k for k, f in rows.items() if f[4].strip() == "open" and k in markers]
for k in sorted(opens): print("  OPEN       %s  %s" % (k, rows[k][2][:60]))
print("  %d marker(s), %d row(s), %d mismatch(es), %d open" % (len(markers), len(rows), bad, len(opens)))
sys.exit(1 if bad else 0)
