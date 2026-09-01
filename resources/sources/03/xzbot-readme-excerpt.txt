amlweems/xzbot README (analysis tooling for CVE-2024-3094; listed in NVD references). URL: https://github.com/amlweems/xzbot  Fetched 2026-09-01. Excerpt: description lines only; the key bytes and demo are omitted deliberately.

# xzbot

Exploration of the xz [backdoor](https://www.openwall.com/lists/oss-security/2024/03/29/4) (CVE-2024-3094).
Includes the following:
* [honeypot](#honeypot): fake vulnerable server to detect exploit attempts
* [ed448 patch](#ed448-patch): patch liblzma.so to use our own ED448 public key
* [backdoor format](#backdoor-format): format of the backdoor payload
* [backdoor demo](#backdoor-demo): cli to trigger the RCE assuming knowledge of the ED448 private key

![xzbot demo](assets/demo.png)



# ed448 patch

The backdoor uses a hardcoded ED448 public key for signature validation and
decrypting the payload. If we replace this key with our own, we can trigger
the backdoor.

The attacker's ED448 key is:
[code block omitted]
