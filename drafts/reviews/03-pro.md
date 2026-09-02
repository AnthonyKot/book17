### 1. Record Accuracy / Ledger Fairness (Severity: 1)
**Location:** Ledger, row 8: `"Microsoft employee Andres Freund identified the exploit"` graded as `HOLDS`.
**The problem:** The ledger awards a `HOLDS` verdict to the folk claim that Freund is a Microsoft employee based entirely on his `oss-security` email. However, the cited email is sent from a personal domain (`anarazel.de`) and does not mention his employer or Microsoft anywhere. The ledger is grading a claim as supported by a record that does not contain that fact.
**What would fix it:** Trim the quoted folk claim to remove "Microsoft employee" so the row only tests what the email can actually prove (investigating a performance regression), or change the verdict to note that the email does not establish his employer.

### 2. Ledger Fairness (Severity: 2)
**Location:** Ledger, row 9: `The backdoor was one implant in liblzma (every retelling).`
**The problem:** AGENT.md explicitly requires that a ledger row must be "quoted or closely paraphrased from a named retelling" to ensure the left column is real and not a straw man. Attributing a claim to "(every retelling)" is a literal straw man and directly violates this core rule.
**What would fix it:** Replace "(every retelling)" with a specific, cited quote from a named retelling (such as WIRED or Ars Technica) that describes the backdoor solely as the payload in the test files, missing the Landlock sabotage entirely. If no specific quote can be found, cut the row.

### 3. Readability / Wall Paragraphs (Severity: 3)
**Location:** Section "The break", paragraph beginning `"The payload's own timeline is longer than a February."`
**The problem:** At 167 words, this paragraph exceeds the 150-word advisory limit. It packs over a month of commits, dates, and review notes into a single dense block of text that is difficult to parse and requires re-reading.
**What would fix it:** Split the paragraph into two. A natural breakpoint is before `"On 15 February a one-line commit added build-to-host.m4 to m4/.gitignore."`

### 4. Readability / Wall Paragraphs (Severity: 4)
**Location:** Section "The break", paragraph beginning `"In June 2022, on the xz-devel list, a poster named Jigar Kumar..."`
**The problem:** At 159 words, this paragraph also exceeds the 150-word limit, running together multiple mailing list posts from different people over several weeks into an unbroken wall of text.
**What would fix it:** Split the paragraph to give the timeline room to breathe. A good split point is before `"Kumar pressed again a week later..."`

### 5. OWASP Fit (Severity: 5)
**Location:** Section "The mechanism", paragraph 1.
**The problem:** AGENT.md requires the chapter to "note where the incident does not fit the category cleanly," explicitly noting that some incidents are not web apps. While xz perfectly matches the definition of a supply chain failure, it is a system-level library injected into an SSH daemon, not a web application (the traditional domain of the OWASP Top 10). The chapter misses the opportunity to note this environmental mismatch.
**What would fix it:** Add a brief sentence acknowledging that while the supply chain mechanism fits the category perfectly, the target was a low-level OS daemon rather than a web application.
