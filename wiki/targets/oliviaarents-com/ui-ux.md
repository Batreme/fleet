---
title: "UI & UX Architecture: oliviaarents-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: oliviaarents-com

## Overview & Design Identity
- **Target**: `oliviaarents-com` (**OliviaOS 96 — Personal Edition**)
- **Production URL**: [https://oliviaarents.com/](https://oliviaarents.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×900px`, Mobile `390×844px`)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#000000` canvas, `#fffde5` ink, `#9e9eff` accent)
- **Summary**: OliviaOS 96 — Personal Edition. Olivia's personal portfolio, imagined as a late-1990s desktop operating system.
- **Total Clean CSS Variables Extracted**: `7` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `VT323`
- **Body Font Stack**: `Tahoma`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 48px`, `line-height: 57.6px`, `font-weight: 400`, `letter-spacing: 2.88px`); rule `h1` (`letter-spacing: 1px`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 17px`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); rule `p` (`font-size: 11px`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | live computed `html` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#fffde5` | live computed `button` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#163e2e` | live computed `main` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#9e9eff` | live computed `a` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#9e9eff` | live computed `a` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#548b59` | `.boot-screen__progress { border: #548b59 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--lightningcss-dark` | `initial` | Canvas / Surface Token |
| `--lightningcss-light` | `initial` | Canvas / Surface Token |
| `--touch-dock-height` | `calc(70px + env(safe-area-inset-bottom,0px))` | Layout / Spatial Grid Token |
| `--taskbar-height` | `48px` | Layout / Spatial Grid Token |
| `--desktop-icon-width` | `94px` | Layout / Spatial Grid Token |
| `--desktop-icon-height` | `88px` | Layout / Spatial Grid Token |
| `--boot-fade-duration` | `450ms` | Motion / Easing Token |
| `--oliviaarents-com-bg` | `#000000` | Canvas Substrate (from live computed `html` `background-color` (`computed_styles.json`)) |
| `--oliviaarents-com-ink` | `#fffde5` | Primary Typography Ink (computed-derived) |
| `--oliviaarents-com-surface` | `#163e2e` | Surface Substrate (computed-derived) |
| `--oliviaarents-com-accent` | `#9e9eff` | Interactive Accent (computed-derived) |
| `--oliviaarents-com-muted` | `#9e9eff` | Secondary Ink (computed-derived) |
| `--oliviaarents-com-border` | `#548b59` | Structural Border (computed-derived) |
| `--oliviaarents-com-container` | `1440px` | Container Bound (computed-derived) |
| `--oliviaarents-com-gap` | `8px` | Grid Gutter (computed-derived) |
| `--oliviaarents-com-pad` | `8px` | Lateral Padding (computed-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.desktop> — `oliviaarents-com`)**:
   - Landmark `<header class="desktop">` (`1440px`) hosting `OliviaOS 96 — Personal Edition` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-sdkn="@vercel/analytics/react"`, `data-sdkv="2.0.1"`, `data-dragging="false"`, `data-dragging="false"`), and stylesheet rule `after { box-sizing:border-box }`.
2. **Hero Stage & Focal Lead (<main.desktop> — `OLIVIAOS 96`)**:
   - Landmark `<main class="desktop">` presenting display lead `OLIVIAOS 96` and copy excerpt *"Drag an icon or use arrow keys to move it. Hold Shift for smaller"* over `#000000` canvas and `#fffde5` ink.
3. **Primary Showcase & Content Grid (<main.desktop:nth(2)> — `Drag an icon or use arrow keys to `)**:
   - Landmark `<main class="desktop">` rendering section `Drag an icon or use arrow keys to move it. Hold ` with copy *"Click anywhere to boot _"*, asset references (`favicon.svg`, `index-DfR-XKA5.js`, `index-BnFyCq9P.css`, `script.js`), and grid rule `body { overscroll-behavior:none;width:100%;height:100%;overflow:hidden }`.
4. **Interactive Detail & Feature Matrix (<main.desktop:nth(3)> — `Click anywhere to boot _`)**:
   - Landmark `<main class="desktop">` framing `Click anywhere to boot _` and `oliviaarents-com Archive & Directory` (*"Drag an icon or use arrow keys to move it. Hold "*) with `#163e2e` surface cards, `#9e9eff` accents, and `root { height:100dvh;overflow:hidden }`.
5. **Colophon & Global Directory Footer (<footer.taskbar> — `https://oliviaarents.com/`)**:
   - Landmark `<footer class="taskbar">` anchoring `OliviaOS 96 — Personal Edition` footer links (`Overview · Index · Archive · About · Contact`), copy *"Click anywhere to boot _"*, and `#548b59` structural dividers.
