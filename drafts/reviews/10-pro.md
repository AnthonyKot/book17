1. **Record accuracy (Contradiction of sources)**
   * **Location:** "On 21 February 2014 Apple shipped iOS 7.0.6, iOS 6.1.6 and, four days later in the same batch of notes, OS X 10.9.2."
   * **The problem:** The claim that OS X 10.9.2 shipped "four days later" introduces a date from memory that contradicts the cited documents and the chapter's own claims file (`10-apple-ship-date`), which states all three shipped on 21 Feb 2014. The cited Langley post explicitly notes he confirmed the fix in 10.9.2 on February 22.
   * **What would fix it:** Remove the phrase "four days later" and state that all three shipped together as supported by the provided record, or find and cite a reliable document that confirms the exact later release date for OS X 10.9.2.

2. **Record accuracy & Ledger fairness (Overstating the source)**
   * **Location:** Prose: "...turned an estimated 8.5 million Windows machines into blue screens." Ledger row 5: `"roughly 8.5 million systems crashed" (Wikipedia lede)` evaluated with a `HOLDS` verdict.
   * **The problem:** The cited Microsoft document states the update "affected 8.5 million Windows devices," not that every single one experienced a blue screen/crash. The chapter overstates the record by mapping a specific technical state (crashing/BSOD) to the entire population count. Consequently, evaluating the Wikipedia claim of 8.5 million *crashes* as `HOLDS` is unearned.
   * **What would fix it:** In the prose, change "turned an estimated 8.5 million Windows machines into blue screens" to "affected an estimated 8.5 million Windows devices." In the ledger, change the verdict to `OVERSTATED` and note that the record explicitly counts affected devices, not confirmed crashes.

3. **Fairness to named people (Attributing motive and emotion)**
   * **Location:** "The review says so with some pride: 'Customers have complete control...'" and "...the CEO's first statement shows how much that version is feared:"
   * **The problem:** The text attributes emotional states ("pride") and motives ("feared") to CrowdStrike and its CEO that are not present in the cited documents. This violates the strict rule against speculating about motive, competence, or character beyond what a document literally states. 
   * **What would fix it:** Remove the emotional attributions. Change "with some pride" to "emphasizes" or "states", and rephrase the CEO setup to focus on the technical tradeoff (e.g., "The CEO's first statement highlights why a security product cannot fail open:").

4. **Mechanism accuracy (Variable initialization state)**
   * **Location:** "If the answer is 'whatever the variable held', and the variable starts at success, you have Apple's bug without the duplicate line."
   * **The problem:** The explanation implies the status variable in Apple's code was explicitly initialized to a success state. In `sslKeyExchange.c`, `OSStatus err;` was uninitialized; it only held a success value at the point of the stray jump because the immediately preceding hash update step had succeeded and overwritten the variable with `0`. A security engineer would note the distinction between an explicitly initialized variable and one that merely retains a prior operation's status.
   * **What would fix it:** Change "and the variable starts at success" to "and the variable holds the success of a previous step."
 all used a wildcard in the field that mattered; `<!-- CHECK: 10-cs-12-tests -->` Finding 5 concedes that the instance was validated but never run in the interpreter, and adds that step. `<!-- CHECK: 10-cs-instance-testing -->`"
* **Problem:** The sentence feels dense and requires re-reading to parse what "and adds that step" means (it means adding the step of running the instance in the interpreter). 
* **Fix:** Split into two sentences and clarify the addition. Example: "The twelve automated tests that passed the Template Type all used a wildcard in the field that mattered. Finding 5 reports that the instance was validated but never run in the interpreter, and adds that requirement to the test suite."
