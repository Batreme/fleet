---
title: "Target Overview: example-app"
date: 2026-11-24
captured_at: 2026-11-24
url: "https://example.com"
final_url: "https://example.com/"
status: blocked
http_status: 200
capture_tier: none
block_reason: "Placeholder Example Domain (no production site)"
tags:
  - target
  - reverse-engineering
  - example-app
auth_required: false
---

# Target Overview: example-app

## Dossier Navigation
- [UI Prompt Blueprint](prompt-blueprint.md)
- [UI Architecture & Design Tokens](ui-ux.md)
- [Discovered APIs & Network Protocols](apis.md)
- [Data Models & Local State](data-models.md)
- [De-obfuscated Source Maps](source-maps.md)

---

## Architecture & Stack Fingerprint
- **Target URL**: [https://example.com](https://example.com)
- **Status**: `blocked` (`http_status: 200`, `capture_tier: none`)
- **Block / Unreachable Reason**: Placeholder Example Domain (no production site)
- **Page Title**: Example Domain
- **Identified Frameworks**: Modern Web Application
- **Recovered Scripts**: `1`
- **Recovered Stylesheets**: `0`

---

## Key Architectural Lessons
- **UI & Design System**: See [ui-ux.md](ui-ux.md) and [prompt-blueprint.md](prompt-blueprint.md) for live computed design tokens and viewport captures.
- **Client State & APIs**: See [data-models.md](data-models.md) and [apis.md](apis.md) for observed endpoints and storage keys.
