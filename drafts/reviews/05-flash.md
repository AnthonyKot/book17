### 1. High — Huntress’s early analysis is cited as describing “the same division of labor” when it stated the reverse

* **Category:** Record accuracy / Mechanism accuracy
* **Location:** “Huntress described the same division of labor: the ISAPI component performed SQL injection under particular headers, while `guestaccess.aspx` prepared a session.” ([chapter](file:///home/diablo/book17/chapters/05-moveit.html#L41); also [claims row 26](file:///home/diablo/book17/checks/claims/05.tsv#L26)).
* **Problem:** Rapid7’s analysis ([`rapid7-analysis-cve-2023-34362.txt:18-35`](file:///home/diablo/book17/resources/sources/05/rapid7-analysis-cve-2023-34362.txt#L18-L35)) established that the ISAPI request (`moveitisapi.dll` calling `machine2.aspx`) was used to populate session variables via `SetAllSessionVarsFromHeaders()`, while `guestaccess.aspx` called `LoadFromSession()` and routed into `UserGetUsersWithEmailAddress()` where the SQL injection occurred. Huntress’s early post ([`huntress-2023-06-01.txt:26`](file:///home/diablo/book17/resources/sources/05/huntress-2023-06-01.txt#L26)) initially stated the opposite: *“moveitisapi.dll is used to perform SQL injection when requested with specific headers, and guestaccess.aspx is used to prepare a session”*. Describing Huntress as providing “the same division of labor” conflates two conflicting accounts and introduces a mechanism error about which component handled session preparation versus query execution.
* **Fix:** Revise the sentence to state that both Huntress and Rapid7 identified the ISAPI handler and `guestaccess.aspx` as the two linked components in the chain, while noting that early reports differed on which component triggered the SQL injection until Rapid7 traced the decompiled call path from `guestaccess.aspx` to `UserGetUsersWithEmailAddress()`.

---

### 2. High — Post-patch code snippet contains an orphan statement and omits `AddAndToWhere()`

* **Category:** Mechanism accuracy
* **Location:** The post-patch code block ([chapter](file:///home/diablo/book17/chapters/05-moveit.html#L70-L83)):
  ```csharp
  string.Format("Email={0}", (object) func("Email"))
  where.WithParameter("Email", (object) EmailAddress);
  where.WithParameter("FirstEmail", (object) string.Format("{0},%", (object) str));
  where.WithParameter("MiddleEmail", (object) string.Format("%,{0},%", (object) str));
  where.WithParameter("LastEmail", (object) string.Format("%,{0}", (object) str));

  this.siGlobs.objWrap.DoReadQuery(
      where.GetQuery(), where.Parameters, ref MyRS, true);
  ```
* **Problem:** Line 76 (`string.Format("Email={0}", (object) func("Email"))`) is an unused, disconnected expression statement. In Rapid7’s published decompilation ([`rapid7-analysis-cve-2023-34362.txt:96-128`](file:///home/diablo/book17/resources/sources/05/rapid7-analysis-cve-2023-34362.txt#L96-L128)), that string was added to a `List<string> values` collection, and the combined clauses were attached to the builder with `where.AddAndToWhere("(" + string.Join(" OR ", values) + ")")`. Because `AddAndToWhere` was omitted from the snippet, the code never shows how the parameterized `Email` placeholder is actually attached to `where`. A developer reading the snippet to understand parameterization sees parameter values registered via `WithParameter()`, but no corresponding WHERE clause placeholders attached to the query builder.
* **Fix:** Update the code block to include `values` and `where.AddAndToWhere(...)` so the post-patch example demonstrates both parameter binding and WHERE clause attachment.

---

### 3. Medium — Pre-patch code snippet is presented as disconnected fragments without array or format context

* **Category:** Mechanism accuracy / Readability
* **Location:** The pre-patch code block ([chapter](file:///home/diablo/book17/chapters/05-moveit.html#L55-L65)):
  ```csharp
  // pre-patch: one formatted SQL string
  (object) "Email='{2}' OR "
  (object) this.siGlobs.objUtility.BuildLikeForSQL(
      "Email", "{1},%", bEscapeAndConvertMatchString: false)

  (object) InstID,
  (object) this.siGlobs.objUtility.EscapeLikeForSQL(EmailAddress),
  (object) EmailAddress

  this.siGlobs.objWrap.DoReadQuery(
      Conversions.ToString(obj), ref MyRS, true);
  ```
* **Problem:** The block presents five floating cast expressions with no enclosing array definition or `Format` invocation, followed by a call referencing an undeclared variable `obj`. While the prose explains that these are selected decompiled expressions from `objArray`, presenting raw array elements as standalone statements makes the code difficult to parse on a whiteboard without knowing what `obj` or the indices correspond to.
* **Fix:** Add context comments or explicit array assignments (e.g. `// format string elements:` and `// format arguments ({0}=InstID, {1}=escaped, {2}=raw):`) so the relationship between the array elements, `{1}`, `{2}`, and `DoReadQuery` is immediately obvious.

---

### 4. Medium — Ledger row 3 folk column attributes an editorial assumption to vendor advisories

* **Category:** Ledger fairness
* **Location:** Ledger row 3, Folk story column ([chapter](file:///home/diablo/book17/chapters/05-moveit.html#L115)): “An attacker could send a crafted payload to an application endpoint (Progress’s 9 and 15 June advisories). The ordinary mental picture is a malicious value in a form field.”
* **Problem:** Under CONTEXT §4, folk claims must be quoted or closely paraphrased from named retellings. Progress’s 9 and 15 June advisories are primary vendor documents using standard boilerplate (*“submit a crafted payload to a MOVEit Transfer application endpoint”*), and neither claims the input came through a form field. The second sentence (*“The ordinary mental picture is a malicious value in a form field”*) is the chapter’s editorial assumption rather than a documented retelling.
* **Fix:** Quote a secondary retelling (such as TechCrunch or general reporting) that described the vulnerability as a direct web-form or input-field submission, or frame the folk column as the generic perception created by boilerplate advisory language.

---

### 5. Low — Lede compresses the 31 May advisory and patch release sequence

* **Category:** Record accuracy
* **Location:** “On 31 May 2023, Progress warned MOVEit Transfer customers about a critical vulnerability and published fixes for supported versions. <!-- CHECK: 05-first-advisory -->” ([chapter](file:///home/diablo/book17/chapters/05-moveit.html#L25)).
* **Problem:** The earliest archived capture of Progress's 31 May advisory ([`progress-kb-advisory-2023-05-31-cve-2023-34362.txt:33`](file:///home/diablo/book17/resources/sources/05/progress-kb-advisory-2023-05-31-cve-2023-34362.txt#L33), captured 2023-06-01 00:22 UTC) shows the initial alert instructed customers to apply immediate mitigations *“while our team produces a patch”* and noted *“Patches for all supported MOVEit Transfer versions are being tested and links will be made available below as they are ready.”* While Progress's Revision History and Form 8-K confirm supported fixes were posted on 31 May, phrasing the sentence as "warned... and published fixes" implies the initial warning and patch download links appeared simultaneously.
* **Fix:** Qualify the lede sentence: “On 31 May 2023, Progress warned MOVEit Transfer customers about a critical vulnerability and released fixes for supported versions later that day.”

---

### 6. Low — Lede conclusion overstates the explanatory scope of a single function

* **Category:** Readability / Tone
* **Location:** “One function explains both the break and the defense.” ([chapter](file:///home/diablo/book17/chapters/05-moveit.html#L25)).
* **Problem:** The exploit chain required multiple components across two functions (`SetAllSessionVarsFromHeaders()` and `UserGetUsersWithEmailAddress()`) as well as ISAPI routing, while the remediation required five SQLi CVE patches over five weeks. The chapter itself later stresses that repairing one function was only the first step and did not certify the product.
* **Fix:** Adjust the sentence to: “That function illustrates the mechanics of both the break and the defense.”
