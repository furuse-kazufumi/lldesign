---
layout: default
title: "Progress"
nav_order: 90
---

# lldesign — Progress

## 2026-05-16 — Bootstrap (v0.0.1)

Skeleton landed:

- `README.md`, `LICENSE` (Apache-2.0), `NOTICE`, `SECURITY.md`, `CONTRIBUTING.md` (DCO)
- `pyproject.toml` — name `llmesh-lldesign`, Python 3.11, deps empty,
  optional-deps `[llive]` `[llove]` `[dev]`
- `src/lldesign/__init__.py` — `__version__ = "0.0.1"`
- `docs/` — Jekyll just-the-docs skeleton with Mermaid 10.9 and a SEO
  card
- `tests/test_smoke.py` — version assertion

No public API implementations yet; all `lldesign.*` symbols other than
`__version__` are reserved for v0.1.0.

### Context

Created as part of the FullSense umbrella expansion in the 2026-05-16
session. lldesign is one of two new products spun up alongside `lltrade`
to stress-test [llive](https://github.com/furuse-kazufumi/llive) on
different axes — lldesign loads TLB / ICP / PM; lltrade loads RPAR /
SIL / DTKR.

### Open items

- [ ] Open the GitHub repo (`furuse-kazufumi/lldesign`, public)
- [ ] Enable GitHub Pages (Settings → Pages → `main` / `/docs`)
- [ ] Implement v0.1.0 Mermaid generator (`generate_diagram`)
- [ ] Wire llove TUI HITL loop
- [ ] Wire llive Stimulus / Approval Bus

### Parked

- Machine CAD (`llcad`), EDA (`lleda`), IC layout (`llchip`) — see FullSense roadmap
