**BLOCK — the chapter contains an unresolved `open` incident claim and presents several source-limited inferences as established facts.**

## Ranked findings

1. **Blocker — The current sentence is unsupported and inaccurately collapsed into the original sentence.**  
   [Chapter line 45](/home/diablo/book17/chapters/01-broken-access-control.html:45) says the district court “reimposed” time served and five years’ probation. Claim `01-resentence-2025` remains `open`; the saved material is only a secondary summary, not the order. That summary describes supervised release with home confinement, not probation. The ledger repeats the problem. ([Claims line 32](/home/diablo/book17/checks/claims/01.tsv:32), [source note](/home/diablo/book17/resources/sources/01/SOURCES.md:48), [CyberScoop summary](/home/diablo/book17/resources/sources/01/cyberscoop-2025.txt:6))  
   **Fix:** Fetch and register the official resentencing order, distinguishing probation from supervised release, or remove the post-remand claim from the chapter and ledger.  
   **Reviewer:** Flash #2 — **CONFIRMED**, with the additional legal-term problem above.

2. **High — The core historical mechanism is stated as fact before the chapter admits it is unproved.**  
   “The first command asked a firewall for its own credentials” ([line 25](/home/diablo/book17/chapters/01-broken-access-control.html:25)) is neither what the complaint says nor technically accurate under the proposed reconstruction: the command would request credentials from the metadata service through the WAF. Similar categorical claims appear at lines 52–63. Only later does the chapter disclose that no court document establishes SSRF or metadata and calls this merely “the most probable reading.” ([line 67](/home/diablo/book17/chapters/01-broken-access-control.html:67), [complaint note](/home/diablo/book17/resources/sources/01/complaint.txt:144))  
   **Fix:** Qualify the reconstruction from the lede onward: the command obtained role credentials; Krebs’s source says this happened through SSRF to metadata; the public primary record does not reveal that step.  
   **Reviewer:** Pro #2 — **CONFIRMED**.

3. **High — The OCC findings are particularized beyond the source.**  
   “A role nobody scoped, an anomaly nobody triaged” and the ledger’s “alerts nobody dispositioned” ([lines 85 and 99](/home/diablo/book17/chapters/01-broken-access-control.html:85)) are not OCC findings. The order reports general deficiencies in risk assessment, network controls, data-loss prevention, alert disposition, audit, and governance. It does not mention the incident, the WAF role, these API calls, or any specific alert. ([OCC findings](/home/diablo/book17/resources/sources/01/occ-consent-order.txt:14), [source caveat](/home/diablo/book17/resources/sources/01/occ-consent-order.txt:37)) Likewise, “Nobody at the bank found it there” is stronger than the evidence that external notice preceded the bank’s determination.  
   **Fix:** Preserve the distinction: the complaint shows unusual logged activity and later external notice; the OCC separately found broader cloud-control and alert-disposition failures. Do not claim that a particular role or alert was unscoped or ignored without a source.

4. **High — The saved AWS evidence is not lossless enough to audit the chapter’s exact claims.**  
   The extraction explicitly says inline link text was dropped ([AWS source lines 5–8](/home/diablo/book17/resources/sources/01/aws-imdsv2.txt:5)). Consequently, strings asserted or quoted in the chapter—including `X-Forwarded-For`, `ec2:RoleDelivery`, and parts of the PUT explanation—are absent from the stored text. In addition, the 2019 post establishes that both versions were enabled by default at launch; it does not support “stayed enabled by default” or the exhaustive “in that post or since” claim. ([chapter line 81](/home/diablo/book17/chapters/01-broken-access-control.html:81), [AWS source line 60](/home/diablo/book17/resources/sources/01/aws-imdsv2.txt:60))  
   **Fix:** Save a lossless article extraction or HTML snapshot. Change the temporal wording to “At launch, both versions were enabled by default,” and source or remove claims about later defaults and unpublished measurements.

5. **High — The Twitter quotation omits material context about the named person.**  
   [Chapter line 41](/home/diablo/book17/chapters/01-broken-access-control.html:41) reproduces the “bomb vest” message as incriminating writing without the immediately relevant context later discussed by Judge Sung: Thompson also expressed suicidal intent and described severe distress. ([CA9 dissent lines 144–162](/home/diablo/book17/resources/sources/01/ca9-opinion.txt:144)) The quotation is not needed to establish the gist linkage, and its dramatic force exceeds its contextual treatment.  
   **Fix:** Omit it, use the less context-sensitive Slack evidence, or briefly state the crisis context and the competing judicial readings.  
   **Reviewer:** Pro #1 — **CONFIRMED**.

6. **High — Two ledger claims are not genuine, specifically sourced folk claims.**  
   “The Capital One hack: a targeted attack on one bank” is inferred from a headline and a Wikipedia section title; neither asserts targeting. “The whole cause in most retellings” is likewise unsupported by the single DOJ sentence cited. ([ledger lines 96 and 99](/home/diablo/book17/chapters/01-broken-access-control.html:96)) This violates the hard rule against straw-man ledger rows.  
   **Fix:** Replace each with an explicit quotation from a named retelling that actually makes the claim, or delete the row. Retain the multi-victim scan as a record-side fact elsewhere.

