---
title: "Target Overview: sadok-mx"
date: 2026-11-24
captured_at: 2026-11-24
url: "https://sadok.mx/"
final_url: "https://sadok.mx/"
status: blocked
http_status: null
capture_tier: none
block_reason: "Network/Navigation failure (Page.goto: Timeout 22000ms exceeded. Call log: - navigating to 'https://sadok.mx/', waiting until 'domcontentloaded' )"
tags:
  - target
  - reverse-engineering
  - sadok-mx
auth_required: false
---

# Target Overview: sadok-mx

## Dossier Navigation
- [UI Prompt Blueprint](prompt-blueprint.md)
- [UI Architecture & Design Tokens](ui-ux.md)
- [Discovered APIs & Network Protocols](apis.md)
- [Data Models & Local State](data-models.md)
- [De-obfuscated Source Maps](source-maps.md)

---

## Architecture & Stack Fingerprint
- **Target URL**: [https://sadok.mx/](https://sadok.mx/)
- **Status**: `blocked` (`http_status: N/A`, `capture_tier: none`)
- **Block / Unreachable Reason**: Network/Navigation failure (Page.goto: Timeout 22000ms exceeded. Call log: - navigating to 'https://sadok.mx/', waiting until 'domcontentloaded' )
- **Page Title**: sadok-mx
- **Identified Frameworks**: Modern Web Application
- **Recovered Scripts**: `3`
- **Recovered Stylesheets**: `5`

---

## Key Architectural Lessons
- **UI & Design System**: See [ui-ux.md](ui-ux.md) and [prompt-blueprint.md](prompt-blueprint.md) for live computed design tokens and viewport captures.
- **Client State & APIs**: See [data-models.md](data-models.md) and [apis.md](apis.md) for observed endpoints and storage keys.
