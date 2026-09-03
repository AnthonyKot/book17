# Chapter 05 — panel findings applied (2026-09-03)

Against `drafts/reviews/05-codex.md`, with the independent Flash and Pro reports consulted after it.

1. **Conflicting exploit-path accounts. Applied.** Removed the sentence saying Huntress described Rapid7’s division of labor. Rapid7’s later decompiled path now stands alone: `machine2.aspx` populated session state, then `guestaccess.aspx` loaded it and reached `UserGetUsersWithEmailAddress()`. The chapter claim and TSV row now match `rapid7-analysis-cve-2023-34362.txt`; the no-longer-used Huntress claim row was removed.
2. **Broken code excerpts. Applied.** Replaced both disconnected fragments with explicitly abridged pseudocode grounded in Rapid7’s saved diff. The pre-patch example now defines the formatted query and labels `{0}`, `{1}` and `{2}`. The post-patch example shows four placeholder clauses, four bindings, `AddAndToWhere()`, and the final query-plus-parameters call. The prose no longer claims that structurally omitted code was merely rewrapped.
3. **Ledger row 3’s form-field straw man and mismatched CVEs. Applied.** Removed the row from both ledgers and removed its TSV claim. No saved retelling describes CVE-2023-34362 as a form-field injection; the vendor text used on the left described later, distinct CVEs.
4. **Ledger row 4’s generic regulator statement. Applied.** Removed the row from both ledgers and removed its TSV claim. The CISA/FBI policy alert is not a named retelling of MOVEit, and Rapid7’s partial-escaping evidence did not contradict its generic explanation. The useful per-use escaping distinction remains in the mechanism section.
5. **Ledger row 5’s invented “one bug” claim. Applied.** Recast the row as a specific omission and changed the verdict from `OVERSTATED` to `MISSING`. TechTarget names the exploited CVE-2023-34362; Progress’s updates show that defenders also needed four later SQL-injection CVE fixes. The row no longer claims that singular grammar means exclusivity.

## Extra corrections
