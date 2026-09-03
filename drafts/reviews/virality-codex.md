# LinkedIn virality estimate

| Chapter | Title | Recognition | Reversal | Takeaway | Audience fit | One-line hook | Composite | Post's first line |
|---:|---|---:|---:|---:|---:|---:|---:|---|
| 00 | A Ranking of Tested Applications | 5 | 5 | 4 | 5 | 5 | 4.80 | The OWASP Top 10 is not a prevalence ranking: two slots are survey picks, and even the data-driven eight use maximum CWE incidence rather than category prevalence. |
| 01 | Three Commands and a Role | 5 | 4 | 5 | 5 | 5 | 4.70 | Capital One's famous “SSRF breach” is not confirmed by any public court record—and the provable failure was a WAF role allowed to do work it never needed. |
| 02 | Three Defaults, Not One | 4 | 5 | 5 | 5 | 5 | 4.75 | MongoDB did not wait for the 2017 ransom wave to ship a safe default: its official packages had bound to localhost since 2014, while the binary still did not. |
| 03 | The Tarball Was Not the Tree | 4 | 5 | 5 | 4 | 5 | 4.60 | The xz backdoor was not in the Git tree everyone reviewed; its trigger existed only in the signed release tarballs distributions built. |
| 04 | The Backup That Outlived the Fix | 4 | 5 | 5 | 4 | 5 | 4.60 | Adobe had already migrated to salted password hashes—the attackers stole the reversibly encrypted backup kept in case the migration failed. |
| 05 | One Function, Three Patches | 4 | 4 | 5 | 5 | 5 | 4.45 | MOVEit's May patch fixed the exploited SQL injection, but four more SQL-injection CVEs followed in five weeks. |
| 06 | What “Turn Off GPS” Left Out | 5 | 3 | 4 | 4 | 4 | 3.95 | Strava's heatmap did not leak private workouts; correctly processed public data exposed bases because sparse regions made a few routes visible. |
| 07 | Not Intended to Be in Use | 5 | 4 | 5 | 5 | 5 | 4.70 | Colonial Pipeline was not breached through an inactive account; it was breached through a legacy VPN path the company believed was disabled but still accepted a password. |
| 08 | The Backup That Was Not a Backup | 5 | 5 | 5 | 5 | 5 | 5.00 | Maersk's synchronized domain controllers were replicas, not backups; recovery depended on finding one live copy outside the blast radius. |
| 09 | Between Alert and Action | 5 | 4 | 5 | 5 | 5 | 4.70 | The Target story is not that nobody saw the alert: Target testified that some intruder activity was surfaced and evaluated, while the public record cannot show what happened next. |
| 10 | One Line Too Many, One Field Too Few | 5 | 5 | 5 | 5 | 5 | 5.00 | Apple's TLS bug silently returned success while CrowdStrike's sensor crashed the host—two famous incidents caused by error paths failing in opposite directions. |

## Ranked by composite

1. Chapter 08 — *The Backup That Was Not a Backup* — 5.00
1. Chapter 10 — *One Line Too Many, One Field Too Few* — 5.00
3. Chapter 00 — *A Ranking of Tested Applications* — 4.80
4. Chapter 02 — *Three Defaults, Not One* — 4.75
5. Chapter 01 — *Three Commands and a Role* — 4.70
5. Chapter 07 — *Not Intended to Be in Use* — 4.70
5. Chapter 09 — *Between Alert and Action* — 4.70
8. Chapter 03 — *The Tarball Was Not the Tree* — 4.60
8. Chapter 04 — *The Backup That Outlived the Fix* — 4.60
10. Chapter 05 — *One Function, Three Patches* — 4.45
11. Chapter 06 — *What “Turn Off GPS” Left Out* — 3.95

## Scores as JSON

```json
{
  "00": {"recognition": 5, "reversal": 5, "takeaway": 4, "fit": 5, "hook": 5, "line": "The OWASP Top 10 is not a prevalence ranking: two slots are survey picks, and even the data-driven eight use maximum CWE incidence rather than category prevalence."},
  "01": {"recognition": 5, "reversal": 4, "takeaway": 5, "fit": 5, "hook": 5, "line": "Capital One's famous ‘SSRF breach’ is not confirmed by any public court record—and the provable failure was a WAF role allowed to do work it never needed."},
  "02": {"recognition": 4, "reversal": 5, "takeaway": 5, "fit": 5, "hook": 5, "line": "MongoDB did not wait for the 2017 ransom wave to ship a safe default: its official packages had bound to localhost since 2014, while the binary still did not."},
  "03": {"recognition": 4, "reversal": 5, "takeaway": 5, "fit": 4, "hook": 5, "line": "The xz backdoor was not in the Git tree everyone reviewed; its trigger existed only in the signed release tarballs distributions built."},
  "04": {"recognition": 4, "reversal": 5, "takeaway": 5, "fit": 4, "hook": 5, "line": "Adobe had already migrated to salted password hashes—the attackers stole the reversibly encrypted backup kept in case the migration failed."},
  "05": {"recognition": 4, "reversal": 4, "takeaway": 5, "fit": 5, "hook": 5, "line": "MOVEit's May patch fixed the exploited SQL injection, but four more SQL-injection CVEs followed in five weeks."},
  "06": {"recognition": 5, "reversal": 3, "takeaway": 4, "fit": 4, "hook": 4, "line": "Strava's heatmap did not leak private workouts; correctly processed public data exposed bases because sparse regions made a few routes visible."},
  "07": {"recognition": 5, "reversal": 4, "takeaway": 5, "fit": 5, "hook": 5, "line": "Colonial Pipeline was not breached through an inactive account; it was breached through a legacy VPN path the company believed was disabled but still accepted a password."},
  "08": {"recognition": 5, "reversal": 5, "takeaway": 5, "fit": 5, "hook": 5, "line": "Maersk's synchronized domain controllers were replicas, not backups; recovery depended on finding one live copy outside the blast radius."},
  "09": {"recognition": 5, "reversal": 4, "takeaway": 5, "fit": 5, "hook": 5, "line": "The Target story is not that nobody saw the alert: Target testified that some intruder activity was surfaced and evaluated, while the public record cannot show what happened next."},
  "10": {"recognition": 5, "reversal": 5, "takeaway": 5, "fit": 5, "hook": 5, "line": "Apple's TLS bug silently returned success while CrowdStrike's sensor crashed the host—two famous incidents caused by error paths failing in opposite directions."}
}
```

## Hacker News differences

For Hacker News, Chapter 03 would rise: the tarball-versus-tree distinction, Autotools mechanics, reproducible-build limits, and dependency edges reward technical curiosity even though they narrow LinkedIn fit. Chapter 10 would remain near the top, but its Apple half would matter more than its management lesson because the one-line C bug invites code-level debate. Chapter 04 could also rise on the ECB/password-storage mechanism. Chapters 00, 07, and 09 would likely fall: OWASP methodology, legacy-access inventory, and SOC handoffs are highly relevant to enterprise leaders but less novel to a technically self-selecting crowd. Chapter 06 might improve slightly because its aggregation and visualization failure crosses security, privacy, and data engineering.
