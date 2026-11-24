---
title: "Target Overview: mstage-group-jp"
date: 2026-11-24
captured_at: 2026-11-24
url: "https://mstage-group.jp/"
final_url: "https://mstage-group.jp/"
status: blocked
http_status: 403
capture_tier: none
block_reason: "Upstream HTTP 403 — CloudFront WAF Block"
tags:
  - target
  - reverse-engineering
  - mstage-group-jp
auth_required: false
---

# Target Overview: mstage-group-jp

## Dossier Navigation
- [UI Prompt Blueprint](prompt-blueprint.md)
- [UI Architecture & Design Tokens](ui-ux.md)
- [Discovered APIs & Network Protocols](apis.md)
- [Data Models & Local State](data-models.md)
- [De-obfuscated Source Maps](source-maps.md)

---

## Architecture & Stack Fingerprint
- **Target URL**: [https://mstage-group.jp/](https://mstage-group.jp/)
- **Status**: `blocked` (`http_status: 403`, `capture_tier: none`)
- **Block / Unreachable Reason**: Upstream HTTP 403 — CloudFront WAF Block
- **Page Title**: ERROR: The request could not be satisfied
- **Identified Frameworks**: Modern Web Application
- **Recovered Scripts**: `0`
- **Recovered Stylesheets**: `0`

---

## Key Architectural Lessons
- **UI & Design System**: See [ui-ux.md](ui-ux.md) and [prompt-blueprint.md](prompt-blueprint.md) for live computed design tokens and viewport captures.
- **Client State & APIs**: See [data-models.md](data-models.md) and [apis.md](apis.md) for observed endpoints and storage keys.
