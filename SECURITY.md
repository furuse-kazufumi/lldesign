# Security Policy

## Reporting a vulnerability

Email: `kazufumi@furuse.work` with subject prefix `[lldesign-security]`.

We aim to acknowledge within 72 hours. Please do not file public issues for
unpatched vulnerabilities.

## Supported versions

| Version | Supported |
|---------|-----------|
| 0.0.x   | yes (alpha) |
| < 0.0   | no |

## Threat model (v0.0.x)

lldesign processes design briefs and emits Mermaid / SVG / Excalidraw / Storybook
artifacts. Untrusted inputs to evaluate carefully:

- Mermaid source containing inline HTML (kramdown / Liquid injection)
- SVG with `<script>` or `xlink:href="javascript:..."` payloads
- Excalidraw JSON with embedded URLs

Generated artifacts are sanitised before being written to disk; tampering with
the sanitiser is in scope. Bypasses of the llive Approval Bus are critical.

See [FullSense SECURITY](https://github.com/furuse-kazufumi/fullsense/blob/main/SECURITY.md)
for the umbrella policy.
