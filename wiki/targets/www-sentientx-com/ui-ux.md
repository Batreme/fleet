---
title: "UI & UX Architecture: www-sentientx-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-sentientx-com

## Overview & Design Identity
- **Target**: `www-sentientx-com` (**SentientX · Enterprise AI & Digital Likeness Protection**)
- **Production URL**: [https://www.sentientx.com](https://www.sentientx.com)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#141414`)
- **Summary**: SentientX is an AI operating partner for consumer products and retail. Production-grade AI across supply chain, finance, and operations....
- **Total Clean CSS Variables Extracted**: `316` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `wfont_0c99ee_2751996ff9224fc486a0c6fe16...`
- **Body Font Stack**: `wf_2751996ff9224fc486a0c6fe1`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 60px`, `line-height: 66px`, `font-weight: 400`, `letter-spacing: -1.8px`); CSS variables `--display: inline-block`, `--comp-display: unset`, `--container-display: grid`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 45px`, `line-height: 49.5px`, `font-weight: 400`, `letter-spacing: -1.35px`); CSS variables `--wst-font-style-h2: var(--font_2)`, `--item-depth2-direction: inherit`, `--item-depth2-align: inherit`; rule `h2` (`font-size: 16px`, `line-height: 1.05`, `font-weight: 400`)
- **Body Copy**: live computed `body` (`font-size: 10px`, `line-height: normal`, `font-weight: 400`); CSS variables `--wst-font-style-body-large: var(--font_7)`, `--wst-font-style-body-medium: var(--font_8)`, `--wst-font-style-body-small: var(--font_9)`; rule `p` (`font-size: 13px`, `line-height: 1.4`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 10px`, `line-height: normal`, `font-weight: 400`); CSS variables `--wst-font-style-body-small: var(--font_9)`, `--wst-font-style-body-x-small: var(--font_10)`, `--label-align: center`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `browser-default` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#dbfac4` | `.sx-toggle-track:before { background: #dbfac4 }` |
| **Interactive Accent / Highlight** | `#141414` | live computed `a` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#141414` | live computed `a` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#757575` | `var(--stroke)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--one-unit` | `1vw` | Dimension / Scale Token |
| `--section-max-width` | `9999px` | Layout / Spatial Grid Token |
| `--spx-stopper-max` | `9999px` | Dimension / Scale Token |
| `--spx-stopper-min` | `0px` | Dimension / Scale Token |
| `--browser-zoom` | `1` | Design System Custom Token |
| `--wst-button-color-fill-primary` | `rgb(var(--color_48))` | Brand / Palette Token |
| `--wst-button-color-border-primary` | `rgb(var(--color_49))` | Brand / Palette Token |
| `--wst-button-color-text-primary` | `rgb(var(--color_50))` | Typography Ink Token |
| `--wst-button-color-fill-primary-hover` | `rgb(var(--color_51))` | Brand / Palette Token |
| `--wst-button-color-border-primary-hover` | `rgb(var(--color_52))` | Brand / Palette Token |
| `--wst-button-color-text-primary-hover` | `rgb(var(--color_53))` | Typography Ink Token |
| `--wst-button-color-fill-primary-disabled` | `rgb(var(--color_54))` | Brand / Palette Token |
| `--wst-button-color-border-primary-disabled` | `rgb(var(--color_55))` | Brand / Palette Token |
| `--wst-button-color-text-primary-disabled` | `rgb(var(--color_56))` | Typography Ink Token |
| `--wst-button-color-fill-secondary` | `rgb(var(--color_57))` | Brand / Palette Token |
| `--wst-button-color-border-secondary` | `rgb(var(--color_58))` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.comp-mqurid64> — `www-sentientx-com`)**:
   - Landmark `<header class="comp-mqurid64 S829f_">` (`1440x140px`) hosting `SentientX · Enterprise AI & Digital ` navigation (`Home`), DOM attributes (`data-url="https://static.parast..."`, `data-url="https://static.parast..."`, `data-url="https://static.parast..."`, `data-url="https://static.parast..."`), and stylesheet rule `root:active-view-transition { view-transition-name:none }`.
2. **Hero Stage & Focal Lead (<section.ke5pl1> — `The Autonomous Enterprise`)**:
   - Landmark `<section class="ke5pl1 comp-mr0mk2kw-container">` presenting display lead `The Autonomous Enterprise` and copy excerpt *"Orchestrates execution - not a bolt-on."* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.comp-mrnlzewt-container> — `One intelligence, three layers`)**:
   - Landmark `<section class="ke5pl1 comp-mrnlzewt-container">` rendering section `One intelligence, three layers` with copy *"Reinvents and runs the corporation."*, asset references (`0b6ff1_2de67bd90d924a449a9260fe7d...`, `cc.js`, `minified.js`, `focus-within-polyfill.js`), and grid rule `root::view-transition { pointer-events:none }`.
4. **Interactive Detail & Feature Matrix (<section.comp-mqqmgqfu-container> — `A new institutional layer for huma`)**:
   - Landmark `<section class="ke5pl1 comp-mqqmgqfu-container">` framing `A new institutional layer for human identity.` and `Monitor, protect, control and enforce.` (*"Protects human identity while extending humanity into the univers"*) with `#dbfac4` surface cards, `#141414` accents, and `SITE_HEADER { view-transition-name:header-group }`.
5. **Colophon & Global Directory Footer (<footer.comp-kbgakxmn> — `https://www.sentientx.com`)**:
   - Landmark `<footer class="comp-kbgakxmn S829f_">` anchoring `SentientX · Enterprise AI & Digi` footer links (`Home`), copy *"A new institutional layer for human identity."*, and `#757575` structural dividers.
