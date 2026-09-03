1. **Ledger fairness (High Severity)**
   - **Location:** Ledger Row 5 ("Attackers 'accessed Adobe customer IDs...'" from Adobe, 3 Oct 2013), Ledger Row 6 ("'every one of the 150+ million customers...'" from Stajano et al.), and Ledger Row 8 ("'the theft of approximately 6.5 million passwords'" from LinkedIn, 12 June 2012).
   - **Problem:** The chapter uses primary records (two vendor incident announcements and a technical paper) in the "Folk story" column. `CONTEXT.md` and `AGENT.md` explicitly mandate that the folk story must be identified from "named retellings" (e.g., Wired, Krebs, Wikipedia) so the left column is a real folk claim representing popular understanding. Vendor statements and academic papers belong in the right column as part of the primary/technical record.
   - **Fix:** Remove these three rows, or replace their left columns with quotes from named secondary retellings that make equivalent claims.

2. **Mechanism accuracy (Low Severity)**
   - **Location:** "Three people with the same password share a row of ciphertext."
   - **Problem:** The terminology is imprecise. In a database, users do not share a single *row*; they each have independent rows, but the *value* of the ciphertext in that column is identical for users with the same password. The whiteboard illustration immediately above the sentence makes this visually clear, but the phrasing itself could trip up a security engineer.
   - **Fix:** Change the phrasing to "Three people with the same password share the same ciphertext value" or "have identical ciphertext in their rows".
