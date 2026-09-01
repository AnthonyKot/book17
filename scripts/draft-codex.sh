#!/usr/bin/env bash
# scripts/draft-codex.sh NN — have codex draft chapter NN from the self-contained brief.
# Fallback lane when the primary drafting model declines a chapter. Needs network for
# sources, so the sandbox is danger-full-access; stdin redirect is mandatory (codex hangs
# on stdin otherwise).
set -uo pipefail
cd "$(dirname "$0")/.."
n="${1:?chapter number, e.g. 01}"
brief="$(sed "s/{{NN}}/$n/g" scripts/prompts/chapter-brief.md)"
mkdir -p drafts/reviews
codex exec --skip-git-repo-check -m gpt-5.6-sol -s danger-full-access -C "$(pwd)" "$brief" < /dev/null > "drafts/$n.codex-draft.log" 2>&1
echo "log in drafts/$n.codex-draft.log"; ls -la chapters/${n}-*.html drafts/$n.* checks/claims/$n.tsv 2>/dev/null
