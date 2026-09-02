**BLOCK — revise before ship: the chapter overstates attribution and build provenance, and several ledger verdicts are not earned by their cited records.**

## Ranked findings

### 1. Blocker — the lede converts an unresolved identity and motive into fact

**Location:** [chapter line 25](/home/diablo/book17/chapters/03-xz.html:25), “Jia Tan spent two years earning trust … Then he slipped a backdoor into it … All of that holds.”

**Problem:** The record establishes an account, commits, signed tarballs, and Collin’s statement that “the maintainer who added the backdoor has disappeared.” It does not establish the person’s identity, gender, or that two years of contribution were undertaken to earn trust. The chapter later contradicts its own lede by saying Jia Tan is named “only as a git identity and a signer of tarballs” ([line 39](/home/diablo/book17/chapters/03-xz.html:39)). WIRED itself treats the identity as unresolved ([retelling lines 10–14](/home/diablo/book17/resources/sources/03/retellings-quoted-sentences.txt:10)).

**Fix:** Attribute the strategy to the folk account and keep the record narrower: an account using the name Jia Tan contributed for two years, became a release signer, and signed the compromised tarballs. Avoid “he,” “earning trust,” “slipped,” and “All of that holds” unless expressly framed as the retelling.

**Missed by both reviewers.**

### 2. Blocker — reproducibility results are presented as proof the source explicitly does not provide

**Location:** [chapter line 62](/home/diablo/book17/chapters/03-xz.html:62), “It showed that Debian’s build machines, which had run the backdoored library for weeks, had not tampered with what they built.”

**Problem:** Cascadian said the sid builders “may have used or built or run” vulnerable xz, and warned that his own verification machine might also have run it and was “not absolutely [the] cleanest of checks”; he called the result “some sort of data point” ([source lines 11–17, 35–42](/home/diablo/book17/resources/sources/03/rb-general-2024-03-30-cascadian.txt:11)). Bit-identical rebuilding increased confidence; it did not prove the build machines had not tampered with outputs, nor prove they had run the backdoor “for weeks.”

**Fix:** Say that the sampled outputs matched independent rebuilds despite stated environmental caveats. Preserve “may have run vulnerable xz” and distinguish evidence of matching outputs from proof about builder conduct.

**Missed by both reviewers.**

### 3. High — the signature explanation is technically false and overreads Collin

**Location:** [chapter line 55](/home/diablo/book17/chapters/03-xz.html:55), “The commits were genuinely from the account … Signing proves who built the artefact.”

**Problem:** “I didn’t spot any signs of committer fraud” is absence of detected fraud, not proof that commits were genuine ([review lines 13–15](/home/diablo/book17/resources/sources/03/tukaani-review-notes-excerpts.txt:13)). A valid signature proves that the corresponding private key signed particular bytes; it does not prove who operated the key or who built the artifact. This weakens the chapter’s central lesson about the limits of signatures.

**Fix:** Replace both claims with: the recorded account made the commits, and the release key signed the tarballs; neither fact establishes the human operator or that the tarball matches reviewed source.

**Missed by both reviewers.**

### 4. High — the first ledger `HOLDS` verdict is unearned

**Location:** [ledger row 1, line 75](/home/diablo/book17/chapters/03-xz.html:75), “chose to ‘spend two years politely and enthusiastically volunteering to help’ — HOLDS.”

**Problem:** Git proves the interval between the first patch and payload commits. It does not prove “chose,” an attack plan, politeness, enthusiasm, or that all contributions were intended to earn trust. The row silently changes proof of chronology into proof of motive.

**Fix:** Narrow the folk claim to the two-year contribution timeline and grade that `HOLDS`; put the strategic intent in a separate `OPEN` row.

**Missed by both reviewers.**

### 5. High — the tarball-versus-tree `MISSING` row attacks sources that already state the distinction

**Location:** [ledger row 5, line 79](/home/diablo/book17/chapters/03-xz.html:79).

