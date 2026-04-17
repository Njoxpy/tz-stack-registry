# Contribution Standards

The value of this registry is directly proportional to the quality of its data. One rumor-based entry poisons the well for every developer who relies on it to prepare for an interview. Submissions are held to an **Elite Standard**.

## 1. Proof of Stack (Non-Negotiable)

Every `stack.json` entry must include at least one verifiable source in the `sources` array. Accepted source types:

| Type                 | Example                                                      | Strength  |
| -------------------- | ------------------------------------------------------------ | --------- |
| `job_post`           | Link to a live or archived job description listing technologies | Strong    |
| `engineering_blog`   | Company engineering blog post describing their stack         | Strongest |
| `conference_talk`    | Recorded talk or slides by a company engineer                | Strong    |
| `github`             | Public repositories owned by the company                     | Strong    |
| `employee_testimony` | Anonymous summary from a verified current or former employee | Moderate  |

**Rejected:**

- "I heard they use X."
- Screenshots without source URLs.
- LinkedIn profiles of individual engineers (a single engineer's skills ≠ a company's stack).
- Testimonies that violate NDAs or name individuals.

## 2. Data Integrity Rules

- `company_name` must match the official company name exactly.
- `industry` must match the parent folder under `/sectors`.
- Every technology listed must be a real, named technology (no vague entries like `"custom framework"` or `"various"`).
- `last_verified` must be set to the date of submission (ISO-8601 format: `YYYY-MM-DD`).
- Do not list a technology unless at least one source confirms it.

## 3. Folder and File Conventions

- Company folder name: lowercase, hyphenated, no spaces. Example: `nala-pay/`, not `NALA Pay/`.
- Required files in every company folder:
  - `stack.json`
  - `interview-questions.md`
- Do not commit draft files, screenshots, or PDFs into company folders.

## 4. Markdown Formatting Rules

- Use ATX-style headers (`#`, `##`, `###`). No setext (`===`) headers.
- Wrap code, technology names, and file paths in backticks: `` `PostgreSQL` ``, `` `stack.json` ``.
- Use fenced code blocks with language tags (`` ```python ``, `` ```json ``) for code samples.
- One blank line between sections. No trailing whitespace.
- Line length: soft target of 100 characters. No hard limit inside code blocks.

## 5. Interview Questions Standard

- Organize questions by seniority: **Junior**, **Mid**, **Senior**.
- Each question must be:
  - Specific enough to be useful (avoid "Explain OOP").
  - Phrased as it was actually asked, where possible.
  - Tagged with the category: `Technical Screening`, `Coding Challenge`, or `System Design`.
- Never include proprietary information, internal codebase details, or anything that violates an NDA.

## 6. Review Process

- Every PR is reviewed against this document before merge.
- A maintainer may request additional sources if a claim is ambiguous.
- Entries without sufficient proof are closed, not merged with a "TODO".

## 7. Updating Existing Entries

- Stacks change. When submitting an update, explain *what* changed and *why* (new source, migration announcement, etc.) in the PR description.
- Update `last_verified` on every change.
- Do not remove historical interview questions unless they are demonstrably incorrect.
