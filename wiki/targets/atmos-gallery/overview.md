---
title: "Target Overview: atmos-gallery"
date: 2026-11-24
captured_at: 2026-11-24
url: "https://atmos.gallery"
final_url: "https://atmos.gallery/"
status: blocked
http_status: 200
capture_tier: none
block_reason: "Live desktop screenshot capture failed (0 valid PNG bytes)"
tags:
  - target
  - reverse-engineering
  - atmos-gallery
auth_required: false
---

# Target Overview: atmos-gallery

## Dossier Navigation
- [UI Prompt Blueprint](prompt-blueprint.md)
- [UI Architecture & Design Tokens](ui-ux.md)
- [Discovered APIs & Network Protocols](apis.md)
- [Data Models & Local State](data-models.md)
- [De-obfuscated Source Maps](source-maps.md)

---

## Architecture & Stack Fingerprint
- **Target URL**: [https://atmos.gallery](https://atmos.gallery)
- **Status**: `blocked` (`http_status: 200`, `capture_tier: none`)
- **Block / Unreachable Reason**: Live desktop screenshot capture failed (0 valid PNG bytes)
- **Page Title**: Atmos Gallery · Image Colour Palette Generator
- **Identified Frameworks**: Modern Web Application
- **Recovered Scripts**: `13`
- **Recovered Stylesheets**: `2`

---

## Key Architectural Lessons
- **UI & Design System**: See [ui-ux.md](ui-ux.md) and [prompt-blueprint.md](prompt-blueprint.md) for live computed design tokens and viewport captures.
- **Client State & APIs**: See [data-models.md](data-models.md) and [apis.md](apis.md) for observed endpoints and storage keys.
