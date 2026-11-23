---
title: "UI & UX Architecture: 360lexingtonave-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: 360lexingtonave-com

## Overview & Design Identity
- **Target**: `360lexingtonave-com` (**360 Lexington Avenue**)
- **Production URL**: [https://360lexingtonave.com](https://360lexingtonave.com)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#0000ee` accent)
- **Summary**: Located at 40th Street and Lexington Avenue, just a two-minute walk from Grand Central Terminal.
- **Total Clean CSS Variables Extracted**: `36` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Instrument Sans`
- **Body Font Stack**: `Instrument Sans Placeholder`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `h1` (`font-size: 110px`, `line-height: 100%`, `letter-spacing: -.03em`, `font-weight: 400`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 74px`, `line-height: 74px`, `font-weight: 400`, `letter-spacing: -2.22px`); rule `h2` (`font-size: 74px`, `line-height: 100%`, `letter-spacing: -.03em`, `font-weight: 400`)
- **Body Copy**: live computed `body` (`font-size: 12px`, `line-height: normal`, `font-weight: 400`); rule `p` (`font-size: 12px`, `line-height: 116%`, `letter-spacing: -.03em`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 12px`, `line-height: normal`, `font-weight: 400`); CSS variables `--letter-spacing: var(--framer-letter-spacing)`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `body` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f5f5f5` | `.framer-jJ6Uj .framer-oq6atu { background-color: #f5f5f5 }` |
| **Interactive Accent / Highlight** | `#0000ee` | live computed `a` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#111213` | live computed `h2` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#111213` | hairline divider derived from live computed `h2` `color` (`computed_styles.json`) |
| **Variable Token (`--token-fcb71b86-915a-48dc-848f-900a8d21781e`)** | `#fff6` | `var(--token-fcb71b86-915a-48dc-848f-900a8d21781e)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--token-c796e2cf-d257-4b33-b047-54ba873a0aa1` | `#111213` | Color / Atmospheric Token |
| `--token-12fc5a7c-f912-48c9-8238-1c64b516e639` | `#fff` | Color / Atmospheric Token |
| `--token-fcb71b86-915a-48dc-848f-900a8d21781e` | `#fff6` | Color / Atmospheric Token |
| `--token-1e846e4d-2af5-4cab-b763-361cb3703674` | `#ffffff29` | Color / Atmospheric Token |
| `--token-fedfb1b7-b3b3-4fcd-a5c5-e2a1955b044e` | `#11121366` | Color / Atmospheric Token |
| `--token-6ac23283-84f0-4aba-8ffe-b86657dd600d` | `#1112130a` | Color / Atmospheric Token |
| `--text-decoration-skip-ink` | `var(--framer-text-decoration-skip-ink)` | Typography Ink Token |
| `--text-underline-offset` | `var(--framer-text-decoration-offset)` | Typography Ink Token |
| `--font-family` | `var(--framer-font-family)` | Typography / Scale Token |
| `--font-style` | `var(--framer-font-style)` | Typography / Scale Token |
| `--font-weight` | `var(--framer-font-weight)` | Typography / Scale Token |
| `--text-color` | `var(--framer-text-color)` | Typography Ink Token |
| `--letter-spacing` | `var(--framer-letter-spacing)` | Typography / Scale Token |
| `--font-size` | `var(--framer-font-size)` | Typography / Scale Token |
| `--text-transform` | `var(--framer-text-transform)` | Typography Ink Token |
| `--line-height` | `var(--framer-line-height)` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.lenis> — `360lexingtonave-com`)**:
   - Landmark `<header class="lenis">` (`1440px`) hosting `360 Lexington Avenue` navigation (`Available Offices · Prime Corner Retail · Contact Us · Explore Retail · Explore Offices`), DOM attributes (`data-framer-font-css`, `data-framer-breakpoint-css`, `data-framer-css-ssr-minified`, `data-framer-components="framer-lib-cursors-ho..."`), and stylesheet rule `.hidden-72rtr7 { display:none!important }`.
2. **Hero Stage & Focal Lead (<div.lenis-smooth> — `Built For Difference Makers`)**:
   - Landmark `<div class="lenis-smooth">` presenting display lead `Built For Difference Makers` and copy excerpt *"Prime Corner Retail"* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<div.framer-jJ6Uj> — `360 Lex has been thoroughly reimag`)**:
   - Landmark `<div class="framer-jJ6Uj">` rendering section `360 Lex has been thoroughly reimagined with a new...` with copy *"Located at 40th Street and Lexington Avenue:"*, asset references (`Grxz4pBrnDA6VjRjN6h8ucts0.png`, `oehMxFzuMfSIeZHPUFXOF3LFOiM.png`, `factors.js`, `fonts.gstatic.com`), and grid rule `.hidden-xwkejd { display:none!important }`.
4. **Interactive Detail & Feature Matrix (<div.framer-DOsz9> — `2-Minute Walk to Grand Central`)**:
   - Landmark `<div class="framer-DOsz9">` framing `2-Minute Walk to Grand Central` and `Surrounded By Dining & Entertainment` (*"just a two-minute walk from Grand Central Terminal."*) with `#f5f5f5` surface cards, `#0000ee` accents, and `.hidden-l5vpik { display:none!important }`.
5. **Colophon & Global Directory Footer (<footer.framer-Kw8IE> — `https://360lexingtonave.com`)**:
   - Landmark `<footer class="framer-Kw8IE">` anchoring `360 Lexington Avenue` footer links (`Available Offices · Prime Corner Retail · Contact Us · Explore Retail · Explore Offices`), copy *"Located at 40th and Lexington Avenue, just a two-minute walk"*, and `#111213` structural dividers.
