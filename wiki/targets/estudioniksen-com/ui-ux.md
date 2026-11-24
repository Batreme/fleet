---
title: "UI & UX Architecture: estudioniksen-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: estudioniksen-com

## Overview & Design Identity
- **Target**: `estudioniksen-com` (**Estudio Niksen**)
- **Production URL**: [https://estudioniksen.com/](https://estudioniksen.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#2e5fdc` accent)
- **Summary**: We are an independent lifestyle brand presenting elevated garments and living-space goods through a mix of influences.
- **Total Clean CSS Variables Extracted**: `633` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `PP Neue Montreal`
- **Body Font Stack**: `PP Neue Montreal`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 42px`, `line-height: 42px`, `font-weight: 400`, `letter-spacing: -1.47px`); CSS variables `--x-shell-disclosure-display: block`, `--x-shell-order-summary-display: none`, `--x-shell-content-display: grid`; rule `h1` (`font-size: var(--x-heading-level1-font-s...`, `line-height: var(--x-typography-li...`, `letter-spacing: var(--x-heading-level...`, `font-weight: var(--x-headi...`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 42px`, `line-height: 42px`, `font-weight: 400`, `letter-spacing: -1.47px`); CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`; rule `h2` (`font-size: var(--x-heading-level2-font-s...`, `line-height: var(--x-typography-li...`, `letter-spacing: var(--x-heading-level...`, `font-weight: var(--x-headi...`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`; rule `p` (`font-size: var(--text-xxs)`, `line-height: 1.1`, `font-weight: var(--font-we...`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-xs: 12px`, `--text-xs--line-height: calc(1 / .75)`, `--default-mono-font-family: var(--font-mono)`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f2f3f5` | `.O9AXs { background-color: #f2f3f5 }` |
| **Interactive Accent / Highlight** | `#2e5fdc` | `.grow_modal__btn-primary { background-color: #2e5fdc }` |
| **Secondary / Muted Copy** | `#4f4f4f` | `var(--pswp-icon-color-secondary)` in `:root` |
| **Structural Hairline Border** | `#4f4f4f` | `var(--pswp-icon-stroke-color)` in `:root` |
| **Variable Token (`--pswp-placeholder-bg`)** | `#222222` | `var(--pswp-placeholder-bg)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--svh` | `1svh` | Layout / Spatial Grid Token |
| `--unit-sm` | `10px` | Dimension / Scale Token |
| `--unit-md` | `20px` | Dimension / Scale Token |
| `--grid-gutter` | `var(--spacing-gutter)` | Layout / Spatial Grid Token |
| `--grid-margin` | `var(--unit-sm)` | Layout / Spatial Grid Token |
| `--header-height` | `calc(var(--spacing) * 8.5)` | Layout / Spatial Grid Token |
| `--announcement-banner-height` | `calc(var(--spacing) * 15)` | Layout / Spatial Grid Token |
| `--pswp-bg` | `#000` | Canvas / Surface Token |
| `--pswp-placeholder-bg` | `#222` | Canvas / Surface Token |
| `--pswp-root-z-index` | `100000` | Elevation / Border Token |
| `--pswp-preloader-color` | `#4f4f4f66` | Brand / Palette Token |
| `--pswp-preloader-color-secondary` | `#ffffffe6` | Brand / Palette Token |
| `--pswp-icon-color` | `#fff` | Brand / Palette Token |
| `--pswp-icon-color-secondary` | `#4f4f4f` | Brand / Palette Token |
| `--pswp-icon-stroke-color` | `#4f4f4f` | Brand / Palette Token |
| `--pswp-icon-stroke-width` | `2px` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.c-header_inner> — `estudioniksen-com`)**:
   - Landmark `<header class="c-header_inner">` (`1440x900px`) hosting `Estudio Niksen` navigation (`Shop All · Outerwear · All Outerwear · Coats · Jackets`), DOM attributes (`data-template="index"`, `data-smooth-scrolling="true"`, `data-scroll-orientation="vertical"`, `data-source-attribution="shopify.exit_intersti..."`), and stylesheet rule `html.lenis body { height:auto }`.
2. **Hero Stage & Focal Lead (<section.shopify-pc__banner__dialog> — `Fall Winter '26`)**:
   - Landmark `<section class="shopify-pc__banner__dialog">` presenting display lead `Fall Winter '26` and copy excerpt *"All prices include duties and taxes. No surprises at delivery."* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.shopify-pc__banner__dialog:nth(2)> — `New arrivals`)**:
   - Landmark `<section class="shopify-pc__banner__dialog">` rendering section `New arrivals` with copy *"Shop all new arrivals"*, asset references (`1437315943278764`, `fbevents.js`, `a2f45e7b43c941fd84b3f91a8.js`, `favicon.svg`), and grid rule `.lenis-stopped { overflow:clip }`.
4. **Interactive Detail & Feature Matrix (<section.shopify-pc__banner__dialog:nth(3)> — `Shop the Look`)**:
   - Landmark `<section class="shopify-pc__banner__dialog">` framing `Shop the Look` and `Niksen Projects` (*"View Product : Wool Pocket Coat"*) with `#f2f3f5` surface cards, `#2e5fdc` accents, and `.lenis.lenis-smooth iframe { pointer-events:none }`.
5. **Colophon & Global Directory Footer (<footer.mt-fluid-3xl> — `https://estudioniksen.com/`)**:
   - Landmark `<footer class="mt-fluid-3xl pb-gutter">` anchoring `Estudio Niksen` footer links (`Shop All · Outerwear · All Outerwear · Coats · Jackets`), copy *"View Product : Boxy Wool Jacket"*, and `#4f4f4f` structural dividers.
