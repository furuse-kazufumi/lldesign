---
layout: default
title: "Spec"
nav_order: 2
---

# lldesign — Design Contract (v0.0.x)

## Mission

Make **design tasks** (UI, Web, diagrams) executable by the FullSense LLM
kernel ([llive](https://github.com/furuse-kazufumi/llive)) while keeping a
**human reviewer** in the loop via [llove](https://github.com/furuse-kazufumi/llove).
Persist what designers accept and reject so the next brief is informed by the
last one.

## Scope

### In-scope

- **Mermaid** flowcharts, sequence diagrams, ER diagrams (kramdown-safe variant
  — no inline `<b>`/`<br/>`/`<i>` HTML; see [feedback_webpage_research_first])
- **SVG** vector output with a11y validation (color contrast, ARIA labels)
- **Excalidraw JSON** for whiteboard-style sketches
- **Storybook stories** for component libraries (React / Vue / Svelte adapters)
- Design **tokens** (color, type, spacing) extraction and round-trip with
  Figma / Penpot exports (read-only first)

### Out-of-scope (intentionally — see roadmap)

| Domain | Reason for parking | Future product |
|---|---|---|
| Machine CAD (Fusion 360, STEP/IGES output) | code-CAD (OpenSCAD/CadQuery) is its own engineering domain | `llcad` |
| Electronic design automation (KiCad schema + Gerber) | EDA toolchains are licence-and-vendor heavy | `lleda` |
| Semiconductor IC layout (GDSII, OpenLane) | requires OpenLane / Magic VLSI stack, RL-based router | `llchip` |

## llive integration points

| llive axis | lldesign responsibility |
|---|---|
| **KAR** (Knowledge Acquisition & Retention) | Ingest design system docs (Material 3, Apple HIG, Fluent 2) into RAD; query before generating |
| **TLB** (Tool & Library Binding) | Bind Mermaid CLI, librsvg, axe-core, Storybook CLI, Penpot API |
| **ICP** (Intent-Constraint Propagation) | Propagate "brand colors", "contrast ≥ 4.5:1", "max 3 colors", "RTL safe" down to leaf nodes |
| **PM** (Process Memory) | Remember accepted vs. rejected design patterns per project; bias future suggestions |
| **APO** (Action Policy Optimization) | Choose Mermaid vs. SVG vs. Excalidraw vs. Storybook per brief |
| **RPAR** (Risk-Proportional Autonomy Routing) | Low (preview), Medium (write to draft branch), High (open PR) — all gated by Approval Bus |
| **SIL** (Semantic Integrity Ledger) | Log every render call + reviewer verdict to SQLite for audit |

## Public API (planned, not yet implemented)

```python
from lldesign import DesignSession

session = DesignSession(llive_backend="ollama:qwen2.5:14b")

# 1. Generate a Mermaid flowchart from a brief
mermaid = session.generate_diagram(
    brief="Show how a user request flows from llove TUI through llmesh to llive memory",
    format="mermaid",
    constraints={"max_nodes": 8, "colors": ["#10b981", "#3b82f6", "#ec4899"]},
)

# 2. Validate a11y on an SVG
report = session.validate_svg(svg_str, rules={"contrast": 4.5, "aria": True})

# 3. Extract design tokens from a Figma export
tokens = session.extract_tokens(figma_export_json)
```

## Competitive positioning (target)

| Capability | Figma | v0.dev | Galileo | Penpot | **lldesign** |
|---|---|---|---|---|---|
| Code-first DSL output | partial | yes | partial | no | **yes** |
| On-prem / OSS | no | no | no | yes (no AI) | **yes** (AI + OSS) |
| HITL audit trail | no | no | no | partial | **yes** (Ledger) |
| Pluggable LLM backend | no | no | no | n/a | **yes** (llmesh) |
| Mermaid native | no | partial | no | no | **yes** |

## Versioning

- v0.0.x — alpha skeleton (this revision)
- v0.1.0 — first working Mermaid generator + llove HITL loop
- v0.2.0 — SVG a11y validator + Excalidraw round-trip
- v0.3.0 — Storybook adapter + design token extraction
- v1.0.0 — PyPI rename to `fullsense-design` (umbrella-wide)

## References

- [FullSense Spec v1.1](https://github.com/furuse-kazufumi/llive/blob/main/docs/fullsense_spec_eternal.md)
- [feedback_webpage_research_first](../../../../.claude/projects/C--Users-puruy-raptor/memory/feedback_webpage_research_first.md) — kramdown / Mermaid pitfalls
- [feedback_competitor_benchmark](../../../../.claude/projects/C--Users-puruy-raptor/memory/feedback_competitor_benchmark.md) — benchmark methodology
