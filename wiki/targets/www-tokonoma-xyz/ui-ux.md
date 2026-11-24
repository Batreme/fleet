---
title: "UI & UX Architecture: www-tokonoma-xyz"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-tokonoma-xyz

## Overview & Design Identity
- **Target**: `www-tokonoma-xyz` (**Tokonoma Studio — Image Making, Art, AI & Creative Direction**)
- **Production URL**: [https://www.tokonoma.xyz/](https://www.tokonoma.xyz/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×2484px`, Mobile `390×872px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#111111` / `#000000`)
- **Summary**: Tokonoma is an image-making studio working across analogue and AI photography, animation, creative coding, art and digital experiences. C...
- **Total Clean CSS Variables Extracted**: `3` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `EurostileMNExtendedBold`
- **Body Font Stack**: `EurostileMNExtendedBold`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `h1` (`letter-spacing: .02em`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 24px`, `line-height: 1.05`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 700`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#111111` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#141414` | `var(--color-panel)` in `:root` |
| **Interactive Accent / Highlight** | `#000000` | `er-detail-menu-cursor .cursor-a... { color: #000000 }` |
| **Secondary / Muted Copy** | `#5f5f5f` | `var(--color-muted)` in `:root` |
| **Structural Hairline Border** | `#000000` | `.newsletter-ring .newsletter-ri... { stroke: #000000 }` |
| **Variable Token (`--cursor-color`)** | `#baff00` | `var(--cursor-color)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--cursor-color` | `#baff00` | Brand / Palette Token |
| `--color-muted` | `#5f5f5f` | Brand / Palette Token |
| `--color-panel` | `#141414` | Brand / Palette Token |
| `--www-tokonoma-xyz-bg` | `#111111` | Canvas Substrate (from live computed `body` `background-color` (`computed_styles.json`)) |
| `--www-tokonoma-xyz-ink` | `#ffffff` | Primary Typography Ink (computed-derived) |
| `--www-tokonoma-xyz-surface` | `#141414` | Surface Substrate (computed-derived) |
| `--www-tokonoma-xyz-accent` | `#000000` | Interactive Accent (computed-derived) |
| `--www-tokonoma-xyz-muted` | `#5f5f5f` | Secondary Ink (computed-derived) |
| `--www-tokonoma-xyz-border` | `#000000` | Structural Border (computed-derived) |
| `--www-tokonoma-xyz-container` | `1440px` | Container Bound (computed-derived) |
| `--www-tokonoma-xyz-gap` | `32px` | Grid Gutter (computed-derived) |
| `--www-tokonoma-xyz-pad` | `20px` | Lateral Padding (computed-derived) |
| `--www-tokonoma-xyz-ease` | `cubic-bezier(.22,1,.36,1)` | Primary Easing Function |
| `--www-tokonoma-xyz-radius` | `999px` | Corner Radius (computed-derived) |
| `--www-tokonoma-xyz-fs-base` | `16px` | Observed Font Size Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.interface> — `www-tokonoma-xyz`)**:
   - Landmark `<nav class="interface">` (`1440x900px`) hosting `Tokonoma Studio — Image Making, Art,` navigation (`ABOUT · SHOWS`), DOM attributes (`data-target="www-tokonoma-xyz"`), and stylesheet rule `property --angle-1 { syntax: "<angle>"; inherits: false; initial-value: -75deg; }`.
2. **Hero Stage & Focal Lead (<main.entry-main> — `Tokonoma Studio — Image Making, Ar`)**:
   - Landmark `<main class="entry-main">` presenting display lead `Tokonoma Studio — Image Making, Art, AI & Creati` and copy excerpt *"Tokonoma is an image-making studio working across analogue and AI"* over `#111111` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<main.entry-main:nth(2)> — `Featured Work & Interactive Showca`)**:
   - Landmark `<main class="entry-main">` rendering section `Featured Work & Interactive Showcase` with copy *"Tokonoma Studio — Image Making, Art, AI & Creati"*, asset references (`EurostileMNExtendedBold.ttf`, `favicon-32x32-dm.png`, `styles.css`, `tokonoma_logo.png (Tokonoma)`), and grid rule `property --angle-2 { syntax: "<angle>"; inherits: false; initial-value: -45deg; }`.
4. **Interactive Detail & Feature Matrix (<main.entry-main:nth(3)> — `Technical Architecture & Narrative`)**:
   - Landmark `<main class="entry-main">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Featured Work & Interactive Showcase"*) with `#141414` surface cards, `#000000` accents, and `html.mobile-project-wheel .viewer... { inset: 160px 0 64px 0; }`.
5. **Colophon & Global Directory Footer (<footer.tokonoma-logo> — `https://www.tokonoma.xyz/`)**:
   - Landmark `<footer class="tokonoma-logo">` anchoring `Tokonoma Studio — Image Making, ` footer links (`ABOUT · SHOWS`), copy *"Technical Architecture & Narrative"*, and `#000000` structural dividers.
