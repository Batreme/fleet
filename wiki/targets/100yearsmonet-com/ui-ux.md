---
title: "UI & UX Architecture: 100yearsmonet-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: 100yearsmonet-com

## Overview & Design Identity
- **Target**: `100yearsmonet-com` (**Monet 100 — A century without Claude Monet · 3D gallery**)
- **Production URL**: [https://100yearsmonet.com](https://100yearsmonet.com)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×828px`, Mobile `390×2616px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#fbf3c6`)
- **Summary**: A hundred years after Claude Monet’s death: walk on water through his paintings into the room of Water Lilies. An immersive 3D tribute wi...
- **Total Clean CSS Variables Extracted**: `7` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Manrope`
- **Body Font Stack**: `Quelia`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 32px`, `line-height: 49.6px`, `font-weight: 400`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 60.48px`, `line-height: 62.8992px`, `font-weight: 400`); rule `h2` (`letter-spacing: -.01em`)
- **Body Copy**: live computed `body` (`font-size: 12px`, `line-height: normal`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 11.5px`, `line-height: 17.25px`, `font-weight: 400`); rule `small` (`letter-spacing: .12em`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `p` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#141006` | live computed `button` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#fbf3c6` | `.mui .mui-gslot .btn--solid { background: #fbf3c6 }` |
| **Secondary / Muted Copy** | `#e5dce9` | live computed `body` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#8c8c8c` | `.mui .mui-go:active { border-color: #8c8c8c }` |
| **Variable Token (`--mui-cream`)** | `#fcf4e9` | `var(--mui-cream)` in stylesheet |
| **Variable Token (`--mui-ink`)** | `#282b36` | `var(--mui-ink)` in stylesheet |
| **Variable Token (`--mui-night`)** | `#15141f` | `var(--mui-night)` in stylesheet |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--snd-r` | `var(--mui-gutter,24px)` | Dimension / Scale Token |
| `--snd-b` | `calc(26px + env(safe-area-inset-bottom,0px))` | Dimension / Scale Token |
| `--cat` | `calc(1 - var(--p,0))` | Design System Custom Token |
| `--fs` | `min(52vh,30vw)` | Dimension / Scale Token |
| `--bx` | `50%` | Dimension / Scale Token |
| `--by` | `46%` | Dimension / Scale Token |
| `--ch` | `150px` | Dimension / Scale Token |
| `--mui-cream` | `#FCF4E9` | Color / Atmospheric Token |
| `--mui-cream-rgb` | `252 244 233` | Design System Custom Token |
| `--mui-ink` | `#282B36` | Typography Ink Token |
| `--mui-night` | `#15141f` | Color / Atmospheric Token |
| `--mui-serif` | `"Quelia","Iowan Old Style",Georgia,serif` | Typography / Scale Token |
| `--mui-sans` | `"Manrope","Helvetica Neue",Arial,system-ui,sans-serif` | Typography / Scale Token |
| `--mui-ui` | `"Manrope","Helvetica Neue",Arial,system-ui,sans-serif` | Dimension / Scale Token |
| `--100yearsmonet-co-bg` | `#000000` | Canvas Substrate (from live computed `body` `background-color` (`computed_styles.json`)) |
| `--100yearsmonet-co-ink` | `#ffffff` | Primary Typography Ink (computed-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.mui-hud> — `100yearsmonet-com`)**:
   - Landmark `<header class="mui-hud mui-hud--top">` (`1360x0px`) hosting `Monet 100 — A century without Claude` navigation (`Musée de l’Orangerie · Musée d’Orsay · The Met · MFA Boston · Museum Barberini`), DOM attributes (`data-title-stay`, `data-enter="sound"`, `data-v="Dawn"`, `data-card="impression"`), and stylesheet rule `body { background:000 }`.
2. **Hero Stage & Focal Lead (<section.mui-hero> — `100 years without Monet`)**:
   - Landmark `<section class="mui-hero">` presenting display lead `100 years without Monet` and copy excerpt *"He died at Giverny on 5 December 1926. A century later, walk on t"* over `#000000` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<article.mui-card> — `100 Years without Monet`)**:
   - Landmark `<article class="mui-card">` rendering section `100 Years without Monet` with copy *"Claude Monet died at Giverny on 5 December 1926. A hundred years "*, asset references (`favicon-32.png`, `apple-touch-icon.png`, `site.webmanifest`, `quelia.woff2`), and grid rule `canvas { position:fixed;inset:0;width:100%;height:100% }`.
4. **Interactive Detail & Feature Matrix (<article.mui-card:nth(2)> — `Claude Monet died at Giverny on 5 `)**:
   - Landmark `<article class="mui-card">` framing `Claude Monet died at Giverny on 5 December 1926.` and `This experience needs JavaScript and WebGL.` (*"This experience needs JavaScript and WebGL."*) with `#141006` surface cards, `#fbf3c6` accents, and `journey { height:2000vh;pointer-events:none }`.
5. **Colophon & Global Directory Footer (<footer.mui> — `https://100yearsmonet.com`)**:
   - Landmark `<footer class="mui">` anchoring `Monet 100 — A century without Cl` footer links (`Musée de l’Orangerie · Musée d’Orsay · The Met · MFA Boston · Museum Barberini`), copy *"Claude Monet 1926 — 2026"*, and `#8c8c8c` structural dividers.
