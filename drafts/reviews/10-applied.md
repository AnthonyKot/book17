# Chapter 10 — panel findings applied (2026-09-01, from drafts/reviews/10-codex.md)

1. Lede now says Microsoft "estimated 8.5 million devices affected"; ledger row re-graded OVERSTATED ("crashed" is stronger than Microsoft's "affected"; estimate, not count).
2. Removed "That is failing closed", "exactly what CrowdStrike's own fix does" and the skips-the-rule claim; the bugcheck is described as an unhandled kernel fault contained at host size; fail-open/closed is labelled explicitly as an analogy about boundary size; the RCA's second mitigation (sensor corrected to supply 21 inputs) added; chapter states the RCA does not say what the interpreter does with rejected content.
3. Fetched Apple's HT1222 list (Wayback 5 Mar 2014: iOS 7.0.6/6.1.6 21 Feb, OS X 10.9.2 25 Feb) plus 2014 copies of HT6147/HT6150 with matching "Last Modified" footers; saved as `apple-security-updates-HT1222-2014.txt`; prose now "OS X 10.9.2 followed on 25 February"; "same batch of notes" removed; TSV `10-apple-ship-date` corrected; `apple-security-notes.txt` header corrected.
4. "reached all Windows sensors ... by 9 August" → "made generally available for Windows sensors 7.11 and later by 9 August".
5. "to every host, at once" → "cloud-delivered outside those controls, and it reached eligible online hosts during the deployment window" (marker `10-cs-window`).
6. Reboot-loop sentence re-sourced to CrowdStrike's remediation guidance ("crash again on reboot", "systems in a boot loop"); new claim `10-cs-boot-loop`, excerpt appended to `crowdstrike-kurtz-2024-07-19.txt`; wording no longer says every host looped.
7. Lede: "anyone on the network" → "an attacker who could intercept a connection impersonate a server to an affected client without holding the certificate's private key" (marker `10-wrong-key`).
8. Ledger row split: Wheeler's "invalid certificates were quietly accepted as valid" graded WRONG; Ars's "skip a crucial verification check" graded HOLDS as its own row.
9. "pride" → "states"; "shows how much that version is feared" → "addresses that concern directly"; "concedes" → "Finding 5: ... did not expose".
10. Both Delta rows removed from the ledger (no named public retelling carries them as folk claims); Delta moved to a labelled "Disputed consequences" paragraph at the end of the defense section; ledger now 9 rows.
11. Moot with 10; the paragraph words the loss as alleged and says no court has found a figure.
12. "never run in the interpreter" removed; chapter and TSV `10-cs-instance-testing` now say the validator's check did not expose the mismatch and that every instance is now tested before deployment.
13. "line 631" removed from chapter, ledger, TSV `10-diff-one-line` and SOURCES.md; text says "the deletion of the duplicate goto fail; line" and the TSV notes the diff alignment is not semantic.
14. "chosen by accident" → "open at authentication, whether or not anyone intended that result".
15. The gotofail.com FAQ passage as quoted by Wheeler saved verbatim in `retellings.txt`; the ledger row now quotes it directly; SOURCES.md notes gotofail.com itself was not fetched.
16. "Channel File 292" sentence removed; paragraph ends with the absence of published independent findings on the research date.
17. NSS clients and Langley's test server re-described as "evidence, not defenses": blast-radius measurement and a post-disclosure negative test that "did not prevent the shipped bug".
18. New OPEN ledger row for "the largest outage in the history of information technology", naming the measure that would settle it.
19. "adds that step" sentence split into two, one per finding, stating the new procedure (every new Template Instance is tested before deployment).
20. "compiled it with all warnings on" → "compiled it with -Wall".
21. Rejected by consolidator — left alone.
22. Rejected by consolidator — left alone.

Also: `drafts/10.ledger.md` rewritten to match the new nine rows; three paragraphs/sentences split to satisfy the structure lint after the edits.
