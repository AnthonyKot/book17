# Sources — chapter 03 (A03:2025 Software Supply Chain Failures — xz-utils, 2024)

All fetched 2026-09-01 unless a row says otherwise (Wikipedia re-fetched and the retellings word-checked 2026-09-02; git receipts re-run 2026-09-02). Excerpts saved alongside as `.txt` where the licence allows
(mailing lists, commits, advisories, OWASP, CC BY-SA pages: freely; press: only the
sentences quoted). Nothing in this chapter rides on memory; each row below names the
part used.

## Primary — the break

| Document | What it is | URL | Used |
|---|---|---|---|
| Andres Freund, "backdoor in upstream xz/liblzma leading to ssh server compromise", oss-security, 29 Mar 2024 08:51 -0700 | mailing-list post; the disclosure | https://www.openwall.com/lists/oss-security/2024/03/29/4 | whole post: symptoms, tarball-vs-git, Makefile hook, test files, trigger conditions, sshd timings, libsystemd link, "not a security researcher", committer assessment. Excerpt: `freund-oss-security-2024-03-29.txt` (extractor line and attachments omitted on purpose) |
| NVD, CVE-2024-3094 | CVE record (Red Hat CNA) | https://nvd.nist.gov/vuln/detail/CVE-2024-3094 | description, published 2024-03-29, CVSS 3.1 base 10.0, CWE-506. Excerpt: `nvd-cve-2024-3094.txt` |
| xz git repository (clone of tukaani-project/xz, HEAD 28a66a3d of 2026-08-20; master never rebased per tukaani.org) | commits, tags, diffs | https://github.com/tukaani-project/xz | commits 6468f7e4, 8ace358d, e2870db5, 3060e107, 4323bc3e, cf44e4b7, 2d7d862e, 328c52da, e5faaebb, 72d2933b, 82ecc538, a3a29bbd, 0b4ccc91, 6e636819, f9cf4c05, e93e13c8, 689ae242, 6b63c4c6; tags v5.4.2–v5.6.1 (tagger Jia Tan), v5.6.2; `git ls-tree v5.6.0 m4/`; per-author commit counts; NEWS at v5.6.2. Output: `xz-git-history.txt` |
| xz git repository — tag objects and URL commits (same clone; run 2026-09-01, re-run 2026-09-02) | raw `git cat-file tag` / `git log` / `git show` output | https://github.com/tukaani-project/xz | tagger and `BEGIN PGP SIGNATURE` lines for v5.4.0–v5.6.2 and per-tag signature-block counts (signatures not verified against a key); the four URL commits of 2024-01-19 (22d86192, 6b63c4c6, fce47580, c26812c5) with stats and the c26812c5 diff; first committer-Jia-Tan commits (`--reverse | head -3`); first author commits; 2023 per-author counts; last Collin commits before v5.6.0; `git log --all -- m4/build-to-host.m4` (empty). Output: `xz-git-tags-and-url-commits.txt` |
| Lasse Collin, "XZ Utils backdoor", tukaani.org (last updated 2025-01-17) | maintainer's statement | https://tukaani.org/xz-backdoor/ | Facts section: tarballs created and signed by Jia Tan; access split (tukaani.org vs GitHub/xz.tukaani.org); email forwarding cut 2024-03-30; decision not to rebase; clean releases 2024-05-29. Excerpt: `tukaani-xz-backdoor-statement.txt` |
| Lasse Collin, "XZ Utils review notes", v1.0, 2024-05-29 | maintainer's commit-by-commit review | https://tukaani.org/xz-backdoor/review.html | 2024-01: "first commit preparing for the backdoor" (RISC-V test files); 2024-02: m4/.gitignore ("Modified build-to-host.m4 had the backdoor trigger"), "Backdoor files", Landlock "." sabotage; 2024-03: "one of the backdoor commits", "More backdoor commits". Excerpt: `tukaani-review-notes-excerpts.txt` |
| xz-devel, thread "XZ for Java", June 2022 (mail-archive.com) | mailing-list posts | https://www.mail-archive.com/xz-devel@tukaani.org/msg00566.html, msg00567, msg00568, msg00569, msg00571 | Jigar Kumar 7 and 14 Jun; Lasse Collin 8 Jun ("unpaid hobby project", "Jia Tan ... perhaps he will have a bigger role") and 29 Jun ("practically a co-maintainer already"); Dennis Ens 21 Jun. Excerpt: `xz-devel-2022-06-maintainer-thread.txt` |
| Debian Security Advisory DSA-5649-1, 29 Mar 2024 | distribution advisory | https://lists.debian.org/debian-security-announce/2024/msg00057.html | affected suites and versions (5.5.1alpha-0.1 uploaded 2024-02-01 to 5.6.1-1); revert to 5.4.5. Excerpt: `debian-dsa-5649-1.txt` |
| Red Hat, "Urgent security alert for Fedora Linux 40 and Fedora Rawhide users", 29 Mar 2024, updated 30 Mar | vendor advisory | https://www.redhat.com/en/blog/urgent-security-alert-fedora-41-and-rawhide-users | Fedora 40 beta shipped xz-libs-5.6.0-1 and -2; "the Git distribution lacks the M4 macro". Excerpt: `redhat-fedora-alert-2024-03-29.txt` |
| openSUSE News, "openSUSE addresses supply chain attack against xz compression library", 29 Mar 2024 | distribution advisory | https://news.opensuse.org/2024/03/29/xz-backdoor/ | Tumbleweed/MicroOS carried 5.6.x 7–28 March; reinstall advice for internet-exposed SSH. Excerpt: `opensuse-news-2024-03-29.txt` |
| Solar Designer, "Re: backdoor in upstream xz/liblzma…", oss-security, 17 Apr 2024 | mailing-list update | https://www.openwall.com/lists/oss-security/2024/04/16/5 | OpenSSH 9.8 notify without libsystemd (bug 2641); systemd dlopen of compression libs (#32028); April analysis summary. Excerpt: `oss-security-2024-04-16-solar-designer.txt` |
| amlweems/xzbot README | analysis tooling (in NVD references) | https://github.com/amlweems/xzbot | that the payload gates on a hard-coded Ed448 key. Excerpt (key bytes omitted): `xzbot-readme-excerpt.txt` |

