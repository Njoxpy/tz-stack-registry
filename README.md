# tz-stack-registry

A community-sourced registry mapping the technical landscape of Tanzanian companies — tech stacks, tooling choices, and interview patterns.

## Mission

Tanzanian developers lose time guessing what to learn and how to prepare for interviews at local companies. This repository centralizes that intelligence so that:

- Developers can align learning paths with actual market demand.
- Candidates can prepare for interviews using real, sector-specific patterns.
- The ecosystem gains visibility into how local companies build software.

## Navigation

Data is organized by **sector**, then by **company**.

```
sectors/
├── fintech/       # Payments, banking, mobile money
├── agritech/      # Agriculture, supply chain, rural tech
├── logistics/     # Delivery, fleet, transport
└── saas/          # B2B software, platforms, tooling
```

Inside each company folder you'll find:

- `stack.json` — structured data describing the tech stack (validated against [schema.json](schema.json)).
- `interview-questions.md` — interview questions categorized by seniority (Junior / Mid / Senior).

## Contributing

Before submitting, read:

- [docs/contribution-standards.md](docs/contribution-standards.md) — submission rules and the "Elite Standard".
- [docs/interview-guidelines.md](docs/interview-guidelines.md) — how to use this data to prepare for interviews.

All submissions must include a **source of proof** (job link, engineering blog, or verified employee testimony). Rumor-based entries are rejected.

## Validation

Run the validator locally before submitting a PR:

```bash
pip install jsonschema
python scripts/validator.py
```

## Disclaimer

All data in this repository is **community-sourced**. Stacks evolve over time; job posts and blogs reflect a point in time, not a guarantee of current practice. Treat every entry as a strong signal, not ground truth. Companies named here are not affiliated with this project and have not endorsed its contents.

## License

See [LICENSE](LICENSE).
