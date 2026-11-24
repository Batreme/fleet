---
title: "UI & UX Architecture: johnhardy-com_collections-billie-eilish-and-finneas"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: johnhardy-com_collections-billie-eilish-and-finneas

## Overview & Design Identity
- **Target**: `johnhardy-com_collections-billie-eilish-and-finneas` (**Billie Eilish and FINNEAS – John Hardy**)
- **Production URL**: [https://johnhardy.com/collections/billie-eilish-and-finneas](https://johnhardy.com/collections/billie-eilish-and-finneas)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#ff5c1d`)
- **Summary**: John Hardy fine luxury jewelry. Made in Bali since 1975. Enjoy complimentary shipping and returns on all orders. Bracelets, Rings, Neckla...
- **Total Clean CSS Variables Extracted**: `966` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `General Sans`
- **Body Font Stack**: `General Sans`
- **Monospace / Technical Font Stack**: `Source Code Pro`
- **Hero Display (`H1`)**: CSS variables `--x-shell-disclosure-display: block`, `--x-shell-order-summary-display: none`, `--x-shell-content-display: grid`; rule `h1` (`font-size: 1.5rem`, `line-height: 1.2`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 32px`, `line-height: 48px`, `font-weight: 500`, `letter-spacing: 0.5px`); rule `h2` (`font-size: var(--hero-title-size-mobile,...`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`, `letter-spacing: 0.5px`); CSS variables `--bonsai-font-body: var(--font-family-general-sans)`, `--bonsai-agent-body-bold-weight: 550`; rule `,p` (`font-size: var(--font-size-3)`, `line-height: var(--line-height-0)`, `letter-spacing: var(--letter-spacing-0)`, `font-weight: var(--font-we...`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`, `letter-spacing: 0.5px`); CSS variables `--letter-spacing-0: 0.5px`, `--letter-spacing-1: 1px`, `--letter-spacing-2: 1px`; rule `small` (`font-size: calc(var(--kl-reviews-reviews...`, `font-weight: var(--kl-revi...`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#e5e5e5` | `var(--rb-smart-collections-reviews-background-color)` in `:root` |
| **Interactive Accent / Highlight** | `#ff5c1d` | `var(--color-brand-orange)` in `:root` |
| **Secondary / Muted Copy** | `#757575` | `var(--bonsai-agent-price-fg)` in `:root` |
| **Structural Hairline Border** | `#cccccc` | `var(--rb-widget-input-border-color)` in `:root` |
| **Variable Token (`--color-neutral-charcoal`)** | `#33383c` | `var(--color-neutral-charcoal)` in `:root` |
| **Variable Token (`--color-neutral-dark-grey`)** | `#646464` | `var(--color-neutral-dark-grey)` in `:root` |
| **Variable Token (`--color-neutral-light-grey`)** | `#e6e6e6` | `var(--color-neutral-light-grey)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--breakpoint-xs` | `0` | Design System Custom Token |
| `--breakpoint-s` | `36rem` | Dimension / Scale Token |
| `--breakpoint-m` | `48rem` | Dimension / Scale Token |
| `--breakpoint-l` | `64rem` | Dimension / Scale Token |
| `--breakpoint-xl` | `90rem` | Dimension / Scale Token |
| `--breakpoint-2xl` | `120rem` | Dimension / Scale Token |
| `--color-brand-black` | `#000` | Canvas / Surface Token |
| `--color-brand-orange` | `#ff5c1d` | Brand / Palette Token |
| `--color-neutral-black` | `#000` | Canvas / Surface Token |
| `--color-neutral-charcoal` | `#33383c` | Brand / Palette Token |
| `--color-neutral-dark-grey` | `#646464` | Canvas / Surface Token |
| `--color-neutral-light-grey` | `#e6e6e6` | Canvas / Surface Token |
| `--color-neutral-medium-grey` | `grey` | Brand / Palette Token |
| `--color-neutral-white` | `#fff` | Canvas / Surface Token |
| `--color-overlay` | `rgba(0,0,0,.3)` | Brand / Palette Token |
| `--color-overlay-background-overlay` | `rgba(0,0,0,.3)` | Canvas / Surface Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-header> — `johnhardy-com_collections-billie-eilish-and-finneas`)**:
   - Landmark `<header class="site-header">` (`1440x87px`) hosting `Billie Eilish and FINNEAS – John Har` navigation (`Wishlist · Featured · New Arrivals · Best Sellers · Holiday Gifting`), DOM attributes (`data-source-attribution="shopify.exit_intersti..."`, `data-rapid="true"`, `data-shop-id="72737456428"`, `data-venmo-supported="true"`), and stylesheet rule `.shopify-payment-button__button--... { visibility:hidden }`.
2. **Hero Stage & Focal Lead (<section.site-header-offset> — `Billie Eilish & FINNEAS`)**:
   - Landmark `<section class="site-header-offset">` presenting display lead `Billie Eilish & FINNEAS` and copy excerpt *"Hard meets soft in two distinct design languages: delicate, roman"* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.hero-banner-section> — `Two Expressions of One Creative Vi`)**:
   - Landmark `<section class="hero-banner-section">` rendering section `Two Expressions of One Creative Vision Two Expres...` with copy *"Billie Eilish & FINNEAS"*, asset references (`rebuy.js`, `loader.js`, `01HNXAYFWDBE125P1ZK44ZZ829`, `117791.ct.js`), and grid rule `opify-payment-button__button--unb... { background-color:1990c6;padding:1em 2em }`.
4. **Interactive Detail & Feature Matrix (<section.template-collection> — `“Jewelry has always been an enormo`)**:
   - Landmark `<section class="template-collection">` framing `“Jewelry has always been an enormous part of how...` and `Two years in the making` (*"Two Expressions of One Creative Vision"*) with `#e5e5e5` surface cards, `#ff5c1d` accents, and `ptions.shopify-payment-button__sk... { width:50%;margin-left:25%;margin-right:25%;border-radius:4px!important;h... }`.
5. **Colophon & Global Directory Footer (<footer.usablenet> — `https://johnhardy.com/collections/billie-eilish-and-finneas`)**:
   - Landmark `<footer class="usablenet">` anchoring `Billie Eilish and FINNEAS – John` footer links (`Wishlist · Featured · New Arrivals · Best Sellers · Holiday Gifting`), copy *"Wildflower Pendant Necklace, Sterling Silver, Lab Grown Diam"*, and `#cccccc` structural dividers.
