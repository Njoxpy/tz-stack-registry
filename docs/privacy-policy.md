# Privacy Policy

This registry exists to help developers — not to expose individuals or leak private information. This document defines what the project will and will not publish, and how to request corrections or removal.

## 1. What This Registry Contains

- Publicly observable facts about companies: technology stacks, infrastructure choices, sectors, and sourced references.
- Interview patterns, generalized and anonymized from candidate experiences.
- Links to public sources (job posts, engineering blogs, conference talks, public repositories).

That is the entire scope. Anything outside of it does not belong here.

## 2. What This Registry Never Contains

The following are **rejected on sight** and will be removed from any submission before merge:

- **Personal names** of employees, interviewers, recruiters, or candidates.
- **Contact details** — emails, phone numbers, LinkedIn profiles, social handles.
- **Screenshots, recordings, or verbatim quotes** from private interview rooms, Slack, email, or internal tools.
- **Internal architecture details** not disclosed publicly by the company (internal diagrams, service names, credentials, endpoints not in public docs).
- **Leaked documents** of any kind, including compensation bands not published by the company.
- **Identifying details** that could let a reader deduce who a testimony came from — team size, exact dates, project names, role titles that only one person holds.
- **Material covered by an NDA**, even if the contributor believes it is harmless.
- **Speculation or rumor** dressed up as fact.

If in doubt, leave it out. The registry is more valuable with fewer, higher-integrity entries than with volume.

## 3. Anonymization Rules for Interview Testimony

When a contributor shares an interview experience, apply these rules before submitting:

1. **Strip all names.** Yours, the interviewer's, the recruiter's, anyone mentioned in the conversation.
2. **Strip dates.** "Q1 2026" is acceptable; "March 14, 2026" is not.
3. **Generalize roles.** "A senior backend engineer" is acceptable; "the engineering lead for the payments team" is not if the team has only one lead.
4. **Paraphrase questions.** Rewrite in your own words. Do not copy-paste the exact wording from a take-home brief.
5. **Remove company-internal jargon.** Project codenames, internal service names, and product acronyms that are not public must be stripped or replaced with a generic description.
6. **Describe the shape of a task, not its contents.** "A coding challenge about wallet reconciliation, 90 minutes, take-home" is fine. "Here is the exact brief they sent me" is not.

A well-anonymized testimony reads as if it could have come from any of the last 20 candidates. If a current employee could read a testimony and identify who wrote it, it is not anonymized enough.

## 4. Contributor Consent

By submitting a contribution, you confirm that:

- The content is yours to share, or is drawn from a public source you have linked.
- Publishing it does not violate any NDA, employment agreement, or other legal obligation you are aware of.
- You license your contribution under the repository's MIT License (see the `LICENSE` file at the repository root).

Contributors may submit anonymously via a PR from a pseudonymous account. Maintainers will not demand real-name identification.

## 5. Data Subject Rights

### For individuals

If you believe content in this registry identifies you or contains information about you that should not be published, open an issue titled `PRIVACY REQUEST` or email the maintainers. We will:

1. Acknowledge within 7 days.
2. Remove or redact the content within 14 days if the claim is valid.
3. Not require you to prove your identity publicly — a private channel confirmation is enough.

### For companies

If you represent a company listed in this registry and you believe an entry is inaccurate, misrepresentative, or sourced improperly:

1. Open an issue titled `COMPANY CORRECTION — [Company Name]`.
2. State which claim is wrong and provide a public source for the correction.
3. Maintainers will update the entry within 14 days of verification.

A company may request full removal of its entry. Removal requests are honored, though maintainers may preserve a record that the entry once existed (without stack details) to prevent re-submission loops.

## 6. What Maintainers Commit To

- Review every PR against this policy before merging.
- Reject submissions that violate the anonymization rules, even if the contributor is well-intentioned.
- Take down in-violation content on discovery, without waiting for a formal request.
- Not monetize the registry in ways that require personal data.
- Not sell, transfer, or license the registry's data to third parties outside of the open-source license.

## 7. Changes to This Policy

Material changes to this policy will be announced via a pinned issue and a changelog entry in the repository. Contributors are expected to re-read this document after any such change.
