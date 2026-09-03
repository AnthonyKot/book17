**BLOCK — do not ship until the contradictory exploit-path account, broken code excerpts, and unearned ledger rows are corrected.**

The consolidated report is saved at [drafts/reviews/05-codex.md](/home/diablo/book17/drafts/reviews/05-codex.md).

It adjudicates all ten reviewer findings and adds five missed issues. `./verify.sh 05` passes, but its gates do not detect these source-semantic and ledger-fairness problems. The `audit-learning-ux` skill informed prioritization of errors that would teach readers the wrong mechanism.
state, followed by `guestaccess.aspx` loading that session and reaching `UserGetUsersWithEmailAddress()` ([Rapid7](/home/diablo/book17/resources/sources/05/rapid7-analysis-cve-2023-34362.txt:18), [call path](/home/diablo/book17/resources/sources/05/rapid7-analysis-cve-2023-34362.txt:26), [session continuation](/home/diablo/book17/resources/sources/05/rapid7-analysis-cve-2023-34362.txt:131)). Huntress’s early post assigns the jobs the other way round: `moveitisapi.dll` “is used to perform SQL injection” and `guestaccess.aspx` “is used to prepare a session” ([Huntress](/home/diablo/book17/resources/sources/05/huntress-2023-06-01.txt:26)). The chapter accurately reproduces Huntress’s sentence but falsely says it agrees with Rapid7, leaving the reader with the wrong whiteboard path. Claim row `05-huntress-route` records only what Huntress said and does not receipt the asserted agreement ([claims](/home/diablo/book17/checks/claims/05.tsv:26)).

**Fix:** Use Rapid7’s later decompiled call path for the mechanism. If Huntress remains, label it as an early conflicting account rather than corroboration, and update the claim row accordingly.

### 2. High — both code blocks are fragments presented as readable code, and the post-patch block hides the very binding relationship the prose asks the reader to count

**Reviewers:** Flash #2 and Pro #1 — **CONFIRMED, with Pro’s rationale narrowed**; Flash #3 — **CONFIRMED**.

**Location:** the pre-patch and post-patch blocks ([chapter](/home/diablo/book17/chapters/05-moveit.html:55), [chapter](/home/diablo/book17/chapters/05-moveit.html:70)).

The pre-patch block removes the `string.Format`/`objArray` enclosure and then calls `DoReadQuery` with undeclared `obj`. The post-patch block removes the `List<string> values` enclosure, the `func` and `str` declarations, the three `BuildLikeForSQL` placeholder expressions, and `where.AddAndToWhere(...)`; it leaves `string.Format("Email={0}", ...)` unattached and unterminated. The published diff shows all of that missing context ([Rapid7 diff](/home/diablo/book17/resources/sources/05/rapid7-analysis-cve-2023-34362.txt:88)). The prose then says four bindings can be counted against their placeholders, although the excerpt displays only the equality placeholder and never attaches it to `where` ([chapter](/home/diablo/book17/chapters/05-moveit.html:85)). Pro is wrong only in suggesting that every unassigned method invocation is syntactically forbidden in C#; the displayed line is nevertheless invalid as printed and semantically disconnected because its list context and terminator are gone.

**Fix:** Show coherent, explicitly elided pseudocode or restore enough of each published diff to define the format arguments/list, placeholders, `str`, `func`, `AddAndToWhere`, and the final call. Do not say the excerpts were “wrapped only for display” when structural code has been removed.

### 3. High — ledger row 3 is both a straw man and an apples-to-oranges comparison between different CVEs

**Reviewers:** Flash #4 and Pro #2 — **CONFIRMED**, with an additional defect missed by both.

**Location:** “The ordinary mental picture is a malicious value in a form field” ([ledger row 3](/home/diablo/book17/chapters/05-moveit.html:115)).

The left cell is not a folk account from a named retelling: it combines vendor boilerplate with the author’s invented “ordinary mental picture,” contrary to CONTEXT §4 and AGENT.md’s hard rule. More importantly, the cited 9 and 15 June advisories describe CVE-2023-35036 and CVE-2023-35708 ([9 June advisory](/home/diablo/book17/resources/sources/05/progress-kb-advisory-2023-06-09-cve-2023-35036.txt:90), [15 June advisory](/home/diablo/book17/resources/sources/05/progress-kb-advisory-2023-06-15-cve-2023-35708.txt:106)); Progress called those flaws distinct from the 31 May vulnerability ([security update](/home/diablo/book17/resources/sources/05/progress-security-page-2023-08-02-wayback.txt:24)). The record cell answers with Rapid7’s route for CVE-2023-34362. Even a genuine retelling of the later advisories could not be graded from a different vulnerability’s path.

