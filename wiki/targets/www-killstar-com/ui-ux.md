---
title: "UI & UX Architecture: www-killstar-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-killstar-com

## Overview & Design Identity
- **Target**: `www-killstar-com` (**KILLSTAR**)
- **Production URL**: [https://www.killstar.com/](https://www.killstar.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×4140px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#f5f5f5` canvas, `#111111` ink, `#f1c40f` accent)
- **Summary**: Clothing & Lifestyle company with a twist of darkness, channeling emotional power and raw energy into every thread.
- **Total Clean CSS Variables Extracted**: `224` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Inter`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--atlas-font-size-display: 40px`, `--atlas-line-height-display: 52px`, `--atlas-margin-display: 24px`; rule `.title` (`font-size: 13px`)
- **Section Heading (`H2`)**: CSS variables `--atlas-font-size-h2: 32px`, `--atlas-line-height-h2: 40px`, `--atlas-margin-h2: 24px`; rule `h2` (`font-size: 2.5em`, `font-weight: 900`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 20px`, `font-weight: 400`); rule `p` (`line-height: 1.6`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 20px`, `font-weight: 400`); CSS variables `--atlas-font-size-small: 14px`, `--atlas-line-height-small: 20px`, `--atlas-margin-small: 8px`; rule `.label` (`font-size: .875em`, `letter-spacing: 2.8px`, `font-weight: 500`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f5f5f5` | live computed `main` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#111111` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#faf9f8` | `var(--atlas-background-main)` in `:root` |
| **Interactive Accent / Highlight** | `#f1c40f` | `rm-box .jconfirm-buttons button... { background-color: #f1c40f }` |
| **Secondary / Muted Copy** | `#747576` | `var(--atlas-text-placeholder)` in `:root` |
| **Structural Hairline Border** | `#41a1e6` | `var(--atlas-border-focus)` in `:root` |
| **Variable Token (`--color-white`)** | `#dcdcd0` | `var(--color-white)` in `:root` |
| **Variable Token (`--color-stone`)** | `#b3ada1` | `var(--color-stone)` in `:root` |
| **Variable Token (`--color-shadow`)** | `#232323` | `var(--color-shadow)` in `:root` |
| **Variable Token (`--color-midnight-light`)** | `#3b3838` | `var(--color-midnight-light)` in `:root` |
| **Variable Token (`--color-bone`)** | `#ebebeb` | `var(--color-bone)` in `:root` |
| **Variable Token (`--color-bone-dark`)** | `#d4d4d4` | `var(--color-bone-dark)` in `:root` |
| **Variable Token (`--color-success`)** | `#32c079` | `var(--color-success)` in `:root` |
| **Variable Token (`--color-failure`)** | `#8b0910` | `var(--color-failure)` in `:root` |
| **Variable Token (`--color-warning`)** | `#ffaa33` | `var(--color-warning)` in `:root` |
| **Variable Token (`--atlas-background-content`)** | `#ffffff` | `var(--atlas-background-content)` in `:root` |
| **Variable Token (`--atlas-background-success`)** | `#518b22` | `var(--atlas-background-success)` in `:root` |
| **Variable Token (`--atlas-background-error`)** | `#be2119` | `var(--atlas-background-error)` in `:root` |
| **Variable Token (`--atlas-text-primary`)** | `#1d1e20` | `var(--atlas-text-primary)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-white` | `#DCDCD0` | Canvas / Surface Token |
| `--color-stone` | `#B3ADA1` | Brand / Palette Token |
| `--color-midnight` | `#111` | Brand / Palette Token |
| `--color-shadow` | `#232323` | Brand / Palette Token |
| `--color-midnight-light` | `#3B3838` | Canvas / Surface Token |
| `--color-bone-light` | `#f5f5f5` | Canvas / Surface Token |
| `--color-bone` | `#ebebeb` | Brand / Palette Token |
| `--color-bone-dark` | `#d4d4d4` | Canvas / Surface Token |
| `--color-success` | `#32C079` | Brand / Palette Token |
| `--color-failure` | `#8b0910` | Brand / Palette Token |
| `--color-warning` | `#FFAA33` | Brand / Palette Token |
| `--atlas-background-main` | `#faf9f8` | Canvas / Surface Token |
| `--atlas-background-content` | `#ffffff` | Canvas / Surface Token |
| `--atlas-background-success` | `#518b22` | Canvas / Surface Token |
| `--atlas-background-error` | `#be2119` | Canvas / Surface Token |
| `--atlas-text-primary` | `#1d1e20` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.shopify-section> — `www-killstar-com`)**:
   - Landmark `<header class="shopify-section shopify-section-group-header-group">` (`1440x71px`) hosting `KILLSTAR` navigation (`NEW IN · DRESSES · WOMENS · PLUS · MENS`), DOM attributes (`data-source-attribution="shopify.exit_intersti..."`, `data-shop-id="53907226789"`, `data-venmo-supported="false"`, `data-environment="production"`), and stylesheet rule `button { box-sizing:border-box;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.shopify-section> — `Dark Haven Coat`)**:
   - Landmark `<section class="shopify-section section-full-width-media">` presenting display lead `Dark Haven Coat` and copy excerpt *"We use cookies & other technologies to provide a personalised exp"* over `#f5f5f5` canvas and `#111111` ink.
3. **Primary Showcase & Content Grid (<section.section-model-image-blocks> — `Nocturnal Sequin Maxi Dress`)**:
   - Landmark `<section class="shopify-section section-model-image-blocks">` rendering section `Nocturnal Sequin Maxi Dress` with copy *"Please select a Size"*, asset references (`reamaze-push.js`, `tp.min.js`, `37086_1783060609.js`, `init.js`), and grid rule `section { display:block }`.
4. **Interactive Detail & Feature Matrix (<section.section-full-width-media> — `Spiderella Knitted Sweater`)**:
   - Landmark `<section class="shopify-section section-full-width-media">` framing `Spiderella Knitted Sweater` and `MIST OF DAWN COAT` (*"Please select a Colour"*) with `#faf9f8` surface cards, `#f1c40f` accents, and `table { border-collapse:collapse;border-spacing:0 }`.
5. **Colophon & Global Directory Footer (<footer.shopify-section> — `https://www.killstar.com/`)**:
   - Landmark `<footer class="shopify-section shopify-section-group-footer-group">` anchoring `KILLSTAR` footer links (`NEW IN · DRESSES · WOMENS · PLUS · MENS`), copy *"70% Polyurethane 22% Viscose 4% Polyester 2% Cotton 2% Metal"*, and `#41a1e6` structural dividers.
