# Interview Guidelines

How to turn the data in this registry into a preparation plan for Tanzanian technical interviews.

## 1. How to Read a `stack.json`

A stack is a signal of what the company values. Read it in this order:

1. **`backend`** — dictates algorithmic and design-pattern style questions. A Go shop and a Java shop will interview very differently.
2. **`database`** — predicts the depth of data-modeling and SQL questions. PostgreSQL-heavy companies ask about indexing and transactions; MongoDB-heavy ones ask about document design and consistency.
3. **`cloud_infra`** — signals system design scope. AWS + Kubernetes means they expect you to reason about deployment, scaling, and failure modes.
4. **`mobile_tech`** — if populated, expect mobile-specific questions (offline sync, low-bandwidth UX, state management).
5. **`frontend`** — the lightest signal for backend roles, heaviest for fullstack roles.

## 2. The Two Axes of a Tanzanian Interview

Most interviews here split cleanly along two axes. Prepare for both.

### A. System Design

Focus on problems the company actually faces. For Tanzanian companies this usually means:

- **Unreliable networks.** How does your system behave on 3G or intermittent connectivity?
- **Mobile money integration.** Callbacks, idempotency, and reconciliation with M-Pesa, Tigo Pesa, Airtel Money, and Halopesa.
- **USSD.** Stateful session flows over a stateless protocol.
- **Multi-currency.** TZS, USD, KES cross-border flows (especially for fintech).
- **Concurrency and transactional integrity.** Double-spend prevention, atomic balance updates.

Typical prompts:
- "Design a wallet service that supports top-ups from mobile money."
- "Design an inventory system for a chain of shops with unreliable internet."
- "Design a ride-hailing dispatch system for Dar es Salaam."

### B. Practical Coding

These are hands-on exercises, often timed. Expect:

- Consume a public REST API and transform the response.
- Implement a small CRUD service with a database.
- Write SQL for a multi-table reporting query.
- Build a component that handles loading, error, and offline states.

Practice against the stack listed in `stack.json` — if the company uses Django, do the exercise in Django, not Flask.

## 3. A Seven-Day Preparation Loop

1. **Day 1** — Read the company's `stack.json` and `interview-questions.md`. Find one engineering blog post or conference talk from the company.
2. **Day 2** — Review fundamentals for their primary backend language and database.
3. **Day 3** — Build a small project using two of their core technologies.
4. **Day 4** — Solve three system-design prompts from this repo aloud, recording yourself.
5. **Day 5** — Do two timed coding challenges in their stack.
6. **Day 6** — Prepare questions for the interviewer, grounded in something specific you saw on their blog or GitHub.
7. **Day 7** — Rest. Reviewing at low energy reinforces mistakes.

## 4. Interview-Day Tactics

- **Narrate your thinking.** Silence reads as "stuck" even when you're making progress.
- **State assumptions.** "I'm assuming users can retry a failed payment — is that correct?" Prevents you from solving the wrong problem.
- **Write trade-offs, not verdicts.** "Postgres gives us transactions; Mongo gives us flexible schemas. For a ledger, I'd pick Postgres because X." Beats "Postgres is better."
- **For mobile money questions, always mention idempotency keys and reconciliation jobs.** These are the two things that separate juniors from seniors in Tanzanian fintech interviews.

## 5. What This Repo Does Not Replace

- Reading the official docs for the technologies listed.
- Building real projects.
- Talking to engineers who work at the company.

Use the registry as a map, not as the territory.
