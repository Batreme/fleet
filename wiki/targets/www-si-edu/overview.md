---
title: "Target Overview: www-si-edu"
date: 2026-11-24
captured_at: 2026-11-24
url: "https://www.si.edu/"
final_url: "https://www.si.edu/"
status: blocked
http_status: 403
capture_tier: none
block_reason: "Upstream HTTP 403 — Cloudflare Origin/WAF Error"
tags:
  - target
  - reverse-engineering
  - www-si-edu
auth_required: false
---

# Target Overview: www-si-edu

## Dossier Navigation
- [UI Prompt Blueprint](prompt-blueprint.md)
- [UI Architecture & Design Tokens](ui-ux.md)
- [Discovered APIs & Network Protocols](apis.md)
- [Data Models & Local State](data-models.md)
- [De-obfuscated Source Maps](source-maps.md)

---

## Architecture & Stack Fingerprint
- **Target URL**: [https://www.si.edu/](https://www.si.edu/)
- **Status**: `blocked` (`http_status: 403`, `capture_tier: none`)
- **Block / Unreachable Reason**: Upstream HTTP 403 — Cloudflare Origin/WAF Error
- **Page Title**: Just a moment...
- **Identified Frameworks**: Modern Web Application
- **Recovered Scripts**: `3`
- **Recovered Stylesheets**: `0`

---

## Key Architectural Lessons
- **UI & Design System**: See [ui-ux.md](ui-ux.md) and [prompt-blueprint.md](prompt-blueprint.md) for live computed design tokens and viewport captures.
- **Client State & APIs**: See [data-models.md](data-models.md) and [apis.md](apis.md) for observed endpoints and storage keys.
