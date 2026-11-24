---
title: "Target Overview: www-lev-com"
date: 2026-11-24
captured_at: 2026-11-24
url: "https://www.lev.com/"
final_url: "https://www.lev.com/"
status: blocked
http_status: 200
capture_tier: none
block_reason: "Live desktop behavioral capture failed (0 valid keyframes)"
tags:
  - target
  - reverse-engineering
  - www-lev-com
auth_required: false
---

# Target Overview: www-lev-com

## Dossier Navigation
- [UI Prompt Blueprint](prompt-blueprint.md)
- [UI Architecture & Design Tokens](ui-ux.md)
- [Discovered APIs & Network Protocols](apis.md)
- [Data Models & Local State](data-models.md)
- [De-obfuscated Source Maps](source-maps.md)

---

## Architecture & Stack Fingerprint
- **Target URL**: [https://www.lev.com/](https://www.lev.com/)
- **Status**: `blocked` (`http_status: 200`, `capture_tier: none`)
- **Block / Unreachable Reason**: Live desktop behavioral capture failed (0 valid keyframes)
- **Page Title**: Lev · The AI platform for commercial real estate
- **Identified Frameworks**: Modern Web Application
- **Recovered Scripts**: `73`
- **Recovered Stylesheets**: `7`

---

## Key Architectural Lessons
- **UI & Design System**: See [ui-ux.md](ui-ux.md) and [prompt-blueprint.md](prompt-blueprint.md) for live computed design tokens and viewport captures.
- **Client State & APIs**: See [data-models.md](data-models.md) and [apis.md](apis.md) for observed endpoints and storage keys.
