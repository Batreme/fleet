---
title: "Target Overview: recurziv-com"
date: 2026-11-23
captured_at: 2026-11-23
url: "https://recurziv.com"
final_url: "https://recurziv.com/"
status: blocked
http_status: null
capture_tier: none
block_reason: "Network/Navigation failure (Page.goto: Timeout 35000ms exceeded. Call log: - navigating to 'https://recurziv.com/', waiting until 'domcontentloaded' )"
tags:
  - target
  - reverse-engineering
  - recurziv-com
auth_required: false
---

# Target Overview: recurziv-com

## Dossier Navigation
- [UI Prompt Blueprint](prompt-blueprint.md)
- [UI Architecture & Design Tokens](ui-ux.md)
- [Discovered APIs & Network Protocols](apis.md)
- [Data Models & Local State](data-models.md)
- [De-obfuscated Source Maps](source-maps.md)

---

## Architecture & Stack Fingerprint
- **Target URL**: [https://recurziv.com](https://recurziv.com)
- **Status**: `blocked` (`http_status: N/A`, `capture_tier: none`)
- **Block / Unreachable Reason**: Network/Navigation failure (Page.goto: Timeout 35000ms exceeded. Call log: - navigating to 'https://recurziv.com/', waiting until 'domcontentloaded' )
- **Page Title**: recurziv-com
- **Identified Frameworks**: Modern Web Application
- **Recovered Scripts**: `16`
- **Recovered Stylesheets**: `1`

---

## Key Architectural Lessons
- **UI & Design System**: See [ui-ux.md](ui-ux.md) and [prompt-blueprint.md](prompt-blueprint.md) for live computed design tokens and viewport captures.
- **Client State & APIs**: See [data-models.md](data-models.md) and [apis.md](apis.md) for observed endpoints and storage keys.
