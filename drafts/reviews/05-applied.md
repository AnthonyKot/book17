# Chapter 05 — panel findings applied (2026-09-03)

Against `drafts/reviews/05-codex.md`, with the independent Flash and Pro reports consulted after it.

1. **Conflicting exploit-path accounts. Applied.** Removed the sentence saying Huntress described Rapid7’s division of labor. Rapid7’s later decompiled path now stands alone: `machine2.aspx` populated session state, then `guestaccess.aspx` loaded it and reached `UserGetUsersWithEmailAddress()`. The chapter claim and TSV row now match `rapid7-analysis-cve-2023-34362.txt`; the no-longer-used Huntress claim row was removed.
2. **Broken code excerpts. Applied.** Replaced both disconnected fragments with explicitly abridged pseudocode grounded in Rapid7’s saved diff. The pre-patch example now defines the formatted query and labels `{0}`, `{1}` and `{2}`. The post-patch example shows four placeholder clauses, four bindings, `AddAndToWhere()`, and the final query-plus-parameters call. The prose no longer claims that structurally omitted code was merely rewrapped.

## Extra corrections

