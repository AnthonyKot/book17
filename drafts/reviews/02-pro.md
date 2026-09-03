### 1. Record accuracy / Ledger fairness (Severity: High)
* **Location:** `The ledger`, row 7 ("MongoDB 'blamed the attacks... on database owners'")
* **Problem:** The folk claim explicitly quotes ZDNet (2020) naming *Davi Ottenheimer* as the one who blamed users ("Back in 2017, Davi Ottenheimer... blamed the attacks"). However, the record column entirely omits Ottenheimer's September 2017 post. Instead, the verdict argues: "Nine weeks after telling users to set the bind address, the vendor filed a ticket to set it for them." This "nine weeks" timeline relies on *Nilsson's* January 2017 post. Ottenheimer blamed users six months *after* the ticket was filed. By swapping the speaker to fix the timeline, the row creates a straw man and invalidates the "OVERSTATED" verdict.
* **Fix:** Either evaluate Ottenheimer's actual September post against the ticket timeline, or change the folk claim to target the January blame (Nilsson) instead of the ZDNet quote.

### 2. Record accuracy (Severity: High)
* **Location:** `The mechanism`, third paragraph ("Matherly's 2015 census: ... and 40 per cent of exposed instances were on 1.8.1.")
* **Problem:** The chapter applies the 40% figure to the entire exposed population (30,000 instances). In the source (`shodan-2015-07-18.txt`), Matherly states this immediately after discussing a specific subset of 319 instances named `hackedDB` ("The name that really sticks out is hackedDB... The interesting thing to note when looking at the results is that 40% of the instances are running a very old version"). The December 2015 post confirms the most popular version overall was 3.0.7 (3,010 instances), proving 1.8.1 could not account for 12,000 instances. This is a severe overstatement of the source.
* **Fix:** Remove the 1.8.1 statistic entirely, or clarify that it only applied to the `hackedDB` subset.

### 3. Mechanism accuracy / Readability (Severity: Medium)
* **Location:** `The mechanism`, fourth paragraph ("Who had none of the three? Anyone on a tarball, anyone on a version older than 2.6...")
* **Problem:** The chapter asks "Who had none of the three?" to describe users who were still exposed. However, it just defined the "first default" as the binary's `0.0.0.0` (listen everywhere) setting. Users on tarballs or older versions did not have "none of the three" defaults; they explicitly had the *first* default.
* **Fix:** Rephrase to something logically sound, such as "Who fell through to the first default?" or "Who was still listening everywhere?"

### 4. OWASP fit (Severity: Medium)
* **Location:** `The mechanism`, first paragraph ("OWASP defines the category as...")
* **Problem:** The chapter quotes the category definition but fails to state where the incident does not fit the category cleanly. The OWASP Top 10 applies to web applications, whereas MongoDB is a database server directly exposed to the internet.
* **Fix:** Add a sentence noting that while MongoDB is not a web application, the principles of the "Security Misconfiguration" category apply directly to its deployment.

### 5. Mechanism accuracy (Severity: Low)
* **Location:** `The mechanism`, fourth paragraph ("The third default is 3.6's, and it is the same line of code with a different constant... That is the whole change.")
* **Problem:** The chapter claims the single constant change was "the whole change" for the 3.6 default. This contradicts the chapter's own `The defense` section, which correctly notes from the record (SERVER-28229) that the fix also included a startup warning and a `--bind_ip_all` flag.
* **Fix:** Clarify that this was the whole change *to the listener binding code*, or remove "That is the whole change."