**Fix:** Replace the left cell with a named retelling that actually describes CVE-2023-34362’s input route, then grade that precise claim; otherwise remove the row.

### 4. High — ledger row 4 uses a regulator’s generic explanation as “folk story,” not a retelling of MOVEit

**Reviewer:** Pro #3 — **CONFIRMED**.

**Location:** “SQL injection succeeds because developers fail to treat user content as potentially malicious” ([ledger row 4](/home/diablo/book17/chapters/05-moveit.html:116)).

The source is a primary CISA/FBI policy alert, not a named secondary retelling, and the quoted proposition is a generic explanation of SQL injection ([CISA/FBI](/home/diablo/book17/resources/sources/05/cisa-fbi-secure-by-design-sqli-2024-03.txt:37)). Its use in the left column violates the ledger contract. The record cell’s raw equality occurrence does not refute the proposition; it shows exactly one occurrence where the value was not safely handled. The partial escaping is useful mechanism nuance, but it is not a fair verdict on this source.

**Fix:** Move the CISA/FBI statement to the defense discussion. Use a genuine MOVEit retelling that claims input was never treated as hostile, if one exists, or delete this ledger row.

### 5. High — ledger row 5 invents the exclusive claim “One bug” and then grades it `OVERSTATED`

**Missed by both reviewers.**

**Location:** “A critical vulnerability”; “a zero-day vulnerability”; “CVE-2023-34362.” “One bug.” ([ledger row 5](/home/diablo/book17/chapters/05-moveit.html:117)).

Wikipedia, TechCrunch, and TechTarget each describe the exploited CVE-2023-34362 in the singular ([Wikipedia](/home/diablo/book17/resources/sources/05/wikipedia-2023-moveit-data-breach.txt:3), [TechCrunch](/home/diablo/book17/resources/sources/05/techcrunch-2023-08-25.txt:5), [TechTarget](/home/diablo/book17/resources/sources/05/techtarget-2023-09-26.txt:5)). None of the saved excerpts says it was the only SQL-injection defect in the product. The chapter adds “One bug,” then rebuts that addition with later, reportedly unexploited CVEs. Singular grammar about the incident’s exploited zero-day does not create an exclusivity claim, and the later distinct defects do not make the description of CVE-2023-34362 numerically wrong.

**Fix:** Find a retelling that expressly says there was only one SQL-injection flaw and grade that claim. Otherwise recast the row as a sourced omission and consider `MISSING`, or keep the five-CVE sequence in prose without a ledger verdict.

### 6. High — ledger row 6 removes TechCrunch’s own overlap caveat and does not establish an `OVERSTATED` number

**Missed by both reviewers.**

**Location:** the 60 million / 62,054,613 / 93.3 million “individuals” row ([ledger row 6](/home/diablo/book17/chapters/05-moveit.html:118)).

TechCrunch immediately says Emsisoft expects overlap among the reported individuals ([TechCrunch](/home/diablo/book17/resources/sources/05/techcrunch-2023-08-25.txt:9)). The ledger strips that material qualification and then supplies it as the correction. Emsisoft’s later tally likewise says overlap is inevitable but unquantified ([Emsisoft](/home/diablo/book17/resources/sources/05/emsisoft-tally.txt:32)); KonBriefing says its own separately compiled sum is records rather than distinct people ([KonBriefing](/home/diablo/book17/resources/sources/05/konbriefing-tally.txt:11)). Those sources establish that the tallies are not deduplicated. They do not establish the distinct-person population or prove that any quoted numerical total is an overstatement, and the saved Wikipedia excerpt does not show that its 93.3 million figure derives from Emsisoft as the record cell claims.

**Fix:** Quote each retelling with its caveat and describe the totals as disclosure/record counts whose distinct-person total is `OPEN`; or obtain a deduplicated estimate before using `OVERSTATED`.