**Problem:** The row cites Freund’s opening line as the compressed folk story, but Freund explains the tarball-only trigger immediately afterward ([source lines 22–42](/home/diablo/book17/resources/sources/03/freund-oss-security-2024-03-29.txt:22)). The saved Ars excerpt likewise says the malicious install script resided only in archived releases while git contained the second-stage artifacts ([retelling line 21](/home/diablo/book17/resources/sources/03/retellings-quoted-sentences.txt:21)). Those named sources do not omit the defender’s fact.

**Fix:** Find a named retelling that genuinely collapses tarball and tree, quote it specifically, or remove/regrade the row.

**Missed by both reviewers.**

### 6. High — the final practical exercise promises more than its diff can show

**Location:** [chapter lines 90–91](/home/diablo/book17/chapters/03-xz.html:90), especially “Any of the three closes the gap,” “exactly one modified macro file,” and “no diff catches it.”

**Problem:** A tarball-versus-`git archive` diff will show many generated files absent from git; `build-to-host.m4` is absent rather than visibly “one modified” file. Distinguishing its malicious change requires comparison with independently regenerated or upstream macro output. “No diff catches” the payload is also too broad: a commit/tag diff shows the binary fixtures being added or changed, though not their meaning.

**Fix:** Specify the relevant comparisons:

- Tarball versus tag reveals undeclared generated inputs.
- Tarball versus independently regenerated release output can isolate altered generated content.
- Tarball versus tag cannot expose malicious bytes present identically in both.
- A history diff can flag added binary fixtures but cannot establish their purpose.

**Missed by both reviewers.**

### 7. High — two ledger rows lack a defensible named source or record

**Location:** [ledger lines 82–83](/home/diablo/book17/chapters/03-xz.html:82).

**Problem:**

- “Microsoft employee Andres Freund … — `HOLDS`”: Freund’s cited disclosure does not mention Microsoft or his employer ([source header and body](/home/diablo/book17/resources/sources/03/freund-oss-security-2024-03-29.txt:5)). The secondary retelling supplies the descriptor, but the record column does not verify it.
- “The backdoor was one implant in liblzma (every retelling)”: “every retelling” violates the requirement for a specific named folk claim and cannot support a `MISSING` verdict.

**Fix:** Remove “Microsoft employee” from the graded claim or add an appropriate record. Replace “every retelling” with an exact named retelling that omits the Landlock sabotage; otherwise cut the row.

**Confirmed from both reviewers’ ledger findings.**

### 8. Medium-high — checked git claims are not fully receipted in the saved source packet

**Location:** [chapter lines 33–34](/home/diablo/book17/chapters/03-xz.html:33); claims `03-tags-jiatan` and `03-url-move`.

**Problem:** The saved git history lists taggers but does not contain the asserted PGP-signature output for all nine tags ([source lines 46–76](/home/diablo/book17/resources/sources/03/xz-git-history.txt:46)). It also shows only one URL-changing commit, while the claim says there were four. The claims TSV names the missing commands/hashes, but that is the assertion register, not underlying evidence.

**Fix:** Append the raw `git cat-file`/signature evidence for all nine tags and the four commit summaries/diffs to the saved source excerpt, or narrow the prose to what is present.

**Missed by both reviewers.**

### 9. Medium-high — the Debian advisory’s qualification is dropped

**Location:** [chapter line 37](/home/diablo/book17/chapters/03-xz.html:37), “No stable release was affected.”

**Problem:** DSA-5649-1 says, “Right now no Debian stable versions are known to be affected” ([source lines 9–16](/home/diablo/book17/resources/sources/03/debian-dsa-5649-1.txt:9)). The chapter turns a time-bounded knowledge statement into a categorical finding.

**Fix:** Use “No Debian stable version was known to be affected at the time of the advisory.”

**Missed by both reviewers.**

### 10. Medium — several unsupported absolutes let the drama outrun the record

**Locations:**

- [Line 25](/home/diablo/book17/chapters/03-xz.html:25): “nobody was measuring that gap.”
- [Line 45](/home/diablo/book17/chapters/03-xz.html:45): “Nobody reads those” and “edited by hand.”
- [Line 53](/home/diablo/book17/chapters/03-xz.html:53): “the one daemon on every server.”
- [Line 90](/home/diablo/book17/chapters/03-xz.html:90): “Every one of those is a file no reviewer has read.”
- [Line 39](/home/diablo/book17/chapters/03-xz.html:39): “No one has been charged and no government has published an attribution.”

