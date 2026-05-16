---
layout: default
title: "lldesign"
description: "Design tooling for the FullSense LLM family"
nav_order: 1
---

# lldesign

> **Design tooling for the FullSense ™ family.** UI / Web / diagram design via
> LLM-friendly DSLs (Mermaid, SVG, Excalidraw, Storybook).

Part of the [FullSense ™](https://furuse-kazufumi.github.io/fullsense/) family.

## What it does

Given a natural-language design brief, lldesign emits:

- **Mermaid** flowcharts / sequence diagrams (kramdown-safe variants)
- **SVG** vector graphics with a11y validation
- **Excalidraw JSON** for whiteboard-style sketches
- **Storybook stories** for UI component libraries

Output is reviewed through the [llove](https://github.com/furuse-kazufumi/llove)
TUI workbench; accepted / rejected patterns are persisted as design DNA in
[llive](https://github.com/furuse-kazufumi/llive) memory.

## Status

**v0.0.1 alpha (skeleton)** — public API will change. See
[PROGRESS]({{ '/PROGRESS' | relative_url }}) for the live changelog and
[SPEC]({{ '/SPEC' | relative_url }}) for the design contract.

## Install

```bash
pip install llmesh-lldesign           # core
pip install "llmesh-lldesign[llive]"  # with llive integration
```

## Why this and not Figma / v0.dev?

- **On-prem** — runs against your own Ollama / LM Studio. No tenant data leaves
  your network.
- **OSS** — Apache-2.0 (+ optional Commercial) — fork, audit, modify.
- **HITL audit trail** — every accept / reject lands in llive's SQLite Ledger.
- **Code-first DSLs** — outputs are diffable text, not opaque binary blobs.

See the full comparison: [FullSense Comparison](https://furuse-kazufumi.github.io/fullsense/comparison.html).

## Links

- [GitHub repo](https://github.com/furuse-kazufumi/lldesign)
- [FullSense umbrella](https://furuse-kazufumi.github.io/fullsense/)
- [llive](https://furuse-kazufumi.github.io/llive/) · [llove](https://furuse-kazufumi.github.io/llove/) · [llmesh](https://furuse-kazufumi.github.io/llmesh/)

---

*lldesign ™ is a trademark of Kazufumi Furuse. Code under Apache-2.0.*
