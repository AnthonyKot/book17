## 1. Fairness to named people (Severity: High)
**Location:** *"On 18 June she had written to a stranger on Twitter: 'Ive basically strapped myself with a bomb vest, fucking dropping capitol ones dox and admitting it. I wanna distribute those buckets i think first'."*
**Problem:** The chapter uses this quote (drawn from the complaint) to show intent to distribute data. However, Judge Sung's dissent in the Ninth Circuit opinion explicitly notes this DM was sent during a severe mental health crisis and expressed suicidal ideation ("I dont care if its jail or death. Prefer to die"). Stripping this context paints the subject as purely malicious or boasting, which violates the instruction to be fair to named people, especially since her mental health was a mitigating factor in her sentence. 
**Fix:** Include the context of her mental health distress, or rely on a different detail (like the Slack messages) to establish the tie to the gist without quoting the crisis DM out of context.

## 2. Record accuracy (Severity: High)
**Location:** *"The first command asked a firewall for its own credentials."*
**Problem:** This overstates the cited source and is technically inaccurate. The complaint (¶11) simply says the command "obtained security credentials for an account known as *****-WAF-Role". The command did not ask the firewall; it asked the cloud metadata service for the credentials via the firewall (which acted as a vulnerable proxy).
**Fix:** Change to "The first command asked the cloud metadata service for the firewall's credentials," or use the complaint's exact wording: "The first command obtained the firewall's own credentials."

## 3. Mechanism accuracy (Severity: Medium)
**Location:** The whiteboard code snippet showing `target = request.param("url")` and `return http.get(target)`.
**Problem:** The chapter attributes the Capital One breach to a misconfigured WAF. A WAF is a reverse proxy, which forwards requests based on routing rules, not by reading a `url` parameter from an incoming request. While the snippet perfectly illustrates an application-level SSRF, a security engineer would wince at it being used to explain a proxy misconfiguration. 
**Fix:** Provide a configuration example of an open reverse proxy, or explicitly note that while the code snippet shows an application-level SSRF, a WAF SSRF relies on proxy routing misconfigurations rather than application code.

## 4. Mechanism accuracy (Severity: Medium)
**Location:** *"Point `target` at the metadata address and the response is the instance role's temporary key, secret and session token."*
**Problem:** Querying the base metadata address (`169.254.169.254` or `/latest/meta-data/`) does not return the credentials; it returns a directory listing. An attacker must query a specific path containing the role name (e.g., `/latest/meta-data/iam/security-credentials/ROLE-NAME`) to get the keys. 
**Fix:** Clarify that the target must be pointed at the specific metadata path for the role's security credentials, not just the base metadata address.

## 5. Record accuracy (Severity: Low)
**Location:** *"On 26 June, on a Slack channel she organised..."*
**Problem:** The complaint (¶18) states that "the Slack channel's Meetup group listed 'Paige Thompson (erratic)' as organizer," not that she organized the Slack channel itself. This is a slight overstatement of the source.
**Fix:** Change to "on a Slack channel linked to a Meetup group she organised" or simply "on a Slack channel".

## 6. Readability (Severity: Low)
**Location:** The paragraph starting *"Each layer maps onto one of the four boxes. Against an open WAF..."*
**Problem:** This is a dense 139-word wall paragraph that strings together four distinct technical defenses ("Against an open WAF...", "Against an open reverse proxy...", "Against an SSRF...", "And against an instance misconfigured..."). It requires re-reading to parse the different scenarios.
**Fix:** Break the four defenses into a bulleted list.