### 7. Medium — ledger row 2 adds an unsourced fatalistic conclusion that TechTarget did not make

**Missed by both reviewers.**

**Location:** “The tempting conclusion is that nothing could have been done” ([ledger row 2](/home/diablo/book17/chapters/05-moveit.html:114)).

TechTarget says Progress patched quickly but instances were already under attack ([TechTarget](/home/diablo/book17/resources/sources/05/techtarget-2023-09-26.txt:5)). It does not say prevention was impossible. The author’s added conclusion is a second claim without a named speaker, while the `HOLDS` verdict applies only to the timing claim. This violates both the no-straw-man rule and CONTEXT §4’s one-specific-claim rule.

**Fix:** Delete the invented conclusion and grade only TechTarget’s timing claim. Keep the defect-class prevention argument in the defense prose.

### 8. Medium — ledger row 8 is a pleading, not a folk retelling

**Reviewer:** Pro #4 — **CONFIRMED**.

**Location:** “Progress allowed SQL-injection flaws to remain for years” ([ledger row 8](/home/diablo/book17/chapters/05-moveit.html:120)).

The left cell is a complaint allegation known only through a court order, not a named secondary retelling. Order 22 is explicit that it is reciting well-pleaded allegations and that the “persistent” SQL-injection allegation merely clears the pleading-stage hurdle ([Order 22](/home/diablo/book17/resources/sources/05/mdl-order-22-2025-07-31.txt:25), [ruling](/home/diablo/book17/resources/sources/05/mdl-order-22-2025-07-31.txt:111)). The chapter characterizes that legal status carefully, but the row still violates the ledger’s source-role rule.

**Fix:** Move the allegation and procedural disposition to the legal-record prose, or replace the left cell with a named retelling that made the duration claim and preserve `OPEN` with the settling evidence named.

## Reviewer adjudication

| Reviewer finding | Verdict | Why |
|---|---|---|
| Flash #1 — Huntress called corroboration despite reversing the roles | **CONFIRMED** | The two saved technical accounts assign session preparation and SQL execution differently. |
| Flash #2 — post-patch excerpt orphaned and missing `AddAndToWhere` | **CONFIRMED** | The Rapid7 diff contains the omitted list and builder attachment; the chapter’s excerpt hides the parameter-to-placeholder path. |
| Flash #3 — pre-patch excerpt is disconnected | **CONFIRMED** | The source’s format array and invocation context were removed, leaving undeclared `obj` and invalid floating fragments. |
| Flash #4 — ledger row 3 uses an editorial form-field assumption | **CONFIRMED** | Neither vendor advisory says “form field,” and neither is a named folk retelling. |
| Flash #5 — lede implies warning and fixes were simultaneous | **REJECTED** | “On 31 May … warned … and published fixes” asserts only a shared calendar date, which Progress’s revision history and 8-K support. The next two paragraphs explicitly distinguish the early mitigation-only state from the later same-day fixes ([KB history](/home/diablo/book17/resources/sources/05/progress-kb-advisory-2023-05-31-cve-2023-34362.txt:37), [8-K](/home/diablo/book17/resources/sources/05/progress-8k-2023-06-05.txt:4)). |
| Flash #6 — “One function explains both the break and the defense” overstates the whole chain | **REJECTED** | In context, the sentence identifies the function as the lens for the SQL-string/bound-parameter contrast; it does not claim the function is the whole exploit chain or whole remediation. The chapter separately explains the route and later patches. |
| Pro #1 — post-patch `string.Format` is a meaningless standalone statement | **CONFIRMED, narrowed** | The excerpt is broken because the list context, comma/terminator, declarations, and consumer are omitted. A terminated method invocation can be a legal C# statement, so the reviewer’s broad syntax rationale is imprecise. |
| Pro #2 — ledger row 3 violates the named-retelling rule | **CONFIRMED** | It uses primary vendor advisories plus an author-created assumption. |
| Pro #3 — ledger row 4 violates the named-retelling rule | **CONFIRMED** | A regulator’s generic alert is primary guidance, not the public folk story. |
| Pro #4 — ledger row 8 uses a complaint as folk story | **CONFIRMED** | A pleading-stage allegation is not a named secondary retelling, even though the record cell labels its legal status correctly. |
