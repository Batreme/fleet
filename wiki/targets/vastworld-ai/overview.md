---
title: "Target Overview: vastworld-ai"
date: 2026-11-23
captured_at: 2026-11-23
url: "https://vastworld.ai/"
final_url: "https://vastworld.ai/"
status: blocked
http_status: 200
capture_tier: none
block_reason: "Headless Preloader / Blank Viewport Capture (cannot hydrate without interactive/GPU session)"
tags:
  - target
  - reverse-engineering
  - vastworld-ai
auth_required: false
---

# Target Overview: vastworld-ai

## Dossier Navigation
- [UI Prompt Blueprint](prompt-blueprint.md)
- [UI Architecture & Design Tokens](ui-ux.md)
- [Discovered APIs & Network Protocols](apis.md)
- [Data Models & Local State](data-models.md)
- [De-obfuscated Source Maps](source-maps.md)

---

## Architecture & Stack Fingerprint
- **Target URL**: [https://vastworld.ai/](https://vastworld.ai/)
- **Status**: `blocked` (`http_status: 200`, `capture_tier: none`)
- **Block / Unreachable Reason**: Headless Preloader / Blank Viewport Capture (cannot hydrate without interactive/GPU session)
- **Page Title**: VAST-A global Leading AI Company
- **Identified Frameworks**: Modern Web Application
- **Recovered Scripts**: `9`
- **Recovered Stylesheets**: `1`

---

## Key Architectural Lessons
- **UI & Design System**: See [ui-ux.md](ui-ux.md) and [prompt-blueprint.md](prompt-blueprint.md) for live computed design tokens and viewport captures.
- **Client State & APIs**: See [data-models.md](data-models.md) and [apis.md](apis.md) for observed endpoints and storage keys.
