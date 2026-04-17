# Fintech

Companies operating in payments, banking, lending, mobile money, and financial infrastructure in Tanzania.

## What to Expect in Interviews

- Heavy emphasis on **transactional integrity**: atomicity, idempotency, reconciliation.
- **Mobile money integration** patterns (M-Pesa, Tigo Pesa, Airtel Money, Halopesa).
- **API security** (signature verification, replay protection, ISO 8583 for card rails).
- Performance under load — peak times around salary days and public holidays.

## Adding a Company

1. Copy `_template/` to a new folder named after the company (lowercase, hyphenated).
2. Fill in `stack.json` — must validate against the root `schema.json`.
3. Fill in `interview-questions.md` following the template structure.
4. Add at least one source to `stack.json` (see [contribution-standards.md](../../docs/contribution-standards.md)).