## Primary — the defense

| Document | What it is | URL | Used |
|---|---|---|---|
| Vagrant Cascadian, "Reproducible Builds for recent Debian security updates", rb-general, 30 Mar 2024, and reply 003323 | mailing-list post | https://lists.reproducible-builds.org/pipermail/rb-general/2024-March/003321.html | what reproducibility was used for after disclosure (verifying Debian's builders), and its caveats. Excerpt: `rb-general-2024-03-30-cascadian.txt` |
| kpcyrd, "New supply-chain security tool: backseat-signed", rb-general, 3 Apr 2024 | mailing-list post | https://lists.reproducible-builds.org/pipermail/rb-general/2024-April/003337.html | "operate on VCS snapshots instead of tarballs"; Arch conversions "in response to the xz incident". Excerpt: `rb-general-2024-04-03-kpcyrd.txt` |
| Simon Josefsson, "Reproducible and minimal source-only tarballs", 13 Apr 2024 | maintainer's blog post (a maintainer's record of a change adopted) | https://blog.josefsson.org/2024/04/13/reproducible-and-minimal-source-only-tarballs/ | libntlm 1.8 ships a git-archive tarball; "tarballs with files that are not included in the git archive offer an opportunity". Excerpt: `josefsson-2024-04-13.txt` |
| OWASP Top 10:2025 A03 | the spine | resources/owasp/A03_2025-Software_Supply_Chain_Failures.txt | definition; "separation of duty"; "Prefer signed packages"; "unmaintained" bullet |

## Secondary — the folk story (named, not relied on for facts)

| Document | URL | Used |
|---|---|---|
| Andy Greenberg, "The Mystery of 'Jia Tan,' the XZ Backdoor Mastermind", WIRED, 3 Apr 2024 | https://www.wired.com/story/jia-tan-xz-backdoor/ | "spend two years politely and enthusiastically volunteering"; "lead open source steward"; "nagging emails"; "remains unclear"; "well-organized group"; "a lone Microsoft engineer"; "unlikely that Jia Tan is a real person". Word-presence check 2026-09-02: the 2,676-word article contains no "tarball", "release", "signed", "Landlock" or "sandbox". Quoted sentences only: `retellings-quoted-sentences.txt` |
| Dan Goodin, "Backdoor found in widely used Linux utility targets encrypted SSH connections", Ars Technica, 29 Mar 2024 | https://arstechnica.com/security/2024/03/backdoor-found-in-widely-used-linux-utility-breaks-encrypted-ssh-connections/ | headline; "not really affecting anyone in the real world" (Dormann); "February 23 update" (Red Hat email); "malicious install script that injected itself into functions used by sshd"; the tarball/git sentence; the correction note. Word-presence check 2026-09-02: no "Landlock" or "sandbox" in the article. Quoted sentences only in `retellings-quoted-sentences.txt` |
| Wikipedia, "XZ Utils backdoor", lede and §Background (CC BY-SA 4.0), as served by the MediaWiki API 2026-09-02 | https://en.wikipedia.org/wiki/XZ_Utils_backdoor | lede: "through OpenSSH"; "deliberately included into the software in February 2024"; "affecting both version 5.6.0 and 5.6.1"; "a campaign lasting years". §Background: "sock puppetry in a pressure campaign"; "suspected sock puppets"; "Microsoft employee and developer Andres Freund". The 2026-09-01 fetch had placed "Microsoft employee" and "sock puppetry" in the lede; the chapter cites the section each phrase is in on 2026-09-02. Excerpt: `wikipedia-xz-utils-backdoor-2026-09-02.txt` |
| Julien Malka, "How NixOS and reproducible builds could have detected the xz backdoor for the benefit of all", 20 Mar 2025 | https://luj.fr/blog/how-nixos-could-have-detected-xz.html | the title claim; the author's own footnote 5 and the nixpkgs-bootstrap conclusion. Quoted sentences only |

## Could not fetch / not used

- Ars Technica and WIRED refused the WebFetch tool; both were fetched with curl and only the quoted sentences were kept.
- No court or government document was found for this incident: nothing in the corpus charges anyone or attributes the account to a person or a state. The chapter states this as a dated limit of the collected record (claim `03-no-attribution`), not as a finding about the world.
- The xz-devel archive for 2022 was read at mail-archive.com; the tukaani.org list archive was not consulted separately.
