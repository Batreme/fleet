---
title: "UI & UX Architecture: rialto-com-au"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: rialto-com-au

## Overview & Design Identity
- **Target**: `rialto-com-au` (**Rialto · The icon of Melbourne's skyline**)
- **Production URL**: [https://rialto.com.au/](https://rialto.com.au/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#080808` canvas, `#ffffff` ink, `#004bff` accent)
- **Summary**: With the prestige of Melbourne's Collins Street address. Rialto hosts world-class amenity, dining and retail, offering unique experiences.
- **Total Clean CSS Variables Extracted**: `128` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Sharp Grotesk`
- **Body Font Stack**: `Gotham`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 200px`, `line-height: 240px`, `font-weight: 700`, `letter-spacing: 3px`); rule `,.h1` (`font-size: 20rem`, `line-height: .84`, `letter-spacing: .015em`, `font-weight: 700`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 100px`, `line-height: 84px`, `font-weight: 700`, `letter-spacing: 1.5px`); rule `,.h2` (`font-size: 10rem`, `line-height: .84`, `letter-spacing: .015em`, `font-weight: 700`)
- **Body Copy**: live computed `body` (`font-size: 24px`, `line-height: 27px`, `font-weight: 300`); CSS variables `--tile-body-opacity: 0`, `--tile-body-translate-y: 2rem`; rule `p` (`line-height: 1.2`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 14px`, `line-height: 17.0002px`, `font-weight: 300`); CSS variables `--button-letter-spacing: 0.185em`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#080808` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#004bff` | live computed `section` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#004bff` | live computed `button` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#004bff` | live computed `button` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#666666` | `#sbi_lightbox .sbi_lightbox_action { border-left: #666666 }` |
| **Variable Token (`--color-black`)** | `#000000` | `var(--color-black)` in `:root` |
| **Variable Token (`--color-gray-300`)** | `#d1d4d6` | `var(--color-gray-300)` in `:root` |
| **Variable Token (`--color-gray-700`)** | `#3d3d3b` | `var(--color-gray-700)` in `:root` |
| **Variable Token (`--color-gray-800`)** | `#231f20` | `var(--color-gray-800)` in `:root` |
| **Variable Token (`--color-pink-400`)** | `#ffc8ff` | `var(--color-pink-400)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--color-white-thin` | `rgba(255, 255, 255, 0.5)` | Canvas / Surface Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-current-thin` | `color-mix(in srgb, currentColor 50%, transparent 50%)` | Brand / Palette Token |
| `--color-current-thin-md` | `color-mix(in srgb, currentColor 75%, transparent 25%)` | Brand / Palette Token |
| `--color-gray-300` | `#d1d4d6` | Brand / Palette Token |
| `--color-gray-700` | `#3d3d3b` | Brand / Palette Token |
| `--color-gray-800` | `#231f20` | Brand / Palette Token |
| `--color-gray-900` | `#080808` | Brand / Palette Token |
| `--color-blue-700` | `#004bff` | Brand / Palette Token |
| `--color-pink-400` | `#ffc8ff` | Typography Ink Token |
| `--color-body-bg` | `#080808` | Canvas / Surface Token |
| `--color-body-color` | `#fff` | Typography Ink Token |
| `--color-accent` | `var(--color-blue-700)` | Brand / Palette Token |
| `--color-secondary` | `var(--color-gray-900)` | Brand / Palette Token |
| `--color-light` | `var(--color-white)` | Canvas / Surface Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header> — `rialto-com-au`)**:
   - Landmark `<header class="header borders">` (`1425x65px`) hosting `Rialto · The icon of Melbourne's sky` navigation (`Discover · What's On · Experience`), DOM attributes (`data-rocket-prefetch`, `data-rocket-preload`, `data-minify="1"`, `data-minify="1"`), and stylesheet rule `sb_instagram { -webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:bord... }`.
2. **Hero Stage & Focal Lead (<section.module> — `CELEBRATING 40 YEARS`)**:
   - Landmark `<section class="module module--landing_animation">` presenting display lead `CELEBRATING 40 YEARS` and copy excerpt *"Rialto is for those who embrace potential, realise goals and cont"* over `#080808` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.module--hero> — `A MELBOURNE ICON`)**:
   - Landmark `<section class="module module--hero">` rendering section `A MELBOURNE ICON` with copy *"AMBITION LIVES HERE"*, asset references (`recaptcha__en.js`, `gtm.js`, `google-analytics.com`, `ajax.googleapis.com`), and grid rule `sb_instagram:after { clear:both;content:"";display:table }`.
4. **Interactive Detail & Feature Matrix (<section.module--image_text> — `AMBITION LIVES HERE`)**:
   - Landmark `<section class="module module--image_text">` framing `AMBITION LIVES HERE` and `WHAT’S ON AT RIALTO` (*"This is a place that welcomes the driven, where we can achieve be"*) with `#004bff` surface cards, `#004bff` accents, and `sb_instagram.sbi_fixed_height { overflow:hidden;overflow-y:auto }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://rialto.com.au/`)**:
   - Landmark `<footer class="footer">` anchoring `Rialto · The icon of Melbourne's` footer links (`Discover · What's On · Experience`), copy *"WHAT’S ON AT RIALTO"*, and `#666666` structural dividers.
