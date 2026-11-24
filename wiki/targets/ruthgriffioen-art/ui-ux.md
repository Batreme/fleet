---
title: "UI & UX Architecture: ruthgriffioen-art"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: ruthgriffioen-art

## Overview & Design Identity
- **Target**: `ruthgriffioen-art` (**Ruth Griffioen – Colourful paintings & art prints**)
- **Production URL**: [https://ruthgriffioen.art/](https://ruthgriffioen.art/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×872px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#c42000`)
- **Summary**: Discover colourful paintings by Dutch artist Ruth Griffioen, from portraits of women to still lifes and landscapes. Art prints coming Jan...
- **Total Clean CSS Variables Extracted**: `62` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Playfair Display`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 160px`, `line-height: 0px`, `font-weight: 400`, `letter-spacing: -4.8px`); CSS variables `--font-display: "Playfair Display", Georgia, "Times New Roman", serif`; rule `h1` (`font-size: var(--step-7)`, `line-height: .95`, `letter-spacing: -.03em`, `font-weight: 400`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 19.2px`, `line-height: 29.76px`, `font-weight: 700`); rule `h2` (`font-size: var(--step-2)`, `font-weight: 400`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24.8px`, `font-weight: 400`); CSS variables `--font-body: "Inter", system-ui, -apple-system, "Segoe UI", sans-serif`; rule `p` (`font-size: var(--step--1)`, `letter-spacing: .3em`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24.8px`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#111111` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f2f4f5` | `to { background-color: #f2f4f5 }` |
| **Interactive Accent / Highlight** | `#c42000` | `var(--highlight-strong)` in `:root` |
| **Secondary / Muted Copy** | `#6f6f6f` | `var(--muted)` in `:root` |
| **Structural Hairline Border** | `#e2e2e2` | `var(--line)` in `:root` (`rgba(17, 17, 17, .12)`) |
| **Variable Token (`--soft`)** | `#f8f1eb` | `var(--soft)` in `:root` |
| **Variable Token (`--accent`)** | `#4d1224` | `var(--accent)` in `:root` |
| **Variable Token (`--accent-light`)** | `#c77b8c` | `var(--accent-light)` in `:root` |
| **Variable Token (`--highlight`)** | `#f55a3a` | `var(--highlight)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ink` | `#111111` | Typography Ink Token |
| `--paper` | `#ffffff` | Canvas / Surface Token |
| `--muted` | `#6f6f6f` | Color / Atmospheric Token |
| `--line` | `rgba(17, 17, 17, .12)` | Color / Atmospheric Token |
| `--soft` | `#f8f1eb` | Color / Atmospheric Token |
| `--accent` | `#4d1224` | Brand / Palette Token |
| `--accent-ink` | `#ffffff` | Typography Ink Token |
| `--accent-light` | `#c77b8c` | Canvas / Surface Token |
| `--highlight` | `#f55a3a` | Canvas / Surface Token |
| `--highlight-strong` | `#c42000` | Canvas / Surface Token |
| `--font-display` | `"Playfair Display", Georgia, "Times New Roman", serif` | Typography / Scale Token |
| `--font-body` | `"Inter", system-ui, -apple-system, "Segoe UI", sans-serif` | Typography / Scale Token |
| `--step--2` | `.6875rem` | Dimension / Scale Token |
| `--step--1` | `.8125rem` | Dimension / Scale Token |
| `--step-0` | `1rem` | Dimension / Scale Token |
| `--step-1` | `clamp(1.125rem, 1.042rem + .3704vw, 1.375rem)` | Dimension / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-header> — `ruthgriffioen-art`)**:
   - Landmark `<header class="site-header">` (`1440x84px`) hosting `Ruth Griffioen – Colourful paintings` navigation (`Home H o m e · Work W o r k · About A b o u t`), DOM attributes (`data-cookie-preferences-ready="true"`, `data-source-attribution="shopify.exit_intersti..."`, `data-shop-id="109163413834"`, `data-venmo-supported="false"`), and stylesheet rule `font-face { font-family:Inter;font-style:normal;font-weight:400 500;font-display:swa... }`.
2. **Hero Stage & Focal Lead (<section.shopify-pc__banner__dialog> — `Ruth Griffioen`)**:
   - Landmark `<section class="shopify-pc__banner__dialog">` presenting display lead `Ruth Griffioen` and copy excerpt *"PAINTINGS — THE NETHERLANDS"* over `#ffffff` canvas and `#111111` ink.
3. **Primary Showcase & Content Grid (<section.artwall> — `PAINTINGS — THE NETHERLANDS`)**:
   - Landmark `<section class="artwall is-ready">` rendering section `PAINTINGS — THE NETHERLANDS` with copy *"Contemplating · Coming soon"*, asset references (`favicon.svg`, `favicon-32.png`, `apple-touch-icon.png`, `playfair-display.woff2`), and grid rule `root { --header-h: 4.5rem }`.
4. **Interactive Detail & Feature Matrix (<section.is-ready> — `Contemplating · Coming soon`)**:
   - Landmark `<section class="artwall is-ready">` framing `Contemplating · Coming soon` and `From Holland with love · Coming soon` (*"From Holland with love · Coming soon"*) with `#f2f4f5` surface cards, `#c42000` accents, and `after { box-sizing:border-box }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://ruthgriffioen.art/`)**:
   - Landmark `<footer class="site-footer site-footer--overlay">` anchoring `Ruth Griffioen – Colourful paint` footer links (`Home H o m e · Work W o r k · About A b o u t`), copy *"Her Sunday Best · Coming soon"*, and `#e2e2e2` structural dividers.
