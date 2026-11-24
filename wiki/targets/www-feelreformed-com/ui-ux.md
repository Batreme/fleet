---
title: "UI & UX Architecture: www-feelreformed-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-feelreformed-com

## Overview & Design Identity
- **Target**: `www-feelreformed-com` (**Reformed: The biggest thing to happen to Coffee since Coffee.**)
- **Production URL**: [https://www.feelreformed.com/](https://www.feelreformed.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×4968px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#f9f8f6` canvas, `#000000` ink, `#ff0000` accent)
- **Summary**: Reformed: Arabica coffee and ceremonial matcha, enriched with functionality: collagen or creatine, adaptogens and twenty-one vitamins.
- **Total Clean CSS Variables Extracted**: `1258` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Optima`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 24px`, `line-height: 27.6px`, `font-weight: 400`); CSS variables `--header-logo-display: none`, `--header-logo-inverse-display: block`, `--text-4xl: calc(var(--base-font-size)*2.25)`; rule `h1` (`line-height: var(--line-height--di...`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 48px`, `line-height: 52.8px`, `font-weight: 400`); CSS variables `--text-2xl: calc(var(--base-font-size)*1.5)`, `--text-2xl--line-height: calc(2/1.5)`, `--font-h2--spacing: 0.25em`; rule `h2` (`font-size: 24px`)
- **Body Copy**: live computed `body` (`font-size: 14px`, `line-height: 22.4px`, `font-weight: 400`); CSS variables `--font-paragraph--line-height: 1`, `--text-base: calc(var(--base-font-size))`, `--text-base--line-height: calc(1.5/1)`; rule `p` (`line-height: var(--line-height--bo...`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 14px`, `line-height: 22.4px`, `font-weight: 400`); CSS variables `--section-height-small: 15rem`, `--oke-text-small: 14px`, `--checkbox-label-padding: 8px`; rule `small` (`font-size: 80%`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f9f8f6` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `a` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#e5e5eb` | `var(--oke-avatar-backgroundColor)` in `:root` |
| **Interactive Accent / Highlight** | `#ff0000` | `.octane-popup__optin-channel-error { color: red }` (`#ff0000`) |
| **Secondary / Muted Copy** | `#7b6f65` | `var(--oke-stars-foregroundColor)` in `:root` |
| **Structural Hairline Border** | `#b3b3b1` | `var(--color-border)` in `:root` (`rgb(0 0 0 / 0.28)`) |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--hover-lift-amount` | `4px` | Dimension / Scale Token |
| `--hover-scale-amount` | `1` | Design System Custom Token |
| `--hover-subtle-zoom-amount` | `1.015` | Design System Custom Token |
| `--hover-shadow-color` | `var(--color-shadow)` | Brand / Palette Token |
| `--hover-transition-duration` | `.25s` | Motion / Easing Token |
| `--hover-transition-timing` | `ease-out` | Motion / Easing Token |
| `--sidebar-width` | `25rem` | Layout / Spatial Grid Token |
| `--narrow-content-width` | `36rem` | Layout / Spatial Grid Token |
| `--normal-content-width` | `42rem` | Layout / Spatial Grid Token |
| `--wide-content-width` | `46rem` | Layout / Spatial Grid Token |
| `--narrow-page-width` | `90rem` | Layout / Spatial Grid Token |
| `--normal-page-width` | `120rem` | Layout / Spatial Grid Token |
| `--wide-page-width` | `150rem` | Layout / Spatial Grid Token |
| `--section-height-small` | `15rem` | Layout / Spatial Grid Token |
| `--section-height-medium` | `25rem` | Layout / Spatial Grid Token |
| `--section-height-large` | `35rem` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.shopify-section> — `www-feelreformed-com`)**:
   - Landmark `<header class="shopify-section shopify-section-group-header-group">` (`1440x0px`) hosting `Reformed: The biggest thing to happe` navigation (`Black Coffee · Mocha · Matcha · Shop All · Mocha with Collagen`), DOM attributes (`data-source-attribution="shopify.exit_intersti..."`, `data-shopify`, `data-shop-id="81515184414"`, `data-venmo-supported="false"`), and stylesheet rule `svg { display:block;max-width:100% }`.
2. **Hero Stage & Focal Lead (<section.shopify-section> — `Black Coffee with Collagen`)**:
   - Landmark `<section class="shopify-section section-wrapper">` presenting display lead `Black Coffee with Collagen` and copy excerpt *"Our lowest prices of the year."* over `#f9f8f6` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.hero-wrapper> — `Matcha with Collagen`)**:
   - Landmark `<section class="shopify-section hero-wrapper">` rendering section `Matcha with Collagen` with copy *"Experience the next era of Coffee & Matcha"*, asset references (`storefront.js`, `page-load`, `shopify.js`, `klaviyo.js`), and grid rule `img { width:100%;height:auto }`.
4. **Interactive Detail & Feature Matrix (<section.section-wrapper> — `Mocha with Collagen`)**:
   - Landmark `<section class="shopify-section hero-wrapper">` framing `Mocha with Collagen` and `FAQ` (*"Made in the United Kingdom"*) with `#e5e5eb` surface cards, `#ff0000` accents, and `select { font:inherit;border-radius:var(--style-border-radius-inputs) }`.
5. **Colophon & Global Directory Footer (<footer.shopify-section> — `https://www.feelreformed.com/`)**:
   - Landmark `<footer class="shopify-section shopify-section-group-footer-group">` anchoring `Reformed: The biggest thing to h` footer links (`Black Coffee · Mocha · Matcha · Shop All · Mocha with Collagen`), copy *"Reformed blends the finest coffee beans or ceremonial-grade "*, and `#b3b3b1` structural dividers.
