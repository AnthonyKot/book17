### Finding 1: Unsourced folk claim in ledger row (Ledger fairness / Sourcing standard)
* **Severity:** Medium-High
* **Location:** Line 83 (`The ledger`, row 9): `"The backdoor was one implant in liblzma (every retelling)."`
* **Problem:** Citing `(every retelling)` violates the rule in CONTEXT §4 ("A row is one *specific* folk claim (quoted or closely paraphrased from a named retelling)") and AGENT.md §Incident rules ("Identify the folk story from named retellings (cite them — Wired, Krebs, the Wikipedia lede) so the ledger's left column is real, not a straw man"). The generic citation creates a composite/straw-man claim rather than testing a specific named source that omitted the CMake Landlock sandbox sabotage.
* **Fix:** Replace `(every retelling)` with a specific quote or close paraphrase from a named retelling in the corpus, such as Ars Technica ("injected itself into functions used by sshd") or Wikipedia ("a malicious backdoor was discovered in the compression software XZ Utils... deliberately inserted in February 2024").

---

### Finding 2: Maintainer count discrepancy (Record accuracy)
* **Severity:** Medium
* **Location:** Line 65 (`The defense`): `"These are two maintainers and one distribution."`
* **Problem:** The preceding text in that paragraph mentions only two entities adopting VCS snapshots or minimal source-only tarballs: kpcyrd (Arch Linux staff — one distribution) and Simon Josefsson (maintainer of libntlm — one maintainer). Describing them as "two maintainers and one distribution" is an inaccurate count in prose.
* **Fix:** Change the phrase to `"This is one maintainer and one distribution."` (or explicitly name a second maintainer if referring to another upstream project).

---

### Finding 3: Pipeline sequence inversion across build-time and runtime (Mechanism accuracy / Readability)
* **Location:** Line 52 (`The mechanism`): `"Box five is the running process... The injected script only proceeds on x86-64 Linux, with gcc and GNU ld, and when building a Debian or RPM package. Freund thought the last condition was 'likely aimed at making it harder to reproduce the issue for investigators'."`
* **Severity:** Low-Medium
* **Problem:** Paragraph 52 opens with runtime execution in Box five ("Box five is the running process. The object replaces the resolvers...") and explains the dynamic linking hijack in `sshd`. The subsequent two sentences jump backwards to describe configure/build-time script preconditions ("The injected script only proceeds on x86-64 Linux..."). This breaks the chronological 5-box pipeline structure by appending Box 3/4 build-time conditions to Box 5 runtime execution.
* **Fix:** Move the build precondition sentences into paragraph 45 (under Box 3/4 where `configure` script execution and Makefile injection are introduced), keeping Box 5 strictly focused on runtime symbol interception in `sshd`.

---

### Finding 4: Overstated disclaimer on investigator background (Fairness to named people / Record accuracy)
* **Severity:** Low
* **Location:** Line 25 (`Lede`): `"and an engineer with no security background caught it because logins were half a second slow."`
* **Problem:** Freund's actual disclosure (`freund-oss-security-2024-03-29.txt`) states: *"I am \*not\* a security researcher, nor a reverse engineer."* Saying he had "no security background" overstates his specific disclaimer; Freund is a principal software engineer working on PostgreSQL internals who disclaimed being a specialist vulnerability researcher/reverse engineer, not someone with zero security knowledge.
* **Fix:** Rephrase to reflect his words more closely: `"and an engineer who was not a security researcher caught it..."` or `"an engineer without a security research background"`.

---

### Finding 5: Inconsistent hyperlink formatting in Reading list (Readability / Sources completeness)
* **Severity:** Low
* **Location:** Line 102 (`Reading`): `"Dan Goodin, Ars Technica, 29 March 2024;"`
* **Problem:** The Ars Technica citation lacks an anchor tag link, whereas the surrounding citations for WIRED and Malka include full hyperlinks, and the Ars Technica URL is indexed in `resources/sources/03/SOURCES.md`.
* **Fix:** Wrap the title in an `<a>` tag: `<a href="https://arstechnica.com/security/2024/03/backdoor-found-in-widely-used-linux-utility-breaks-encrypted-ssh-connections/">"Backdoor found in widely used Linux utility targets encrypted SSH connections"</a>, Ars Technica, 29 March 2024;`.