**Problem:** The corpus cannot establish these universal negatives. Not every server runs sshd; the record shows a modified macro, not how it was edited; and the current charges/attribution claim has no incident claim marker or underlying record.

**Fix:** Use bounded formulations such as “the collected record shows no comparison before Freund,” “often treated as generated noise,” and “a common internet-facing daemon.” Phrase the legal claim as a dated corpus limitation and receipt it.

**Missed by both reviewers.**

### 11. Medium — “no security background” overstates Freund’s disclaimer

**Location:** [chapter line 25](/home/diablo/book17/chapters/03-xz.html:25).

**Problem:** Freund said he was “not a security researcher, nor a reverse engineer” ([source lines 188–192](/home/diablo/book17/resources/sources/03/freund-oss-security-2024-03-29.txt:188)). That does not establish that he had no security background.

**Fix:** Use his actual boundary: “an engineer who was not a security researcher or reverse engineer.”

**Confirmed from flash reviewer finding 4.**

### 12. Medium-low — the adoption count is unsupported

**Location:** [chapter line 65](/home/diablo/book17/chapters/03-xz.html:65), “These are two maintainers and one distribution.”

**Problem:** The cited records establish Arch package conversions and one maintainer’s libntlm change. kpcyrd reports Arch’s distribution-level adoption but does not record a second project-level adoption ([source lines 16–27](/home/diablo/book17/resources/sources/03/rb-general-2024-04-03-kpcyrd.txt:16)).

**Fix:** Change to “one upstream project and one distribution,” or cite a second maintainer adoption.

**Confirmed from flash reviewer finding 2.**

### 13. Low — build-time conditions are placed after runtime behavior

**Location:** [chapter line 52](/home/diablo/book17/chapters/03-xz.html:52).

**Problem:** The paragraph reaches box five and runtime symbol interception, then jumps backward to configure-time build gates. This weakens the otherwise chronological pipeline.

**Fix:** Move the x86-64/GCC/GNU-ld/package-build conditions to box three or four.

**Confirmed from flash reviewer finding 3.**

### 14. Low — the Ars reading entry is the only unlinked named retelling

**Location:** [chapter line 102](/home/diablo/book17/chapters/03-xz.html:102).

**Problem:** The URL exists in [SOURCES.md](/home/diablo/book17/resources/sources/03/SOURCES.md:38), but the reading entry omits the title and link.

**Fix:** Link the indexed Ars article and include its title.

**Confirmed from flash reviewer finding 5.**

## Reviewer-finding adjudication

| Reviewer finding | Disposition | Why |
|---|---|---|
| Flash 1 — unnamed “every retelling” ledger claim | **CONFIRMED** | Violates the named-retelling rule and cannot sustain the verdict. |
| Flash 2 — “two maintainers and one distribution” | **CONFIRMED** | The adoption record establishes one upstream project and Arch, not two maintainer adoptions. |
| Flash 3 — build/runtime sequence inversion | **CONFIRMED** | Build gates appear after the runtime box. |
| Flash 4 — “no security background” | **CONFIRMED** | Freund disclaimed two specialist roles, not all security background. |
| Flash 5 — missing Ars hyperlink | **CONFIRMED** | URL is indexed but absent from the reading entry. |
| Pro 1 — Microsoft employment unsupported by ledger record | **CONFIRMED** | Freund’s disclosure contains no employer information. |
| Pro 2 — unnamed “every retelling” ledger claim | **CONFIRMED** | Duplicate of Flash 1. |
| Pro 3 — alleged 167-word payload paragraph | **REJECTED** | The project tokenizer counts 148 words; the advisory triggers only above 150. |
| Pro 4 — alleged 159-word June 2022 paragraph | **REJECTED** | The project tokenizer counts exactly 150 words, so it does not exceed the threshold. |
| Pro 5 — missing non-web-app disclaimer | **REJECTED** | Xz matches A03’s express coverage of building, distribution, third-party code, tools, and dependencies. The checklist requires a caveat where fit is unclean; this category fit is direct. |
