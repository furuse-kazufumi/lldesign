# lldesign

> **Design tooling for the FullSense ™ family.** UI / Web / diagram design via LLM-friendly DSLs (Mermaid, SVG, Excalidraw JSON, Storybook).

Part of [FullSense ™](https://furuse-kazufumi.github.io/fullsense/) — Apache-2.0 OSS family for self-evolving, on-prem, audit-friendly LLM systems.

## Scope (v0.0.x — alpha)

- Generate diagrams (Mermaid, Excalidraw JSON, SVG) from natural-language briefs
- Validate accessibility (color contrast, ARIA structure) and design tokens
- Route HITL review through [llove](https://github.com/furuse-kazufumi/llove) TUI workbench
- Persist accepted / rejected design patterns into [llive](https://github.com/furuse-kazufumi/llive) memory (KAR + PM axes)

## Out of scope (parked for future)

- Machine CAD (`llcad`), EDA / PCB (`lleda`), IC layout (`llchip`) — see [FullSense roadmap](https://furuse-kazufumi.github.io/fullsense/roadmap.html)

## Install

```bash
pip install llmesh-lldesign           # core
pip install "llmesh-lldesign[llive]"  # with llive integration
```

## Competitive positioning

| Capability | Figma | v0.dev | Galileo AI | **lldesign** |
|---|---|---|---|---|
| Code-first DSL output | partial | yes | partial | **yes** (Mermaid/SVG/Excalidraw native) |
| On-prem / OSS | no | no | no | **yes** (Apache-2.0, Ollama-compatible) |
| HITL audit trail | no | no | no | **yes** (llive SQLite Ledger) |
| Pluggable LLM backend | no | no | no | **yes** (via llmesh) |

## Related

- [llmesh](https://github.com/furuse-kazufumi/llmesh) — secure LLM hub (on-prem MCP)
- [llive](https://github.com/furuse-kazufumi/llive) — self-evolving memory + execution kernel
- [llove](https://github.com/furuse-kazufumi/llove) — TUI dashboard / HITL workbench

## License

Code: **Apache-2.0**. Commercial license available — see [LICENSE-COMMERCIAL](https://github.com/furuse-kazufumi/llive/blob/main/LICENSE-COMMERCIAL).

*lldesign ™ is a trademark of Kazufumi Furuse, part of the FullSense ™ family.*
