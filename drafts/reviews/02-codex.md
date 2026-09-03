**BLOCK — revise before shipping: the chapter contains an unsupported release date, multiple ledger verdicts that the cited record does not earn, and several source-scope errors.**

## Ranked findings

### 1. Blocker — 8 November is not established as the 3.6 GA date

**Reviewer:** Flash #1 — **CONFIRMED**, with a narrower conclusion than the reviewer states.

**Location:** “on the day 3.6 shipped,” “General availability came on 8 November 2017,” and “GA 8 Nov 2017” ([chapter](/home/diablo/book17/chapters/02-mongodb-ransom.html:29), [defense](/home/diablo/book17/chapters/02-mongodb-ransom.html:77), [ledger row 5](/home/diablo/book17/chapters/02-mongodb-ransom.html:98)).

The press release says MongoDB “announced the release” on 8 November, but never says GA. The contemporaneous TNW report says release candidates were available and the final release was expected in December ([press release](/home/diablo/book17/resources/sources/02/mongodb-newsroom-2017-11-08.txt:5), [TNW](/home/diablo/book17/resources/sources/02/tnw-2017-11-08.txt:10)). Thus the chapter resolves conflicting evidence as a precise GA date without support. The reviewer’s replacement claim that GA occurred in “early December” is also not established by the supplied sources.

**Fix:** Say “announced on 8 November; TNW reported that the final release was expected in December,” or add a primary source for the actual 3.6.0 GA date. Recalculate “seven months,” “two months before 3.6,” and the ledger timeline.

### 2. Blocker — Horowitz’s conditional claim is graded as though it were unconditional

**Missed by both reviewers.**

**Location:** Ledger row 8, “If you don’t explicitly turn it on, that entire method of doing ransomware goes away” → `OVERSTATED` ([chapter](/home/diablo/book17/chapters/02-mongodb-ransom.html:101)).

Horowitz explicitly limits the claim to an installation where external networking is not enabled. The record column answers with attacks against the installed base, old images, and configurations where networking was enabled—none contradict the quoted condition. The chapter’s own explanation concedes it is “True for a fresh install that keeps its default.”

**Fix:** Grade the quote `HOLDS`, or source a retelling that generalized it to the installed base and grade that distinct claim.

### 3. Blocker — the 78% ledger verdict is not supported by comparable evidence

**Missed by both reviewers.**

**Location:** Ledger row 4 ([chapter](/home/diablo/book17/chapters/02-mongodb-ransom.html:97)).

The folk claim concerns Gevers’s January 2017 attacked/exposed hosts. The rebuttal uses Matherly’s December 2015 population of exposed hosts. That earlier census shows that safe-default versions could be exposed, but it does not show that such hosts were among Gevers’s January 2017 population or invalidate his 78% figure. `MISSING` is therefore not earned for the specific claim.

**Fix:** Obtain version/configuration telemetry for the 2017 victims, mark the claim `OPEN`, or recast the row as a general explanation of the exposed population rather than a verdict on Gevers’s 78%.

### 4. High — ledger row 7 substitutes a different speaker and timeline

**Reviewer:** Pro #1 — **CONFIRMED**.

**Location:** Ledger row 7 ([chapter](/home/diablo/book17/chapters/02-mongodb-ransom.html:100)).

The folk column attributes the “blamed database owners” characterization to Ottenheimer’s September post via ZDNet. The record answers primarily with Nilsson’s January advice and a ticket filed nine weeks later. That does not test the stated folk claim. Ottenheimer’s own post both describes users leaving systems insecure and describes MongoDB’s product-level default changes ([source](/home/diablo/book17/resources/sources/02/ottenheimer-2017-09-08.txt:13)).

**Fix:** Compare ZDNet directly with Ottenheimer’s complete post; its omission of his product-change discussion may support `OVERSTATED`. Keep the Nilsson-to-ticket sequence as a separate row.

### 5. High — ledger row 2 combines three claims and gives them the wrong common verdict

**Reviewer:** Flash #2 — **CONFIRMED**.  
**Additional issue missed by both:** the row violates CONTEXT §4’s one-specific-claim rule.

**Location:** Ledger row 2 ([chapter](/home/diablo/book17/chapters/02-mongodb-ransom.html:95)).

The raw binary and non-package distributions remained open by default until the 3.6 change, while official RPM/DEB packages had bound to localhost since 2.6. The folk account is therefore true in outline but collapses materially different installation paths: `OVERSTATED`, not `WRONG`. Moreover, TNW, Wikipedia, and The Register make distinct claims that cannot fairly share one verdict.

**Fix:** Split the row by retelling and judge each independently. At minimum, change the broad “unsafe until 3.6” claim to `OVERSTATED`.

### 6. High — the tracking sheet is misdescribed, and its provenance is overclaimed

**Reviewer:** Flash #3 — **CONFIRMED**.  
**Additional issue missed by both:** “behind every January figure” is unsupported.

**Location:** “one row per actor, 109 rows in all” and “The document behind every January figure” ([chapter](/home/diablo/book17/chapters/02-mongodb-ransom.html:43)).

The sheet uses multiple continuation rows for single actors such as Harak1r1 and Kraken0 ([sheet excerpt](/home/diablo/book17/resources/sources/02/gevers-merrigan-sheet-excerpt.txt:8)). It therefore does not contain 109 distinct actors. Nor does the record establish that the sheet underlies every January number: the 1,800 figure is attributed to Matherly, the payment count to Blockchain.info, and the 52,000 exposed-host figure to Shodan.