7. **Medium — The OWASP explanation conflates distinct weaknesses and overstates SSRF.**  
   “The harm at the end of it is always access the requester was never granted” and CWE-441 being “the older name for the same thing” ([lines 54 and 65](/home/diablo/book17/chapters/01-broken-access-control.html:54)) are categorical and unsupported. OWASP lists CWE-441 and CWE-918 separately, not as synonyms. ([OWASP CWE list](/home/diablo/book17/resources/owasp/A01_2025-Broken_Access_Control.txt:173))  
   **Fix:** Say that *in this reconstruction* SSRF supplies the route and over-broad authorization supplies the impact; describe confused deputy as a related model, not an older name for SSRF.

8. **Medium — The defensive takeaway audits enumeration while neglecting the permissions that caused the loss.**  
   The closing exercise asks only “what can it list?” and calls enumeration “the whole of A01.” ([lines 107–109](/home/diablo/book17/chapters/01-broken-access-control.html:107)) A role can be dangerous without bucket-list permission if it can read, write, delete, or create against known resources. Likewise, a tightly scoped role without `ListBuckets` permission would not make all three commands “return a list.” ([line 83](/home/diablo/book17/chapters/01-broken-access-control.html:83))  
   **Fix:** Have the reader enumerate every allowed action and resource—list, read, write, delete, and create—and compare each with the workload’s actual job.

9. **Medium — The lede’s scale is not receipted by its attached claim.**  
   “Roughly a hundred million people” is supported later by the trial record, but the adjacent marker `01-arrest` covers the arrest and seized devices, not the population figure. ([chapter line 25](/home/diablo/book17/chapters/01-broken-access-control.html:25), [claim row](/home/diablo/book17/checks/claims/01.tsv:3))  
   **Fix:** Attach `01-ca9-98m` or a Capital One count marker to the numerical clause, and phrase the arrest allegation separately.  
   **Reviewer:** Flash #4 — **CONFIRMED as a traceability problem**, not because the eventual roughly-100-million figure is false.

10. **Medium — The pseudocode conflates three different request-routing failures.**  
    The comments name a URL-fetch feature, Host-header routing, and an open reverse proxy, but the code models only a user-controlled URL parameter. ([lines 58–63](/home/diablo/book17/chapters/01-broken-access-control.html:58)) That weakens the whiteboard test for the alleged WAF path.  
    **Fix:** Label it explicitly as generic application-level SSRF, then explain in prose that an open WAF or reverse proxy can expose the same trust boundary through routing configuration. Do not add a working proxy configuration.  
    **Reviewer:** Pro #3 — **CONFIRMED**, with the reviewer’s proposed configuration example rejected on capability grounds.

11. **Low — Slack-channel ownership is overstated.**  
    “On a Slack channel she organised” ([line 41](/home/diablo/book17/chapters/01-broken-access-control.html:41)) compresses two facts: the complaint says she organized a Meetup group, and that group contained an invitation to the Slack channel. ([raw complaint lines 328–340](/home/diablo/book17/resources/sources/01/complaint-ocr-raw.txt:328))  
    **Fix:** Use “on a Slack channel linked from a Meetup group she organised.”  
    **Reviewer:** Pro #5 — **CONFIRMED**.

12. **Low — Navigation contains duplicate Contents controls.**  
    The current HTML no longer matches Flash’s report, but it does render “← Contents” beside another “Contents” link. ([lines 124–127](/home/diablo/book17/chapters/01-broken-access-control.html:124))  
    **Fix:** Remove the redundant left control or disable the previous-chapter slot.

## Reviewer adjudication

| Reviewer finding | Verdict | Why |
|---|---|---|
| Flash #1 — GitHub/GitLab resume mismatch | **REJECTED** | The prose says the resume was *linked from* the GitHub profile, not hosted there. The complaint says exactly that the GitHub profile linked to a GitLab page containing the resume. ([raw complaint line 308](/home/diablo/book17/resources/sources/01/complaint-ocr-raw.txt:308)) |
| Flash #2 — open resentencing claim | **CONFIRMED** | Claim remains `open`; no primary order is saved. |
| Flash #3 — truncated Amazon quotation | **REJECTED** | The chapter quotes a contiguous, meaning-preserving portion of the sentence. An ellipsis is not required merely because words after the quoted fragment were omitted. |
| Flash #4 — arrest/100-million conflation | **CONFIRMED, narrowed** | The later record supports the scale, but the attached claim marker does not. |
| Flash #5 — placeholder navigation | **REJECTED** | It describes stale HTML. The current links form the existing pilot sequence 1 → 3 → 10 and pass the internal-link check; only the duplicated Contents control remains. |
| Pro #1 — crisis context omitted | **CONFIRMED** | The Ninth Circuit dissent supplies directly relevant omitted context. |
| Pro #2 — “asked a firewall” | **CONFIRMED** | Neither the complaint nor the proposed technical reconstruction supports that wording. |
| Pro #3 — pseudocode/WAF mismatch | **CONFIRMED** | The code implements only one of the three patterns named in its comments. |
| Pro #4 — exact metadata credential path | **UNVERIFIABLE** | The supplied evidence does not document bare-endpoint behavior or the credential path, and “metadata address” need not mean only the bare IP. Adding a live credential path would also violate the chapter’s capability constraint; “credential endpoint” is sufficient. |
| Pro #5 — Slack organiser | **CONFIRMED** | The complaint attributes organization to the Meetup group, not the Slack channel. |
| Pro #6 — 139-word wall paragraph | **REJECTED** | It is below the project’s 150-word advisory threshold, has four clearly signposted parallel cases, and the structure check reports the chapter as `ok`. |
