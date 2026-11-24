---
title: "Target Overview: fromearth-love"
date: 2026-11-24
captured_at: 2026-11-24
url: "http://fromearth.love"
final_url: "https://fromearth.love/"
status: blocked
http_status: null
capture_tier: none
block_reason: "Network/Navigation failure (Page.goto: Timeout 22000ms exceeded. Call log: - navigating to 'http://fromearth.love/', waiting until 'domcontentloaded' )"
tags:
  - target
  - reverse-engineering
  - fromearth-love
auth_required: false
---

# Target Overview: fromearth-love

## Dossier Navigation
- [UI Prompt Blueprint](prompt-blueprint.md)
- [UI Architecture & Design Tokens](ui-ux.md)
- [Discovered APIs & Network Protocols](apis.md)
- [Data Models & Local State](data-models.md)
- [De-obfuscated Source Maps](source-maps.md)

---

## Architecture & Stack Fingerprint
- **Target URL**: [http://fromearth.love](http://fromearth.love)
- **Status**: `blocked` (`http_status: N/A`, `capture_tier: none`)
- **Block / Unreachable Reason**: Network/Navigation failure (Page.goto: Timeout 22000ms exceeded. Call log: - navigating to 'http://fromearth.love/', waiting until 'domcontentloaded' )
- **Page Title**: fromearth-love
- **Identified Frameworks**: Modern Web Application
- **Recovered Scripts**: `50`
- **Recovered Stylesheets**: `6`

---

## Key Architectural Lessons
- **UI & Design System**: See [ui-ux.md](ui-ux.md) and [prompt-blueprint.md](prompt-blueprint.md) for live computed design tokens and viewport captures.
- **Client State & APIs**: See [data-models.md](data-models.md) and [apis.md](apis.md) for observed endpoints and storage keys.