**Fix:** Describe it as “109 spreadsheet rows across dozens of actors/campaign signatures.” Replace “every January figure” with a claim limited to the totals demonstrably derived from it.

### 7. High — the 40% statistic has unresolved scope

**Reviewer:** Pro #2 — **UNVERIFIABLE as stated**, but the chapter still requires revision.

The source places “40% of the instances” immediately after discussing the 319 `hackedDB` results, strongly suggesting that subset, but it never explicitly names the denominator in the saved text ([source](/home/diablo/book17/resources/sources/02/shodan-2015-07-18.txt:51)). The reviewer cannot conclusively prove the subset from this excerpt; conversely, the chapter cannot safely expand it to all exposed instances.

**Fix:** Say “Matherly reported 40% in the results he was discussing, apparently the `hackedDB` subset,” or remove the statistic unless the original page/chart settles its scope.

### 8. High — factual assertions escape the receipt standard

**Missed by both reviewers.**

Examples include:

- “Authentication is off by default in 3.6 as it was in 1.8” ([chapter](/home/diablo/book17/chapters/02-mongodb-ransom.html:63)); the adjacent claim row records Horowitz’s quotation, not this two-version product claim.
- “Shadowserver has scanned … daily for years” ([chapter](/home/diablo/book17/chapters/02-mongodb-ransom.html:83)); the saved source describes the probe but says neither “daily” nor “for years” ([source](/home/diablo/book17/resources/sources/02/shadowserver-open-mongodb-report.txt:5)).
- The specific “config file copied from a 2013 tutorial” example ([chapter](/home/diablo/book17/chapters/02-mongodb-ransom.html:61)) has no supporting record.

**Fix:** Add precise sources and claim rows or remove/qualify the assertions.

### 9. Medium — the defense is said to have reached the installed base without evidence

**Missed by both reviewers.**

**Location:** “The defense that reached the installed base was the instrument” ([chapter](/home/diablo/book17/chapters/02-mongodb-ransom.html:87)).

The sources establish that scanners and vendor alerts existed, not that operators received or acted on them. The paragraph then admits there is no published uptake figure.

**Fix:** Say scanning and alerting were the defenses capable of examining existing installations, while the record does not show their reach or effect.

### 10. Medium — the ticket is quoted selectively in a way that distorts its advice

**Missed by both reviewers.**

**Location:** “the shortest fix on any forum is the one the vendor itself prints … `bindIp: 0.0.0.0`” ([chapter](/home/diablo/book17/chapters/02-mongodb-ransom.html:63)).

SERVER-28229 does show that example, but also tells readers to review the Security Checklist, discusses binding selected addresses, and warns about external connections ([source](/home/diablo/book17/resources/sources/02/jira-server-28229.txt:17)). The chapter makes the example sound like MongoDB’s recommended universal shortcut.

**Fix:** Include the ticket’s warning and selected-address option; remove the unsupported “shortest fix on any forum” generalization.

### 11. Medium — MongoDB terminology is wrong

**Reviewer:** Flash #4 — **CONFIRMED**.

“Table named WARNING” reproduces Bleeping Computer’s terminology, but MongoDB uses databases, collections, and documents. Attribution does not make it technically correct in the lede.

**Fix:** Use “collection/document reported at the time as a table,” then use MongoDB terminology thereafter.

### 12. Medium — “no password” blurs disabled authentication with an empty password

**Reviewer:** Flash #5 — **CONFIRMED as a clarity problem**, though the reviewer overstates what the record proves about whether an admin account existed.

The secondary sources use “no password on the admin account,” while the technical account describes anonymous access and authentication being disabled. The chapter adopts the shorthand before explaining the distinction.

**Fix:** Introduce it as the contemporary report’s wording and immediately clarify that the operative condition was unauthenticated access, not necessarily an account with a blank password.

### 13. Low — “none of the three” reverses the chapter’s own model

**Reviewer:** Pro #3 — **CONFIRMED**.

Tarballs and pre-2.6 versions had the first default—the binary’s all-interface behavior—not “none of the three.” The same error appears in the page description ([chapter](/home/diablo/book17/chapters/02-mongodb-ransom.html:7)).

**Fix:** Use “fell through to the first default” or “had none of the later localhost defaults.”

### 14. Low — “That is the whole change” is literally false

**Reviewer:** Pro #5 — **CONFIRMED**.

The commit also changed IPv6 behavior, introduced `--bind_ip_all`, altered option handling, and added a warning ([commit](/home/diablo/book17/resources/sources/02/commit-60636b4.txt:10)).

**Fix:** Say “That is the binding-default change.”

### 15. Low — two reader-facing mechanism statements are too absolute

**Missed by both reviewers.**

“A database bound to localhost refuses the application server next to it” is false if the application runs on the same host; “There are only three places” a bind address can originate ignores command-line flags, orchestration, entrypoints, generated configuration, and managed-service controls ([chapter](/home/diablo/book17/chapters/02-mongodb-ransom.html:63), [chapter](/home/diablo/book17/chapters/02-mongodb-ransom.html:108)).

**Fix:** Say “an application server on another host” and present binary/package/operator as three common layers, not an exhaustive taxonomy.

## Rejected reviewer finding

**Pro #4 — OWASP fit: REJECTED.** A02’s quoted definition expressly covers “a system, application, or cloud service,” and an exposed database with unsafe deployment settings fits Security Misconfiguration directly. CONTEXT specifically identifies other chapters whose incidents need an out-of-scope qualification; it does not require inventing a mismatch for MongoDB.
