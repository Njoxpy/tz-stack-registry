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
- [docs/privacy-policy.md](docs/privacy-policy.md) — what the registry will and will not publish, and how to anonymize interview testimony.
- [docs/code-of-conduct.md](docs/code-of-conduct.md) — expectations for everyone in the project.
- [docs/interview-guidelines.md](docs/interview-guidelines.md) — how to use this data to prepare for interviews.

All submissions must include a **source of proof** (job link, engineering blog, or verified employee testimony). Rumor-based entries are rejected. Interview testimony must be anonymized per the Privacy Policy.

## Validation

Run the validator locally before submitting a PR:

```bash
pip install jsonschema
python scripts/validator.py
```

## Documentation Site

A browsable MkDocs site is configured at the repo root ([mkdocs.yml](mkdocs.yml)):

```bash
./scripts/setup-mkdocs.sh        # one-time: creates .venv, installs deps, builds
source .venv/bin/activate
mkdocs serve                      # preview at http://127.0.0.1:8000
./scripts/deploy.sh               # build and (after confirmation) gh-deploy
```

The site is configured to publish to the `gh-pages` branch of this repository. Enable GitHub Pages for that branch in the repo settings after the first deploy.

## Disclaimer

All data in this repository is **community-sourced**. Stacks evolve over time; job posts and blogs reflect a point in time, not a guarantee of current practice. Treat every entry as a strong signal, not ground truth. Companies named here are not affiliated with this project and have not endorsed its contents.

## License

See [LICENSE](LICENSE).
