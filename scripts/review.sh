#!/usr/bin/env bash
# scripts/review.sh NN — panel review of chapters/NN-*.html.
# Two Gemini reviewers via agy review independently; codex (gpt-5.6-sol) consolidates,
# adversarial toward their findings. Outputs: drafts/reviews/NN-{flash,pro,codex}.md.
# Either agy run may return zero bytes (known intermittent failure) — fine if two of three
# produced text. `--codex-only` skips agy and has codex review directly.
set -uo pipefail
cd "$(dirname "$0")/.."
n="${1:?chapter number, e.g. 01}"; shift || true
f=$(ls chapters/${n}-*.html 2>/dev/null | head -1); [ -n "$f" ] || { echo "no chapters/${n}-*.html"; exit 1; }
out=drafts/reviews; mkdir -p "$out"
prompt="$(cat scripts/prompts/review-checklist.md)

The chapter file is: $f  (repo root: $(pwd); NN=$n). Write your findings as markdown."

if [ "${1:-}" != "--codex-only" ]; then
  echo "== agy flash"; agy --dangerously-skip-permissions --print-timeout 14m --model gemini-3.7-flash-high -p "$prompt" > "$out/$n-flash.md" 2>"$out/$n-flash.err" &
  echo "== agy pro";   agy --dangerously-skip-permissions --print-timeout 14m --model gemini-3.1-pro-high  -p "$prompt" > "$out/$n-pro.md"   2>"$out/$n-pro.err" &
  wait
  for r in flash pro; do printf '  %-5s %6s bytes\n' $r "$(wc -c < "$out/$n-$r.md")"; done
  cons="Two reviewers assessed $f independently; their reports are in $out/$n-flash.md and $out/$n-pro.md (either may be empty).
Read CONTEXT.md, AGENT.md, the chapter, checks/claims/$n.tsv, resources/sources/$n/, and both reports. Be adversarial toward
the REVIEWERS: for each of their findings, verify it against the chapter and the sources and mark it CONFIRMED / REJECTED
(with why) / UNVERIFIABLE. Then add findings they both missed, using the checklist in scripts/prompts/review-checklist.md.
Output one consolidated markdown report, ranked, with a one-line ship / revise / block verdict at the top."
else
  cons="$prompt"
fi
echo "== codex"; codex exec --skip-git-repo-check -m gpt-5.6-sol -C "$(pwd)" "$cons" < /dev/null > "$out/$n-codex.md" 2>"$out/$n-codex.err"
printf '  codex %6s bytes\n' "$(wc -c < "$out/$n-codex.md")"
echo "reports in $out/"
