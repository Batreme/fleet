---
title: "Target Overview: offform-net"
date: 2026-11-23
captured_at: 2026-11-23
url: "https://offform.net/"
final_url: "https://offform.net/"
status: blocked
http_status: 502
capture_tier: none
block_reason: "Upstream HTTP 502 (502 Bad Gateway)"
tags:
  - target
  - reverse-engineering
  - offform-net
auth_required: false
---

# Target Overview: offform-net

## Dossier Navigation
- [UI Prompt Blueprint](prompt-blueprint.md)
- [UI Architecture & Design Tokens](ui-ux.md)
- [Discovered APIs & Network Protocols](apis.md)
- [Data Models & Local State](data-models.md)
- [De-obfuscated Source Maps](source-maps.md)

---

## Architecture & Stack Fingerprint
- **Target URL**: [https://offform.net/](https://offform.net/)
- **Status**: `blocked` (`http_status: 502`, `capture_tier: none`)
- **Block / Unreachable Reason**: Upstream HTTP 502 (502 Bad Gateway)
- **Page Title**: 502 Bad Gateway
- **Identified Frameworks**: Modern Web Application
- **Recovered Scripts**: `0`
- **Recovered Stylesheets**: `0`

---

## Key Architectural Lessons
- **UI & Design System**: See [ui-ux.md](ui-ux.md) and [prompt-blueprint.md](prompt-blueprint.md) for live computed design tokens and viewport captures.
- **Client State & APIs**: See [data-models.md](data-models.md) and [apis.md](apis.md) for observed endpoints and storage keys.
