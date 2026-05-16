# Contributing to lldesign

Thank you for considering a contribution! lldesign is part of the FullSense ™
family — please read the [umbrella CONTRIBUTING](https://github.com/furuse-kazufumi/fullsense/blob/main/CONTRIBUTING.md)
first for the shared policy.

## Developer Certificate of Origin (DCO)

All commits must be signed off:

```bash
git commit -s -m "your message"
```

This adds a `Signed-off-by: Your Name <your@email>` line certifying the
[Developer Certificate of Origin v1.1](https://developercertificate.org/).
PRs without DCO sign-off will be asked to amend.

## PR workflow

1. Fork the repo and create a topic branch from `main`
2. Implement + add tests under `tests/`
3. Run `pytest` locally and make sure it passes
4. Open the PR with a clear description and link to any related issue

## Style

- Python 3.11 only (the project pins `>=3.11,<3.12`)
- Format with `ruff format`, lint with `ruff check`
- Type-check with `mypy src/`

## Areas where help is welcome

- Mermaid / SVG / Excalidraw schema validation
- a11y (color contrast, ARIA) validators
- llove TUI integration tests
- llive Stimulus / Approval Bus wiring examples
