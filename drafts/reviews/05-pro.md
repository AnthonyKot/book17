### 1. Mechanism accuracy / Reader (Severity 1)
**Location:** `string.Format("Email={0}", (object) func("Email"))` (in the `post-patch: a builder plus named values` code block)
**Problem:** The chapter presents this as a standalone statement. In C#, `string.Format` returns a string without side effects, so an unassigned call is syntactically meaningless. In the actual Rapid7 patch diff, this line was an element within a `List<string> values = new List<string>() { ... };` initialization block that was abbreviated away. A security engineer reading this example would wince because the data flow is broken and the code snippet is invalid.
**Fix:** Restore the array initialization or the method call that consumes the formatted string so the mechanism reflects the actual patch and is comprehensible to the reader.

### 2. Ledger fairness (Severity 2)
**Location:** "An attacker could send a crafted payload to an application endpoint (Progress’s 9 and 15 June advisories). The ordinary mental picture is a malicious value in a form field." (Ledger row 3)
**Problem:** The chapter uses a primary vendor advisory combined with an invented "ordinary mental picture" as the folk story. The incident rules explicitly dictate that the folk story must be "quoted or closely paraphrased from a named retelling" to ensure the left column is real, not a straw man.
**Fix:** Replace this claim with an actual quote from a named secondary source (e.g., TechCrunch, TechTarget) that makes this assumption about the route, or remove the row if no retelling made it.

### 3. Ledger fairness (Severity 2)
**Location:** "SQL injection succeeds because developers fail to treat user content as potentially malicious (CISA/FBI Secure by Design alert)." (Ledger row 4)
**Problem:** The chapter uses a primary regulator document (the CISA/FBI alert) in the left column. This violates the ledger rules requiring the folk story to be sourced from named secondary retellings, essentially turning a primary source into a straw man.
**Fix:** Quote a named secondary source that makes this claim about developer failure, or remove the row.

### 4. Ledger fairness (Severity 2)
**Location:** "Progress allowed SQL-injection flaws to remain for years (plaintiffs’ Bellwether Complaint, as recited in MDL Order 22)." (Ledger row 8)
**Problem:** A legal complaint cited from a court order is a primary source for allegations, not a "folk story" from the public narrative. Using it in the left column violates the rule that folk claims must come from named retellings.
**Fix:** Attribute this claim to a named retelling if the press reported on the flaw's age, or remove the row.
