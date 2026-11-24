---
title: "Target Overview: www-fragment-im"
date: 2026-11-24
captured_at: 2026-11-24
url: "https://www.fragment.im"
final_url: "https://www.fragment.im/"
status: blocked
http_status: 200
capture_tier: none
block_reason: "Live desktop behavioral capture failed (0 valid keyframes)"
tags:
  - target
  - reverse-engineering
  - www-fragment-im
auth_required: false
---

# Target Overview: www-fragment-im

## Dossier Navigation
- [UI Prompt Blueprint](prompt-blueprint.md)
- [UI Architecture & Design Tokens](ui-ux.md)
- [Discovered APIs & Network Protocols](apis.md)
- [Data Models & Local State](data-models.md)
- [De-obfuscated Source Maps](source-maps.md)

---

## Architecture & Stack Fingerprint
- **Target URL**: [https://www.fragment.im](https://www.fragment.im)
- **Status**: `blocked` (`http_status: 200`, `capture_tier: none`)
- **Block / Unreachable Reason**: Live desktop behavioral capture failed (0 valid keyframes)
- **Page Title**: www-fragment-im
- **Identified Frameworks**: Modern Web Application
- **Recovered Scripts**: `28`
- **Recovered Stylesheets**: `0`

---

## Key Architectural Lessons
- **UI & Design System**: See [ui-ux.md](ui-ux.md) and [prompt-blueprint.md](prompt-blueprint.md) for live computed design tokens and viewport captures.
- **Client State & APIs**: See [data-models.md](data-models.md) and [apis.md](apis.md) for observed endpoints and storage keys.
