---
title: "Target Overview: mychess-events"
date: 2026-11-14
url: "https://mychess.events/"
status: analyzed
tags:
  - target
  - reverse-engineering
  - mychess-events
auth_required: false
---

# Target Overview: mychess-events

## 🧭 Dossier Navigation
- [Discovered APIs & Network Protocols](apis.md)
- [Data Models & Local State](data-models.md)
- [UI Architecture & Design Tokens](ui-ux.md)
- [De-obfuscated Source Maps](source-maps.md)

---

## 🏗️ Architecture & Stack Fingerprint
- **Target URL**: `https://mychess.events/`
- **Page Title**: Find Chess Tournaments Worldwide | MyChess.Events
- **Identified Frameworks**: Modern Web Application
- **Auth Profile Used**: None (Public session)
- **Recorded API Endpoints**: 6
- **Recovered Scripts**: 87
- **Recovered Stylesheets**: 53

---

## 💡 Key Architectural Lessons (Anti-AI-Slop Insights)
- **Domain Modeling**: See [data-models](data-models.md) for concrete entity structures observed in network requests and local storage.
- **Client Architecture**: Inferred from UI layout primitives and client storage persistence.
- **[UI Prompt Blueprint](prompt-blueprint.md)** — 7-part design system analysis, desktop/mobile visual captures, and zero-shot generation prompt.
