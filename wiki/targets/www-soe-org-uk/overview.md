---
title: "Target Overview: www-soe-org-uk"
date: 2026-11-24
captured_at: 2026-11-24
url: "https://www.soe.org.uk/"
final_url: "https://soe.org.uk/"
status: blocked
http_status: 403
capture_tier: none
block_reason: "Upstream HTTP 403 (Checking your browser...)"
tags:
  - target
  - reverse-engineering
  - www-soe-org-uk
auth_required: false
---

# Target Overview: www-soe-org-uk

## Dossier Navigation
- [UI Prompt Blueprint](prompt-blueprint.md)
- [UI Architecture & Design Tokens](ui-ux.md)
- [Discovered APIs & Network Protocols](apis.md)
- [Data Models & Local State](data-models.md)
- [De-obfuscated Source Maps](source-maps.md)

---

## Architecture & Stack Fingerprint
- **Target URL**: [https://www.soe.org.uk/](https://www.soe.org.uk/)
- **Final Redirected URL**: [https://soe.org.uk/](https://soe.org.uk/)
- **Status**: `blocked` (`http_status: 403`, `capture_tier: none`)
- **Block / Unreachable Reason**: Upstream HTTP 403 (Checking your browser...)
- **Page Title**: Checking your browser...
- **Identified Frameworks**: Modern Web Application
- **Recovered Scripts**: `4`
- **Recovered Stylesheets**: `0`

---

## Key Architectural Lessons
- **UI & Design System**: See [ui-ux.md](ui-ux.md) and [prompt-blueprint.md](prompt-blueprint.md) for live computed design tokens and viewport captures.
- **Client State & APIs**: See [data-models.md](data-models.md) and [apis.md](apis.md) for observed endpoints and storage keys.
