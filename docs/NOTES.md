---
layout: default
title: "Notes"
nav_order: 91
---

# lldesign — Design Notes

## Decisions

### Why a separate package, not a submodule of llive?

llive is a kernel (memory + execution); lldesign is an **application** that
calls into llive. Keeping them separate lets users install llive alone and
lets lldesign rev independently. Same pattern as llove.

### Why `llmesh-lldesign` on PyPI?

For now, all FullSense packages live under the `llmesh-*` namespace
(`llmesh`, `llmesh-llive`, `llmesh-llove`, `llmesh-lldesign`, `llmesh-lltrade`).
The `fullsense-*` namespace is reserved for the v1.0 rename — see
[llive v1.0 migration plan](https://github.com/furuse-kazufumi/llive/blob/main/docs/v1.0_migration_plan.md).

### Why Mermaid first, not SVG?

Mermaid is the most text-native DSL of the three, so it stresses the
LLM-to-DSL pipeline cleanly without requiring rendering libraries.
Once the generation loop is robust on Mermaid, SVG (with rendering +
a11y) becomes a natural extension.

### Why no real Figma / Penpot write integration in v0.x?

Both APIs require OAuth and per-user tokens, which complicates on-prem
deployments. v0.x is read-only (import exports); write integration is
v0.4+ once the trust model is sorted.

## Pitfalls observed (from FullSense portal work, 2026-05-16)

- **kramdown breaks fenced ` ```mermaid ` blocks containing `<b>` / `<br/>`
  / `<i>` HTML.** Always emit pure Mermaid (use the styled `style` directive
  for emphasis instead of inline HTML).
- **GitHub Topic UI requires Enter / Tab to chip-confirm.** When emitting
  documentation that asks users to set topics, instruct one-per-line +
  Enter explicitly.
- **OG card `image:` should point to PNG, not SVG.** Social crawlers
  don't render SVG.

These are captured globally in
[`feedback_webpage_research_first`](../../../../.claude/projects/C--Users-puruy-raptor/memory/feedback_webpage_research_first.md).

## Deferred

- **Real-time Figma plugin** — defer until v0.4+
- **Multi-page Storybook generation** — defer until v0.3+
- **VS Code extension** for in-IDE preview — defer until v0.5+
