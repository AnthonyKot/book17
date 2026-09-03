1. **Record accuracy (Overstatement)**
   - **Location:** "Cisco says M.E.Doc let its responders inspect engineers' accounts, logs and code." (claim `08-cisco-access`)
   - **Problem:** The cited Cisco report states that M.E.Doc arranged "access to engineers and administrators who walked the team through the system and provided access to log files and code." It does not state that Cisco inspected the engineers' *accounts* themselves. An attacker had stolen an administrator's credentials, but claiming Cisco was allowed to inspect "engineers' accounts" overstates the access granted in the record.
   - **Fix:** Change "inspect engineers' accounts, logs and code" to "interview engineers and inspect logs and code" or "access engineers, logs and code."

2. **Ledger fairness (Straw man)**
   - **Location:** `The update-server shorthand makes 27 June sound like one poisoned download.` (Ledger row 4)
   - **Problem:** The ledger rules in `CONTEXT.md` §4 require that each row use "one specific folk claim (quoted or closely paraphrased from a named retelling)." This row is not a folk claim from a named source, but the author's own critique of the abbreviation used in the previous row. It acts as a straw man to introduce the `MISSING` verdict regarding the staged attack.
   - **Fix:** Either replace the left column with an attributed quote from a retelling that explicitly claims the attack was a single, one-time download event, or cut the row entirely (leaving the discussion of the stages exclusively in the prose).

3. **Ledger fairness (Unearned verdict)**
   - **Location:** `Darknet Diaries says Maersk had a functioning network after about nine days.` with verdict `OVERSTATED` (Ledger row 7)
   - **Problem:** The ledger grades Darknet Diaries' "about nine days" as `OVERSTATED` against Maersk's "ten days". Grading an explicit approximation ("about") that misses by just one day as "wrong in a way that matters" (the definition of `OVERSTATED`) is unfairly harsh. Even if "functioning" and "rebuilt" carry different technical nuances, calling the folk story an overstatement on these grounds is pedantic.
   - **Fix:** Regrade the row to `HOLDS`, acknowledging that "about nine" is a reasonable colloquial fit for a ten-day rebuild, or cut the row if it doesn't provide a meaningful contrast.
